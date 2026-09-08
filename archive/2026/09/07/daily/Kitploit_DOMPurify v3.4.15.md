---
title: DOMPurify v3.4.15
url: https://kitploit.com/en/posts/github-cure53-dompurify-3415
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:41:02.311571
---

# DOMPurify v3.4.15

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/237/ddaac853f5ec658e80d8055488a7d4178798f3656c57d8ff20fd53d56a076de1.png)

New releaseSep 7, 2026

# DOMPurify v3.4.15

DOMPurify - a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG. DOMPurify works with a secure default, but offers a lot of configurability and hooks. Demo:

Share

# DOMPurify

[![npm](https://img.shields.io/npm/v/dompurify.svg)](https://www.npmjs.com/package/dompurify) [![License](https://img.shields.io/badge/license-MPL--2.0%20OR%20Apache--2.0-blue.svg)](https://github.com/cure53/DOMPurify/blob/main/LICENSE) [![Downloads](https://img.shields.io/npm/dm/dompurify.svg)](https://www.npmjs.com/package/dompurify) [![dependents](https://badgen.net/github/dependents-repo/cure53/dompurify?color=green&label=dependents)](https://github.com/cure53/DOMPurify/network/dependents) ![npm package minimized gzipped size (select exports)](https://img.shields.io/bundlejs/size/dompurify?color=%233C1&label=gzip) [![Cloudback](https://app.cloudback.it/badge/cure53/DOMPurify)](https://cloudback.it)

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/12162/badge)](https://www.bestpractices.dev/projects/12162) [![Build & Test](https://github.com/cure53/DOMPurify/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/cure53/DOMPurify/actions/workflows/build-and-test.yml) [![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/cure53/DOMPurify/badge)](https://scorecard.dev/viewer/?uri=github.com/cure53/DOMPurify) [![Socket Badge](https://badge.socket.dev/npm/package/dompurify/latest)](https://badge.socket.dev/npm/package/dompurify/latest) [![snyk.io package health](https://img.shields.io/badge/snyk.io%20package%20health-97/100-brightgreen)](https://security.snyk.io/package/npm/dompurify)

DOMPurify is a DOM-only, super-fast, uber-tolerant XSS sanitizer for HTML, MathML and SVG.

It's also very simple to use and get started with. DOMPurify was [started in February 2014](https://github.com/cure53/DOMPurify/commit/a630922616927373485e0e787ab19e73e3691b2b) and, meanwhile, has reached version **v3.4.15**.

DOMPurify runs as JavaScript and works in all modern browsers (Safari (10+), Opera (15+), Edge, Firefox and Chrome - as well as almost anything else using Blink, Gecko or WebKit). It doesn't break on MSIE or other legacy browsers. It simply does nothing.

**Note that [DOMPurify v2.5.9](https://github.com/cure53/DOMPurify/releases/tag/2.5.9) is the latest version supporting MSIE. For important security updates compatible with MSIE, please use the [2.x branch](https://github.com/cure53/DOMPurify/tree/2.x).**

Our automated tests cover 9 browser/OS combinations on the current engines (Chromium, Firefox, and WebKit across Ubuntu, macOS, and Windows) on every push, and a separate matrix re-runs the suite on older engine snapshots (back to roughly Chromium 110, Firefox 108 and WebKit 16.4, around three years old) so regressions on outdated browsers get caught too. We also run Node.js v20, v22, v24, v25 and v26 with DOMPurify on [jsdom](https://github.com/jsdom/jsdom). Older Node versions are known to work as well, but hey... no guarantees.

DOMPurify is written by security people who have vast background in web attacks and XSS. Fear not. For more details please also read about our [Security Goals & Threat Model](https://github.com/cure53/DOMPurify/wiki/Security-Goals-%26-Threat-Model). Please, read it. Like, really. And if you enjoy the gory details, the [Attack Classes & Bypass History](https://github.com/cure53/DOMPurify/wiki/Attack-Classes-%26-Bypass-History) page catalogs the parser-mutation, namespace, clobbering, and template tricks DOMPurify defends against.

The DOMPurify project inspired the creation of the [HTML Sanitizer API](https://wicg.github.io/sanitizer-api/#sanitizer), which is already shipping in [many browsers](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Sanitizer_API#browser_compatibility). The same capability is now being standardized directly in the [WHATWG HTML specification](https://html.spec.whatwg.org/#html-sanitization).

## Table of Contents

* [What does it do?](#what-does-it-do)
* [How do I use it?](#how-do-i-use-it)
* [Is there a demo?](#is-there-a-demo)
* [What if I find a *security* bug?](#what-if-i-find-a-security-bug)
* [Some purification samples please?](#some-purification-samples-please)
* [What is supported?](#what-is-supported)
* [What about legacy browsers like Internet Explorer?](#what-about-legacy-browsers-like-internet-explorer)
* [What about DOMPurify and Trusted Types?](#what-about-dompurify-and-trusted-types)
* [Can I configure DOMPurify?](#can-i-configure-dompurify)
* [Persistent Configuration](#persistent-configuration)
* [Hooks](#hooks)
* [Removed Configuration](#removed-configuration)
* [Continuous Integration](#continuous-integration)
* [Security Mailing List](#security-mailing-list)
* [Who contributed?](#who-contributed)

## What does it do?

DOMPurify sanitizes HTML and prevents XSS attacks. You can feed DOMPurify with e.g. a string full of dirty HTML and it will return a string (unless configured otherwise) with clean HTML. DOMPurify will strip out everything that contains dangerous HTML and thereby prevent XSS attacks and other nastiness. It's also damn bloody fast. We use the technologies the browser provides and turn them into an XSS filter. The faster your browser, the faster DOMPurify will be.

## How do I use it?

It's easy. Just include DOMPurify on your website.

### Using the unminified version (source-map available)

root@kitploit:~

```
<script type="text/javascript" src="dist/purify.js"></script>
```

### Using the minified and tested production version (source-map available)

root@kitploit:~

```
<script type="text/javascript" src="dist/purify.min.js"></script>
```

Afterwards you can sanitize strings by executing the following code:

root@kitploit:~

```
const clean = DOMPurify.sanitize(dirty);
```

Or maybe this, if you love working with Angular or alike:

root@kitploit:~

```
import DOMPurify from 'dompurify';

const clean = DOMPurify.sanitize('<b>hello there</b>');
```

The resulting HTML can be written into a DOM element using `innerHTML` or the DOM using `document.write()`. That is fully up to you.
Note that by default, we permit HTML, SVG **and** MathML. If you only need HTML, which might be a very common use-case, you can easily set that up as well:

root@kitploit:~

```
const clean = DOMPurify.sanitize(dirty, { USE_PROFILES: { html: true } });
```

### Is there any foot-gun potential?

Well, please note, if you *first* sanitize HTML and then modify it *afterwards*, you might easily **void the effects of sanitization**. If you feed the sanitized markup to another library *after* sanitization, please be certain that the library doesn't mess around with the HTML on its own. See the [Security Goals & Threat Model](https://github.com/cure53/DOMPurify/wiki/Security-Goals-%26-Threat-Model) for safe-usage recipes and the tags/attributes worth thinking twice about, and [Attack Classes & Bypass History](https://github.com/cure53/DOMPurify/wiki/Attack-Classes-%26-Bypass-History) for why post-processing and changing the markup context defeat sanitization.

### Okay, makes sense, let's move on

After sanitizing your markup, you can also have a look at the property `DOMPurify.removed` and find out, what elements and attributes were thrown out. Please **do not use** this property for making any security critical decisions. This is just a little helper for curious minds.

### Running DOMPurify on the server

DOMPurify technica...