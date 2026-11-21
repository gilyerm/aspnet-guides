// רשימת כל המדריכים באתר.
// כדי לפרסם מדריך חדש: יוצרים את הקובץ בתיקיית guides ומשנים כאן ready ל-true.
(function () {
    var SECTIONS = [
        { id: 'start', title: 'התחלה וכלים', note: 'מכאן מתחילים: הקמת הפרויקט והכלים שנעבוד איתם כל הזמן.' },
        { id: 'pages', title: 'בניית עמודים', note: 'איך אתר MVC עובד, ואיך בונים ומעצבים עמודים.' },
        { id: 'data', title: 'נתונים', note: 'מודלים, טפסים ומסד נתונים.' },
        { id: 'users', title: 'תמונות ומשתמשים', note: '' },
        { id: 'advanced', title: 'רשות למתקדמים', note: 'למי שסיים את המסלול הבסיסי ורוצה להמשיך.' },
        { id: 'tools', title: 'עזרים', note: 'לשימוש בכל שלב.' }
    ];

    var GUIDES = [
        { num: '1', slug: '01-create-project', section: 'start', title: 'יצירת פרויקט', desc: 'פרויקט MVC עם מערכת משתמשים, מבנה התיקיות והרצה ראשונה', ready: true },
        { num: '2', slug: '02-visual-studio', section: 'start', title: 'עבודה ב-Visual Studio', desc: 'הכרת המסך, הרצה, קיצורים, NuGet וצפייה במסד הנתונים', ready: true },
        { num: '3', slug: '03-git-github', section: 'start', title: 'Git ו-GitHub', desc: 'שמירת גיבוי ב-GitHub בלחיצות כפתור, ומעבר בין מחשבים', ready: true },

        { num: '4', slug: '04-how-mvc-works', section: 'pages', title: 'איך אתר MVC עובד', desc: 'התמונה הכללית: כתובת, Controller, View ודפדפן' },
        { num: '5', slug: '05-cshtml', section: 'pages', title: 'מה זה cshtml?', desc: 'HTML משולב עם C#, הסימן @ ותחביר Razor' },
        { num: '6', slug: '06-layout', section: 'pages', title: 'Layout ותפריט', desc: 'הקובץ שעוטף את כל העמודים, וקישורים בתפריט' },
        { num: '7', slug: '07-new-pages', section: 'pages', title: 'עמודים חדשים', desc: 'עמוד ב-Controller קיים, או אזור חדש עם Controller משלו' },
        { num: '8', slug: '08-css-js', section: 'pages', title: 'CSS ו-JS', desc: 'קבצי עיצוב וסקריפטים, עברית מימין לשמאל, וכלי המפתחים' },
        { num: '9', slug: '09-bootstrap', section: 'pages', title: 'Bootstrap', desc: 'רכיבים מוכנים לאתר יפה בלי הרבה CSS' },

        { num: '10', slug: '10-models', section: 'data', title: 'מודלים', desc: 'מחלקה שמייצגת נתונים, והעברת מידע ל-View' },
        { num: '11', slug: '11-forms', section: 'data', title: 'טפסים', desc: 'ממלאים טופס והמידע מגיע לשרת' },
        { num: '12', slug: '12-validation', section: 'data', title: 'בדיקת קלט', desc: '"שדה חובה", "אימייל לא תקין" ועוד' },
        { num: '13', slug: '13-database', section: 'data', title: 'מסד נתונים', desc: 'טבלה משלכם, DbContext ו-Migrations' },
        { num: '14', slug: '14-relationships', section: 'data', title: 'קשרים בין טבלאות', desc: 'קטגוריה עם הרבה מוצרים, משתמש עם הרבה הזמנות' },
        { num: '15', slug: '15-scaffolding', section: 'data', title: 'הכול בלחיצת כפתור', desc: 'עמודי הצגה, הוספה, עריכה ומחיקה שנוצרים לבד' },

        { num: '16', slug: '16-images', section: 'users', title: 'העלאת תמונות', desc: 'טופס להעלאת קובץ, שמירה והצגה' },
        { num: '17', slug: '17-users', section: 'users', title: 'עבודה עם משתמשים', desc: 'עמודים למחוברים בלבד, המשתמש המחובר ותפקידים' },

        { num: 'א', slug: 'adv-a-partial-views', section: 'advanced', title: 'Partial Views', desc: 'חלקי עמוד שחוזרים על עצמם' },
        { num: 'ב', slug: 'adv-b-search', section: 'advanced', title: 'חיפוש וסינון', desc: 'הצגת חלק מהנתונים עם LINQ' },
        { num: 'ג', slug: 'adv-c-identity', section: 'advanced', title: 'התאמת ההרשמה', desc: 'שדות נוספים למשתמש ודפי הרשמה בעברית' },
        { num: 'ד', slug: 'adv-d-fetch', section: 'advanced', title: 'JS שמדבר עם השרת', desc: 'עדכון חלק מהעמוד בלי לטעון מחדש' },
        { num: 'ה', slug: 'adv-e-cart', section: 'advanced', title: 'עגלת קניות', desc: 'הוספה לעגלה, עמוד עגלה ומחיקה' },

        { num: '🛠️', slug: 'tool-errors', section: 'tools', title: 'קריאת שגיאות ושגיאות נפוצות', desc: 'איך מבינים מה השתבש, ואיך מתקנים' },
        { num: '🛠️', slug: 'tool-debug', section: 'tools', title: 'דיבאג עם Breakpoints', desc: 'עוצרים את הקוד ובודקים ערכים' },
        { num: '🛠️', slug: 'tool-planning', section: 'tools', title: 'תכנון הפרויקט', desc: 'תבנית למילוי לפני שמתחילים לכתוב קוד' },
        { num: '📚', slug: 'snippets', section: 'tools', title: 'ספריית קטעי קוד', desc: 'קטעים מוכנים להעתקה, עם הסבר מה לשנות' }
    ];

    var script = document.currentScript;
    var root = new URL('..', script.src).href; // תיקיית הבסיס של האתר

    function guideUrl(g) { return root + 'guides/' + g.slug + '.html'; }

    function el(tag, attrs, html) {
        var e = document.createElement(tag);
        for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
        if (html !== undefined) e.innerHTML = html;
        return e;
    }

    // ---------- כותרת עליונה ----------
    var header = el('header', { 'class': 'site-header' },
        '<div class="inner">' +
        '<a class="brand" href="' + root + 'index.html">🎓 מדריכי ASP.NET Core MVC</a>' +
        '<nav><a href="' + root + 'index.html">כל המדריכים</a>' +
        (GUIDES.some(function (g) { return g.slug === 'snippets' && g.ready; })
            ? '<a href="' + root + 'guides/snippets.html">קטעי קוד</a>' : '') +
        '</nav>' +
        '</div>');
    document.body.insertBefore(header, document.body.firstChild);

    // ---------- כפתור העתקה לכל בלוק קוד ----------
    document.querySelectorAll('pre.code-block').forEach(function (pre) {
        var wrap = el('div', { 'class': 'code-wrap' });
        pre.parentNode.insertBefore(wrap, pre);
        wrap.appendChild(pre);
        var btn = el('button', { 'class': 'copy-btn', 'type': 'button' }, 'העתק');
        btn.addEventListener('click', function () {
            var text = pre.innerText.replace(/ /g, ' ');
            var done = function () {
                btn.textContent = '✓ הועתק';
                setTimeout(function () { btn.textContent = 'העתק'; }, 1500);
            };
            if (navigator.clipboard) {
                navigator.clipboard.writeText(text).then(done, function () { btn.textContent = 'סמנו והעתיקו ידנית'; });
            }
        });
        wrap.appendChild(btn);
    });

    // ---------- הקודם / הבא ----------
    var current = document.body.getAttribute('data-guide');
    var main = document.querySelector('main');
    if (current && main) {
        var ready = GUIDES.filter(function (g) { return g.ready; });
        var i = ready.findIndex(function (g) { return g.slug === current; });
        if (i !== -1) {
            var pager = el('nav', { 'class': 'guide-pager' });
            if (i > 0) {
                var p = ready[i - 1];
                pager.appendChild(el('a', { href: guideUrl(p), 'class': 'prev' }, '<small>→ המדריך הקודם</small>' + p.num + '. ' + p.title));
            }
            if (i < ready.length - 1) {
                var n = ready[i + 1];
                pager.appendChild(el('a', { href: guideUrl(n), 'class': 'next' }, '<small>המדריך הבא ←</small>' + n.num + '. ' + n.title));
            }
            main.appendChild(pager);
        }
    }

    // ---------- רשימת המדריכים בדף הבית ----------
    var index = document.getElementById('guide-index');
    if (index) {
        SECTIONS.forEach(function (s) {
            var sec = el('section', { 'class': 'home-section' });
            sec.appendChild(el('h2', {}, s.title));
            if (s.note) sec.appendChild(el('p', { 'class': 'section-note' }, s.note));
            var ul = el('ul', { 'class': 'guide-cards' });
            GUIDES.filter(function (g) { return g.section === s.id; }).forEach(function (g) {
                var inner = '<span class="num">' + (/^[0-9א-ת]+$/.test(g.num) ? 'מדריך ' + g.num : g.num) + '</span>' +
                    '<span class="title">' + g.title + '</span>' +
                    '<span class="desc">' + g.desc + '</span>' +
                    (g.ready ? '' : '<br><span class="badge">בקרוב</span>');
                var li = el('li', { 'class': 'guide-card ' + (g.ready ? 'ready' : 'soon') });
                li.innerHTML = g.ready ? '<a href="' + guideUrl(g) + '">' + inner + '</a>' : inner;
                ul.appendChild(li);
            });
            sec.appendChild(ul);
            index.appendChild(sec);
        });
    }

    document.body.appendChild(el('footer', { 'class': 'site-footer' }, 'מדריכים לתלמידים · ASP.NET Core MVC'));
})();
