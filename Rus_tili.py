import random
import time

def draw_table(answers_log):
    """Natijalarni aniq chizilgan jadval ko'rinishida chiqarish"""
    print("\n" + "=" * 65)
    print("BATAFSIL NATIJALAR JADVALI".center(65))
    print("=" * 65)
    print(f"| {'№':^3} | {'Misol':^14} | {'Sizning javob':^15} | {'To‘g‘ri javob':^14} | {'Holat':^8} |")
    print("|" + "-" * 5 + "|" + "-" * 16 + "|" + "-" * 17 + "|" + "-" * 16 + "|" + "-" * 10 + "|")
    
    for row in answers_log:
        status = "To'g'ri" if row["is_correct"] else "Xato"
        print(f"| {row['num']:^3} | {row['problem']:^14} | {str(row['user_ans']):^15} | {str(row['correct_ans']):^14} | {status:^8} |")
    
    print("=" * 65)

def main():
    print("=" * 60)
    print(" MATEMATIKA TRENAJORI: KO'PAYTIRISH VA BO'LISH".center(60))
    print(" Tuzuvchi: Quljanova Shukurjon Zaribovna".center(60))
    print("=" * 60)

    # O'quvchi ma'lumotlari
    student_name = input("\nO'quvchining ismi va familiyasini kiriting: ").strip()
    while not student_name:
        student_name = input("Iltimos, ism va familiyangizni kiriting: ").strip()

    # Bosh menyu: Amal turini tanlash
    print("\n--- MASHQ TURINI TANLANG ---")
    print("1. Aralash (Ko'paytirish va Bo'lish)")
    print("2. Faqat Ko'paytirish (×)")
    print("3. Faqat Bo'lish (÷)")
    
    while True:
        menu_choice = input("Tanlovingizni kiriting (1, 2 yoki 3): ").strip()
        if menu_choice in ["1", "2", "3"]:
            break
        print("Noto'g'ri tanlov! Faqat 1, 2 yoki 3 ni tanlang.")

    score = 0
    total_questions = 15
    answers_log = []

    print("\n" + "-" * 40)
    print(f"Mashq boshlandi! Jami {total_questions} ta savol.")
    print("-" * 40)
    
    start_time = time.time()

    for i in range(1, total_questions + 1):
        # Menyuga asosan amalni aniqlash
        if menu_choice == "2":
            operation = "*"
        elif menu_choice == "3":
            operation = "/"
        else:
            operation = random.choice(["*", "/"])

        # Misol sonlarini shakllantirish
        if operation == "*":
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            correct_answer = a * b
            problem_text = f"{a} * {b}"
        else:
            # Bo'lish doim qoldiqsiz butun son chiqishi uchun
            b = random.randint(2, 9)
            ans = random.randint(2, 9)
            a = b * ans
            correct_answer = ans
            problem_text = f"{a} / {b}"

        # Javobni kiritish va xatolikni tekshirish
        while True:
            try:
                user_answer = int(input(f"{i}-savol: {problem_text} = "))
                break
            except ValueError:
                print("Iltimos, faqat butun son kiriting!")

        is_correct = (user_answer == correct_answer)
        if is_correct:
            print("To'g'ri!\n")
            score += 1
        else:
            print(f"Noto'g'ri! To'g'ri javob: {correct_answer}\n")

        # Natijalar jadvali uchun ma'lumotlarni to'plash
        answers_log.append({
            "num": i,
            "problem": problem_text,
            "user_ans": user_answer,
            "correct_ans": correct_answer,
            "is_correct": is_correct
        })

    elapsed_time = round(time.time() - start_time, 1)
    accuracy = round((score / total_questions) * 100, 1)

    # Aniq chizilgan jadvalni chiqarish
    draw_table(answers_log)

    # Yakuniy hisobot
    print(f"\nO'quvchi: {student_name}")
    print(f"Jami savollar: {total_questions}")
    print(f"To'g'ri javoblar: {score}")
    print(f"Noto'g'ri javoblar: {total_questions - score}")
    print(f"Aniqlik darajasi: {accuracy}%")
    print(f"Sarflangan vaqt: {elapsed_time} soniya")
    print("=" * 60)

if __name__ == "__main__":
    main()
