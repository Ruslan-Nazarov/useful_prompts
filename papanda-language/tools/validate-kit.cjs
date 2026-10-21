#!/usr/bin/env node
// Checks the assignment, not an implemented application's behavior.
const fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const root=path.resolve(__dirname,'..');
const read=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const assert=(ok,message)=>{if(!ok)throw new Error(message);};
const hash=p=>crypto.createHash('sha256').update(fs.readFileSync(path.join(root,p))).digest('hex');
const walk=dir=>fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]);
const relative=p=>path.relative(root,p).split(path.sep).join('/');
let checks=0;
const check=(ok,message)=>{assert(ok,message);checks++;};
const documents=['README','PROMPT','SPEC','FEATURES','DATA','AI','VISUAL','ACCEPTANCE','DEPLOYMENT','DEVELOPMENT','SOURCES'];
for(const doc of documents)for(const suffix of ['', '.en'])check(fs.existsSync(path.join(root,doc+suffix+'.md')),'Missing document '+doc+suffix);
const manifest=read('reference/manifest.json');
for(const [file,digest] of Object.entries(manifest.sha256))check(hash(file)===digest,'Hash mismatch: '+file);
const allReference=walk(path.join(root,'reference')).map(relative).filter(p=>p!=='reference/manifest.json').sort();
check(JSON.stringify(allReference)===JSON.stringify(Object.keys(manifest.sha256).sort()),'Reference inventory differs from manifest');
const tokens=read('reference/design-tokens.json'),langs=tokens.languages.map(l=>l.code),labels=new Set(tokens.languages.map(l=>l.label)),roles=new Set(tokens.roles);
check(langs.length===7&&new Set(langs).size===7,'Expected seven unique practice languages');
const words=read('reference/content/words.json');
check(words.length===manifest.counts.words,'Word count');
check(new Set(words.map(w=>w.eng)).size===words.length,'Duplicate word keys');
for(const w of words){
 check(typeof w.eng==='string'&&!!w.eng.trim(),'Empty word key');
 check(w.count===0&&w.is_learned===0&&Object.keys(w.knowledge_stats).length===0&&Object.keys(w.show_stats).length===0,'Nonzero author progress');
 check(!['last_shown','last_shown_by_lang','personal_association','snoozed_until_by_lang','is_favorite'].some(k=>k in w),'Personal fields in static dictionary');
 check(langs.every(c=>typeof w.translations[c]==='string'),'Missing translation slot');
}
const sentences=read('reference/content/sentences.json');
check(sentences.length===manifest.counts.sentences,'Sentence count');
check(new Set(sentences.map(s=>s.id)).size===sentences.length,'Duplicate sentence IDs');
function sentenceShape(s){
 check(typeof s.id==='string'&&!!s.id&&labels.has(s.language)&&typeof s.sentence==='string'&&!!s.sentence.trim()&&s.words.length>0,'Invalid sentence identity');
 for(const t of s.words){
  check(typeof t.text==='string'&&!!t.text&&roles.has(t.role)&&typeof t.label==='string'&&typeof t.translation==='string','Invalid token');
  check(Array.isArray(t.parts)&&t.parts.join('')===t.text,'Parts do not match '+s.id+': '+t.text);
  check(t.clauseIndex===undefined||(Number.isSafeInteger(t.clauseIndex)&&t.clauseIndex>=0),'Invalid clause index');
  if(s.source==='seed')check(t.is_in_my_dict===false&&!t.dictionary_word,'Historical dictionary membership');
 }
 for(const hint of s.markerHints||[])check(hint.evidence.length>0&&hint.evidence.every(e=>Number.isSafeInteger(e.tokenIndex)&&s.words[e.tokenIndex]?.text.includes(e.form)),'Invalid marker evidence');
}
for(const s of sentences)sentenceShape(s);
check(tokens.languages.every(l=>sentences.some(s=>s.language===l.label)),'Offline coverage for each language');
const study=read('reference/content/study-examples.json');
for(const c of langs){check(study.chains[c].length===4,'Four development steps '+c);for(const s of study.chains[c])sentenceShape(s);}
check(study.comparison.length===7,'Seven-language comparison');
const book=read('reference/book/catalog.json');
check(book.chapters.length===manifest.counts.bookMaterials&&book.chapters.length===66,'Book material count');
check(new Set(book.chapters.map(c=>c.id)).size===book.chapters.length,'Duplicate chapter IDs');
const blockIds=new Set();
for(const c of book.chapters){
 const normalizedSource=fs.readFileSync(path.join(root,'reference',c.sourcePath),'utf8').replace(/\r\n/g,'\n');
 check(crypto.createHash('sha256').update(normalizedSource).digest('hex')===c.sourceHash,'Book source mismatch '+c.sourcePath);
 for(const b of c.blocks){check(!blockIds.has(b.id)&&!!b.id,'Duplicate block ID');blockIds.add(b.id);}
}
check(!book.languages.some(l=>l.code==='la')&&book.languages.some(l=>l.code==='ru'),'Book language boundaries');
const catalog=read('reference/feature-catalog.json');
check(catalog.features.length===96&&catalog.acceptance.length===36,'Checklist sizes');
for(const [file,items] of [['FEATURES',catalog.features],['ACCEPTANCE',catalog.acceptance]]){
 const ru=fs.readFileSync(path.join(root,file+'.md'),'utf8'),en=fs.readFileSync(path.join(root,file+'.en.md'),'utf8');
 for(const item of items)check(ru.includes(item.id)&&en.includes(item.id),'Bilingual checklist ID '+item.id);
}
const covered=new Set();
for(const a of catalog.acceptance){
 const text=a.features.replace(/F(\d{3})[–-]F(\d{3})/g,(_,lo,hi)=>Array.from({length:+hi-+lo+1},(_,i)=>'F'+String(+lo+i).padStart(3,'0')).join(','));
 for(const id of text.match(/F\d{3}/g)||[]){check(catalog.features.some(f=>f.id===id),'Unknown acceptance feature '+id);covered.add(id);}
}
check(catalog.features.every(f=>covered.has(f.id)),'A feature lacks acceptance coverage');
const f=read('reference/fixtures.json'),p=f.backup.data;
check(f.backup.app==='papanda'&&f.backup.version===1,'Fixture backup envelope');
check(p.activeLanguages.every(c=>langs.includes(c))&&p.readingTexts.length<=10,'Fixture language/text bounds');
for(const s of p.customSentences)sentenceShape(s);
for(const t of p.readingTexts){check(t.position>=0&&t.position<t.segments.length,'Fixture position');for(const [i,s] of Object.entries(t.cards))check(s.sentence===t.segments[+i]&&s.language===t.language,'Fixture reading link');}
check(Math.abs(f.cases.memoryAtClockExpected-(0.35+0.65*Math.exp(-2/81)))<1e-12,'Memory fixture');
const files=walk(root);
for(const file of files.filter(p=>p.endsWith('.md'))){
 const source=fs.readFileSync(file,'utf8').replace(/```[\s\S]*?```/g,'');
 for(const match of source.matchAll(/\]\(([^)]+)\)/g)){
  const target=match[1].replace(/^<|>$/g,'').split('#')[0];
  if(!target||/^[a-z][a-z0-9+.-]*:/i.test(target))continue;
  check(fs.existsSync(path.resolve(path.dirname(file),decodeURIComponent(target))),'Broken Markdown link '+relative(file)+': '+target);
 }
}
for(const file of files){
 const rel=relative(file);
 check(!/(^|\/)(\.env$|\.dev\.vars$|node_modules\/|\.git\/)|\.(apk|aab|jks|keystore|p12|db)$/i.test(rel),'Forbidden public file '+rel);
 if(/\.(md|json|txt|ts|toml|cjs)$/.test(file)){
  const s=fs.readFileSync(file,'utf8');
  check(!/AIza[0-9A-Za-z_-]{30,}|\bsk-[A-Za-z0-9_-]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/.test(s),'Potential secret '+rel);
 }
}
console.log(JSON.stringify({ok:true,checks,files:files.length,words:words.length,sentences:sentences.length,bookMaterials:book.chapters.length,bookBlocks:blockIds.size,features:catalog.features.length,acceptance:catalog.acceptance.length,scope:'assignment integrity only; no app/device/live AI verification'},null,2));
