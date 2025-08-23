import random
questions = [
    {
        "question_text": "پایتخت ایران کدام شهر است؟",
        "answer": "تهران"
    },
    {
        "question_text": "اسم سازنده این برنامه چیه؟",
        "answer": "سینا"
    },
    {
        "question_text": "بزرگترین قاره جهان کدام است؟",
        "answer": "آسیا"
    },
    {
        "question_text": "طولانی‌ترین رود جهان چیست؟",
        "answer": "نیل"
    },
    {
        "question_text": "کدام سیاره نزدیک‌ترین سیاره به خورشید است؟",
        "answer": "عطارد"
    },
    {
        "question_text": "بزرگترین حیوان روی زمین چیست؟",
        "answer": "نهنگ آبی"
    },
    {
        "question_text": "اولین انسان روی کره ماه چه کسی بود؟",
        "answer": "نیل آرمسترانگ"
    },
    {
        "question_text": "کدام کشور به سرزمین آفتاب تابان معروف است؟",
        "answer": "ژاپن"
    },
    {
        "question_text": "حاصل جمع ۷ و ۸ چند می‌شود؟",
        "answer": "۱۵"
    },
    {
        "question_text": "واحد پول اروپا چیست؟",
        "answer": "یورو"
    },
    {
        "question_text": "کدام کشور بیشترین جمعیت جهان را دارد؟",
        "answer": "چین"
    },
    {
        "question_text": "بلندترین کوه جهان چه نام دارد؟",
        "answer": "اورست"
    },
    {
        "question_text": "کدام حیوان به سلطان جنگل معروف است؟",
        "answer": "شیر"
    },
    {
        "question_text": "کدام زبان بیشترین گویشور در جهان دارد؟",
        "answer": "چینی ماندارین"
    },
    {
        "question_text": "در شطرنج، مهره‌ای که فقط به صورت ضربدری حرکت می‌کند چیست؟",
        "answer": "فیل"
    },
    {
        "question_text": "آب در چند درجه سانتی‌گراد یخ می‌زند؟",
        "answer": "۰"
    },
    {
        "question_text": "کدام کشور میزبان جام جهانی فوتبال ۲۰۲۲ بود؟",
        "answer": "قطر"
    },
    {
        "question_text": "چه کسی لامپ برق را اختراع کرد؟",
        "answer": "توماس ادیسون"
    },
    {
        "question_text": "کدام فلز رسانای اصلی در سیم برق است؟",
        "answer": "مس"
    },
    {
        "question_text": "نویسنده شاهنامه چه کسی بود؟",
        "answer": "فردوسی"
    },
    {
        "question_text": "کدام کشور بزرگترین تولیدکننده نفت در جهان است؟",
        "answer": "عربستان سعودی"
    },
    {
        "question_text": "اولین پیامبر در ادیان ابراهیمی کیست؟",
        "answer": "حضرت نوح"
    },
    {
        "question_text": "کدام کشور قدیمی‌ترین تمدن دنیا را دارد؟",
        "answer": "مصر"
    },
    {
        "question_text": "کدام رنگ حاصل ترکیب آبی و زرد است؟",
        "answer": "سبز"
    },
    {
        "question_text": "چه کسی نظریه نسبیت را مطرح کرد؟",
        "answer": "آلبرت انیشتین"
    },
    {
        "question_text": "کدام حیوان سریع‌ترین حیوان خشکی است؟",
        "answer": "یوزپلنگ"
    },
    {
        "question_text": "بزرگترین دریاچه جهان چه نام دارد؟",
        "answer": "دریای خزر"
    },
    {
        "question_text": "پایتخت کشور فرانسه چیست؟",
        "answer": "پاریس"
    },
    {
        "question_text": "در کدام فصل سال برگ درختان می‌ریزد؟",
        "answer": "پاییز"
    },
    {
        "question_text": "نخستین کامپیوتر جهان چه نام داشت؟",
        "answer": "انیـاک (ENIAC)"
    }
]
random.shuffle(questions)
score = 0
count_questions = int(input("به جه تعداد سوال میخواهید پاسخ دهید"))
selected_questions = questions[:count_questions]

for question in selected_questions:
    print(f"سوال: {question['question_text']}")
    user_answer = input("پاسخ خود را وارد کنید")
    if user_answer.lower() == question['answer']:
        print("پاسخ شما صحیح است")
        score += 1
    else:
        print("پاسخ شما اشتباه است.")

print(f"بازی تمام شد! امتیاز نهایی شما: {score} از {len(selected_questions)}")

