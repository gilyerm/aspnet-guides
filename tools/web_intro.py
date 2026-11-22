# The intro page of the web basics section: what HTML, CSS and JavaScript are.
# Run through build_web.py (it provides pg, concept, table, c, page, code, box).

CARD_HTML = '''<div class="card">
    <div class="pic">🎒</div>
    <h3>תיק גב</h3>
    <p class="price">89 ₪</p>
    <button id="add">הוספה לעגלה</button>
    <p id="msg"></p>
</div>'''

CARD_CSS = '''body {
    font-family: system-ui, Arial, sans-serif;
    background: #f3f3f6;
}

.card {
    background: white;
    width: 220px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.12);
}

.pic {
    font-size: 60px;
}

.price {
    color: #16825d;
    font-size: 22px;
    font-weight: bold;
}

button {
    background: #68217a;
    color: white;
    border: none;
    padding: 10px 18px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
}'''

CARD_JS = '''let count = 0;

document.getElementById("add").addEventListener("click", function () {
    count++;
    document.getElementById("msg").textContent = "בעגלה: " + count;
});'''

STEPS = [
    ('שלב 1: רק HTML', 'html',
     '<strong>יש תוכן, אין עיצוב.</strong> הדפדפן יודע שיש כאן כותרת, פסקה וכפתור, ומציג אותם בעיצוב הרגיל שלו: שחור על לבן, אחד מתחת לשני. לחצו על הכפתור: לא קורה כלום.',
     CARD_HTML),
    ('שלב 2: מוסיפים CSS', 'css',
     '<strong>אותו HTML בדיוק, עם CSS.</strong> לא הוספנו אף מילה לתוכן. ה-CSS רק אמר לדפדפן איך להציג אותו: רקע, מסגרת מעוגלת, צבעים וגדלים. לחצו על הכפתור: עדיין לא קורה כלום.',
     CARD_CSS),
    ('שלב 3: מוסיפים JavaScript', 'javascript',
     '<strong>ועכשיו הכפתור עובד.</strong> ה-JavaScript מחכה ללחיצה, ובכל לחיצה משנה את הטקסט שמתחת לכפתור. לחצו כמה פעמים.',
     CARD_JS),
]


def layers_demo():
    tabs = ''.join(
        f'<button type="button" data-step="{i}"{" class=active" if i == 0 else ""} aria-pressed="{"true" if i == 0 else "false"}">{label}</button>'
        for i, (label, _, _, _) in enumerate(STEPS))
    notes = ''.join(
        f'<p class="layers-note" data-step="{i}"{"" if i == 0 else " hidden"}>{note}</p>'
        for i, (_, _, note, _) in enumerate(STEPS))
    codes = ''.join(
        f'<div class="layers-code" data-step="{i}"{"" if i == 0 else " hidden"}>'
        f'<div class="layers-code-label">{"הקוד" if i == 0 else "מה הוספנו בשלב הזה"} ({["HTML", "CSS", "JavaScript"][i]})</div>'
        f'{code(src, lang)}</div>'
        for i, (_, lang, _, src) in enumerate(STEPS))
    sources = (f'<textarea hidden class="layers-src" data-part="html">{html.escape(CARD_HTML)}</textarea>'
               f'<textarea hidden class="layers-src" data-part="css">{html.escape(CARD_CSS)}</textarea>'
               f'<textarea hidden class="layers-src" data-part="js">{html.escape(CARD_JS)}</textarea>')
    script = '''<script>
(function () {
    var box = document.getElementById('layers');
    var src = {};
    box.querySelectorAll('.layers-src').forEach(function (t) { src[t.getAttribute('data-part')] = t.value; });
    var frame = box.querySelector('.layers-frame');
    function show(step) {
        var s = 'scr' + 'ipt';
        frame.srcdoc = '<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8">' +
            (step >= 1 ? '<style>' + src.css + '</style>' : '') + '</head><body>' + src.html +
            (step >= 2 ? '<' + s + '>' + src.js + '</' + s + '>' : '') + '</body></html>';
        box.querySelectorAll('[data-step]').forEach(function (e) {
            var on = +e.getAttribute('data-step') === step;
            if (e.tagName === 'BUTTON') { e.classList.toggle('active', on); e.setAttribute('aria-pressed', on); }
            else e.hidden = !on;
        });
    }
    box.querySelector('.layers-tabs').addEventListener('click', function (e) {
        var b = e.target.closest('button');
        if (b) show(+b.getAttribute('data-step'));
    });
    show(0);
})();
</script>'''
    return (f'<div class="layers" id="layers">'
            f'<div class="layers-tabs">{tabs}</div>'
            f'<div class="layers-body"><iframe class="layers-frame" sandbox="allow-scripts" title="התוצאה"></iframe>{notes}</div>'
            f'{codes}{sources}</div>\n{script}')


