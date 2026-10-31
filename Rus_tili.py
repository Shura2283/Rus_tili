Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading

# Ovozli talaffuz uchun (ixtiyoriy, agar o'rnatilmagan bo'lsa xatolik bermaydi)
try:
    import pyttsx3
    tts_engine = pyttsx3.init()
    # Rus tili ovozini topishga urinish
    voices = tts_engine.getProperty('voices')
    for voice in voices:
        if 'ru' in voice.id.lower() or 'russian' in voice.name.lower():
            tts_engine.setProperty('voice', voice.id)
            break
    tts_engine.setProperty('rate', 140)
except Exception:
    tts_engine = None

def speak_text(text):
    """Matnni alohida oqimda ruscha talaffuz qilish"""
    if tts_engine:
        def _run():
            try:
                tts_engine.say(text)
                tts_engine.runAndWait()
            except Exception:
                pass
        threading.Thread(target=_run, daemon=True).start()

# =====================================================================
# 1. BAZALAR (ALIFBO, MATNLAR, 200 TA SO'ZLIK VIKTORINA)
# =====================================================================

LETTERS_DATA = [
    {"char": "А", "small": "а", "type": "Unli", "word": "Арбуз", "uz": "Tarvuz"},
    {"char": "Б", "small": "б", "type": "Undosh", "word": "Бабочка", "uz": "Kapalak"},
    {"char": "В", "small": "в", "type": "Undosh", "word": "Волк", "uz": "Bo‘ri"},
    {"char": "Г", "small": "г", "type": "Undosh", "word": "Гриб", "uz": "Qo‘ziqorin"},
    {"char": "Д", "small": "д", "type": "Undosh", "word": "Дом", "uz": "Uy"},
    {"char": "Е", "small": "е", "type": "Unli", "word": "Ель", "uz": "Archa"},
    {"char": "Ё", "small": "ё", "type": "Unli", "word": "Ёж", "uz": "Tipratikan"},
    {"char": "Ж", "small": "ж", "type": "Undosh", "word": "Жираф", "uz": "Jirafa"},
    {"char": "З", "small": "з", "type": "Undosh", "word": "Заяц", "uz": "Quyon"},
    {"char": "И", "small": "и", "type": "Unli", "word": "Игла", "uz": "Igna"},
    {"char": "Й", "small": "й", "type": "Undosh", "word": "Йогурт", "uz": "Yogurt"},
    {"char": "К", "small": "к", "type": "Undosh", "word": "Кот", "uz": "Mushuk"},
    {"char": "Л", "small": "л", "type": "Undosh", "word": "Лимон", "uz": "Limon"},
    {"char": "М", "small": "м", "type": "Undosh", "word": "Медведь", "uz": "Ayiq"},
    {"char": "Н", "small": "н", "type": "Undosh", "word": "Ножницы", "uz": "Qaychi"},
    {"char": "О", "small": "о", "type": "Unli", "word": "Окно", "uz": "Deraza"},
    {"char": "П", "small": "п", "type": "Undosh", "word": "Птица", "uz": "Qush"},
    {"char": "Р", "small": "р", "type": "Undosh", "word": "Рыба", "uz": "Baliq"},
    {"char": "С", "small": "с", "type": "Undosh", "word": "Солнце", "uz": "Quyosh"},
    {"char": "Т", "small": "т", "type": "Undosh", "word": "Тигр", "uz": "Yo‘lbars"},
    {"char": "У", "small": "у", "type": "Unli", "word": "Утка", "uz": "O‘rdak"},
    {"char": "Ф", "small": "ф", "type": "Undosh", "word": "Флаг", "uz": "Bayroq"},
    {"char": "Х", "small": "х", "type": "Undosh", "word": "Хлеб", "uz": "Non"},
    {"char": "Ц", "small": "ц", "type": "Undosh", "word": "Цветок", "uz": "Gul"},
    {"char": "Ч", "small": "ч", "type": "Undosh", "word": "Часы", "uz": "Soat"},
    {"char": "Ш", "small": "ш", "type": "Undosh", "word": "Шапка", "uz": "Shapka"},
    {"char": "Щ", "small": "щ", "type": "Undosh", "word": "Щётка", "uz": "Cho‘tka"},
    {"char": "Ъ", "small": "ъ", "type": "Belgi", "word": "Подъезд", "uz": "Podyezd"},
    {"char": "Ы", "small": "ы", "type": "Unli", "word": "Сыр", "uz": "Pishloq"},
    {"char": "Ь", "small": "ь", "type": "Belgi", "word": "Конь", "uz": "Ot (hayvon)"},
    {"char": "Э", "small": "э", "type": "Unli", "word": "Экран", "uz": "Ekran"},
    {"char": "Ю", "small": "ю", "type": "Unli", "word": "Юбка", "uz": "Yubka"},
    {"char": "Я", "small": "я", "type": "Unli", "word": "Яблоко", "uz": "Olma"}
]

