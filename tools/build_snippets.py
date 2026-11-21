"""Builds guides/snippets.html from the snippet list below (code is escaped automatically)."""
import html

G = lambda slug, label: f'<a href="{slug}.html">{label}</a>'


def code(src, lang=None):
    attr = f' data-lang="{lang}"' if lang else ''
    return f'<pre class="code-block"{attr}>{html.escape(src.strip(chr(10)))}</pre>'


def snippet(title, what, parts, change=None, guide=None, star=False):
    s = ['<div class="snippet">', f'<h3>{"<span class=star>⭐</span> " if star else ""}{title}</h3>', f'<p>{what}</p>']
    for where, src, *lang in parts:
        s.append(f'<p class="where">{where}</p>')
        s.append(code(src, lang[0] if lang else None))
    if change:
        s.append(f'<p class="change-note">{change}</p>')
    if guide:
        s.append(f'<p class="guide-link">הסבר מלא: {guide}</p>')
    s.append('</div>')
    return '\n'.join(s)


sections = []

# ======================= הצגת מידע =======================
sections.append(('הצגת מידע', [
    snippet('טבלה עם נתונים מהמסד',
            'מציג את כל השורות מטבלה במסד הנתונים, בטבלת Bootstrap.',
            [('ב-Controller, Action בשם Index', '''
public IActionResult Index()
{
    var products = _context.Products.ToList();
    return View(products);
}'''),
             ('ב-View: Views/Products/Index.cshtml', '''
@model List<Product>

<table class="table table-striped table-hover">
    <thead>
        <tr>
            <th>שם</th>
            <th>מחיר</th>
        </tr>
    </thead>
    <tbody>
        @foreach (var product in Model)
        {
            <tr>
                <td>@product.Name</td>
                <td>@product.Price ₪</td>
            </tr>
        }
    </tbody>
</table>''')],
            change='החליפו את <code class="inline">Products</code>/<code class="inline">Product</code> בשם הטבלה והמודל שלכם, ואת העמודות בשדות שלכם.',
            guide=G('13-database', 'מדריך 13') + ', ' + G('10-models', 'מדריך 10')),

    snippet('כרטיסים ברשת',
            'כל פריט ככרטיס עם תמונה: שלושה בשורה במחשב, אחד בשורה בטלפון.',
            [('ב-View (במקום טבלה)', '''
<div class="row">
    @foreach (var product in Model)
    {
        <div class="col-12 col-md-6 col-lg-4 mb-4">
            <div class="card h-100">
                <img src="@(product.ImageUrl ?? "https://placehold.co/400x300?text=No+Image")" class="card-img-top" alt="@product.Name" />
                <div class="card-body">
                    <h5 class="card-title">@product.Name</h5>
                    <p class="card-text">@product.Price ₪</p>
                    <a asp-action="Details" asp-route-id="@product.Id" class="btn btn-primary">לפרטים</a>
                </div>
            </div>
        </div>
    }
</div>''')],
            change='אם אין לכם <code class="inline">ImageUrl</code>, מחקו את שורת ה-<code class="inline">&lt;img&gt;</code>.',
            guide=G('09-bootstrap', 'מדריך 9') + ', ' + G('adv-a-partial-views', 'מתקדם א (אותו כרטיס בכמה עמודים)')),

    snippet('עמוד פרטים של פריט אחד',
            'עמוד שמציג פריט אחד לפי המספר שבכתובת, למשל /Products/Details/5.',
            [('ב-Controller', '''
public IActionResult Details(int id)
{
    var product = _context.Products.Find(id);
    if (product == null)
    {
        return NotFound();
    }
    return View(product);
}'''),
             ('ב-View: Details.cshtml', '''
@model Product
@{
    ViewData["Title"] = Model.Name;
}

<h1>@Model.Name</h1>
<p>@Model.Description</p>
<p><strong>מחיר:</strong> @Model.Price ₪</p>
<a asp-action="Index" class="btn btn-secondary">חזרה לרשימה</a>'''),
             ('הקישור לעמוד (למשל בטבלה)', '''
<a asp-action="Details" asp-route-id="@product.Id">פרטים</a>''')],
            guide=G('10-models', 'מדריך 10, סעיף 5')),

    snippet('"אין עדיין נתונים" כשהרשימה ריקה',
            'במקום טבלה ריקה, הודעה ידידותית.',
            [('ב-View, לפני הטבלה או הלולאה', '''
@if (Model.Count == 0)
{
    <div class="alert alert-info">אין עדיין מוצרים. 🙂</div>
}
else
{
    @* כאן הטבלה או הכרטיסים *@
}''')]),

    snippet('עיצוב תאריכים ומחירים',
            'תאריך בפורמט ישראלי, ומחיר עם שתי ספרות אחרי הנקודה.',
            [('ב-View', '''
<p>תאריך: @item.CreatedAt.ToString("dd/MM/yyyy")</p>
<p>תאריך ושעה: @item.CreatedAt.ToString("dd/MM/yyyy HH:mm")</p>
<p>מחיר: @product.Price.ToString("N2") ₪</p>''')],
            change='<code class="inline">N2</code> = עם פסיק לאלפים ושתי ספרות אחרי הנקודה (1,250.00). <code class="inline">N0</code> = בלי ספרות אחרי הנקודה.',
            star=True),

    snippet('חלוקה לעמודים',
            'כשיש הרבה פריטים: 9 בכל עמוד, וקישורים לעמוד 1, 2, 3...',
            [('ב-Controller', '''
public IActionResult Index(int page = 1)
{
    int pageSize = 9;
    int total = _context.Products.Count();

    var products = _context.Products
        .OrderBy(p => p.Id)
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToList();

    ViewBag.Page = page;
    ViewBag.TotalPages = (int)Math.Ceiling(total / (double)pageSize);
    return View(products);
}'''),
             ('ב-View, מתחת לרשימה', '''
<nav>
    <ul class="pagination">
        @for (int i = 1; i <= ViewBag.TotalPages; i++)
        {
            <li class="page-item @(i == ViewBag.Page ? "active" : "")">
                <a class="page-link" asp-action="Index" asp-route-page="@i">@i</a>
            </li>
        }
    </ul>
</nav>''')],
            change='<code class="inline">pageSize</code> קובע כמה פריטים בכל עמוד.'),

    snippet('ספירה: "נמצאו 12 מוצרים"',
            'מציג כמה פריטים יש ברשימה.',
            [('ב-View', '''
<p class="text-muted">נמצאו @Model.Count מוצרים</p>''')]),

    snippet('תמונת ברירת מחדל',
            'כשלפריט אין תמונה, מוצגת תמונה כללית.',
            [('ב-View', '''
<img src="@(product.ImageUrl ?? "https://placehold.co/400x300?text=No+Image")" alt="@product.Name" class="img-fluid" />''')],
            change='אפשר לשים תמונה משלכם ב-<code class="inline">wwwroot/images</code> ולכתוב <code class="inline">"/images/no-image.png"</code> במקום הכתובת.',
            guide=G('16-images', 'מדריך 16')),

    snippet('קיצור טקסט ארוך',
            'מציג רק את 100 התווים הראשונים של תיאור ארוך, עם "...".',
            [('ב-View', '''
@{
    var text = product.Description ?? "";
}
<p>@(text.Length > 100 ? text.Substring(0, 100) + "..." : text)</p>
<a asp-action="Details" asp-route-id="@product.Id">קרא עוד</a>''')]),
]))

