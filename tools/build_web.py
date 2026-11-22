"""Builds the web basics pages (guides/web-intro.html, web-html.html, web-css.html, web-js.html and the part 2 pages).

Edit the content below and run:  python tools/build_web.py
Code inside pg(...) is escaped automatically and becomes a live "try it yourself" editor.
"""
import html
import os

OUT = os.path.join(os.path.dirname(__file__), '..', 'guides')


def pg(html_src='', css='', js='', title='נסו בעצמכם', height=220, bootstrap=False):
    parts = [f'<div class="playground" data-title="{html.escape(title)}" data-height="{height}"{" data-bootstrap" if bootstrap else ""}>']
    for lang, src in (('html', html_src), ('css', css), ('js', js)):
        if src.strip():
            parts.append(f'<textarea data-lang="{lang}">{html.escape(src.strip(chr(10)))}</textarea>')
    parts.append('</div>')
    return '\n'.join(parts)


def concept(title, text, example=None):
    ex = f'<span class="example">{example}</span>' if example else ''
    return f'<div class="concept"><span class="concept-title">📖 {title}</span>{text}{ex}</div>'


def table(head, rows):
    h = ''.join(f'<th>{c}</th>' for c in head)
    r = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in rows)
    return f'<table class="simple"><tr>{h}</tr>{r}</table>'


def c(x):
    return f'<code class="inline">{html.escape(x)}</code>'


def page(slug, title, subtitle, intro, sections, summary, more):
    body = []
    for h2, items in sections:
        body.append(f'    <h2>{h2}</h2>')
        body.extend(items)
    s = '\n'.join(f'<li>{x}</li>' for x in summary)
    out = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="../assets/theme-init.js"></script>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body data-guide="{slug}">
<main>
    <h1>{title}</h1>
    <div class="subtitle">{subtitle}</div>

    <div class="explanation">{intro}
        <br><br>
        <strong>✏️ איך עובדים עם העמוד:</strong> בכל עורך קוד אפשר <strong>לשנות את הקוד</strong>, והתוצאה מתעדכנת מיד בחלון הדפדפן שלידו. אם יש כמה קבצים (index.html, style.css, script.js), לחצו על השם שלהם כדי לעבור ביניהם. ↺ איפוס מחזיר את הדוגמה למצב ההתחלתי, ושני הכפתורים הקטנים לידו מסדרים את העורך והתוצאה זה ליד זה או אחד מעל השני. אי אפשר לשבור כלום, אז תתפרעו!
    </div>

{chr(10).join(body)}

    <div class="summary">
        <h3>📌 מה למדנו</h3>
        <ul>{s}</ul>
    </div>
    <p style="margin-top:1.5rem">🔎 <strong>רוצים עוד?</strong> {more}</p>
</main>
<script src="../assets/site.js"></script>
</body>
</html>
'''
    open(os.path.join(OUT, slug + '.html'), 'w', encoding='utf-8').write(out)


# =====================================================================
# HTML
# =====================================================================
page('web-html', 'יסודות HTML', 'התגיות שנשתמש בהן בפרויקט, עם דוגמה חיה לכל אחת',
     '<strong>💡 על מה העמוד הזה?</strong> HTML הוא השלד של כל עמוד: מה יש בו (כותרת, פסקה, תמונה, טופס). כל קובץ cshtml בפרויקט הוא בעצם HTML, עם תוספות של C# (מדריך 5). כאן נעבור על התגיות שבאמת צריך. חדשים בזה? התחילו ב-<a href="web-intro.html">מה זה HTML, CSS ו-JavaScript?</a>',
     [
         ('1. איך נראית תגית', [
             concept('תגית (Tag)', f'מילה בתוך סוגריים משולשים שאומרת לדפדפן "מה זה". לרוב יש תגית פותחת ותגית סוגרת (עם {c("/")}), והתוכן ביניהן.',
                     f'דוגמה: {c("<p>שלום</p>")} היא פסקה עם המילה "שלום". חלק מהתגיות לא סוגרים, כמו {c("<br>")} (ירידת שורה) ו-{c("<img>")} (תמונה).'),
             concept('תכונה (Attribute)', f'מידע נוסף שכותבים בתוך התגית הפותחת: {c("שם=\"ערך\"")}.',
                     f'דוגמה: {c("<a href=\"https://google.com\">גוגל</a>")}. ה-{c("href")} אומר לאן הקישור מוביל.'),
             '<div class="explanation"><strong>💡 ומה עם &lt;html&gt;, &lt;head&gt; ו-&lt;body&gt;?</strong> בכל עמוד HTML יש את שלושתם. בפרויקט שלנו הם כתובים פעם אחת ב-' + c('_Layout.cshtml') + ' (מדריך 6), ולכן בקבצי ה-View כותבים רק את מה שבתוך ה-body.</div>',
         ]),
         ('2. כותרות וטקסט', [
             table(['תגית', 'מה היא'], [
                 [c('<h1>') + ' עד ' + c('<h6>'), 'כותרות. h1 הכי גדולה וחשובה (אחת בעמוד), h6 הכי קטנה.'],
                 [c('<p>'), 'פסקה.'],
                 [c('<strong>'), 'טקסט מודגש (חשוב).'],
                 [c('<em>'), 'טקסט נטוי (הדגשה).'],
                 [c('<br>'), 'ירידת שורה, בלי לסגור.'],
                 [c('<hr>'), 'קו מפריד.'],
             ]),
             pg('''
<h1>כותרת ראשית</h1>
<h2>כותרת משנה</h2>
<p>זו פסקה רגילה. אפשר להדגיש <strong>מילה חשובה</strong> או <em>מילה אחרת</em>.</p>
<p>שורה ראשונה<br>שורה שנייה, באותה פסקה</p>
<hr>
<h3>כותרת קטנה יותר</h3>''', title='נסו: שנו את הטקסטים, או הוסיפו h4', height=260),
         ]),
         ('3. קישורים ותמונות', [
             table(['תגית', 'תכונות חשובות'], [
                 [c('<a>') + ' (קישור)', c('href') + ': לאן. ' + c('target="_blank"') + ': פותח בלשונית חדשה.'],
                 [c('<img>') + ' (תמונה)', c('src') + ': כתובת התמונה. ' + c('alt') + ': תיאור (חשוב לנגישות). ' + c('width') + ': רוחב.'],
             ]),
             pg('''
<p>
    <a href="https://www.google.com" target="_blank">קישור לגוגל</a>
</p>

<img src="https://placehold.co/300x150?text=My+Image" alt="תמונה לדוגמה" width="300">

<p>
    <a href="https://www.google.com" target="_blank">
        <img src="https://placehold.co/120x60?text=Click" alt="תמונה שהיא קישור">
    </a>
