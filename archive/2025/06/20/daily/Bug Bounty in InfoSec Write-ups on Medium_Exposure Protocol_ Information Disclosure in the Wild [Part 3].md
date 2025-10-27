---
title: Exposure Protocol: Information Disclosure in the Wild [Part 3]
url: https://infosecwriteups.com/exposure-protocol-information-disclosure-in-the-wild-part-3-2bea07098768?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-06-20
fetch_date: 2025-10-06T22:51:57.283822
---

# Exposure Protocol: Information Disclosure in the Wild [Part 3]

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F2bea07098768&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposure-protocol-information-disclosure-in-the-wild-part-3-2bea07098768&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fexposure-protocol-information-disclosure-in-the-wild-part-3-2bea07098768&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-2bea07098768---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-2bea07098768---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Exposure Protocol: Information Disclosure in the Wild [Part 3]

## Source Code Disclosure via Backup Files — Hunting Sensitive Data Left in the Wild 🔍🗃️

[![Aditya Bhatt](https://miro.medium.com/v2/resize:fill:64:64/1*6TFmlC58KtmaRsYHdjy9Qg.jpeg)](https://medium.com/%40adityabhatt3010?source=post_page---byline--2bea07098768---------------------------------------)

[Aditya Bhatt](https://medium.com/%40adityabhatt3010?source=post_page---byline--2bea07098768---------------------------------------)

6 min read

·

Jun 18, 2025

--

Listen

Share

> *“Sometimes, the juiciest secrets aren’t hidden — they’re just… forgotten.”
> ~ Aditya Bhatt, Source Code Archaeologist 🕵️‍♂️*

## 📌 Preface

Welcome back to Exposure Protocol, a series diving deep into real-world Information Disclosure bugs that often get overlooked — until someone smart enough pokes in the right place.

In [Part 1](/exposure-protocol-information-disclosure-in-the-wild-part-1-588de47882b1), we exploited a verbose error message that leaked the Apache Struts version, laying the groundwork for CVE-based exploitation. → 🛠️ PoC: [GitHub — When Servers Overshare](https://github.com/AdityaBhatt3010/When-Servers-Overshare-Information-disclosure-in-error-messages)

[Part 2](/exposure-protocol-information-disclosure-in-the-wild-part-2-e6f4f9e21584) raised the stakes with a misconfigured debug page — exposing the `SECRET_KEY`, a treasure trove for session forgery or further lateral movement. → 🛠️ PoC: [GitHub - SECRET\_KEY Exposed](https://github.com/AdityaBhatt3010/Information-Disclosure-on-Debug-Page-SECRET_KEY-Exposed)

Now in Part 3, we go hunting for neglected backup files — `.bak`, `.zip`, `.old` — tucked away in a `/backup` directory revealed through `robots.txt`. What did we find? The hard-coded Postgres DB credentials inside a leaked Java source file. Proof once again that content discovery + lazy devs = bounty gold.

💡 Key themes:

* Recon magic with `robots.txt`
* Backup file enumeration
* Automated extraction of secrets from source dumps

🧰 PoC for this article: [GitHub — Source Code Disclosure via Backup Files](https://github.com/AdityaBhatt3010/Source-Code-Disclosure-via-Backup-Files) 📚 Full Series: [Medium Playlist](https://medium.com/%40adityabhatt3010/list/exposure-protocol-information-disclosure-in-the-wild-55842309767d)

Press enter or click to view image in full size

![]()

## Introduction

Information disclosure vulnerabilities remain a frequent and critical issue in web security. One surprisingly common mistake developers make is unintentionally exposing sensitive files — like source code backups or configuration files — in publicly accessible directories. These exposures can leak hard-coded credentials, API keys, or other secrets, instantly turning a simple app into an easy target 🎯.

In this write-up, I walk through a practical example from a recent BurpSuite lab focused on Source Code Disclosure via Backup Files — a classic yet often overlooked vulnerability that can yield high-impact rewards in bug bounty programs 💰.

Press enter or click to view image in full size

![]()

## Lab Overview: Source Code Disclosure via Backup Files

The lab simulates a real-world scenario where a web application leaks its source code through backup files stored in a hidden directory. The goal is to discover and retrieve a hard-coded database password embedded inside the leaked source code 🔐.

## Step-by-Step Walkthrough

## 1. Access the Lab

Navigate to the lab URL: <https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files> 🌐.

Press enter or click to view image in full size

![]()

## 2. Check robots.txt for Clues

Open `/robots.txt` to see if any disallowed paths might hint at hidden directories. The file reveals a `/backup` directory—a potential goldmine for leftover files 🗂️.

Press enter or click to view image in full size

![]()

## 3. Explore the `/backup` Directory

Browsing to `/backup` lists available files, including `ProductTemplate.java.bak`. This is clearly a backup file, potentially containing sensitive source code 🧾.

Press enter or click to view image in full size

![]()

## 4. Inspect the Backup Source Code

Opening `/backup/ProductTemplate.java.bak` reveals the entire Java source file. Scanning through the code, we spot a connection builder with a hard-coded Postgres database password. This careless developer left the keys to the kingdom right in the code—likely a result of rushed work or overlooked cleanup 🔑.

> “Click on weird links to get weird bounties” — Aditya Bhatt 🗿 *Just kidding, but sometimes it really is that simple 😅.*

Press enter or click to view image in full size

![]()

## 5. Submit the Extracted Password

Copy the discovered password and submit it via the lab’s solution interface ✅.

Press enter or click to view image in full size

![]()

## 6. Lab Solved!

**Success! 🎉**

The lab confirms the vulnerability exploitation, demonstrating the risks of leaving backup files accessible in production environments.

Press enter or click to view image in full size

![]()

## Source Code

You can simply clone the script from [My GitHub](https://github.com/AdityaBhatt3010/Source-Code-Disclosure-via-Backup-Files/blob/main/SourceCode.py) 😉.

```
import requests
import re
from bs4 import BeautifulSoup

# Replace with the lab URL base
BASE_URL = "https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files"

def get_robots_txt(url):
    r = requests.get(f"{url}/robots.txt")
    if r.status_code == 200:
        return r.text
    return ""

def find_backup_path(robots_txt):
    # Simple regex to find disallowed paths
    matches = re.findall(r'Disallow: (/.+)', robots_txt)
    for path in matches:
        if "backup" in path.lower():
            return path
    return None

def fetch_backup_file(url, backup_path, filename):
    full_url = f"{url}{backup_path}/{filename}"
   ...