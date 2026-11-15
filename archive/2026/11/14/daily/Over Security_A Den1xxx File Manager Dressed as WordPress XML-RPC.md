---
title: A Den1xxx File Manager Dressed as WordPress XML-RPC
url: https://lukeleal.com/research/posts/den1xxx-filemanager-wp-xmlrpc-costume/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:39.085199
---

# A Den1xxx File Manager Dressed as WordPress XML-RPC

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

# [A Den1xxx File Manager Dressed as WordPress XML-RPC](https://lukeleal.com/research/posts/den1xxx-filemanager-wp-xmlrpc-costume/)

2026-11-09Luke

#[Den1xxx](https://lukeleal.com/research/tags/den1xxx/)
#[Filemanager](https://lukeleal.com/research/tags/filemanager/)
#[WP File Manager](https://lukeleal.com/research/tags/wp-file-manager/)
#[XML-RPC](https://lukeleal.com/research/tags/xml-rpc/)
#[web shell](https://lukeleal.com/research/tags/web-shell/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![A Den1xxx File Manager Dressed as WordPress XML-RPC](https://lukeleal.com/research/den1xxx-filemanager-wp-xmlrpc-costume-cover-q90.jpg "Cover Image")

## Table of Contents

* [What It Does](#what-it-does)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)

The first comment says *“XML-RPC protocol support for WordPress … @package WordPress”* and the second is a **fake plugin header**: *“Plugin Name: WP File Manager … Author: mndpsingh287 … Version: 8.0”*. Neither is real. The file is **84,401 bytes** and underneath is the public **Den1xxx Filemanager** (“PHP File Manager Mini”; `github.com/Den1xxx/Filemanager` is in the footer).

![Fake XML-RPC running live in the sandbox](/research/shell-live-5392b72f57.jpg)

*Screenshot of the shell running live in an offline sandbox, on a dummy WordPress site with invented accounts, domains and files.*

## What It Does[#](#what-it-does)

* **The login is off.** The configuration is a JSON string: `{"authorize":"0","login":"admin","password":"phpfm","cookie_name":"fm_user","days_authorization":"30", ...}`. `authorize` is `0`, so the script never asks for a login. If someone sets it to `1`, the default password is the well-known `phpfm`.
* **Features.** File list, edit with an editor, rename, chmod, delete, zip and gzip (`zip`, `gz`, `decompress`, `gzfile`), a recursive file **search**, an **SQL console** (`sql`, `sqlrun`), **PHP evaluation** (`php`, `phprun`), a proxy, `phpinfo`, and a language list (English, German, Russian, French, Ukrainian).
* **Costume.** The WordPress comments have no effect: the only reason to add them is to make a file in `wp-includes` or a plugin folder look normal in a quick review.

## Detection & Cleanup[#](#detection--cleanup)

```
# strings from this file
grep -rlF -e 'Plugin Name: WP File Manager' -e 'phpfm' -e 'fm_login' .
```

* Compare any file named `xmlrpc.php` with the one from a WordPress release: `sha256sum xmlrpc.php` against the official file. A 84 KB `xmlrpc.php` is not the 3 KB core one.

## IOCs[#](#iocs)

```
File      5392b72f5726a3205e16c5d06398e9d7   84,401 bytes
sha256    59b0c524c4c3342d1f16ecf2e3117e176d991ea2e17471cffa02e6cab18826be
md5       1800786e998bb9c008bb0eb97bf5b3ee
Strings   "XML-RPC protocol support for WordPress" + "Plugin Name: WP File Manager" + "Version: 8.0"   $authorization '{"authorize":"0","login":"admin","password":"phpfm"   fm_login   fm_config
```

---

[< ['PHP File Manager Mini' - A goto-Obfuscated Shell With Mass Deface]](https://lukeleal.com/research/posts/php-file-manager-mini-mass-deface/)::
[[One Hacked cPanel Account: Five Phishing Kits, SEO Spam, Mailers and a Zoo of Webshells] >](https://lukeleal.com/research/posts/hacked-cpanel-five-phishing-kits-and-a-shell-zoo/)

© 2026 Luke Leal

Disclaimer: The research posted on this website is for information purposes only. Do not use it for illegal purposes.