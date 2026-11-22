# "Bootstrap part 2": interactive components. Run through build_web.py (it provides pg, concept, table, c, page, code, box).

IMG = 'https://placehold.co/800x320/{bg}/ffffff?text={text}'

page('09b-bootstrap-components', "Bootstrap חלק ב': רכיבים שזזים",
     'קרוסלה, חלון קופץ, שאלות נפתחות, לשוניות, תפריט צד והודעות, בלי לכתוב JavaScript',
     '<strong>💡 על מה העמוד הזה?</strong> ב<a href="09-bootstrap.html">מדריך 9</a> ראינו רכיבים שרק נראים טוב: כפתורים, כרטיסים, טבלאות. כאן נכיר רכיבים ש<strong>עושים</strong> משהו: נפתחים, מתחלפים וקופצים. ל-Bootstrap יש קובץ JavaScript משלו שמפעיל אותם, ולכן לרובם מספיק HTML עם כמה תכונות מיוחדות.',
     [
         ('1. איך זה עובד: תכונות data-bs', [
             concept('data-bs-...', 'תכונות שכותבים בתוך תגית HTML, ו"מדברות" עם ה-JavaScript של Bootstrap. ' + c('data-bs-toggle') + ' אומר <strong>מה</strong> לעשות (לפתוח חלון, להחליף לשונית), ו-' + c('data-bs-target') + ' אומר <strong>על מי</strong>, לפי ה-' + c('id') + ' שלו עם ' + c('#') + ' לפניו.',
                     'דוגמה: ' + c('<button data-bs-toggle="modal" data-bs-target="#myModal">') + ' פירושו "כשלוחצים, פתח את החלון שה-id שלו myModal".'),
             '<p>בפרויקט שלכם זה כבר עובד, בלי להתקין כלום: בסוף ' + c('Views/Shared/_Layout.cshtml') + ' יש שורה שטוענת את ה-JavaScript של Bootstrap. בדקו שהיא שם:</p>',
             code('<script src="~/lib/bootstrap/dist/js/bootstrap.bundle.min.js"></script>', 'cshtml'),
             '<div class="warning"><strong>⚠️ חשוב: כל id פעם אחת בעמוד.</strong> אם יש שני רכיבים עם אותו ' + c('id') + ', הכפתור יפתח את הלא נכון (או אף אחד). זה קורה בעיקר בתוך ' + c('@foreach') + ', ולכן שם מוסיפים ל-id את המספר של הפריט, למשל ' + c('id="delete-@product.Id"') + ' (סעיף 3).</div>',
         ]),
         ('2. קרוסלה (Carousel): שקופיות מתחלפות', [
             '<p>מתאים לבאנר בדף הבית, או לכמה תמונות של אותו מוצר.</p>',
             pg('''
<div id="mainCarousel" class="carousel slide" data-bs-ride="carousel">
    <!-- הנקודות למטה -->
    <div class="carousel-indicators">
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="0" class="active"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="1"></button>
        <button type="button" data-bs-target="#mainCarousel" data-bs-slide-to="2"></button>
    </div>

    <!-- השקופיות -->
    <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="3000">
            <img src="''' + IMG.format(bg='5c2d91', text='Sale') + '''" class="d-block w-100" alt="מבצע">
            <div class="carousel-caption">
                <h5>מבצע סוף שנה</h5>
                <p>20% הנחה על הכול</p>
            </div>
        </div>
        <div class="carousel-item" data-bs-interval="3000">
            <img src="''' + IMG.format(bg='0d6efd', text='New') + '''" class="d-block w-100" alt="חדש">
            <div class="carousel-caption">
                <h5>הגיעו מוצרים חדשים</h5>
            </div>
        </div>
        <div class="carousel-item" data-bs-interval="3000">
            <img src="''' + IMG.format(bg='198754', text='Delivery') + '''" class="d-block w-100" alt="משלוח">
            <div class="carousel-caption">
                <h5>משלוח חינם מעל 100 ₪</h5>
            </div>
        </div>
    </div>

    <!-- החצים -->
    <button class="carousel-control-prev" type="button" data-bs-target="#mainCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#mainCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
    </button>
</div>''', title='נסו: שנו את 3000 ל-1000 (שנייה אחת לשקופית). ואז הוסיפו שקופית רביעית', height=300, bootstrap=True),
             table(['חלק', 'מה הוא עושה'], [
                 [c('carousel slide'), 'העטיפה של הכול. ' + c('slide') + ' = אנימציה של החלקה (' + c('carousel-fade') + ' = היעלמות).'],
                 [c('data-bs-ride="carousel"'), 'מתחילה להתחלף לבד כשהעמוד נטען. בלי זה, רק החצים מחליפים.'],
                 [c('carousel-item active'), 'שקופית. ' + c('active') + ' = השקופית שמופיעה ראשונה. <strong>חייבת להיות בדיוק אחת כזו.</strong>'],
                 [c('data-bs-interval="3000"'), 'כמה זמן כל שקופית מוצגת, באלפיות שנייה (3000 = 3 שניות).'],
                 [c('carousel-caption'), 'טקסט מעל התמונה.'],
                 [c('carousel-indicators') + ', ' + c('carousel-control-prev/next'), 'הנקודות והחצים. אפשר למחוק אותם אם לא צריך.'],
             ]),
             '<h3>קרוסלה של מוצרים מהמסד</h3>',
             '<p>בפרויקט, השקופיות מגיעות מהמסד עם לולאה. הבעיה: רק לשקופית <strong>הראשונה</strong> צריך ' + c('active') + '. לכן משתמשים ב-' + c('for') + ' עם מונה ' + c('i') + ', ובודקים ' + c('i == 0') + ':</p>',
             code('''@model List<Product>

<div id="productsCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        @for (int i = 0; i < Model.Count; i++)
        {
            var product = Model[i];
            <div class="carousel-item @(i == 0 ? "active" : "")">
                <img src="@product.ImageUrl" class="d-block w-100" alt="@product.Name" />
                <div class="carousel-caption">
                    <h5>@product.Name</h5>
                    <p>@product.Price ₪</p>
                </div>
            </div>
        }
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#productsCarousel" data-bs-slide="prev">
        <span class="carousel-control-prev-icon"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#productsCarousel" data-bs-slide="next">
        <span class="carousel-control-next-icon"></span>
    </button>
</div>''', 'cshtml'),
             '<p class="change-note">' + c('@(i == 0 ? "active" : "")') + ' פירושו: "אם זו השקופית הראשונה, כתוב active, אחרת אל תכתוב כלום". ' + c('ImageUrl') + ' מגיע מ<a href="16-images.html">מדריך 16</a>. אם אין לכם תמונות, מחקו את שורת ה-' + c('<img>') + ' ותנו ל-' + c('carousel-item') + ' גובה וצבע רקע.</p>',
             '<div class="checkpoint">הקרוסלה מופיעה ומתחלפת? אם היא <strong>לא מופיעה בכלל</strong>, כנראה אף שקופית לא קיבלה ' + c('active') + ', או שהרשימה ריקה (אין מוצרים במסד).</div>',
         ]),
         ('3. חלון קופץ (Modal)', [
             '<p>חלון שמופיע מעל העמוד, והרקע מאחוריו מתכהה. מתאים לפרטים נוספים, לטופס קצר, ובעיקר לשאלה "בטוחים?" לפני מחיקה.</p>',
             pg('''
<button type="button" class="btn btn-primary m-3" data-bs-toggle="modal" data-bs-target="#infoModal">
    פרטים על המשלוח
</button>

<div class="modal fade" id="infoModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">משלוחים</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                <p>משלוח עד הבית תוך 3 ימי עסקים. מעל 100 ₪ המשלוח חינם.</p>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">סגירה</button>
            </div>
        </div>
    </div>
</div>''', title='נסו: הוסיפו modal-dialog-centered ל-class של modal-dialog, כדי שהחלון יופיע באמצע המסך', height=300, bootstrap=True),
             table(['חלק', 'מה הוא עושה'], [
                 [c('data-bs-toggle="modal" data-bs-target="#infoModal"'), 'על הכפתור: פותח את החלון שה-id שלו infoModal.'],
                 [c('modal fade') + ' + ' + c('id'), 'החלון עצמו (מוסתר עד שפותחים אותו). ' + c('fade') + ' = מופיע בהדרגה.'],
                 [c('modal-header / modal-body / modal-footer'), 'כותרת, תוכן וכפתורים בתחתית.'],
                 [c('data-bs-dismiss="modal"'), 'על כפתור: סוגר את החלון.'],
             ]),
             '<h3>בפרויקט: "בטוחים שרוצים למחוק?"</h3>',
             '<p>חלון אחד לכל מוצר, בתוך ה-' + c('@foreach') + '. בגלל זה ה-id כולל את ' + c('@product.Id') + ': כך לכל מוצר יש חלון משלו, והכפתור פותח את הנכון.</p>',
             code('''@foreach (var product in Model)
{
    <tr>
        <td>@product.Name</td>
        <td>
            <button type="button" class="btn btn-sm btn-danger"
                    data-bs-toggle="modal" data-bs-target="#delete-@product.Id">
                מחיקה
            </button>

            <div class="modal fade" id="delete-@product.Id" tabindex="-1">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">מחיקת מוצר</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                        </div>
                        <div class="modal-body">
                            בטוחים שרוצים למחוק את <strong>@product.Name</strong>? אי אפשר לבטל את זה.
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">ביטול</button>
                            <form asp-action="Delete" asp-route-id="@product.Id" method="post">
                                <button type="submit" class="btn btn-danger">כן, למחוק</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </td>
    </tr>
}''', 'cshtml'),
             '<p class="change-note">הטופס שבתוך החלון שולח ל-Action בשם ' + c('Delete') + ' עם POST. ה-Action הזה צריך להיות קיים ב-Controller (בספריית קטעי הקוד: <a href="snippets.html">"הוספה, עריכה ומחיקה"</a>).</p>',
         ]),
         ('4. שאלות נפתחות (Accordion)', [
             '<p>רשימה של כותרות, וכל אחת נפתחת כשלוחצים עליה. מושלם לעמוד "שאלות נפוצות".</p>',
             pg('''
<div class="accordion" id="faq">
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#q1">
                כמה זמן לוקח משלוח?
            </button>
        </h2>
        <div id="q1" class="accordion-collapse collapse show" data-bs-parent="#faq">
            <div class="accordion-body">עד 3 ימי עסקים.</div>
        </div>
    </div>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#q2">
                אפשר להחזיר מוצר?
            </button>
        </h2>
        <div id="q2" class="accordion-collapse collapse" data-bs-parent="#faq">
            <div class="accordion-body">כן, תוך 14 יום מהקנייה.</div>
        </div>
    </div>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#q3">
                איך משלמים?
            </button>
        </h2>
        <div id="q3" class="accordion-collapse collapse" data-bs-parent="#faq">
            <div class="accordion-body">בכרטיס אשראי או ב-Bit.</div>
        </div>
    </div>
</div>''', title='נסו: מחקו את שלושת ה-data-bs-parent="#faq". עכשיו אפשר לפתוח כמה שאלות בבת אחת', height=300, bootstrap=True),
             table(['חלק', 'מה הוא עושה'], [
                 [c('data-bs-toggle="collapse" data-bs-target="#q1"'), 'על הכותרת: פותח וסוגר את התשובה שה-id שלה q1.'],
                 [c('collapse show'), 'התשובה. ' + c('show') + ' = פתוחה כבר בהתחלה.'],
                 [c('collapsed'), 'על הכפתור של שאלה סגורה (כדי שהחץ יצביע לכיוון הנכון).'],
                 [c('data-bs-parent="#faq"'), 'כשפותחים שאלה אחת, האחרות נסגרות.'],
             ]),
         ]),
         ('5. לשוניות (Tabs)', [
             '<p>כמה "עמודים" באותו מקום, ומחליפים ביניהם בלי לטעון את העמוד מחדש. למשל בעמוד מוצר: תיאור, מפרט וביקורות.</p>',
             pg('''
<ul class="nav nav-tabs" role="tablist">
    <li class="nav-item">
        <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#desc" type="button">תיאור</button>
    </li>
    <li class="nav-item">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#specs" type="button">מפרט</button>
    </li>
    <li class="nav-item">
        <button class="nav-link" data-bs-toggle="tab" data-bs-target="#reviews" type="button">ביקורות</button>
    </li>
</ul>

<div class="tab-content border border-top-0 p-3">
    <div class="tab-pane fade show active" id="desc">תיק גב עמיד למים, עם תא למחשב נייד.</div>
    <div class="tab-pane fade" id="specs">נפח: 25 ליטר. משקל: 700 גרם.</div>
    <div class="tab-pane fade" id="reviews">⭐⭐⭐⭐⭐ "התיק הכי נוח שהיה לי!"</div>
</div>''', title='נסו: החליפו nav-tabs ב-nav-pills', height=200, bootstrap=True),
             '<p>כמו בקרוסלה: הלשונית הראשונה וגם התוכן הראשון מקבלים ' + c('active') + ' (והתוכן גם ' + c('show') + ').</p>',
         ]),
         ('6. תפריט שנשלף מהצד (Offcanvas)', [
             '<p>חלונית שנכנסת מצד המסך. מתאים לעגלת קניות, לסינון מוצרים, או לתפריט בטלפון.</p>',
             pg('''
<button class="btn btn-success m-3" type="button" data-bs-toggle="offcanvas" data-bs-target="#cart">
    🛒 העגלה שלי
</button>

<div class="offcanvas offcanvas-end" tabindex="-1" id="cart">
    <div class="offcanvas-header">
        <h5 class="offcanvas-title">העגלה שלי</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas"></button>
    </div>
    <div class="offcanvas-body">
        <ul class="list-group mb-3">
            <li class="list-group-item d-flex justify-content-between">תיק גב <span>89 ₪</span></li>
            <li class="list-group-item d-flex justify-content-between">מחברת <span>12 ₪</span></li>
        </ul>
        <button class="btn btn-primary w-100">לתשלום</button>
    </div>
</div>''', title='נסו: החליפו offcanvas-end ב-offcanvas-start, ואחר כך ב-offcanvas-bottom', height=300, bootstrap=True),
             '<p>' + c('offcanvas-end') + ' = מהסוף של השורה. באתר בעברית (מימין לשמאל) הסוף הוא <strong>שמאל</strong>, ו-' + c('offcanvas-start') + ' נכנס מימין.</p>',
         ]),
         ('7. הודעה קופצת (Toast) והסבר צף (Tooltip)', [
             '<p>שני רכיבים ש-Bootstrap לא מפעיל לבד, ולכן צריך שורה או שתיים של JavaScript.</p>',
             '<h3>Toast: "המוצר נוסף לעגלה"</h3>',
             pg('''
<button id="addBtn" class="btn btn-primary m-3">הוספה לעגלה</button>

<div class="toast-container position-fixed bottom-0 start-0 p-3">
    <div id="cartToast" class="toast text-bg-success">
        <div class="toast-body d-flex justify-content-between">
            ✓ המוצר נוסף לעגלה
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast"></button>
        </div>
    </div>
</div>''', js='''
document.getElementById("addBtn").addEventListener("click", function () {
    var toast = bootstrap.Toast.getOrCreateInstance(document.getElementById("cartToast"));
    toast.show();
});''', title='נסו: לחצו על הכפתור. ואז שנו text-bg-success ל-text-bg-danger', height=200, bootstrap=True),
             '<p class="change-note">' + c('bootstrap.Toast.getOrCreateInstance(...)') + ' לוקח את ה-div של ההודעה, ו-' + c('.show()') + ' מציג אותה. אחרי 5 שניות היא נעלמת לבד.</p>',
             '<h3>Tooltip: הסבר קטן כשהעכבר מעל</h3>',
             pg('''
<div class="p-4">
    <button class="btn btn-outline-danger" data-bs-toggle="tooltip" data-bs-title="מחיקת המוצר">🗑️</button>
    <button class="btn btn-outline-primary" data-bs-toggle="tooltip" data-bs-title="עריכה">✏️</button>
    <button class="btn btn-outline-secondary" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="אני מופיע למטה">⬇️</button>
</div>''', js='''
// מפעיל את כל ה-tooltips בעמוד
document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (el) {
    new bootstrap.Tooltip(el);
});''', title='נסו: עברו עם העכבר על הכפתורים. ואז שנו את הטקסט ב-data-bs-title', height=160, bootstrap=True),
             '<p class="change-note">בפרויקט, את שלוש השורות של ה-JavaScript שמים פעם אחת ב-' + c('wwwroot/js/site.js') + ', וכל כפתור עם ' + c('data-bs-toggle="tooltip"') + ' באתר יקבל הסבר.</p>',
         ]),
         ('8. תוספות קטנות שעושות הרבה', [
             '<p>אלה לא זזים, אבל הם הופכים אתר לנראה מקצועי, וכולם עובדים עם CSS בלבד:</p>',
             pg('''
<div class="p-3">
    <!-- Badge: מספר קטן ליד כפתור -->
    <button class="btn btn-primary position-relative">
        🛒 עגלה
        <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">3</span>
    </button>
    <span class="badge text-bg-success ms-3">חדש!</span>

    <!-- Spinner: "טוען..." -->
    <div class="d-flex align-items-center gap-2 my-3">
        <div class="spinner-border spinner-border-sm text-primary"></div> טוען מוצרים...
    </div>

    <!-- Progress: פס התקדמות -->
    <div class="progress mb-3">
        <div class="progress-bar" style="width: 60%">60%</div>
    </div>

    <!-- Floating label: התווית "צפה" מעל השדה -->
    <div class="form-floating">
        <input type="email" class="form-control" id="mail" placeholder="name@example.com">
        <label for="mail">אימייל</label>
    </div>
</div>''', title='נסו: שנו את 60% ל-90%, ולחצו על שדה האימייל', height=280, bootstrap=True),
             table(['רכיב', 'class עיקרי', 'מתי'], [
                 ['Badge', c('badge text-bg-danger'), 'מספר על אייקון (פריטים בעגלה), תגית "חדש" או "מבצע".'],
                 ['Spinner', c('spinner-border'), 'כשמשהו נטען.'],
                 ['Progress', c('progress') + ' + ' + c('progress-bar'), 'כמה הושלם: שלבי הרשמה, ציון.'],
                 ['Floating label', c('form-floating'), 'טפסי הרשמה והתחברות. שימו לב: ה-' + c('<input>') + ' לפני ה-' + c('<label>') + ', וחייב ' + c('placeholder') + '.'],
             ]),
             '''<div class="troubleshoot">
        <h3>🔧 אם זה לא עובד</h3>
        <ul>
            <li><strong>לוחצים ולא קורה כלום:</strong> בדקו שה-''' + c('data-bs-target') + ''' מתחיל ב-''' + c('#') + ''', ושהשם אחרי ה-''' + c('#') + ''' זהה בדיוק ל-''' + c('id') + ''' (כולל אותיות גדולות וקטנות).</li>
            <li><strong>אף רכיב לא עובד באתר:</strong> בדקו שהשורה של ''' + c('bootstrap.bundle.min.js') + ''' קיימת בסוף ''' + c('_Layout.cshtml') + '''. בכלי המפתחים (F12 ← Console) תופיע שגיאה כמו ''' + c('bootstrap is not defined') + '''.</li>
            <li><strong>הקרוסלה לא מופיעה:</strong> אין אף ''' + c('carousel-item') + ''' עם ''' + c('active') + ''', או שיש יותר מאחד.</li>
            <li><strong>הכפתור בתוך הלולאה פותח את החלון של מוצר אחר:</strong> ה-''' + c('id') + ''' לא ייחודי. הוסיפו לו ''' + c('@product.Id') + ''' (סעיף 3).</li>
            <li><strong>Tooltip או Toast לא מופיעים:</strong> הם צריכים את שורות ה-JavaScript מסעיף 7. בלעדיהן, Bootstrap לא מפעיל אותם.</li>
        </ul>
    </div>''',
             '''<div class="exercise"><h3>✏️ תרגיל מסכם: עמוד מוצר</h3><ol>
        <li>בעמוד ''' + c('Details') + ''' של מוצר, הוסיפו קרוסלה עם 3 תמונות (אפשר מ-placehold.co).</li>
        <li>מתחתיה, לשוניות: "תיאור" (עם ''' + c('@Model.Description') + '''), "מפרט" ו"משלוחים".</li>
        <li>הוסיפו כפתור "הוספה לעגלה" שמציג Toast.</li>
        <li>בונוס: ב-''' + c('Index') + ''', החליפו את המחיקה ב-Modal של "בטוחים?" מסעיף 3.</li>
    </ol></div>''',
         ]),
     ],
     ['תכונות ' + c('data-bs-toggle') + ' ו-' + c('data-bs-target="#id"') + ' מפעילות רכיבים בלי לכתוב JavaScript.',
      'Carousel, Modal, Accordion, Tabs ו-Offcanvas: רק HTML. Toast ו-Tooltip: צריך שורת JavaScript.',
      'בקרוסלה ובלשוניות: בדיוק פריט אחד עם ' + c('active') + '. מהמסד: ' + c('@(i == 0 ? "active" : "")') + '.',
      'בתוך ' + c('@foreach') + ', כל id צריך להיות ייחודי: מוסיפים ' + c('@product.Id') + '.'],
     'כל הרכיבים, עם עוד אפשרויות: <a href="https://getbootstrap.com/docs/5.3/components/carousel/" target="_blank">getbootstrap.com</a>, תחת Components (באנגלית).')