page('web-intro', 'מה זה HTML, CSS ו-JavaScript?', 'שלוש השפות שכל עמוד אינטרנט בנוי מהן, ומה התפקיד של כל אחת',
     '<strong>💡 על מה העמוד הזה?</strong> כל עמוד שאתם רואים בדפדפן, כולל האתר שתבנו בפרויקט, בנוי משלוש שפות שעובדות יחד. לפני שנכנסים לפרטים בעמודים הבאים, כאן נראה מה כל אחת עושה, איך הן משתלבות, ואיפה כל אחת נמצאת בפרויקט שלכם.',
     [
         ('1. שלוש שפות, שלושה תפקידים', [
             '<p>הדרך הכי פשוטה לזכור: אם עמוד אינטרנט היה גוף, <strong>HTML</strong> הוא השלד, <strong>CSS</strong> הוא הבגדים, ו-<strong>JavaScript</strong> הוא מה שגורם לו לזוז.</p>',
             table(['שפה', 'התפקיד', 'שואלת', 'דוגמה קטנה'], [
                 ['<strong>HTML</strong>', 'התוכן והמבנה: כותרות, פסקאות, תמונות, כפתורים, טפסים.', '<strong>מה</strong> יש בעמוד?', c('<h1>החנות שלנו</h1>')],
                 ['<strong>CSS</strong>', 'העיצוב: צבעים, גדלים, גופנים, רווחים ומיקום.', '<strong>איך</strong> זה נראה?', c('h1 { color: purple; }')],
                 ['<strong>JavaScript</strong>', 'ההתנהגות: מה קורה כשלוחצים, מקלידים או גוללים.', 'מה <strong>קורה</strong> כש...?', c('alert("שלום!");')],
             ]),
             concept('דפדפן (Browser)', 'התוכנה שבה גולשים באינטרנט: Chrome, Edge, Firefox. הדפדפן הוא זה שקורא את שלוש השפות ומצייר מהן את העמוד על המסך.',
                     'דוגמה: כשאתם מריצים את הפרויקט ב-Visual Studio, נפתח דפדפן שמציג את האתר שלכם.'),
             box('warning', '⚠️ JavaScript זה לא Java.', 'למרות השם הדומה, אלה שתי שפות שונות לגמרי. וגם C#, השפה שבה כותבים את ה-Controllers, היא שפה אחרת: היא רצה בשרת, לא בדפדפן (סעיף 4).'),
         ]),
         ('2. אותו כרטיס, שלב אחרי שלב', [
             '<p>הנה כרטיס מוצר קטן. לחצו על השלבים כדי לראות מה כל שפה מוסיפה. שימו לב: בכל שלב <strong>מוסיפים</strong> שכבה, ולא מוחקים את מה שהיה.</p>',
             layers_demo(),
         ]),
         ('3. נסו בעצמכם', [
             '<p>כאן הכרטיס המלא, עם שלוש לשוניות, אחת לכל שפה. שנו משהו בכל לשונית וראו מה משתנה.</p>',
             pg(CARD_HTML, CARD_CSS, CARD_JS, title='נסו: שנו את המחיר ב-HTML, את צבע הכפתור ב-CSS, ואת ההודעה ב-JavaScript', height=330),
             box('checkpoint', '', 'שיניתם את המחיר בלשונית HTML והוא השתנה בתוצאה? שיניתם את ' + c('#68217a') + ' בלשונית CSS (למשל ל-' + c('tomato') + ') והכפתור החליף צבע? מצוין, הבנתם את החלוקה.'),
         ]),
         ('4. מי רץ איפה: שרת ודפדפן', [
             '<p>בפרויקט ASP.NET יש עוד שחקן: <strong>C#</strong>. הוא רץ על השרת (המחשב שמריץ את האתר), ותפקידו להכין את ה-HTML. רק אחרי שהעמוד מוכן הוא נשלח לדפדפן, ושם נכנסים לפעולה CSS ו-JavaScript.</p>',
             concept('שרת (Server)', 'המחשב שמריץ את האתר ושולח עמודים למי שמבקש אותם. כשאתם מפתחים, השרת הוא המחשב שלכם: Visual Studio מריץ אותו, ולכן הכתובת היא ' + c('localhost') + '.',
                     'דוגמה: כשמישהו נכנס לאתר שעלה לאינטרנט, השרת נמצא אי שם בענן, והדפדפן נמצא אצל הגולש.'),
             '''<div class="flow">
        <div class="step"><b>1. C# בשרת</b><span>ה-Controller וה-View בונים עמוד HTML</span></div>
        <div class="arrow">←</div>
        <div class="step browser"><b>2. HTML</b><span>נשלח לדפדפן</span></div>
        <div class="arrow">←</div>
        <div class="step browser"><b>3. CSS</b><span>הדפדפן מעצב את העמוד</span></div>
        <div class="arrow">←</div>
        <div class="step browser"><b>4. JavaScript</b><span>מגיב ללחיצות, בלי לחזור לשרת</span></div>
    </div>''',
             '<p>לכן כשלוחצים על כפתור שמשנה טקסט ב-JavaScript, זה קורה מיד: הכול כבר בדפדפן. אבל כששולחים טופס שנשמר במסד הנתונים, הדפדפן חייב לשלוח בקשה חדשה לשרת, ל-C#.</p>',
             '<p>רוצים לראות מה הדפדפן קיבל בפועל? באתר שלכם, לחצו קליק ימני ← <strong>View page source</strong>. תראו HTML רגיל לגמרי, בלי אף שורת C#: הוא כבר עשה את העבודה שלו בשרת.</p>',
         ]),
         ('5. איפה כל אחת נמצאת בפרויקט', [
             table(['שפה', 'איפה בפרויקט', 'מדריך'], [
                 ['<strong>HTML</strong>', 'בקבצי ' + c('.cshtml') + ' שבתיקייה ' + c('Views') + '. אלה קבצי HTML עם תוספות של C# (הסימן ' + c('@') + '). המסגרת של כל העמודים נמצאת ב-' + c('Views/Shared/_Layout.cshtml') + '.', '<a href="05-cshtml.html">5</a>, <a href="06-layout.html">6</a>'],
                 ['<strong>CSS</strong>', 'ב-' + c('wwwroot/css/site.css') + '. בנוסף, Bootstrap מביא הרבה עיצוב מוכן.', '<a href="08-css-js.html">8</a>, <a href="09-bootstrap.html">9</a>'],
                 ['<strong>JavaScript</strong>', 'ב-' + c('wwwroot/js/site.js') + ', או בתוך View מסוים (ב-' + c('@section Scripts') + ').', '<a href="08-css-js.html">8</a>'],
                 ['<strong>C#</strong>', 'ב-' + c('Controllers') + ', ' + c('Models') + ', ' + c('Program.cs') + ', ובתוך ה-' + c('.cshtml') + ' אחרי ' + c('@') + '.', '<a href="04-how-mvc-works.html">4</a>'],
             ]),
             '<p>הקבצים מתחברים זה לזה ב-' + c('_Layout.cshtml') + ': בראש הקובץ יש שורה שטוענת את ה-CSS, ובסופו שורה שטוענת את ה-JavaScript. כך כל עמוד באתר מקבל את שניהם.</p>',
             code('''<head>
    ...
    <link rel="stylesheet" href="~/css/site.css" asp-append-version="true" />
</head>
<body>
    ...
    <script src="~/js/site.js" asp-append-version="true"></script>
</body>''', 'cshtml'),
         ]),
         ('6. איך יודעים איזו שפה לפניכם?', [
             '<p>כשאתם רואים קוד ולא בטוחים מה הוא, חפשו את הסימנים האלה:</p>',
             table(['אם רואים...', 'זה כנראה'], [
                 ['סוגריים משולשים: ' + c('<p>') + ', ' + c('<div class="card">'), 'HTML'],
                 ['שם, ואחריו סוגריים מסולסלים עם ' + c('תכונה: ערך;') + ', למשל ' + c('.card { color: red; }'), 'CSS'],
                 [c('let') + ', ' + c('function') + ', ' + c('document.') + ', ' + c('addEventListener'), 'JavaScript'],
                 [c('public class') + ', ' + c('IActionResult') + ', ' + c('return View()'), 'C#'],
                 ['HTML שיש בו ' + c('@') + ', למשל ' + c('@Model.Name') + ' או ' + c('@foreach'), 'cshtml (HTML עם C#)'],
             ]),
             '<div class="exercise"><h3>✏️ תרגיל</h3><ol>'
             '<li>בפרויקט שלכם, פתחו את ' + c('Views/Home/Index.cshtml') + '. מצאו שורה אחת של HTML ושורה אחת של C# (עם ' + c('@') + ').</li>'
             '<li>פתחו את ' + c('wwwroot/css/site.css') + ' ומצאו כלל CSS אחד. מה הוא משנה, ולמי?</li>'
             '<li>בעמוד "נסו בעצמכם" למעלה, הוסיפו ב-HTML שורה ' + c('<p>משלוח חינם</p>') + ', וב-CSS תנו לה צבע משלה.</li>'
             '</ol></div>',
         ]),
     ],
     ['<strong>HTML</strong> קובע מה יש בעמוד, <strong>CSS</strong> קובע איך זה נראה, ו-<strong>JavaScript</strong> קובע מה קורה כשהמשתמש עושה משהו.',
      'כל שפה מוסיפה שכבה, בלי לשנות את האחרות.',
      'C# רץ בשרת ובונה את ה-HTML. CSS ו-JavaScript רצים בדפדפן.',
      'בפרויקט: HTML ב-' + c('Views') + ', CSS ב-' + c('wwwroot/css') + ', JavaScript ב-' + c('wwwroot/js') + '.'],
     'ממשיכים ל-<a href="web-html.html">יסודות HTML</a>, ואחריו <a href="web-css.html">יסודות CSS</a> ו-<a href="web-js.html">יסודות JavaScript</a>.')
