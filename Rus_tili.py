import streamlit as st
import streamlit.components.v1 as components

# Sahifa sozlamalari
st.set_page_config(
    page_title="Rus tili 0 dan — Quljanova Shukurjon Zaribovna",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Barcha funksiyalarga ega to'liq interaktiv platforma (HTML + JS)
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
        body {
            font-family: 'Nunito', sans-serif;
            background: radial-gradient(circle at 10% 20%, rgba(220, 252, 231, 0.7) 0%, rgba(224, 242, 254, 0.7) 35%, rgba(254, 249, 195, 0.7) 70%, rgba(254, 226, 226, 0.5) 100%);
            background-attachment: fixed;
            min-height: 100vh;
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
<body class="text-slate-800 p-2 sm:p-4 selection:bg-yellow-300">

    <!-- HEADER -->
    <header class="bg-white/90 backdrop-blur-md border-b-4 border-emerald-400 rounded-3xl p-4 shadow-sm mb-6 max-w-6xl mx-auto flex flex-wrap justify-between items-center gap-4">
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
            <button onclick="switchTab('gender')" id="tab-gender" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-venus-mars text-indigo-500"></i> Rodlar
            </button>
            <button onclick="switchTab('texts')" id="tab-texts" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-book-reader text-sky-500"></i> 50 Matn
            </button>
            <button onclick="switchTab('quiz')" id="tab-quiz" class="px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100">
                <i class="fas fa-gamepad text-rose-500"></i> Viktorina (50 Test)
            </button>
        </nav>
    </header>

    <main class="max-w-6xl mx-auto space-y-6">

        <!-- 1. ALIFBO -->
        <section id="section-alphabet" class="space-y-4">
            <div class="bg-white/80 p-5 rounded-3xl border-2 border-emerald-100 shadow-sm flex flex-wrap justify-between items-center gap-2">
                <div>
                    <h2 class="text-xl font-black text-slate-800">Rus Alifbosi (33 ta Harf)</h2>
                    <p class="text-xs text-slate-600">Harfni eshitish uchun bosing!</p>
                </div>
                <div class="flex gap-2 text-xs font-bold">
                    <span class="px-3 py-1 bg-rose-100 text-rose-700 rounded-full">10 ta Unli</span>
                    <span class="px-3 py-1 bg-sky-100 text-sky-700 rounded-full">21 ta Undosh</span>
                    <span class="px-3 py-1 bg-amber-100 text-amber-700 rounded-full">2 ta Belgi</span>
                </div>
            </div>
            <div id="alphabet-grid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-3"></div>
        </section>

        <!-- 2. YOZMA DOSKA -->
        <section id="section-write" class="hidden space-y-4">
            <div class="bg-white/80 p-4 rounded-3xl border-2 border-amber-200 flex flex-wrap justify-between items-center gap-2">
                <h2 class="text-lg font-black text-slate-800">Yozma Shaklda Yozish (Propis)</h2>
                <div class="flex items-center gap-2">
                    <label class="text-xs font-bold text-slate-700">Harf:</label>
                    <select id="letter-select" onchange="changeCanvasLetter(this.value)" class="bg-amber-50 border-2 border-amber-300 font-extrabold text-amber-700 rounded-xl px-3 py-1.5 text-sm"></select>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
                <div class="lg:col-span-2 bg-white rounded-3xl p-4 border-2 border-amber-200 shadow-sm flex flex-col items-center">
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
                            <button onclick="clearCanvas()" class="px-3 py-1 bg-rose-100 text-rose-700 rounded-lg text-xs font-bold">Tozalash</button>
                            <button onclick="speakCurrentCanvasLetter()" class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-lg text-xs font-bold">Eshitish</button>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-3xl p-5 border shadow-sm flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-2">
                            <span id="canvas-card-badge" class="px-2.5 py-0.5 bg-rose-100 text-rose-700 text-xs font-bold rounded-full">UNLI</span>
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

        <!-- 3. RODLAR -->
        <section id="section-gender" class="hidden space-y-4">
            <div class="bg-white/80 p-5 rounded-3xl border-2 border-indigo-100">
                <h2 class="text-xl font-black text-slate-800">Rus Tilida Otlarning Rodlari</h2>
                <p class="text-xs text-slate-600 mt-1">Har bir ot quyidagi 3 ta rodning biriga tegishli bo'ladi:</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <div class="bg-white p-5 rounded-3xl border-t-8 border-sky-500 border shadow-sm">
                    <h3 class="text-lg font-black text-sky-600 mb-1">Мужской род (ОН)</h3>
                    <p class="text-xs text-slate-500 mb-3">Undosh harflar, -й yoki -ь bilan tugaydi.</p>
                    <div class="space-y-2 text-sm">
                        <div onclick="playSound('Стол, Дом, Брат')" class="p-2.5 bg-sky-50 rounded-xl cursor-pointer font-bold">Стол, Дом, Брат <span class="text-xs text-slate-400 block font-normal">Stol, Uy, Aka</span></div>
                        <div onclick="playSound('Чай, Музей')" class="p-2.5 bg-sky-50 rounded-xl cursor-pointer font-bold">Чай, Музей <span class="text-xs text-slate-400 block font-normal">Choy, Muzey (-й)</span></div>
                        <div onclick="playSound('Словарь, День')" class="p-2.5 bg-sky-50 rounded-xl cursor-pointer font-bold">Словарь, День <span class="text-xs text-slate-400 block font-normal">Lug'at, Kun (-ь)</span></div>
                    </div>
                </div>
                <div class="bg-white p-5 rounded-3xl border-t-8 border-rose-500 border shadow-sm">
                    <h3 class="text-lg font-black text-rose-600 mb-1">Женский род (ОНА)</h3>
                    <p class="text-xs text-slate-500 mb-3">-а, -я yoki -ь bilan tugaydi.</p>
                    <div class="space-y-2 text-sm">
                        <div onclick="playSound('Книга, Мама, Ручка')" class="p-2.5 bg-rose-50 rounded-xl cursor-pointer font-bold">Книга, Мама, Ручка <span class="text-xs text-slate-400 block font-normal">Kitob, Ona, Ruchka (-а)</span></div>
                        <div onclick="playSound('Семья, Земля')" class="p-2.5 bg-rose-50 rounded-xl cursor-pointer font-bold">Семья, Земля <span class="text-xs text-slate-400 block font-normal">Oila, Yer (-я)</span></div>
                        <div onclick="playSound('Тетрадь, Ночь')" class="p-2.5 bg-rose-50 rounded-xl cursor-pointer font-bold">Тетрадь, Ночь <span class="text-xs text-slate-400 block font-normal">Daftar, Tun (-ь)</span></div>
                    </div>
                </div>
                <div class="bg-white p-5 rounded-3xl border-t-8 border-amber-500 border shadow-sm">
                    <h3 class="text-lg font-black text-amber-600 mb-1">Средний род (ОНО)</h3>
                    <p class="text-xs text-slate-500 mb-3">-о, -е, -ё yoki -мя bilan tugaydi.</p>
                    <div class="space-y-2 text-sm">
                        <div onclick="playSound('Окно, Письмо')" class="p-2.5 bg-amber-50 rounded-xl cursor-pointer font-bold">Окно, Письмо <span class="text-xs text-slate-400 block font-normal">Deraza, Xat (-о)</span></div>
                        <div onclick="playSound('Море, Солнце')" class="p-2.5 bg-amber-50 rounded-xl cursor-pointer font-bold">Море, Солнце <span class="text-xs text-slate-400 block font-normal">Dengiz, Quyosh (-е)</span></div>
                        <div onclick="playSound('Имя, Время')" class="p-2.5 bg-amber-50 rounded-xl cursor-pointer font-bold">Имя, Время <span class="text-xs text-slate-400 block font-normal">Ism, Vaqt (-мя)</span></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. MATNLAR -->
        <section id="section-texts" class="hidden space-y-4">
            <div class="bg-white/80 p-4 rounded-3xl border-2 border-sky-100 flex justify-between items-center">
                <h2 class="text-lg font-black text-slate-800">50 ta O'qish Matni</h2>
                <span class="text-xs font-bold bg-sky-100 text-sky-700 px-3 py-1 rounded-xl">Jami: 50 ta</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="texts-container"></div>
            <div class="flex justify-center gap-2 mt-4" id="texts-pagination"></div>
        </section>

        <!-- 5. 50 TA TEST VIKTORINA (200 TA SO'Z BAZASI BILAN) -->
        <section id="section-quiz" class="hidden max-w-2xl mx-auto space-y-4">
            <div id="quiz-question-box" class="bg-white rounded-3xl p-6 border-2 border-rose-200 shadow-sm">
                <div class="flex justify-between items-center pb-3 border-b mb-4">
                    <span class="text-sm font-black text-slate-700">Savol: <span id="quiz-current-num" class="text-rose-500">1</span> / 50</span>
                    <span class="text-sm font-black text-emerald-600">Ball: <span id="quiz-score">0</span> / 100</span>
                </div>
                <div class="w-full bg-slate-100 h-2 rounded-full overflow-hidden mb-4">
                    <div id="quiz-progress-bar" class="bg-emerald-500 h-full w-[2%] transition-all"></div>
                </div>
                <div class="p-6 bg-slate-50 rounded-2xl text-center border">
                    <span class="text-xs font-bold text-rose-500 bg-rose-50 px-3 py-1 rounded-full">So'zning birinchi harfini toping!</span>
                    <h3 id="quiz-word-display" class="text-3xl font-black text-slate-800 my-3">_ рбуз</h3>
                    <p id="quiz-uz-translation" class="text-sm font-semibold text-slate-500 mb-3">Tarjimasi: Tarvuz</p>
                    <button onclick="playQuizWordAudio()" class="px-3 py-1.5 bg-sky-500 hover:bg-sky-600 text-white rounded-xl text-xs font-bold inline-flex items-center gap-1 shadow">
                        <i class="fas fa-volume-high"></i> Eshitish
                    </button>
                </div>

                <div class="grid grid-cols-2 gap-3 mt-4" id="quiz-options"></div>
                <div id="quiz-feedback" class="mt-3 text-center font-bold text-sm h-6"></div>
                <div class="mt-4 flex justify-end">
                    <button id="quiz-next-btn" onclick="goToNextQuestion()" disabled class="px-5 py-2 bg-slate-200 text-slate-400 rounded-xl font-bold text-xs transition cursor-not-allowed">
                        Keyingi savol ➜
                    </button>
                </div>
            </div>

            <!-- Natija ekrani -->
            <div id="quiz-result-box" class="hidden bg-white rounded-3xl p-8 border-2 border-emerald-300 text-center space-y-4">
                <div class="w-20 h-20 mx-auto rounded-full bg-emerald-500 text-white text-3xl flex items-center justify-center shadow-lg">
                    <i class="fas fa-award"></i>
                </div>
                <h3 class="text-2xl font-black text-slate-800">Sinov Yakunlandi!</h3>
                <div class="grid grid-cols-3 gap-2 max-w-sm mx-auto p-3 bg-slate-50 rounded-2xl">
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Ball</span><span id="res-total-score" class="text-xl font-black text-emerald-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">To'g'ri</span><span id="res-correct-count" class="text-xl font-black text-sky-600">0</span></div>
                    <div class="p-2 bg-white rounded-xl shadow-sm"><span class="text-xs text-slate-400 block font-bold">Xato</span><span id="res-wrong-count" class="text-xl font-black text-rose-500">0</span></div>
                </div>
                <div id="res-grade-badge" class="inline-block px-4 py-2 rounded-xl text-xs font-bold"></div>
                <div>
                    <button onclick="startQuizSession()" class="px-6 py-2.5 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl font-bold text-xs shadow-md">
                        Qaytadan boshlash (Yangi 50 ta savol)
                    </button>
                </div>
            </div>
        </section>

    </main>

    <footer class="mt-8 text-center text-xs font-bold text-slate-500 pb-4">
        © Quljanova Shukurjon Zaribovna — Rus tilini o'rganish platformasi
    </footer>

    <script>
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
            { ru: 'Яблоко', uz: 'Olma', char: 'Я' }, { ru: 'Ягода', uz: 'Rezavor meva', char: 'Я' }, { ru: 'Язык', uz: 'Til', char: 'Я' }, { ru: 'Яйцо', uz: 'Tuxum', char: 'Я' }, { ru: 'Якорь', uz: 'Langar', char: 'Я' },
            { ru: 'Сыр', uz: 'Pishloq', char: 'С' }, { ru: 'Дым', uz: 'Tutun', char: 'Д' }, { ru: 'Бык', uz: 'Ho‘kiz', char: 'Б' }, { ru: 'Мышь', uz: 'Sichqon', char: 'М' }, { ru: 'Рысь', uz: 'Silovsin', char: 'Р' },
            { ru: 'Картина', uz: 'Rasm', char: 'К' }, { ru: 'Зеркаlo', uz: 'Oyna', char: 'З' }, { ru: 'Подушка', uz: 'Yostiq', char: 'П' }, { ru: 'Одеяло', uz: 'Ko‘rpa', char: 'О' },
            { ru: 'Платье', uz: 'Ko‘ylak', char: 'П' }, { ru: 'Пальто', uz: 'Palto', char: 'П' }, { ru: 'Ботинки', uz: 'Botinkalar', char: 'Б' }, { ru: 'Носки', uz: 'Paypoqlar', char: 'Н' },
            { ru: 'Вилка', uz: 'Sanchqi', char: 'В' }, { ru: 'Нож', uz: 'Pichoq', char: 'Н' }, { ru: 'Чайник', uz: 'Choynak', char: 'Ч' }, { ru: 'Сковорода', uz: 'Tova', char: 'С' },
            { ru: 'Кастрюля', uz: 'Qozon', char: 'К' }, { ru: 'Сахар', uz: 'Shakar', char: 'С' }, { ru: 'Соль', uz: 'Tuz', char: 'С' }, { ru: 'Масло', uz: 'Yog‘', char: 'М' },
            { ru: 'Мясо', uz: 'Go‘sht', char: 'М' }, { ru: 'Суп', uz: 'Sho‘rva', char: 'С' }, { ru: 'Каша', uz: 'Bo‘tqa', char: 'К' }, { ru: 'Салат', uz: 'Salat', char: 'С' },
            { ru: 'Морковь', uz: 'Sabzi', char: 'М' }, { ru: 'Картофель', uz: 'Kartoshka', char: 'К' }, { ru: 'Лук', uz: 'Piyoz', char: 'Л' }, { ru: 'Огурец', uz: 'Bodring', char: 'О' },
            { ru: 'Помидор', uz: 'Pomidor', char: 'П' }, { ru: 'Капуста', uz: 'Karam', char: 'К' }, { ru: 'Свекла', uz: 'Lavlagi', char: 'С' }, { ru: 'Чеснок', uz: 'Sarimsoq', char: 'Ч' },
            { ru: 'Виноград', uz: 'Uzum', char: 'В' }, { ru: 'Персик', uz: 'Shaftoli', char: 'П' }, { ru: 'Слива', uz: 'Olxo‘ri', char: 'С' }, { ru: 'Вишня', uz: 'Olcha', char: 'В' },
            { ru: 'Клубника', uz: 'Qulupnay', char: 'К' }, { ru: 'Малина', uz: 'Malina', char: 'М' }, { ru: 'Орех', uz: 'Yong‘oq', char: 'О' }, { ru: 'Мёд', uz: 'Asal', char: 'М' },
            { ru: 'Автомобиль', uz: 'Avtomobil', char: 'А' }, { ru: 'Самолёт', uz: 'Samolyot', char: 'С' }, { ru: 'Вертолёт', uz: 'Vertolyot', char: 'В' }, { ru: 'Корабль', uz: 'Kema', char: 'К' },
            { ru: 'Лодка', uz: 'Qayiq', char: 'Л' }, { ru: 'Велосипед', uz: 'Velosiped', char: 'В' }, { ru: 'Метро', uz: 'Metro', char: 'М' }, { ru: 'Трамвай', uz: 'Tramvay', char: 'Т' },
            { ru: 'Вокзал', uz: 'Vokzal', char: 'В' }, { ru: 'Аэропорт', uz: 'Aeroport', char: 'А' }, { ru: 'Мост', uz: 'Ko‘prik', char: 'М' }, { ru: 'Площадь', uz: 'Maydon', char: 'П' },
            { ru: 'Больница', uz: 'Shifoxona', char: 'Б' }, { ru: 'Аптека', uz: 'Dorixona', char: 'А' }, { ru: 'Магазин', uz: 'Do‘kon', char: 'М' }, { ru: 'Рынок', uz: 'Bozor', char: 'Р' },
            { ru: 'Музей', uz: 'Muzey', char: 'М' }, { ru: 'Театр', uz: 'Teatr', char: 'Т' }, { ru: 'Кино', uz: 'Kino', char: 'К' }, { ru: 'Стадион', uz: 'Stadion', char: 'С' }
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

        function playSound(text) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const u = new SpeechSynthesisUtterance(text);
                u.lang = 'ru-RU';
                u.rate = 0.85;
                window.speechSynthesis.speak(u);
            }
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
                            <button onclick="event.stopPropagation(); playSound('${item.char}');" class="w-6 h-6 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center text-xs">
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
            ['alphabet', 'write', 'gender', 'texts', 'quiz'].forEach(t => {
                document.getElementById(`section-${t}`).classList.add('hidden');
                document.getElementById(`tab-${t}`).className = "px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold bg-white text-slate-600 hover:bg-slate-100";
            });
            document.getElementById(`section-${tabId}`).classList.remove('hidden');
            const color = tabId === 'alphabet' ? 'bg-emerald-500' : (tabId === 'write' ? 'bg-amber-500' : (tabId === 'gender' ? 'bg-indigo-500' : (tabId === 'texts' ? 'bg-sky-500' : 'bg-rose-500')));
            document.getElementById(`tab-${tabId}`).className = `px-3 py-2 rounded-xl text-xs sm:text-sm font-extrabold ${color} text-white shadow-md`;
            if (tabId === 'quiz' && quizSessionQuestions.length === 0) startQuizSession();
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
                            <button onclick="playSound('${t.ru.replace(/'/g, "\\'")}')" class="text-xs bg-sky-500 text-white px-2.5 py-1 rounded-lg font-bold">🔊 Eshitish</button>
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

        // VIKTORINA
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
                btn.className = "p-3 bg-emerald-500 border-2 border-emerald-600 rounded-xl text-xl font-black text-white";
                quizScore += 2; correctCount++;
                document.getElementById('quiz-score').textContent = quizScore;
                document.getElementById('quiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-emerald-600";
                document.getElementById('quiz-feedback').textContent = `✔ Barakalla! To'g'ri javob (+2 ball)`;
                playSound(`Правильно! ${item.ru}`);
            } else {
                btn.className = "p-3 bg-rose-500 border-2 border-rose-600 rounded-xl text-xl font-black text-white";
                for (let b of allBtns) {
                    if (b.textContent === item.char) b.className = "p-3 bg-emerald-500 border-2 border-emerald-600 rounded-xl text-xl font-black text-white";
                }
                document.getElementById('quiz-feedback').className = "mt-3 text-center font-bold text-sm h-6 text-rose-500";
                document.getElementById('quiz-feedback').textContent = `✖ Noto'g'ri! To'g'ri harf: ${item.char}`;
                playSound(`Неправильно. Это ${item.ru}`);
            }
            document.getElementById('quiz-next-btn').disabled = false;
            document.getElementById('quiz-next-btn').className = "px-5 py-2 bg-rose-500 text-white rounded-xl font-bold text-xs transition cursor-pointer shadow";
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
            if (quizScore >= 86) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-emerald-100 text-emerald-800"; b.textContent = "A'lo (5 Baho)"; }
            else if (quizScore >= 70) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-sky-100 text-sky-800"; b.textContent = "Yaxshi (4 Baho)"; }
            else if (quizScore >= 50) { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-amber-100 text-amber-800"; b.textContent = "Qoniqarli (3 Baho)"; }
            else { b.className = "inline-block px-4 py-2 rounded-xl text-xs font-bold bg-rose-100 text-rose-800"; b.textContent = "Qayta topshiring"; }
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderAlphabet();
            initCanvas();
            renderTexts(1);
        });
    </script>
</body>
</html>
"""

# Streamlit ilovasida butun veb-portalni chiqarish
components.html(app_html, height=950, scrolling=True)