QUIZ_WORDS_200 = [
    {"ru": "Арбуз", "uz": "Tarvuz", "char": "А"}, {"ru": "Ананас", "uz": "Ananas", "char": "А"}, {"ru": "Автобус", "uz": "Avtobus", "char": "А"}, {"ru": "Апельсин", "uz": "Apelsin", "char": "А"}, {"ru": "Альбом", "uz": "Albom", "char": "А"}, {"ru": "Акула", "uz": "Akula", "char": "А"},
    {"ru": "Бабочка", "uz": "Kapalak", "char": "Б"}, {"ru": "Банан", "uz": "Banan", "char": "Б"}, {"ru": "Брат", "uz": "Aka / Uka", "char": "Б"}, {"ru": "Бумага", "uz": "Qog‘oz", "char": "Б"}, {"ru": "Берёза", "uz": "Qayin daraxti", "char": "Б"}, {"ru": "Барабан", "uz": "Nog‘ora", "char": "Б"},
    {"ru": "Волк", "uz": "Bo‘ri", "char": "В"}, {"ru": "Вода", "uz": "Suv", "char": "В"}, {"ru": "Воздух", "uz": "Havo", "char": "В"}, {"ru": "Ветер", "uz": "Shamol", "char": "В"}, {"ru": "Время", "uz": "Vaqt", "char": "В"}, {"ru": "Врач", "uz": "Shifokor", "char": "В"},
    {"ru": "Гриб", "uz": "Qo‘ziqorin", "char": "Г"}, {"ru": "Город", "uz": "Shahar", "char": "Г"}, {"ru": "Глаз", "uz": "Ko‘z", "char": "Г"}, {"ru": "Груша", "uz": "Nok", "char": "Г"}, {"ru": "Гора", "uz": "Tog‘", "char": "Г"}, {"ru": "Голова", "uz": "Bosh", "char": "Г"},
    {"ru": "Дом", "uz": "Uy", "char": "Д"}, {"ru": "Дверь", "uz": "Eshik", "char": "Д"}, {"ru": "Друг", "uz": "Do‘st", "char": "Д"}, {"ru": "Дерево", "uz": "Daraxt", "char": "Д"}, {"ru": "Дождь", "uz": "Yomg‘ir", "char": "Д"}, {"ru": "Дорога", "uz": "Yo‘l", "char": "Д"},
    {"ru": "Ель", "uz": "Archa", "char": "Е"}, {"ru": "Енот", "uz": "Yenot", "char": "Е"}, {"ru": "Еда", "uz": "Ovqat", "char": "Е"}, {"ru": "Ежевика", "uz": "Maymunjon", "char": "Е"},
    {"ru": "Ёж", "uz": "Tipratikan", "char": "Ё"}, {"ru": "Ёлка", "uz": "Yangi yil archasi", "char": "Ё"}, {"ru": "Ёрш", "uz": "Tikanli baliqcha", "char": "Ё"},
    {"ru": "Жираф", "uz": "Jirafa", "char": "Ж"}, {"ru": "Жук", "uz": "Qo‘ng‘iz", "char": "Ж"}, {"ru": "Жизнь", "uz": "Hayot", "char": "Ж"}, {"ru": "Железо", "uz": "Temir", "char": "Ж"}, {"ru": "Женщина", "uz": "Ayol", "char": "Ж"},
    {"ru": "Заяц", "uz": "Quyon", "char": "З"}, {"ru": "Звезда", "uz": "Yulduz", "char": "З"}, {"ru": "Земля", "uz": "Yer", "char": "З"}, {"ru": "Зима", "uz": "Qish", "char": "З"}, {"ru": "Зуб", "uz": "Tish", "char": "З"}, {"ru": "Зонт", "uz": "Soyabon", "char": "З"},
    {"ru": "Игла", "uz": "Igna", "char": "И"}, {"ru": "Игра", "uz": "O‘yin", "char": "И"}, {"ru": "Имя", "uz": "Ism", "char": "И"}, {"ru": "Инженер", "uz": "Muhandis", "char": "И"}, {"ru": "Инструмент", "uz": "Asbob", "char": "И"},
    {"ru": "Йогурт", "uz": "Yogurt", "char": "Й"}, {"ru": "Йод", "uz": "Yod eritmasi", "char": "Й"},
    {"ru": "Кот", "uz": "Mushuk", "char": "К"}, {"ru": "Книга", "uz": "Kitob", "char": "К"}, {"ru": "Карандаш", "uz": "Qalam", "char": "К"}, {"ru": "Комната", "uz": "Xona", "char": "К"}, {"ru": "Корова", "uz": "Sigir", "char": "К"}, {"ru": "Компьютер", "uz": "Kompyuter", "char": "К"},
    {"ru": "Лимон", "uz": "Limon", "char": "Л"}, {"ru": "Лес", "uz": "O‘rmon", "char": "Л"}, {"ru": "Луна", "uz": "Oy", "char": "Л"}, {"ru": "Лист", "uz": "Barg / Qog‘oz", "char": "Л"}, {"ru": "Лошадь", "uz": "Ot", "char": "Л"}, {"ru": "Ложка", "uz": "Qoshiq", "char": "Л"},
    {"ru": "Медведь", "uz": "Ayiq", "char": "М"}, {"ru": "Мама", "uz": "Ona", "char": "М"}, {"ru": "Машина", "uz": "Mashina", "char": "М"}, {"ru": "Молоко", "uz": "Sut", "char": "М"}, {"ru": "Море", "uz": "Dengiz", "char": "М"}, {"ru": "Мыло", "uz": "Sovun", "char": "М"},
    {"ru": "Ножницы", "uz": "Qaychi", "char": "Н"}, {"ru": "Нос", "uz": "Burun", "char": "Н"}, {"ru": "Ночь", "uz": "Tun", "char": "Н"}, {"ru": "Небо", "uz": "Osmon", "char": "Н"}, {"ru": "Нога", "uz": "Oyoq", "char": "Н"}, {"ru": "Номер", "uz": "Raqam", "char": "Н"},
    {"ru": "Окно", "uz": "Deraza", "char": "О"}, {"ru": "Огонь", "uz": "Olov", "char": "О"}, {"ru": "Озеро", "uz": "Ko‘l", "char": "О"}, {"ru": "Осень", "uz": "Kuz", "char": "О"}, {"ru": "Остров", "uz": "Orol", "char": "О"}, {"ru": "Очки", "uz": "Ko‘zoynak", "char": "О"},
    {"ru": "Птица", "uz": "Qush", "char": "П"}, {"ru": "Папа", "uz": "Dada", "char": "П"}, {"ru": "Письмо", "uz": "Xat", "char": "П"}, {"ru": "Поезд", "uz": "Poyezd", "char": "П"}, {"ru": "Поле", "uz": "Dala", "char": "П"}, {"ru": "Парк", "uz": "Bog‘ / Park", "char": "П"},
    {"ru": "Рыба", "uz": "Baliq", "char": "Р"}, {"ru": "Рука", "uz": "Qo‘l", "char": "Р"}, {"ru": "Ручка", "uz": "Ruchka", "char": "Р"}, {"ru": "Река", "uz": "Daryo", "char": "Р"}, {"ru": "Роза", "uz": "Atirgul", "char": "Р"}, {"ru": "Работа", "uz": "Ish", "char": "Р"},
    {"ru": "Солнце", "uz": "Quyosh", "char": "С"}, {"ru": "Стол", "uz": "Stol", "char": "С"}, {"ru": "Стул", "uz": "Stul", "char": "С"}, {"ru": "Семья", "uz": "Oila", "char": "С"}, {"ru": "Снег", "uz": "Qor", "char": "С"}, {"ru": "Собака", "uz": "It", "char": "С"},
    {"ru": "Тигр", "uz": "Yo‘lbars", "char": "Т"}, {"ru": "Тетрадь", "uz": "Daftar", "char": "Т"}, {"ru": "Телефон", "uz": "Telefon", "char": "Т"}, {"ru": "Тарелка", "uz": "Tarelka", "char": "Т"}, {"ru": "Трава", "uz": "O‘t / Maysa", "char": "Т"}, {"ru": "Торт", "uz": "Tort", "char": "Т"},
    {"ru": "Утка", "uz": "O‘rdak", "char": "У"}, {"ru": "Ученик", "uz": "O‘quvchi", "char": "У"}, {"ru": "Учитель", "uz": "O‘qituvchi", "char": "У"}, {"ru": "Улица", "uz": "Ko‘cha", "char": "У"}, {"ru": "Утро", "uz": "Ertalab / Tong", "char": "У"}, {"ru": "Ухо", "uz": "Quloq", "char": "У"},
    {"ru": "Флаг", "uz": "Bayroq", "char": "Ф"}, {"ru": "Фрукт", "uz": "Meva", "char": "Ф"}, {"ru": "Фонарь", "uz": "Fonar", "char": "Ф"}, {"ru": "Фото", "uz": "Surat", "char": "Ф"}, {"ru": "Футбол", "uz": "Futbol", "char": "Ф"},
    {"ru": "Хлеб", "uz": "Non", "char": "Х"}, {"ru": "Холод", "uz": "Sovuq", "char": "Х"}, {"ru": "Художник", "uz": "Rassom", "char": "Х"}, {"ru": "Хвост", "uz": "Dum", "char": "Х"},
    {"ru": "Цветок", "uz": "Gul", "char": "Ц"}, {"ru": "Царь", "uz": "Podsho", "char": "Ц"}, {"ru": "Цирк", "uz": "Sirk", "char": "Ц"}, {"ru": "Цена", "uz": "Narx", "char": "Ц"}, {"ru": "Цепь", "uz": "Zanjir", "char": "Ц"},
    {"ru": "Часы", "uz": "Soat", "char": "Ч"}, {"ru": "Чай", "uz": "Choy", "char": "Ч"}, {"ru": "Человек", "uz": "Inson", "char": "Ч"}, {"ru": "Чашка", "uz": "Chashka", "char": "Ч"}, {"ru": "Число", "uz": "Son", "char": "Ч"},
    {"ru": "Шапка", "uz": "Shapka", "char": "Ш"}, {"ru": "Школа", "uz": "Maktab", "char": "Ш"}, {"ru": "Шарф", "uz": "Sharf", "char": "Ш"}, {"ru": "Шкаф", "uz": "Shkaf", "char": "Ш"}, {"ru": "Шаг", "uz": "Qadam", "char": "Ш"},
    {"ru": "Щётка", "uz": "Cho‘tka", "char": "Щ"}, {"ru": "Щит", "uz": "Qalqon", "char": "Щ"}, {"ru": "Щенок", "uz": "Kuchukcha", "char": "Щ"}, {"ru": "Щука", "uz": "Cho‘rtanbaliq", "char": "Щ"},
    {"ru": "Экран", "uz": "Ekran", "char": "Э"}, {"ru": "Этаж", "uz": "Qavat", "char": "Э"}, {"ru": "Экскурсия", "uz": "Sayohat", "char": "Э"}, {"ru": "Энергия", "uz": "Energiya", "char": "Э"},
    {"ru": "Юбка", "uz": "Yubka", "char": "Ю"}, {"ru": "Юг", "uz": "Janub", "char": "Ю"}, {"ru": "Юмор", "uz": "Hazil", "char": "Ю"}, {"ru": "Юноша", "uz": "O‘smir yigit", "char": "Ю"},
    {"ru": "Яблоко", "uz": "Olma", "char": "Я"}, {"ru": "Ягода", "uz": "Rezavor meva", "char": "Я"}, {"ru": "Язык", "uz": "Til", "char": "Я"}, {"ru": "Яйцо", "uz": "Tuxum", "char": "Я"}, {"ru": "Якорь", "uz": "Langar", "char": "Я"},
    {"ru": "Сыр", "uz": "Pishloq", "char": "С"}, {"ru": "Дым", "uz": "Tutun", "char": "Д"}, {"ru": "Бык", "uz": "Ho‘kiz", "char": "Б"}, {"ru": "Мышь", "uz": "Sichqon", "char": "М"}, {"ru": "Рысь", "uz": "Silovsin", "char": "Р"},
    {"ru": "Картина", "uz": "Rasm / Kartina", "char": "К"}, {"ru": "Зеркало", "uz": "Oyna", "char": "З"}, {"ru": "Подушка", "uz": "Yostiq", "char": "П"}, {"ru": "Одеяло", "uz": "Ko‘rpa", "char": "О"},
    {"ru": "Платье", "uz": "Ko‘ylak", "char": "П"}, {"ru": "Пальто", "uz": "Palto", "char": "П"}, {"ru": "Ботинки", "uz": "Botinkalar", "char": "Б"}, {"ru": "Носки", "uz": "Paypoqlar", "char": "Н"},
    {"ru": "Вилка", "uz": "Sanchqi", "char": "В"}, {"ru": "Нож", "uz": "Pichoq", "char": "Н"}, {"ru": "Чайник", "uz": "Choynak", "char": "Ч"}, {"ru": "Сковорода", "uz": "Tova", "char": "С"},
    {"ru": "Кастрюля", "uz": "Qozon", "char": "К"}, {"ru": "Сахар", "uz": "Shakar", "char": "С"}, {"ru": "Соль", "uz": "Tuz", "char": "С"}, {"ru": "Масло", "uz": "Yog‘", "char": "М"},
    {"ru": "Мясо", "uz": "Go‘sht", "char": "М"}, {"ru": "Суп", "uz": "Sho‘rva", "char": "С"}, {"ru": "Каша", "uz": "Bo‘tqa", "char": "К"}, {"ru": "Салат", "uz": "Salat", "char": "С"},
    {"ru": "Морковь", "uz": "Sabzi", "char": "М"}, {"ru": "Картофель", "uz": "Kartoshka", "char": "К"}, {"ru": "Лук", "uz": "Piyoz", "char": "Л"}, {"ru": "Огурец", "uz": "Bodring", "char": "О"},
    {"ru": "Помидор", "uz": "Pomidor", "char": "П"}, {"ru": "Капуста", "uz": "Karam", "char": "К"}, {"ru": "Свекла", "uz": "Lavlagi", "char": "С"}, {"ru": "Чеснок", "uz": "Sarimsoq", "char": "Ч"},
    {"ru": "Виноград", "uz": "Uzum", "char": "В"}, {"ru": "Персик", "uz": "Shaftoli", "char": "П"}, {"ru": "Слива", "uz": "Olxo‘ri", "char": "С"}, {"ru": "Вишня", "uz": "Gilos / Olcha", "char": "В"},
    {"ru": "Клубника", "uz": "Qulupnay", "char": "К"}, {"ru": "Малина", "uz": "Malina", "char": "М"}, {"ru": "Орех", "uz": "Yong‘oq", "char": "О"}, {"ru": "Мёд", "uz": "Asal", "char": "М"},
    {"ru": "Автомобиль", "uz": "Avtomobil", "char": "А"}, {"ru": "Самолёт", "uz": "Samolyot", "char": "С"}, {"ru": "Вертолёт", "uz": "Vertolyot", "char": "В"}, {"ru": "Корабль", "uz": "Kema", "char": "К"},
    {"ru": "Лодка", "uz": "Qayiq", "char": "Л"}, {"ru": "Велосипед", "uz": "Velosiped", "char": "В"}, {"ru": "Метро", "uz": "Metro", "char": "М"}, {"ru": "Трамвай", "uz": "Tramvay", "char": "Т"},
    {"ru": "Вокзал", "uz": "Vokzal", "char": "В"}, {"ru": "Аэропорт", "uz": "Aeroport", "char": "А"}, {"ru": "Мост", "uz": "Ko‘prik", "char": "М"}, {"ru": "Площадь", "uz": "Maydon", "char": "П"},
    {"ru": "Больница", "uz": "Shifoxona", "char": "Б"}, {"ru": "Аптека", "uz": "Dorixona", "char": "А"}, {"ru": "Магазин", "uz": "Do‘kon", "char": "М"}, {"ru": "Рынок", "uz": "Bozor", "char": "Р"},
    {"ru": "Музей", "uz": "Muzey", "char": "М"}, {"ru": "Театр", "uz": "Teatr", "char": "Т"}, {"ru": "Кино", "uz": "Kino", "char": "К"}, {"ru": "Стадион", "uz": "Stadion", "char": "С"}
]

