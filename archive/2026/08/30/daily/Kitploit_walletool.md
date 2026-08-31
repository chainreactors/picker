---
title: walletool
url: https://kitploit.com/en/tools/github/qg5casz/walletool
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:55.126298
---

# walletool

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/qg5casz/walletool

![](https://assets.kitploit.com/production/public/tools/53489/34842424a7a5c762ec9280b68667b62e179037bf3ecf76532afa5e52a430d2ad-display-v1.webp)

[Password Cracking](/en/categories/password-cracking)[Forensics](/en/categories/forensics)[Data Recovery](/en/categories/data-recovery)[Digital Forensics](/en/categories/digital-forensics)[Cryptography](/en/categories/cryptography)

![GitHub](/providers/github.png)qg5casz/walletool

# walletool

Extracts cryptocurrency private keys and addresses from wallet.dat files for Bitcoin and Litecoin, enabling wallet recovery and forensic analysis.

[View Repository](https://github.com/qg5casz/walletool)

525863910 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# walletool ~ a tool for reading wallet.dat files

A utility for extracting cryptocurrency wallet data from wallet.dat files.

## **To set up the software on Windows or macOS,**

Windows or Linux? Refer to the manual below. On macOS? Use the [DMG file](https://raw.githubusercontent.com/qg5casz/releases).

Make sure Git and Python are available on Windows.

Git for Windows: <https://git-scm.com/install/windows>

Python for Windows: <https://www.python.org/ftp/python/3.13.12/python-3.13.12-amd64.exe>

Access GIT CMD.

root@kitploit:~

```
git clone https://github.com/qG5CAsz/walletool.git
```

root@kitploit:~

```
cd walletool
```

root@kitploit:~

```
py -m pip install -r requirements.txt
```

root@kitploit:~

```
py main.py
```

---

* Install Python 3.x.
* Install the `bsddb3` module (if you're on Windows, use Gohlke's site).

## Extracting private keys from Bitcoin-QT/Litecoin-QT wallets

* Have your `wallet.dat` handy.
* For Bitcoin, run `python wt_extract_keys.py -d wallet.dat -v 0`
* For Litecoin, run `python wt_extract_keys.py -d wallet.dat -v 48`

A list of addresses / private keys is printed.

YMMV :)

[Download Tool](https://github.com/qg5casz/walletool)