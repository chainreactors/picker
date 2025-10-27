---
title: CSP Bypass via Redirection —Compress-a-thon — Pentathon 2025
url: https://infosecwriteups.com/compress-a-thon-web-exploitation-pentathon-2025-fea9adf9fa6b?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-05-13
fetch_date: 2025-10-06T22:25:30.893994
---

# CSP Bypass via Redirection —Compress-a-thon — Pentathon 2025

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffea9adf9fa6b&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcompress-a-thon-web-exploitation-pentathon-2025-fea9adf9fa6b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcompress-a-thon-web-exploitation-pentathon-2025-fea9adf9fa6b&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fea9adf9fa6b---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fea9adf9fa6b---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CSP Bypass via Redirection — Compress-a-thon — Pentathon 2025

[![Somnath Das](https://miro.medium.com/v2/resize:fill:64:64/1*eoBuIaTUq15vI7awvMmLVQ.jpeg)](https://medium.com/%40dassomnath?source=post_page---byline--fea9adf9fa6b---------------------------------------)

[Somnath Das](https://medium.com/%40dassomnath?source=post_page---byline--fea9adf9fa6b---------------------------------------)

10 min read

·

May 7, 2025

--

1

Listen

Share

Compress-a-thon is a “web exploitation” challenge that was featured in Pentathon 2025 Finale Jeopardy CTF Round. This challenge involved chaining Content Security Policy (CSP) Bypass and HTML sanitization that led to Reflected XSS which is then used to exfiltrate user cookies.

Press enter or click to view image in full size

![]()

Featured Image

Press enter or click to view image in full size

![]()

A screenshot describing the challenge details.

## Black-Box Review

To begin our testing, it is always a good idea to look at the application as a “user” and go over its functionalities while having the brain of a “tester” to notice the details behind its functionalities as we go along-the-way.

Press enter or click to view image in full size

![]()

Screenshot for the “/” route of the target web application.

We observe a `textarea` in which we can provide `html-input` and it is supposed to “compress” it. We also observe credits to `kangax/html-minifier` and make a guess for it being the library that is providing this “compression or minification” functionality, and then there is an `Output` area in which our `minified html` is supposed to be shown.

There are two buttons, `Submit` and `Share` , `Submit` button probably triggers the compression and we are not so sure about `Share` button’s exact functionality but we can make a guess that it is supposed to “share our html” with someone else or something like that.

Press enter or click to view image in full size

![]()

HTML Source for the “/” route of the target Web Application.

Okay so we see two more `routes` for this web application.

* `/render` route which is where our `html-input` goes for “compression/minification”.
* `/redirect` route and looking at its `parameter "url="` we can make be sure that it is supposed provide `server-side redirect` functionality from this application to another `url`.

Let’s also take a look at `/js/main.js` file which contains `Client-side javascript` code.

Press enter or click to view image in full size

![]()

Client-side Javascript Source File at “/js/main.js” path

```
window.minify = require("html-minifier").minify;

(function() {
    // <-- SNIP -->
  })();
```

So it is making use of `html-minifier` library as expected and everything else is inside an [**IIFE**](https://developer.mozilla.org/en-US/docs/Glossary/IIFE) (Immediately Invoked Function Expression) which simply means that function will execute as soon as it is defined in the code.

```
function minifyHTML(htmlstring) {
  return window.minify(htmlstring, {
    collapseWhitespace: true,
    minifyCSS: true,
    minifyJS: true,
    keepClosingSlash: true,
    processConditionalComments: true,
  });
}

function getHtmlInput() {
  return document.querySelector('textarea[name="html"]').value;
}

function setOutput(styledHtml) {
  document.querySelector(".output").innerHTML = styledHtml;
}
```

* `minifyHTML()` function takes our input `htmlstring` and uses method from `html-minifer` to `minify` our `html-code` with some specific `settings` being passed into it.
* `getHtmlInput()` and `setOutput` simply `gets` our `html-input` from the mentioned `textarea` and `setOutput` `sets` or shows the result to us by setting `.output` area to provided `styledHtml` input, interesting part is that it does so by setting `.innerHTML` to `styledHtml` input and now if `styledHtml` input is not sanitized properly then this will lead to `XSS` vulnerability.

```
function styleHtml() {
  var html = getHtmlInput();
  let initialLength = html.length;
  var styledHtml = minifyHTML(html);
  let formattedLength = styledHtml.length;
  document.getElementById("initialLength").value = initialLength;
  document.getElementById("formattedLength").value = formattedLength;
  return styledHtml;
}

function handleSubmit(event) {
  event.preventDefault();
  var styledHtml = styleHtml();
  document.querySelector('textarea[name="html"]').value = styledHtml;
  event.target.submit();
}

function initializeEventListeners() {
  document.querySelector("form").addEventListener("submit", handleSubmit);
  document.querySelector(".share-btn").addEventListener("click", (event) => {
    event.preventDefault();
    shareContent();
  });
}
```

* `styleHtml()` function combines the use of previously defined functions and `minifies` our `html-input` and returns it.
* `initializeEventListeners()` function sets up `handlers` for `Submit` button and `Share` button.
* `handleSubmit()` is `a handler function` for `Submit` button that was mentioned previously. Interesting thing to note is that after `minifying` our `html-input`, this function immediately changes our `textarea` that is our old `html-input` contents back to `minified-html` contents.
* So it won’t be wrong to assume that `/render` endpoint is doing something more to our `html-input` before showing the result in the `output`.

```
function init() {
  initializeEventListeners();
}

function shareContent() {
  const form = document.querySelector("form");
  const htmlContent = form.querySelector('textarea[name="html"]').value;

  const body = new URLSearchParams({
    html: htmlContent,
  }).toString();

  fetch("/share", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: body,
  })
    .then((response) => response.json())
    .then((data) => {
      alert("Content shared successfully!");
    })
    .catch((error) => {
      console.error("Error sharing content:", error);
    });
}

init();
```

* `sh...