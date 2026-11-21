// רשימת כל המדריכים באתר.
// כדי לפרסם מדריך חדש: יוצרים את הקובץ בתיקיית guides ומשנים כאן ready ל-true.
// keywords: מילים נוספות שהחיפוש בדף הראשי ימצא.
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
        { num: '1', slug: '01-create-project', section: 'start', title: 'יצירת פרויקט', desc: 'פרויקט MVC עם מערכת משתמשים, מבנה התיקיות והרצה ראשונה', ready: true,
          keywords: 'Individual Accounts תבנית wwwroot Controllers Models Views Program.cs appsettings תיקיות SSL אישור' },
        { num: '2', slug: '02-visual-studio', section: 'start', title: 'עבודה ב-Visual Studio', desc: 'הכרת המסך, הרצה, קיצורים, NuGet וצפייה במסד הנתונים', ready: true,
          keywords: 'Solution Explorer Error List Output localhost Hot Reload IntelliSense קיצורי מקלדת NuGet חבילה Package Manager Console SQL Server Object Explorer Apply Migrations Register LocalDB דיבאג הרצה עצירה' },
        { num: '3', slug: '03-git-github', section: 'start', title: 'Git ו-GitHub', desc: 'שמירת גיבוי ב-GitHub בלחיצות כפתור, ומעבר בין מחשבים', ready: true,
          keywords: 'Commit Push Pull Clone מאגר Repository גיבוי בית בית ספר Update-Database gitignore Conflict' },

        { num: '4', slug: '04-how-mvc-works', section: 'pages', title: 'איך אתר MVC עובד', desc: 'התמונה הכללית: כתובת, Controller, View ודפדפן', ready: true,
          keywords: 'Model View Controller Action בקשה כתובת URL ניתוב Routing return View' },
        { num: '5', slug: '05-cshtml', section: 'pages', title: 'מה זה cshtml?', desc: 'HTML משולב עם C#, הסימן @ ותחביר Razor', ready: true,
          keywords: 'Razor @ ViewData לולאה foreach if תנאי משתנה' },
        { num: '6', slug: '06-layout', section: 'pages', title: 'Layout ותפריט', desc: 'הקובץ שעוטף את כל העמודים, וקישורים בתפריט', ready: true,
          keywords: '_Layout RenderBody navbar תפריט קישור asp-controller asp-action footer כותרת' },
        { num: '7', slug: '07-new-pages', section: 'pages', title: 'עמודים חדשים', desc: 'עמוד ב-Controller קיים, או אזור חדש עם Controller משלו', ready: true,
          keywords: 'Add View Add Controller Action כללי שמות Razor View Empty MVC Controller Empty עמוד חדש' },
        { num: '8', slug: '08-css-js', section: 'pages', title: 'CSS ו-JS', desc: 'קבצי עיצוב וסקריפטים, עברית מימין לשמאל, וכלי המפתחים', ready: true,
          keywords: 'wwwroot site.css site.js RenderSection Styles Scripts asp-append-version מטמון RTL עברית F12 Console' },
        { num: '9', slug: '09-bootstrap', section: 'pages', title: 'Bootstrap', desc: 'רכיבים מוכנים לאתר יפה בלי הרבה CSS', ready: true,
          keywords: 'כרטיס card טבלה table כפתור btn רשת grid row col container alert צבעים' },

        { num: '10', slug: '10-models', section: 'data', title: 'מודלים', desc: 'מחלקה שמייצגת נתונים, והעברת מידע ל-View',
          keywords: 'Model מחלקה class property @model' },
        { num: '11', slug: '11-forms', section: 'data', title: 'טפסים', desc: 'ממלאים טופס והמידע מגיע לשרת',
          keywords: 'form POST GET HttpPost asp-for ValidateAntiForgeryToken' },
        { num: '12', slug: '12-validation', section: 'data', title: 'בדיקת קלט', desc: '"שדה חובה", "אימייל לא תקין" ועוד',
          keywords: 'Validation Required ModelState ErrorMessage' },
        { num: '13', slug: '13-database', section: 'data', title: 'מסד נתונים', desc: 'טבלה משלכם, DbContext ו-Migrations',
          keywords: 'DbContext DbSet Migration Add-Migration Update-Database LocalDB טבלה' },
        { num: '14', slug: '14-relationships', section: 'data', title: 'קשרים בין טבלאות', desc: 'קטגוריה עם הרבה מוצרים, משתמש עם הרבה הזמנות',
          keywords: 'Foreign Key מפתח זר Include אחד לרבים' },
        { num: '15', slug: '15-scaffolding', section: 'data', title: 'הכול בלחיצת כפתור', desc: 'עמודי הצגה, הוספה, עריכה ומחיקה שנוצרים לבד',
          keywords: 'Scaffolding CRUD async await Entity Framework' },

        { num: '16', slug: '16-images', section: 'users', title: 'העלאת תמונות', desc: 'טופס להעלאת קובץ, שמירה והצגה',
          keywords: 'IFormFile upload קובץ תמונה wwwroot' },
        { num: '17', slug: '17-users', section: 'users', title: 'עבודה עם משתמשים', desc: 'עמודים למחוברים בלבד, המשתמש המחובר ותפקידים',
          keywords: 'Authorize Roles מנהל Admin User.Identity Login' },

        { num: 'א', slug: 'adv-a-partial-views', section: 'advanced', title: 'Partial Views', desc: 'חלקי עמוד שחוזרים על עצמם' },
        { num: 'ב', slug: 'adv-b-search', section: 'advanced', title: 'חיפוש וסינון', desc: 'הצגת חלק מהנתונים עם LINQ', keywords: 'LINQ Where OrderBy' },
        { num: 'ג', slug: 'adv-c-identity', section: 'advanced', title: 'התאמת ההרשמה', desc: 'שדות נוספים למשתמש ודפי הרשמה בעברית', keywords: 'Identity ApplicationUser Scaffold' },
        { num: 'ד', slug: 'adv-d-fetch', section: 'advanced', title: 'JS שמדבר עם השרת', desc: 'עדכון חלק מהעמוד בלי לטעון מחדש', keywords: 'fetch JSON AJAX' },
        { num: 'ה', slug: 'adv-e-cart', section: 'advanced', title: 'עגלת קניות', desc: 'הוספה לעגלה, עמוד עגלה ומחיקה', keywords: 'Session חנות' },

        { num: '🛠️', slug: 'tool-errors', section: 'tools', title: 'קריאת שגיאות ושגיאות נפוצות', desc: 'איך מבינים מה השתבש, ואיך מתקנים', keywords: 'Error שגיאה Exception Clean Rebuild' },
        { num: '🛠️', slug: 'tool-debug', section: 'tools', title: 'דיבאג עם Breakpoints', desc: 'עוצרים את הקוד ובודקים ערכים', keywords: 'Breakpoint F10 F11 Watch' },
        { num: '🛠️', slug: 'tool-planning', section: 'tools', title: 'תכנון הפרויקט', desc: 'תבנית למילוי לפני שמתחילים לכתוב קוד' },
        { num: '📚', slug: 'snippets', section: 'tools', title: 'ספריית קטעי קוד', desc: 'קטעים מוכנים להעתקה, עם הסבר מה לשנות' }
    ];

    var script = document.currentScript;
    var root = new URL('..', script.src).href; // תיקיית הבסיס של האתר
    var current = document.body.getAttribute('data-guide');
    var main = document.querySelector('main');

    function guideUrl(g) { return root + 'guides/' + g.slug + '.html'; }
    function numLabel(g) { return /^[0-9א-ת]+$/.test(g.num) ? 'מדריך ' + g.num : g.num; }

    function el(tag, attrs, html) {
        var e = document.createElement(tag);
        for (var k in attrs || {}) e.setAttribute(k, attrs[k]);
        if (html !== undefined) e.innerHTML = html;
        return e;
    }

    // ---------- זיכרון: אילו מדריכים כבר נפתחו (רק בדפדפן הזה) ----------
    var VISITED_KEY = 'aspnet-guides-visited';
    function getVisited() {
        try { return JSON.parse(localStorage.getItem(VISITED_KEY)) || {}; } catch (e) { return {}; }
    }
    function markVisited(slug) {
        try { var v = getVisited(); v[slug] = true; localStorage.setItem(VISITED_KEY, JSON.stringify(v)); } catch (e) { }
    }
    if (current) markVisited(current);
    var visited = getVisited();

    // ---------- כותרת עליונה עם תפריט "כל המדריכים" ----------
    var menuHtml = SECTIONS.map(function (s) {
        var items = GUIDES.filter(function (g) { return g.section === s.id; }).map(function (g) {
            var label = '<span class="m-num">' + g.num + '</span> ' + g.title;
            if (!g.ready) return '<li class="soon">' + label + ' <small>(בקרוב)</small></li>';
            var cls = g.slug === current ? ' class="current"' : '';
            return '<li' + cls + '><a href="' + guideUrl(g) + '">' + label + (visited[g.slug] ? ' <span class="tick">✓</span>' : '') + '</a></li>';
        }).join('');
        return '<div class="menu-section"><h4>' + s.title + '</h4><ul>' + items + '</ul></div>';
    }).join('');

    var header = el('header', { 'class': 'site-header' },
        '<div class="inner">' +
        '<a class="brand" href="' + root + 'index.html">🎓 <span>מדריכי ASP.NET Core MVC</span></a>' +
        '<nav>' +
        '<button type="button" class="menu-btn" aria-expanded="false">כל המדריכים ▾</button>' +
        (GUIDES.some(function (g) { return g.slug === 'snippets' && g.ready; })
            ? '<a href="' + root + 'guides/snippets.html">קטעי קוד</a>' : '') +
        '</nav>' +
        '</div>' +
        '<div class="guide-menu" hidden><div class="inner">' + menuHtml + '</div></div>');
    document.body.insertBefore(header, document.body.firstChild);

    var menuBtn = header.querySelector('.menu-btn');
    var menu = header.querySelector('.guide-menu');
    function setMenu(open) {
        menu.hidden = !open;
        menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }
    menuBtn.addEventListener('click', function (e) { e.stopPropagation(); setMenu(menu.hidden); });
    document.addEventListener('click', function (e) { if (!menu.hidden && !menu.contains(e.target)) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });

    // ---------- תוכן עניינים בתוך מדריך ----------
    if (current && main) {
        var heads = main.querySelectorAll(':scope > h2');
        if (heads.length >= 3) {
            var toc = el('nav', { 'class': 'toc' }, '<strong>📑 בעמוד הזה</strong>');
            var ol = el('ul');
            heads.forEach(function (h, i) {
                if (!h.id) h.id = 'part-' + (i + 1);
                var li = el('li');
                li.appendChild(el('a', { href: '#' + h.id }, h.textContent));
                ol.appendChild(li);
            });
            toc.appendChild(ol);
            var anchor = main.querySelector('.subtitle');
            if (anchor) anchor.insertAdjacentElement('afterend', toc);
        }
    }

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
            } else {
                btn.textContent = 'סמנו והעתיקו ידנית';
            }
        });
        wrap.appendChild(btn);
    });

    // ---------- הקודם / הבא ----------
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

    // ---------- כפתור "חזרה למעלה" ----------
    var topBtn = el('button', { 'class': 'to-top', 'type': 'button', 'aria-label': 'חזרה למעלה', 'title': 'חזרה למעלה' }, '↑');
    topBtn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
    document.body.appendChild(topBtn);
    window.addEventListener('scroll', function () { topBtn.classList.toggle('show', window.scrollY > 600); }, { passive: true });

    // ---------- דף הבית: חיפוש ורשימת המדריכים ----------
    var index = document.getElementById('guide-index');
    if (index) {
        var searchBox = el('div', { 'class': 'search-box' },
            '<input type="search" placeholder="🔍 חיפוש מדריך (למשל: טופס, Migration, תפריט)" aria-label="חיפוש מדריך">');
        index.parentNode.insertBefore(searchBox, index);
        var noResults = el('p', { 'class': 'no-results', hidden: '' }, 'לא נמצא מדריך מתאים. נסו מילה אחרת.');
        index.parentNode.insertBefore(noResults, index.nextSibling);

        SECTIONS.forEach(function (s) {
            var sec = el('section', { 'class': 'home-section' });
            sec.appendChild(el('h2', {}, s.title));
            if (s.note) sec.appendChild(el('p', { 'class': 'section-note' }, s.note));
            var ul = el('ul', { 'class': 'guide-cards' });
            GUIDES.filter(function (g) { return g.section === s.id; }).forEach(function (g) {
                var inner = '<span class="num">' + numLabel(g) + (visited[g.slug] && g.ready ? ' <span class="tick" title="כבר פתחתם את המדריך הזה">✓ נקרא</span>' : '') + '</span>' +
                    '<span class="title">' + g.title + '</span>' +
                    '<span class="desc">' + g.desc + '</span>' +
                    (g.ready ? '' : '<br><span class="badge">בקרוב</span>');
                var li = el('li', { 'class': 'guide-card ' + (g.ready ? 'ready' : 'soon') });
                li.setAttribute('data-search', (g.num + ' ' + g.title + ' ' + g.desc + ' ' + (g.keywords || '')).toLowerCase());
                li.innerHTML = g.ready ? '<a href="' + guideUrl(g) + '">' + inner + '</a>' : inner;
                ul.appendChild(li);
            });
            sec.appendChild(ul);
            index.appendChild(sec);
        });

        searchBox.querySelector('input').addEventListener('input', function () {
            var q = this.value.trim().toLowerCase();
            var any = false;
            index.querySelectorAll('.home-section').forEach(function (sec) {
                var shown = 0;
                sec.querySelectorAll('.guide-card').forEach(function (card) {
                    var match = !q || card.getAttribute('data-search').indexOf(q) !== -1;
                    card.hidden = !match;
                    if (match) shown++;
                });
                sec.hidden = shown === 0;
                if (shown) any = true;
            });
            noResults.hidden = any;
        });
    }

    document.body.appendChild(el('footer', { 'class': 'site-footer' }, 'מדריכים לתלמידים · ASP.NET Core MVC'));
})();
