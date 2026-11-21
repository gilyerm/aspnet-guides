# ASP.NET Core MVC Guides (Hebrew)

**🌐 Live site: [gilyerm.github.io/aspnet-guides](https://gilyerm.github.io/aspnet-guides/)**

A series of step-by-step guides, written in Hebrew, for high-school students building their first website with **ASP.NET Core MVC** in **Visual Studio**. The guides assume only basic C# and HTML, and explain every new concept with a short example.

## What's inside

| Section | Topics |
|---|---|
| Getting started | Creating a project with Individual Accounts, working in Visual Studio, Git & GitHub (GUI only) |
| Building pages | How MVC works, Razor (`.cshtml`), the Layout and menu, adding pages, CSS & JS, RTL, Bootstrap |
| Data | Models, forms, validation, Entity Framework & migrations, relationships, scaffolding |
| Images & users | Image upload, authorization and roles |
| Optional (advanced) | Partial views, search & filtering, customizing Identity, `fetch`, a shopping cart |
| Tools | Reading errors, debugging with breakpoints, project planning, a code snippet library |

Every guide includes:

- Copy-ready code with a **Copy** button and syntax highlighting
- Concept boxes in plain Hebrew, each with an example
- Checkpoints ("you should now see…") and a troubleshooting section
- A short exercise and a "what we learned" summary

## Project structure

```
index.html            Home page (guide list is built from assets/site.js)
guides/               One HTML file per guide
assets/style.css      Shared styles
assets/site.js        Guide list, navigation, table of contents, search, copy buttons, highlighting
assets/vendor/        Prism.js (syntax highlighting) and the VS Code Dark+ theme
tools/build_snippets.py  Generates guides/snippets.html (edit the snippet list there, then run it)
```

## Adding or publishing a guide

1. Create the page in `guides/` (copy an existing guide as a template).
2. In `assets/site.js`, find the guide in the `GUIDES` list and set `ready: true`.
3. Commit and push. GitHub Pages publishes the change within a minute or two.

## Credits

Syntax highlighting by [Prism](https://prismjs.com/) (MIT) with the VS Code Dark+ theme from [prism-themes](https://github.com/PrismJS/prism-themes) (MIT).
