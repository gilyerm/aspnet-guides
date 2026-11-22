# Part 2 of the web basics pages. Run through build_web.py (it provides pg, concept, table, c, page, code, box).

FONT_LINK = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;700&display=swap">'
ICONS_LINK = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">'

# =====================================================================
# עיצוב שנראה מקצועי
# =====================================================================
page('web-design', 'עיצוב שנראה מקצועי', 'גופנים בעברית, אייקונים, סרטונים ומפות, וכמה כללי עיצוב שעושים את כל ההבדל',
     '<strong>💡 על מה העמוד הזה?</strong> אתר יכול לעבוד מצוין ועדיין להיראות "של תלמיד". רוב ההבדל לא בקוד מסובך, אלא בכמה בחירות פשוטות: גופן טוב, אייקונים, רווחים וצבעים שמתאימים זה לזה. מומלץ להכיר קודם את <a href="web-css.html">יסודות CSS</a>.',
     [
         ('1. גופן בעברית מ-Google Fonts', [
             '<p>הגופן שמגיע כברירת מחדל לא מיועד לעברית. ב-<a href="https://fonts.google.com/?subset=hebrew" target="_blank">Google Fonts</a> יש גופנים חינמיים שנראים מצוין בעברית, למשל <strong>Rubik</strong>, <strong>Heebo</strong>, <strong>Assistant</strong> ו-<strong>Varela Round</strong>.</p>',
             pg(FONT_LINK + '''
<h2 class="before">לפני: הגופן הרגיל</h2>
<p class="before">ברוכים הבאים לחנות שלנו! כאן תמצאו את כל הציוד לבית הספר.</p>
<hr>
<h2 class="after">אחרי: הגופן Rubik</h2>
<p class="after">ברוכים הבאים לחנות שלנו! כאן תמצאו את כל הציוד לבית הספר.</p>''', css='''
.before {
    font-family: "Times New Roman", serif;
}

.after {
    font-family: "Rubik", sans-serif;
}''', title='נסו: בשורת ה-link שבראש ה-HTML, ובשורה של .after, החליפו Rubik ב-Heebo', height=260),
             '<h3>איך מוסיפים לפרויקט</h3>',
             '<ul class="step-list"><li>ב-<a href="https://fonts.google.com/?subset=hebrew" target="_blank">fonts.google.com</a> בחרו גופן, לחצו <strong>Get font</strong> ואז <strong>Get embed code</strong>. העתיקו את שורת ה-' + c('<link>') + ' שמופיעה שם.</li>'
             '<li>ב-' + c('Views/Shared/_Layout.cshtml') + ', הדביקו אותה בתוך ה-' + c('<head>') + ', <strong>לפני</strong> השורה של ' + c('site.css') + '. לדוגמה:' + code(FONT_LINK) + '</li>'
             '<li>ב-' + c('wwwroot/css/site.css') + ', הוסיפו:' + code('''
body {
    font-family: "Rubik", sans-serif;
}''') + '</li></ul>',
             '<div class="checkpoint">כל האתר בגופן החדש, כולל התפריט והכפתורים.</div>',
         ]),
         ('2. אייקונים', [
             '<p><a href="https://icons.getbootstrap.com/" target="_blank">Bootstrap Icons</a> היא ספרייה של כ-2,000 אייקונים חינמיים, שמתאימה ל-Bootstrap. כל אייקון הוא תגית ' + c('<i>') + ' עם class.</p>',
             pg(ICONS_LINK + '''
<p>
    <i class="bi bi-cart"></i> עגלה
    &nbsp; <i class="bi bi-heart-fill" style="color: crimson"></i> אהבתי
    &nbsp; <i class="bi bi-trash"></i> מחיקה
    &nbsp; <i class="bi bi-person-circle"></i> הפרופיל שלי
</p>

<button class="btn-icon"><i class="bi bi-plus-lg"></i> הוספת מוצר</button>
<button class="btn-icon"><i class="bi bi-search"></i> חיפוש</button>''', css='''
.bi {
    font-size: 1.3rem;
    vertical-align: middle;
}

.btn-icon {
    padding: 8px 14px;
    font-size: 16px;
    border: 1px solid #888;
    border-radius: 8px;
    background: white;
    cursor: pointer;
}''', title='נסו: באתר icons.getbootstrap.com חפשו אייקון, והחליפו bi-cart בשם שלו', height=170),
             '<h3>איך מוסיפים לפרויקט</h3>',
             '<p>ב-' + c('_Layout.cshtml') + ', בתוך ה-' + c('<head>') + ', הוסיפו:</p>' + code(ICONS_LINK) +
             '<p>ומעכשיו בכל עמוד: ' + c('<i class="bi bi-cart"></i>') + '. את השם של כל אייקון מוצאים באתר, בחיפוש באנגלית (cart, heart, trash, user...).</p>',
             box('explanation', '💡 גם אימוג\'י עובד!', 'בכפתורים פשוטים אפשר גם לכתוב אימוג\'י ישירות בטקסט (🛒 ❤️ 🗑️). זה פחות אחיד מאייקונים, אבל לא צריך להוסיף כלום.'),
         ]),
         ('3. סרטון YouTube ומפה', [
             '<p>אתרים כמו YouTube ו-Google Maps נותנים קוד מוכן להטמעה (embed). זו תגית ' + c('<iframe>') + ': "חלון" לאתר אחר בתוך העמוד שלכם.</p>',
             '<h3>סרטון YouTube</h3>',
             '<ul class="step-list"><li>ב-YouTube, מתחת לסרטון, לחצו <strong>שיתוף (Share)</strong> ואז <strong>הטמעה (Embed)</strong>.</li><li>העתיקו את הקוד שמופיע (מתחיל ב-' + c('<iframe') + ') והדביקו ב-View שלכם.</li><li>כדי שהסרטון יתאים לרוחב המסך, עטפו אותו ב-div של Bootstrap:' + code('''
<div class="ratio ratio-16x9">
    <iframe src="https://www.youtube.com/embed/VIDEO_ID" allowfullscreen></iframe>
</div>''') + 'ב-' + c('VIDEO_ID') + ' יופיע הקוד של הסרטון, אם העתקתם מ-YouTube.</li></ul>',
             '<h3>מפה של Google</h3>',
             '<p>הדרך הקלה: כתובת עם ' + c('q=') + ' ושם המקום. למשל, מפה של "תל אביב":</p>',
             code('''
<div class="ratio ratio-16x9">
    <iframe src="https://maps.google.com/maps?q=Tel%20Aviv&output=embed"></iframe>
</div>'''),
             '<p>וכך זה נראה:</p><div class="screenshot" style="padding:0"><iframe src="https://maps.google.com/maps?q=Tel%20Aviv&amp;output=embed" style="width:100%;height:280px;border:0;border-radius:8px" loading="lazy" title="מפה לדוגמה"></iframe></div>',
             '<p class="change-note">החליפו את ' + c('Tel%20Aviv') + ' בכתובת שלכם (' + c('%20') + ' = רווח).</p>',
         ]),
         ('4. כללי עיצוב שעושים את כל ההבדל', [
             '<p>הנה אותו כרטיס פעמיים. שניהם "עובדים", אבל ההבדל ברור. אחרי הדוגמה מוסבר כל כלל:</p>',
             pg(FONT_LINK + '''
<div class="bad">
    <h2>מבצע מטורף!!!</h2>
    <p>מחברות במחיר מיוחד רק השבוע!!! אל תפספסו!!! כל המחברות בחנות במחיר מוזל.</p>
    <button>לקנייה</button>
</div>

<div class="good">
    <h2>מבצע השבוע</h2>
    <p>כל המחברות בחנות ב-10 ₪ בלבד, עד יום חמישי.</p>
    <button>לקנייה</button>
</div>''', css='''
/* לפני: יותר מדי צבעים, בלי רווחים, קשה לקרוא */
.bad {
    background: yellow;
    color: red;
    font-family: "Comic Sans MS";
    border: 4px dashed blue;
    margin-bottom: 20px;
}
.bad h2 { color: green; text-align: center; }
.bad button { background: purple; color: lime; }

/* אחרי: צבע אחד מוביל, רווחים, ניגודיות טובה */
.good {
    font-family: "Rubik", sans-serif;
    background: white;
    color: #333;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.12);
    max-width: 400px;
}
.good h2 { color: #4c1d95; margin-top: 0; }
.good p { line-height: 1.6; }
.good button {
    background: #4c1d95;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
}''', title='נסו: שנו את הצבע #4c1d95 בשלושת המקומות לצבע אחר', height=360),
             table(['כלל', 'למה', 'איך'], [
                 ['<strong>2-3 צבעים בלבד</strong>', 'יותר צבעים = בלגן. צבע אחד "מוביל" (לכפתורים ולכותרות), ושאר העמוד בשחור, אפור ולבן.', 'בחרו צבע מוביל אחד, והשתמשו בו בכל האתר.'],
                 ['<strong>ניגודיות</strong>', 'טקסט צהוב על לבן, או אפור בהיר על אפור, קשה לקרוא.', 'טקסט כהה על רקע בהיר (או הפוך).'],
                 ['<strong>רווחים</strong>', 'צפיפות מעייפת את העין. רווח "נותן לתוכן לנשום".', c('padding') + ' בתוך קופסאות, ' + c('margin') + ' ביניהן, ' + c('line-height: 1.6') + ' בטקסט.'],
                 ['<strong>היררכיה</strong>', 'צריך לראות מיד מה הכי חשוב.', 'כותרת גדולה, טקסט רגיל, ופעולה אחת בולטת (כפתור בצבע המוביל).'],
                 ['<strong>עקביות</strong>', 'אתר שבו כל עמוד נראה אחרת נראה לא גמור.', 'אותו גופן, אותם צבעים, אותו סגנון כפתורים בכל העמודים. (בשביל זה יש ' + c('site.css') + ' ומשתני CSS, ראו <a href="web-css2.html">CSS חלק ב\'</a>.)'],
                 ['<strong>פחות זה יותר</strong>', 'סימני קריאה, אנימציות ומסגרות צועקות מסיחים את הדעת.', 'כל קישוט צריך סיבה.'],
             ]),
             box('explanation', '💡 לא בטוחים באילו צבעים לבחור?', 'באתרים כמו <a href="https://coolors.co" target="_blank">coolors.co</a> יש פלטות מוכנות של צבעים שמתאימים זה לזה. לחצו רווח כדי לקבל פלטה חדשה, והעתיקו את הקודים.'),
         ]),
     ],
     ['גופן מ-Google Fonts: שורת link ב-Layout, ו-font-family ב-site.css.',
      'אייקונים: Bootstrap Icons, שורת link אחת, ואז ' + c('<i class="bi bi-...">') + '.',
      'סרטונים ומפות: קוד הטמעה (iframe), עטוף ב-' + c('ratio ratio-16x9') + '.',
      'עיצוב: צבע מוביל אחד, ניגודיות, רווחים, היררכיה ועקביות.'],
     'השראה: עברו על אתרים שאתם אוהבים, ופתחו F12 ← Elements כדי לראות איזה גופן, צבעים ורווחים הם בחרו.')