TEXTS_50 = [
    {"id": 1, "ru": "Здравствуйте! Меня зовут Азиз. Я учу русский язык.", "uz": "Assalomu alaykum! Mening ismim Aziz. Men rus tilini o'rganyapman."},
    {"id": 2, "ru": "Это моя семья. Папа, мама и я живём дружно.", "uz": "Bu mening oilam. Dadam, onam va men ahil yashaymiz."},
    {"id": 3, "ru": "Сегодня солнечный день. На небе нет туч.", "uz": "Bugun quyoshli kun. Osmonda bulutlar yo'q."},
    {"id": 4, "ru": "Вот наша школа. В ней большие и светлые классы.", "uz": "Mana bizning maktabimiz. Unda katta va yorug' sinflar bor."},
    {"id": 5, "ru": "Мой друг любит читать книги. Он много знает.", "uz": "Mening do'stim kitob o'qishni yaxshi ko'radi. U ko'p narsani biladi."},
    {"id": 6, "ru": "На столе лежат тетрадь, ручка и карандаш.", "uz": "Stol ustida daftar, ruchka va qalam yotibdi."},
    {"id": 7, "ru": "У меня есть кот. Его зовут Барсик. Он очень пушистый.", "uz": "Mening mushugim bor. Uning ismi Barsik. U juda paxmoq."},
    {"id": 8, "ru": "Утром я пью тёплый чай с лимоном и ем хлеб.", "uz": "Ertalab men limonli iliq choy ichaman va non yeyman."},
    {"id": 9, "ru": "Летом в саду созревают сладкие яблоки и груши.", "uz": "Yozda bog'da shirin olmalar va noklar pishadi."},
    {"id": 10, "ru": "Мы часто гуляем в красивом городском парке.", "uz": "Biz ko'pincha shaharning go'zal bog'ida sayr qilamiz."},
    {"id": 11, "ru": "Моя сестра хорошо поёт и играет на пианино.", "uz": "Mening singlim chiroyli qo'shiq aytadi va pianino chaladi."},
    {"id": 12, "ru": "Учительница объясняет нам новое правило.", "uz": "O'qituvchi ayol bizga yangi qoidani tushuntirmoqda."},
    {"id": 13, "ru": "Зимой часто идёт белый пушистый снег.", "uz": "Qishda tez-tez oq, mayin qor yog'adi."},
    {"id": 14, "ru": "Мама готовит вкусный обед для всей семьи.", "uz": "Onam butun oila uchun mazali tushlik tayyorlayapti."},
    {"id": 15, "ru": "Папа пришёл с работы и принёс вкусный торт.", "uz": "Dadam ishdan keldi va shirin tort olib keldi."},
    {"id": 16, "ru": "Я люблю рисовать яркими красками природу.", "uz": "Men tabiatni yorqin bo'yoqlar bilan chizishni yaxshi ko'raman."},
    {"id": 17, "ru": "На уроке русского языка мы пишем и говорим.", "uz": "Rus tili darsida biz yozamiz va gapiramiz."},
    {"id": 18, "ru": "Птицы вьют гнёзда на высоких деревьях.", "uz": "Qushlar baland daraxtlarda in qurishadi."},
    {"id": 19, "ru": "У меня новая синяя куртка и тёплая шапка.", "uz": "Menda yangi ko'k kurtka va issiq shapka bor."},
    {"id": 20, "ru": "Вечером мы все вместе смотрим добрый фильм.", "uz": "Kechqurun biz hammamiz birga yaxshi film tomosha qilamiz."},
    {"id": 21, "ru": "Это большой магазин. Там продают свежие фрукты.", "uz": "Bu katta do'kon. U yerda yangi mevalar sotiladi."},
    {"id": 22, "ru": "Мой брат учится в университете на инженера.", "uz": "Mening akam universitetda muhandislik yo'nalishida o'qiydi."},
    {"id": 23, "ru": "В лесу растут грибы, ягоды и высокие дубы.", "uz": "O'rmonda qo'ziqorinlar, rezavorlar va baland emanlar o'sadi."},
    {"id": 24, "ru": "Каждое утро я делаю зарядку, чтобы быть здоровым.", "uz": "Har kuni ertalab men sog'lom bo'lish uchun badantarbiya qilaman."},
    {"id": 25, "ru": "Собака громко лает, защищая свой дом.", "uz": "It o'z uyini himoya qilib baland ovozda huriydi."},
    {"id": 26, "ru": "Осенью листья на деревьях становятся жёлтыми.", "uz": "Kuzda daraxtlardagi barglar sariq rangga kiradi."},
    {"id": 27, "ru": "Девочка помогает маме поливать красивые цветы.", "uz": "Qizaloq onasiga chiroyli gullarni sug'orishda yordam bermoqda."},
    {"id": 28, "ru": "Мы едем на автобусе в центр нашего города.", "uz": "Biz avtobusda shahrimiz markaziga ketyapmiz."},
    {"id": 29, "ru": "Вода в реке чистая, прозрачная и прохладная.", "uz": "Daryodagi suv toza, shaffof va salqin."},
    {"id": 30, "ru": "Я знаю все тридцать три буквы русского алфавита.", "uz": "Men rus alifbosidagi barcha o'ttiz uchta harfni bilaman."},
    {"id": 31, "ru": "Этот мальчик быстро бегает и играет в футбол.", "uz": "Bu bola tez yuguradi va futbol o'ynaydi."},
    {"id": 32, "ru": "На стене висят большие часы и красивая картина.", "uz": "Devorda katta soat va chiroyli rasm osilib turibdi."},
    {"id": 33, "ru": "В библиотеке всегда тихо. Там много интересных книг.", "uz": "Kutubxonada doim jimjitlik. U yerda qiziqarli kitoblar ko'p."},
    {"id": 34, "ru": "Я люблю пить холодное молоко со сладким печеньем.", "uz": "Men sovuq sutni shirin pechenye bilan ichishni yaxshi ko'raman."},
    {"id": 35, "ru": "Моя бабушка вяжет тёплые носки к зиме.", "uz": "Mening buvim qishga issiq paypoqlar to'qiyapti."},
    {"id": 36, "ru": "Дедушка рассказывает нам мудрые и интересные сказки.", "uz": "Bobom bizga dono va qiziqarli ertaklar aytib beradi."},
    {"id": 37, "ru": "В саду распустились красные и белые розы.", "uz": "Bog'da qizil va oq atirgullar ochildi."},
    {"id": 38, "ru": "На небе ярко сияет луна и горят звёзды.", "uz": "Osmonda oy yorqin porlaydi va yulduzlar charaqlaydi."},
    {"id": 39, "ru": "Завтра у нас будет спортивный праздник в школе.", "uz": "Ertaga maktabimizda sport bayrami bo'ladi."},
    {"id": 40, "ru": "Я пишу письмо моему другу в другой город.", "uz": "Men boshqa shahardagi do'stimga xat yozyapman."},
    {"id": 41, "ru": "Рыбы плавают глубоко в чистом озере.", "uz": "Baliqlar toza ko'lning tubida suzadi."},
    {"id": 42, "ru": "Мы купили сладкий сочный арбуз на базаре.", "uz": "Biz bozordan shirin sersuv tarvuz sotib oldik."},
    {"id": 43, "ru": "Солнце встаёт на востоке и дарит всем тепло.", "uz": "Quyosh sharqdan chiqadi va hammaga iliqlik ulashadi."},
    {"id": 44, "ru": "Ученики внимательно слушают своего учителя.", "uz": "O'quvchilar o'qituvchilarini diqqat bilan tinglashmoqda."},
    {"id": 45, "ru": "Я умею красиво писать буквы в тетради.", "uz": "Men daftarga harflarni chiroyli qilib yoza olaman."},
    {"id": 46, "ru": "Весной природа просыпается и цветут деревья.", "uz": "Bahorda tabiat uyg'onadi va daraxtlar gullaydi."},
    {"id": 47, "ru": "Это сладкое мороженое очень вкусное.", "uz": "Bu shirin muzqaymoq juda mazali."},
    {"id": 48, "ru": "Дорога в школу занимает у меня десять минут.", "uz": "Maktabgacha bo'lgan yo'l mening o'n daqiqa vaqtimni oladi."},
    {"id": 49, "ru": "Русский язык очень богатый, красивый и звучный.", "uz": "Rus tili juda boy, chiroyli va jarangdor til."},
    {"id": 50, "ru": "Мы учимся каждый день и узнаём много нового!", "uz": "Biz har kuni o'qiymiz va juda ko'p yangi narsalarni bilib olamiz!"}
]

