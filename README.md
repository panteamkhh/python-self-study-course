# Python Self-Study Path — Fundamentals to Advanced

یک دوره‌ی کامل و خودآموز پایتون، از صفر تا سطح پیشرفته، برای یادگیری مستقل بدون نیاز به ویدیو. هر درس یک واحد کامل شامل توضیح مفهومی، مثال‌های اجرا‌شدنی، تمرین، پاسخ‌نامه و کوییز است.

این ریپو از سه بخش تشکیل شده که پشت‌سرهم و به‌ترتیب باید مطالعه شوند. شماره‌ی درس‌ها در کل ریپو پیوسته است (۱ تا ۱۵) تا مسیر یادگیری واضح و بدون ابهام باشد.

---

## ساختار دوره

| بخش | عنوان | درس‌ها | توضیح |
|---|---|---|---|
| 📗 [01-python-fundamentals](./01-python-fundamentals) | Python Fundamentals | درس ۱ تا ۵ | مبانی پایتون، برای افرادی که هیچ تجربه‌ی برنامه‌نویسی ندارند |
| 📘 [02-python-intermediate](./02-python-intermediate) | Python Intermediate | درس ۶ تا ۱۰ | ساختمان‌داده‌ها، توابع، و مدیریت خطا |
| 📙 [03-python-advanced](./03-python-advanced) | Python Advanced | درس ۱۱ تا ۱۵ | برنامه‌نویسی شی‌گرا، متدهای ویژه، و جنریتورها |

---

## فهرست کامل درس‌ها (۱ تا ۱۵)

### 📗 بخش اول — Python Fundamentals (درس ۱–۵)

| # | درس | موضوع |
|---|---|---|
| 01 | [Lesson-01-Your-First-Program](./01-python-fundamentals/Lesson-01-Your-First-Program) | `print()`، کامنت‌ها، ترتیب اجرای برنامه |
| 02 | [Lesson-02-Variables-and-Data-Types](./01-python-fundamentals/Lesson-02-Variables-and-Data-Types) | متغیرها، `int`، `float`، `str`، `bool`، `type()` |
| 03 | [Lesson-03-Working-with-Numbers](./01-python-fundamentals/Lesson-03-Working-with-Numbers) | عملگرهای محاسباتی، تقسیم صحیح، باقی‌مانده، توان |
| 04 | [Lesson-04-Type-Conversion](./01-python-fundamentals/Lesson-04-Type-Conversion) | `int()`، `float()`، `str()`، `bool()` و نکات تبدیل نوع |
| 05 | [Lesson-05-Comparison-and-Boolean-Logic](./01-python-fundamentals/Lesson-05-Comparison-and-Boolean-Logic) | `==`، `!=`، `<`، `>`، `and`، `or`، `not` |

📄 مرجع سریع: [CheatSheet-Part-01.md](./01-python-fundamentals/CheatSheet-Part-01.md)

### 📘 بخش دوم — Python Intermediate (درس ۶–۱۰)

| # | درس | موضوع |
|---|---|---|
| 06 | [Lesson-06-Sets-and-Operations](./02-python-intermediate/Lesson-06-Sets-and-Operations) | مجموعه‌ها (Sets) و عملیات روی آن‌ها |
| 07 | [Lesson-07-Defining-Functions](./02-python-intermediate/Lesson-07-Defining-Functions) | تعریف توابع |
| 08 | [Lesson-08-Arguments-and-Scope](./02-python-intermediate/Lesson-08-Arguments-and-Scope) | آرگومان‌ها و دامنه‌ی متغیرها (Scope) |
| 09 | [Lesson-09-Higher-Order-Functions](./02-python-intermediate/Lesson-09-Higher-Order-Functions) | توابع مرتبه‌بالاتر (Higher-Order Functions) |
| 10 | [Lesson-10-Try-and-Except](./02-python-intermediate/Lesson-10-Try-and-Except) | مدیریت خطا با `try` و `except` |

📄 مرجع سریع: [CheatSheet-Part-02.md](./02-python-intermediate/CheatSheet-Part-02.md)

### 📙 بخش سوم — Python Advanced (درس ۱۱–۱۵)

| # | درس | موضوع |
|---|---|---|
| 11 | [Lesson-11-Classes-and-Objects](./03-python-advanced/Lesson-11-Classes-and-Objects) | کلاس‌ها و اشیاء |
| 12 | [Lesson-12-Inheritance-and-Polymorphism](./03-python-advanced/Lesson-12-Inheritance-and-Polymorphism) | وراثت و چندریختی (Polymorphism) |
| 13 | [Lesson-13-Special-Methods](./03-python-advanced/Lesson-13-Special-Methods) | متدهای ویژه / Dunder Methods |
| 14 | [Lesson-14-Generators-and-Yield](./03-python-advanced/Lesson-14-Generators-and-Yield) | جنریتورها و `yield` |
| 15 | [Lesson-15-Generator-Expressions](./03-python-advanced/Lesson-15-Generator-Expressions) | عبارات جنریتوری (Generator Expressions) |

📄 مرجع سریع: [CheatSheet-Part-03.md](./03-python-advanced/CheatSheet-Part-03.md)

---

## ساختار هر درس

هر پوشه‌ی `Lesson-XX-Topic-Name` دقیقاً شامل این فایل‌هاست:

```text
Lesson-XX-Topic-Name/
├── lesson.md       آموزش کامل: مفاهیم، مثال‌ها، اشتباهات رایج
├── examples.py     تمام مثال‌های درس، آماده‌ی اجرا
├── exercise.md      تمرین‌های عملی (ساده تا سخت) — فقط سؤال
├── solution.py      پاسخ کامل و توضیح‌داده‌شده‌ی هر تمرین
└── quiz.md          کوییز پایان درس همراه با پاسخنامه
```

## نحوه‌ی مطالعه

1. `lesson.md` را کامل بخوانید.
2. `examples.py` را خودتان اجرا کنید و مقادیر را تغییر دهید.
3. تمرین‌های `exercise.md` را بدون نگاه‌کردن به پاسخ حل کنید.
4. جواب‌های خودتان را با `solution.py` مقایسه کنید.
5. `quiz.md` را بزنید تا از یادگیری خودتان مطمئن شوید.
6. درس بعدی را طبق شماره‌ی پیوسته (۱ تا ۱۵) ادامه دهید.

> توجه: هر بخش (fundamentals / intermediate / advanced) یک فایل `README.md` اختصاصی هم دارد که نسخه‌ی اصلی و کامل‌تر توضیحات همان بخش است.

## پیش‌نیازها

- نصب بودن Python 3 (`python3 --version`)
- یک ویرایشگر متن
- ترمینال / خط فرمان

نیازی به هیچ نرم‌افزار یا حساب کاربری دیگری نیست.

## لایسنس

این دوره صرفاً برای استفاده‌ی شخصی و خودآموزی ارائه شده است.
