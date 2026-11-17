# AI sinov natijalari (prompt v2)

Prompt: docs/prompt.md
Kalit: docs/test-essays.md

> ESLATMA: Quyidagi "Reference: Claude" natijalari essay va kalit muallifi
> tomonidan baholangan, shuning uchun adolatli taqqoslash uchun yaroqsiz.
> Modellarni taqqoslashda ularni kalitni ko'rsatmasdan sinang.

## Reference: Claude (kalit muallifi baholadi)

| Essay | Topilgan xato / jami | Noto'g'ri "xato" | JSON to'g'rimi? |
|---|---|---|---|
| 1 | 8/8 | 0 | ha |
| 2 (xatosiz) | 0/0 | 0 | ha |
| 3 | 8/8 | 0 | ha |
| 4 | 5/5 | 0 | ha |
| 5 | 29/29 (18 ta yozuvda) | 0 | ha |

### Essay 1

```json
{
  "estimated_level": "B1",
  "scores": {"grammar": 5, "vocabulary": 6, "task_achievement": 8, "coherence": 7},
  "errors": [
    {"original": "school uniforms are good idea", "type": "grammar", "correction": "school uniforms are a good idea", "explanation_uz": "'idea' sanaladigan birlik ot, oldidan 'a' artikli kerak."},
    {"original": "nobody feel poor or rich", "type": "grammar", "correction": "nobody feels poor or rich", "explanation_uz": "'nobody' birlik hisoblanadi, shuning uchun fe'lga -s qo'shiladi."},
    {"original": "childrens", "type": "grammar", "correction": "children", "explanation_uz": "'children' o'zi ko'plik shakli, unga -s qo'shilmaydi."},
    {"original": "uniforms saves time", "type": "grammar", "correction": "uniforms save time", "explanation_uz": "'uniforms' ko'plik, shuning uchun fe'lga -s qo'shilmaydi."},
    {"original": "dont", "type": "spelling", "correction": "don't", "explanation_uz": "Inkor qisqartmasida apostrof qo'yiladi: don't."},
    {"original": "express theirselves", "type": "grammar", "correction": "express themselves", "explanation_uz": "To'g'ri qaytim olmoshi 'themselves', 'theirselves' degan so'z yo'q."},
    {"original": "they can express them by hobbies", "type": "grammar", "correction": "they can express themselves through hobbies", "explanation_uz": "Ega o'ziga qaytganda 'themselves' kerak. 'by' o'rniga 'through' tabiiyroq."},
    {"original": "I am agree", "type": "grammar", "correction": "I agree", "explanation_uz": "'agree' o'zi fe'l, 'am' yordamchi fe'li kerak emas."}
  ],
  "style_tips_uz": ["Har bir sababga bitta aniq misol qo'shsangiz, insho yanada ishonarli bo'ladi."],
  "advice_uz": "Insho tuzilishi aniq: kirish, sabablar, qarama-qarshi fikr va xulosa bor. Ega va fe'l moslashuvini (subject-verb agreement), artikllarni va qaytim olmoshlarini takrorlang."
}
```

### Essay 2 (xatosiz)

```json
{
  "estimated_level": "B2",
  "scores": {"grammar": 9, "vocabulary": 8, "task_achievement": 9, "coherence": 9},
  "errors": [],
  "style_tips_uz": ["'saves money' kabi umumiy fikrlarga bitta aniq misol qo'shing."],
  "advice_uz": "Insho aniq tuzilgan, bog'lovchilar o'rinli ishlatilgan, grammatik xato topilmadi. Yuqori ball uchun fikrlarni aniq misollar bilan mustahkamlang va ba'zi sodda so'zlarni boyroq sinonimlar bilan almashtiring."
}
```

### Essay 3

```json
{
  "estimated_level": "B1",
  "scores": {"grammar": 5, "vocabulary": 6, "task_achievement": 7, "coherence": 7},
  "errors": [
    {"original": "city life have", "type": "grammar", "correction": "city life has", "explanation_uz": "'life' birlik ot, shuning uchun 'has' ishlatiladi."},
    {"original": "some problem", "type": "grammar", "correction": "some problems", "explanation_uz": "'some' dan keyin ko'plik ot keladi: problems."},
    {"original": "I visit my grandmother's village", "type": "grammar", "correction": "I visited my grandmother's village", "explanation_uz": "'Last summer' o'tgan vaqtni bildiradi, shuning uchun 'visited' kerak."},
    {"original": "very relax", "type": "grammar", "correction": "very relaxed", "explanation_uz": "Holatni bildirish uchun sifatdosh 'relaxed' ishlatiladi."},
    {"original": "more fresh", "type": "grammar", "correction": "fresher", "explanation_uz": "Qisqa sifatlarning qiyosiy darajasi -er bilan yasaladi: fresher."},
    {"original": "less opportunities", "type": "grammar", "correction": "fewer opportunities", "explanation_uz": "Sanaladigan ko'plik otlar bilan 'fewer' ishlatiladi, 'less' emas."},
    {"original": "the best choice depend", "type": "grammar", "correction": "the best choice depends", "explanation_uz": "'choice' birlik ot, fe'lga -s qo'shiladi."},
    {"original": "on person's age", "type": "grammar", "correction": "on a person's age", "explanation_uz": "'person's' oldidan artikl kerak: a person's age."}
  ],
  "style_tips_uz": ["'in buses' o'rniga 'on buses' tabiiyroq eshitiladi."],
  "advice_uz": "Fikrlar mantiqiy va misollar bor. Fe'l zamonlari va ega-fe'l moslashuviga e'tibor bering, 'less' va 'fewer' farqini takrorlang."
}
```

### Essay 4

