# Deployment and installation

[Русский](DEPLOYMENT.md)

These instructions target the **app implemented by the agent**. Commands assume
its package.json/scripts/gemini-proxy already exist; they do not run an app from
this assignment alone. The agent must record actual tool versions/commands and lockfiles.

## Offline development

Node.js 22+, npm and Git. Validate this package with `node tools/validate-kit.cjs`.
From the generated app root:

```sh
npm ci
npm ci --prefix gemini-proxy
npm run book:check
npm run check
npx expo start --web
```

Use npm install only to create/update lockfiles, then npm ci. Empty
EXPO_PUBLIC_GEMINI_PROXY_URL enables offline mode. Use `npx expo start --dev-client`
after building a development client; Expo Go is suitable only when its installed
version supports the chosen SDK. Native local Android needs SDK/compatible JDK and
`npx expo run:android`; local iOS needs macOS/Xcode and `npx expo run:ios`.
Do not promise a local iOS build on Windows. Implement book:build/book:check,
type-check/type-check:proxy/test/check/check:ui per DEVELOPMENT.en.md. Normal
automated checks must not spend live AI quota.

## Owner-controlled AI proxy

Use your Cloudflare account with Workers/SQLite Durable Object availability and
at least one provider key. Adapt reference/config/wrangler.example.toml into
gemini-proxy/wrangler.toml; choose your name and supported model, implement Worker/
QuotaLimiter per AI.en.md. CHOOSE_SUPPORTED_MODEL is a placeholder, not release config.

```sh
cd gemini-proxy
npm ci
npx wrangler login
npx wrangler secret put GEMINI_API_KEY
npm run type-check
npm run build
npx wrangler deploy
```

build must be dry-run (`wrangler deploy --dry-run`); deploy actually publishes
and applies the Durable Object migration. Other providers need their own secret/
adapter. Enable fallback only when configured. Do not rewrite deployed migration
tags: introduce new migrations for schema changes.

Check GET https://<your-worker>.workers.dev/health and one small actual POST, which
spends quota. Verify rate/global limits and nonsecret errors/logs. Local tests mock
upstream/time. App root .env:

```dotenv
EXPO_PUBLIC_GEMINI_PROXY_URL=https://<your-worker>.workers.dev/v1/generate
```

Restart Metro, optionally `npx expo start --clear`. Never put provider keys here:
EXPO_PUBLIC values are bundled and inspectable. Local Worker secrets may use
git-ignored .dev.vars; commit only an empty example.

## EAS and Android APK

Choose your own slug/android.package/ios.bundleIdentifier/assets in app config.
Create your Expo/EAS project:

```sh
npx eas-cli login
npx eas-cli init
npx eas-cli build:configure
```

Do not copy author owner/projectId/signing credentials. Keep your signing key
for upgrades. A new package is a separate app; upgrading an existing install
requires matching package/signature and increased versionCode. App version and
native build number are distinct.

Use reference/config/eas.example.json profiles. For online builds:

```sh
npx eas-cli env:create --environment preview --name EXPO_PUBLIC_GEMINI_PROXY_URL --value https://<your-worker>.workers.dev/v1/generate --visibility plaintext
npx eas-cli env:create --environment production --name EXPO_PUBLIC_GEMINI_PROXY_URL --value https://<your-worker>.workers.dev/v1/generate --visibility plaintext
npx eas-cli build --platform android --profile preview
```

An ignored local .env is not a reliable cloud environment source; match the profile's
environment. The public endpoint is plaintext, not a provider secret. Omit it for
offline builds. Preview buildType=apk yields an installable file; Android production
defaults to store AAB. JavaScript bundles/dist are not APKs.

Wait for EAS completion, retrieve that exact artifact, record version/versionCode/
SHA-256. Physically test Android install, offline startup, restart, native backup
picker/share, Back/keyboard/tables/insets and an upgrade preserving a test profile.
Do not substitute disabling device protection for checking artifact origin.
Hash with `Get-FileHash -Algorithm SHA256 ./app.apk` in PowerShell or
`shasum -a 256 ./app.apk` on macOS. Keep signing material out of Git/public archives.
Cloud EAS/Apple distribution can require owner accounts and service terms.

## iOS and web

```sh
npx eas-cli build --platform ios --profile production
npx expo export --platform web --output-dir dist
```

iOS needs separate Apple signing/distribution; APK is not usable there. Serve
web output with HTTPS hosting and appropriate routing. Deploy proxy separately,
with CORS supporting the web client. Changing web origins creates different local
storage; use export/import to migrate. Hosting alone does not synchronize progress.

## Mocked UI checks

PowerShell from the generated app:

```powershell
$env:EXPO_PUBLIC_GEMINI_PROXY_URL = 'https://smoke.invalid/v1/generate'
npx expo export --platform web --output-dir dist-audit
npm run check:ui
Remove-Item Env:EXPO_PUBLIC_GEMINI_PROXY_URL
```

POSIX: `EXPO_PUBLIC_GEMINI_PROXY_URL=https://smoke.invalid/v1/generate npx expo export --platform web --output-dir dist-audit`,
then `npm run check:ui`. Harness must intercept requests and block external traffic.
Do not release this mock build; rebuild with production configuration or no AI URL.

## Updates and troubleshooting

| Symptom | Check |
|---|---|
| AI missing only in APK | Profile environment and bundled public URL |
| Generation 404 | Full /v1/generate path and Worker deployment |
| 429 | Quota/window/global budget; no infinite retries |
| Empty/invalid response | Adapter/schema/model; reject card, retain offline data |
| QUOTA missing | Binding, exported class, SQLite migration, deployment |
| New book chapter absent | book:build → book:check → new app build |
| Unreadable progress | Preserve storage; retry/recover instead of clearing |
| URL changes need restart | Public environment values are bundled at build time |

Before updates export a test profile, exercise migrations and run checks. Worker
provider/model/quota changes require Worker deployment; URL/native dependency
changes require the appropriate client build. UI rollback does not undo data-schema
migrations; keep compatible recovery. Do not rename migrations to evade quotas.

Official references: [EAS environments](https://docs.expo.dev/eas/environment-variables/),
[EAS builds](https://docs.expo.dev/deploy/build-project/),
[Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/),
[Durable Object migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).
Check version-specific SDK docs before API changes; old version roots may redirect
to current docs. These are instructions, not claims of a completed deployment.
