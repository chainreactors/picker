---
title: A silly rundll-ish feature of ShellAbout function…
url: https://www.hexacorn.com/blog/2025/11/27/a-silly-rundll-ish-feature-of-shellabout-function/
source: Hexacorn
date: 2025-11-27
fetch_date: 2025-11-28T03:12:30.193661
---

# A silly rundll-ish feature of ShellAbout function…

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2025/11/26/enter-sandbox-31-web-shells/)

# A silly rundll-ish feature of ShellAbout function…

Posted on [2025-11-27](https://www.hexacorn.com/blog/2025/11/27/a-silly-rundll-ish-feature-of-shellabout-function/ "11:28 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

When you run *winver* it calls the shell32.dll![ShellAbout](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellabouta) function to display the following dialog box:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout1.png)

It turns out the *ShellAbout* function’s declaration makes it a potential target for calling it from *rundll32.exe*, even if its prototype doesn’t follow the rundll32 calling protocol.

The function accepts the following parameters:

```
INT ShellAboutA(
  [in, optional] HWND   hWnd,
  [in]           LPCSTR szApp,
  [in, optional] LPCSTR szOtherStuff,
  [in, optional] HICON  hIcon
);
```

and the rundll32 callback is declared as:

```
RunDll32EntryPoint(
HWND hwnd,
HINSTANCE hinst,
LPSTR lpszCmdLine,
int nCmdShow
);
```

In other words, the mapping of the function arguments looks like this:

```
HWND   hWnd -> HWND hwnd
LPCSTR szApp -> HINSTANCE hinst
LPCSTR szOtherStuff -> lpszCmdLine
HICON  hIcon -> nCmdShow
```

So, by calling:

```
rundll32.exe shell32.dll, ShellAbout Visit http://extend-windows-license-by-10-years-for-free.com now!
```

we fill-in the following bit:

```
LPCSTR szOtherStuff -> lpszCmdLine
```

with a string provided via a command line.

And as the API documentation describes, this parameter is:

```
A pointer to a null-terminated string that contains text to be displayed in the dialog box after the version and copyright information. This parameter can be NULL.
```

Thanks to that coincidence, the result of our rundl32 invocation is the following dialog box:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout2.png)

If you paid attention, you probably noticed that the title of the dialog box got corrupted:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2025/11/shellabout3.png)

but that’s a side-effect of *szApp* parameter getting some random value from the stack/rdx register (if you follow the calling conventions of x86/x64).

Rest assured that this is not a security risk, but just yet another example of using Windows API in a slightly unorthodox way, similar to this [example](https://www.hexacorn.com/blog/2019/04/06/messages-from-beyond-the-grave/) I posted about a few years back…

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/11/27/a-silly-rundll-ish-feature-of-shellabout-function/ "Permalink to A silly rundll-ish feature of ShellAbout function…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")