```json
{
  "estimated_level": "B1",
  "scores": {"grammar": 5, "vocabulary": 6, "task_achievement": 7, "coherence": 7},
  "errors": [
    {"original": "in social media", "type": "grammar", "correction": "on social media", "explanation_uz": "Ijtimoiy tarmoqlar bilan 'on' predlogi ishlatiladi: on social media."},
    {"original": "friends who lives", "type": "grammar", "correction": "friends who live", "explanation_uz": "'friends' ko'plik, shuning uchun 'who live'."},
    {"original": "and doesn't do their homework", "type": "grammar", "correction": "and don't do their homework", "explanation_uz": "Ega 'they' (ko'plik), shuning uchun 'don't' kerak."},
    {"original": "bullying in the internet", "type": "grammar", "correction": "bullying on the internet", "explanation_uz": "'the internet' bilan 'on' predlogi ishlatiladi."},
    {"original": "their children spends", "type": "grammar", "correction": "their children spend", "explanation_uz": "'children' ko'plik, fe'lga -s qo'shilmaydi."}
  ],
  "style_tips_uz": [],
  "advice_uz": "Insho mavzuni yaxshi yoritadi, afzallik va kamchiliklar muvozanatli. Predloglar (on/in) va ega-fe'l moslashuvini takrorlang."
}
```

### Essay 5

```json
{
  "estimated_level": "A2",
  "scores": {"grammar": 2, "vocabulary": 4, "task_achievement": 6, "coherence": 5},
  "errors": [
    {"original": "I go to my friend house", "type": "grammar", "correction": "I went to my friend's house", "explanation_uz": "Voqea o'tgan hafta bo'lgan, shuning uchun 'went' kerak. Egalikda 'friend's house' deyiladi."},
    {"original": "We play football and then we eat lunch in cafe", "type": "grammar", "correction": "We played football and then we ate lunch in a cafe", "explanation_uz": "O'tgan zamon: play → played, eat → ate (noto'g'ri fe'l). 'cafe' oldida 'a' kerak."},
    {"original": "we goes to cinema and watch a film", "type": "grammar", "correction": "we went to the cinema and watched a film", "explanation_uz": "go → went (noto'g'ri fe'l), watch → watched. 'the cinema' artikl bilan ishlatiladi."},
    {"original": "very interesting film", "type": "grammar", "correction": "a very interesting film", "explanation_uz": "Sanaladigan birlik ot oldidan 'a' artikli kerak."},
    {"original": "I come back home", "type": "grammar", "correction": "I came back home", "explanation_uz": "come → came (noto'g'ri fe'l), o'tgan zamon."},
    {"original": "My mother ask me", "type": "grammar", "correction": "My mother asked me", "explanation_uz": "O'tgan zamon: ask → asked."},
    {"original": "I tell her everything", "type": "grammar", "correction": "I told her everything", "explanation_uz": "tell → told (noto'g'ri fe'l)."},
    {"original": "I wake up late", "type": "grammar", "correction": "I woke up late", "explanation_uz": "wake → woke (noto'g'ri fe'l)."},
    {"original": "I have breakfast with my family and then I help my father", "type": "grammar", "correction": "I had breakfast with my family and then I helped my father", "explanation_uz": "have → had (noto'g'ri fe'l), help → helped."},
    {"original": "We plant three small tree", "type": "grammar", "correction": "We planted three small trees", "explanation_uz": "O'tgan zamon: planted. 'three' dan keyin ko'plik ot: trees."},
    {"original": "My little sister want to help", "type": "grammar", "correction": "My little sister wanted to help", "explanation_uz": "O'tgan zamon: want → wanted."},
    {"original": "I do my homework", "type": "grammar", "correction": "I did my homework", "explanation_uz": "do → did (noto'g'ri fe'l)."},
    {"original": "boring book", "type": "grammar", "correction": "a boring book", "explanation_uz": "Birlik sanaladigan ot oldidan 'a' artikli kerak."},
    {"original": "I must to finish", "type": "grammar", "correction": "I had to finish", "explanation_uz": "'must' dan keyin 'to' ishlatilmaydi. O'tgan zamonda 'had to' deyiladi."},
    {"original": "my grandfather call me and we talk", "type": "grammar", "correction": "my grandfather called me and we talked", "explanation_uz": "O'tgan zamon: call → called, talk → talked."},
    {"original": "He ask me many questions and I answer him", "type": "grammar", "correction": "He asked me many questions and I answered him", "explanation_uz": "O'tgan zamon: asked, answered."},
    {"original": "I watch TV with my brother and then I go to bed", "type": "grammar", "correction": "I watched TV with my brother and then I went to bed", "explanation_uz": "O'tgan zamon: watch → watched, go → went."},
    {"original": "I want go to my friend house", "type": "grammar", "correction": "I want to go to my friend's house", "explanation_uz": "'want' dan keyin 'to' kerak. Egalikda 'friend's house' deyiladi."}
  ],
  "style_tips_uz": ["Oxirgi gapda 'I am very happy' o'rniga hikoya zamoniga mos 'I was very happy' ham ishlatsa bo'ladi."],
  "advice_uz": "Hikoya mazmuni aniq va voqealar ketma-ketligi tushunarli. Eng katta muammo: butun hikoya o'tgan zamonda bo'lishi kerak, lekin ko'p fe'l hozirgi zamonda yozilgan. Noto'g'ri fe'llarni (go, eat, come, tell, wake, have, do) yodlang va artikllarni takrorlang."
}
```

## Xulosa (keyin to'ldiriladi)

Boshqa modellar kalitsiz sinalgach, quyidagi jadvalni to'ldiring:

| Essay | Model B: topilgan / jami | Model B: noto'g'ri "xato" |
|---|---|---|
| 1 | | |
| 2 (xatosiz) | | |
| 3 | | |
| 4 | | |
| 5 | | |