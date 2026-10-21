# Развёртывание и установка

[English](DEPLOYMENT.en.md)

Это договор на инструкции **созданного агентом приложения**. Команды ниже
предполагают, что агент уже реализовал package.json, scripts и gemini-proxy/.
Они не запускают приложение из одного комплекта задания. Фактические зависимости,
версии инструментов и команды агент обязан закрепить в README и lock-файлах.

## 1. Автономная разработка

Node.js 22+, npm, Git. Сначала проверьте комплект `node tools/validate-kit.cjs`.
В корне уже созданного приложения:

```sh
npm ci
npm ci --prefix gemini-proxy
npm run book:check
npm run check
npx expo start --web
```

При первом создании lock-файла агент использует npm install; последующие установки
— npm ci. Пустой EXPO_PUBLIC_GEMINI_PROXY_URL оставляет автономный режим.
Для нативного клиента: `npx expo start --dev-client` после его отдельной сборки;
Expo Go допустим только если установленная версия поддерживает выбранный SDK.
Для Android по USB/эмулятору: Android SDK, совместимый JDK, затем
`npx expo run:android`. Локальный iOS: macOS, Xcode и `npx expo run:ios`.
Нельзя обещать локальную iOS-сборку на Windows.

В проекте должны работать: book:build, book:check, type-check,
type-check:proxy, test, check, check:ui. Их содержание — DEVELOPMENT.md.
Первые проверки не должны расходовать настоящую квоту ИИ.

## 2. Собственный ИИ-прокси

Cloudflare-аккаунт с доступностью Workers и SQLite Durable Objects, ключ хотя бы
одного провайдера. Скопируйте шаблон reference/config/wrangler.example.toml в
gemini-proxy/wrangler.toml, задайте собственное имя и доступную модель, реализуйте
Worker и QuotaLimiter по AI.md. Шаблон с CHOOSE_SUPPORTED_MODEL не готов к выпуску.

```sh
cd gemini-proxy
npm ci
npx wrangler login
npx wrangler secret put GEMINI_API_KEY
npm run type-check
npm run build
npx wrangler deploy
```

`build` обязан означать dry-run (`wrangler deploy --dry-run`), а последняя команда
создаёт/обновляет настоящий Worker и применяет миграцию Durable Object.
Альтернативные провайдеры требуют своего secret и адаптера; не включайте fallback
на несуществующий ключ. Никогда не меняйте существующий migration tag задним
числом: для изменения схемы добавляйте новую миграцию.

Проверьте `GET https://<ваш-worker>.workers.dev/health`, затем один настоящий
небольшой POST. Он расходует квоту. Убедитесь, что ограничение запросов и глобальная
квота срабатывают, ключи не попадают в ответ/логи и ошибки объясняют повторяемость.
Локальные Worker-тесты используют фиктивный upstream и виртуальное время.

В корневом .env приложения:

```dotenv
EXPO_PUBLIC_GEMINI_PROXY_URL=https://<ваш-worker>.workers.dev/v1/generate
```

Перезапустите Metro; при сомнениях `npx expo start --clear`.
Ключи провайдера сюда не помещать. EXPO_PUBLIC встраивается в клиент и доступен
пользователю. Для локального Worker secret можно использовать игнорируемый
`.dev.vars`; в Git допускается только пример с пустыми значениями.

## 3. Собственный EAS-проект и Android APK

В app.json/app.config задайте собственные slug, android.package,
ios.bundleIdentifier и assets. Создайте собственный Expo/EAS-проект:

```sh
npx eas-cli login
npx eas-cli init
npx eas-cli build:configure
```

Не копируйте owner/projectId или подпись автора. Сохраните собственную подпись
для обновлений; новый android.package ставится как отдельное приложение.
Для обновления существующего приложения нужны совпадающие package/signature
и увеличенный versionCode. Версия приложения и номер нативной сборки — разные поля.

Укажите build profiles из reference/config/eas.example.json. Для сетевой сборки:

```sh
npx eas-cli env:create --environment preview --name EXPO_PUBLIC_GEMINI_PROXY_URL --value https://<ваш-worker>.workers.dev/v1/generate --visibility plaintext
npx eas-cli env:create --environment production --name EXPO_PUBLIC_GEMINI_PROXY_URL --value https://<ваш-worker>.workers.dev/v1/generate --visibility plaintext
npx eas-cli build --platform android --profile preview
```