# =====================================================================
# CSS חלק ב'
# =====================================================================
page('web-css2', "CSS חלק ב'", 'מיקום, משתני צבע, Grid ואנימציות',
     '<strong>💡 על מה העמוד הזה?</strong> המשך של <a href="web-css.html">יסודות CSS</a>, למי שכבר מרגיש בנוח עם סלקטורים, צבעים ו-Box Model. כאן: איך להצמיד דברים למקום, להגדיר צבעים פעם אחת לכל האתר, לבנות פריסות מורכבות, ולהוסיף תנועה.',
     [
         ('1. משתני CSS: הצבעים של האתר במקום אחד', [
             concept('משתנה CSS', f'שם שמחזיק ערך. מגדירים פעם אחת ב-{c(":root")} (עם שני מקפים בהתחלה), ומשתמשים עם {c("var(...)")}.',
                     'ככה, כשרוצים להחליף את הצבע של כל האתר, משנים שורה אחת.'),
             pg('''
<h2>החנות שלנו</h2>
<p>כל הצבעים בעמוד מגיעים משלושה משתנים.</p>
<button class="main-btn">לקנייה</button>
<span class="tag">חדש!</span>''', css='''
:root {
    --main-color: #4c1d95;
    --light-color: #ede9fe;
    --radius: 10px;
}

h2 {
    color: var(--main-color);
}

.main-btn {
    background: var(--main-color);
    color: white;
    border: none;
    padding: 10px 18px;
    border-radius: var(--radius);
}

.tag {
    background: var(--light-color);
    color: var(--main-color);
    padding: 4px 10px;
    border-radius: var(--radius);
}''', title='נסו: שנו רק את --main-color ל-teal. כל העמוד משתנה', height=180),
             box('explanation', '💡 בפרויקט:', 'שימו את ה-' + c(':root') + ' בראש ' + c('site.css') + ', והשתמשו במשתנים בכל העיצוב שלכם.'),
         ]),
         ('2. מיקום (position)', [
             table(['ערך', 'מה הוא עושה', 'שימוש נפוץ'], [
                 [c('sticky'), 'האלמנט גולל כרגיל, עד שהוא מגיע לראש המסך, ואז "נדבק" שם.', 'תפריט שתמיד נשאר למעלה.'],
                 [c('fixed'), 'קבוע במקום על המסך, גם כשגוללים.', 'כפתור צף ("וואטסאפ", "חזרה למעלה").'],
                 [c('relative') + ' + ' + c('absolute'), c('absolute') + ' ממקם ביחס להורה הקרוב שיש לו ' + c('relative') + '.', 'תווית "מבצע!" בפינה של כרטיס.'],
             ]),
             pg('''
<nav class="sticky-bar">תפריט שנדבק למעלה (גללו בחלון הזה)</nav>

<div class="card">
    <span class="badge">מבצע!</span>
    <h3>מחברת</h3>
    <p>12 ₪</p>
</div>

<p>טקסט כדי שיהיה מה לגלול.</p>
<p>עוד טקסט.</p>
<p>ועוד.</p>
<p>ועוד קצת.</p>
<p>כמעט נגמר.</p>
<p>סוף.</p>

<button class="float-btn">💬</button>''', css='''
.sticky-bar {
    position: sticky;
    top: 0;
    background: #4c1d95;
    color: white;
    padding: 10px;
}

.card {
    position: relative;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 15px;
    margin: 15px 0;
    width: 200px;
}

.badge {
    position: absolute;
    top: -10px;
    left: -10px;
    background: crimson;
    color: white;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 14px;
}

.float-btn {
    position: fixed;
    bottom: 15px;
    left: 15px;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    border: none;
    background: seagreen;
    font-size: 22px;
}''', title='נסו: גללו בתוצאה. ואז שנו left של .badge ל-right', height=260),
         ]),
         ('3. CSS Grid: שורות ועמודות', [
             concept('Grid', f'פריסה בשתי ממדים: מגדירים על העוטף כמה עמודות יהיו, והילדים מסתדרים בתוכן לבד. {c("repeat(3, 1fr)")} פירושו "3 עמודות ברוחב שווה" ({c("fr")} = חלק מהמקום הפנוי).',
                     'מתי Flexbox ומתי Grid? Flexbox לשורה אחת (תפריט, כפתורים). Grid לרשת שלמה (גלריה, לוח).'),
             pg('''
<div class="gallery">
    <div>1</div><div>2</div><div>3</div>
    <div>4</div><div class="wide">5 (רחב)</div>
    <div>6</div><div>7</div><div>8</div>
</div>''', css='''
.gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.gallery div {
    background: lightsteelblue;
    padding: 25px;
    text-align: center;
    font-size: 20px;
    border-radius: 8px;
}

.gallery .wide {
    grid-column: span 2;
    background: steelblue;
    color: white;
}''', title='נסו: repeat(4, 1fr), ואחר כך span 3', height=280),
             pg('''
<div class="auto">
    <div>🍎</div><div>🍌</div><div>🍇</div><div>🍓</div>
    <div>🍒</div><div>🥝</div><div>🍍</div><div>🥭</div>
</div>
<p>הקטינו את רוחב החלון: מספר העמודות משתנה לבד!</p>''', css='''
.auto {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
    gap: 10px;
}

.auto div {
    background: #fef3c7;
    font-size: 40px;
    text-align: center;
    padding: 15px;
    border-radius: 8px;
}''', title='קסם: גלריה שמתאימה את עצמה לכל מסך, בשורה אחת', height=230),
         ]),
         ('4. אנימציות', [
             concept('@keyframes', f'מגדירים "תסריט" של תנועה: איך האלמנט נראה בהתחלה ({c("from")}) ובסוף ({c("to")}), או באחוזים לאורך הדרך. אחר כך מפעילים אותו עם {c("animation")}.'),
             pg('''
<div class="pulse">❤️</div>
<div class="spin">⚙️</div>
<p class="fade">טקסט שמופיע לאט</p>''', css='''
@keyframes beat {
    0%   { transform: scale(1); }
    50%  { transform: scale(1.3); }
    100% { transform: scale(1); }
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

@keyframes appear {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.pulse { font-size: 50px; display: inline-block; animation: beat 1s infinite; }
.spin  { font-size: 50px; display: inline-block; animation: rotate 3s linear infinite; }
.fade  { font-size: 22px; animation: appear 2s; }''', title='נסו: שנו 1s ל-0.3s, ו-3s ל-10s', height=190),
             table(['חלק ב-animation', 'פירוש'], [
                 [c('beat'), 'שם ה-@keyframes.'],
                 [c('1s'), 'כמה זמן לוקח סיבוב אחד.'],
                 [c('infinite'), 'לחזור בלי סוף. בלי זה, פעם אחת.'],
                 [c('linear'), 'מהירות קבועה (בלי האטה בהתחלה ובסוף).'],
             ]),
             box('warning', '⚠️ במידה:', 'אנימציה אחת קטנה מוסיפה חיים. הרבה אנימציות מסיחות את הדעת ומעייפות. השתמשו בזה על דבר אחד שרוצים שישימו אליו לב.'),
         ]),
     ],
     ['משתני CSS (' + c('--name') + ' ו-' + c('var()') + '): צבעים וגדלים במקום אחד.',
      'position: sticky לתפריט, fixed לכפתור צף, relative + absolute לתווית על כרטיס.',
      'Grid לרשתות: ' + c('grid-template-columns: repeat(3, 1fr)') + ', ו-auto-fill לגלריה שמתאימה את עצמה.',
      'אנימציות עם @keyframes ו-animation, במידה.'],
     'משחק שמלמד Grid: <a href="https://cssgridgarden.com/#he" target="_blank">Grid Garden</a> (יש גם בעברית). ועוד על אנימציות: <a href="https://www.w3schools.com/css/css3_animations.asp" target="_blank">w3schools</a>.')