# ======================= פעולות על נתונים =======================
sections.append(('פעולות על נתונים', [
    snippet('הוספה, עריכה ומחיקה',
            'הדרך המהירה: Scaffolding יוצר את כל העמודים בלחיצה. כאן העריכה והמחיקה, למי שכותב ביד.',
            [('ב-Controller: עריכה', '''
public IActionResult Edit(int id)
{
    var product = _context.Products.Find(id);
    if (product == null)
    {
        return NotFound();
    }
    return View(product);
}

[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Edit(Product product)
{
    if (!ModelState.IsValid)
    {
        return View(product);
    }
    _context.Products.Update(product);
    _context.SaveChanges();
    return RedirectToAction("Index");
}'''),
             ('ב-View: Edit.cshtml (כמו Create, עם שדה נסתר ל-Id)', '''
<form asp-action="Edit" method="post">
    <input type="hidden" asp-for="Id" />
    @* כאן אותם שדות כמו בטופס ההוספה *@
    <button type="submit" class="btn btn-success">שמירה</button>
</form>'''),
             ('ב-Controller: מחיקה', '''
[HttpPost]
[ValidateAntiForgeryToken]
public IActionResult Delete(int id)
{
    var product = _context.Products.Find(id);
    if (product != null)
    {
        _context.Products.Remove(product);
        _context.SaveChanges();
    }
    return RedirectToAction("Index");
}''')],
            change='בטופס העריכה חובה <code class="inline">&lt;input type="hidden" asp-for="Id" /&gt;</code>, אחרת האתר לא יודע איזו שורה לעדכן.',
            guide=G('15-scaffolding', 'מדריך 15 (הדרך האוטומטית)') + ', ' + G('11-forms', 'מדריך 11')),

    snippet('חלון אישור לפני מחיקה',
            'לפני מחיקה קופץ "בטוחים?", ורק אישור מוחק.',
            [('ב-View, כפתור מחיקה ליד כל פריט', '''
<form asp-action="Delete" asp-route-id="@product.Id" method="post"
      onsubmit="return confirm('בטוחים שרוצים למחוק?');">
    <button type="submit" class="btn btn-sm btn-danger">מחיקה</button>
</form>''')]),

    snippet('הודעת "נשמר בהצלחה"',
            'אחרי שמירה ומעבר לעמוד אחר, מופיעה הודעה ירוקה פעם אחת.',
            [('ב-Controller, לפני ה-RedirectToAction', '''
TempData["Message"] = "המוצר נשמר בהצלחה!";
return RedirectToAction("Index");'''),
             ('ב-_Layout.cshtml, מעל @RenderBody()', '''
@if (TempData["Message"] != null)
{
    <div class="alert alert-success alert-dismissible fade show mt-3">
        @TempData["Message"]
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    </div>
}''')],
            change='<code class="inline">TempData</code> שורד מעבר עמוד אחד (Redirect), ואז נמחק לבד. כשההודעה ב-Layout, היא עובדת בכל העמודים.'),

    snippet('רשימה נפתחת מטבלה אחרת',
            'בחירת קטגוריה למוצר מתוך טבלת הקטגוריות.',
            [('ב-Controller, בשני ה-Create (וגם ב-Edit)', '''
ViewBag.Categories = new SelectList(_context.Categories.ToList(), "Id", "Name");'''),
             ('בטופס', '''
<select asp-for="CategoryId" asp-items="ViewBag.Categories" class="form-select">
    <option value="">-- בחרו קטגוריה --</option>
</select>''')],
            guide=G('14-relationships', 'מדריך 14, סעיף 4')),

    snippet('חיפוש, מיון וסינון',
            'תיבת חיפוש לפי שם, מיון לפי מחיר וסינון לפי קטגוריה.',
            [('ב-Controller (הבסיס)', '''
public IActionResult Index(string? search)
{
    var products = _context.Products.AsQueryable();
    if (!string.IsNullOrEmpty(search))
    {
        products = products.Where(p => p.Name.Contains(search));
    }
    ViewBag.Search = search;
    return View(products.ToList());
}'''),
             ('ב-View', '''
<form asp-action="Index" method="get" class="mb-3">
    <input type="text" name="search" value="@ViewBag.Search" class="form-control" placeholder="חיפוש..." />
</form>''')],
            guide=G('adv-b-search', 'מתקדם ב (כולל מיון וסינון לפי קטגוריה)')),

    snippet('העלאת תמונה',
            'טופס עם בחירת קובץ, ושמירה ב-wwwroot.',
            [('בטופס', '''
<form asp-action="Create" method="post" enctype="multipart/form-data">
    <input type="file" name="imageFile" class="form-control" accept="image/*" />
    ...
</form>''')],
            change='ב-<code class="inline">Program.cs</code> צריך גם <code class="inline">app.UseStaticFiles();</code> לפני <code class="inline">app.UseRouting();</code>, אחרת תמונות שהועלו לא יוצגו.',
            guide=G('16-images', 'מדריך 16 (כולל הקוד המלא לשמירה ב-Controller)')),

    snippet('נתונים התחלתיים (Seed)',
            'מוצרים לדוגמה שנכנסים למסד הנתונים לבד, אם הטבלה ריקה. נוח מאוד במחשב חדש.',
            [('ב-Program.cs, מיד אחרי var app = builder.Build();', '''
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();

    if (!db.Products.Any())
    {
        db.Products.AddRange(
            new Product { Name = "עט", Price = 5, Description = "עט כחול" },
            new Product { Name = "מחברת", Price = 12, Description = "מחברת 80 דפים" },
            new Product { Name = "תיק", Price = 150, Description = "תיק גב" }
        );
        db.SaveChanges();
    }
}''')],
            change='החליפו את המוצרים בנתונים שלכם. <code class="inline">Product</code> יסומן באדום: <span class="keyboard">Ctrl+.</span> יוסיף בראש <code class="inline">Program.cs</code> את ה-<code class="inline">using</code> של התיקייה Models. אם עשיתם את מדריך 17, אפשר לשים את זה באותו בלוק <code class="inline">using</code> של יצירת המנהל.',
            star=True),

    snippet('סינון לפי קטגוריה',
            'קישורים לכל קטגוריה, שמציגים רק את המוצרים שלה.',
            [('ב-View', '''
@foreach (var category in (List<Category>)ViewBag.Categories)
{
    <a asp-action="Index" asp-route-categoryId="@category.Id" class="btn btn-sm btn-outline-primary">@category.Name</a>
}'''),
             ('ב-Controller, בתוך Index(int? categoryId)', '''
if (categoryId != null)
{
    products = products.Where(p => p.CategoryId == categoryId);
}
ViewBag.Categories = _context.Categories.ToList();''')],
            guide=G('adv-b-search', 'מתקדם ב, סעיף 3')),

    snippet('כפתור "אהבתי" עם מונה',
            'לחיצה מעלה מונה, בלי לטעון את העמוד מחדש.',
            [('בעמוד (הכפתור)', '''
<button type="button" class="btn btn-sm btn-outline-danger like-btn" data-id="@product.Id">
    ❤️ <span class="count">@product.Likes</span>
</button>''')],
            guide=G('adv-d-fetch', 'מתקדם ד (הקוד המלא: מודל, Controller ו-JavaScript)')),
]))

