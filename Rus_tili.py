import streamlit as st
import streamlit.components.v1 as components

# 1. Sahifani to'liq kenglikka sozlash
st.set_page_config(
    page_title="Rus tili 0 dan — Quljanova Shukurjon Zaribovna",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Hoshiyalarni olib tashlash
st.markdown("""
    <style>
        header {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        #MainMenu {visibility: hidden !important;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        .stApp {
            margin: 0 !important;
            padding: 0 !important;
            background: #f0fdf4 !important;
        }
        iframe {
            display: block;
            width: 100% !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. 100 ta rasmli o'qish bo'limi qo'shilgan veb-kod
app_html = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Marck+Script&family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; }
        body {
            font-family: 'Nunito', sans-serif;
            background: radial-gradient(circle at 10% 20%, rgba(220, 252, 231, 0.85) 0%, rgba(224, 242, 254, 0.85) 35%, rgba(254, 249, 195, 0.85) 70%, rgba(254, 226, 226, 0.6) 100%);
            background-attachment: fixed;
            min-height: 100vh;
            margin: 0;
            padding: 12px;
        }
        .propis-font { font-family: 'Marck Script', cursive; }
        .propis-notebook {
            background-color: #ffffff;
            background-image: 
                repeating-linear-gradient(0deg, #e2e8f0, #e2e8f0 1px, transparent 1px, transparent 40px),
                repeating-linear-gradient(75deg, rgba(203, 213, 225, 0.4), rgba(203, 213, 225, 0.4) 1px, transparent 1px, transparent 60px);
        }
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
                <i class="fas fa-book-open-reader text-teal-600"></i> Harflarni Qo'shib O'qish
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

        <!-- 3. HARFLARNI QO'SHIB O'QISH (4 TA BOSQICH, SHUNDAN 4-BOSQICH 100 TA RASMLI O'QISH) -->
        <section id="section-syllables" class="hidden space-y-6">
            <div class="bg-white/90 p-5 rounded-2xl border-2 border-teal-200 shadow-sm flex flex-wrap justify-between items-center gap-3">
                <div>
                    <h2 class="text-xl font-black text-slate-800">📖 Harflarni Qo'shib O'qishni O'rganish (Чтение по слогам)</h2>
                    <p class="text-xs text-slate-600 mt-1">Harflarni bir-biriga qo'shib o'qishni 4 ta bosqichda o'rganing. Istalgan so'z ustiga bosing!</p>
                </div>
                <div class="flex flex-wrap gap-2">
                    <button onclick="filterSyllableTab('level1')" id="btn-syl-1" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-teal-600 text-white shadow">
                        1-bosqich: Bo'g'inlar
                    </button>
                    <button onclick="filterSyllableTab('level2')" id="btn-syl-2" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">
                        2-bosqich: Qisqa so'zlar
                    </button>
                    <button onclick="filterSyllableTab('level3')" id="btn-syl-3" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">
                        3-bosqich: Bo'g'inli so'zlar
                    </button>
                    <button onclick="filterSyllableTab('level4')" id="btn-syl-4" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">
                        🌟 4-bosqich: 100 ta Rasmli So'z
                    </button>
                </div>
            </div>

            <!-- 1-BOSQICH -->
            <div id="syl-level1-box" class="space-y-4">
                <div class="bg-teal-50/80 p-4 rounded-2xl border border-teal-200 text-xs text-teal-900 font-bold">
                    💡 Qoida: Undoshga unli qo'shilganda bo'g'in hosil bo'ladi. M + A = MA.
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 lg:grid-cols-8 gap-3" id="syl-grid-level1"></div>
            </div>

            <!-- 2-BOSQICH -->
            <div id="syl-level2-box" class="hidden space-y-4">
                <div class="bg-sky-50/80 p-4 rounded-2xl border border-sky-200 text-xs text-sky-900 font-bold">
                    💡 Qoida: 2, 3 va 4 harfli eng sodda ruscha so'zlarni birgalikda o'qing:
                </div>
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3" id="syl-grid-level2"></div>
            </div>

            <!-- 3-BOSQICH -->
            <div id="syl-level3-box" class="hidden space-y-4">
                <div class="bg-amber-50/80 p-4 rounded-2xl border border-amber-200 text-xs text-amber-900 font-bold">
                    💡 Qoida: Bo'g'inlarni alohida talaffuz qilib, so'ng so'zga birlashtiring:
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3.5" id="syl-grid-level3"></div>
            </div>

            <!-- 4-BOSQICH: 100 TA RASMLI SO'Z (PAGINATION BILAN) -->
            <div id="syl-level4-box" class="hidden space-y-4">
                <div class="bg-purple-50/90 p-4 rounded-2xl border border-purple-200 flex flex-wrap justify-between items-center gap-2">
                    <p class="text-xs text-purple-900 font-extrabold">
                        📸 4-bosqich: 100 ta eng kerakli so'zni sifatli rasmlari va bo'g'inlari bilan o'qishni mashq qiling. Ovozini eshitish uchun bosing!
                    </p>
                    <span class="text-xs font-black text-purple-700 bg-purple-100 px-3 py-1 rounded-xl">Jami: 100 ta so'z</span>
                </div>

                <!-- 100 ta rasmli kartochkalar konteyneri -->
                <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3.5" id="syl-grid-level4"></div>

                <!-- Sahifalash tugmalari (10 tadan 10 ta sahifa) -->
                <div class="flex flex-wrap justify-center gap-1.5 pt-4" id="syl-level4-pagination"></div>
            </div>
        </section>

        <!-- 4. RODLAR -->
        <section id="section-gender" class="hidden space-y-6">
            <div class="bg-white/90 p-5 rounded-2xl border-2 border-indigo-100 shadow-sm flex flex-wrap justify-between items-center gap-2">
                <div>
                    <h2 class="text-xl font-black text-slate-800">Род имён существительных в русском языке</h2>
                    <p class="text-xs text-slate-600 mt-1">Правила, окончания и по 20 озвученных примеров предложений для каждого рода:</p>
                </div>
                <div class="text-xs font-bold bg-indigo-50 text-indigo-700 px-3.5 py-2 rounded-xl border border-indigo-100">
                    Вопросы: <span class="font-extrabold">Он мой? / Она моя? / Оно моё?</span>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-white p-5 rounded-2xl border-t-8 border-sky-500 border shadow-sm">
                    <h3 class="text-lg font-black text-sky-600 mb-1 flex items-center justify-between">
                        <span>Мужской род (ОН)</span>
                        <span class="text-xs bg-sky-100 text-sky-700 px-2 py-0.5 rounded-lg">Этот / Мой</span>
                    </h3>
                    <p class="text-xs text-slate-500 mb-2">Оканчивается на согласный, <b>-й</b> или <b>-ь</b>.</p>
                </div>
                <div class="bg-white p-5 rounded-2xl border-t-8 border-rose-500 border shadow-sm">
                    <h3 class="text-lg font-black text-rose-600 mb-1 flex items-center justify-between">
                        <span>Женский род (ОНА)</span>
                        <span class="text-xs bg-rose-100 text-rose-700 px-2 py-0.5 rounded-lg">Эта / Моя</span>
                    </h3>
                    <p class="text-xs text-slate-500 mb-2">Оканчивается на <b>-а</b>, <b>-я</b> или <b>-ь</b>.</p>
                </div>
                <div class="bg-white p-5 rounded-2xl border-t-8 border-amber-500 border shadow-sm">
                    <h3 class="text-lg font-black text-amber-600 mb-1 flex items-center justify-between">
                        <span>Средний род (ОНО)</span>
                        <span class="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded-lg">Это / Моё</span>
                    </h3>
                    <p class="text-xs text-slate-500 mb-2">Оканчивается на <b>-о</b>, <b>-е</b>, <b>-ё</b> или <b>-мя</b>.</p>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <div class="bg-white p-4 rounded-2xl border-2 border-sky-200 shadow-sm">
                    <div class="flex items-center justify-between pb-3 border-b border-sky-100 mb-3">
                        <span class="font-black text-sky-700 text-sm"><i class="fas fa-mars"></i> Мужской род (20 предложений)</span>
                        <span class="text-[11px] font-bold text-sky-600 bg-sky-50 px-2 py-0.5 rounded-md">Он</span>
                    </div>
                    <div class="space-y-2.5 max-h-[650px] overflow-y-auto pr-1" id="male-sentences"></div>
                </div>

                <div class="bg-white p-4 rounded-2xl border-2 border-rose-200 shadow-sm">
                    <div class="flex items-center justify-between pb-3 border-b border-rose-100 mb-3">
                        <span class="font-black text-rose-700 text-sm"><i class="fas fa-venus"></i> Женский род (20 предложений)</span>
                        <span class="text-[11px] font-bold text-rose-600 bg-rose-50 px-2 py-0.5 rounded-md">Она</span>
                    </div>
                    <div class="space-y-2.5 max-h-[650px] overflow-y-auto pr-1" id="female-sentences"></div>
                </div>

                <div class="bg-white p-4 rounded-2xl border-2 border-amber-200 shadow-sm">
                    <div class="flex items-center justify-between pb-3 border-b border-amber-100 mb-3">
                        <span class="font-black text-amber-700 text-sm"><i class="fas fa-neuter"></i> Средний род (20 предложений)</span>
                        <span class="text-[11px] font-bold text-amber-600 bg-amber-50 px-2 py-0.5 rounded-md">Оно</span>
                    </div>
                    <div class="space-y-2.5 max-h-[650px] overflow-y-auto pr-1" id="neuter-sentences"></div>
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
                <div class="w-20 h-20 mx-auto rounded-full bg-emerald-500 text-white text-3xl flex items-center justify-center shadow-lg">
                    <i class="fas fa-award"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-800">Тест завершён!</h3>
                <div class="grid grid-cols-3 gap-2 max-w-sm mx-auto p-3 bg-slate-50 rounded-2xl">
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Баллы</span><span id="res-total-score" class="text-xl font-black text-emerald-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Правильно</span><span id="res-correct-count" class="text-xl font-black text-sky-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Ошибки</span><span id="res-wrong-count" class="text-xl font-black text-rose-500">0</span></div>
                </div>
                <div id="res-grade-badge" class="inline-block px-4 py-2 rounded-xl text-xs font-bold"></div>
                <div>
                    <button onclick="startQuizSession()" class="px-6 py-2.5 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl font-bold text-xs shadow-md">
                        Пройти снова
                    </button>
                </div>
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
                    <button onclick="switchPicVariant(1)" id="btn-pic-var1" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white shadow">
                        1-variant (1-25)
                    </button>
                    <button onclick="switchPicVariant(2)" id="btn-pic-var2" class="px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200">
                        2-variant (26-50)
                    </button>
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
                <div class="w-20 h-20 mx-auto rounded-full bg-purple-600 text-white text-3xl flex items-center justify-center shadow-lg shadow-purple-200">
                    <i class="fas fa-image"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-800">Rasmli Test Yakunlandi!</h3>
                <div class="grid grid-cols-3 gap-2 max-w-sm mx-auto p-3 bg-slate-50 rounded-2xl">
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Ball</span><span id="picres-total-score" class="text-xl font-black text-emerald-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">To'g'ri</span><span id="picres-correct-count" class="text-xl font-black text-purple-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Xato</span><span id="picres-wrong-count" class="text-xl font-black text-rose-500">0</span></div>
                </div>
                <div id="picres-grade-badge" class="inline-block px-4 py-2 rounded-xl text-xs font-bold"></div>
                <div>
                    <button onclick="restartCurrentPicVariant()" class="px-6 py-2.5 bg-purple-600 hover:bg-purple-700 text-white rounded-xl font-bold text-xs shadow-md">
                        Qaytadan topshirish
                    </button>
                </div>
            </div>
        </section>

    </main>

    <footer class="mt-8 text-center text-xs font-bold text-slate-500 pb-4">
        © Quljanova Shukurjon Zaribovna — Rus tilini o'rganish platformasi
    </footer>

    <script>
        function playSound(text) {
            try {
                if ('speechSynthesis' in window) {
                    window.speechSynthesis.cancel();
                    if (window.speechSynthesis.paused) window.speechSynthesis.resume();
                    const u = new SpeechSynthesisUtterance(text);
                    u.lang = 'ru-RU';
                    u.rate = 0.85;
                    u.volume = 1.0;
                    window.speechSynthesis.speak(u);
                }
            } catch (e) {
                console.error("Audio xatosi:", e);
            }
        }

        // ========================================================
        // 1-3 BOSQICHLAR: BO'G'INLAR VA SO'ZLAR
        // ========================================================
        const syllablesLevel1 = [
            { syl: "МА", uz: "M + A" }, { syl: "ПА", uz: "P + A" }, { syl: "БА", uz: "B + A" }, { syl: "ДА", uz: "D + A" },
            { syl: "ТА", uz: "T + A" }, { syl: "НА", uz: "N + A" }, { syl: "РА", uz: "R + A" }, { syl: "СА", uz: "S + A" },
            { syl: "МО", uz: "M + O" }, { syl: "ПО", uz: "P + O" }, { syl: "БО", uz: "B + O" }, { syl: "ДО", uz: "D + O" },
            { syl: "КО", uz: "K + O" }, { syl: "ТО", uz: "T + O" }, { syl: "НО", uz: "N + O" }, { syl: "РО", uz: "R + O" },
            { syl: "МУ", uz: "M + U" }, { syl: "ПУ", uz: "P + U" }, { syl: "БУ", uz: "B + U" }, { syl: "ДУ", uz: "D + U" },
            { syl: "ЛУ", uz: "L + U" }, { syl: "РУ", uz: "R + U" }, { syl: "СУ", uz: "S + U" }, { syl: "ТУ", uz: "T + U" },
            { syl: "МИ", uz: "M + I" }, { syl: "ЛИ", uz: "L + I" }, { syl: "СИ", uz: "S + I" }, { syl: "ЗИ", uz: "Z + I" },
            { syl: "МЫ", uz: "M + Y" }, { syl: "БЫ", uz: "B + Y" }, { syl: "РЫ", uz: "R + Y" }, { syl: "СЫ", uz: "S + Y" }
        ];

        const syllablesLevel2 = [
            { word: "ОН", syll: "ОН", uz: "U (erkak)" }, { word: "ОНА", syll: "О-НА", uz: "U (ayol)" },
            { word: "ОНО", syll: "О-НО", uz: "U (o'rta)" }, { word: "МЫ", syll: "МЫ", uz: "Biz" },
            { word: "ВЫ", syll: "ВЫ", uz: "Siz" }, { word: "ДА", syll: "ДА", uz: "Ha" },
            { word: "НЕТ", syll: "НЕТ", uz: "Yo'q" }, { word: "ДОМ", syll: "ДОМ", uz: "Uy" },
            { word: "КОТ", syll: "КОТ", uz: "Mushuk" }, { word: "СЫР", syll: "СЫР", uz: "Pishloq" },
            { word: "САД", syll: "САД", uz: "Bog'" }, { word: "РОТ", syll: "РОТ", uz: "Og'iz" },
            { word: "НОС", syll: "НОС", uz: "Burun" }, { word: "ЛЕС", syll: "ЛЕС", uz: "O'rmon" },
            { word: "СОК", syll: "СОК", uz: "Sharbat" }, { word: "МАМА", syll: "МА-МА", uz: "Ona" },
            { word: "ПАПА", syll: "ПА-ПА", uz: "Dada" }, { word: "РОЗА", syll: "РО-ЗА", uz: "Atirgul" },
            { word: "КАША", syll: "КА-ША", uz: "Bo'tqa" }, { word: "ВОДА", syll: "ВО-ДА", uz: "Suv" },
            { word: "РЫБА", syll: "РЫ-БА", uz: "Baliq" }, { word: "РУКА", syll: "РУ-КА", uz: "Qo'l" },
            { word: "НОГА", syll: "НО-ГА", uz: "Oyoq" }, { word: "НЕБО", syll: "НЕ-БО", uz: "Osmon" },
            { word: "ЛУНА", syll: "ЛУ-НА", uz: "Oy" }
        ];

        const syllablesLevel3 = [
            { word: "МАШИНА", syll: "МА - ШИ - НА", uz: "Mashina" }, { word: "МОЛОКО", syll: "МО - ЛО - КО", uz: "Sut" },
            { word: "СОБАКА", syll: "СО - БА - КА", uz: "It" }, { word: "ДЕРЕВО", syll: "ДЕ - РЕ - ВО", uz: "Daraxt" },
            { word: "ЯБЛОКО", syll: "ЯБ - ЛО - КО", uz: "Olma" }, { word: "ШКОЛА", syll: "ШКО - ЛА", uz: "Maktab" },
            { word: "КНИГА", syll: "КНИ - ГА", uz: "Kitob" }, { word: "РУЧКА", syll: "РУЧ - КА", uz: "Ruchka" },
            { word: "ТЕТРАДЬ", syll: "ТЕТ - РАДЬ", uz: "Daftar" }, { word: "ЛИМОН", syll: "ЛИ - МОН", uz: "Limon" },
            { word: "АРБУЗ", syll: "АР - БУЗ", uz: "Tarvuz" }, { word: "БАНАН", syll: "БА - НАН", uz: "Banan" },
            { word: "ГОРОД", syll: "ГО - РОД", uz: "Shahar" }, { word: "УЛИЦА", syll: "У - ЛИ - ЦА", uz: "Ko'cha" },
            { word: "УЧЕНИК", syll: "У - ЧЕ - НИК", uz: "O'quvchi" }, { word: "УЧИТЕЛЬ", syll: "У - ЧИ - ТЕЛЬ", uz: "O'qituvchi" },
            { word: "ДЕВОЧКА", syll: "ДЕ - ВОЧ - КА", uz: "Qizaloq" }, { word: "МАЛЬЧИК", syll: "МАЛЬ - ЧИК", uz: "O'g'il bola" },
            { word: "ПОГОДА", syll: "ПО - ГО - ДА", uz: "Ob-havo" }, { word: "СОЛНЦЕ", syll: "СОЛН - ЦЕ", uz: "Quyosh" },
            { word: "ЦВЕТОК", syll: "ЦВЕ - ТОК", uz: "Gul" }, { word: "КАРАНДАШ", syll: "КА - РАН - ДАШ", uz: "Qalam" },
            { word: "КОМПЬЮТЕР", syll: "КОМ - ПЬЮ - ТЕР", uz: "Kompyuter" }, { word: "ТЕЛЕФОН", syll: "ТЕ - ЛЕ - ФОН", uz: "Telefon" }
        ];

        // ========================================================
        // 4-BOSQICH: 100 TA RASMLI O'QISH BAZASI (100 слов с фото)
        // ========================================================
        const readingPics100 = [
            { word: "Арбуз", syll: "АР - БУЗ", uz: "Tarvuz", img: "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=400&q=80" },
            { word: "Ананас", syll: "А - НА - НАС", uz: "Ananas", img: "https://images.unsplash.com/photo-1550258987-190a2d41a8ba?auto=format&fit=crop&w=400&q=80" },
            { word: "Апельсин", syll: "А - ПЕЛЬ - СИН", uz: "Apelsin", img: "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?auto=format&fit=crop&w=400&q=80" },
            { word: "Автобус", syll: "АВ - ТО - БУС", uz: "Avtobus", img: "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=400&q=80" },
            { word: "Бабочка", syll: "БА - БОЧ - КА", uz: "Kapalak", img: "https://images.unsplash.com/photo-1559253664-ca249d4608c6?auto=format&fit=crop&w=400&q=80" },
            { word: "Банан", syll: "БА - НАН", uz: "Banan", img: "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=400&q=80" },
            { word: "Волк", syll: "ВОЛК", uz: "Bo'ri", img: "https://images.unsplash.com/photo-1564466809058-bf4114d55352?auto=format&fit=crop&w=400&q=80" },
            { word: "Вода", syll: "ВО - ДА", uz: "Suv", img: "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?auto=format&fit=crop&w=400&q=80" },
            { word: "Велосипед", syll: "ВЕ - ЛО - СИ - ПЕД", uz: "Velosiped", img: "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=400&q=80" },
            { word: "Гриб", syll: "ГРИБ", uz: "Qo'ziqorin", img: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=400&q=80" },

            { word: "Груша", syll: "ГРУ - ША", uz: "Nok", img: "https://images.unsplash.com/photo-1615484477778-ca3b783256fd?auto=format&fit=crop&w=400&q=80" },
            { word: "Гора", syll: "ГО - РА", uz: "Tog'", img: "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=400&q=80" },
            { word: "Город", syll: "ГО - РОД", uz: "Shahar", img: "https://images.unsplash.com/photo-1477959858617-67f30bc75b82?auto=format&fit=crop&w=400&q=80" },
            { word: "Дом", syll: "ДОМ", uz: "Uy", img: "https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=400&q=80" },
            { word: "Дверь", syll: "ДВЕРЬ", uz: "Eshik", img: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=400&q=80" },
            { word: "Дерево", syll: "ДЕ - РЕ - ВО", uz: "Daraxt", img: "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=400&q=80" },
            { word: "Дождь", syll: "ДОЖДЬ", uz: "Yomg'ir", img: "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?auto=format&fit=crop&w=400&q=80" },
            { word: "Ель", syll: "ЕЛЬ", uz: "Archa", img: "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=400&q=80" },
            { word: "Ёж", syll: "ЁЖ", uz: "Tipratikan", img: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=400&q=80" },
            { word: "Жираф", syll: "ЖИ - РАФ", uz: "Jirafa", img: "https://images.unsplash.com/photo-1538099130811-745e64318258?auto=format&fit=crop&w=400&q=80" },

            { word: "Заяц", syll: "ЗА - ЯЦ", uz: "Quyon", img: "https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?auto=format&fit=crop&w=400&q=80" },
            { word: "Звезда", syll: "ЗВЕЗ - ДА", uz: "Yulduz", img: "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=400&q=80" },
            { word: "Зонт", syll: "ЗОНТ", uz: "Soyabon", img: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=400&q=80" },
            { word: "Зима", syll: "ЗИ - МА", uz: "Qish", img: "https://images.unsplash.com/photo-1517299321609-52687d1bc55a?auto=format&fit=crop&w=400&q=80" },
            { word: "Игла", syll: "ИГ - ЛА", uz: "Igna", img: "https://images.unsplash.com/photo-1584824486509-112e4181ff6b?auto=format&fit=crop&w=400&q=80" },
            { word: "Йогурт", syll: "ЙО - ГУРТ", uz: "Yogurt", img: "https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=400&q=80" },
            { word: "Кот", syll: "КОТ", uz: "Mushuk", img: "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80" },
            { word: "Книга", syll: "КНИ - ГА", uz: "Kitob", img: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=400&q=80" },
            { word: "Карандаш", syll: "КА - РАН - ДАШ", uz: "Qalam", img: "https://images.unsplash.com/photo-1585336261026-77894a861616?auto=format&fit=crop&w=400&q=80" },
            { word: "Корова", syll: "КО - РО - ВА", uz: "Sigir", img: "https://images.unsplash.com/photo-1546445317-29f4545e9d53?auto=format&fit=crop&w=400&q=80" },

            { word: "Компьютер", syll: "КОМ - ПЬЮ - ТЕР", uz: "Kompyuter", img: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80" },
            { word: "Корабль", syll: "КО - РАБЛЬ", uz: "Kema", img: "https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=400&q=80" },
            { word: "Лимон", syll: "ЛИ - МОН", uz: "Limon", img: "https://images.unsplash.com/photo-1533038590840-1cde6e668a91?auto=format&fit=crop&w=400&q=80" },
            { word: "Лес", syll: "ЛЕС", uz: "O'rmon", img: "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=400&q=80" },
            { word: "Луна", syll: "ЛУ - НА", uz: "Oy", img: "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=400&q=80" },
            { word: "Лошадь", syll: "ЛО - ШАДЬ", uz: "Ot (hayvon)", img: "https://images.unsplash.com/photo-1553284965-83fd3e82fa5a?auto=format&fit=crop&w=400&q=80" },
            { word: "Ложка", syll: "ЛОЖ - КА", uz: "Qoshiq", img: "https://images.unsplash.com/photo-1584269600519-112d071b35e6?auto=format&fit=crop&w=400&q=80" },
            { word: "Лук", syll: "ЛУК", uz: "Piyoz", img: "https://images.unsplash.com/photo-1580201092675-a0a6a6cafbb1?auto=format&fit=crop&w=400&q=80" },
            { word: "Медведь", syll: "МЕД - ВЕДЬ", uz: "Ayiq", img: "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?auto=format&fit=crop&w=400&q=80" },
            { word: "Машина", syll: "МА - ШИ - НА", uz: "Mashina", img: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=400&q=80" },

            { word: "Молоко", syll: "МО - ЛО - КО", uz: "Sut", img: "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=400&q=80" },
            { word: "Море", syll: "МО - РЕ", uz: "Dengiz", img: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=400&q=80" },
            { word: "Мыло", syll: "МЫ - ЛО", uz: "Sovun", img: "https://images.unsplash.com/photo-1607006314170-07e05ebf3fae?auto=format&fit=crop&w=400&q=80" },
            { word: "Морковь", syll: "МОР - КОВЬ", uz: "Sabzi", img: "https://images.unsplash.com/photo-1598170845058-32b9d6a5c317?auto=format&fit=crop&w=400&q=80" },
            { word: "Мёд", syll: "МЁД", uz: "Asal", img: "https://images.unsplash.com/photo-1587049352847-4a222e784d38?auto=format&fit=crop&w=400&q=80" },
            { word: "Малина", syll: "МА - ЛИ - НА", uz: "Malina", img: "https://images.unsplash.com/photo-1577069808021-5a52cf1dfbf9?auto=format&fit=crop&w=400&q=80" },
            { word: "Мясо", syll: "МЯ - СО", uz: "Go'sht", img: "https://images.unsplash.com/photo-1603048588665-791ca8aea617?auto=format&fit=crop&w=400&q=80" },
            { word: "Мост", syll: "МОСТ", uz: "Ko'prik", img: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=400&q=80" },
            { word: "Метро", syll: "МЕТ - РО", uz: "Metro", img: "https://images.unsplash.com/photo-1519501025264-65ba15a82390?auto=format&fit=crop&w=400&q=80" },
            { word: "Ножницы", syll: "НОЖ - НИ - ЦЫ", uz: "Qaychi", img: "https://images.unsplash.com/photo-1503792501406-2c40da09e1e2?auto=format&fit=crop&w=400&q=80" },

            { word: "Ночь", syll: "НОЧЬ", uz: "Tun", img: "https://images.unsplash.com/photo-1509114397022-ed747cca3f65?auto=format&fit=crop&w=400&q=80" },
            { word: "Небо", syll: "НЕ - БО", uz: "Osmon", img: "https://images.unsplash.com/photo-1513002749550-c59d786b8e6c?auto=format&fit=crop&w=400&q=80" },
            { word: "Нож", syll: "НОЖ", uz: "Pichoq", img: "https://images.unsplash.com/photo-1593618998160-e34014e67546?auto=format&fit=crop&w=400&q=80" },
            { word: "Носки", syll: "НОС - КИ", uz: "Paypoqlar", img: "https://images.unsplash.com/photo-1582966770380-457cf68c4a52?auto=format&fit=crop&w=400&q=80" },
            { word: "Окно", syll: "ОК - НО", uz: "Deraza", img: "https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=400&q=80" },
            { word: "Огонь", syll: "О - ГОНЬ", uz: "Olov", img: "https://images.unsplash.com/photo-1527489377706-5bf97e608852?auto=format&fit=crop&w=400&q=80" },
            { word: "Озеро", syll: "О - ЗЕ - РО", uz: "Ko'l", img: "https://images.unsplash.com/photo-1439066615861-d1af74d74000?auto=format&fit=crop&w=400&q=80" },
            { word: "Осень", syll: "О - СЕНЬ", uz: "Kuz", img: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=400&q=80" },
            { word: "Очки", syll: "ОЧ - КИ", uz: "Ko'zoynak", img: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=400&q=80" },
            { word: "Огурец", syll: "О - ГУ - РЕЦ", uz: "Bodring", img: "https://images.unsplash.com/photo-1604977042946-1eecc30f269e?auto=format&fit=crop&w=400&q=80" },

            { word: "Орех", syll: "О - РЕХ", uz: "Yong'oq", img: "https://images.unsplash.com/photo-1543208543-690c5861c8f1?auto=format&fit=crop&w=400&q=80" },
            { word: "Одеяло", syll: "О - ДЕ - Я - ЛО", uz: "Ko'rpa", img: "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=400&q=80" },
            { word: "Птица", syll: "ПТИ - ЦА", uz: "Qush", img: "https://images.unsplash.com/photo-1444464666168-49d633b86797?auto=format&fit=crop&w=400&q=80" },
            { word: "Письмо", syll: "ПИСЬ - МО", uz: "Xat", img: "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=400&q=80" },
            { word: "Поезд", syll: "ПО - ЕЗД", uz: "Poyezd", img: "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=400&q=80" },
            { word: "Поле", syll: "ПО - ЛЕ", uz: "Dala", img: "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=400&q=80" },
            { word: "Парк", syll: "ПАРК", uz: "Bog' / Park", img: "https://images.unsplash.com/photo-1519331379826-f10be5486c6f?auto=format&fit=crop&w=400&q=80" },
            { word: "Помидор", syll: "ПО - МИ - ДОР", uz: "Pomidor", img: "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=400&q=80" },
            { word: "Персик", syll: "ПЕР - СИК", uz: "Shaftoli", img: "https://images.unsplash.com/photo-1595126731133-489e92359dd4?auto=format&fit=crop&w=400&q=80" },
            { word: "Пальто", syll: "ПАЛЬ - ТО", uz: "Palto", img: "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?auto=format&fit=crop&w=400&q=80" },

            { word: "Подушка", syll: "ПО - ДУШ - КА", uz: "Yostiq", img: "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?auto=format&fit=crop&w=400&q=80" },
            { word: "Рыба", syll: "РЫ - БА", uz: "Baliq", img: "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?auto=format&fit=crop&w=400&q=80" },
            { word: "Ручка", syll: "РУЧ - КА", uz: "Ruchka", img: "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?auto=format&fit=crop&w=400&q=80" },
            { word: "Река", syll: "РЕ - КА", uz: "Daryo", img: "https://images.unsplash.com/photo-1437482078695-73f5ca6c96e2?auto=format&fit=crop&w=400&q=80" },
            { word: "Роза", syll: "РО - ЗА", uz: "Atirgul", img: "https://images.unsplash.com/photo-1559563458-527698bf5295?auto=format&fit=crop&w=400&q=80" },
            { word: "Солнце", syll: "СОЛН - ЦЕ", uz: "Quyosh", img: "https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=400&q=80" },
            { word: "Стол", syll: "СТОЛ", uz: "Stol", img: "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?auto=format&fit=crop&w=400&q=80" },
            { word: "Стул", syll: "СТУЛ", uz: "Stul", img: "https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&w=400&q=80" },
            { word: "Снег", syll: "СНЕГ", uz: "Qor", img: "https://images.unsplash.com/photo-1517299321609-52687d1bc55a?auto=format&fit=crop&w=400&q=80" },
            { word: "Собака", syll: "СО - БА - КА", uz: "It", img: "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80" },

            { word: "Сыр", syll: "СЫР", uz: "Pishloq", img: "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=400&q=80" },
            { word: "Сахар", syll: "СА - ХАР", uz: "Shakar", img: "https://images.unsplash.com/photo-1581441363689-1f3c3c414635?auto=format&fit=crop&w=400&q=80" },
            { word: "Соль", syll: "СОЛЬ", uz: "Tuz", img: "https://images.unsplash.com/photo-1518110925495-5fe2fda0442c?auto=format&fit=crop&w=400&q=80" },
            { word: "Суп", syll: "СУП", uz: "Sho'rva", img: "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=400&q=80" },
            { word: "Салат", syll: "СА - ЛАТ", uz: "Salat", img: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=400&q=80" },
            { word: "Слива", syll: "СЛИ - ВА", uz: "Olxo'ri", img: "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb?auto=format&fit=crop&w=400&q=80" },
            { word: "Самолёт", syll: "СА - МО - ЛЁТ", uz: "Samolyot", img: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=400&q=80" },
            { word: "Стадион", syll: "СТА - ДИ - ОН", uz: "Stadion", img: "https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&w=400&q=80" },
            { word: "Тигр", syll: "ТИГР", uz: "Yo'lbars", img: "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?auto=format&fit=crop&w=400&q=80" },
            { word: "Тетрадь", syll: "ТЕТ - РАДЬ", uz: "Daftar", img: "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=400&q=80" },

            { word: "Телефон", syll: "ТЕ - ЛЕ - ФОН", uz: "Telefon", img: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=400&q=80" },
            { word: "Тарелка", syll: "ТА - РЕЛ - КА", uz: "Tarelka", img: "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=400&q=80" },
            { word: "Трава", syll: "ТРА - ВА", uz: "O't / Maysa", img: "https://images.unsplash.com/photo-1533240332313-0db49b459ad6?auto=format&fit=crop&w=400&q=80" },
            { word: "Торт", syll: "ТОРТ", uz: "Tort", img: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=400&q=80" },
            { word: "Театр", syll: "ТЕ - АТР", uz: "Teatr", img: "https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?auto=format&fit=crop&w=400&q=80" },
            { word: "Утка", syll: "УТ - КА", uz: "O'rdak", img: "https://images.unsplash.com/photo-1555854877-bab0e564b8d5?auto=format&fit=crop&w=400&q=80" },
            { word: "Улица", syll: "У - ЛИ - ЦА", uz: "Ko'cha", img: "https://images.unsplash.com/photo-1514924013411-cbf25faa35bb?auto=format&fit=crop&w=400&q=80" },
            { word: "Флаг", syll: "ФЛАГ", uz: "Bayroq", img: "https://images.unsplash.com/photo-1508873696983-2df57046475a?auto=format&fit=crop&w=400&q=80" },
            { word: "Фонарь", syll: "ФО - НАРЬ", uz: "Fonar", img: "https://images.unsplash.com/photo-1517457373958-b7bdd4587205?auto=format&fit=crop&w=400&q=80" },
            { word: "Футбол", syll: "ФУТ - БОЛ", uz: "Futbol", img: "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=400&q=80" },

            { word: "Хлеб", syll: "ХЛЕБ", uz: "Non", img: "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=400&q=80" },
            { word: "Цветок", syll: "ЦВЕ - ТОК", uz: "Gul", img: "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=400&q=80" },
            { word: "Цирк", syll: "ЦИРК", uz: "Sirk", img: "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?auto=format&fit=crop&w=400&q=80" },
            { word: "Часы", syll: "ЧА - СЫ", uz: "Soat", img: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=400&q=80" },
            { word: "Чай", syll: "ЧАЙ", uz: "Choy", img: "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=400&q=80" },
            { word: "Чашка", syll: "ЧАШ - КА", uz: "Chashka", img: "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=400&q=80" },
            { word: "Шапка", syll: "ШАП - КА", uz: "Shapka", img: "https://images.unsplash.com/photo-1576871337622-98d48d1cf531?auto=format&fit=crop&w=400&q=80" },
            { word: "Школа", syll: "ШКО - ЛА", uz: "Maktab", img: "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=400&q=80" },
            { word: "Шарф", syll: "ШАРФ", uz: "Sharf", img: "https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?auto=format&fit=crop&w=400&q=80" },
            { word: "Шкаф", syll: "ШКАФ", uz: "Shkaf", img: "https://images.unsplash.com/photo-1595428774223-ef52624120d2?auto=format&fit=crop&w=400&q=80" },

            { word: "Щётка", syll: "ЩЁТ - КА", uz: "Cho'tka", img: "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?auto=format&fit=crop&w=400&q=80" },
            { word: "Экран", syll: "ЭК - РАН", uz: "Ekran", img: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=400&q=80" },
            { word: "Юбка", syll: "ЮБ - КА", uz: "Yubka", img: "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=400&q=80" },
            { word: "Яблоко", syll: "ЯБ - ЛО - КО", uz: "Olma", img: "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=400&q=80" },
            { word: "Ягода", syll: "Я - ГО - ДА", uz: "Rezavor meva", img: "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=400&q=80" },
            { word: "Яйцо", syll: "ЯЙ - ЦО", uz: "Tuxum", img: "https://images.unsplash.com/photo-1506976785307-8732e854ad03?auto=format&fit=crop&w=400&q=80" },
            { word: "Рюкзак", syll: "РЮК - ЗАК", uz: "Ryukzak / Sumka", img: "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=400&q=80" },
            { word: "Мяч", syll: "МЯЧ", uz: "Koptok", img: "https://images.unsplash.com/photo-1579952363873-27f3bade9f55?auto=format&fit=crop&w=400&q=80" },
            { word: "Окно", syll: "ОК - НО", uz: "Deraza", img: "https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=400&q=80" },
            { word: "Картина", syll: "КАР - ТИ - НА", uz: "Rasm / Kartina", img: "https://images.unsplash.com/photo-1579783902614-a3fb3927b675?auto=format&fit=crop&w=400&q=80" }
        ];

        let currentReadingPage = 1;
        const readingItemsPerPage = 10;
        const totalReadingPages = Math.ceil(readingPics100.length / readingItemsPerPage);

        function renderReadingPicsPage(page) {
            currentReadingPage = page;
            const container = document.getElementById('syl-grid-level4');
            container.innerHTML = '';

            const start = (page - 1) * readingItemsPerPage;
            const end = start + readingItemsPerPage;
            const pageItems = readingPics100.slice(start, end);

            pageItems.forEach((item, index) => {
                const globalIndex = start + index + 1;
                const card = document.createElement('div');
                card.className = "bg-white p-3 rounded-2xl border-2 border-slate-100 hover:border-purple-400 hover:shadow-lg transition cursor-pointer flex flex-col justify-between group active:scale-95";
                card.innerHTML = `
                    <div>
                        <div class="flex justify-between items-center mb-1.5">
                            <span class="text-[10px] font-black text-purple-700 bg-purple-50 px-2 py-0.5 rounded-lg border border-purple-100">#${globalIndex}</span>
                            <button onclick="event.stopPropagation(); playSound('${item.word}');" class="w-6 h-6 rounded-lg bg-purple-50 text-purple-600 flex items-center justify-center text-xs group-hover:bg-purple-600 group-hover:text-white transition">
                                <i class="fas fa-volume-high"></i>
                            </button>
                        </div>
                        <div class="w-full h-24 rounded-xl overflow-hidden mb-2 bg-slate-100 shadow-inner">
                            <img src="${item.img}" alt="${item.word}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" loading="lazy">
                        </div>
                        <div class="text-center">
                            <span class="text-xs font-black text-purple-600 bg-purple-50 px-2 py-0.5 rounded-md inline-block mb-1 border border-purple-100">${item.syll}</span>
                            <h4 class="text-base font-black text-slate-800">${item.word}</h4>
                            <p class="text-[11px] font-semibold text-slate-400 mt-0.5">${item.uz}</p>
                        </div>
                    </div>
                `;
                card.onclick = () => playSound(`${item.word}`);
                container.appendChild(card);
            });

            renderReadingPagination();
        }

        function renderReadingPagination() {
            const pagBox = document.getElementById('syl-level4-pagination');
            pagBox.innerHTML = '';

            for (let i = 1; i <= totalReadingPages; i++) {
                const btn = document.createElement('button');
                btn.className = `px-3 py-1.5 rounded-xl font-black text-xs transition ${
                    i === currentReadingPage
                        ? 'bg-purple-600 text-white shadow-md shadow-purple-200'
                        : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
                }`;
                btn.textContent = `${(i - 1) * 10 + 1}-${i * 10}`;
                btn.onclick = () => renderReadingPicsPage(i);
                pagBox.appendChild(btn);
            }
        }

        function renderSyllables() {
            // Level 1: Slogi
            const g1 = document.getElementById('syl-grid-level1');
            g1.innerHTML = '';
            syllablesLevel1.forEach(item => {
                const card = document.createElement('div');
                card.className = "p-3 bg-white hover:bg-teal-50 border-2 border-slate-100 hover:border-teal-400 rounded-2xl shadow-sm text-center cursor-pointer transition flex flex-col justify-between active:scale-95";
                card.innerHTML = `
                    <div class="text-2xl font-black text-teal-700">${item.syl}</div>
                    <div class="text-[11px] font-bold text-slate-400 mt-1">${item.uz}</div>
                `;
                card.onclick = () => playSound(item.syl);
                g1.appendChild(card);
            });

            // Level 2: Qisqa so'zlar
            const g2 = document.getElementById('syl-grid-level2');
            g2.innerHTML = '';
            syllablesLevel2.forEach(item => {
                const card = document.createElement('div');
                card.className = "p-3.5 bg-white hover:bg-sky-50 border-2 border-slate-100 hover:border-sky-400 rounded-2xl shadow-sm cursor-pointer transition flex flex-col justify-between active:scale-95";
                card.innerHTML = `
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-xs font-black text-sky-600 bg-sky-100 px-2 py-0.5 rounded-lg">${item.syll}</span>
                        <i class="fas fa-volume-high text-xs text-sky-500"></i>
                    </div>
                    <div class="text-xl font-black text-slate-800 my-1">${item.word}</div>
                    <div class="text-xs font-semibold text-slate-400">${item.uz}</div>
                `;
                card.onclick = () => playSound(item.word);
                g2.appendChild(card);
            });

            // Level 3: Bo'g'inli so'zlar
            const g3 = document.getElementById('syl-grid-level3');
            g3.innerHTML = '';
            syllablesLevel3.forEach(item => {
                const card = document.createElement('div');
                card.className = "p-3.5 bg-white hover:bg-amber-50 border-2 border-slate-100 hover:border-amber-400 rounded-2xl shadow-sm cursor-pointer transition flex flex-col justify-between active:scale-95";
                card.innerHTML = `
                    <div class="flex justify-between items-center mb-1.5">
                        <span class="text-sm font-black text-amber-600 bg-amber-50 px-2.5 py-0.5 rounded-lg border border-amber-200">${item.syll}</span>
                        <i class="fas fa-volume-high text-xs text-amber-500"></i>
                    </div>
                    <div class="text-lg font-black text-slate-800 my-0.5">${item.word}</div>
                    <div class="text-xs font-semibold text-slate-500">${item.uz}</div>
                `;
                card.onclick = () => playSound(item.word);
                g3.appendChild(card);
            });

            // Level 4: 100 ta rasmli so'z
            renderReadingPicsPage(1);
        }

        function filterSyllableTab(lvl) {
            ['level1', 'level2', 'level3', 'level4'].forEach(l => {
                document.getElementById(`syl-${l}-box`).classList.add('hidden');
            });
            document.getElementById('btn-syl-1').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";
            document.getElementById('btn-syl-2').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";
            document.getElementById('btn-syl-3').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";
            document.getElementById('btn-syl-4').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";

            document.getElementById(`syl-${lvl}-box`).classList.remove('hidden');

            if (lvl === 'level1') document.getElementById('btn-syl-1').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-teal-600 text-white shadow";
            if (lvl === 'level2') document.getElementById('btn-syl-2').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-sky-600 text-white shadow";
            if (lvl === 'level3') document.getElementById('btn-syl-3').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-amber-600 text-white shadow";
            if (lvl === 'level4') document.getElementById('btn-syl-4').className = "px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white shadow";
        }

        // ==========================================
        // 50 TA RASMLI TEST BAZASI
        // ==========================================
        const picQuiz50 = [
            // 1-VARIANT: 1 - 25
            { ru: "Яблоко", uz: "Bu nima? (Olma)", wrong: "Апельсин", img: "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=600&q=80" },
            { ru: "Кот", uz: "Bu nima? (Mushuk)", wrong: "Собака", img: "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=600&q=80" },
            { ru: "Дом", uz: "Bu nima? (Uy)", wrong: "Школа", img: "https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=600&q=80" },
            { ru: "Машина", uz: "Bu nima? (Mashina)", wrong: "Поезд", img: "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=600&q=80" },
            { ru: "Книга", uz: "Bu nima? (Kitob)", wrong: "Тетрадь", img: "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80" },
            { ru: "Солнце", uz: "Bu nima? (Quyosh)", wrong: "Луна", img: "https://images.unsplash.com/photo-1532767153582-b1a0e5145009?auto=format&fit=crop&w=600&q=80" },
            { ru: "Хлеб", uz: "Bu nima? (Non)", wrong: "Торт", img: "https://images.unsplash.com/photo-1509440159596-0249088772ff?auto=format&fit=crop&w=600&q=80" },
            { ru: "Арбуз", uz: "Bu nima? (Tarvuz)", wrong: "Дыня", img: "https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=600&q=80" },
            { ru: "Цветок", uz: "Bu nima? (Gul)", wrong: "Дерево", img: "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=600&q=80" },
            { ru: "Рыба", uz: "Bu nima? (Baliq)", wrong: "Птица", img: "https://images.unsplash.com/photo-1522069169874-c58ec4b76be5?auto=format&fit=crop&w=600&q=80" },
            { ru: "Банан", uz: "Bu nima? (Banan)", wrong: "Лимон", img: "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=600&q=80" },
            { ru: "Часы", uz: "Bu nima? (Soat)", wrong: "Очки", img: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=600&q=80" },
            { ru: "Птица", uz: "Bu nima? (Qush)", wrong: "Бабочка", img: "https://images.unsplash.com/photo-1444464666168-49d633b86797?auto=format&fit=crop&w=600&q=80" },
            { ru: "Дерево", uz: "Bu nima? (Daraxt)", wrong: "Трава", img: "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=600&q=80" },
            { ru: "Чай", uz: "Bu nima? (Choy)", wrong: "Молоко", img: "https://images.unsplash.com/photo-1544787219-7f47ccb76574?auto=format&fit=crop&w=600&q=80" },
            { ru: "Молоко", uz: "Bu nima? (Sut)", wrong: "Вода", img: "https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=600&q=80" },
            { ru: "Стол", uz: "Bu nima? (Stol)", wrong: "Стул", img: "https://images.unsplash.com/photo-1533090161767-e6ffed986c88?auto=format&fit=crop&w=600&q=80" },
            { ru: "Стул", uz: "Bu nima? (Stul)", wrong: "Диван", img: "https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&w=600&q=80" },
            { ru: "Карандаш", uz: "Bu nima? (Qalam)", wrong: "Ручка", img: "https://images.unsplash.com/photo-1585336261026-77894a861616?auto=format&fit=crop&w=600&q=80" },
            { ru: "Ручка", uz: "Bu nima? (Ruchka)", wrong: "Ножницы", img: "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?auto=format&fit=crop&w=600&q=80" },
            { ru: "Шапка", uz: "Bu nima? (Shapka)", wrong: "Шарф", img: "https://images.unsplash.com/photo-1576871337622-98d48d1cf531?auto=format&fit=crop&w=600&q=80" },
            { ru: "Окно", uz: "Bu nima? (Deraza)", wrong: "Дверь", img: "https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=600&q=80" },
            { ru: "Дверь", uz: "Bu nima? (Eshik)", wrong: "Стена", img: "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80" },
            { ru: "Гриб", uz: "Bu nima? (Qo'ziqorin)", wrong: "Ягода", img: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80" },
            { ru: "Сыр", uz: "Bu nima? (Pishloq)", wrong: "Масло", img: "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?auto=format&fit=crop&w=600&q=80" },

            // 2-VARIANT: 26 - 50
            { ru: "Собака", uz: "Bu nima? (It)", wrong: "Волк", img: "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80" },
            { ru: "Волк", uz: "Bu nima? (Bo'ri)", wrong: "Лиса", img: "https://images.unsplash.com/photo-1564466809058-bf4114d55352?auto=format&fit=crop&w=600&q=80" },
            { ru: "Медведь", uz: "Bu nima? (Ayiq)", wrong: "Тигр", img: "https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?auto=format&fit=crop&w=600&q=80" },
            { ru: "Тигр", uz: "Bu nima? (Yo'lbars)", wrong: "Лев", img: "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?auto=format&fit=crop&w=600&q=80" },
            { ru: "Заяц", uz: "Bu nima? (Quyon)", wrong: "Еж", img: "https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?auto=format&fit=crop&w=600&q=80" },
            { ru: "Лимон", uz: "Bu nima? (Limon)", wrong: "Апельсин", img: "https://images.unsplash.com/photo-1533038590840-1cde6e668a91?auto=format&fit=crop&w=600&q=80" },
            { ru: "Апельсин", uz: "Bu nima? (Apelsin)", wrong: "Яблоко", img: "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?auto=format&fit=crop&w=600&q=80" },
            { ru: "Морковь", uz: "Bu nima? (Sabzi)", wrong: "Огурец", img: "https://images.unsplash.com/photo-1598170845058-32b9d6a5c317?auto=format&fit=crop&w=600&q=80" },
            { ru: "Огурец", uz: "Bu nima? (Bodring)", wrong: "Помидор", img: "https://images.unsplash.com/photo-1604977042946-1eecc30f269e?auto=format&fit=crop&w=600&q=80" },
            { ru: "Помидор", uz: "Bu nima? (Pomidor)", wrong: "Яблоко", img: "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?auto=format&fit=crop&w=600&q=80" },
            { ru: "Картофель", uz: "Bu nima? (Kartoshka)", wrong: "Лук", img: "https://images.unsplash.com/photo-1518977676601-b53f82aba655?auto=format&fit=crop&w=600&q=80" },
            { ru: "Самолет", uz: "Bu nima? (Samolyot)", wrong: "Вертолет", img: "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=600&q=80" },
            { ru: "Поезд", uz: "Bu nima? (Poyezd)", wrong: "Автобус", img: "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=600&q=80" },
            { ru: "Корабль", uz: "Bu nima? (Kema)", wrong: "Лодка", img: "https://images.unsplash.com/photo-1559136555-9303baea8ebd?auto=format&fit=crop&w=600&q=80" },
            { ru: "Велосипед", uz: "Bu nima? (Velosiped)", wrong: "Машина", img: "https://images.unsplash.com/photo-1485965120184-e220f721d03e?auto=format&fit=crop&w=600&q=80" },
            { ru: "Луна", uz: "Bu nima? (Oy)", wrong: "Солнце", img: "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?auto=format&fit=crop&w=600&q=80" },
            { ru: "Звезда", uz: "Bu nima? (Yulduz)", wrong: "Облако", img: "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80" },
            { ru: "Снег", uz: "Bu nima? (Qor)", wrong: "Дождь", img: "https://images.unsplash.com/photo-1517299321609-52687d1bc55a?auto=format&fit=crop&w=600&q=80" },
            { ru: "Очки", uz: "Bu nima? (Ko'zoynak)", wrong: "Часы", img: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80" },
            { ru: "Зонт", uz: "Bu nima? (Soyabon)", wrong: "Шляпа", img: "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80" },
            { ru: "Море", uz: "Bu nima? (Dengiz)", wrong: "Река", img: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80" },
            { ru: "Гора", uz: "Bu nima? (Tog')", wrong: "Холм", img: "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80" },
            { ru: "Телефон", uz: "Bu nima? (Telefon)", wrong: "Компьютер", img: "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80" },
            { ru: "Торт", uz: "Bu nima? (Tort)", wrong: "Хлеб", img: "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=600&q=80" },
            { ru: "Бабочка", uz: "Bu nima? (Kapalak)", wrong: "Птица", img: "https://images.unsplash.com/photo-1559253664-ca249d4608c6?auto=format&fit=crop&w=600&q=80" }
        ];

        let currentPicVariant = 1, picQuestions = [], currPicIdx = 0, picScore = 0, picCorrectCount = 0, isPicAnswered = false;

        function switchPicVariant(v) {
            currentPicVariant = v;
            document.getElementById('btn-pic-var1').className = v === 1 ? "px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white shadow" : "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";
            document.getElementById('btn-pic-var2').className = v === 2 ? "px-3 py-1.5 rounded-xl text-xs font-bold bg-purple-600 text-white shadow" : "px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 text-slate-700 hover:bg-slate-200";
            initPicVariantQuestions();
        }

        function initPicVariantQuestions() {
            picQuestions = currentPicVariant === 1 ? picQuiz50.slice(0, 25) : picQuiz50.slice(25, 50);
            currPicIdx = 0; picScore = 0; picCorrectCount = 0;
            document.getElementById('picquiz-question-box').classList.remove('hidden');
            document.getElementById('picquiz-result-box').classList.add('hidden');
            loadPicQuestion(0);
        }

        function loadPicQuestion(idx) {
            isPicAnswered = false;
            const item = picQuestions[idx];
            document.getElementById('picquiz-num').textContent = idx + 1;
            document.getElementById('picquiz-score').textContent = picScore;
            document.getElementById('picquiz-progress-bar').style.width = `${((idx + 1) / 25) * 100}%`;
            document.getElementById('picquiz-img').src = item.img;
            document.getElementById('picquiz-uz-hint').textContent = item.uz;
            document.getElementById('picquiz-feedback').textContent = '';

            const nextBtn = document.getElementById('picquiz-next-btn');
            nextBtn.disabled = true;
            nextBtn.className = "px-5 py-2 bg-slate-200 text-slate-400 rounded-xl font-bold text-xs transition cursor-not-allowed";

            const opts = [item.ru, item.wrong].sort(() => 0.5 - Math.random());
            const optBox = document.getElementById('picquiz-options');
            optBox.innerHTML = '';
            const labels = ['A', 'B'];

            opts.forEach((text, i) => {
                const btn = document.createElement('button');
                btn.className = "pic-opt-btn p-4 bg-white border-2 border-slate-200 hover:border-purple-400 hover:bg-purple-50/50 rounded-2xl flex items-center gap-3 transition shadow-sm font-extrabold text-lg text-slate-800 active:scale-95";
                btn.innerHTML = `
                    <span class="w-8 h-8 rounded-xl bg-purple-100 text-purple-700 text-xs flex items-center justify-center font-black">${labels[i]}</span>
                    <span class="flex-1 text-center font-black text-xl">${text}</span>
                `;
                btn.onclick = () => selectPicAnswer(text, btn, item);
                optBox.appendChild(btn);
            });
        }

        function playPicQuizAudio() { playSound(picQuestions[currPicIdx].ru); }

        function selectPicAnswer(selectedText, btn, item) {
            if (isPicAnswered) return;
            isPicAnswered = true;
            const allBtns = document.querySelectorAll('.pic-opt-btn');
            allBtns.forEach(b => b.classList.add('cursor-default'));

            if (selectedText === item.ru) {
                btn.className = "p-4 bg-emerald-500 border-2 border-emerald-600 rounded-2xl flex items-center gap-3 text-white shadow-md font-extrabold text-lg";
                btn.querySelector('span').className = "w-8 h-8 rounded-xl bg-emerald-600 text-white text-xs flex items-center justify-center font-black";
                picScore += 2; picCorrectCount++;
                document.getElementById('picquiz-score').textContent = picScore;
                document.getElementById('picquiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-emerald-600";
                document.getElementById('picquiz-feedback').textContent = `✔ To'g'ri! (+2 ball): ${item.ru}`;
                playSound(`Правильно! ${item.ru}`);
            } else {
                btn.className = "p-4 bg-rose-500 border-2 border-rose-600 rounded-2xl flex items-center gap-3 text-white shadow-md font-extrabold text-lg";
                btn.querySelector('span').className = "w-8 h-8 rounded-xl bg-rose-600 text-white text-xs flex items-center justify-center font-black";
                allBtns.forEach(b => {
                    if (b.innerText.includes(item.ru)) {
                        b.className = "p-4 bg-emerald-500 border-2 border-emerald-600 rounded-2xl flex items-center gap-3 text-white shadow-md font-extrabold text-lg";
                        b.querySelector('span').className = "w-8 h-8 rounded-xl bg-emerald-600 text-white text-xs flex items-center justify-center font-black";
                    }
                });
                document.getElementById('picquiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-rose-500";
                document.getElementById('picquiz-feedback').textContent = `✖ Noto'g'ri! To'g'ri javob: ${item.ru}`;
                playSound(`Неправильно. Это ${item.ru}`);
            }

            const nextBtn = document.getElementById('picquiz-next-btn');
            nextBtn.disabled = false;
            nextBtn.className = "px-5 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-xl font-bold text-xs transition cursor-pointer shadow-md";
        }

        function goToNextPicQuestion() {
            if (currPicIdx < 24) { currPicIdx++; loadPicQuestion(currPicIdx); }
            else showPicResult();
        }

        function showPicResult() {
            document.getElementById('picquiz-question-box').classList.add('hidden');
            document.getElementById('picquiz-result-box').classList.remove('hidden');
            document.getElementById('picres-total-score').textContent = `${picScore} / 50`;
            document.getElementById('picres-correct-count').textContent = picCorrectCount;
            document.getElementById('picres-wrong-count').textContent = 25 - picCorrectCount;
            const b = document.getElementById('picres-grade-badge');
            if (picScore >= 44) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-emerald-100 text-emerald-800"; b.textContent = "A'lo! (5 Baho)"; }
            else if (picScore >= 34) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-sky-100 text-sky-800"; b.textContent = "Yaxshi! (4 Baho)"; }
            else if (picScore >= 24) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-amber-100 text-amber-800"; b.textContent = "Qoniqarli (3 Baho)"; }
            else { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-rose-100 text-rose-800"; b.textContent = "Qaytadan topshiring!"; }
        }

        function restartCurrentPicVariant() { initPicVariantQuestions(); }

        // ==========================================
        // ESKI RO'YXATLAR VA BAZALAR
        // ==========================================
        const lettersData = [
            { char: 'А', small: 'а', type: 'unli', word: 'Арбуз', uz: 'Tarvuz', img: 'https://images.unsplash.com/photo-1587049352846-4a222e784d38?auto=format&fit=crop&w=400&q=80' },
            { char: 'Б', small: 'б', type: 'undosh', word: 'Бабочка', uz: 'Kapalak', img: 'https://images.unsplash.com/photo-1559253664-ca249d4608c6?auto=format&fit=crop&w=400&q=80' },
            { char: 'В', small: 'в', type: 'undosh', word: 'Волк', uz: 'Bo‘ri', img: 'https://images.unsplash.com/photo-1564466809058-bf4114d55352?auto=format&fit=crop&w=400&q=80' },
            { char: 'Г', small: 'г', type: 'undosh', word: 'Гриб', uz: 'Qo‘ziqorin', img: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=400&q=80' },
            { char: 'Д', small: 'д', type: 'undosh', word: 'Дом', uz: 'Uy', img: 'https://images.unsplash.com/photo-1518780664697-55e3ad937233?auto=format&fit=crop&w=400&q=80' },
            { char: 'Е', small: 'е', type: 'unli', word: 'Ель', uz: 'Archa', img: 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ё', small: 'ё', type: 'unli', word: 'Ёж', uz: 'Tipratikan', img: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=400&q=80' },
            { char: 'Ж', small: 'ж', type: 'undosh', word: 'Жираф', uz: 'Jirafa', img: 'https://images.unsplash.com/photo-1538099130811-745e64318258?auto=format&fit=crop&w=400&q=80' },
            { char: 'З', small: 'з', type: 'undosh', word: 'Заяц', uz: 'Quyon', img: 'https://images.unsplash.com/photo-1585110396000-c9ffd4e4b308?auto=format&fit=crop&w=400&q=80' },
            { char: 'И', small: 'и', type: 'unli', word: 'Игла', uz: 'Igna', img: 'https://images.unsplash.com/photo-1584824486509-112e4181ff6b?auto=format&fit=crop&w=400&q=80' },
            { char: 'Й', small: 'й', type: 'undosh', word: 'Йогурт', uz: 'Yogurt', img: 'https://images.unsplash.com/photo-1488477181946-6428a0291777?auto=format&fit=crop&w=400&q=80' },
            { char: 'К', small: 'к', type: 'undosh', word: 'Кот', uz: 'Mushuk', img: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80' },
            { char: 'Л', small: 'л', type: 'undosh', word: 'Лимон', uz: 'Limon', img: 'https://images.unsplash.com/photo-1533038590840-1cde6e668a91?auto=format&fit=crop&w=400&q=80' },
            { char: 'М', small: 'м', type: 'undosh', word: 'Медведь', uz: 'Ayiq', img: 'https://images.unsplash.com/photo-1530595467537-0b5996c41f2d?auto=format&fit=crop&w=400&q=80' },
            { char: 'Н', small: 'н', type: 'undosh', word: 'Ножницы', uz: 'Qaychi', img: 'https://images.unsplash.com/photo-1503792501406-2c40da09e1e2?auto=format&fit=crop&w=400&q=80' },
            { char: 'О', small: 'о', type: 'unli', word: 'Окно', uz: 'Deraza', img: 'https://images.unsplash.com/photo-1509644851169-2acc08aa25b5?auto=format&fit=crop&w=400&q=80' },
            { char: 'П', small: 'п', type: 'undosh', word: 'Птица', uz: 'Qush', img: 'https://images.unsplash.com/photo-1444464666168-49d633b86797?auto=format&fit=crop&w=400&q=80' },
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
            { ru: 'Арбуз', uz: 'Tarvuz', char: 'А' }, { ru: 'Ананас', uz: 'Ananas', char: 'А' }, { ru: 'Автобус', uz: 'Avtobus', char: 'А' }, { ru: 'Апельсин', uz: 'Apelsin', char: 'А' }, { ru: 'Альбом', uz: 'Albom', char: 'А' }, { ru: 'Акула', uz: 'Akula', char: 'А' },
            { ru: 'Бабочка', uz: 'Kapalak', char: 'Б' }, { ru: 'Банан', uz: 'Banan', char: 'Б' }, { ru: 'Брат', uz: 'Aka / Uka', char: 'Б' }, { ru: 'Бумага', uz: 'Qog‘oz', char: 'Б' }, { ru: 'Берёза', uz: 'Qayin daraxti', char: 'Б' }, { ru: 'Барабан', uz: 'Nog‘ora', char: 'Б' },
            { ru: 'Волк', uz: 'Bo‘ri', char: 'В' }, { ru: 'Вода', uz: 'Suv', char: 'В' }, { ru: 'Воздух', uz: 'Havo', char: 'В' }, { ru: 'Ветер', uz: 'Shamol', char: 'В' }, { ru: 'Время', uz: 'Vaqt', char: 'В' }, { ru: 'Врач', uz: 'Shifokor', char: 'В' },
            { ru: 'Гриб', uz: 'Qo‘ziqorin', char: 'Г' }, { ru: 'Город', uz: 'Shahar', char: 'Г' }, { ru: 'Глаз', uz: 'Ko‘z', char: 'Г' }, { ru: 'Груша', uz: 'Nok', char: 'Г' }, { ru: 'Гора', uz: 'Tog‘', char: 'Г' }, { ru: 'Голова', uz: 'Bosh', char: 'Г' },
            { ru: 'Дом', uz: 'Uy', char: 'Д' }, { ru: 'Дверь', uz: 'Eshik', char: 'Д' }, { ru: 'Друг', uz: 'Do‘st', char: 'Д' }, { ru: 'Дерево', uz: 'Daraxt', char: 'Д' }, { ru: 'Дождь', uz: 'Yomg‘ir', char: 'Д' }, { ru: 'Дорога', uz: 'Yo‘l', char: 'Д' },
            { ru: 'Ель', uz: 'Archa', char: 'Е' }, { ru: 'Енот', uz: 'Yenot', char: 'Е' }, { ru: 'Еда', uz: 'Ovqat', char: 'Е' }, { ru: 'Ежевика', uz: 'Maymunjon', char: 'Е' },
            { ru: 'Ёж', uz: 'Tipratikan', char: 'Ё' }, { ru: 'Ёлка', uz: 'Yangi yil archasi', char: 'Ё' }, { ru: 'Ёрш', uz: 'Baliqcha', char: 'Ё' },
            { ru: 'Жираф', uz: 'Jirafa', char: 'Ж' }, { ru: 'Жук', uz: 'Qo‘ng‘iz', char: 'Ж' }, { ru: 'Жизнь', uz: 'Hayot', char: 'Ж' }, { ru: 'Железо', uz: 'Temir', char: 'Ж' }, { ru: 'Женщина', uz: 'Ayol', char: 'Ж' },
            { ru: 'Заяц', uz: 'Quyon', char: 'З' }, { ru: 'Звезда', uz: 'Yulduz', char: 'З' }, { ru: 'Земля', uz: 'Yer', char: 'З' }, { ru: 'Зима', uz: 'Qish', char: 'З' }, { ru: 'Зуб', uz: 'Tish', char: 'З' }, { ru: 'Зонт', uz: 'Soyabon', char: 'З' },
            { ru: 'Игла', uz: 'Igna', char: 'И' }, { ru: 'Игра', uz: 'O‘yin', char: 'И' }, { ru: 'Имя', uz: 'Ism', char: 'И' }, { ru: 'Инженер', uz: 'Muhandis', char: 'И' }, { ru: 'Инструмент', uz: 'Asbob', char: 'И' },
            { ru: 'Йогурт', uz: 'Yogurt', char: 'Й' }, { ru: 'Йод', uz: 'Yod eritmasi', char: 'Й' },
            { ru: 'Кот', uz: 'Mushuk', char: 'К' }, { ru: 'Книга', uz: 'Kitob', char: 'К' }, { ru: 'Карандаш', uz: 'Qalam', char: 'К' }, { ru: 'Комната', uz: 'Xona', char: 'К' }, { ru: 'Корова', uz: 'Sigir', char: 'К' }, { ru: 'Компьютер', uz: 'Kompyuter', char: 'К' },
            { ru: 'Лимон', uz: 'Limon', char: 'Л' }, { ru: 'Лес', uz: 'O‘rmon', char: 'Л' }, { ru: 'Луна', uz: 'Oy', char: 'Л' }, { ru: 'Лист', uz: 'Barg', char: 'Л' }, { ru: 'Лошадь', uz: 'Ot', char: 'Л' }, { ru: 'Ложка', uz: 'Qoshiq', char: 'Л' },
            { ru: 'Медведь', uz: 'Ayiq', char: 'М' }, { ru: 'Мама', uz: 'Ona', char: 'М' }, { ru: 'Машина', uz: 'Mashina', char: 'М' }, { ru: 'Молоко', uz: 'Sut', char: 'М' }, { ru: 'Море', uz: 'Dengiz', char: 'М' }, { ru: 'Мыло', uz: 'Sovun', char: 'М' },
            { ru: 'Ножницы', uz: 'Qaychi', char: 'Н' }, { ru: 'Нос', uz: 'Burun', char: 'Н' }, { ru: 'Ночь', uz: 'Tun', char: 'Н' }, { ru: 'Небо', uz: 'Osmon', char: 'Н' }, { ru: 'Нога', uz: 'Oyoq', char: 'Н' }, { ru: 'Номер', uz: 'Raqam', char: 'Н' },
            { ru: 'Окно', uz: 'Deraza', char: 'О' }, { ru: 'Огонь', uz: 'Olov', char: 'О' }, { ru: 'Озеро', uz: 'Ko‘l', char: 'О' }, { ru: 'Осень', uz: 'Kuz', char: 'О' }, { ru: 'Остров', uz: 'Orol', char: 'О' }, { ru: 'Очки', uz: 'Ko‘zoynak', char: 'О' },
            { ru: 'Птица', uz: 'Qush', char: 'П' }, { ru: 'Папа', uz: 'Dada', char: 'П' }, { ru: 'Письмо', uz: 'Xat', char: 'П' }, { ru: 'Поезд', uz: 'Poyezd', char: 'П' }, { ru: 'Поле', uz: 'Dala', char: 'П' }, { ru: 'Парк', uz: 'Bog‘', char: 'П' },
            { ru: 'Рыба', uz: 'Baliq', char: 'Р' }, { ru: 'Рука', uz: 'Qo‘l', char: 'Р' }, { ru: 'Ручка', uz: 'Ruchka', char: 'Р' }, { ru: 'Река', uz: 'Daryo', char: 'Р' }, { ru: 'Роза', uz: 'Atirgul', char: 'Р' }, { ru: 'Работа', uz: 'Ish', char: 'Р' },
            { ru: 'Солнце', uz: 'Quyosh', char: 'С' }, { ru: 'Стол', uz: 'Stol', char: 'С' }, { ru: 'Стул', uz: 'Stul', char: 'С' }, { ru: 'Семья', uz: 'Oila', char: 'С' }, { ru: 'Снег', uz: 'Qor', char: 'С' }, { ru: 'Собака', uz: 'It', char: 'С' },
            { ru: 'Тигр', uz: 'Yo‘lbars', char: 'Т' }, { ru: 'Тетрадь', uz: 'Daftar', char: 'Т' }, { ru: 'Телефон', uz: 'Telefon', char: 'Т' }, { ru: 'Тарелка', uz: 'Tarelka', char: 'Т' }, { ru: 'Трава', uz: 'O‘t', char: 'Т' }, { ru: 'Торт', uz: 'Tort', char: 'Т' },
            { ru: 'Утка', uz: 'O‘rdak', char: 'У' }, { ru: 'Ученик', uz: 'O‘quvchi', char: 'У' }, { ru: 'Учитель', uz: 'O‘qituvchi', char: 'У' }, { ru: 'Улица', uz: 'Ko‘cha', char: 'У' }, { ru: 'Утро', uz: 'Ertalab', char: 'У' }, { ru: 'Ухо', uz: 'Quloq', char: 'У' },
            { ru: 'Флаг', uz: 'Bayroq', char: 'Ф' }, { ru: 'Фрукт', uz: 'Meva', char: 'Ф' }, { ru: 'Фонарь', uz: 'Fonar', char: 'Ф' }, { ru: 'Фото', uz: 'Surat', char: 'Ф' }, { ru: 'Футбол', uz: 'Futbol', char: 'Ф' },
            { ru: 'Хлеб', uz: 'Non', char: 'Х' }, { ru: 'Холод', uz: 'Sovuq', char: 'Х' }, { ru: 'Художник', uz: 'Rassom', char: 'Х' }, { ru: 'Хвост', uz: 'Dum', char: 'Х' },
            { ru: 'Цветок', uz: 'Gul', char: 'Ц' }, { ru: 'Царь', uz: 'Podsho', char: 'Ц' }, { ru: 'Цирк', uz: 'Sirk', char: 'Ц' }, { ru: 'Цена', uz: 'Narx', char: 'Ц' }, { ru: 'Цепь', uz: 'Zanjir', char: 'Ц' },
            { ru: 'Часы', uz: 'Soat', char: 'Ч' }, { ru: 'Чай', uz: 'Choy', char: 'Ч' }, { ru: 'Человек', uz: 'Inson', char: 'Ч' }, { ru: 'Чашка', uz: 'Chashka', char: 'Ч' }, { ru: 'Число', uz: 'Son', char: 'Ч' },
            { ru: 'Шапка', uz: 'Shapka', char: 'Ш' }, { ru: 'Школа', uz: 'Maktab', char: 'Ш' }, { ru: 'Шарф', uz: 'Sharf', char: 'Ш' }, { ru: 'Шкаф', uz: 'Shkaf', char: 'Ш' }, { ru: 'Шаг', uz: 'Qadam', char: 'Ш' },
            { ru: 'Щётка', uz: 'Cho‘tka', char: 'Щ' }, { ru: 'Щит', uz: 'Qalqon', char: 'Щ' }, { ru: 'Щенок', uz: 'Kuchukcha', char: 'Щ' }, { ru: 'Щука', uz: 'Cho‘rtanbaliq', char: 'Щ' },
            { ru: 'Экран', uz: 'Ekran', char: 'Э' }, { ru: 'Этаж', uz: 'Qavat', char: 'Э' }, { ru: 'Экскурсия', uz: 'Sayohat', char: 'Э' }, { ru: 'Энергия', uz: 'Energiya', char: 'Э' },
            { ru: 'Юбка', uz: 'Yubka', char: 'Ю' }, { ru: 'Юг', uz: 'Janub', char: 'Ю' }, { ru: 'Юмор', uz: 'Hazil', char: 'Ю' }, { ru: 'Юноша', uz: 'O‘smir yigit', char: 'Ю' },
            { ru: 'Яблоко', uz: 'Olma', char: 'Я' }, { ru: 'Ягода', uz: 'Rezavor meva', char: 'Я' }, { ru: 'Язык', uz: 'Til', char: 'Я' }, { ru: 'Яйцо', uz: 'Tuxum', char: 'Я' }, { ru: 'Якорь', uz: 'Langar', char: 'Я' }
        ];

        const maleSentences = [
            { ru: "Этот большой стол стоит в комнате.", uz: "Bu katta stol xonada turibdi." },
            { ru: "Мой папа работает инженером на заводе.", uz: "Mening dadam zavodda muhandis bo'lib ishlaydi." },
            { ru: "Новый дом построили очень быстро.", uz: "Yangi uyni juda tez qurishdi." },
            { ru: "Старший брат всегда помогает мне учиться.", uz: "Katta akam doim menga o'qishda yordam beradi." },
            { ru: "Горячий чай согревает в холодный день.", uz: "Issiq choy sovuq kunda isitadi." },
            { ru: "Русский словарь лежит на моём столе.", uz: "Ruscha lug'at stolim ustida yotibdi." },
            { ru: "Солнечный день радует всех людей.", uz: "Quyoshli kun barcha insonlarni quvontiradi." },
            { ru: "Белый карандаш лежит в пенале.", uz: "Oq qalam qalamdonda yotibdi." },
            { ru: "Маленький кот спит на мягком диване.", uz: "Kichkina mushuk yumshoq divanda uxlayapti." },
            { ru: "Сладкий арбуз принёс дедушка с базара.", uz: "Shirin tarvuzni bobom bozordan olib keldi." },
            { ru: "Быстрый поезд едет прямо в Москву.", uz: "Tez yurar poyezd to'g'ri Moskvaga ketyapti." },
            { ru: "Красивый город сияет вечерними огнями.", uz: "Go'zal shahar kechki chiroqlar bilan charaqlamoqda." },
            { ru: "Зелёный лес шумит от свежего ветра.", uz: "Yashil o'rmon toza shamoldan shovullaydi." },
            { ru: "Опытный врач внимательно осматривает больного.", uz: "Tajribali shifokor bemorni diqqat bilan ko'rmoqda." },
            { ru: "Свежий хлеб очень вкусно пахнет.", uz: "Yangi yopilgan non juda xushbo'y hid taratadi." },
            { ru: "Умный ученик быстро решил сложную задачу.", uz: "Aqlli o'quvchi qiyin masalani tezda yechdi." },
            { ru: "Храбрый лев считается царём всех зверей.", uz: "Jasur sher barcha hayvonlarning podshohi hisoblanadi." },
            { ru: "Новый компьютер работает очень быстро.", uz: "Yangi kompyuter juda tez ishlaydi." },
            { ru: "Наш школьный класс светлый и просторный.", uz: "Bizning maktab sinfimiz yorug' va keng." },
            { ru: "Этот спелый банан очень сладкий.", uz: "Bu pishgan banan juda shirin." }
        ];

        const femaleSentences = [
            { ru: "Интересная книга открывает новый мир.", uz: "Qiziqarli kitob yangi dunyoni ochadi." },
            { ru: "Моя добрая мама готовит вкусный обед.", uz: "Mening mehribon onam mazali tushlik tayyorlaydi." },
            { ru: "Младшая сестра учится в третьем классе.", uz: "Kichik singlim uchinchi sinfda o'qiydi." },
            { ru: "Синяя ручка аккуратно пишет в тетради.", uz: "Ko'k ruchka daftarga chiroyli yozadi." },
            { ru: "Школьная тетрадь должна быть чистой.", uz: "Maktab daftari toza bo'lishi kerak." },
            { ru: "Наша дружная семья живёт в согласии.", uz: "Bizning ahil oilamiz totuvlikda yashaydi." },
            { ru: "Тёмная ночь накрыла весь город тишиной.", uz: "Qorong'i tun butun shaharni sukunatga burkadi." },
            { ru: "Новая машина быстро едет по дороге.", uz: "Yangi mashina yo'lda tez ketyapti." },
            { ru: "Входная дверь была закрыта на ключ.", uz: "Kirish eshigi qulfga yopilgan edi." },
            { ru: "Красная рыба плавает в прозрачной воде.", uz: "Qizil baliq tiniq suvda suzib yuribdi." },
            { ru: "Красивая роза цветет в нашем саду.", uz: "Chiroyli atirgul bog'imizda ochilib turibdi." },
            { ru: "Маленькая птица звонко поёт на ветке.", uz: "Kichkina qush shoxda jarangdor sayramoqda." },
            { ru: "Спелая груша упала прямо на траву.", uz: "Pishgan nok to'g'ri o'tlar ustiga tushdi." },
            { ru: "Зимняя шапка надёжно защищает от холода.", uz: "Qishki shapka sovuqdan yaxshi himoya qiladi." },
            { ru: "Большая школа находится рядом с домом.", uz: "Katta maktab uyimizning yonida joylashgan." },
            { ru: "Узкая улица ведёт к старинной площади.", uz: "Tor ko'cha qadimiy maydonga olib boradi." },
            { ru: "Чистая река протекает возле деревни.", uz: "Toza daryo qishloq yonidan oqib o'tadi." },
            { ru: "Зелёная трава покрыла весенний луг.", uz: "Yashil maysa bahorgi o'tloqni qopladi." },
            { ru: "Сладкая клубника созрела на грядке.", uz: "Shirin qulupnay polizda yetilib pishdi." },
            { ru: "Любимая собака радостно встречает хозяина.", uz: "Sevimli it egasini quvonch bilan kutib oladi." }
        ];

        const neuterSentences = [
            { ru: "Большое окно пропускает много света.", uz: "Katta deraza juda ko'p yorug'lik o'tkazadi." },
            { ru: "Синее море спокойно шумит на закате.", uz: "Moviy dengiz quyosh botishida osoyishta shovullaydi." },
            { ru: "Яркое солнце дарит тепло всей природе.", uz: "Yorqin quyosh butun tabiatga iliqlik ulashadi." },
            { ru: "Важное письмо доставили вовремя.", uz: "Muhim xatni o'z vaqtida yetkazib berishdi." },
            { ru: "Красное яблоко лежит на белой тарелке.", uz: "Qizil olma oq tarelka ustida yotibdi." },
            { ru: "Тёплое молоко очень полезно для детей.", uz: "Iliq sut bolalar uchun juda foydali." },
            { ru: "Широкое поле простирается до горизонта.", uz: "Keng dala ufqqacha cho'zilib ketgan." },
            { ru: "Моё имя знают все мои одноклассники.", uz: "Mening ismimni barcha sinfdoshlarim bilishadi." },
            { ru: "Свободное время я люблю проводить с книгой.", uz: "Bo'sh vaqtimni kitob o'qish bilan o'tkazishni yaxshi ko'raman." },
            { ru: "Высокое здание построили в центре столицы.", uz: "Baland binoni poytaxt markazida qurishdi." },
            { ru: "Раннее утро встретило нас прохладой.", uz: "Erta tong bizni salqinlik bilan qarshiladi." },
            { ru: "Сладкое мороженое особенно вкусно летом.", uz: "Shirin muzqaymoq yozda ayniqsa mazali bo'ladi." },
            { ru: "Красивое платье отлично подошло сестре.", uz: "Chiroyli ko'ylak singlimga juda yarashdi." },
            { ru: "Тёплое пальто согреет в морозные дни.", uz: "Issiq palto qahraton kunlarda isitadi." },
            { ru: "Свежее яйцо добавили в утреннее тесто.", uz: "Yangi tuxumni ertalabki xamirga qo'shishdi." },
            { ru: "Чистое зеркало висит на стене прихожей.", uz: "Toza oyna yo'lak devorida osilib turibdi." },
            { ru: "Мягкое одеяло приятно согревает ночью.", uz: "Yumshoq ko'rpa tunda yoqimli isitadi." },
            { ru: "Сливочное масло положили на свежий хлеб.", uz: "Sariyog'ni yangi non ustiga surtishdi." },
            { ru: "Зелёное дерево шелестит сочной листвой.", uz: "Yashil daraxt sersuv barglari bilan shitirlaydi." },
            { ru: "Глубокое озеро славится чистейшей водой.", uz: "Chuqur ko'l o'zining top-toza suvi bilan mashhur." }
        ];

        const texts50 = [
            { id: 1, ru: "Здравствуйте! Меня зовут Азиз. Я учу русский язык.", uz: "Assalomu alaykum! Mening ismim Aziz. Men rus tilini o'rganyapman." },
            { id: 2, ru: "Это моя семья. Папа, мама и я живём дружно.", uz: "Bu mening oilam. Dadam, onam va men ahil yashaymiz." },
            { id: 3, ru: "Сегодня солнечный день. На небе нет туч.", uz: "Bugun quyoshli kun. Osmonda bulutlar yo'q." },
            { id: 4, ru: "Вот наша школа. В ней большие и светлые классы.", uz: "Mana bizning maktabimiz. Unda katta va yorug' sinflar bor." },
            { id: 5, ru: "Мой друг любит читать книги. Он много знает.", uz: "Mening do'stim kitob o'qishni yaxshi ko'radi. U ko'p narsani biladi." },
            { id: 6, ru: "На столе лежат тетрадь, ручка и карандаш.", uz: "Stol ustida daftar, ruchka va qalam yotibdi." },
            { id: 7, ru: "У меня есть кот. Его зовут Барсик. Он очень пушистый.", uz: "Mening mushugim bor. Uning ismi Barsik. U juda paxmoq." },
            { id: 8, ru: "Утром я пью тёплый чай с лимоном и ем хлеб.", uz: "Ertalab men limonli iliq choy ichaman va non yeyman." },
            { id: 9, ru: "Летом в саду созревают сладкие яблоки и груши.", uz: "Yozda bog'da shirin olmalar va noklar pishadi." },
            { id: 10, ru: "Мы часто гуляем в красивом городском парке.", uz: "Biz ko'pincha shaharning go'zal bog'ida sayr qilamiz." },
            { id: 11, ru: "Моя сестра хорошо поёт и играет на пианино.", uz: "Mening singlim chiroyli qo'shiq aytadi va pianino chaladi." },
            { id: 12, ru: "Учительница объясняет нам новое правило.", uz: "O'qituvchi ayol bizga yangi qoidani tushuntirmoqda." },
            { id: 13, ru: "Зимой часто идёт белый пушистый снег.", uz: "Qishda tez-tez oq, mayin qor yog'adi." },
            { id: 14, ru: "Мама готовит вкусный обед для всей семьи.", uz: "Onam butun oila uchun mazali tushlik tayyorlayapti." },
            { id: 15, ru: "Папа пришёл с работы и принёс вкусный торт.", uz: "Dadam ishdan keldi va shirin tort olib keldi." },
            { id: 16, ru: "Я люблю рисовать яркими красками природу.", uz: "Men tabiatni yorqin bo'yoqlar bilan chizishni yaxshi ko'raman." },
            { id: 17, ru: "На уроке русского языка мы пишем и говорим.", uz: "Rus tili darsida biz yozamiz va gapiramiz." },
            { id: 18, ru: "Птицы вьют гнёзда на высоких деревьях.", uz: "Qushlar baland daraxtlarda in qurishadi." },
            { id: 19, ru: "У меня новая синяя куртка и тёплая шапка.", uz: "Menda yangi ko'k kurtka va issiq shapka bor." },
            { id: 20, ru: "Вечером мы все вместе смотрим добрый фильм.", uz: "Kechqurun biz hammamiz birga yaxshi film tomosha qilamiz." },
            { id: 21, ru: "Это большой магазин. Там продают свежие фрукты.", uz: "Bu katta do'kon. U yerda yangi mevalar sotiladi." },
            { id: 22, ru: "Мой брат учится в университете на инженера.", uz: "Mening akam universitetda muhandislik yo'nalishida o'qiydi." },
            { id: 23, ru: "В лесу растут грибы, ягоды и высокие дубы.", uz: "O'rmonda qo'ziqorinlar, rezavorlar va baland emanlar o'sadi." },
            { id: 24, ru: "Каждое утро я делаю зарядку, чтобы быть здоровым.", uz: "Har kuni ertalab men sog'lom bo'lish uchun badantarbiya qilaman." },
            { id: 25, ru: "Собака громко лает, защищая свой дом.", uz: "It o'z uyini himoya qilib baland ovozda huriydi." },
            { id: 26, ru: "Осенью листья на деревьях становятся жёлтыми.", uz: "Kuzda daraxtlardagi barglar sariq rangga kiradi." },
            { id: 27, ru: "Девочка помогает маме поливать красивые цветы.", uz: "Qizaloq onasiga chiroyli gullarni sug'orishda yordam bermoqda." },
            { id: 28, ru: "Мы едем на автобусе в центр нашего города.", uz: "Biz avtobusda shahrimiz markaziga ketyapmiz." },
            { id: 29, ru: "Вода в реке чистая, прозрачная и прохладная.", uz: "Daryodagi suv toza, shaffof va salqin." },
            { id: 30, ru: "Я знаю все тридцать три буквы русского алфавита.", uz: "Men rus alifbosidagi barcha o'ttiz uchta harfni bilaman." },
            { id: 31, ru: "Этот мальчик быстро бегает и играет в футбол.", uz: "Bu bola tez yuguradi va futbol o'ynaydi." },
            { id: 32, ru: "На стене висят большие часы и красивая картина.", uz: "Devorda katta soat va chiroyli rasm osilib turibdi." },
            { id: 33, ru: "В библиотеке всегда тихо. Там много интересных книг.", uz: "Kutubxonada doim jimjitlik. U yerda qiziqarli kitoblar ko'p." },
            { id: 34, ru: "Я люблю пить холодное молоко со сладким печеньем.", uz: "Men sovuq sutni shirin pechenye bilan ichishni yaxshi ko'raman." },
            { id: 35, ru: "Моя бабушка вяжет тёплые носки к зиме.", uz: "Mening buvim qishga issiq paypoqlar to'qiyapti." },
            { id: 36, ru: "Дедушка рассказывает нам мудрые и интересные сказки.", uz: "Bobom bizga dono va qiziqarli ertaklar aytib beradi." },
            { id: 37, ru: "В саду распустились красные и белые розы.", uz: "Bog'da qizil va oq atirgullar ochildi." },
            { id: 38, ru: "На небе ярко сияет луна и горят звёзды.", uz: "Osmonda oy yorqin porlaydi va yulduzlar charaqlaydi." },
            { id: 39, ru: "Завтра у нас будет спортивный праздник в школе.", uz: "Ertaga maktabimizda sport bayrami bo'ladi." },
            { id: 40, ru: "Я пишу письмо моему другу в другой город.", uz: "Men boshqa shahardagi do'stimga xat yozyapman." },
            { id: 41, ru: "Рыбы плавают глубоко в чистом озере.", uz: "Baliqlar toza ko'lning tubida suzadi." },
            { id: 42, ru: "Мы купили сладкий сочный арбуз на базаре.", uz: "Biz bozordan shirin sersuv tarvuz sotib oldik." },
            { id: 43, ru: "Солнце встаёт на востоке и дарит всем тепло.", uz: "Quyosh sharqdan chiqadi va hammaga iliqlik ulashadi." },
            { id: 44, ru: "Ученики внимательно слушают своего учителя.", uz: "O'quvchilar o'qituvchilarini diqqat bilan tinglashmoqda." },
            { id: 45, ru: "Я умею красиво писать буквы в тетради.", uz: "Men daftarga harflarni chiroyli qilib yoza olaman." },
            { id: 46, ru: "Весной природа просыпается и цветут деревья.", uz: "Bahorda tabiat uyg'onadi va daraxtlar gullaydi." },
            { id: 47, ru: "Это сладкое мороженое очень вкусное.", uz: "Bu shirin muzqaymoq juda mazali." },
            { id: 48, ru: "Дорога в школу занимает у меня десять минут.", uz: "Maktabgacha bo'lgan yo'l mening o'n daqiqa vaqtimni oladi." },
            { id: 49, ru: "Русский язык очень богатый, красивый и звучный.", uz: "Rus tili juda boy, chiroyli va jarangdor til." },
            { id: 50, ru: "Мы учимся каждый день и узнаём много нового!", uz: "Biz har kuni o'qiymiz va juda ko'p yangi narsalarni bilib olamiz!" }
        ];

        function renderGenderSentences() {
            const renderGroup = (arr, elementId, colorClass, btnBg) => {
                const el = document.getElementById(elementId);
                el.innerHTML = '';
                arr.forEach((item, idx) => {
                    const row = document.createElement('div');
                    row.className = "p-2.5 bg-slate-50 hover:bg-slate-100 rounded-xl border border-slate-100 flex flex-col justify-between transition";
                    row.innerHTML = `
                        <div class="flex justify-between items-start gap-2 mb-1">
                            <p class="font-extrabold text-xs text-slate-800 leading-snug">
                                <span class="font-black ${colorClass}">#${idx + 1}</span> ${item.ru}
                            </p>
                            <button onclick="playSound('${item.ru.replace(/'/g, "\\'")}')" class="shrink-0 w-6 h-6 rounded-lg ${btnBg} flex items-center justify-center text-[10px] text-white shadow-sm hover:opacity-90">
                                <i class="fas fa-volume-high"></i>
                            </button>
                        </div>
                        <p class="text-[11px] font-semibold text-slate-500">${item.uz}</p>
                    `;
                    el.appendChild(row);
                });
            };

            renderGroup(maleSentences, 'male-sentences', 'text-sky-600', 'bg-sky-500');
            renderGroup(femaleSentences, 'female-sentences', 'text-rose-600', 'bg-rose-500');
            renderGroup(neuterSentences, 'neuter-sentences', 'text-amber-600', 'bg-amber-500');
        }

        function renderAlphabet() {
            const grid = document.getElementById('alphabet-grid');
            grid.innerHTML = '';
            lettersData.forEach(item => {
                const card = document.createElement('div');
                card.className = "bg-white rounded-2xl p-3 border hover:border-emerald-400 hover:shadow transition flex flex-col justify-between cursor-pointer";
                let badge = item.type === 'unli' ? 'bg-rose-100 text-rose-700' : (item.type === 'undosh' ? 'bg-sky-100 text-sky-700' : 'bg-amber-100 text-amber-700');
                card.innerHTML = `
                    <div>
                        <div class="flex justify-between items-center mb-1">
                            <span class="text-[10px] font-black px-1.5 py-0.5 rounded-full ${badge}">${item.type.toUpperCase()}</span>
                            <button onclick="event.stopPropagation(); playSound('${item.char}');" class="w-7 h-7 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center text-xs shadow-sm">
                                <i class="fas fa-volume-high"></i>
                            </button>
                        </div>
                        <div class="text-center my-1">
                            <div class="text-2xl font-black text-slate-800">${item.char}${item.small}</div>
                            <div class="text-lg text-amber-600 propis-font font-bold">${item.char}${item.small}</div>
                        </div>
                        <img src="${item.img}" class="w-full h-16 object-cover rounded-lg my-1">
                        <div class="text-center">
                            <p class="font-bold text-xs text-slate-800">${item.word}</p>
                            <p class="text-[10px] text-slate-400">${item.uz}</p>
                        </div>
                    </div>
                `;
                card.onclick = () => playSound(`${item.char}. ${item.word}`);
                grid.appendChild(card);
            });
        }

        function switchTab(tabId) {
            ['alphabet', 'write', 'syllables', 'gender', 'texts', 'quiz', 'picquiz'].forEach(t => {
                document.getElementById(`section-${t}`).classList.add('hidden');
                document.getElementById(`tab-${t}`).className = "px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100";
            });
            document.getElementById(`section-${tabId}`).classList.remove('hidden');
            const color = tabId === 'alphabet' ? 'bg-emerald-500' : (tabId === 'write' ? 'bg-amber-500' : (tabId === 'syllables' ? 'bg-teal-600' : (tabId === 'gender' ? 'bg-indigo-500' : (tabId === 'texts' ? 'bg-sky-500' : (tabId === 'quiz' ? 'bg-rose-500' : 'bg-purple-600')))));
            document.getElementById(`tab-${tabId}`).className = `px-3.5 py-2 rounded-xl text-xs sm:text-sm font-extrabold ${color} text-white shadow-md`;
            
            if (tabId === 'quiz' && quizSessionQuestions.length === 0) startQuizSession();
            if (tabId === 'picquiz' && picQuestions.length === 0) initPicVariantQuestions();
        }

        // CANVAS
        const canvas = document.getElementById('paint-canvas');
        const ctx = canvas.getContext('2d');
        let isPainting = false, strokeColor = '#2563eb', currentLetter = lettersData[0];

        function initCanvas() {
            const select = document.getElementById('letter-select');
            lettersData.forEach(item => {
                const opt = document.createElement('option');
                opt.value = item.char;
                opt.textContent = `${item.char}${item.small} (${item.word})`;
                select.appendChild(opt);
            });
            changeCanvasLetter('А');
            canvas.addEventListener('mousedown', startPos);
            canvas.addEventListener('mouseup', endPos);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('touchstart', (e) => { e.preventDefault(); startPos(e.touches[0]); });
            canvas.addEventListener('touchend', endPos);
            canvas.addEventListener('touchmove', (e) => { e.preventDefault(); draw(e.touches[0]); });
        }

        function startPos(e) { isPainting = true; draw(e); }
        function endPos() { isPainting = false; ctx.beginPath(); }
        function draw(e) {
            if (!isPainting) return;
            const r = canvas.getBoundingClientRect();
            const x = (e.clientX - r.left) * (canvas.width / r.width);
            const y = (e.clientY - r.top) * (canvas.height / r.height);
            ctx.lineWidth = 12; ctx.lineCap = 'round'; ctx.strokeStyle = strokeColor;
            ctx.lineTo(x, y); ctx.stroke(); ctx.beginPath(); ctx.moveTo(x, y);
        }
        function clearCanvas() { ctx.clearRect(0, 0, canvas.width, canvas.height); }
        function setStrokeColor(c) { strokeColor = c; }
        function changeCanvasLetter(char) {
            clearCanvas();
            currentLetter = lettersData.find(l => l.char === char) || lettersData[0];
            document.getElementById('canvas-guide-letter').textContent = `${currentLetter.char}${currentLetter.small}`;
            document.getElementById('canvas-card-letter-print').textContent = `${currentLetter.char}${currentLetter.small}`;
            document.getElementById('canvas-card-letter-propis').textContent = `${currentLetter.char}${currentLetter.small}`;
            document.getElementById('canvas-card-ru-word').textContent = currentLetter.word;
            document.getElementById('canvas-card-uz-word').textContent = currentLetter.uz;
            document.getElementById('canvas-card-img').src = currentLetter.img;
        }
        function speakCurrentCanvasLetter() { playSound(`${currentLetter.char}. ${currentLetter.word}`); }

        // MATNLAR
        let currentPage = 1;
        function renderTexts(p) {
            currentPage = p;
            const container = document.getElementById('texts-container');
            container.innerHTML = '';
            const slice = texts50.slice((p - 1) * 10, p * 10);
            slice.forEach(t => {
                const card = document.createElement('div');
                card.className = "bg-white p-4 rounded-2xl border shadow-sm flex flex-col justify-between";
                card.innerHTML = `
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-xs font-bold text-sky-700 bg-sky-100 px-2 py-0.5 rounded-lg">#${t.id}</span>
                            <button onclick="playSound('${t.ru.replace(/'/g, "\\'")}')" class="text-xs bg-sky-500 hover:bg-sky-600 text-white px-3 py-1 rounded-lg font-bold">🔊 Слушать</button>
                        </div>
                        <p class="font-bold text-slate-800 text-sm mb-1">${t.ru}</p>
                        <p class="text-xs text-slate-500">${t.uz}</p>
                    </div>
                `;
                container.appendChild(card);
            });
            const pag = document.getElementById('texts-pagination');
            pag.innerHTML = '';
            for (let i = 1; i <= 5; i++) {
                const btn = document.createElement('button');
                btn.className = `w-8 h-8 rounded-lg text-xs font-bold ${i === currentPage ? 'bg-sky-500 text-white' : 'bg-white border'}`;
                btn.textContent = i;
                btn.onclick = () => renderTexts(i);
                pag.appendChild(btn);
            }
        }

        // ESKI HARF TESTI
        let quizSessionQuestions = [], currQIdx = 0, quizScore = 0, correctCount = 0, isAns = false;
        function startQuizSession() {
            quizSessionQuestions = [...quizWords200].sort(() => 0.5 - Math.random()).slice(0, 50);
            currQIdx = 0; quizScore = 0; correctCount = 0;
            document.getElementById('quiz-question-box').classList.remove('hidden');
            document.getElementById('quiz-result-box').classList.add('hidden');
            loadQuizQ(0);
        }
        function loadQuizQ(idx) {
            isAns = false;
            const item = quizSessionQuestions[idx];
            document.getElementById('quiz-current-num').textContent = idx + 1;
            document.getElementById('quiz-score').textContent = quizScore;
            document.getElementById('quiz-progress-bar').style.width = `${((idx + 1) / 50) * 100}%`;
            document.getElementById('quiz-word-display').textContent = `_ ${item.ru.slice(1)}`;
            document.getElementById('quiz-uz-translation').textContent = `Tarjimasi: ${item.uz}`;
            document.getElementById('quiz-feedback').textContent = '';
            document.getElementById('quiz-next-btn').disabled = true;
            document.getElementById('quiz-next-btn').className = "px-5 py-2 bg-slate-200 text-slate-400 rounded-xl font-bold text-xs transition cursor-not-allowed";

            const chars = lettersData.map(l => l.char).filter(c => c !== item.char && !['Ъ','Ь','Ы'].includes(c));
            const opts = [item.char, ...chars.sort(() => 0.5 - Math.random()).slice(0, 3)].sort(() => 0.5 - Math.random());
            
            const optBox = document.getElementById('quiz-options');
            optBox.innerHTML = '';
            opts.forEach(c => {
                const b = document.createElement('button');
                b.className = "p-3 bg-white border-2 border-slate-200 hover:border-indigo-400 rounded-xl text-xl font-black text-slate-800 transition";
                b.textContent = c;
                b.onclick = () => selectAns(c, b, item);
                optBox.appendChild(b);
            });
        }
        function playQuizWordAudio() { playSound(quizSessionQuestions[currQIdx].ru); }
        function selectAns(c, btn, item) {
            if (isAns) return;
            isAns = true;
            document.getElementById('quiz-word-display').textContent = item.ru;
            const allBtns = document.getElementById('quiz-options').children;

            if (c === item.char) {
                btn.className = "p-3 bg-emerald-500 border-2 border-emerald-600 rounded-xl text-xl font-black text-white shadow-md";
                quizScore += 2; correctCount++;
                document.getElementById('quiz-score').textContent = quizScore;
                document.getElementById('quiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-emerald-600";
                document.getElementById('quiz-feedback').textContent = `✔ Правильно! (+2 балла)`;
                playSound(`Правильно! ${item.ru}`);
            } else {
                btn.className = "p-3 bg-rose-500 border-2 border-rose-600 rounded-xl text-xl font-black text-white shadow-md";
                for (let b of allBtns) {
                    if (b.textContent === item.char) b.className = "p-3 bg-emerald-500 border-2 border-emerald-600 rounded-xl text-xl font-black text-white shadow-md";
                }
                document.getElementById('quiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-rose-500";
                document.getElementById('quiz-feedback').textContent = `✖ Неправильно! Правильная буква: ${item.char}`;
                playSound(`Неправильно. Это ${item.ru}`);
            }
            document.getElementById('quiz-next-btn').disabled = false;
            document.getElementById('quiz-next-btn').className = "px-5 py-2 bg-rose-500 hover:bg-rose-600 text-white rounded-xl font-bold text-xs transition cursor-pointer shadow";
        }
        function goToNextQuestion() {
            if (currQIdx < 49) { currQIdx++; loadQuizQ(currQIdx); }
            else showResult();
        }
        function showResult() {
            document.getElementById('quiz-question-box').classList.add('hidden');
            document.getElementById('quiz-result-box').classList.remove('hidden');
            document.getElementById('res-total-score').textContent = quizScore;
            document.getElementById('res-correct-count').textContent = correctCount;
            document.getElementById('res-wrong-count').textContent = 50 - correctCount;
            const b = document.getElementById('res-grade-badge');
            if (quizScore >= 86) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-emerald-100 text-emerald-800"; b.textContent = "Отлично! (Оценка: 5)"; }
            else if (quizScore >= 70) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-sky-100 text-sky-800"; b.textContent = "Хорошо! (Оценка: 4)"; }
            else if (quizScore >= 50) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-amber-100 text-amber-800"; b.textContent = "Удовлетворительно (Оценка: 3)"; }
            else { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-rose-100 text-rose-800"; b.textContent = "Попробуйте ещё раз!"; }
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderAlphabet();
            initCanvas();
            renderSyllables();
            renderGenderSentences();
            renderTexts(1);
        });
    </script>
</body>
</html>
"""

# 4. Saytni chiqarish
components.html(app_html, height=1350, scrolling=True)
