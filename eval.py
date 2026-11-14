from ask import ask

tests = [
    ("حافظ در چه قرنی زندگی می‌کرد؟", "هشتم"),
    ("حافظ در کدام شهر زندگی کرد؟", "شیراز"),
    ("فردوسی کدام کتاب را سرود؟", "شاهنامه"),
    ("اصفهان به چه لقبی معروف است؟", "نصف جهان"),
    ("پایتخت ایران کدام شهر است؟", "تهران"),
]

score = 0
for question, keyword in tests:
    answer = ask(question)
    ok = keyword in answer
    score += ok
    print("OK " if ok else "BAD", question, "->", answer.replace("\n", " "))
