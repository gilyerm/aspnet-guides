// רשימת כל המדריכים באתר.
// כדי לפרסם מדריך חדש: יוצרים את הקובץ בתיקיית guides ומשנים כאן ready ל-true.
// keywords: מילים נוספות שהחיפוש בדף הראשי ימצא.
(function () {
    var SECTIONS = [
        { id: 'start', title: 'התחלה וכלים', note: 'מכאן מתחילים: הקמת הפרויקט והכלים שנעבוד איתם כל הזמן.' },
        { id: 'web', title: 'יסודות הווב: HTML, CSS ו-JavaScript', note: 'חומר עזר עם דוגמאות שאפשר לשנות ולראות את התוצאה מיד. חזרו לכאן בכל פעם שמשהו לא ברור.' },
        { id: 'pages', title: 'בניית עמודים', note: 'איך אתר MVC עובד, ואיך בונים ומעצבים עמודים.' },
        { id: 'data', title: 'נתונים', note: 'מודלים, טפסים ומסד נתונים.' },
        { id: 'users', title: 'תמונות ומשתמשים', note: '' },
        { id: 'advanced', title: 'רשות למתקדמים', note: 'למי שסיים את המסלול הבסיסי ורוצה להמשיך.' },
        { id: 'tools', title: 'עזרים', note: 'לשימוש בכל שלב.' }
    ];

    var GUIDES = [
        { num: '0', slug: '00-install-vs', section: 'start', title: 'התקנת Visual Studio 2026', desc: 'הורדה, בחירת הרכיבים הנכונים והתחברות לחשבון', ready: true,
          keywords: 'התקנה Install Community Workloads ASP.NET and web development Installer Modify Repair Sign in' },
        { num: '1', slug: '01-create-project', section: 'start', title: 'יצירת פרויקט', desc: 'פרויקט MVC עם מערכת משתמשים, מבנה התיקיות והרצה ראשונה', ready: true,
          keywords: 'Individual Accounts תבנית wwwroot Controllers Models Views Program.cs appsettings תיקיות SSL אישור' },
        { num: '2', slug: '02-visual-studio', section: 'start', title: 'עבודה ב-Visual Studio', desc: 'הכרת המסך, הרצה, קיצורים, NuGet וצפייה במסד הנתונים', ready: true,
          keywords: 'Solution Explorer Error List Output localhost Hot Reload IntelliSense קיצורי מקלדת NuGet חבילה Package Manager Console SQL Server Object Explorer Apply Migrations Register LocalDB דיבאג הרצה עצירה' },
        { num: '3', slug: '03-git-github', section: 'start', title: 'Git ו-GitHub', desc: 'שמירת גיבוי ב-GitHub בלחיצות כפתור, ומעבר בין מחשבים', ready: true,
          keywords: 'Commit Push Pull Clone מאגר Repository גיבוי בית בית ספר Update-Database gitignore Conflict' },

        { num: 'מבוא', slug: 'web-intro', section: 'web', title: 'מה זה HTML, CSS ו-JavaScript?', desc: 'שלוש השפות של כל עמוד אינטרנט: מה כל אחת עושה ואיפה היא בפרויקט', ready: true,
          keywords: 'שפה שפות דפדפן שרת Browser Server שלד עיצוב התנהגות מבוא Java C#' },
        { num: 'HTML', slug: 'web-html', section: 'web', title: 'יסודות HTML', desc: 'תגיות, קישורים ותמונות, רשימות, טבלאות וטפסים, עם דוגמאות חיות', ready: true,
          keywords: 'תגית tag h1 p a img ul li table tr td form input label select textarea div span class id' },
        { num: 'CSS', slug: 'web-css', section: 'web', title: 'יסודות CSS', desc: 'צבעים, רווחים (Box Model), Flexbox, hover, התאמה לטלפון ו-Bootstrap', ready: true,
          keywords: 'עיצוב color background margin padding border flex flexbox hover media query responsive selector סלקטור rem px' },
        { num: 'JS', slug: 'web-js', section: 'web', title: 'יסודות JavaScript', desc: 'לחיצות, הקלדה, הצגה והסתרה, רשימות ובדיקת טופס, עם דוגמאות חיות', ready: true,
          keywords: 'getElementById querySelector addEventListener click textContent classList toggle hidden let const forEach alert confirm' },

        { num: '🎨', slug: 'web-design', section: 'web', title: 'עיצוב שנראה מקצועי', desc: 'גופנים בעברית, אייקונים, סרטונים ומפות, וכללי עיצוב', ready: true,
          keywords: 'Google Fonts גופן Rubik Heebo אייקונים Bootstrap Icons YouTube מפה iframe embed צבעים פלטה ניגודיות favicon אייקון לשונית כרטיסייה' },
        { num: 'CSS 2', slug: 'web-css2', section: 'web', title: "CSS חלק ב'", desc: 'משתני צבע, position, Grid ואנימציות', ready: true,
          keywords: 'var משתנים root position sticky fixed absolute relative grid keyframes animation אנימציה' },
        { num: 'JS 2', slug: 'web-js2', section: 'web', title: "JavaScript חלק ב'", desc: 'פונקציות, אובייקטים, טיימרים, משחקים קטנים ו-localStorage', ready: true,
          keywords: 'function return object template literal setTimeout setInterval Math.random random data- dataset localStorage שעון משחק' },
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

        { num: '9ב', slug: '09b-bootstrap-components', section: 'pages', title: "Bootstrap חלק ב': רכיבים שזזים", desc: 'קרוסלה, חלון קופץ, שאלות נפתחות, לשוניות, תפריט צד והודעות', ready: true,
          keywords: 'carousel קרוסלה שקופיות באנר modal חלון קופץ accordion שאלות נפוצות tabs לשוניות offcanvas עגלה toast tooltip badge spinner progress floating data-bs-toggle' },
        { num: '10', slug: '10-models', section: 'data', title: 'מודלים', desc: 'מחלקה שמייצגת נתונים, והעברת מידע ל-View', ready: true,
          keywords: 'Model מחלקה class property @model' },
        { num: '11', slug: '11-forms', section: 'data', title: 'טפסים', desc: 'ממלאים טופס והמידע מגיע לשרת', ready: true,
          keywords: 'form POST GET HttpPost asp-for ValidateAntiForgeryToken' },
        { num: '12', slug: '12-validation', section: 'data', title: 'בדיקת קלט', desc: '"שדה חובה", "אימייל לא תקין" ועוד', ready: true,
          keywords: 'Validation Required ModelState ErrorMessage' },
        { num: '13', slug: '13-database', section: 'data', title: 'מסד נתונים', desc: 'טבלה משלכם, DbContext ו-Migrations', ready: true,
          keywords: 'DbContext DbSet Migration Add-Migration Update-Database LocalDB טבלה' },
        { num: '14', slug: '14-relationships', section: 'data', title: 'קשרים בין טבלאות', desc: 'קטגוריה עם הרבה מוצרים, משתמש עם הרבה הזמנות', ready: true,
          keywords: 'Foreign Key מפתח זר Include אחד לרבים' },
        { num: '15', slug: '15-scaffolding', section: 'data', title: 'הכול בלחיצת כפתור', desc: 'עמודי הצגה, הוספה, עריכה ומחיקה שנוצרים לבד', ready: true,
          keywords: 'Scaffolding CRUD async await Entity Framework' },

        { num: '16', slug: '16-images', section: 'users', title: 'העלאת תמונות', desc: 'טופס להעלאת קובץ, שמירה והצגה', ready: true,
          keywords: 'IFormFile upload קובץ תמונה wwwroot' },
        { num: '17', slug: '17-users', section: 'users', title: 'עבודה עם משתמשים', desc: 'עמודים למחוברים בלבד, המשתמש המחובר ותפקידים', ready: true,
          keywords: 'Authorize Roles מנהל Admin User.Identity Login' },

        { num: 'א', slug: 'adv-a-partial-views', section: 'advanced', title: 'Partial Views', desc: 'חלקי עמוד שחוזרים על עצמם', ready: true },
        { num: 'ב', slug: 'adv-b-search', section: 'advanced', title: 'חיפוש וסינון', desc: 'הצגת חלק מהנתונים עם LINQ', ready: true, keywords: 'LINQ Where OrderBy' },
        { num: 'ג', slug: 'adv-c-identity', section: 'advanced', title: 'התאמת ההרשמה', desc: 'שדות נוספים למשתמש ודפי הרשמה בעברית', ready: true, keywords: 'Identity ApplicationUser Scaffold' },
        { num: 'ד', slug: 'adv-d-fetch', section: 'advanced', title: 'JS שמדבר עם השרת', desc: 'עדכון חלק מהעמוד בלי לטעון מחדש', ready: true, keywords: 'fetch JSON AJAX' },
        { num: 'ה', slug: 'adv-e-cart', section: 'advanced', title: 'עגלת קניות', desc: 'הוספה לעגלה, עמוד עגלה ומחיקה', ready: true, keywords: 'Session חנות' },

        { num: '🗺️', slug: 'tool-project-map', section: 'tools', title: 'מפת הפרויקט', desc: 'כל תיקייה וקובץ: מה יש בו, מתי נוגעים בו, ואם מותר למחוק', ready: true,
          keywords: 'Solution Explorer תיקייה קובץ wwwroot Controllers Models Views Data Migrations _ViewImports _ViewStart _Layout launchSettings appsettings Program.cs bin obj Dependencies Areas' },
        { num: '🛠️', slug: 'tool-errors', section: 'tools', title: 'קריאת שגיאות ושגיאות נפוצות', desc: 'איך מבינים מה השתבש, ואיך מתקנים', ready: true, keywords: 'Error שגיאה Exception Clean Rebuild' },
        { num: '🛠️', slug: 'tool-debug', section: 'tools', title: 'דיבאג עם Breakpoints', desc: 'עוצרים את הקוד ובודקים ערכים', ready: true, keywords: 'Breakpoint F10 F11 Watch' },
        { num: '🛠️', slug: 'tool-planning', section: 'tools', title: 'תכנון הפרויקט', desc: 'תבנית למילוי לפני שמתחילים לכתוב קוד', ready: true },
        { num: '📚', slug: 'snippets', section: 'tools', title: 'ספריית קטעי קוד', desc: 'קטעים מוכנים להעתקה, עם הסבר מה לשנות', ready: true }
    ];

    var script = document.currentScript;
    var root = new URL('..', script.src).href; // תיקיית הבסיס של האתר
    var current = document.body.getAttribute('data-guide');
    var main = document.querySelector('main');

    function guideUrl(g) { return root + 'guides/' + g.slug + '.html'; }

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

    // ---------- מצב כהה / בהיר ----------
    var THEME_KEY = 'aspnet-guides-theme';
    function currentTheme() { return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'light'; }
    function setTheme(t) {
        document.documentElement.setAttribute('data-theme', t);
        try { localStorage.setItem(THEME_KEY, t); } catch (e) { }
        var btn = document.querySelector('.theme-btn');
        if (btn) {
            btn.textContent = t === 'dark' ? '☀️' : '🌙';
            btn.title = t === 'dark' ? 'מעבר למצב בהיר' : 'מעבר למצב כהה';
        }
    }

    // ---------- רשימת המדריכים (לתפריט ולסרגל הצד), בנויה כמו Solution Explorer ----------
    var currentGuide = GUIDES.filter(function (g) { return g.slug === current; })[0];
    var FOLDERS_KEY = 'aspnet-guides-folders';
    var folderState = {};
    try { folderState = JSON.parse(localStorage.getItem(FOLDERS_KEY)) || {}; } catch (e) { }
    function buildMenu(forSidebar) {
        return SECTIONS.map(function (s) {
            var list = GUIDES.filter(function (g) { return g.section === s.id; });
            var items = list.map(function (g) {
                var label = '<span class="m-num">' + g.num + '</span><span>' + g.title + '</span>';
                if (!g.ready) return '<li><span class="soon">' + label + ' <small>(בקרוב)</small></span></li>';
                var cls = g.slug === current ? ' class="current"' : '';
                return '<li' + cls + '><a href="' + guideUrl(g) + '"' + (g.slug === current ? ' aria-current="page"' : '') + '>' + label +
                    (visited[g.slug] ? '<span class="tick" title="כבר פתחתם">✓</span>' : '') + '</a></li>';
            }).join('');
            var open = !forSidebar || (s.id in folderState ? folderState[s.id] : (currentGuide ? currentGuide.section === s.id : true));
            return '<div class="nav-section"><details data-sec="' + s.id + '"' + (open ? ' open' : '') + '>' +
                '<summary><span>' + s.title + '</span><span class="count">' + list.length + '</span></summary>' +
                '<ul>' + items + '</ul></details></div>';
        }).join('');
    }
    var menuHtml = buildMenu(false);

    // ---------- כותרת עליונה ----------
    var header = el('header', { 'class': 'site-header' },
        '<div class="inner">' +
        '<a class="brand" href="' + root + 'index.html"><span class="brand-mark" aria-hidden="true">MVC</span><span class="brand-text">מדריכי ASP.NET Core MVC</span></a>' +
        '<nav>' +
        (GUIDES.some(function (g) { return g.slug === 'snippets' && g.ready; })
            ? '<a class="nav-link-snippets" href="' + root + 'guides/snippets.html">ספריית קטעי קוד</a>' : '') +
        '<button type="button" class="header-btn menu-btn" aria-expanded="false">כל המדריכים ▾</button>' +
        '<button type="button" class="header-btn theme-btn" aria-label="החלפת מצב כהה ובהיר"></button>' +
        '</nav>' +
        '</div>' +
        '<div class="guide-menu" hidden><div class="inner">' + menuHtml + '</div></div>');
    document.body.insertBefore(header, document.body.firstChild);
    setTheme(currentTheme());
    header.querySelector('.theme-btn').addEventListener('click', function () {
        setTheme(currentTheme() === 'dark' ? 'light' : 'dark');
    });

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
    // data-toc="deep" על ה-body: גם כותרות h3 שבתוך .snippet נכנסות לתוכן העניינים
    var tocList = null;
    if (current && main) {
        var deep = document.body.getAttribute('data-toc') === 'deep';
        var heads = main.querySelectorAll(deep ? ':scope > h2, .snippet > h3' : ':scope > h2');
        if (main.querySelectorAll(':scope > h2').length >= 3) {
            var toc = el('nav', { 'class': 'toc' + (deep ? ' deep' : '') }, '<strong>📑 בעמוד הזה</strong>');
            var list = el('ul'), sub = null;
            heads.forEach(function (h, i) {
                if (!h.id) h.id = 'part-' + (i + 1);
                var li = el('li');
                li.appendChild(el('a', { href: '#' + h.id }, h.textContent));
                if (h.tagName === 'H3' && sub) { sub.appendChild(li); return; }
                list.appendChild(li);
                if (deep) { sub = el('ul'); li.appendChild(sub); }
            });
            toc.appendChild(list);
            tocList = list;
            var anchor = main.querySelector('.subtitle');
            if (anchor) anchor.insertAdjacentElement('afterend', toc);
        }
    }

    // ---------- שביל ניווט מעל הכותרת ----------
    if (currentGuide && main) {
        var sec = SECTIONS.filter(function (x) { return x.id === currentGuide.section; })[0];
        var h1 = main.querySelector('h1');
        if (h1 && sec) {
            h1.insertAdjacentElement('beforebegin', el('nav', { 'class': 'crumbs', 'aria-label': 'מיקום באתר' },
                '<a href="' + root + 'index.html">ראשי</a><span class="sep">/</span>' +
                '<a href="' + root + 'index.html#sec-' + sec.id + '">' + sec.title + '</a>'));
        }
    }

    // ---------- פריסה למחשב: סרגל צד עם כל המדריכים, ותוכן עניינים צמוד ----------
    if (current && main) {
        document.body.classList.add('has-sidebar');
        var layout = el('div', { 'class': 'layout' + (tocList ? ' with-toc' : '') });
        var sidebar = el('aside', { 'class': 'sidebar', 'aria-label': 'כל המדריכים' },
            '<div class="sidebar-title">מפת הקורס</div>' + buildMenu(true));
        main.parentNode.insertBefore(layout, main);
        layout.appendChild(sidebar);
        layout.appendChild(main);
        sidebar.querySelectorAll('details').forEach(function (d) {
            d.addEventListener('toggle', function () {
                folderState[d.getAttribute('data-sec')] = d.open;
                try { localStorage.setItem(FOLDERS_KEY, JSON.stringify(folderState)); } catch (e) { }
            });
        });
        var cur = sidebar.querySelector('li.current');
        if (cur) setTimeout(function () { sidebar.scrollTop = cur.offsetTop - sidebar.clientHeight / 3; }, 0);

        if (tocList) {
            var side = el('aside', { 'class': 'toc-side', 'aria-label': 'בעמוד הזה' }, '<strong>בעמוד הזה</strong>');
            side.appendChild(tocList.cloneNode(true));
            layout.appendChild(side);
            var links = side.querySelectorAll('a');
            var targets = [].map.call(links, function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
            var onScroll = function () {
                var y = window.scrollY + 120, active = 0;
                targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top + window.scrollY <= y) active = i; });
                links.forEach(function (a, i) { a.classList.toggle('active', i === active); });
                var act = links[active];
                if (act && (act.offsetTop < side.scrollTop || act.offsetTop > side.scrollTop + side.clientHeight - 40)) {
                    side.scrollTop = act.offsetTop - side.clientHeight / 2;
                }
            };
            window.addEventListener('scroll', onScroll, { passive: true });
            onScroll();
        }
    }

    // ---------- טבלאות: עטיפה שגוללת הצידה, ובטלפון שורות שהופכות לכרטיסים ----------
    document.querySelectorAll('main table.simple').forEach(function (t) {
        var wrap = el('div', { 'class': 'table-wrap' });
        t.parentNode.insertBefore(wrap, t);
        wrap.appendChild(t);
        if (t.classList.contains('fill')) return;
        var rows = t.querySelectorAll('tr');
        var head = rows[0];
        if (!head || head.querySelector('td')) return;
        var labels = [].map.call(head.children, function (c) { return c.textContent.trim(); });
        if (labels.length < 3) return;
        head.classList.add('head-row');
        t.classList.add('stack');
        [].slice.call(rows, 1).forEach(function (r) {
            [].forEach.call(r.children, function (c, i) { if (labels[i]) c.setAttribute('data-label', labels[i]); });
        });
    });

    // ---------- צביעת קוד (Prism, שמור בתיקייה assets/vendor) ----------
    function detectLanguage(text) {
        var t = text.trim();
        if (/^(Add-Migration|Update-Database|Remove-Migration|Install-Package)\b/m.test(t)) return 'powershell';
        var htmlTag = /(^|[^\w])<\/?[a-z!][\w-]*(\s|>|\/)/m.test(t);
        if (/^\s*@[\w{*]/m.test(t) || htmlTag || /&copy;/.test(t)) return 'cshtml';
        if (/\bdocument\.|\bfunction\s*\(|\baddEventListener\b|\bconst\s|\blet\s|=>\s*\{?\s*$|\bfetch\(/m.test(t) && !/\bpublic\b|\bvar\s+\w+\s*=\s*new\b/.test(t)) return 'javascript';
        if (/^[\w\s.#:>,-]+\{\s*$/m.test(t) && /^\s*[\w-]+\s*:\s*[^;]+;\s*$/m.test(t) && !/\b(public|return|var)\b/.test(t)) return 'css';
        return 'csharp';
    }

    function wrapChanges(root, words) {
        if (!words.length) return;
        var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
        var nodes = [];
        while (walker.nextNode()) nodes.push(walker.currentNode);
        nodes.forEach(function (node) {
            words.forEach(function (w) {
                var i = node.nodeValue.indexOf(w);
                if (i === -1 || !node.parentNode) return;
                var after = node.splitText(i);
                after.splitText(w.length);
                var span = document.createElement('span');
                span.className = 'change';
                after.parentNode.replaceChild(span, after);
                span.appendChild(after);
            });
        });
    }

    // Prism נטען פעם אחת, רק בעמודים שיש בהם קוד
    var prismWaiting = null;
    function withPrism(cb) {
        if (window.Prism && window.Prism.highlightElement) { cb(); return; }
        if (prismWaiting) { prismWaiting.push(cb); return; }
        prismWaiting = [cb];
        document.head.appendChild(el('link', { rel: 'stylesheet', href: root + 'assets/vendor/prism-vsc-dark-plus.css' }));
        window.Prism = window.Prism || {};
        window.Prism.manual = true;
        var ps = el('script', { src: root + 'assets/vendor/prism.js' });
        ps.onload = function () { prismWaiting.forEach(function (f) { f(); }); };
        document.head.appendChild(ps);
    }

    var blocks = document.querySelectorAll('pre.code-block');
    if (blocks.length) {
        withPrism(function () {
            blocks.forEach(function (pre) {
                var words = [];
                pre.querySelectorAll('.change').forEach(function (s) {
                    if (words.indexOf(s.textContent) === -1) words.push(s.textContent);
                });
                var text = pre.textContent;
                var lang = pre.getAttribute('data-lang') || detectLanguage(text);
                var code = document.createElement('code');
                code.className = 'language-' + lang;
                code.textContent = text;
                pre.textContent = '';
                pre.appendChild(code);
                window.Prism.highlightElement(code);
                wrapChanges(code, words);
            });
        });
    }

    // ---------- נסו בעצמכם: עורך חי עם תוצאה ----------
    // <div class="playground" data-title="..." data-height="220" data-bootstrap>
    //   <textarea data-lang="html">...</textarea> <textarea data-lang="css">...</textarea> <textarea data-lang="js">...</textarea>
    // </div>
    var pgCount = 0;
    // סידור העורך והתוצאה: זה ליד זה או אחד מעל השני. הבחירה נשמרת ומשפיעה על כל העורכים באתר
    var PG_LAYOUT_KEY = 'aspnet-guides-pg-layout';
    var pgLayout = 'side';
    try { pgLayout = localStorage.getItem(PG_LAYOUT_KEY) === 'stack' ? 'stack' : 'side'; } catch (e) { }
    function setPgLayout(mode) {
        pgLayout = mode;
        try { localStorage.setItem(PG_LAYOUT_KEY, mode); } catch (e) { }
        document.querySelectorAll('.playground').forEach(function (x) {
            x.classList.toggle('pg-side', mode === 'side');
            x.classList.toggle('pg-stack', mode === 'stack');
            x.querySelectorAll('[data-layout]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-layout') === mode); });
        });
    }
    var BOOTSTRAP_CSS = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css';
    var BOOTSTRAP_JS = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js';
    document.querySelectorAll('.playground').forEach(function (pg) {
        var id = 'pg' + (++pgCount);
        var langs = ['html', 'css', 'js'];
        var names = { html: 'HTML', css: 'CSS', js: 'JavaScript' };
        var original = {}, current = {};
        langs.forEach(function (l) {
            var t = pg.querySelector('textarea[data-lang="' + l + '"]');
            if (t) { original[l] = t.value.replace(/^\n/, ''); current[l] = original[l]; }
        });
        var present = langs.filter(function (l) { return l in original; });
        var active = present[0];

        // המשימה: שורה מעל העורך, כי זו הוראה לתלמיד ולא חלק מהחלון
        var task = el('p', { 'class': 'pg-task' }, '<span aria-hidden="true">✏️</span> ' + (pg.getAttribute('data-title') || 'נסו בעצמכם: שנו את הקוד וראו מה קורה'));
        pg.parentNode.insertBefore(task, pg);

        // שורת הלשוניות: כמו קבצים פתוחים ב-Visual Studio
        var FILES = { html: 'index.html', css: 'style.css', js: 'script.js' };
        var bar = el('div', { 'class': 'pg-bar' },
            '<span class="pg-tabs" role="tablist">' + present.map(function (l) {
                return '<button type="button" role="tab" data-tab="' + l + '" aria-selected="' + (l === active) + '" title="' + names[l] + '"' +
                    (l === active ? ' class="active"' : '') + '><span class="pg-file pg-file-' + l + '" aria-hidden="true"></span>' + FILES[l] + '</button>';
            }).join('') + '</span>' +
            '<span class="pg-actions">' +
            '<span class="pg-layout" role="group" aria-label="סידור">' +
            '<button type="button" data-layout="side" title="זה ליד זה" aria-label="זה ליד זה"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="11" rx="1.5"/><path d="M8 2.5v11"/></svg></button>' +
            '<button type="button" data-layout="stack" title="אחד מעל השני" aria-label="אחד מעל השני"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="1.5" y="2.5" width="13" height="11" rx="1.5"/><path d="M1.5 8h13"/></svg></button>' +
            '</span>' +
            '<button type="button" class="pg-reset" data-act="reset" title="החזרת הקוד המקורי">↺ איפוס</button></span>');
        var editor = el('textarea', { 'class': 'pg-editor', spellcheck: 'false', autocapitalize: 'off', autocomplete: 'off', 'aria-label': 'עורך קוד' });
        editor.value = current[active];
        // שכבת צבעים מתחת לתיבת הטקסט: מקלידים בתיבה (שהטקסט שלה שקוף) ורואים את הקוד הצבוע מתחתיה
        var PRISM_LANG = { html: 'markup', css: 'css', js: 'javascript' };
        var hlCode = el('code');
        var hl = el('pre', { 'class': 'pg-hl', 'aria-hidden': 'true' });
        hl.appendChild(hlCode);
        var codeBox = el('div', { 'class': 'pg-code' });
        codeBox.appendChild(hl);
        codeBox.appendChild(editor);
        function paintCode() {
            var text = editor.value;
            if (text.slice(-1) === '\n') text += ' ';
            var P = window.Prism, lang = PRISM_LANG[active];
            if (P && P.highlight && P.languages && P.languages[lang]) {
                hlCode.innerHTML = P.highlight(text, P.languages[lang], lang);
            } else {
                hlCode.textContent = text;
            }
            hl.scrollTop = editor.scrollTop;
            hl.scrollLeft = editor.scrollLeft;
        }
        editor.addEventListener('scroll', function () { hl.scrollTop = editor.scrollTop; hl.scrollLeft = editor.scrollLeft; });
        paintCode();
        withPrism(paintCode);
        var frame = el('iframe', { 'class': 'pg-frame', sandbox: 'allow-scripts allow-modals allow-forms', title: 'תוצאה' });
        frame.style.height = (pg.getAttribute('data-height') || 220) + 'px';
        // העורך גבוה מספיק כדי להראות את כל הקוד (עד גבול), גם כשהתוצאה קטנה
        var maxLines = Math.max.apply(null, present.map(function (l) { return original[l].split('\n').length; }));
        var fitHeight = Math.min(Math.round(maxLines * 21.9 + 30), 460);
        editor.style.minHeight = Math.max(+(pg.getAttribute('data-height') || 220), fitHeight, 140) + 'px';
        // התוצאה: בתוך "חלון דפדפן"
        var result = el('div', { 'class': 'pg-result' },
            '<div class="pg-chrome" aria-hidden="true"><span class="pg-dots"><i></i><i></i><i></i></span>' +
            '<span class="pg-url">localhost</span><span class="pg-live">מתעדכן תוך כדי הקלדה</span></div>');
        result.appendChild(frame);
        var editorPane = el('div', { 'class': 'pg-pane' });
        editorPane.appendChild(bar);
        editorPane.appendChild(codeBox);
        var body = el('div', { 'class': 'pg-body' });
        body.appendChild(editorPane);
        body.appendChild(result);
        pg.classList.add('pg-' + pgLayout);
        var err = el('div', { 'class': 'pg-error' });
        var con = el('div', { 'class': 'pg-console' });
        pg.appendChild(body); pg.appendChild(err); pg.appendChild(con);

        function render() {
            err.className = 'pg-error';
            con.innerHTML = '';
            con.className = 'pg-console';
            var js = (current.js || '').replace(/<\/script/gi, '<\\/script');
            frame.srcdoc = '<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8">' +
                (pg.hasAttribute('data-bootstrap') ? '<link rel="stylesheet" href="' + BOOTSTRAP_CSS + '">' : '') +
                '<style>body{font-family:system-ui,-apple-system,Arial,sans-serif;margin:0;padding:12px;line-height:1.5}</style>' +
                '<style>' + (current.css || '') + '</style></head><body>' + (current.html || '') +
                '<script>window.onerror=function(m){parent.postMessage({pg:"' + id + '",err:String(m)},"*");};' +
                '(function(){function f(v){try{return typeof v==="object"&&v!==null?JSON.stringify(v):String(v);}catch(e){return String(v);}}' +
                '["log","info","warn","error","table"].forEach(function(t){var o=console[t];console[t]=function(){var a=[].slice.call(arguments);' +
                'var d=null;if(t==="table"){try{d=JSON.parse(JSON.stringify(a[0]));}catch(e){}}' +
                'parent.postMessage({pg:"' + id + '",con:t,text:a.map(f).join(" "),data:d},"*");o&&o.apply(console,arguments);};});' +
                'console.clear=function(){parent.postMessage({pg:"' + id + '",con:"clear"},"*");};' +
                // טופס שעבר את הבדיקה של הדפדפן: לא שולחים באמת לשום מקום, רק מראים שהוא עבר
                'document.addEventListener("submit",function(e){if(e.defaultPrevented)return;e.preventDefault();' +
                'var n=document.createElement("div");n.textContent="✓ הטופס עבר את הבדיקה ונשלח (בדוגמה הוא לא נשלח באמת לשום מקום)";' +
                'n.style.cssText="position:fixed;top:8px;left:8px;right:8px;background:#eaf6f0;color:#16825d;border:1px solid #16825d;border-radius:6px;padding:8px 10px;font-size:14px;z-index:9999";' +
                'document.body.appendChild(n);setTimeout(function(){n.remove();},3000);});' +
                '})();<\/script>' +
                (pg.hasAttribute('data-bootstrap') ? '<script src="' + BOOTSTRAP_JS + '"><\/script>' : '') +
                (js ? '<script>' + js + '<\/script>' : '') + '</body></html>';
        }
        var timer;
        editor.addEventListener('input', function () {
            current[active] = editor.value;
            paintCode();
            clearTimeout(timer);
            timer = setTimeout(render, 350);
        });
        editor.addEventListener('keydown', function (e) {
            if (e.key === 'Tab') {
                e.preventDefault();
                var s = editor.selectionStart, en = editor.selectionEnd;
                editor.value = editor.value.slice(0, s) + '    ' + editor.value.slice(en);
                editor.selectionStart = editor.selectionEnd = s + 4;
                editor.dispatchEvent(new Event('input'));
            }
        });
        bar.addEventListener('click', function (e) {
            var b = e.target.closest('button');
            if (!b) return;
            if (b.getAttribute('data-layout')) {
                setPgLayout(b.getAttribute('data-layout'));
            } else if (b.getAttribute('data-tab')) {
                active = b.getAttribute('data-tab');
                editor.value = current[active];
                paintCode();
                bar.querySelectorAll('[data-tab]').forEach(function (x) {
                    x.classList.toggle('active', x === b);
                    x.setAttribute('aria-selected', x === b);
                });
            } else if (b.getAttribute('data-act') === 'reset') {
                present.forEach(function (l) { current[l] = original[l]; });
                editor.value = current[active];
                paintCode();
                render();
            }
        });
        window.addEventListener('message', function (e) {
            if (!e.data || e.data.pg !== id) return;
            if (e.data.err) {
                err.textContent = '⚠️ שגיאה ב-JavaScript: ' + e.data.err;
                err.className = 'pg-error show';
            } else if (e.data.con === 'clear') {
                con.innerHTML = '';
            } else if (e.data.con) {
                if (!con.childNodes.length) con.appendChild(el('div', { 'class': 'pg-console-title' }, 'Console (כמו F12 ← Console בדפדפן)'));
                var line = el('div', { 'class': 'pg-line pgl-' + e.data.con });
                var d = e.data.data;
                if (e.data.con === 'table' && d && typeof d === 'object') {
                    var rows = Array.isArray(d) ? d : Object.keys(d).map(function (k) { return d[k]; });
                    var keys = Array.isArray(d) ? d.map(function (_, i) { return i; }) : Object.keys(d);
                    var cols = [];
                    rows.forEach(function (r) {
                        if (r && typeof r === 'object') Object.keys(r).forEach(function (k) { if (cols.indexOf(k) === -1) cols.push(k); });
                    });
                    var t = el('table', { 'class': 'pg-ctable' });
                    var head = '<tr><th>(index)</th>' + (cols.length ? cols.map(function (k) { return '<th></th>'; }).join('') : '<th>Value</th>') + '</tr>';
                    t.innerHTML = head;
                    var ths = t.querySelectorAll('th');
                    cols.forEach(function (k, i) { ths[i + 1].textContent = k; });
                    rows.forEach(function (r, i) {
                        var tr = el('tr');
                        var cells = [keys[i]].concat(cols.length ? cols.map(function (k) { return r && typeof r === 'object' ? r[k] : ''; }) : [r]);
                        cells.forEach(function (v) { var td = el('td'); td.textContent = v === undefined ? '' : (typeof v === 'object' ? JSON.stringify(v) : v); tr.appendChild(td); });
                        t.appendChild(tr);
                    });
                    line.appendChild(t);
                } else {
                    line.textContent = (e.data.con === 'warn' ? '⚠ ' : e.data.con === 'error' ? '✖ ' : e.data.con === 'info' ? 'ℹ ' : '› ') + e.data.text;
                }
                con.appendChild(line);
                con.className = 'pg-console show';
                con.scrollTop = con.scrollHeight;
            }
        });
        render();
    });
    if (pgCount) setPgLayout(pgLayout);

    // ---------- תצוגה מקדימה לבלוק קוד: לשוניות "קוד" ו"תצוגה" ----------
    // <pre class="code-block" data-preview>...</pre>  תצוגה של הקוד עצמו
    // ואם בקוד יש C# (@foreach וכו'), אחריו: <template class="code-sample">HTML לדוגמה</template>
    function addPreview(wrap, pre, sampleTpl) {
        var id = 'pv' + (++pvCount);
        wrap.classList.add('has-preview');
        var head = el('div', { 'class': 'cv-head', role: 'tablist' },
            '<button type="button" role="tab" data-view="code" aria-selected="true" class="active">קוד</button>' +
            '<button type="button" role="tab" data-view="preview" aria-selected="false">תצוגה מקדימה</button>' +
            (sampleTpl ? '<span class="cv-note">עם נתונים לדוגמה</span>' : ''));
        wrap.insertBefore(head, pre);
        var box = null, frame = null;
        function build() {
            box = el('div', { 'class': 'cv-preview', hidden: '' },
                '<div class="cv-chrome" aria-hidden="true"><span class="pg-dots"><i></i><i></i><i></i></span><span class="cv-url">localhost</span></div>');
            frame = el('iframe', { 'class': 'cv-frame', sandbox: 'allow-scripts allow-modals', title: 'תצוגה מקדימה', loading: 'lazy' });
            var src = sampleTpl ? sampleTpl.innerHTML : pre.textContent;
            frame.srcdoc = '<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8">' +
                '<link rel="stylesheet" href="' + BOOTSTRAP_CSS + '">' +
                '<style>body{padding:16px;margin:0;min-height:60px}</style></head><body>' + src +
                '<script src="' + BOOTSTRAP_JS + '"><\/script>' +
                '<script>(function(){function h(){parent.postMessage({pv:"' + id + '",h:document.documentElement.scrollHeight},"*");}' +
                'window.addEventListener("load",h);if(window.ResizeObserver)new ResizeObserver(h).observe(document.body);setTimeout(h,300);})();' +
                'document.addEventListener("submit",function(e){e.preventDefault();});' +
                'document.addEventListener("click",function(e){var a=e.target.closest("a[href]");if(a&&!a.hasAttribute("data-bs-toggle")&&!a.hasAttribute("data-bs-slide"))e.preventDefault();});<\/script>' +
                '</body></html>';
            box.appendChild(frame);
            wrap.appendChild(box);
            window.addEventListener('message', function (e) {
                if (e.data && e.data.pv === id && e.data.h) frame.style.height = Math.min(Math.max(e.data.h, 120), 640) + 'px';
            });
        }
        head.addEventListener('click', function (e) {
            var b = e.target.closest('button[data-view]');
            if (!b) return;
            var showPreview = b.getAttribute('data-view') === 'preview';
            if (showPreview && !box) build();
            head.querySelectorAll('button').forEach(function (x) {
                x.classList.toggle('active', x === b);
                x.setAttribute('aria-selected', x === b);
            });
            pre.hidden = showPreview;
            wrap.classList.toggle('showing-preview', showPreview);
            if (box) box.hidden = !showPreview;
        });
    }

    // ---------- כפתור העתקה לכל בלוק קוד ----------
    var pvCount = 0;
    document.querySelectorAll('pre.code-block').forEach(function (pre) {
        var sampleTpl = pre.nextElementSibling && pre.nextElementSibling.matches('template.code-sample') ? pre.nextElementSibling : null;
        var wrap = el('div', { 'class': 'code-wrap' });
        pre.parentNode.insertBefore(wrap, pre);
        wrap.appendChild(pre);
        if (pre.hasAttribute('data-preview')) addPreview(wrap, pre, sampleTpl);
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
        (wrap.querySelector('.cv-head') || wrap).appendChild(btn);
    });

    // ---------- קישור לספריית קטעי הקוד בסוף כל מדריך ----------
    var snippetsGuide = GUIDES.filter(function (g) { return g.slug === 'snippets'; })[0];
    if (current && main && current !== 'snippets' && snippetsGuide && snippetsGuide.ready) {
        main.appendChild(el('p', { 'class': 'snippets-link' },
            '📚 צריכים קוד מוכן לפרויקט? בספריית קטעי הקוד יש קטעים להעתקה, עם הסבר מה לשנות. ' +
            '<a href="' + guideUrl(snippetsGuide) + '">לספריית קטעי הקוד</a>'));
    }

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

            // פס סטטוס בתחתית המסך (במחשב בלבד)
            var readyCount = ready.length;
            var seen = ready.filter(function (g) { return visited[g.slug]; }).length;
            var bar = el('footer', { 'class': 'statusbar', 'aria-label': 'התקדמות' },
                '<span class="sb-item" title="נשמר רק בדפדפן הזה">פתחתם ' + seen + ' מתוך ' + readyCount +
                '<span class="sb-bar"><span style="width:' + Math.round(100 * seen / readyCount) + '%"></span></span></span>' +
                '<span class="grow"></span>' +
                (i > 0 ? '<a href="' + guideUrl(ready[i - 1]) + '" title="' + ready[i - 1].title + '">→ הקודם</a>' : '') +
                '<span class="sb-item">מדריך ' + (i + 1) + ' מתוך ' + readyCount + '</span>' +
                (i < readyCount - 1 ? '<a href="' + guideUrl(ready[i + 1]) + '" title="' + ready[i + 1].title + '">הבא ←</a>' : ''));
            document.body.appendChild(bar);
        }
    }

    // ---------- הגעה לסעיף מקישור: גוללים אליו ומסמנים אותו לרגע, כדי שהעין תמצא איפה להתחיל ----------
    function flashTarget(scroll) {
        var id = decodeURIComponent(location.hash.slice(1));
        var t = id && document.getElementById(id);
        if (!t) return;
        if (scroll) t.scrollIntoView({ block: 'start' });
        t.classList.remove('flash');
        void t.offsetWidth;
        t.classList.add('flash');
    }
    if (location.hash) requestAnimationFrame(function () { flashTarget(true); });
    window.addEventListener('hashchange', function () { flashTarget(false); });

    // ---------- כפתור "חזרה למעלה" ----------
    var topBtn = el('button', { 'class': 'to-top', 'type': 'button', 'aria-label': 'חזרה למעלה', 'title': 'חזרה למעלה' }, '↑');
    topBtn.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
    document.body.appendChild(topBtn);
    window.addEventListener('scroll', function () { topBtn.classList.toggle('show', window.scrollY > 600); }, { passive: true });

    // ---------- דף הבית: חיפוש ורשימת המדריכים ----------
    var index = document.getElementById('guide-index');
    if (index) {
        document.body.classList.add('home');
        var readyGuides = GUIDES.filter(function (g) { return g.ready; });
        var readCount = readyGuides.filter(function (g) { return visited[g.slug]; }).length;
        var statEl = document.getElementById('stat-guides');
        if (statEl) statEl.textContent = readyGuides.length;
        var tools = el('div', { 'class': 'home-tools' });
        var searchBox = el('div', { 'class': 'search-box' },
            '<input type="search" placeholder="חיפוש מדריך, למשל: טופס, Migration, תפריט" aria-label="חיפוש מדריך">');
        tools.appendChild(searchBox);
        tools.appendChild(el('div', { 'class': 'progress', title: 'נשמר רק בדפדפן הזה' },
            'פתחתם ' + readCount + ' מתוך ' + readyGuides.length +
            '<span class="progress-bar"><span style="width:' + Math.round(100 * readCount / Math.max(1, readyGuides.length)) + '%"></span></span>'));
        index.parentNode.insertBefore(tools, index);
        var noResults = el('p', { 'class': 'no-results', hidden: '' }, 'לא נמצא מדריך מתאים. נסו מילה אחרת.');
        index.parentNode.insertBefore(noResults, index.nextSibling);

        SECTIONS.forEach(function (s) {
            var sec = el('section', { 'class': 'home-section' });
            var n = GUIDES.filter(function (g) { return g.section === s.id; }).length;
            sec.appendChild(el('h2', { id: 'sec-' + s.id }, s.title + ' <span class="count">' + n + '</span>'));
            if (s.note) sec.appendChild(el('p', { 'class': 'section-note' }, s.note));
            var ul = el('ul', { 'class': 'guide-cards' });
            GUIDES.filter(function (g) { return g.section === s.id; }).forEach(function (g) {
                var inner = '<span class="num">' + g.num + '</span>' +
                    '<span class="title">' + g.title + (g.ready ? '' : ' <span class="badge">(בקרוב)</span>') + '</span>' +
                    (visited[g.slug] && g.ready ? '<span class="tick" title="כבר פתחתם את המדריך הזה">✓ נקרא</span>' : '') +
                    '<span class="desc">' + g.desc + '</span>';
                var li = el('li', { 'class': 'guide-card ' + (g.ready ? 'ready' : 'soon') });
                li.setAttribute('data-search', (g.num + ' ' + g.title + ' ' + g.desc + ' ' + (g.keywords || '')).toLowerCase());
                li.innerHTML = g.ready ? '<a href="' + guideUrl(g) + '">' + inner + '</a>' : '<div class="row">' + inner + '</div>';
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


    // ---------- דף הבית: חלון עורך שמקליד קוד פעם אחת ----------
    var heroCode = document.getElementById('hero-code');
    if (heroCode) {
        var T = [
            ['kw', 'public class '], ['ty', 'HomeController'], ['', ' : '], ['ty', 'Controller'], ['', '\n{\n    '],
            ['cm', '// כתובת: /Home/Index'], ['', '\n    '],
            ['kw', 'public '], ['ty', 'IActionResult '], ['fn', 'Index'], ['', '()\n    {\n        '],
            ['', 'ViewData['], ['st', '"Title"'], ['', '] = '], ['st', '"Home"'], ['', ';\n        '],
            ['ctl', 'return '], ['fn', 'View'], ['', '();\n    }\n}']
        ];
        var total = T.reduce(function (n, t) { return n + t[1].length; }, 0);
        var esc = function (x) { return x.replace(/&/g, '&amp;').replace(/</g, '&lt;'); };
        var paint = function (count, done) {
            var html = '', left = count, line = 1;
            var ln = function () { return '<span class="ln">' + line + '</span>'; };
            html += ln();
            for (var k = 0; k < T.length && left > 0; k++) {
                var part = T[k][1].slice(0, left);
                left -= part.length;
                var pieces = part.split('\n');
                pieces.forEach(function (pc, pi) {
                    if (pi > 0) { line++; html += '\n' + ln(); }
                    if (pc) html += T[k][0] ? '<span class="' + T[k][0] + '">' + esc(pc) + '</span>' : esc(pc);
                });
            }
            heroCode.innerHTML = html + (done ? '' : '<span class="caret"></span>');
        };
        var statusEl = document.getElementById('hero-status');
        var finish = function () {
            paint(total, true);
            if (statusEl) statusEl.textContent = '✓ Build succeeded';
        };
        var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (still) finish();
        else {
            var shown = 0;
            paint(0);
            setTimeout(function step() {
                shown += 2;
                if (shown >= total) { finish(); return; }
                paint(shown);
                setTimeout(step, 28);
            }, 500);
        }
    }

    document.body.appendChild(el('footer', { 'class': 'site-footer' }, 'מדריכים לתלמידים ללימוד ASP.NET Core MVC.<br>' +
        'הקוד ברישיון <a href="https://github.com/gilyerm/aspnet-guides/blob/main/LICENSE">MIT</a>, ' +
        'והתוכן ברישיון <a href="https://github.com/gilyerm/aspnet-guides/blob/main/LICENSE-CONTENT.md">CC BY 4.0</a>.'));
})();
