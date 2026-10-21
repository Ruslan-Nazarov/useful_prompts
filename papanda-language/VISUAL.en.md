# Visual specification

[Русский](VISUAL.md)

reference/design-tokens.json is the numeric baseline. Brand/role/tab/token values
come from source; common page/card/touch metrics are normative reconstruction
defaults where screens differed. This is not a pixel-perfect capture of every state.
Existing logo and mascot are supplied in reference/assets/.

## System

Light mobile UI, system font supporting Cyrillic, Kazakh and Latin diacritics.
Background #F8F9FA, white surfaces, text #1E293B, secondary #64748B, borders #E2E8F0.
Accent #F97316, dark #C2410C, pressed #EA580C, light #FFF7ED, accent border #FED7AA.
Do not borrow the time-management papanda kit's warmer background/geometries.
Title 22/700, sections 18/700, body 15/24, secondary 12..14. Page padding 16,
card padding 20/radius 16, main touch targets >=44. Wrap important translations;
use restrained shadows and readable contrast. Label roles in addition to color.

## Navigation and states

White bottom bar: 📊 📚 💬 ⚡ ⚙️, equal item widths, raised central 56 circle
with white 4 border. Base height 64 plus bottom safe-area, paddingTop 6.
Respect Android navigation/status insets. Show current screen title; icon actions
need accessibility labels/roles. Nested screens have named back controls. Keyboard
must not hide saving/navigation.

Loading shows a local phase/cancel, not an indefinitely blocked whole app. Empty
states explain missing language/data/eligible words/results. Storage errors offer
non-destructive retry. Unconfigured AI leaves offline practice visible. Routine
successful actions do not produce a distracting stream of alerts.

## Screens

- Words: centered card maxWidth 420, large Russian meaning, secondary source,
  ordered flag/code/translation rows. Favorite/edit/statistics above, association
  below. Persistent tour count; vertical scrolling accommodates all seven languages.
- Recognition: target language/cue, explicit reveal control, large answer,
  known/unknown, back, snooze/favorite/progress. Swipe transitions the deck once.
- Trainer: language/mode header, brief goal, whole source, wrapping token grid,
  step controls. Tokens minWidth 80/minHeight 64, padding 12/radius 12/border 2;
  source 18/600, gloss 14, role 10/600. Hidden placeholders do not leak answers.
  Visual add badge 22 with expanded accessible hit area.
- Workshop: five compact wrapping/scrollable mode controls, language, source,
  role question, selectable tokens, check/hint/dispute/next. Label selection/errors
  as well as changing border/color. Growing mode shows step/new occurrences;
  language comparison uses one card per language.
- Book: section/contents/search/resume/bookmarks, body default 17 with 15..23
  controls. Wide tables default to cards; grid mode scrolls horizontally inside.
  Highlight the found block and scroll it into view.
- Statistics: labeled values, explanation of heuristic iMW/self-report, units,
  chart legends/empty states, separate structure skill and reasoned review plan.
  Never show invented growth without actual events.
- Settings: language/order, tour/session sizes, backup, about and reset groups.
  Selected chips are clear; boundary order arrows disabled.

Role colors: Predicate #EF4444, Subject #3B82F6, Object #F97316,
Attribute/Attribute_Subject/Attribute_Object #10B981,
Circumstance/Adverbial #8B5CF6, function roles #CBD5E1. Morpheme styling uses
neutral root and emphasized meaningful parts only when segmentation is supplied.

## Modals and responsiveness

White radius-16 menus/editors/explanations with reachable title/close, maxHeight
85% and internal vertical scrolling. Keyboard must not cover save. Explanation
starts with core text; word details/sources collapsed. Backup preview clearly
separates Cancel from Replace progress.

Verify 320/390/768/1440 logical pixels, long German forms, Kazakh letters, seven
languages and enlarged system text. No page-wide horizontal scroll. Center narrow
study cards on tablets/desktop. Keyboard/screen-reader support includes focus,
selected/disabled state and meaningful labels. Respect reduced motion. Capture
screenshots after animations settle.