</p>''', title='נסו: שנו את הגודל בכתובת התמונה (300x150)', height=300),
             '<div class="explanation"><strong>💡 בפרויקט:</strong> לקישורים בין עמודים באתר משתמשים ב-' + c('asp-controller') + ' וב-' + c('asp-action') + ' במקום ' + c('href') + ' (מדריך 6). לתמונות מתיקיית wwwroot כותבים ' + c('src="~/images/..."') + ' (מדריך 8).</div>',
         ]),
         ('4. רשימות', [
             table(['תגית', 'מה היא'], [
                 [c('<ul>'), 'רשימה עם נקודות (לא ממוספרת).'],
                 [c('<ol>'), 'רשימה ממוספרת.'],
                 [c('<li>'), 'פריט אחד ברשימה. תמיד בתוך ul או ol.'],
             ]),
             pg('''
<h3>קניות</h3>
<ul>
    <li>חלב</li>
    <li>לחם</li>
    <li>ביצים</li>
</ul>

<h3>שלבים</h3>
<ol>
    <li>פותחים את Visual Studio</li>
    <li>יוצרים פרויקט</li>
    <li>לוחצים Play</li>
</ol>''', title='נסו: הוסיפו פריט לכל רשימה', height=300),
         ]),
         ('5. div, span, class ו-id', [
             concept('div ו-span', f'{c("<div>")} היא "קופסה" שעוטפת חלק מהעמוד, ומתחילה בשורה חדשה. {c("<span>")} עוטפת חלק קטן בתוך שורה. לבד הן לא עושות כלום: משתמשים בהן כדי לעצב (CSS) או לבחור חלק בעמוד (JavaScript).'),
             concept('class ו-id', f'{c("class")} נותן לתגית "שם קבוצה". הרבה תגיות יכולות לקבל את אותו class. {c("id")} נותן לתגית שם <strong>ייחודי</strong>: רק תגית אחת בעמוד.',
                     f'Bootstrap עובד כולו עם class: {c("<button class=\"btn btn-primary\">")} (מדריך 9).'),
             pg('''
<div class="box">
    אני div עם class בשם box.
    ובתוכי יש <span class="highlight">span מודגש</span> באמצע שורה.
</div>

<div class="box" id="special">
    גם אני box, אבל יש לי גם id ייחודי.
</div>''', css='''
.box {
    border: 2px solid steelblue;
    padding: 10px;
    margin-bottom: 10px;
}

.highlight {
    background-color: yellow;
}

#special {
    background-color: lavender;
}''', title='נסו: לחצו על הלשונית CSS ושנו צבעים', height=220),
         ]),
         ('6. טבלאות', [
             table(['תגית', 'מה היא'], [
                 [c('<table>'), 'הטבלה כולה.'],
                 [c('<thead>') + ' / ' + c('<tbody>'), 'חלק הכותרות / חלק הנתונים.'],
                 [c('<tr>'), 'שורה (table row).'],
                 [c('<th>'), 'תא כותרת (מודגש).'],
                 [c('<td>'), 'תא רגיל (table data).'],
             ]),
             '<h3>תכונות של תאים: איחוד תאים</h3>',
             table(['תכונה', 'מה היא עושה', 'דוגמה'], [
                 [c('colspan'), 'התא תופס כמה <strong>עמודות</strong>.', c('<td colspan="2">')],
                 [c('rowspan'), 'התא תופס כמה <strong>שורות</strong>.', c('<td rowspan="2">')],
             ]),
             '<h3>עיצוב הטבלה: עם CSS</h3>',
             '<p>בדוגמאות ישנות באינטרנט תראו תכונות כמו ' + c('border="1"') + ' ו-' + c('cellpadding="6"') + ' ישירות על ' + c('<table>') + '. הן עדיין עובדות, אבל הן <strong>מיושנות</strong>: היום מעצבים טבלה עם CSS, שנותן הרבה יותר שליטה. הנה מה מחליף כל אחת:</p>',
             table(['תכונה ישנה (לא מומלץ)', 'מה עושים במקום (CSS)'], [
                 [c('border="1"'), c('border: 1px solid #ccc;') + ' על ' + c('th, td') + ', ו-' + c('border-collapse: collapse;') + ' על ' + c('table') + ' (כדי שלא יהיו קווים כפולים).'],
                 [c('cellpadding="6"'), c('padding: 6px;') + ' על ' + c('th, td') + '.'],
                 [c('cellspacing="0"'), c('border-collapse: collapse;') + ' על ' + c('table') + '.'],
                 [c('width="100%"'), c('width: 100%;')],
                 [c('bgcolor="yellow"'), c('background-color: yellow;')],
                 [c('align="center"'), c('text-align: center;') + ' (לתוכן התאים).'],
             ]),
             pg('''
<table class="products">
    <thead>
        <tr>
            <th>שם</th>
            <th>מחיר</th>
            <th>מלאי</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>עט</td>
            <td>5 ₪</td>
            <td>120</td>
        </tr>
        <tr>
            <td>מחברת</td>
            <td>12 ₪</td>
            <td>45</td>
        </tr>
        <tr>
            <td>תיק</td>
            <td>150 ₪</td>
            <td>8</td>
        </tr>
        <tr>
            <td colspan="2"><strong>סה"כ פריטים במלאי</strong></td>
            <td><strong>173</strong></td>
        </tr>
    </tbody>
</table>''', css='''
.products {
    border-collapse: collapse;
    width: 100%;
}

.products th,
.products td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}

.products th {
    background-color: #4c1d95;
    color: white;
}

/* כל שורה זוגית בצבע אחר ("זברה") */
.products tbody tr:nth-child(even) {
    background-color: #f3f0ff;
}

/* שורה שהעכבר עליה */
.products tbody tr:hover {
    background-color: #fff3cd;
}''', title='נסו: בלשונית CSS שנו צבעים, או מחקו את border-collapse ותראו מה קורה', height=280),
             table(['תכונת CSS', 'מה היא עושה'], [
                 [c('border-collapse: collapse'), 'מאחדת את הקווים של תאים צמודים לקו אחד.'],
                 [c('tr:nth-child(even)'), 'בוחרת כל שורה זוגית (' + c('odd') + ' = אי-זוגית). ככה עושים "זברה".'],
                 [c('tr:hover'), 'השורה שהעכבר עליה.'],
                 [c('vertical-align: top'), 'יישור התוכן בתא לגובה (למעלה / ' + c('middle') + ' / ' + c('bottom') + ').'],
             ]),
             '<div class="explanation"><strong>💡 בפרויקט:</strong> את השורות לא כותבים ביד, אלא בונים בלולאה ' + c('@foreach') + ' מתוך נתונים (מדריך 10). ואפשר לוותר על רוב ה-CSS: ' + c('class="table table-striped table-hover"') + ' של Bootstrap עושה את כל זה בשבילכם (מדריך 9).</div>',
         ]),
         ('7. טפסים', [
             '<p>טפסים הם החלק הכי חשוב ב-HTML בשביל הפרויקט: הרשמה, הוספת מוצר, צור קשר. כל שדה הוא ' + c('<input>') + ' עם ' + c('type') + ' אחר.</p>',
             table(['תגית / type', 'מה היא'], [
                 [c('<form>'), 'עוטפת את כל השדות. כשלוחצים על כפתור submit, כל מה שבתוכה נשלח.'],
                 [c('<label for="...">'), 'תווית של שדה. ה-' + c('for') + ' מחבר אותה ל-' + c('id') + ' של השדה (לחיצה על התווית מפעילה את השדה).'],
                 [c('type="text"'), 'שורת טקסט.'],
                 [c('type="email"') + ', ' + c('type="password"') + ', ' + c('type="number"') + ', ' + c('type="date"'), 'אימייל, סיסמה (מוסתרת), מספר, תאריך.'],
                 [c('type="checkbox"') + ' / ' + c('type="radio"'), 'תיבת סימון / בחירה אחת מכמה (לכל ה-radio באותה קבוצה אותו ' + c('name') + ').'],
                 [c('<select>') + ' + ' + c('<option>'), 'רשימה נפתחת.'],
                 [c('<textarea>'), 'טקסט ארוך.'],
                 [c('<button type="submit">'), 'כפתור ששולח את הטופס.'],
             ]),
             pg('''