# ======================= טפסים =======================
sections.append(('טפסים', [
    snippet('הודעות שגיאה בעברית',
            'הכללים הנפוצים, כל אחד עם הודעה בעברית.',
            [('במודל (בראש הקובץ: using System.ComponentModel.DataAnnotations;)', '''
[Required(ErrorMessage = "שדה חובה")]
[StringLength(50, MinimumLength = 2, ErrorMessage = "בין 2 ל-50 תווים")]
[Display(Name = "שם")]
public string Name { get; set; } = "";

[Required(ErrorMessage = "נא להזין אימייל")]
[EmailAddress(ErrorMessage = "אימייל לא תקין")]
[Display(Name = "אימייל")]
public string Email { get; set; } = "";

[Phone(ErrorMessage = "מספר טלפון לא תקין")]
[Display(Name = "טלפון")]
public string? Phone { get; set; }

[Range(1, 120, ErrorMessage = "גיל בין 1 ל-120")]
[Display(Name = "גיל")]
public int Age { get; set; }''')],
            guide=G('12-validation', 'מדריך 12'),
            star=True),

    snippet('בחירת תאריך',
            'שדה עם לוח שנה לבחירת תאריך.',
            [('במודל', '''
[DataType(DataType.Date)]
[Display(Name = "תאריך")]
public DateTime EventDate { get; set; } = DateTime.Today;'''),
             ('בטופס', '''
<input asp-for="EventDate" class="form-control" />''')],
            change='בלי <code class="inline">[DataType(DataType.Date)]</code> השדה יבקש גם שעה.'),

    snippet('תיבת סימון (כן/לא)',
            'Property מסוג bool הופך לתיבת סימון.',
            [('במודל', '''
[Display(Name = "מוצג באתר")]
public bool IsActive { get; set; }'''),
             ('בטופס', '''
<div class="form-check mb-3">
    <input asp-for="IsActive" class="form-check-input" />
    <label asp-for="IsActive" class="form-check-label"></label>
</div>''')]),

    snippet('טקסט ארוך',
            'תיבת טקסט גבוהה, לתיאור או להודעה.',
            [('בטופס', '''
<textarea asp-for="Description" class="form-control" rows="5"></textarea>''')]),

    snippet('רשימה נפתחת עם ערכים קבועים',
            'בחירה מתוך כמה אפשרויות קבועות, בלי טבלה במסד.',
            [('בטופס', '''
<select asp-for="Size" class="form-select">
    <option value="">-- בחרו מידה --</option>
    <option value="S">קטן</option>
    <option value="M">בינוני</option>
    <option value="L">גדול</option>
</select>''')],
            change='<code class="inline">value</code> הוא מה שנשמר, והטקסט הוא מה שרואים.'),

    snippet('טופס "צור קשר" שנשמר במסד',
            'מודל להודעות, שנשמרות בטבלה ומוצגות למנהל.',
            [('מודל: Models/ContactMessage.cs (בתוך המחלקה)', '''
public int Id { get; set; }

[Required(ErrorMessage = "נא להזין שם")]
[Display(Name = "שם")]
public string Name { get; set; } = "";

[Required(ErrorMessage = "נא להזין אימייל")]
[EmailAddress(ErrorMessage = "אימייל לא תקין")]
[Display(Name = "אימייל")]
public string Email { get; set; } = "";

[Required(ErrorMessage = "נא לכתוב הודעה")]
[Display(Name = "הודעה")]
public string Message { get; set; } = "";

public DateTime SentAt { get; set; } = DateTime.Now;''')],
            change='אחר כך: <code class="inline">DbSet</code> ו-Migration (מדריך 13), ו-Scaffolding (מדריך 15) או Controller עם Create (מדריך 11). את עמוד הרשימה חוסמים למנהל (מדריך 17).',
            guide=G('11-forms', 'מדריך 11') + ', ' + G('13-database', 'מדריך 13')),
]))