# =====================================================================
# JavaScript חלק ב'
# =====================================================================
page('web-js2', "JavaScript חלק ב'", 'פונקציות, אובייקטים, טיימרים, מספרים אקראיים וזיכרון בדפדפן',
     '<strong>💡 על מה העמוד הזה?</strong> המשך של <a href="web-js.html">יסודות JavaScript</a>, למי שכבר יודע למצוא אלמנט, להגיב ללחיצה ולשנות טקסט. כאן נבנה דברים קצת יותר מעניינים: כרטיסים מתוך נתונים, שעון, משחקים קטנים.',
     [
         ('1. פונקציות עם פרמטרים', [
             concept('פרמטר', 'ערך שמעבירים לפונקציה כשקוראים לה. ככה אותה פונקציה עושה דברים שונים לפי מה שמקבלת.',
                     f'דוגמה: {c("function greet(name) { ... }")} ואז {c("greet(\"דנה\")")} או {c("greet(\"יוסי\")")}. עם {c("return")} הפונקציה גם מחזירה תוצאה.'),
             pg('''
<button id="b1">חשב מחיר עם מע"מ</button>
<p id="out"></p>''', js='''
function withVat(price) {
    return price * 1.18;
}

function show(text) {
    document.getElementById("out").textContent = text;
}

document.getElementById("b1").addEventListener("click", function () {
    var total = withVat(100);
    show("100 ₪ עם מע\\"מ: " + total.toFixed(2) + " ₪");
});''', title='נסו: חשבו גם ל-250', height=130),
         ]),
         ('2. אובייקטים ו-template literals', [
             concept('אובייקט', f'כמה ערכים שקשורים זה לזה, בתוך {c("{ }")}, כל אחד עם שם. בדיוק כמו מודל ב-C# (מדריך 10).',
                     f'דוגמה: {c("{ name: \"עט\", price: 5 }")}. ניגשים עם נקודה: {c("product.name")}.'),
             concept('Template literal', f'מחרוזת בתוך גרשיים הפוכים ({c("`")}, המקש משמאל ל-1), שאפשר להכניס לתוכה ערכים עם {c("${...}")}. נוח מאוד לבנות HTML.',
                     f'דוגמה: {c("`שלום ${name}!`")} במקום {c("\"שלום \" + name + \"!\"")}.'),
             pg('''
<div id="products"></div>''', css='''
#products {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
}

.card {
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 12px;
    width: 120px;
    text-align: center;
}

.price { color: green; font-weight: bold; }''', js='''
var products = [
    { name: "עט", price: 5, emoji: "🖊️" },
    { name: "מחברת", price: 12, emoji: "📓" },
    { name: "תיק", price: 150, emoji: "🎒" }
];

var html = "";
products.forEach(function (p) {
    html += `
        <div class="card">
            <div style="font-size: 40px">${p.emoji}</div>
            <h4>${p.name}</h4>
            <div class="price">${p.price} ₪</div>
        </div>`;
});

document.getElementById("products").innerHTML = html;''', title='נסו: הוסיפו מוצר רביעי למערך', height=220),
             box('explanation', '💡 זה הבסיס ל-fetch:', 'כשהשרת מחזיר JSON (<a href="adv-d-fetch.html">מתקדם ד</a>), מקבלים בדיוק מערך של אובייקטים כזה, ובונים ממנו HTML באותה דרך.'),
         ]),
         ('3. טיימרים', [
             table(['פונקציה', 'מה היא עושה'], [
                 [c('setTimeout(function, 2000)'), 'מריצה את הפונקציה <strong>פעם אחת</strong>, אחרי 2000 מילישניות (2 שניות).'],
                 [c('setInterval(function, 1000)'), 'מריצה את הפונקציה <strong>שוב ושוב</strong>, כל שנייה.'],
                 [c('clearInterval(id)'), 'עוצרת setInterval.'],
             ]),
             pg('''
<h2 id="clock"></h2>
<p>ספירה לאחור: <strong id="count">10</strong></p>
<button id="start">התחל</button>''', js='''
// שעון שמתעדכן כל שנייה
setInterval(function () {
    document.getElementById("clock").textContent = new Date().toLocaleTimeString("he-IL");
}, 1000);

// ספירה לאחור
document.getElementById("start").addEventListener("click", function () {
    var n = 10;
    var timer = setInterval(function () {
        n = n - 1;
        document.getElementById("count").textContent = n;
        if (n === 0) {
            clearInterval(timer);
            document.getElementById("count").textContent = "🚀 המראה!";
        }
    }, 1000);
});''', title='נסו: שנו את הספירה להתחיל מ-5', height=180),
             pg('''
<div id="slide"></div>''', css='''
#slide {
    font-size: 80px;
    text-align: center;
    padding: 20px;
    transition: opacity 0.5s;
}''', js='''
var pictures = ["🌅", "🏖️", "🏔️", "🌃"];
var i = 0;

function showNext() {
    document.getElementById("slide").textContent = pictures[i];
    i = (i + 1) % pictures.length;
}

showNext();
setInterval(showNext, 1500);''', title='מצגת שמתחלפת לבד. נסו: הוסיפו תמונה, או שנו את המהירות', height=160),
             concept('מה זה % ?', f'שארית חלוקה. {c("(i + 1) % 4")} עובר 1, 2, 3, 0, 1, 2... כך המצגת חוזרת להתחלה אחרי התמונה האחרונה.'),
         ]),
         ('4. מספרים אקראיים: משחקים קטנים', [
             concept('Math.random', f'{c("Math.random()")} נותן מספר אקראי בין 0 ל-1. כדי לקבל מספר שלם בין 1 ל-6: {c("Math.floor(Math.random() * 6) + 1")}.'),
             pg('''
<button id="roll">🎲 הטל קובייה</button>
<span id="dice" style="font-size: 50px"></span>

<hr>
<p>חשבתי על מספר בין 1 ל-20. נחשו!</p>
<input type="number" id="guess" min="1" max="20">
<button id="check">בדוק</button>
<p id="hint"></p>''', js='''
var faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"];
document.getElementById("roll").addEventListener("click", function () {
    var n = Math.floor(Math.random() * 6);
    document.getElementById("dice").textContent = faces[n];
});

var secret = Math.floor(Math.random() * 20) + 1;
var tries = 0;
document.getElementById("check").addEventListener("click", function () {
    var g = Number(document.getElementById("guess").value);
    tries++;
    var hint = document.getElementById("hint");
    if (g === secret) {
        hint.textContent = "🎉 נכון! הצלחתם ב-" + tries + " ניסיונות";
    } else if (g < secret) {
        hint.textContent = "גבוה יותר ⬆️";
    } else {
        hint.textContent = "נמוך יותר ⬇️";
    }
});''', title='נסו: שנו את המשחק למספר בין 1 ל-100', height=250),
         ]),
         ('5. תכונות data-: כפתור אחד, הרבה פריטים', [
             '<p>כשיש הרבה כפתורים דומים (למשל "הוספה לעגלה" ליד כל מוצר), לא כותבים קוד לכל אחד. שומרים על כל כפתור מידע בתכונה שמתחילה ב-' + c('data-') + ', וקוראים אותה עם ' + c('dataset') + ':</p>',
             pg('''
<button class="add" data-name="עט" data-price="5">🖊️ עט</button>
<button class="add" data-name="מחברת" data-price="12">📓 מחברת</button>
<button class="add" data-name="תיק" data-price="150">🎒 תיק</button>
<p>בעגלה: <span id="items">ריק</span></p>
<p>סה"כ: <strong id="total">0</strong> ₪</p>''', js='''
var total = 0;
var names = [];

document.querySelectorAll(".add").forEach(function (btn) {
    btn.addEventListener("click", function () {
        names.push(btn.dataset.name);
        total += Number(btn.dataset.price);
        document.getElementById("items").textContent = names.join(", ");
        document.getElementById("total").textContent = total;
    });
});''', title='נסו: הוסיפו כפתור רביעי. אין צורך לשנות את ה-JavaScript!', height=190),
             box('explanation', '💡 בפרויקט:', 'ב-cshtml כותבים ' + c('data-id="@product.Id"') + ' בתוך ה-' + c('@foreach') + ', וכך כל כפתור "יודע" לאיזה מוצר הוא שייך (<a href="adv-d-fetch.html">מתקדם ד</a>).'),
         ]),
         ('6. localStorage: הדפדפן זוכר', [
             concept('localStorage', 'מקום קטן בדפדפן שבו אפשר לשמור טקסט, והוא נשאר גם אחרי רענון או סגירה של הדפדפן. כל משתמש, בדפדפן שלו בלבד.',
                     'מתאים להעדפות (מצב לילה, גודל טקסט). <strong>לא</strong> מתאים לנתונים חשובים או משותפים: אלה הולכים למסד הנתונים.'),
             table(['קוד', 'מה הוא עושה'], [
                 [c('localStorage.setItem("theme", "dark")'), 'שומר.'],
                 [c('localStorage.getItem("theme")'), 'קורא (או ' + c('null') + ' אם אין).'],
                 [c('localStorage.removeItem("theme")'), 'מוחק.'],
             ]),
             '<p>דוגמה: מצב לילה שנשמר. בדוגמה הזאת אין עורך חי, כי העורך בעמוד רץ בסביבה מוגנת שבה localStorage חסום. העתיקו אותה לעמוד בפרויקט שלכם:</p>',
             code('''
<button id="mode">🌙 מצב לילה</button>

<script>
    // בטעינת העמוד: אם נשמר מצב לילה, מפעילים אותו
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark");
    }

    document.getElementById("mode").addEventListener("click", function () {
        document.body.classList.toggle("dark");
        var isDark = document.body.classList.contains("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");
    });
</script>'''),
             '<p>וב-CSS:</p>',
             code('''
body.dark {
    background-color: #1e1e1e;
    color: #eee;
}'''),
             '<div class="checkpoint">הפעילו מצב לילה, ורעננו את העמוד (או סגרו ופתחו את הדפדפן). מצב הלילה נשאר!</div>',
         ]),
     ],
     ['פונקציה עם פרמטרים ו-return עושה דברים שונים לפי מה שמקבלת.',
      'מערך של אובייקטים + template literal (' + c('`${...}`') + ') = HTML שנבנה מנתונים.',
      'setTimeout לפעם אחת, setInterval לחזרה, clearInterval לעצירה.',
      'Math.random למשחקים, data- לכפתורים רבים, localStorage להעדפות.'],
     'המשך מצוין: <a href="https://javascript.info/" target="_blank">javascript.info</a> (באנגלית), או <a href="https://www.w3schools.com/js/" target="_blank">w3schools</a>.')
