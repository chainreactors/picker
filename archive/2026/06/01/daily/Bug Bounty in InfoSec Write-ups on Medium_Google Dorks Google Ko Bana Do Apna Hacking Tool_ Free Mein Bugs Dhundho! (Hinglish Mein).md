---
title: Google Dorks Google Ko Bana Do Apna Hacking Tool: Free Mein Bugs Dhundho! (Hinglish Mein)
url: https://infosecwriteups.com/google-dorks-google-ko-bana-do-apna-hacking-tool-free-mein-bugs-dhundho-hinglish-mein-287c3a7ffc75?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-01
fetch_date: 2026-06-02T06:31:19.706961
---

# Google Dorks Google Ko Bana Do Apna Hacking Tool: Free Mein Bugs Dhundho! (Hinglish Mein)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-dorks-google-ko-bana-do-apna-hacking-tool-free-mein-bugs-dhundho-hinglish-mein-287c3a7ffc75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-dorks-google-ko-bana-do-apna-hacking-tool-free-mein-bugs-dhundho-hinglish-mein-287c3a7ffc75&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-287c3a7ffc75---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-287c3a7ffc75---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Google Dorks Google Ko Bana Do Apna Hacking Tool: Free Mein Bugs Dhundho! (Hinglish Mein)

[![Hacker MD](https://miro.medium.com/v2/resize:fill:64:64/1*mArHieH3GY7HX9TX7ZAoIg.jpeg)](https://medium.com/%40HackerMD?source=post_page---byline--287c3a7ffc75---------------------------------------)

[Hacker MD](https://medium.com/%40HackerMD?source=post_page---byline--287c3a7ffc75---------------------------------------)

7 min read

·

Apr 13, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D287c3a7ffc75&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgoogle-dorks-google-ko-bana-do-apna-hacking-tool-free-mein-bugs-dhundho-hinglish-mein-287c3a7ffc75&source=---header_actions--287c3a7ffc75---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**Series: Bug Bounty Zero se Hero 🦸 | Article #11**
*By HackerMD | 17 min read*

## Aaj Kya Seekhenge?

* Google Dorks kya hai bilkul basics se
* Kaise kaam karta hai Google index ki power
* Sabhi operators ek ek deeply
* Bug bounty ke liye best dorks
* Sensitive files, admin panels, exposed configs
* GHDB Google Hacking Database
* Elite automated dorking workflow

**Kyun zaroori hai?** Shodan aur Censys ke liye API key chahiye **Google Dorks bilkul FREE hai!** Aur Google itna powerful crawler hai ki usne woh cheezein index kar rakhi hain jo companies **kabhi public nahi karna chahti thin!** Exposed config files, database backups, passwords sab Google pe mil jaata hai!

## Google Dorks Kya Hai? Simple Analogy

Normal Google search:

```
"best restaurants in Mumbai"
→ Restaurant websites milti hain
```

Google Dork:

```
site:company.com filetype:sql
→ Company ka database backup publicly accessible! 😱

site:company.com inurl:admin intitle:"Login"
→ Admin panel Google mein indexed! 🎯

site:company.com ext:env "DB_PASSWORD"
→ .env file mein password exposed! 🔴
```

**Dork = Specially crafted Google search query jo sensitive information expose karta hai!**

## Yeh Kaise Possible Hai?

Samjho ek story se:

Ek developer ne `config.php` file accidentally **public folder** mein upload kar di usme database password tha।

Developer ko pata bhi nahi chala।

**Google ka crawler aaya → File index ho gayi → 3 din baad Google pe searchable!**

Tum dork lagate ho:

```
site:company.com filetype:php "db_password"
```

**Result: Database password seedha Google search mein!** 🔴

## Get Hacker MD’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Yahi Google Dorks ka power hai **Google ne pehle se kar rakha hai kaam!**

## PART 1: Core Operators Sab Samjho

## Operator 1: `site:` Domain Pe Focus Karo

```
site:example.com
→ Sirf example.com ke pages

site:example.com login
→ example.com pe login pages

site:*.example.com
→ Sabhi subdomains ke pages

# Bug bounty use:
site:target.com
# Pehle dekho kitne pages indexed hain
# Interesting patterns dhundho
```

## Operator 2: `inurl:` URL Mein Kya Hai?

```
inurl:admin
→ URL mein "admin" wale pagesinurl:login site:target.com
→ target.com ke login pagesinurl:dashboard site:target.com
→ Dashboards!inurl:api/v1 site:target.com
→ API endpoints!inurl:.php?id= site:target.com
→ Possible SQL injection points! 🎯
```

## Operator 3: `intitle:` Page Title Mein Kya Hai?

```
intitle:"Admin Panel" site:target.com
intitle:"phpMyAdmin" site:target.com
intitle:"Dashboard" site:target.com
intitle:"Index of" site:target.com
→ Directory listing exposed! 🎯

intitle:"Grafana" site:target.com
intitle:"Jenkins" site:target.com
```

## Operator 4: `filetype:` / `ext:` File Type Filter

```
filetype:pdf site:target.com
→ PDF documents — internal docs?

filetype:sql site:target.com
→ Database backup files! 🔴

filetype:log site:target.com
→ Log files — usernames, errors!

ext:env site:target.com
→ .env files — passwords! 🔴

ext:xml site:target.com
→ XML config files

ext:bak site:target.com
→ Backup files! 🎯

ext:conf site:target.com
→ Config files!

ext:txt site:target.com
→ Text files — sometimes sensitive

ext:json site:target.com "api_key"
→ JSON mein API keys! 🔴
```

## Operator 5: `intext:` Page Content Mein Dhundho

```
intext:"password" filetype:log site:target.com
→ Log file mein password!

intext:"api_key" site:target.com
→ Page mein API key exposed!

intext:"DB_PASSWORD" site:target.com
→ Database password in page content!

intext:"BEGIN RSA PRIVATE KEY" site:target.com
→ Private key exposed! 🔴 Critical!
```

## Operator 6: `allinurl:` aur `allintitle:`

```
allinurl:admin login panel
→ URL mein teeno words honge

allintitle:admin login dashboard site:target.com
→ Title mein teeno words
```

## Operator 7: `-`Exclude Karo

```
site:target.com -www
→ www chhod ke baaki subdomains

site:target.com filetype:php -inurl:index
→ Index.php chhod ke baaki PHP files
```

## Operator 8: `"`Exact Match

```
"Index of /backup" site:target.com
→ Exact string match — backup directory!

"ORA-01756" site:target.com
→ Oracle SQL error — SQL injection clue!

"Warning: mysql_fetch" site:target.com
→ MySQL error — database info leak!
```

## Operator 9: `OR` Multiple Options

```
site:target.com (ext:env OR ext:cfg OR ext:conf)
→ Koi bhi config file!

(inurl:admin OR inurl:administrator OR inurl:panel) site:target.com
```

## Operator 10: `*` Wildcard

```
site:*.target.com
→ Sabhi subdomains!

"api_key = *" site:target.com
→ API key pattern dhundho
```

## PART 2: Bug Bounty Ke Liye Best Dorks Category Wise

## Category 1: Exposed Sensitive Files

```
# Environment files — GOLDMINE!
site:target.com ext:env
site:target.com "DB_PASSWORD"
site:target.com "APP_SECRET"
site:target.com ".env" "DB_HOST"

# Config files
site:target.com ext:conf "password"
site:target.com ext:cfg "password"
site:target.com filetype:xml "password"
site:target.com ext:ini "password"

# Database files
site:target.com ext:sql
...