# ======================= משתמשים =======================
sections.append(('משתמשים', [
    snippet('"שלום, [שם]"',
            'ברכה למשתמש המחובר, וקישורי הרשמה לאורח.',
            [('בכל View', '''
@if (User.Identity?.IsAuthenticated == true)
{
    <p>שלום, @User.Identity.Name!</p>
}
else
{
    <a asp-area="Identity" asp-page="/Account/Login">התחברות</a>
    <a asp-area="Identity" asp-page="/Account/Register">הרשמה</a>
}''')],
            guide=G('17-users', 'מדריך 17, סעיף 3') + ', ' + G('adv-c-identity', 'מתקדם ג (שם מלא במקום אימייל)')),

    snippet('כפתור שרק מנהל רואה',
            'מסתיר כפתור מכל מי שאינו מנהל. (ההגנה האמיתית היא [Authorize] ב-Controller!)',
            [('ב-View', '''
@if (User.IsInRole("Admin"))
{
    <a asp-action="Create" class="btn btn-primary">הוספת מוצר</a>
}''')],
            guide=G('17-users', 'מדריך 17, סעיף 5')),

    snippet('עמוד שרק מנהל נכנס אליו',
            'חוסם Action אחד, או Controller שלם.',
            [('מעל Action או מעל ה-class של ה-Controller', '''
[Authorize(Roles = "Admin")]''')],
            guide=G('17-users', 'מדריך 17, סעיף 4')),

    snippet('יצירת המנהל הראשון',
            'בכל הפעלה: יוצר את התפקיד Admin ונותן אותו לאימייל מסוים.',
            [('ב-Program.cs (דורש .AddRoles&lt;IdentityRole&gt;())', '''
using (var scope = app.Services.CreateScope())
{
    var roleManager = scope.ServiceProvider.GetRequiredService<RoleManager<IdentityRole>>();
    var userManager = scope.ServiceProvider.GetRequiredService<UserManager<IdentityUser>>();

    if (!await roleManager.RoleExistsAsync("Admin"))
    {
        await roleManager.CreateAsync(new IdentityRole("Admin"));
    }

    var admin = await userManager.FindByEmailAsync("admin@example.com");
    if (admin != null && !await userManager.IsInRoleAsync(admin, "Admin"))
    {
        await userManager.AddToRoleAsync(admin, "Admin");
    }
}''')],
            change='החליפו את האימייל. אם עשיתם את מתקדם ג, כתבו <code class="inline">ApplicationUser</code> במקום <code class="inline">IdentityUser</code>.',
            guide=G('17-users', 'מדריך 17, סעיף 4 (כל השלבים)')),

    snippet('רק הנתונים של המשתמש המחובר ("ההזמנות שלי")',
            'כל משתמש רואה רק את מה שהוא יצר. מתאים להזמנות, פוסטים, משימות.',
            [('במודל: שדה שישמור מי יצר', '''
public string UserId { get; set; } = "";'''),
             ('ב-Controller (בראש הקובץ: using System.Security.Claims;)', '''
[Authorize]
public IActionResult MyOrders()
{
    var userId = User.FindFirstValue(ClaimTypes.NameIdentifier);
    var orders = _context.Orders.Where(o => o.UserId == userId).ToList();
    return View(orders);
}

[HttpPost]
[ValidateAntiForgeryToken]
[Authorize]
public IActionResult Create(Order order)
{
    order.UserId = User.FindFirstValue(ClaimTypes.NameIdentifier)!;
    ModelState.Remove("UserId");

    if (!ModelState.IsValid)
    {
        return View(order);
    }
    _context.Orders.Add(order);
    _context.SaveChanges();
    return RedirectToAction("MyOrders");
}''')],
            change='<code class="inline">ModelState.Remove("UserId")</code>: את השדה הזה ממלאים בקוד ולא בטופס, אז לא בודקים אותו. ואחרי הוספת השדה למודל: Migration.',
            star=True),

    snippet('ניהול משתמשים ומתן הרשאת מנהל',
            'עמוד למנהל: רשימת כל המשתמשים, וכפתור שהופך משתמש למנהל.',
            [('Controller חדש: AdminUsersController (בתוך המחלקה)', '''
private readonly UserManager<IdentityUser> _userManager;

public AdminUsersController(UserManager<IdentityUser> userManager)
{
    _userManager = userManager;
}

public IActionResult Index()
{
    return View(_userManager.Users.ToList());
}

[HttpPost]
[ValidateAntiForgeryToken]
public async Task<IActionResult> MakeAdmin(string id)
{
    var user = await _userManager.FindByIdAsync(id);
    if (user != null)
    {
        await _userManager.AddToRoleAsync(user, "Admin");
    }
    return RedirectToAction("Index");
}'''),
             ('מעל ה-class של ה-Controller', '''
[Authorize(Roles = "Admin")]'''),
             ('ב-View: Views/AdminUsers/Index.cshtml', '''
@model List<Microsoft.AspNetCore.Identity.IdentityUser>

<h1>משתמשים</h1>
<table class="table">
    @foreach (var user in Model)
    {
        <tr>
            <td>@user.Email</td>
            <td>
                <form asp-action="MakeAdmin" asp-route-id="@user.Id" method="post">
                    <button type="submit" class="btn btn-sm btn-warning">הפוך למנהל</button>
                </form>
            </td>
        </tr>
    }
</table>''')],
            change='אם עשיתם את מתקדם ג, החליפו כל <code class="inline">IdentityUser</code> ב-<code class="inline">ApplicationUser</code>.',
            guide=G('17-users', 'מדריך 17')),

    snippet('עמוד "הפרופיל שלי"',
            'לכל משתמש כבר יש עמוד מוכן לשינוי סיסמה ואימייל. רק צריך קישור אליו.',
            [('בתפריט או בכל עמוד', '''
<a asp-area="Identity" asp-page="/Account/Manage/Index">הפרופיל שלי</a>''')]),

    snippet('הפניה לעמוד מסוים אחרי התחברות',
            'אחרי ההתחברות, המשתמש יגיע לעמוד שבחרתם ולא לדף הבית.',
            [('קישור ההתחברות', '''
<a asp-area="Identity" asp-page="/Account/Login" asp-route-returnUrl="/Products">התחברו כדי לקנות</a>''')],
            change='<code class="inline">returnUrl</code> הוא הכתובת שאליה יחזרו אחרי ההתחברות.'),
]))