<form>
    <label for="name">שם:</label><br>
    <input type="text" id="name" placeholder="השם שלכם"><br><br>

    <label for="email">אימייל:</label><br>
    <input type="email" id="email"><br><br>

    <label for="age">גיל:</label>
    <input type="number" id="age" min="1" max="120"><br><br>

    <label for="date">תאריך:</label>
    <input type="date" id="date"><br><br>

    <label for="grade">כיתה:</label>
    <select id="grade">
        <option>י'</option>
        <option>י"א</option>
        <option>י"ב</option>
    </select><br><br>

    <input type="checkbox" id="agree">
    <label for="agree">אני מסכים לתנאים</label><br><br>

    <label for="msg">הודעה:</label><br>
    <textarea id="msg" rows="3"></textarea><br><br>

    <button type="submit">שליחה</button>
</form>''', title='נסו: הוסיפו שדה "טלפון" (type="tel")', height=460),
             '<h3>שדות חובה</h3>',
             '<p>בטופס שלמעלה אפשר ללחוץ "שליחה" גם כשהכול ריק. כדי לחייב את המשתמש למלא שדה, מוסיפים לו את המילה ' + c('required') + '. אין לה ערך: עצם זה שהיא כתובה בתגית אומר "חובה".</p>',
             concept('שדה חובה (required)', 'שדה שאי אפשר לשלוח את הטופס בלי למלא. כשלוחצים "שליחה" והוא ריק, הדפדפן עוצר את השליחה, קופץ לשדה ומציג הודעה קטנה לידו.',
                     'דוגמה: ' + c('<input type="text" id="name" required>') + '. נהוג לסמן שדות חובה בכוכבית אדומה ליד התווית, כדי שהמשתמש יידע מראש.'),
             table(['תכונה', 'מה היא בודקת', 'דוגמה'], [
                 [c('required'), 'שהשדה לא ריק. ב-checkbox: שסימנו אותו.', c('<input type="text" required>')],
                 [c('type="email"'), 'שמה שנכתב נראה כמו אימייל (יש @). בודק רק אם השדה לא ריק, אז משלבים עם ' + c('required') + '.', c('<input type="email" required>')],
                 [c('minlength') + ' / ' + c('maxlength'), 'מספר תווים מינימלי / מקסימלי.', c('<input type="password" minlength="6">')],
                 [c('min') + ' / ' + c('max'), 'הערך הכי קטן / הכי גדול (במספרים ובתאריכים).', c('<input type="number" min="1" max="120">')],
             ]),
             pg('''
<form>
    <p>שדות עם <span class="req">*</span> הם חובה</p>

    <label for="name2">שם: <span class="req">*</span></label><br>
    <input type="text" id="name2" required><br><br>

    <label for="email2">אימייל: <span class="req">*</span></label><br>
    <input type="email" id="email2" required><br><br>

    <label for="pass2">סיסמה (לפחות 6 תווים): <span class="req">*</span></label><br>
    <input type="password" id="pass2" required minlength="6"><br><br>

    <label for="phone2">טלפון (לא חובה):</label><br>
    <input type="tel" id="phone2"><br><br>

    <input type="checkbox" id="agree2" required>
    <label for="agree2">אני מסכים לתנאים <span class="req">*</span></label><br><br>

    <button type="submit">שליחה</button>
</form>''', css='''
.req {
    color: #c72e2e;
    font-weight: bold;
}

/* מסגרת אדומה לשדה חובה שהמשתמש נגע בו ולא מילא נכון */
input:user-invalid {
    border: 2px solid #c72e2e;
}''', title='נסו: לחצו "שליחה" בלי למלא כלום. אחר כך מלאו הכול ושלחו שוב. ואז מחקו את required מהשם ובדקו מה השתנה', height=420),
             '<div class="checkpoint">' + 'לחצתם "שליחה" כשהשם ריק, והדפדפן עצר וקפץ לשדה עם הודעה? וכשמילאתם הכול הופיעה הודעה ירוקה שהטופס נשלח? מצוין.</div>',
             '<div class="warning"><strong>⚠️ הבדיקה של הדפדפן היא רק עזרה למשתמש.</strong> ' + 'מי שמבין קצת יכול לעקוף אותה (למשל למחוק את ' + c('required') + ' בכלי המפתחים, F12). לכן בפרויקט בודקים שוב בשרת, עם ' + c('[Required]') + ' במודל: <a href="12-validation.html">מדריך 12</a>. החדשות הטובות: כשכותבים ' + c('[Required]') + ' במודל, ASP.NET מוסיף לשדה את הבדיקה בדפדפן לבד.' + '</div>',
             '<div class="explanation"><strong>💡 בפרויקט:</strong> במקום ' + c('id') + ' ו-' + c('name') + ' כותבים ' + c('asp-for="Name"') + ', ו-ASP.NET ממלא אותם לבד ומחבר את השדה למודל (מדריך 11). אבל בסוף, בדפדפן, זה בדיוק אותו HTML.</div>',
         ]),
         ('8. תגיות שמתארות את מבנה העמוד', [
             '<p>תגיות שמתנהגות כמו ' + c('<div>') + ', אבל השם שלהן אומר מה התפקיד של החלק. הן עוזרות לקרוא את הקוד, ולמנועי חיפוש ולקוראי מסך להבין את העמוד. כבר תמצאו אותן ב-' + c('_Layout.cshtml') + ':</p>',
             table(['תגית', 'התפקיד'], [
                 [c('<header>'), 'החלק העליון (לוגו, תפריט).'],
                 [c('<nav>'), 'תפריט ניווט.'],
                 [c('<main>'), 'התוכן הראשי של העמוד.'],
                 [c('<section>'), 'חלק בעמוד, עם נושא משלו.'],
                 [c('<footer>'), 'החלק התחתון.'],
             ]),
         ]),
     ],
     ['תגית פותחת וסוגרת, ותכונות כמו ' + c('href') + ' ו-' + c('src') + '.',
      'טקסט: h1-h6, p, strong. קישורים ותמונות: a, img. רשימות: ul/ol/li. טבלאות: table/tr/th/td.',
      'div ו-span עוטפים חלקים, ו-class/id נותנים להם שם לעיצוב ול-JavaScript.',
      'טפסים: form, label, input עם type, select, textarea, button. בפרויקט asp-for בונה אותם בשבילנו.',
      'שדה חובה: מוסיפים ' + c('required') + '. הדפדפן לא ישלח את הטופס עד שימלאו אותו, ובשרת בודקים שוב עם ' + c('[Required]') + '.'],
     'רשימה מלאה של כל התגיות, עם דוגמאות: <a href="https://www.w3schools.com/html/" target="_blank">w3schools HTML</a> או <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element" target="_blank">MDN</a> (באנגלית).')

# =====================================================================
# CSS
# =====================================================================
box_model_demo = '''
<div class="bm-demo" dir="rtl">
    <div class="bm-controls">
        <label>margin (רווח מבחוץ): <input type="range" min="0" max="40" value="20" data-prop="margin"> <span>20</span>px</label>
        <label>border (מסגרת): <input type="range" min="0" max="20" value="4" data-prop="borderWidth"> <span>4</span>px</label>
        <label>padding (רווח מבפנים): <input type="range" min="0" max="40" value="15" data-prop="padding"> <span>15</span>px</label>
    </div>
    <div class="bm-stage"><div class="bm-box">התוכן</div></div>
    <p class="bm-code" dir="ltr"></p>
