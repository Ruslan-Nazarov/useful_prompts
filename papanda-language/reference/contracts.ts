/** Public reconstruction contract, no runtime dependencies. Validate untrusted data at runtime. */
export type LanguageCode = 'en'|'it'|'es'|'de'|'fr'|'kz'|'la';
export type SyntaxRole = 'Predicate'|'Subject'|'Attribute'|'Attribute_Subject'|'Object'|'Attribute_Object'|'Circumstance'|'Adverbial'|'Conjunction'|'Preposition'|'Particle'|'Article'|'Other';
export interface Word {
  eng: string; word?: string; ru?: string; meaning?: string;
  translations: Partial<Record<LanguageCode|string,string>>;
  source_language?: LanguageCode; count: number; is_learned: 0|1;
  knowledge_stats?: Record<string,boolean>; show_stats?: Record<string,number>;
  last_shown?: string; last_shown_by_lang?: Record<string,string>;
  snoozed_until_by_lang?: Record<string,string>;
  personal_association?: string; is_favorite?: boolean;
}
export interface UserWordProgress {
  count?: number; is_learned?: 0|1;
  knowledge_stats?: Record<string,boolean>; show_stats?: Record<string,number>;
  last_shown?: string; last_shown_by_lang?: Record<string,string>;
  snoozed_until_by_lang?: Record<string,string>;
  personal_association?: string; is_favorite?: boolean;
  custom_word?: string; custom_ru?: string; custom_translations?: Record<string,string>;
  ai_verification?: {status:'verified'|'flagged';checkedAt:string;issues?:{lang:string;issue:string;suggestion?:string}[]};
}
export interface Token {
  text:string; label:string; role:SyntaxRole; parts?:string[]; translation:string;
  is_in_my_dict:boolean; dictionary_word?:string|null; dictionary_form?:string;
  clauseIndex?:number; // mandatory for newly AI-annotated cards; absent in legacy seeds
}
export interface MarkerHint {
  clauseIndex:number;role:SyntaxRole;explanation:string;
  evidence:{tokenIndex:number;form:string}[];source:'authored'|'ai';
}
export interface Sentence {
  id:string;language:string;sentence:string;words:Token[];
  source?:'seed'|'manual'|'generated';createdAt?:number;
  literalTranslation?:string;learningGoal?:string;markerHints?:MarkerHint[];
  generationTaskId?:string;generationBatchId?:string;chainStep?:number;
}
export interface StructureAttempt {
  id:string;sentenceId:string;language:string;role:SyntaxRole;clauseIndex:number;
  selected:number[];expected:number[];result:'correct'|'incorrect'|'disputed';
  hintLevel:0|1|2;createdAt:string;
}
export interface ReadingText {
  id:string;title:string;language:string;segments:string[];position:number;
  cards:Record<string,Sentence>;
}
export interface WorkoutSnapshot {date:string;total:number;correct:number}
export interface ImwSnapshot {date:string;imw:number;byLang:Record<string,number>}
export interface PersistedProgress {
  structureAttempts:StructureAttempt[];readingTexts:ReadingText[];
  userWordProgress:Record<string,UserWordProgress>;
  customWords:Word[];customSentences:Sentence[];generatedSentences:Sentence[];
  activeLanguages:LanguageCode[];dailyShows:Record<string,number>;
  workoutSnapshots:WorkoutSnapshot[];imwSnapshots:ImwSnapshot[];
  wordTourSize:number;workoutWordCount:number;workoutLearnedWordCount:number;
  workoutFavoritesOnly:boolean;hasSeenSnoozeHint:boolean;
}
export interface ProgressBackup {app:'papanda';version:1;exportedAt:string;data:PersistedProgress}
export interface BookCell {markdown:string;text:string;colSpan:number;rowSpan:number;header:boolean}
export type BookBlock = {id:string;kind:'heading';text:string;level:number}|
  {id:string;kind:'text';text:string;markdown:string}|
  {id:string;kind:'table';text:string;rows:BookCell[][]};
export interface BookChapter {
  id:string;language:string;number:number;title:string;
  sourcePath:string;sourceHash:string;blocks:BookBlock[];
}
export interface BookLocation {chapterId:string;blockId?:string}
export interface BookReaderState {lastLocation?:BookLocation;bookmarks:BookLocation[];fontSize:number}
export type SentenceFocus = 'core'|'attribute'|'object'|'circumstance'|'negative'|'reading'|'question'|'complex'|'usage';
export interface SentenceTask {id:string;focus:SentenceFocus;goal:string;develops?:string}
export interface SentenceDraft {taskId:string;sentence:string}
export interface QualityVerdict {
  taskId:string;natural:boolean;translation:boolean;roles:boolean;morphology:boolean;chain:boolean;reason:string;
}
export interface GenerationConfig {
  temperature?:number;topP?:number;maxOutputTokens?:number;
  responseMimeType?:'application/json';responseJsonSchema?:Record<string,unknown>;
  thinkingConfig?:{thinkingBudget?:number;includeThoughts?:boolean};
}
export interface GenerateRequest {prompt:string;provider?:'gemini'|'cerebras'|'groq';generationConfig?:GenerationConfig}
export type GenerateResponse = {text:string}|{error:string;code?:string;retryable?:boolean;daily?:boolean};