# ======================= עיצוב ומבנה =======================
sections.append(('עיצוב ומבנה', [
    snippet('האתר בעברית, מימין לשמאל',
            'שני שינויים ב-_Layout.cshtml.',
            [('בשורה הראשונה אחרי DOCTYPE', '''
<html lang="he" dir="rtl">'''),
             ('במקום הקישור ל-bootstrap.min.css', '''
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.rtl.min.css" />''')],
            change='בדקו את גרסת ה-Bootstrap בפרויקט (בשורה הראשונה של <code class="inline">wwwroot/lib/bootstrap/dist/css/bootstrap.min.css</code>) ושימו אותה במקום 5.3.3.',
            guide=G('08-css-js', 'מדריך 8, סעיף 6'),
            star=True),

    snippet('קישור בתפריט',
            'עוד פריט בתפריט העליון.',
            [('ב-_Layout.cshtml, ליד שאר ה-nav-item', '''
<li class="nav-item">
    <a class="nav-link text-dark" asp-controller="Products" asp-action="Index">מוצרים</a>
</li>''')],
            guide=G('06-layout', 'מדריך 6, סעיף 3')),

    snippet('תפריט שמשתנה לפי מי שמחובר',
            'קישורים שונים לאורח, למשתמש ולמנהל.',
            [('ב-_Layout.cshtml, בתוך התפריט', '''
@if (User.Identity?.IsAuthenticated == true)
{
    <li class="nav-item">
        <a class="nav-link text-dark" asp-controller="Orders" asp-action="MyOrders">ההזמנות שלי</a>
    </li>
}
@if (User.IsInRole("Admin"))
{
    <li class="nav-item">
        <a class="nav-link text-danger" asp-controller="Categories" asp-action="Index">ניהול</a>
    </li>
}''')]),

    snippet('סימון הקישור הפעיל בתפריט',
            'הקישור של העמוד הנוכחי מודגש, כך שרואים איפה נמצאים.',
            [('ב-_Layout.cshtml, לפני התפריט', '''
@{
    var currentController = ViewContext.RouteData.Values["controller"]?.ToString();
}'''),
             ('בכל קישור בתפריט', '''
<a class="nav-link @(currentController == "Products" ? "active fw-bold" : "text-dark")"
   asp-controller="Products" asp-action="Index">מוצרים</a>''')],
            change='בכל קישור, כתבו בתנאי את שם ה-Controller שלו.'),

    snippet('כפתור "חזרה"',
            'חוזר לעמוד הקודם, כמו כפתור החזרה של הדפדפן.',
            [('בכל View', '''
<a href="javascript:history.back()" class="btn btn-secondary">→ חזרה</a>''')]),

    snippet('חלון קופץ (Modal)',
            'חלון שנפתח מעל העמוד בלחיצה על כפתור. Bootstrap כבר כולל את ה-JavaScript שלו.',
            [('בכל View', '''
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#infoModal">
    מידע נוסף
</button>

<div class="modal fade" id="infoModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">מידע נוסף</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <div class="modal-body">
                כאן כותבים את התוכן של החלון.
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">סגירה</button>
            </div>
        </div>
    </div>
</div>''')],
            change='ה-<code class="inline">data-bs-target</code> של הכפתור חייב להיות זהה ל-<code class="inline">id</code> של החלון (עם # לפניו).'),

    snippet('הודעה שנסגרת בלחיצה',
            'הודעה עם X לסגירה.',
            [('בכל View', '''
<div class="alert alert-warning alert-dismissible fade show">
    שימו לב: המבצע מסתיים ביום חמישי!
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
</div>''')]),

    snippet('לוגו בתפריט ואייקון לכרטיסייה',
            'תמונה במקום (או ליד) שם האתר, ואייקון משלכם בלשונית של הדפדפן.',
            [('ב-_Layout.cshtml, בתוך ה-navbar-brand', '''
<a class="navbar-brand" asp-controller="Home" asp-action="Index">
    <img src="~/images/logo.png" alt="לוגו" height="32" />
    האתר שלי
</a>'''),
             ('ב-_Layout.cshtml, בתוך ה-head', '''
<link rel="icon" href="~/images/icon.png" />''')],
            change='שימו את התמונות בתיקייה <code class="inline">wwwroot/images</code>.'),

    snippet('עמוד 404 מעוצב',
            'במקום עמוד ריק כשכתובת לא קיימת, עמוד "העמוד לא נמצא" משלכם.',
            [('ב-Program.cs, לפני app.UseRouting();', '''
app.UseStatusCodePagesWithReExecute("/Home/PageNotFound");'''),
             ('ב-HomeController', '''
public IActionResult PageNotFound()
{
    return View();
}'''),
             ('Views/Home/PageNotFound.cshtml', '''
@{
    ViewData["Title"] = "העמוד לא נמצא";
}

<div class="text-center mt-5">
    <h1 class="display-1">404</h1>
    <p class="lead">אופס, העמוד שחיפשתם לא קיים. 🤔</p>
    <a asp-controller="Home" asp-action="Index" class="btn btn-primary">לדף הבית</a>
</div>''')]),

    snippet('Footer',
            'השורה התחתונה של האתר.',
            [('ב-_Layout.cshtml, בתוך ה-footer', '''
<div class="container text-center">
    &copy; 2027 · האתר של גיל ·
    <a asp-controller="Home" asp-action="Privacy">פרטיות</a> ·
    <a href="mailto:dana@example.com">צרו קשר</a>
</div>''')]),
]))