# =====================================================================
# 2. ASOSIY GRAFIK DASTUR SINF (TKINTER GUI)
# =====================================================================

class RussianLearningApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rus Tili 0 dan — Quljanova Shukurjon Zaribovna")
        self.geometry("1100x750")
        self.minsize(950, 650)
        self.configure(bg="#F0FDF4") # Ochiq nafis yashil fon

        # Ranglar palitrasi
        self.COLOR_GREEN = "#10B981"
        self.COLOR_BLUE = "#0284C7"
        self.COLOR_RED = "#EF4444"
        self.COLOR_YELLOW = "#F59E0B"
        self.COLOR_DARK = "#1E293B"

        self.setup_ui()

    def setup_ui(self):
        # 1. Header (Bosh qism)
        header_frame = tk.Frame(self, bg="white", height=75, highlightthickness=2, highlightbackground="#34D399")
        header_frame.pack(fill="x", side="top")

        title_lbl = tk.Label(
            header_frame, 
            text="Rus Tili 0 dan O'rganish Platformasi", 
            font=("Helvetica", 16, "bold"), 
            bg="white", 
            fg=self.COLOR_DARK
        )
        title_lbl.pack(anchor="w", padx=25, pady=(8, 0))

        author_lbl = tk.Label(
            header_frame, 
            text="Tuzuvchi va muallif: Quljanova Shukurjon Zaribovna", 
            font=("Helvetica", 10, "bold"), 
            bg="white", 
            fg="#6366F1"
        )
        author_lbl.pack(anchor="w", padx=25, pady=(0, 8))

        # 2. Notebook (Sahifalar boshqaruvi)
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#F0FDF4")
        style.configure("TNotebook.Tab", font=("Helvetica", 10, "bold"), padding=[14, 6])
        style.map("TNotebook.Tab", background=[("selected", self.COLOR_GREEN)], foreground=[("selected", "white")])

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=15, pady=10)

        # Tablar yaratish
        self.tab_alphabet = tk.Frame(self.notebook, bg="#F8FAFC")
        self.tab_write = tk.Frame(self.notebook, bg="#F8FAFC")
        self.tab_gender = tk.Frame(self.notebook, bg="#F8FAFC")
        self.tab_texts = tk.Frame(self.notebook, bg="#F8FAFC")
        self.tab_quiz = tk.Frame(self.notebook, bg="#F8FAFC")

        self.notebook.add(self.tab_alphabet, text=" 🔤 Rus Alifbosi (33) ")
        self.notebook.add(self.tab_write, text=" ✍️ Yozma Doska (Propis) ")
        self.notebook.add(self.tab_gender, text=" 🚻 Rodlar (Grammatika) ")
        self.notebook.add(self.tab_texts, text=" 📖 50 ta O'qish Matni ")
        self.notebook.add(self.tab_quiz, text=" 🏆 Viktorina (50 Test) ")

        # Bo'limlarni yuklash
        self.build_alphabet_tab()
        self.build_write_tab()
        self.build_gender_tab()
        self.build_texts_tab()
        self.build_quiz_tab()

        # 3. Footer
        footer_frame = tk.Frame(self, bg="white", height=35, highlightthickness=1, highlightbackground="#E2E8F0")
        footer_frame.pack(fill="x", side="bottom")

        ft_text = tk.Label(
            footer_frame, 
            text="© Quljanova Shukurjon Zaribovna — Rus tilini o'rganish kursi", 
            font=("Helvetica", 9, "bold"), 
            bg="white", 
            fg="#64748B"
        )
        ft_text.pack(pady=6)

    # =================================================================
    # TAB 1: ALIFBO
    # =================================================================
    def build_alphabet_tab(self):
        info_lbl = tk.Label(
            self.tab_alphabet, 
            text="Har bir harf ustiga bosib, uning to'g'ri ruscha talaffuzini eshiting:", 
            font=("Helvetica", 11, "bold"), 
            bg="#F8FAFC", 
            fg=self.COLOR_DARK
        )
        info_lbl.pack(pady=8)

        canvas = tk.Canvas(self.tab_alphabet, bg="#F8FAFC", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_alphabet, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#F8FAFC")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=20)
        scrollbar.pack(side="right", fill="y")

        cols = 6
        for idx, item in enumerate(LETTERS_DATA):
            r = idx // cols
            c = idx % cols

            card_bg = "#FEF2F2" if item["type"] == "Unli" else ("#F0FDF4" if item["type"] == "Undosh" else "#FEF3C7")
            border_color = "#F87171" if item["type"] == "Unli" else ("#34D399" if item["type"] == "Undosh" else "#FBBF24")

            frame = tk.Frame(scrollable_frame, bg=card_bg, highlightthickness=2, highlightbackground=border_color, width=135, height=125)
            frame.grid(row=r, column=c, padx=8, pady=8)
            frame.pack_propagate(False)

            char_lbl = tk.Label(frame, text=f"{item['char']}{item['small']}", font=("Helvetica", 22, "bold"), bg=card_bg, fg=self.COLOR_DARK)
            char_lbl.pack(pady=(6, 2))

            word_lbl = tk.Label(frame, text=item["word"], font=("Helvetica", 10, "bold"), bg=card_bg, fg=self.COLOR_BLUE)
            word_lbl.pack()

            uz_lbl = tk.Label(frame, text=item["uz"], font=("Helvetica", 8), bg=card_bg, fg="#64748B")
            uz_lbl.pack()

            btn = tk.Button(
                frame, 
                text="🔊 Tinglash", 
                font=("Helvetica", 8, "bold"), 
                bg="white", 
                fg=self.COLOR_GREEN,
                relief="flat",
                command=lambda w=item["word"], ch=item["char"]: speak_text(f"{ch}. {w}")
            )
            btn.pack(pady=(4, 0))

    # =================================================================
    # TAB 2: YOZMA HARFLAR DOSKASI
    # =================================================================
    def build_write_tab(self):
        top_ctrl = tk.Frame(self.tab_write, bg="#F8FAFC")
        top_ctrl.pack(fill="x", pady=10, padx=20)

        lbl = tk.Label(top_ctrl, text="Yozma shaklni mashq qilish uchun harfni tanlang:", font=("Helvetica", 11, "bold"), bg="#F8FAFC")
        lbl.pack(side="left", padx=5)

        self.selected_draw_char = tk.StringVar(value="Аа")
        char_combo = ttk.Combobox(
            top_ctrl, 
            textvariable=self.selected_draw_char, 
            values=[f"{item['char']}{item['small']} — {item['word']}" for item in LETTERS_DATA], 
            state="readonly", 
            width=22,
            font=("Helvetica", 10, "bold")
        )
        char_combo.pack(side="left", padx=10)
        char_combo.bind("<<ComboboxSelected>>", self.on_change_propis_letter)

        self.pen_color = self.COLOR_BLUE

        # Ranglar
        tk.Button(top_ctrl, text="Ko'k", bg="#2563EB", fg="white", font=("Helvetica", 9, "bold"), command=lambda: self.set_color("#2563EB")).pack(side="left", padx=3)
        tk.Button(top_ctrl, text="Yashil", bg="#10B981", fg="white", font=("Helvetica", 9, "bold"), command=lambda: self.set_color("#10B981")).pack(side="left", padx=3)
        tk.Button(top_ctrl, text="Qizil", bg="#EF4444", fg="white", font=("Helvetica", 9, "bold"), command=lambda: self.set_color("#EF4444")).pack(side="left", padx=3)
        tk.Button(top_ctrl, text="Qora", bg="#1E293B", fg="white", font=("Helvetica", 9, "bold"), command=lambda: self.set_color("#1E293B")).pack(side="left", padx=3)

        tk.Button(top_ctrl, text="🧹 Tozalash", bg="#FEE2E2", fg=self.COLOR_RED, font=("Helvetica", 9, "bold"), command=self.clear_board).pack(side="right", padx=5)
        tk.Button(top_ctrl, text="🔊 Eshitish", bg="#DCFCE7", fg=self.COLOR_GREEN, font=("Helvetica", 9, "bold"), command=self.speak_propis_letter).pack(side="right", padx=5)

        # Chizish Canvas
        self.draw_canvas = tk.Canvas(self.tab_write, bg="white", width=700, height=450, highlightthickness=3, highlightbackground="#FCD34D")
        self.draw_canvas.pack(pady=10)

        self.draw_canvas.bind("<Button-1>", self.start_draw)
        self.draw_canvas.bind("<B1-Motion>", self.do_draw)

        self.draw_notebook_lines()
        self.draw_guide_letter("Аа")

    def set_color(self, c):
        self.pen_color = c

    def draw_notebook_lines(self):
        # Maktab daftari qiya va gorizontal chiziqlari
        for y in range(40, 450, 45):
            self.draw_canvas.create_line(0, y, 700, y, fill="#E2E8F0", width=1)
        for x in range(0, 750, 60):
            self.draw_canvas.create_line(x, 0, x - 80, 450, fill="#F1F5F9", width=1)

    def draw_guide_letter(self, text):
        self.draw_canvas.create_text(
            350, 220, 
            text=text, 
            font=("Times New Roman", 150, "italic"), 
            fill="#E2E8F0", 
            tags="guide_letter"
        )

    def on_change_propis_letter(self, event):
        val = self.selected_draw_char.get().split()[0]
        self.clear_board()
        self.draw_guide_letter(val)

    def clear_board(self):
        self.draw_canvas.delete("all")
        self.draw_notebook_lines()
        val = self.selected_draw_char.get().split()[0]
        self.draw_guide_letter(val)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def do_draw(self, event):
        self.draw_canvas.create_line(
            self.last_x, self.last_y, event.x, event.y, 
            width=5, fill=self.pen_color, capstyle=tk.ROUND, smooth=True
        )
        self.last_x, self.last_y = event.x, event.y

    def speak_propis_letter(self):
        val = self.selected_draw_char.get().split()[0]
        speak_text(val)

    # =================================================================
    # TAB 3: RODLAR (GRAMMATIKA)
    # =================================================================
    def build_gender_tab(self):
        title = tk.Label(
            self.tab_gender, 
            text="Rus Tilida Otlarning 3 ta Rodi (Он / Она / Оно)", 
            font=("Helvetica", 14, "bold"), 
            bg="#F8FAFC", 
            fg=self.COLOR_DARK
        )
        title.pack(pady=12)

        main_box = tk.Frame(self.tab_gender, bg="#F8FAFC")
        main_box.pack(fill="both", expand=True, padx=20, pady=10)

        # 3 ta ustun
        genders = [
            {
                "title": "Мужской род (ОН)",
                "color": self.COLOR_BLUE,
                "bg": "#E0F2FE",
                "rules": "Qoida: Undosh harflar, -й yoki -ь bilan tugaydi.",
                "examples": [("Стол (Stol)", "Стол"), ("Дом (Uy)", "Дом"), ("Чай (Choy)", "Чай"), ("Словарь (Lug'at)", "Словарь"), ("Папа (Dada)", "Папа")]
            },
            {
                "title": "Женский род (ОНА)",
                "color": self.COLOR_RED,
                "bg": "#FEE2E2",
                "rules": "Qoida: -а, -я yoki -ь bilan tugaydi.",
                "examples": [("Книга (Kitob)", "Книга"), ("Мама (Ona)", "Мама"), ("Семья (Oila)", "Семья"), ("Тетрадь (Daftar)", "Тетрадь"), ("Ручка (Ruchka)", "Ручка")]
            },
            {
                "title": "Средний род (ОНО)",
                "color": self.COLOR_YELLOW,
                "bg": "#FEF3C7",
                "rules": "Qoida: -о, -е, -ё yoki -мя bilan tugaydi.",
                "examples": [("Окно (Deraza)", "Окно"), ("Море (Dengiz)", "Море"), ("Письмо (Xat)", "Письмо"), ("Имя (Ism)", "Имя"), ("Время (Vaqt)", "Время")]
            }
        ]

        for idx, g in enumerate(genders):
            col_frame = tk.Frame(main_box, bg="white", highlightthickness=2, highlightbackground=g["color"])
            col_frame.grid(row=0, column=idx, sticky="nsew", padx=10, pady=5)
            main_box.grid_columnconfigure(idx, weight=1)

            t_lbl = tk.Label(col_frame, text=g["title"], font=("Helvetica", 12, "bold"), bg=g["bg"], fg=g["color"], pady=8)
            t_lbl.pack(fill="x")

            r_lbl = tk.Label(col_frame, text=g["rules"], font=("Helvetica", 9, "italic"), bg="white", fg="#475569", wraplength=250, pady=8)
            r_lbl.pack(padx=10)

            ex_title = tk.Label(col_frame, text="Misollar (Tinglash uchun bosing):", font=("Helvetica", 9, "bold"), bg="white", fg=self.COLOR_DARK)
            ex_title.pack(anchor="w", padx=15, pady=(10, 5))

            for text_uz, text_ru in g["examples"]:
                btn = tk.Button(
                    col_frame, 
                    text=f"🔊 {text_uz}", 
                    font=("Helvetica", 9), 
                    bg=g["bg"], 
                    relief="flat", 
                    anchor="w",
                    command=lambda r=text_ru: speak_text(r)
                )
                btn.pack(fill="x", padx=15, pady=3)

    # =================================================================
    # TAB 4: 50 TA MATN
    # =================================================================
    def build_texts_tab(self):
        top_bar = tk.Frame(self.tab_texts, bg="#F8FAFC")
        top_bar.pack(fill="x", pady=10, padx=20)

        lbl = tk.Label(top_bar, text="50 ta Kichik O'qish Matni va Parallel Tarjimasi:", font=("Helvetica", 12, "bold"), bg="#F8FAFC")
        lbl.pack(side="left")

        # Scrollable ro'yxat
        canvas = tk.Canvas(self.tab_texts, bg="#F8FAFC", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tab_texts, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#F8FAFC")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=(0, 10))
        scrollbar.pack(side="right", fill="y", pady=(0, 10))

        for item in TEXTS_50:
            card = tk.Frame(scrollable_frame, bg="white", highlightthickness=1, highlightbackground="#E2E8F0", padx=15, pady=10)
            card.pack(fill="x", expand=True, pady=6)

            h_frame = tk.Frame(card, bg="white")
            h_frame.pack(fill="x")

            num_lbl = tk.Label(h_frame, text=f"#{item['id']}", font=("Helvetica", 10, "bold"), bg="#E0F2FE", fg=self.COLOR_BLUE, padx=8, pady=2)
            num_lbl.pack(side="left")

            sound_btn = tk.Button(
                h_frame, 
                text="🔊 Matnni Eshitish", 
                font=("Helvetica", 9, "bold"), 
                bg="#DCFCE7", 
                fg=self.COLOR_GREEN, 
                relief="flat",
                command=lambda t=item["ru"]: speak_text(t)
            )
            sound_btn.pack(side="right")

            ru_txt = tk.Label(card, text=item["ru"], font=("Helvetica", 11, "bold"), bg="white", fg=self.COLOR_DARK, wraplength=850, justify="left", pady=6)
            ru_txt.pack(anchor="w")

            uz_txt = tk.Label(card, text=f"Tarjimasi: {item['uz']}", font=("Helvetica", 10), bg="white", fg="#059669", wraplength=850, justify="left")
            uz_txt.pack(anchor="w")

    # =================================================================
    # TAB 5: 50 TA SAVOLLIK VIKTORINA (200 TA SO'Z BAZASI BILAN)
    # =================================================================
    def build_quiz_tab(self):
        self.quiz_questions = []
        self.quiz_curr_idx = 0
        self.quiz_score = 0
        self.quiz_correct_count = 0
        self.quiz_answered = False

        # Asosiy container
        self.quiz_container = tk.Frame(self.tab_quiz, bg="#F8FAFC")
        self.quiz_container.pack(fill="both", expand=True, padx=30, pady=15)

        # 1. Viktorina Savol Paneli
        self.quiz_play_frame = tk.Frame(self.quiz_container, bg="white", highlightthickness=2, highlightbackground="#FDA4AF", padx=30, pady=20)
        self.quiz_play_frame.pack(fill="both", expand=True)

        # Top Bar (Savol raqami va Ball)
        top_status = tk.Frame(self.quiz_play_frame, bg="white")
        top_status.pack(fill="x", pady=(0, 15))

        self.lbl_q_num = tk.Label(top_status, text="Savol: 1 / 50", font=("Helvetica", 12, "bold"), bg="white", fg=self.COLOR_RED)
        self.lbl_q_num.pack(side="left")

        self.lbl_q_score = tk.Label(top_status, text="To'plangan Ball: 0 / 100", font=("Helvetica", 12, "bold"), bg="white", fg=self.COLOR_GREEN)
        self.lbl_q_score.pack(side="right")

        # Savol markazi
        self.lbl_q_hint = tk.Label(self.quiz_play_frame, text="So'zning birinchi harfini toping!", font=("Helvetica", 11, "bold"), bg="#FFF1F2", fg=self.COLOR_RED, pady=4)
        self.lbl_q_hint.pack(fill="x", pady=5)

        self.lbl_q_word = tk.Label(self.quiz_play_frame, text="_ рбуз", font=("Helvetica", 28, "bold"), bg="white", fg=self.COLOR_DARK)
        self.lbl_q_word.pack(pady=10)

        self.lbl_q_uz = tk.Label(self.quiz_play_frame, text="Tarjimasi: Tarvuz", font=("Helvetica", 12, "bold"), bg="white", fg="#64748B")
        self.lbl_q_uz.pack()

        self.btn_q_listen = tk.Button(
            self.quiz_play_frame, 
            text="🔊 So'zni Ruscha Tinglash", 
            font=("Helvetica", 9, "bold"), 
            bg="#E0F2FE", 
            fg=self.COLOR_BLUE, 
            relief="flat", 
            command=self.play_current_quiz_audio
        )
        self.btn_q_listen.pack(pady=8)

        # 4 TA VARIANT TUGMALARI
        options_box = tk.Frame(self.quiz_play_frame, bg="white")
        options_box.pack(pady=15)

        self.opt_buttons = []
        for i in range(4):
            btn = tk.Button(
                options_box, 
                text=f"A", 
                font=("Helvetica", 16, "bold"), 
                width=14, 
                height=2, 
                bg="white", 
                fg=self.COLOR_DARK, 
                highlightthickness=2,
                highlightbackground="#E2E8F0",
                relief="flat",
                command=lambda idx=i: self.select_quiz_answer(idx)
            )
            r = i // 2
            c = i % 2
            btn.grid(row=r, column=c, padx=12, pady=10)
            self.opt_buttons.append(btn)

        # Feedback
        self.lbl_q_feedback = tk.Label(self.quiz_play_frame, text="", font=("Helvetica", 11, "bold"), bg="white")
        self.lbl_q_feedback.pack(pady=5)

        # Keyingi savolga o'tish tugmasi
        self.btn_q_next = tk.Button(
            self.quiz_play_frame, 
            text="Keyingi Savol ➜", 
            font=("Helvetica", 11, "bold"), 
            bg="#CBD5E1", 
            fg="white", 
            relief="flat", 
            state="disabled", 
            padx=15, 
            pady=6, 
            command=self.go_next_question
        )
        self.btn_q_next.pack(side="right", pady=5)

        # 2. Viktorina Yakuniy Natija Paneli (Dastlab yashirin)
        self.quiz_result_frame = tk.Frame(self.quiz_container, bg="white", highlightthickness=2, highlightbackground="#34D399", padx=30, pady=30)

        # Viktorinani boshlash
        self.start_quiz_session()

    def start_quiz_session(self):
        # 200 ta so'zdan tasodifiy 50 tasini tanlash
        self.quiz_questions = random.sample(QUIZ_WORDS_200, 50)
        self.quiz_curr_idx = 0
        self.quiz_score = 0
        self.quiz_correct_count = 0

        self.quiz_result_frame.pack_forget()
        self.quiz_play_frame.pack(fill="both", expand=True)

        self.load_quiz_question(0)

    def load_quiz_question(self, idx):
        self.quiz_answered = False
        item = self.quiz_questions[idx]

        self.lbl_q_num.config(text=f"Savol: {idx + 1} / 50")
        self.lbl_q_score.config(text=f"To'plangan Ball: {self.quiz_score} / 100")

        # So'zni birinchi harfisiz ko'rsatish
        hidden_word = f"_ {item['ru'][1:]}"
        self.lbl_q_word.config(text=hidden_word)
        self.lbl_q_uz.config(text=f"Tarjimasi: {item['uz']}")

        self.lbl_q_feedback.config(text="", fg="black")
        self.btn_q_next.config(state="disabled", bg="#CBD5E1")

        # 4 ta variant (1 ta to'g'ri, 3 ta xato)
        correct_char = item["char"]
        all_chars = list(set([w["char"] for w in QUIZ_WORDS_200 if w["char"] != correct_char]))
        wrong_chars = random.sample(all_chars, 3)
        self.current_options = [correct_char] + wrong_chars
        random.shuffle(self.current_options)

        prefixes = ["A) ", "B) ", "C) ", "D) "]
        for i, btn in enumerate(self.opt_buttons):
            btn.config(
                text=f"{prefixes[i]} {self.current_options[i]}", 
                bg="white", 
                fg=self.COLOR_DARK, 
                state="normal"
            )

    def play_current_quiz_audio(self):
        item = self.quiz_questions[self.quiz_curr_idx]
        speak_text(item["ru"])

    def select_quiz_answer(self, opt_idx):
        if self.quiz_answered:
            return
        self.quiz_answered = True

        selected_char = self.current_options[opt_idx]
        correct_char = self.quiz_questions[self.quiz_curr_idx]["char"]
        full_word = self.quiz_questions[self.quiz_curr_idx]["ru"]

        # Butun so'zni ochish
        self.lbl_q_word.config(text=full_word)

        # Barcha tugmalarni muzlatish
        for btn in self.opt_buttons:
            btn.config(state="disabled")

        if selected_char == correct_char:
            # TO'G'RI JAVOB: KATAK YASHIL BO'LADI
            self.opt_buttons[opt_idx].config(bg=self.COLOR_GREEN, fg="white")
            self.quiz_score += 2
            self.quiz_correct_count += 1
            self.lbl_q_score.config(text=f"To'plangan Ball: {self.quiz_score} / 100")
            self.lbl_q_feedback.config(text=f"✔ Barakalla! To'g'ri javob (+2 ball): {full_word}", fg=self.COLOR_GREEN)
            speak_text(f"Правильно! {full_word}")
        else:
            # XATO JAVOB: TANLANGAN KATAK QIZIL, TO'G'RISI YASHIL BO'LADI
            self.opt_buttons[opt_idx].config(bg=self.COLOR_RED, fg="white")
            for i, c in enumerate(self.current_options):
                if c == correct_char:
                    self.opt_buttons[i].config(bg=self.COLOR_GREEN, fg="white")
            self.lbl_q_feedback.config(text=f"✖ Noto'g'ri! To'g'ri javob: {full_word}", fg=self.COLOR_RED)
            speak_text(f"Неправильно. Это {full_word}")

        # Keyingi tugmani faollashtirish
        self.btn_q_next.config(state="normal", bg=self.COLOR_BLUE)

    def go_next_question(self):
        if self.quiz_curr_idx < 49:
            self.quiz_curr_idx += 1
            self.load_quiz_question(self.quiz_curr_idx)
        else:
            self.show_final_quiz_result()

    def show_final_quiz_result(self):
        self.quiz_play_frame.pack_forget()
        self.quiz_result_frame.pack(fill="both", expand=True)

        for widget in self.quiz_result_frame.winfo_children():
            widget.destroy()

        t_lbl = tk.Label(self.quiz_result_frame, text="🎉 Viktorina Muvaffaqiyatli Yakunlandi!", font=("Helvetica", 18, "bold"), bg="white", fg=self.COLOR_DARK)
        t_lbl.pack(pady=15)

        author_res = tk.Label(self.quiz_result_frame, text="Quljanova Shukurjon Zaribovna nomidagi test hisoboti", font=("Helvetica", 10, "bold"), bg="white", fg="#6366F1")
        author_res.pack()

        stats_frame = tk.Frame(self.quiz_result_frame, bg="#F8FAFC", highlightthickness=1, highlightbackground="#CBD5E1", padx=25, pady=15)
        stats_frame.pack(pady=20)

        tk.Label(stats_frame, text=f"Jami To'plangan Ball: {self.quiz_score} / 100", font=("Helvetica", 14, "bold"), bg="#F8FAFC", fg=self.COLOR_GREEN).pack(pady=3)
        tk.Label(stats_frame, text=f"To'g'ri javoblar: {self.quiz_correct_count} ta savol", font=("Helvetica", 11, "bold"), bg="#F8FAFC", fg=self.COLOR_BLUE).pack(pady=3)
        tk.Label(stats_frame, text=f"Xato javoblar: {50 - self.quiz_correct_count} ta savol", font=("Helvetica", 11, "bold"), bg="#F8FAFC", fg=self.COLOR_RED).pack(pady=3)
... 
...         # Baholash
...         if self.quiz_score >= 86:
...             grade_text = "Baho: 5 (A'lo) — Rus tili so'zlarini ajoyib o'zlashtirdingiz!"
...             grade_color = self.COLOR_GREEN
...         elif self.quiz_score >= 70:
...             grade_text = "Baho: 4 (Yaxshi) — Bilimlaringiz ancha mustahkam!"
...             grade_color = self.COLOR_BLUE
...         elif self.quiz_score >= 50:
...             grade_text = "Baho: 3 (Qoniqarli) — Yana bir oz takrorlash lozim."
...             grade_color = self.COLOR_YELLOW
...         else:
...             grade_text = "Baho: Qayta urinib ko'ring! Alifboni qaytadan o'rganing."
...             grade_color = self.COLOR_RED
... 
...         tk.Label(self.quiz_result_frame, text=grade_text, font=("Helvetica", 12, "bold"), bg="white", fg=grade_color).pack(pady=10)
... 
...         restart_btn = tk.Button(
...             self.quiz_result_frame, 
...             text="🔄 Yangi 50 ta Savol Bilan Qayta Boshlash", 
...             font=("Helvetica", 11, "bold"), 
...             bg=self.COLOR_GREEN, 
...             fg="white", 
...             relief="flat", 
...             padx=20, 
...             pady=10, 
...             command=self.start_quiz_session
...         )
...         restart_btn.pack(pady=15)
... 
... 
... # =====================================================================
... # 3. DASTURNI ISHGA TUSHIRISH
... # =====================================================================
... if __name__ == "__main__":
...     app = RussianLearningApp()
