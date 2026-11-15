---
title: 'PHP File Manager Mini' - A goto-Obfuscated Shell With Mass Deface
url: https://lukeleal.com/research/posts/php-file-manager-mini-mass-deface/
source: Over Security
date: 2026-11-14
fetch_date: 2026-11-15T08:37:39.306950
---

# 'PHP File Manager Mini' - A goto-Obfuscated Shell With Mass Deface

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

# [‘PHP File Manager Mini’ - A goto-Obfuscated Shell With Mass Deface](https://lukeleal.com/research/posts/php-file-manager-mini-mass-deface/)

2026-11-13Luke

#[goto obfuscation](https://lukeleal.com/research/tags/goto-obfuscation/)
#[mass deface](https://lukeleal.com/research/tags/mass-deface/)
#[web shell](https://lukeleal.com/research/tags/web-shell/)
#[backdoor](https://lukeleal.com/research/tags/backdoor/)
#[symlink](https://lukeleal.com/research/tags/symlink/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
!['PHP File Manager Mini' - A goto-Obfuscated Shell With Mass Deface](https://lukeleal.com/research/php-file-manager-mini-mass-deface-cover-q90.jpg "Cover Image")

## Table of Contents

* [What It Does](#what-it-does)
* [Detection & Cleanup](#detection--cleanup)
* [IOCs](#iocs)

The page title is *“PHP File Manager Mini”* and the file is **53,271 bytes**. Like `UCHIHA RAJON` it is run through a **goto obfuscator** (`<?php goto gULgC; jsdh_: ?>`), so the order of the code in the file is not the order it runs.

![File Manager Mini running live in the sandbox](/research/shell-live-80ea2acac7.jpg)

*Screenshot of the shell running live in an offline sandbox, on a dummy WordPress site with invented accounts, domains and files.*

## What It Does[#](#what-it-does)

The menu is a row of links: **Home, Jumping, Symlink, Auto edit user, Config, Command, Adminer, Logout**. Around it are the file list and these forms:

* **Edit, rename, chmod, delete, download.** Standard file actions, with a FILE EDITOR box.
* **Multimass.** A form with a choice of **Massdeface** or **Massdelete**, a target file name (default `index.php`) and a text box: it writes the same content to a file name in every folder, or removes them. The text says *“if you used Massdelete please empty the text”*.
* **Upload** in two modes (`biasa` and `home_root`).
* **Command.** `exe()` runs a command with `system`, falling back to `exec`, `passthru` and the other functions if one is disabled.
* **Symlink, Jumping, Auto edit user, Config.** Labels in the menu. In shells of this type they are used on shared hosting to link other accounts’ files into the web root and read their config files. I did not trace this file’s code for them, so I am only reporting the labels.
* **Adminer** and a `gzinflate` call for a compressed extra.
* **Logout.** A function that drops a session value named `md5(...)`. There is no login screen.

## Detection & Cleanup[#](#detection--cleanup)

```
# strings from this file
grep -rlF -e 'PHP File Manager Mini' -e 'Multimass' .
```

* Mass operations leave a pattern: the same file (often `index.php`) with the same new content in many folders. `find . -name index.php -newer <date> -exec sha256sum {} + | sort | uniq -c -w64 | sort -rn | head` shows one hash repeated across folders.
* The goto layout is searchable: `grep -rlE '^<\?php goto [A-Za-z0-9_]{5};' --include='*.php' .`.

## IOCs[#](#iocs)

```
File      80ea2acac7f1af0cc3ebaaba656224c8   53,271 bytes
sha256    e8eb5bddb7962ef2b71566cf3d757e8cc6057b048859bc59863bc69a9417f11c
md5       8363f2c63baf260d5941699d725ed982
Strings   "PHP File Manager Mini"   '<?php goto gULgC;'   massdeface   massdelete   Multimass   "Auto edit user"
```

---

[[A Den1xxx File Manager Dressed as WordPress XML-RPC] >](https://lukeleal.com/research/posts/den1xxx-filemanager-wp-xmlrpc-costume/)

© 2026 Luke Leal

Disclaimer: The research posted on this website is for information purposes only. Do not use it for illegal purposes.