# ======================= JavaScript =======================
sections.append(('JavaScript פשוט', [
    snippet('כפתור "הצג סיסמה"',
            'תיבת סימון שמציגה את הסיסמה שהוקלדה.',
            [('בטופס, מתחת לשדה הסיסמה', '''
<div class="form-check">
    <input type="checkbox" class="form-check-input" id="showPassword" />
    <label class="form-check-label" for="showPassword">הצג סיסמה</label>
</div>'''),
             ('בסוף העמוד', '''
@section Scripts {
    <script>
        document.getElementById("showPassword").addEventListener("change", function () {
            var input = document.querySelector('input[type="password"], input.password-field');
            input.classList.add("password-field");
            input.type = this.checked ? "text" : "password";
        });
    </script>
}''')],
            change='בדפי ההרשמה וההתחברות צריך קודם להוציא אותם לעריכה (מתקדם ג, סעיף 4).'),

    snippet('מונה תווים בתיבת טקסט',
            'מציג כמה תווים הוקלדו מתוך המקסימום.',
            [('בטופס', '''
<textarea asp-for="Message" class="form-control" maxlength="500" id="messageBox"></textarea>
<small class="text-muted"><span id="charCount">0</span>/500</small>'''),
             ('בסוף העמוד', '''
@section Scripts {
    <script>
        var box = document.getElementById("messageBox");
        box.addEventListener("input", function () {
            document.getElementById("charCount").textContent = box.value.length;
        });
    </script>
}''')]),
]))