Игнорируемый локальный .env не является надёжным источником облачного окружения.
Проверьте имя environment в профиле. Публичный URL имеет plaintext visibility,
это не способ хранения ключа. Для автономной сборки не задавайте адрес.
Preview с buildType=apk — установочный файл; production Android по умолчанию AAB
для магазина. Загруженный JS bundle или dist/ не является APK.

Дождитесь завершения EAS, получите именно артефакт этой сборки, запишите version,
versionCode и SHA-256. Проверьте установку на Android, запуск без сети, перезапуск,
системный выбор/отправку backup, Back, клавиатуру, таблицы, безопасные отступы.
Для обновления проверьте сохранение реального тестового профиля после установки
поверх. Не предлагайте отключать защиту устройства вместо проверки происхождения.

SHA-256: `Get-FileHash -Algorithm SHA256 ./app.apk` (PowerShell) либо
`shasum -a 256 ./app.apk` (macOS). Храните релизные подписи вне Git и публичного архива.
Cloud EAS и Apple distribution могут требовать собственные аккаунты/условия сервиса.

## 4. iOS и web

```sh
npx eas-cli build --platform ios --profile production
npx expo export --platform web --output-dir dist
```

Для iOS отдельно настраиваются Apple signing и распространение; Android APK не
подходит. Экспорт web можно отдавать статическим HTTPS-хостингом с поддержкой
выбранной маршрутизации. Прокси развёртывается отдельно, его CORS должен разрешать
используемый web-клиент. Изменение hostname web создаёт другое локальное хранилище;
перенос — через экспорт/импорт. Hosting не даёт синхронизацию прогресса автоматически.

## 5. UI-проверка с фиктивным ИИ

В PowerShell из созданного приложения:

```powershell
$env:EXPO_PUBLIC_GEMINI_PROXY_URL = 'https://smoke.invalid/v1/generate'
npx expo export --platform web --output-dir dist-audit
npm run check:ui
Remove-Item Env:EXPO_PUBLIC_GEMINI_PROXY_URL
```

В POSIX: `EXPO_PUBLIC_GEMINI_PROXY_URL=https://smoke.invalid/v1/generate npx expo export --platform web --output-dir dist-audit`,
затем `npm run check:ui`. UI harness обязан перехватывать запросы и блокировать
внешнюю сеть. Использовать эту сборку только для проверки. Выпуск собирается
заново с настоящим окружением или пустым URL автономного режима.

## 6. Обновление и неисправности

| Симптом | Проверка |
|---|---|
| ИИ не подключён только в APK | EAS environment профиля и встроенный публичный URL |
| 404 у генерации | Полный путь /v1/generate и deployment Worker |
| 429 | Квота/окно/глобальный бюджет; не бесконечный retry |
| Пустой/невалидный ответ | Адаптер/схема/модель; отклонить карточку, оставить офлайн |
| QUOTA отсутствует | binding, export класса, SQLite migration и deployment |
| Новая глава отсутствует | book:build → book:check → новая сборка |
| Прогресс не читается | Не очищать storage; повтор/экспорт исходного для восстановления |
| Новый URL работает только после перезапуска | Публичные env встраиваются при сборке, обновить bundle |

Перед обновлением: экспорт тестового профиля, тест миграции, проверки, новые
артефакты. Изменение провайдера/модели/квот Worker требует его deployment;
изменение URL или native dependency — соответствующей новой клиентской сборки.
Откат UI не откатывает уже изменённую схему данных: сохранить совместимую миграцию
и проверенный backup. Не сбрасывать квоты переименованием миграции ради обхода бюджета.

Официальные справочники для проверки команд: [Expo/EAS environments](https://docs.expo.dev/eas/environment-variables/),
[EAS builds](https://docs.expo.dev/deploy/build-project/),
[Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/),
[Durable Object migrations](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).
Проверьте версионную документацию перед сменой SDK; корневая страница старой версии
может перенаправлять на текущую. Команды — инструкция, не заявление о выполненном deployment.