</div>
<style>
.bm-demo { border: 2px solid #0ea5e9; border-radius: 10px; padding: 1rem; margin: 1rem 0 1.5rem; background: white; }
.bm-controls { display: grid; gap: 0.4rem; margin-bottom: 0.8rem; }
.bm-controls input { vertical-align: middle; width: 160px; }
.bm-stage { background: repeating-linear-gradient(45deg, #fde68a, #fde68a 6px, #fef3c7 6px, #fef3c7 12px); display: inline-block; }
.bm-box { background-color: #bfdbfe; border-style: solid; border-color: #1d4ed8; display: inline-block; }
.bm-code { font-family: Consolas, monospace; text-align: left; margin: 0.6rem 0 0; color: #334155; }
</style>
<script>
(function () {
    var demo = document.currentScript.previousElementSibling.previousElementSibling;
    var box = demo.querySelector('.bm-box');
    function update() {
        var v = {};
        demo.querySelectorAll('input').forEach(function (i) {
            v[i.dataset.prop] = i.value;
            i.nextElementSibling.textContent = i.value;
        });
        box.style.margin = v.margin + 'px';
        box.style.borderWidth = v.borderWidth + 'px';
        box.style.padding = v.padding + 'px';
        demo.querySelector('.bm-code').textContent =
            '.box { margin: ' + v.margin + 'px; border: ' + v.borderWidth + 'px solid blue; padding: ' + v.padding + 'px; }';
    }
    demo.querySelectorAll('input').forEach(function (i) { i.addEventListener('input', update); });
    update();
})();
</script>
<table class="simple"><tr><th>צבע בהמחשה</th><th>החלק</th></tr>
<tr><td>🟨 פסים צהובים</td><td><strong>margin</strong>: רווח מחוץ למסגרת, בין הקופסה לשכנים שלה. שקוף.</td></tr>
<tr><td>🟦 קו כחול כהה</td><td><strong>border</strong>: המסגרת.</td></tr>
<tr><td>🟦 תכלת</td><td><strong>padding</strong> והתוכן: הרווח בין המסגרת לתוכן מקבל את צבע הרקע של הקופסה.</td></tr>
</table>'''

page('web-css', 'יסודות CSS', 'איך מעצבים: צבעים, רווחים, סידור בשורה, ועמוד שמתאים לטלפון',
     '<strong>💡 על מה העמוד הזה?</strong> אם HTML הוא השלד, CSS הוא הבגדים: צבעים, גדלים, רווחים ומיקום. Bootstrap (מדריך 9) נותן הרבה עיצוב מוכן, אבל כדי לשנות אותו ולהתאים לאתר שלכם צריך להכיר את הבסיס. איפה שמים את ה-CSS בפרויקט: מדריך 8. חדשים בזה? התחילו ב-<a href="web-intro.html">מה זה HTML, CSS ו-JavaScript?</a>',
     [
         ('1. איך כותבים כלל CSS', [
             concept('כלל CSS', f'"למי" (סלקטור), ואז בסוגריים מסולסלים "מה לשנות" (תכונה: ערך;).',
                     f'דוגמה: {c("h1 { color: red; }")} פירושו "כל ה-h1 בעמוד, בצבע אדום". אל תשכחו את הנקודה-פסיק בסוף כל שורה!'),
             pg('''
<h1>כותרת</h1>
<p>פסקה ראשונה.</p>
<p>פסקה שנייה.</p>''', css='''
h1 {
    color: darkblue;
    font-size: 40px;
}

p {
    color: gray;
}''', title='נסו: בלשונית CSS שנו את darkblue ל-crimson', height=200),
         ]),
         ('2. סלקטורים: למי הכלל שייך', [
             table(['סלקטור', 'דוגמה', 'למי'], [
                 ['שם תגית', c('p'), 'כל ה-p בעמוד.'],
                 ['class (עם נקודה)', c('.price'), 'כל מה שיש לו ' + c('class="price"') + '. <strong>הכי נפוץ.</strong>'],
                 ['id (עם סולמית)', c('#main-title'), 'התגית היחידה עם ' + c('id="main-title"') + '.'],
                 ['בתוך', c('.card p'), 'כל p שנמצא בתוך משהו עם class="card".'],
                 [':hover', c('a:hover'), 'קישור, כשהעכבר עליו.'],
             ]),
             pg('''
<h2 id="main-title">המוצרים שלנו</h2>
<div class="card">
    <p>עט כחול</p>
    <p class="price">5 ₪</p>
</div>
<div class="card">
    <p>מחברת</p>
    <p class="price">12 ₪</p>
</div>
<p>פסקה מחוץ לכרטיס</p>''', css='''
#main-title {
    color: purple;
}

.card {
    border: 1px solid #ccc;
    padding: 8px;
    margin-bottom: 8px;
}

.card p {
    margin: 4px 0;
}

.price {
    color: green;
    font-weight: bold;
}''', title='נסו: שנו את הצבע של .price, ושימו לב מה משתנה', height=300),
         ]),
         ('3. צבעים, טקסט ורקע', [
             table(['תכונה', 'מה היא', 'דוגמה'], [
                 [c('color'), 'צבע הטקסט', c('color: tomato;')],
                 [c('background-color'), 'צבע הרקע', c('background-color: #f0f8ff;')],
                 [c('font-size'), 'גודל הטקסט', c('font-size: 20px;')],
                 [c('font-weight'), 'עובי', c('font-weight: bold;')],
                 [c('text-align'), 'יישור', c('text-align: center;')],
                 [c('font-family'), 'גופן', c('font-family: Arial;')],
             ]),
             concept('איך כותבים צבע', f'בשם ({c("red")}, {c("steelblue")}), בקוד hex ({c("#ff6347")}), או ב-rgb ({c("rgb(255, 99, 71)")}). כולם עובדים.',
                     'טיפ: בגוגל חפשו "color picker", בחרו צבע והעתיקו את קוד ה-hex שלו.'),
             pg('''
<div class="banner">
    <h2>מבצע!</h2>
    <p>כל המחברות ב-10 ₪</p>
</div>''', css='''
.banner {
    background-color: #fff3cd;
    color: #8a5a00;
    text-align: center;
    font-family: Arial, sans-serif;
}

.banner h2 {
    font-size: 32px;
    font-weight: bold;
    color: #d9480f;
}''', title='נסו: שנו את צבע הרקע לקוד hex משלכם', height=200),
         ]),
         ('4. Box Model: רווחים ומסגרת', [
             concept('Box Model', f'כל אלמנט בעמוד הוא קופסה, עם שלוש "שכבות" סביב התוכן: {c("padding")} (רווח פנימי), {c("border")} (מסגרת), ו-{c("margin")} (רווח חיצוני).',
                     'הזיזו את הסליידרים וראו מה כל אחד עושה:'),
             box_model_demo,
             pg('''
<div class="box">קופסה 1</div>
<div class="box">קופסה 2</div>''', css='''
.box {
    background-color: lightblue;
    padding: 20px;
    border: 3px solid navy;
    margin: 15px;
    border-radius: 10px;
}''', title='נסו: margin: 0 ו-padding: 40px. מה ההבדל?', height=230),
             '<div class="explanation"><strong>💡 קיצורים:</strong> ' + c('margin: 10px;') + ' = מכל הצדדים. ' + c('margin: 10px 20px;') + ' = למעלה ולמטה 10, לצדדים 20. ' + c('margin-top: 10px;') + ' = רק למעלה. אותו דבר ב-padding.</div>',
         ]),
         ('5. גדלים ויחידות', [
             table(['יחידה', 'פירוש', 'מתי'], [
                 [c('px'), 'פיקסלים: גודל קבוע.', 'מסגרות, רווחים קטנים.'],
                 [c('%'), 'אחוז מהאלמנט שעוטף.', 'רוחב: ' + c('width: 50%;')],
                 [c('rem'), 'ביחס לגודל הטקסט הבסיסי (1rem ≈ 16px).', 'גודלי טקסט.'],
                 [c('vh') + ' / ' + c('vw'), 'אחוז מגובה / רוחב החלון.', 'אזור שתופס מסך שלם: ' + c('height: 100vh;')],
             ]),
             pg('''
<div class="half">אני ברוחב 50%</div>
<div class="limited">אני ברוחב 100%, אבל לא יותר מ-300px</div>''', css='''
.half {
    width: 50%;
    background-color: khaki;
    padding: 10px;
    margin-bottom: 10px;
}

.limited {
    width: 100%;
    max-width: 300px;
    background-color: lightgreen;
    padding: 10px;
}''', title='נסו: שנו 50% ל-80%', height=170),
         ]),
         ('6. Flexbox: לסדר דברים בשורה', [
             concept('Flexbox', f'הדרך הכי קלה לסדר כמה דברים אחד ליד השני, ולשלוט ברווחים וביישור. שמים {c("display: flex;")} על ה<strong>עוטף</strong>, והילדים שלו מסתדרים בשורה.'),
             table(['תכונה (על העוטף)', 'ערכים נפוצים', 'מה היא עושה'], [
                 [c('justify-content'), c('flex-start') + ', ' + c('center') + ', ' + c('space-between') + ', ' + c('space-around'), 'פיזור לאורך השורה.'],
                 [c('align-items'), c('flex-start') + ', ' + c('center') + ', ' + c('flex-end'), 'יישור לגובה.'],
                 [c('gap'), c('10px'), 'רווח בין הילדים.'],
                 [c('flex-wrap'), c('wrap'), 'אם אין מקום, לרדת לשורה הבאה.'],
             ]),
             pg('''
<div class="row">
    <div class="item">1</div>
    <div class="item tall">2</div>
    <div class="item">3</div>
</div>''', css='''
.row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    background-color: #eee;
    padding: 10px;
    height: 150px;
}

.item {
    background-color: coral;
    color: white;
    padding: 20px;
    font-size: 24px;
}

.tall {
    padding: 40px 20px;
}''', title='נסו: justify-content: center, ואחר כך align-items: flex-start', height=200),
             '<div class="explanation"><strong>💡 ב-Bootstrap:</strong> אותו דבר בקלאסים: ' + c('class="d-flex justify-content-between align-items-center gap-2"') + '.</div>',
         ]),
         ('7. hover, פינות מעוגלות וצל', [
             pg('''
<button class="fancy">עברו עליי עם העכבר</button>''', css='''
.fancy {
    background-color: royalblue;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 18px;
    border-radius: 25px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    transition: all 0.3s;
}

.fancy:hover {
    background-color: darkorange;
    transform: scale(1.1);
}''', title='נסו: שנו את 0.3s ל-2s', height=140),
             table(['תכונה', 'מה היא עושה'], [
                 [c(':hover'), 'הכלל חל רק כשהעכבר מעל האלמנט.'],
                 [c('border-radius'), 'פינות מעוגלות. ' + c('50%') + ' על ריבוע = עיגול.'],
                 [c('box-shadow'), 'צל: הזזה לצד, הזזה למטה, טשטוש, צבע.'],
                 [c('transition'), 'השינוי קורה בהדרגה, ולא בבת אחת.'],
                 [c('cursor: pointer'), 'העכבר הופך ליד, כמו על קישור.'],
             ]),
         ]),
         ('8. עמוד שמתאים לטלפון', [
             concept('Media Query', f'כלל CSS שחל רק כשהמסך בגודל מסוים. {c("@media (max-width: 600px) { ... }")} פירושו "רק כשהמסך צר מ-600 פיקסלים".'),
             pg('''
<div class="cards">
    <div class="card">כרטיס 1</div>
    <div class="card">כרטיס 2</div>
    <div class="card">כרטיס 3</div>
</div>
<p class="hint">במסך רחב: שלושה בשורה. במסך צר: אחד מתחת לשני.</p>''', css='''
.cards {
    display: flex;
    gap: 10px;
}

.card {
    flex: 1;
    background-color: plum;
    padding: 20px;
    text-align: center;
}

@media (max-width: 400px) {
    .cards {
        flex-direction: column;
    }
}''', title='נסו: שנו 400px ל-1000px, ותראו את התצוגה של "טלפון"', height=200),
             '<div class="explanation"><strong>💡 ב-Bootstrap:</strong> זה בדיוק מה ש-' + c('col-12 col-md-4') + ' עושה בשבילכם (מדריך 9, סעיף 5).</div>',
         ]),
         ('9. CSS משלכם יחד עם Bootstrap', [
             '<p>הדרך הנכונה לשנות עיצוב של Bootstrap: <strong>לא</strong> לגעת בקבצים של Bootstrap, אלא להוסיף class משלכם ב-' + c('site.css') + '. הוא נטען אחרי Bootstrap, ולכן הכלל שלכם "מנצח".</p>',
             pg('''
<button class="btn btn-primary">כפתור רגיל של Bootstrap</button>
<button class="btn btn-primary btn-pink">אותו כפתור, עם class משלי</button>''', css='''
.btn-pink {
    background-color: hotpink;
    border-color: hotpink;
    border-radius: 0;
}''', title='נסו: שנו את הצבע של .btn-pink', height=120, bootstrap=True),
             '<div class="warning"><strong>⚠️ אם הכלל שלכם לא עובד:</strong> F12 ← Elements, בחרו את האלמנט, ובצד תראו את כל הכללים שחלים עליו. כלל שמחוק בקו הוא כלל ש"הפסיד" לכלל אחר. נסו סלקטור ספציפי יותר (למשל ' + c('.card .btn-pink') + ').</div>',
         ]),
     ],
     ['כלל CSS: סלקטור { תכונה: ערך; }. הסלקטור הנפוץ ביותר הוא class (' + c('.name') + ').',
      'צבעים וטקסט: color, background-color, font-size, text-align.',
      'Box Model: padding בפנים, border מסגרת, margin בחוץ.',
      'Flexbox מסדר בשורה, ו-@media מתאים לטלפון.',
      'משנים את Bootstrap עם class משלכם ב-site.css, ולא בקבצים שלו.'],
     'ההמשך באתר: <a href="web-css2.html">CSS חלק ב\'</a> (מיקום, משתני צבע, Grid ואנימציות) ו-<a href="web-design.html">עיצוב שנראה מקצועי</a>. כל התכונות, עם דוגמאות: <a href="https://www.w3schools.com/css/" target="_blank">w3schools CSS</a>. משחק שמלמד Flexbox: <a href="https://flexboxfroggy.com/#he" target="_blank">Flexbox Froggy</a> (יש גם בעברית).')

# =====================================================================
# JavaScript
# =====================================================================
page('web-js', 'יסודות JavaScript', 'איך גורמים לעמוד להגיב: לחיצות, הקלדה, הצגה והסתרה',
     '<strong>💡 על מה העמוד הזה?</strong> HTML הוא השלד, CSS הבגדים, ו-JavaScript הוא מה שגורם לעמוד <strong>לזוז</strong>: כפתור שעושה משהו, הודעה שמופיעה, טופס שבודק את עצמו. JavaScript רץ בדפדפן, אחרי שהעמוד כבר הגיע מהשרת. איפה שמים אותו בפרויקט: מדריך 8, סעיף 4. חדשים בזה? התחילו ב-<a href="web-intro.html">מה זה HTML, CSS ו-JavaScript?</a>',
     [
         ('1. הצעד הראשון: לחיצה על כפתור', [
             '<p>כמעט כל קוד JavaScript באתר עובד ככה: <strong>מוצאים</strong> אלמנט בעמוד, <strong>מחכים</strong> שמשהו יקרה לו (לחיצה), ואז <strong>משנים</strong> משהו.</p>',
             pg('''
<button id="myBtn">לחצו עליי</button>
<p id="message"></p>''', js='''
// 1. מוצאים את הכפתור לפי ה-id שלו
var btn = document.getElementById("myBtn");

// 2. מחכים ללחיצה
btn.addEventListener("click", function () {

    // 3. משנים את הטקסט של הפסקה
    document.getElementById("message").textContent = "לחצתם! 🎉";
});''', title='נסו: שנו את ההודעה, או הוסיפו שורה שמשנה גם את טקסט הכפתור', height=150),
             table(['שורה', 'מה היא עושה'], [
                 [c('document.getElementById("myBtn")'), 'מוצא בעמוד את התגית עם ' + c('id="myBtn"') + '.'],
                 [c('addEventListener("click", function () { ... })'), '"כשלוחצים, תריץ את מה שבסוגריים המסולסלים".'],
                 [c('.textContent = "..."'), 'מחליף את הטקסט שבתוך התגית.'],
                 [c('// ...'), 'הערה. JavaScript מתעלם ממנה.'],
             ]),
         ]),
         ('2. console.log: הודעות למתכנת', [
             '<p>' + c('alert') + ' מקפיץ הודעה <strong>למשתמש</strong>. אבל כשרוצים לבדוק מה קורה בקוד (מה הערך של משתנה, האם פונקציה רצה בכלל), כותבים הודעה <strong>לעצמנו</strong>, ב-Console. המשתמש לא רואה אותה.</p>',
             concept('Console', f'חלון בכלי המפתחים של הדפדפן ({c("F12")} ← לשונית Console), שמציג הודעות מהקוד ושגיאות. בעורכים בעמוד הזה, ההודעות מופיעות בחלון שחור מתחת לתוצאה.'),
             table(['פקודה', 'איך זה נראה', 'מתי משתמשים'], [
                 [c('console.log("טקסט", x)'), 'שורה רגילה.', 'הכי נפוץ: להדפיס ערך של משתנה, או לבדוק שהקוד הגיע לשורה מסוימת.'],
                 [c('console.info(...)'), 'שורה עם סימן מידע (ℹ).', 'מידע כללי. בפועל, כמעט כמו log.'],
                 [c('console.warn(...)'), 'שורה <strong>צהובה</strong> עם ⚠.', 'משהו חשוד, אבל לא שגיאה.'],
                 [c('console.error(...)'), 'שורה <strong>אדומה</strong> עם ✖.', 'משהו השתבש. (גם שגיאות אמיתיות של JavaScript מופיעות באדום.)'],
                 [c('console.table(array)'), 'מערך או אובייקט כטבלה.', 'לראות רשימה של אובייקטים בבת אחת.'],
                 [c('console.clear()'), 'מנקה את החלון.', 'כשיש יותר מדי הודעות.'],
             ]),
             pg('''
<button id="go">לחצו ובדקו את ה-Console</button>''', js='''
var price = 120;
var products = [
    { name: "עט", price: 5 },
    { name: "מחברת", price: 12 }
];

document.getElementById("go").addEventListener("click", function () {
    console.log("הכפתור נלחץ!");
    console.log("המחיר הוא:", price);
    console.info("יש", products.length, "מוצרים");
    console.warn("המלאי עומד להיגמר");
    console.error("לא הצלחנו להתחבר לשרת (סתם, זו דוגמה)");
    console.table(products);
});''', title='נסו: לחצו על הכפתור, ואז הוסיפו console.log משלכם', height=110),
             '<div class="explanation"><strong>💡 טריק הדיבאג הכי פשוט:</strong> כשמשהו לא עובד, שימו ' + c('console.log') + ' בכמה מקומות בקוד. אם הודעה לא מופיעה, הקוד לא הגיע לשם. אם הערך שמודפס לא מה שציפיתם, מצאתם את הבעיה. (ב-C# יש לזה כלי חזק יותר: <a href="tool-debug.html">Breakpoints</a>.)</div>',
             '<div class="warning"><strong>⚠️ לפני שמסיימים:</strong> מחקו את ה-' + c('console.log') + '-ים שהוספתם לבדיקה. הם לא מזיקים, אבל קוד נקי יותר נוח לקרוא.</div>',
         ]),
         ('3. משתנים', [
             concept('משתנה', f'"קופסה" עם שם, ששומרת ערך. ב-JavaScript מגדירים עם {c("let")} (אפשר לשנות אחר כך) או {c("const")} (קבוע).',
                     f'דוגמה: {c("let count = 0;")} ואחר כך {c("count = count + 1;")}. בשונה מ-C#, לא כותבים את הסוג (int, string).'),
             pg('''
<button id="plus">+1</button>
<button id="reset">איפוס</button>
<p>לחצתם <strong id="count">0</strong> פעמים</p>''', js='''
let count = 0;

document.getElementById("plus").addEventListener("click", function () {
    count = count + 1;
    document.getElementById("count").textContent = count;
});

document.getElementById("reset").addEventListener("click", function () {
    count = 0;
    document.getElementById("count").textContent = count;
});''', title='נסו: הוסיפו כפתור "1-"', height=150),
         ]),
         ('4. מוצאים אלמנטים', [
             table(['פונקציה', 'מה היא מחזירה'], [
                 [c('document.getElementById("x")'), 'האלמנט עם ' + c('id="x"') + '.'],
                 [c('document.querySelector(".card")'), 'האלמנט <strong>הראשון</strong> שמתאים לסלקטור CSS (כמו בעמוד ה-CSS).'],
                 [c('document.querySelectorAll(".card")'), '<strong>כל</strong> האלמנטים שמתאימים. עוברים עליהם עם ' + c('forEach') + '.'],
             ]),
             pg('''
<p class="item">פריט א</p>
<p class="item">פריט ב</p>
<p class="item">פריט ג</p>
<button id="paint">צבעו את כולם</button>''', js='''
document.getElementById("paint").addEventListener("click", function () {
    document.querySelectorAll(".item").forEach(function (p) {
        p.style.color = "crimson";
        p.style.fontWeight = "bold";
    });
});''', title='נסו: החליפו querySelectorAll ב-querySelector. מה השתנה?', height=190),
         ]),
         ('5. משנים עיצוב עם classList', [
             '<p>אפשר לשנות עיצוב ישירות (' + c('element.style.color = "red"') + '), אבל עדיף להגדיר class ב-CSS, ורק להוסיף או להוריד אותו ב-JavaScript:</p>',
             table(['פונקציה', 'מה היא עושה'], [
                 [c('element.classList.add("x")'), 'מוסיפה את ה-class.'],
                 [c('element.classList.remove("x")'), 'מורידה.'],
                 [c('element.classList.toggle("x")'), 'אם יש, מורידה. אם אין, מוסיפה. מושלם לכפתורי "הפעל/כבה".'],
             ]),
             pg('''
<button id="mode">🌙 מצב לילה</button>
<div class="page">
    <h3>כותרת</h3>
    <p>טקסט כלשהו בעמוד.</p>
</div>''', css='''
.page {
    padding: 15px;
    transition: all 0.4s;
}

.page.dark {
    background-color: #222;
    color: white;
}''', js='''
document.getElementById("mode").addEventListener("click", function () {
    document.querySelector(".page").classList.toggle("dark");
});''', title='נסו: בלשונית CSS שנו את הצבעים של .dark', height=190),
         ]),
         ('6. הצגה והסתרה', [
             pg('''
<button id="toggle">הצג תשובה</button>
<p id="answer" hidden>התשובה היא 42 🙂</p>''', js='''
var btn = document.getElementById("toggle");
var answer = document.getElementById("answer");

btn.addEventListener("click", function () {
    answer.hidden = !answer.hidden;
    btn.textContent = answer.hidden ? "הצג תשובה" : "הסתר תשובה";
});''', title='נסו: הוסיפו עוד שאלה ותשובה', height=130),
             concept('מה זה ? :', f'תנאי מקוצר: {c("תנאי ? אם-כן : אם-לא")}. כאן: אם התשובה מוסתרת, הכפתור אומר "הצג". אחרת, "הסתר".'),
         ]),
         ('7. אירועים נוספים: הקלדה', [
             '<p>חוץ מ-' + c('"click"') + ' יש עוד אירועים. ' + c('"input"') + ' קורה בכל פעם שהמשתמש מקליד בשדה:</p>',
             pg('''
<label for="name">איך קוראים לכם?</label>
<input type="text" id="name">
<p id="greet"></p>''', js='''
document.getElementById("name").addEventListener("input", function () {
    var name = this.value;
    document.getElementById("greet").textContent = name ? "שלום, " + name + "!" : "";
});''', title='נסו: הקלידו שם', height=130),
             table(['אירוע', 'מתי'], [
                 [c('click'), 'לחיצה.'], [c('input'), 'כל הקלדה בשדה.'], [c('change'), 'שינוי של select או checkbox.'],
                 [c('submit'), 'שליחת טופס.'], [c('mouseover'), 'העכבר נכנס לאלמנט.'],
             ]),
         ]),
         ('8. רשימות ולולאות', [
             '<p>מערך (' + c('[ ]') + ') הוא רשימה. לולאה עוברת עליו ובונה HTML לכל פריט:</p>',
             pg('''
<input type="text" id="newItem" placeholder="משימה חדשה">
<button id="add">הוסף</button>
<ul id="list"></ul>''', js='''
let tasks = ["לקנות חלב", "לעשות שיעורי בית"];

function showTasks() {
    var list = document.getElementById("list");
    list.innerHTML = "";
    tasks.forEach(function (task) {
        var li = document.createElement("li");
        li.textContent = task;
        list.appendChild(li);
    });
}

document.getElementById("add").addEventListener("click", function () {
    var input = document.getElementById("newItem");
    if (input.value !== "") {
        tasks.push(input.value);
        input.value = "";
        showTasks();
    }
});

showTasks();''', title='נסו: הוסיפו משימות, או שנו את המשימות ההתחלתיות', height=220),
             table(['קוד', 'מה הוא עושה'], [
                 [c('tasks.push(x)'), 'מוסיף פריט לסוף המערך.'],
                 [c('document.createElement("li")'), 'יוצר תגית חדשה (עוד לא בעמוד).'],
                 [c('list.appendChild(li)'), 'מכניס אותה לעמוד, בסוף הרשימה.'],
                 [c('function showTasks() { ... }'), 'פונקציה משלנו, שאפשר לקרוא לה כמה פעמים.'],
             ]),
         ]),
         ('9. בדיקת טופס לפני שליחה', [
             pg('''
<form id="signup">
    <input type="text" id="user" placeholder="שם משתמש">
    <button type="submit">הרשמה</button>
    <p id="error" style="color:red"></p>
</form>''', js='''
document.getElementById("signup").addEventListener("submit", function (event) {
    var user = document.getElementById("user").value;

    if (user.length < 3) {
        event.preventDefault();   // עוצר את שליחת הטופס
        document.getElementById("error").textContent = "שם המשתמש חייב להיות לפחות 3 תווים";
    } else {
        event.preventDefault();   // (רק בדוגמה הזאת, כדי לא לצאת מהעמוד)
        document.getElementById("error").textContent = "";
        alert("נשלח! 🎉");
    }
});''', title='נסו: שלחו עם שם קצר, ואז עם שם ארוך', height=150),
             '<div class="warning"><strong>⚠️ חשוב:</strong> בדיקה ב-JavaScript היא רק לנוחות. משתמש יכול לעקוף אותה, ולכן תמיד בודקים <strong>גם בשרת</strong>. בפרויקט, ASP.NET עושה את שתי הבדיקות בשבילכם (מדריך 12).</div>',
         ]),
         ('10. חלונות קופצים', [
             table(['פונקציה', 'מה היא עושה'], [
                 [c('alert("טקסט")'), 'הודעה עם כפתור "אישור".'],
                 [c('confirm("בטוחים?")'), 'שאלה עם "אישור" ו"ביטול". מחזירה ' + c('true') + ' או ' + c('false') + '.'],
                 [c('prompt("איך קוראים לך?")'), 'שאלה עם תיבת טקסט. מחזירה את מה שהמשתמש הקליד (או ' + c('null') + ' אם ביטל).'],
             ]),
             pg('''
<button id="del">מחיקה</button>
<p id="status"></p>''', js='''
document.getElementById("del").addEventListener("click", function () {
    if (confirm("בטוחים שרוצים למחוק?")) {
        document.getElementById("status").textContent = "נמחק ✔";
    } else {
        document.getElementById("status").textContent = "בוטל";
    }
});''', title='נסו: לחצו, ובחרו פעם "אישור" ופעם "ביטול"', height=120),
             pg('''
<button id="ask">הכירו אותי</button>
<p id="hello"></p>''', js='''
document.getElementById("ask").addEventListener("click", function () {
    var name = prompt("איך קוראים לך?");
    if (name) {
        document.getElementById("hello").textContent = "נעים מאוד, " + name + "! 👋";
    }
});''', title='נסו: prompt', height=110),
             '<div class="explanation"><strong>💡 מתי להשתמש בהם?</strong> הם נוחים לבדיקות ולדברים קטנים (כמו "בטוחים שרוצים למחוק?"). באתר מעוצב עדיף להציג הודעות בתוך העמוד, או בחלון קופץ של Bootstrap (בספריית קטעי הקוד: "חלון קופץ").</div>',
             '<div class="explanation"><strong>💡 בפרויקט:</strong> חלון אישור לפני מחיקה, בשורה אחת: בספריית קטעי הקוד, "חלון אישור לפני מחיקה". ו-JavaScript שמדבר עם השרת בלי לטעון את העמוד: מתקדם ד.</div>',
         ]),
         ('11. כשמשהו לא עובד', [
             '<p>ב-JavaScript, שגיאה אחת עוצרת את כל הקוד שאחריה, ובדרך כלל <strong>לא רואים אותה בעמוד</strong>. איפה מוצאים אותה:</p>',
             '<ul><li><strong>בעמוד הזה:</strong> שגיאה תופיע בפס אדום מתחת לתוצאה. נסו לכתוב בדוגמה ' + c('getElementByid') + ' (עם d קטנה).</li><li><strong>באתר שלכם:</strong> F12 ← Console. השגיאה מופיעה שם באדום, עם הקובץ ומספר השורה.</li><li><strong>אין שגיאה, אבל זה לא עובד?</strong> הוסיפו ' + c('console.log') + ' (סעיף 2) כדי לראות עד איפה הקוד מגיע ומה הערכים.</li></ul>',
             table(['שגיאה נפוצה', 'הסיבה'], [
                 [c("Cannot read properties of null"), 'ה-id בקוד לא זהה ל-id בתגית, או שהסקריפט רץ לפני שהתגית קיימת.'],
                 [c('... is not a function'), 'טעות כתיב בשם פונקציה. JavaScript רגיש לאותיות גדולות: ' + c('getElementById') + ' ולא ' + c('getElementByid') + '.'],
                 [c('... is not defined'), 'משתנה שלא הוגדר, או טעות כתיב בשם שלו.'],
             ]),
         ]),
     ],
     ['מוצאים אלמנט (getElementById / querySelector), מחכים לאירוע (addEventListener), ומשנים משהו (textContent, classList).',
      'console.log (וגם warn, error, table) כותב הודעות לעצמכם ב-Console. alert, confirm ו-prompt מדברים עם המשתמש.',
      'משתנים עם let ו-const. מערכים עם [ ], ו-forEach עובר עליהם.',
      'hidden מסתיר, classList.toggle מחליף עיצוב.',
      'בדיקה ב-JavaScript היא לנוחות. הבדיקה האמיתית בשרת.',
      'שגיאות רואים ב-F12 ← Console.'],
     'ההמשך באתר: <a href="web-js2.html">JavaScript חלק ב\'</a> (אובייקטים, טיימרים, משחקים קטנים ו-localStorage). מדריך מלא: <a href="https://www.w3schools.com/js/" target="_blank">w3schools JavaScript</a>, או <a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript" target="_blank">MDN</a> (באנגלית).')



def code(src, lang=None):
    attr = f' data-lang="{lang}"' if lang else ''
    return f'<pre class="code-block"{attr}>{html.escape(src.strip(chr(10)))}</pre>'


def box(kind, title, text):
    return f'<div class="{kind}"><strong>{title}</strong> {text}</div>'


exec(open(os.path.join(os.path.dirname(__file__), 'web_intro.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(__file__), 'web_part2.py'), encoding='utf-8').read())

print('built web basics pages')