# ======================= page =======================
body = []
for title, items in sections:
    body.append(f'    <h2>{title}</h2>')
    body.extend(items)

page = f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ספריית קטעי קוד</title>
    <script src="../assets/theme-init.js"></script>
    <link rel="stylesheet" href="../assets/style.css">
</head>
<body data-guide="snippets" data-toc="deep">
<main>
    <h1>📚 ספריית קטעי קוד</h1>
    <div class="subtitle">קטעים מוכנים להעתקה: מה כל קטע עושה, איפה מדביקים אותו, ומה צריך לשנות</div>

    <div class="explanation">
        <strong>💡 איך משתמשים בספרייה?</strong> מצאו את מה שאתם צריכים בתוכן העניינים (או חפשו עם <span class="keyboard">Ctrl+F</span>), העתיקו עם כפתור "העתק", והדביקו בקובץ שכתוב ליד "📁 איפה".
        <ul style="margin-bottom:0">
            <li>בדוגמאות השמות הם של מוצרים (<code class="inline">Product</code>, <code class="inline">_context.Products</code>). <strong>החליפו אותם בשמות של הפרויקט שלכם.</strong></li>
            <li>רוב הקטעים מניחים שה-Controller כבר מחובר למסד הנתונים (<code class="inline">_context</code>, מדריך 13).</li>
            <li>לא בטוחים מה קטע עושה? בתחתית שלו יש קישור למדריך שמסביר אותו לעומק.</li>
            <li>קטעים שמסומנים ב-<span class="star">⭐</span> שימושיים כמעט בכל פרויקט.</li>
        </ul>
    </div>

{chr(10).join(body)}
</main>
<script src="../assets/site.js"></script>
</body>
</html>
'''
open(__import__('os').path.join(__import__('os').path.dirname(__file__), '..', 'guides', 'snippets.html'), 'w', encoding='utf-8').write(page)
print('snippets:', sum(len(i) for _, i in sections))
