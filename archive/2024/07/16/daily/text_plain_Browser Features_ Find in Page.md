---
title: Browser Features: Find in Page
url: https://textslashplain.com/2024/07/15/browser-features-find-in-page/
source: text/plain
date: 2024-07-16
fetch_date: 2025-10-06T17:44:14.999243
---

# Browser Features: Find in Page

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Browser Features: Find in Page

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-07-152024-09-20](https://textslashplain.com/2024/07/15/browser-features-find-in-page/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [UX](https://textslashplain.com/tag/ux/), [webdev](https://textslashplain.com/tag/webdev/)

For busy web users, the humble Find-in-Page feature in the browser is one of the most important features available. While Google or Bing can get you to the page you’re looking for faster than ever before, once you get to that page, you’ve got to find the information you’re looking for1, and that’s where Find-in-Page comes into play.

Fortunately, with the death of Adobe Flash, Find-in-Page sometimes works better than it did fifteen years decade ago, because 3rd-party plugin content couldn’t participate in the browser’s Find-in-Page feature. (*Chromium’s PDF viewer plugin does use the browser’s Find-in-Page*).

Unfortunately, the value of Find-in-Page has been on the decline in recent years, largely due to three trends:

1. Breaking information out over multiple pages
2. Virtualized DOMs (Lazy-loading)
3. Non-DOM web applications

## How it works

Conceptually, Find-in-Page is simple: simply gather the text of the page, and then search it, highlight the matches, and allow the user to navigate between each.

As a browser developer, the UX simplicity is a facade over a complicated set of conditions:

* Pages may be made up of multiple frames; some of those frames may be running in other processes, requiring cross-process, asynchronous communication
* Pages are dynamic: their contents can change, and frames can be added/removed/modified [at any time](https://webdbg.com/test/find/), including in the middle of a Find operation. A user can invoke a Find operation as the page loads, or as it’s navigating away.
* Providing the user with feedback like a Match Count or playing a “ding” sound when no more matches are found gets [quite complicated](https://issues.chromium.org/issues?q=ericlaw%20find-in-page).
* Moving the search bubble so that it doesn’t cover up the highlighted search result may be tricky.
* Figuring out how search should behave for invisible, or collapsed elements requires thought.

In Edge, things get even more complicated, with its AI-powered “Find Related” feature making network calls and hunting for related terms:

[![](https://textslashplain.com/wp-content/uploads/2024/07/image-5.png?w=921)](https://textslashplain.com/wp-content/uploads/2024/07/image-5.png)

Beyond all of these complexities, the nature of the modern web makes it harder for Find-in-Page to function as well that users hope it would.

## Problem: Paging

The problem with paging is pretty simple– many sites serve ads on each page, and the simplest way to increase page views is to [split content out over multiple pages](https://www.anandtech.com/show/21469/amd-details-ryzen-ai-300-series-for-mobile-strix-point-with-rdna-35-igpu-xdna-2-npu) so that the user must navigate to new pages to get all of their content. If the user hits CTRL+F on a page, only the content of that current page is searched. If the content you’re looking for appears on a later page, you won’t find it until you visit that later page.

There’s no easy answer here… many problems in software are the direct result of economics, and this one is no different.

## Problem: Virtualized DOMs

In other cases, a page might load content dynamically for performance reasons — loading tons of content “below the fold” might result in wasting the user’s memory or bandwidth for things they’ll never see. Returning more content into the page might put additional load onto the server, so it might use [Intersection Observer](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API) or other techniques to figure out what content should be visible and not add invisible content to the DOM.

New features like `[content-visibility](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility)` aim to allow web developers to get the performance benefits of virtual DOMs while solving some [problems like Find-in-Page](https://github.com/WICG/display-locking/blob/main/find-in-page-compat.md).

## Problem: Non-DOM Pages

On Google Docs, if you invoke the browser’s native Find experience from the … menu, you get this surprising outcome where most instances of what you’re searching for aren’t found even while they’re literally in bold text in the middle of the visible page:

[![](https://textslashplain.com/wp-content/uploads/2024/07/image.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/07/image.png)

You can see a similar effect in Microsoft’s Web version of Excel:

[![](https://textslashplain.com/wp-content/uploads/2024/07/image-2.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/07/image-2.png)

If you use the Developer Tools, it’s easy to see what’s going on here: The entire content area of the document and spreadsheet are HTML5 Canvas elements, meaning that there’s no DOM to search at all:

[![](https://textslashplain.com/wp-content/uploads/2024/07/image-4.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/07/image-4.png)

[![](https://textslashplain.com/wp-content/uploads/2024/07/image-3.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/07/image-3.png)

To address these problems, web applications may take over the `CTRL+F` keystroke to pop up their own Find experience, like the Find UX in Google Docs:

[![](https://textslashplain.com/wp-content/uploads/2024/07/image-1.png?w=1024)](https://textslashplain.com/wp-content/uploads/2024/07/image-1.png)

### Security / Privacy Implications

Most Web users may expect that websites cannot determine what they’re searching for within a web page. That expectation is faulty– there are a number of tricks a website can use to determine what the user is searching for, ranging from detecting how the browser scrolls to matches, to replacing the Find UX entirely with a lookalike (since the Find box is below the [Line-of-Death](https://textslashplain.com/2017/01/14/the-line-of-death/)).

---

1Unless the search engine takes advantage of a new web platform feature called [Scroll-to-Text-Fragment](https://developer.mozilla.org/en-US/docs/Web/Text_fragments), which deserves a blog post all its own given its usefulness and subtle security implications.

### Share this:

* [Click to share on X (Opens in new window)
  X](https://textslashplain.com/2024/07/15/browser-features-find-in-page/?share=twitter)
* [Click to share on Facebook (Opens in new window)
  Facebook](https://textslashplain.com/2024/07/15/browser-features-find-in-page/?share=facebook)

Like Loading...

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-07-152024-09-20](https://textslashplain.com/2024/07/15/browser-features-find-in-page/)Posted in[browsers](https://textslashplain.com/category/browsers/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [UX](https://textslashplain.com/tag/ux/), [webdev](https://textslashplain.com/tag/webdev/)

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity. [View more posts](https://textslashplain.com/author/ericlaw1979/)

## Post navigation

[Previous Post Previous post:
Memento Mori – Farewells](https://textslashplain.com/2024/06/10/memento-mori-farewells/)

[Next Post Next post:
Welcome to Fall, I guess?](https://textslashplain.com/2024/09/16/welcome-to-fal...