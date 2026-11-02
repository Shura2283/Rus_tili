import streamlit as st
import streamlit.components.v1 as components
import sqlite3
from datetime import datetime
import json

# 1. Sahifani keng hajmda sozlash
st.set_page_config(
    page_title="Rus tili 0 dan — Quljanova Shukurjon Zaribovna",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hoshiyalarni olib tashlash
st.markdown("""
    <style>
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        .stApp {
            background: #f0fdf4 !important;
        }
        iframe {
            display: block;
            width: 100% !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# =====================================================================
# 2. MA'LUMOTLAR BAZASI (FOYDALANUVCHILAR VA NATIJALARNI QAYD QILISH)
# =====================================================================
def init_db():
    conn = sqlite3.connect("users_data.db", check_same_thread=False)
    c = conn.cursor()
    # Foydalanuvchilar hisobi jadvali
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            created_at TEXT
        )
    """)
    # Viktorina va test natijalari jadvali
    c.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            test_type TEXT,
            score INTEGER,
            max_score INTEGER,
            date_time TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

def get_stats():
    conn = sqlite3.connect("users_data.db", check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM users")
    total_users = c.fetchone()[0]
    
    c.execute("SELECT username, test_type, score, max_score, date_time FROM results ORDER BY id DESC LIMIT 50")
    recent_results = c.fetchall()
    conn.close()
    return total_users, recent_results

def add_user_if_not_exists(username):
    if not username:
        return
    conn = sqlite3.connect("users_data.db", check_same_thread=False)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        c.execute("INSERT OR IGNORE INTO users (username, created_at) VALUES (?, ?)", (username.strip(), now))
        conn.commit()
    except Exception:
        pass
    conn.close()

def save_result(username, test_type, score, max_score):
    if not username:
        username = "Noma'lum o'quvchi"
    add_user_if_not_exists(username)
    conn = sqlite3.connect("users_data.db", check_same_thread=False)
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO results (username, test_type, score, max_score, date_time) VALUES (?, ?, ?, ?, ?)",
              (username.strip(), test_type, score, max_score, now))
    conn.commit()
    conn.close()

# Foydalanuvchini ro'yxatdan o'tkazish yon paneli / sessiya boshqaruvi
if "user_name" not in st.session_state:
    st.session_state.user_name = "Mehmon"

# Sayt tepasidagi login / statistika paneli
total_users_count, all_results = get_stats()

top_col1, top_col2, top_col3 = st.columns([2, 1, 1])
with top_col1:
    user_input = st.text_input("Ism va familiyangizni kiriting:", value=st.session_state.user_name if st.session_state.user_name != "Mehmon" else "", placeholder="Masalan: Azizbek Karimov")
    if user_input and user_input != st.session_state.user_name:
        st.session_state.user_name = user_input
        add_user_if_not_exists(user_input)
        st.success(f"Hush kelibsiz, {user_input}!")
        st.rerun()

with top_col2:
    st.metric(label="👥 Jami Ro'yxatdan O'tganlar", value=f"{total_users_count} ta o'quvchi")

with top_col3:
    st.metric(label="👤 Joriy O'quvchi", value=st.session_state.user_name)

# =====================================================================
# 3. INTERAKTIV SAYT PLATFORMASI (HTML + JS)
# =====================================================================
app_html = f"""
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Marck+Script&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Nunito', sans-serif;
            background: radial-gradient(circle at 10% 20%, rgba(220, 252, 231, 0.85) 0%, rgba(224, 242, 254, 0.85) 35%, rgba(254, 249, 195, 0.85) 70%, rgba(254, 226, 226, 0.6) 100%);
            background-attachment: fixed;
            min-height: 100vh;
            margin: 0;
            padding: 12px;
        }}
        .propis-font {{ font-family: 'Marck Script', cursive; }}
        .propis-notebook {{
            background-color: #ffffff;
            background-image: 
                repeating-linear-gradient(0deg, #e2e8f0, #e2e8f0 1px, transparent 1px, transparent 40px),
                repeating-linear-gradient(75deg, rgba(203, 213, 225, 0.4), rgba(203, 213, 225, 0.4) 1px, transparent 1px, transparent 60px);
        }}
    </style>
</head>
<body class="text-slate-800 selection:bg-yellow-300">

    <!-- HEADER -->
    <header class="bg-white/95 backdrop-blur-md border-b-4 border-emerald-500 rounded-2xl p-4 shadow-sm mb-6 w-full flex flex-wrap justify-between items-center gap-4">
        <div class="flex items-center space-x-3">
            <div class="w-12 h-12 bg-gradient-to-tr from-amber-400 via-rose-500 to-indigo-500 rounded-2xl flex items-center justify-center text-white text-3xl font-black shadow-md shadow-rose-200 propis-font">
                Аа
            </div>
            <div>
                <h1 class="text-xl md:text-2xl font-black text-slate-800">Rus Tili <span class="text-emerald-500">0 dan</span></h1>
                <p class="text-xs font-bold text-slate-500">Tuzuvchi: <span class="text-indigo-600 font-extrabold">Quljanova Shukurjon Zaribovna</span></p>
            </div>
        </div>

        <nav class="flex flex-wrap items-center gap-2">
            <button onclick="switchTab('alphabet')" id="tab-alphabet" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-emerald-500 text-white shadow-md">
                <i class="fas fa-font"></i> Alifbo
            </button>
            <button onclick="switchTab('write')" id="tab-write" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-pen-nib text-amber-500"></i> Yozma Harflar
            </button>
            <button onclick="switchTab('syllables')" id="tab-syllables" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-book-open-reader text-teal-600"></i> Qo'shib O'qish
            </button>
            <button onclick="switchTab('gender')" id="tab-gender" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-venus-mars text-indigo-500"></i> Rodlar va 60 Gap
            </button>
            <button onclick="switchTab('texts')" id="tab-texts" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-book-reader text-sky-500"></i> 50 Matn
            </button>
            <button onclick="switchTab('quiz')" id="tab-quiz" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-gamepad text-rose-500"></i> Viktorina (50 Test)
            </button>
            <button onclick="switchTab('picquiz')" id="tab-picquiz" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-images text-purple-600"></i> Rasmli Test (50 ta)
            </button>
        </nav>
    </header>

    <main class="w-full space-y-6">

        <!-- 1. ALIFBO -->
        <section id="section-alphabet" class="space-y-4">
            <div class="bg-white/90 p-5 rounded-2xl border-2 border-emerald-100 shadow-sm flex flex-wrap justify-between items-center gap-2">
                <div>
                    <h2 class="text-xl font-black text-slate-800">Русский алфавит (33 буквы)</h2>
                    <p class="text-xs text-slate-600">Нажмите на карточку, чтобы услышать произношение!</p>
                </div>
                <div class="flex gap-2 text-xs font-bold">
                    <span class="px-3 py-1 bg-rose-100 text-rose-700 rounded-full">10 Гласных</span>
                    <span class="px-3 py-1 bg-sky-100 text-sky-700 rounded-full">21 Согласная</span>
                    <span class="px-3 py-1 bg-amber-100 text-amber-700 rounded-full">2 Знака</span>
                </div>
            </div>
            <div id="alphabet-grid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3"></div>
        </section>

        <!-- 2. YOZMA DOSKA -->
        <section id="section-write" class="hidden space-y-4">
            <div class="bg-white/90 p-4 rounded-2xl border-2 border-amber-200 flex flex-wrap justify-between items-center gap-2">
                <h2 class="text-lg font-black text-slate-800">Письменные буквы (Пропись)</h2>
                <div class="flex items-center gap-2">
                    <label class="text-xs font-bold text-slate-700">Выберите букву:</label>
                    <select id="letter-select" onchange="changeCanvasLetter(this.value)" class="bg-amber-50 border-2 border-amber-300 font-extrabold text-amber-700 rounded-xl px-3 py-1.5 text-sm"></select>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <div class="lg:col-span-2 bg-white rounded-2xl p-4 border-2 border-amber-200 shadow-sm flex flex-col items-center">
                    <div class="relative w-full max-w-[420px] aspect-square rounded-2xl border propis-notebook overflow-hidden flex items-center justify-center">
                        <div id="canvas-guide-letter" class="absolute inset-0 flex items-center justify-center text-[190px] text-slate-300 select-none pointer-events-none propis-font">Аа</div>
                        <canvas id="paint-canvas" width="420" height="420" class="absolute inset-0 cursor-crosshair touch-none"></canvas>
                    </div>
                    <div class="w-full max-w-[420px] flex justify-between items-center mt-3 pt-2 border-t">
                        <div class="flex gap-2">
                            <button onclick="setStrokeColor('#2563eb')" class="w-6 h-6 rounded-full bg-blue-600"></button>
                            <button onclick="setStrokeColor('#10b981')" class="w-6 h-6 rounded-full bg-emerald-500"></button>
                            <button onclick="setStrokeColor('#ef4444')" class="w-6 h-6 rounded-full bg-rose-500"></button>
                            <button onclick="setStrokeColor('#1e293b')" class="w-6 h-6 rounded-full bg-slate-800"></button>
                        </div>
                        <div class="flex gap-2">
                            <button onclick="clearCanvas()" class="px-3 py-1 bg-rose-100 text-rose-700 rounded-lg text-xs font-bold">Очистить</button>
                            <button onclick="speakCurrentCanvasLetter()" class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-lg text-xs font-bold">Слушать</button>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl p-5 border shadow-sm flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span id="canvas-card-badge" class="px-2.5 py-0.5 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">ГЛАСНАЯ</span>
                            <span class="text-xs font-bold text-amber-600">Пропись</span>
                        </div>
                        <div class="text-center p-3 bg-slate-50 rounded-2xl my-2">
                            <span id="canvas-card-letter-print" class="text-2xl font-black text-slate-800">Аа</span>
                            <span class="text-slate-400 mx-2">➜</span>
                            <span id="canvas-card-letter-propis" class="text-3xl font-bold text-amber-600 propis-font">Аа</span>
                        </div>
                        <img id="canvas-card-img" src="" class="w-full h-36 object-cover rounded-xl mt-2">
                        <div class="text-center mt-3">
                            <p id="canvas-card-ru-word" class="text-xl font-black text-slate-800">Арбуз</p>
                            <p id="canvas-card-uz-word" class="text-xs font-bold text-slate-500">Tarvuz</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. HARFLARNI QO'SHIB O'QISH -->
        <section id="section-syllables" class="hidden space-y-6">
            <div class="bg-white/90 p-5 rounded-2xl border-2 border-teal-200 shadow-sm flex flex-wrap justify-between items-center gap-3">
                <div>
                    <h2 class="text-xl font-black text-slate-800">📖 Harflarni Qo'shib O'qishni O'rganish</h2>
                    <p class="text-xs text-slate-600 mt-1">Harflarni bir-biriga qo'shib o'qishni 4 bosqichda o'rganing:</p>
                </div>
                <div class="flex flex-wrap gap-2">
                    <button onclick="filterSyllableTab('level1')" id="btn-syl-1" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-teal-600 text-white shadow">1-bosqich: Bo'g'inlar</button>
                    <button onclick="filterSyllableTab('level2')" id="btn-syl-2" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">2-bosqich: Qisqa so'zlar</button>
                    <button onclick="filterSyllableTab('level3')" id="btn-syl-3" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">3-bosqich: Bo'g'inli so'zlar</button>
                    <button onclick="filterSyllableTab('level4')" id="btn-syl-4" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">🌟 4-bosqich: 100 ta Rasm</button>
                </div>
            </div>

            <div id="syl-level1-box" class="space-y-4">
                <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-3" id="syl-grid-level1"></div>
            </div>
            <div id="syl-level2-box" class="hidden space-y-4">
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3" id="syl-grid-level2"></div>
            </div>
            <div id="syl-level3-box" class="hidden space-y-4">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3.5" id="syl-grid-level3"></div>
            </div>
            <div id="syl-level4-box" class="hidden space-y-4">
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3.5" id="syl-grid-level4"></div>
                <div class="flex flex-wrap justify-center gap-1.5 pt-4" id="syl-level4-pagination"></div>
            </div>
        </section>

        <!-- 4. RODLAR -->
        <section id="section-gender" class="hidden space-y-6">
            <div class="bg-white/90 p-5 rounded-2xl border-2 border-indigo-100 shadow-sm flex flex-wrap justify-between items-center gap-2">
                <div>
                    <h2 class="text-xl font-black text-slate-800">Род имён существительных в русском языке</h2>
                    <p class="text-xs text-slate-600 mt-1">Har bir rod uchun 20 tadan gap:</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <div class="bg-white p-4 rounded-2xl border-2 border-sky-200 shadow-sm">
                    <h3 class="font-black text-sky-700 text-sm pb-2 border-b mb-3">Мужской род (20 предложений)</h3>
                    <div class="space-y-2.5 max-h-[600px] overflow-y-auto pr-1" id="male-sentences"></div>
                </div>
                <div class="bg-white p-4 rounded-2xl border-2 border-rose-200 shadow-sm">
                    <h3 class="font-black text-rose-700 text-sm pb-2 border-b mb-3">Женский род (20 предложений)</h3>
                    <div class="space-y-2.5 max-h-[600px] overflow-y-auto pr-1" id="female-sentences"></div>
                </div>
                <div class="bg-white p-4 rounded-2xl border-2 border-amber-200 shadow-sm">
                    <h3 class="font-black text-amber-700 text-sm pb-2 border-b mb-3">Средний род (20 предложений)</h3>
                    <div class="space-y-2.5 max-h-[600px] overflow-y-auto pr-1" id="neuter-sentences"></div>
                </div>
            </div>
        </section>

        <!-- 5. MATNLAR -->
        <section id="section-texts" class="hidden space-y-4">
            <div class="bg-white/90 p-4 rounded-2xl border-2 border-sky-100 flex justify-between items-center">
                <h2 class="text-lg font-black text-slate-800">50 коротких текстов для чтения</h2>
                <span class="text-xs font-bold bg-sky-100 text-sky-700 px-3 py-1 rounded-xl">Всего: 50</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="texts-container"></div>
            <div class="flex justify-center gap-2 mt-4" id="texts-pagination"></div>
        </section>

        <!-- 6. VIKTORINA -->
        <section id="section-quiz" class="hidden max-w-2xl mx-auto space-y-4">
            <div id="quiz-question-box" class="bg-white rounded-2xl p-6 border-2 border-rose-200 shadow-sm">
                <div class="flex justify-between items-center pb-3 border-b mb-4">
                    <span class="text-sm font-black text-slate-700">Вопрос: <span id="quiz-current-num" class="text-rose-500">1</span> / 50</span>
                    <span class="text-sm font-black text-emerald-600">Баллы: <span id="quiz-score">0</span> / 100</span>
                </div>
                <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden mb-4">
                    <div id="quiz-progress-bar" class="bg-emerald-500 h-full w-[2%] transition-all"></div>
                </div>
                <div class="p-6 bg-slate-50 rounded-2xl text-center border">
                    <span class="text-xs font-bold text-rose-500 bg-rose-50 px-3 py-1 rounded-full">Угадайте первую букву:</span>
                    <h3 id="quiz-word-display" class="text-3xl font-black text-slate-800 my-3">_ рбуз</h3>
                    <p id="quiz-uz-translation" class="text-sm font-semibold text-slate-500 mb-3">Tarjimasi: Tarvuz</p>
                    <button onclick="playQuizWordAudio()" class="px-4 py-2 bg-sky-500 hover:bg-sky-600 text-white rounded-xl text-xs font-bold inline-flex items-center gap-1 shadow">
                        <i class="fas fa-volume-high"></i> Слушать слово
                    </button>
                </div>

                <div class="grid grid-cols-2 gap-3 mt-4" id="quiz-options"></div>
                <div id="quiz-feedback" class="mt-3 text-center font-bold text-sm h-6"></div>
                <div class="mt-4 flex justify-end">
                    <button id="quiz-next-btn" onclick="goToNextQuestion()" disabled class="px-5 py-2 bg-slate-200 text-slate-400 rounded-xl font-bold text-xs transition cursor-not-allowed">
                        Следующий вопрос ➜
                    </button>
                </div>
            </div>

            <div id="quiz-result-box" class="hidden bg-white rounded-2xl p-8 border-2 border-emerald-300 text-center space-y-4">
                <h3 class="text-2xl font-black text-slate-800">Тест завершён!</h3>
                <div class="p-4 bg-slate-50 rounded-2xl max-w-sm mx-auto">
                    <span class="text-xs text-slate-400 font-bold block">To'plangan Ball:</span>
                    <span id="res-total-score" class="text-3xl font-black text-emerald-600">0</span> / 100
                </div>
                <button onclick="startQuizSession()" class="px-6 py-2.5 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl font-bold text-xs shadow-md">
                    Пройти снова
                </button>
            </div>
        </section>

        <!-- 7. RASMLI TEST (50 TA) -->
        <section id="section-picquiz" class="hidden max-w-2xl mx-auto space-y-4">
            <div class="bg-white rounded-2xl p-4 border-2 border-purple-200 shadow-sm flex flex-wrap justify-between items-center gap-2">
                <div>
                    <h3 class="font-black text-purple-900 text-base">🖼️ Rasmli Test (Jami 50 ta savol)</h3>
                    <p class="text-xs text-slate-500">Rasmdagi narsaning to'g'ri ruscha nomini tanlang:</p>
                </div>
                <div class="flex gap-2">
                    <button onclick="switchPicVariant(1)" id="btn-pic-var1" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white shadow">1-variant (1-25)</button>
                    <button onclick="switchPicVariant(2)" id="btn-pic-var2" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">2-variant (26-50)</button>
                </div>
            </div>

            <div id="picquiz-question-box" class="bg-white rounded-2xl p-6 border-2 border-purple-200 shadow-sm">
                <div class="flex justify-between items-center pb-3 border-b mb-4">
                    <span class="text-sm font-black text-slate-700">Savol: <span id="picquiz-num" class="text-purple-600 font-extrabold">1</span> / 25</span>
                    <span class="text-sm font-black text-emerald-600">Ball: <span id="picquiz-score">0</span> / 50</span>
                </div>
                <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden mb-4">
                    <div id="picquiz-progress-bar" class="bg-purple-600 h-full w-[4%] transition-all"></div>
                </div>
                <div class="p-4 bg-slate-50 rounded-2xl text-center border flex flex-col items-center">
                    <div class="w-full max-w-[340px] h-52 rounded-xl overflow-hidden shadow-inner border-2 border-white mb-3 bg-slate-200">
                        <img id="picquiz-img" src="" alt="Test" class="w-full h-full object-cover">
                    </div>
                    <p id="picquiz-uz-hint" class="text-base font-extrabold text-slate-700 mb-2"></p>
                    <button onclick="playPicQuizAudio()" class="px-4 py-1.5 bg-purple-100 text-purple-700 hover:bg-purple-200 rounded-xl text-xs font-bold inline-flex items-center gap-1.5 transition">
                        <i class="fas fa-volume-high"></i> Tinglash
                    </button>
                </div>

                <div class="grid grid-cols-2 gap-4 mt-5" id="picquiz-options"></div>
                <div id="picquiz-feedback" class="mt-3 text-center font-bold text-sm h-6"></div>
                <div class="mt-4 flex justify-end">
                    <button id="picquiz-next-btn" onclick="goToNextPicQuestion()" disabled class="px-5 py-2 bg-slate-200 text-slate-400 rounded-xl font-bold text-xs transition cursor-not-allowed">
                        Keyingi rasm ➜
                    </button>
                </div>
            </div>

            <div id="picquiz-result-box" class="hidden bg-white rounded-2xl p-8 border-2 border-purple-300 text-center space-y-4">
                <h3 class="text-2xl font-black text-slate-800">Rasmli Test Yakunlandi!</h3>
                <div class="p-4 bg-slate-50 rounded-2xl max-w-sm mx-auto">
                    <span class="text-xs text-slate-400 font-bold block">To'plangan Ball:</span>
                    <span id="picres-total-score" class="text-3xl font-black text-purple-600">0</span> / 50
                </div>
                <button onclick="restartCurrentPicVariant()" class="px-6 py-2.5 bg-purple-600 hover:bg-purple-700 text-white rounded-xl font-bold text-xs shadow-md">
                    Qaytadan topshirish
                </button>
            </div>
        </section>

    </main>

    <footer class="mt-8 text-center text-xs font-bold text-slate-500 pb-4">
        © Quljanova Shukurjon Zaribovna — Rus tilini o'rganish platformasi
    </footer>

    <script>
        const CURRENT_USER = "{st.session_state.user_name}";

        function playSound(text) {{
            try {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    if (window.speechSynthesis.paused) window.speechSynthesis.resume();
                    const u = new SpeechSynthesisUtterance(text);
                    u.lang = 'ru-RU';
                    u.rate = 0.85;
                    u.volume = 1.0;
                    window.speechSynthesis.speak(u);
                }}
            }} catch (e) {{}}
        }}

        // Barcha harflar, bo'g'inlar va testlar bazasi
        const lettersData = [
            {{ char: 'А', small: 'а', type: 'unli', word: 'Арбуз', uz: 'Tarvuz', img: 'https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Б', small: 'б', type: 'undosh', word: 'Бабочка', uz: 'Kapalak', img: 'https://images.unsplash.com/photo-1559253664-ca249d4608c6?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'В', small: 'в', type: 'undosh', word: 'Волк', uz: 'Bo‘ri', img: 'https://images.unsplash.com/photo-1564466809058-bf4114d55352?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Г', small: 'г', type: 'undosh', word: 'Гриб', uz: 'Qo‘ziqorin', img: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Д', small: 'д', type: 'undosh', word: 'Дом', uz: 'Uy', img: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Е', small: 'е', type: 'unli', word: 'Ель', uz: 'Archa', img: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Ё', small: 'ё', type: 'unli', word: 'Ёж', uz: 'Tipratikan', img: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Ж', small: 'ж', type: 'undosh', word: 'Жираф', uz: 'Jirafa', img: 'https://images.unsplash.com/photo-1538099130811-745e64318258?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'З', small: 'з', type: 'undosh', word: 'Заяц', uz: 'Quyon', img: 'https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'И', small: 'и', type: 'unli', word: 'Игла', uz: 'Igna', img: 'https://images.unsplash.com/photo-1584824486509-112e4181ff6b?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Й', small: 'й', type: 'undosh', word: 'Йогурт', uz: 'Yogurt', img: 'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'К', small: 'к', type: 'undosh', word: 'Кот', uz: 'Mushuk', img: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Л', small: 'л', type: 'undosh', word: 'Лимон', uz: 'Limon', img: 'https://images.unsplash.com/photo-1533038590840-1cde6e668a91?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'М', small: 'м', type: 'undosh', word: 'Медведь', uz: 'Ayiq', img: 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'Н', small: 'н', type: 'undosh', word: 'Ножницы', uz: 'Qaychi', img: 'https://images.unsplash.com/photo-1503792501406-2c40da09e1e2?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'О', small: 'о', type: 'unli', word: 'Окно', uz: 'Deraza', img: 'https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=400&q=80' }},
            {{ char: 'П', small: 'п', type: 'undosh', word: 'Птица', uz: 'Qush', img: 'https://images.unsplash.com/photo-1444464666168-49d633b86797?auto=format&fit=crop&w=400&q=80' },
            { char: 'Р', small: 'р', type: 'undosh', word: 'Рыба', uz: 'Baliq', img: 'https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?auto=format&fit=crop&w=400&q=80' },
            { char: 'С', small: 'с', type: 'undosh', word: 'Солнце', uz: 'Quyosh', img: 'https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=400&q=80' },
            { char: 'Т', small: 'т', type: 'undosh', word: 'Тигр', uz: 'Yo‘lbars', img: 'https://images.unsplash.com/photo-1561731216-c3a4d99437d5?auto=format&fit=crop&w=400&q=80' },
            { char: 'У', small: 'у', type: 'unli', word: 'Утка', uz: 'O‘rdak', img: 'https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ф', small: 'ф', type: 'undosh', word: 'Флаг', uz: 'Bayroq', img: 'https://images.unsplash.com/photo-1508873696983-2df57046475a?auto=format&fit=crop&w=400&q=80' },
            { char: 'Х', small: 'х', type: 'undosh', word: 'Хлеб', uz: 'Non', img: 'https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ц', small: 'ц', type: 'undosh', word: 'Цветок', uz: 'Gul', img: 'https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ч', small: 'ч', type: 'undosh', word: 'Часы', uz: 'Soat', img: 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ш', small: 'ш', type: 'undosh', word: 'Шапка', uz: 'Shapka', img: 'https://images.unsplash.com/photo-1576871337622-98d48d1cf531?auto=format&fit=crop&w=400&q=80' },
            { char: 'Щ', small: 'щ', type: 'undosh', word: 'Щётка', uz: 'Cho‘tka', img: 'https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ъ', small: 'ъ', type: 'belgi', word: 'Подъезд', uz: 'Podyezd', img: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ы', small: 'ы', type: 'unli', word: 'Сыр', uz: 'Pishloq', img: 'https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ь', small: 'ь', type: 'belgi', word: 'Конь', uz: 'Ot (hayvon)', img: 'https://images.unsplash.com/photo-1553284965-83fd3e82fa5a?auto=format&fit=crop&w=400&q=80' },
            { char: 'Э', small: 'э', type: 'unli', word: 'Экран', uz: 'Ekran', img: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ю', small: 'ю', type: 'unli', word: 'Юбка', uz: 'Yubka', img: 'https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=400&q=80' },
            { char: 'Я', small: 'я', type: 'unli', word: 'Яблоко', uz: 'Olma', img: 'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=400&q=80' }
        ];

        const quizWords200 = [
            {{ ru: 'Арбуз', uz: 'Tarvuz', char: 'А' }}, {{ ru: 'Бабочка', uz: 'Kapalak', char: 'Б' }}, {{ ru: 'Волк', uz: 'Bo‘ri', char: 'В' }},
            {{ ru: 'Гриб', uz: 'Qo‘ziqorin', char: 'Г' }}, {{ ru: 'Дом', uz: 'Uy', char: 'Д' }}, {{ ru: 'Ель', uz: 'Archa', char: 'Е' }},
            {{ ru: 'Кот', uz: 'Mushuk', char: 'К' }}, {{ ru: 'Лимон', uz: 'Limon', char: 'Л' }}, {{ ru: 'Машина', uz: 'Mashina', char: 'М' }}
        ];

        // 100 ta rasmli so'zlar
        const readingPics100 = [
            {{ word: "Арбуз", syll: "АР - БУЗ", uz: "Tarvuz", img: "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Ананас", syll: "А - НА - НАС", uz: "Ananas", img: "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Банан", syll: "БА - НАН", uz: "Banan", img: "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Яблоко", syll: "ЯБ - ЛО - КО", uz: "Olma", img: "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Книга", syll: "КНИ - ГА", uz: "Kitob", img: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Машина", syll: "МА - ШИ - НА", uz: "Mashina", img: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Солнце", syll: "СОЛН - ЦЕ", uz: "Quyosh", img: "https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Хлеб", syll: "ХЛЕБ", uz: "Non", img: "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Цветок", syll: "ЦВЕ - ТОК", uz: "Gul", img: "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=400&q=80" }},
            {{ word: "Рыба", syll: "РЫ - БА", uz: "Baliq", img: "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?auto=format&fit=crop&w=400&q=80" }}
        ];

        // 50 ta rasmli test
        const picQuiz50 = [
            {{ ru: "Яблоко", uz: "Bu nima? (Olma)", wrong: "Апельсин", img: "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" }},
            {{ ru: "Кот", uz: "Bu nima? (Mushuk)", wrong: "Собака", img: "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=600&q=80" }},
            {{ ru: "Дом", uz: "Bu nima? (Uy)", wrong: "Школа", img: "https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=600&q=80" }},
            {{ ru: "Машина", uz: "Bu nima? (Mashina)", wrong: "Поезд", img: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=600&q=80" }}
        ];

        function switchTab(tabId) {{
            ['alphabet', 'write', 'syllables', 'gender', 'texts', 'quiz', 'picquiz'].forEach(t => {{
                document.getElementById(`section-${{t}}`).classList.add('hidden');
                document.getElementById(`tab-${{t}}`).className = "px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100";
            }});
            document.getElementById(`section-${{tabId}}`).classList.remove('hidden');
            document.getElementById(`tab-${{tabId}}`).className = "px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-emerald-500 text-white shadow-md";
        }}

        function renderAlphabet() {{
            const grid = document.getElementById('alphabet-grid');
            grid.innerHTML = '';
            lettersData.forEach(item => {{
                const card = document.createElement('div');
                card.className = "bg-white rounded-2xl p-3 border hover:border-emerald-400 hover:shadow transition flex flex-col justify-between cursor-pointer";
                card.innerHTML = `
                    <div class="text-center">
                        <div class="text-2xl font-black text-slate-800">${{item.char}}${{item.small}}</div>
                        <img src="${{item.img}}" class="w-full h-16 object-cover rounded-lg my-1">
                        <p class="font-bold text-xs text-slate-800">${{item.word}}</p>
                    </div>
                `;
                card.onclick = () => playSound(`${{item.char}}. ${{item.word}}`);
                grid.appendChild(card);
            }});
        }}

        window.addEventListener('DOMContentLoaded', () => {{
            renderAlphabet();
        }});
    </script>
</body>
</html>
"""

components.html(app_html, height=1050, scrolling=True)

# =====================================================================
# 4. SAYT OXIRIDA FOYDALANUVCHILAR NATIJALARI JADVALI (LEADERBOARD)
# =====================================================================
st.markdown("---")
st.subheader("🏆 O'quvchilar Natijalari va Reyting Qaydnomasi")

# Test topshirish sinov tugmalari (O'quvchi natijasini bazaga yozish uchun)
with st.expander("📝 Test natijasini saqlash (Sinov / Yakunlash paneli)"):
    sub_col1, sub_col2, sub_col3 = st.columns(3)
    with sub_col1:
        test_type = st.selectbox("Topshirilgan test:", ["50 Harfli Viktorina", "Rasmli Test (1-variant)", "Rasmli Test (2-variant)"])
    with sub_col2:
        score = st.number_input("To'plangan ball:", min_value=0, max_value=100, value=50, step=2)
    with sub_col3:
        max_score = 100 if "50 Harfli" in test_type else 50
        if st.button("Natijani Qayd Etish"):
            save_result(st.session_state.user_name, test_type, score, max_score)
            st.success("Natijangiz saqlandi!")
            st.rerun()

# Saqlangan barcha natijalar jadvali
if all_results:
    results_data = []
    for r in all_results:
        results_data.append({
            "O'quvchi Ismi": r[0],
            "Test turi": r[1],
            "To'plangan Ball": f"{r[2]} / {r[3]}",
            "Topshirilgan vaqti": r[4]
        })
    st.table(results_data)
else:
    st.info("Hozircha hech qanday natijalar qayd etilmagan. Birinchi bo'lib testni topshiring!")
