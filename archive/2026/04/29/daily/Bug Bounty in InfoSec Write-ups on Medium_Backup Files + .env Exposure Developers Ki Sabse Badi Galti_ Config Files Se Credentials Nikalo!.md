---
title: Backup Files + .env Exposure Developers Ki Sabse Badi Galti: Config Files Se Credentials Nikalo!
url: https://infosecwriteups.com/backup-files-env-exposure-developers-ki-sabse-badi-galti-config-files-se-credentials-nikalo-1432674639b8?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-04-29
fetch_date: 2026-04-30T05:28:58.428128
---

# Backup Files + .env Exposure Developers Ki Sabse Badi Galti: Config Files Se Credentials Nikalo!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbackup-files-env-exposure-developers-ki-sabse-badi-galti-config-files-se-credentials-nikalo-1432674639b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbackup-files-env-exposure-developers-ki-sabse-badi-galti-config-files-se-credentials-nikalo-1432674639b8&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1432674639b8---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1432674639b8---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# Backup Files + .env Exposure Developers Ki Sabse Badi Galti: Config Files Se Credentials Nikalo! (Hinglish Mein)

[![Hacker MD](https://miro.medium.com/v2/resize:fill:64:64/1*mArHieH3GY7HX9TX7ZAoIg.jpeg)](https://medium.com/%40HackerMD?source=post_page---byline--1432674639b8---------------------------------------)

[Hacker MD](https://medium.com/%40HackerMD?source=post_page---byline--1432674639b8---------------------------------------)

7 min read

·

Apr 23, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D1432674639b8&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbackup-files-env-exposure-developers-ki-sabse-badi-galti-config-files-se-credentials-nikalo-1432674639b8&source=---header_actions--1432674639b8---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**Series: Bug Bounty Zero se Hero 🦸 | Article #21**
*By HackerMD | 17 min read*

## Aaj Kya Seekhenge?

* Backup files exposure kya hai basics se
* .env, .git, config files sabhi types
* Kahan dhundhen complete checklist
* Automated tools Dirsearch, Feroxbuster, Nuclei
* .git exposure source code nikalo
* Real exploitation credentials se aage
* Complete bug bounty workflow

> **Kyun zaroori hai?** Yeh **sabse easy Critical bugs** hain bug bounty mein! Koi fancy technique nahi sirf URL mein `.env` lagao aur dekho! Developers test mein files upload karte hain production mein wahi rehta hai **database passwords, API keys, AWS credentials sab exposed!** Bounty: **$500 se $10,000+**

## Yeh Kaise Hota Hai? Simple Story

```
Ek developer hai — Rahul।

Step 1: Local machine pe .env banaya:
DB_HOST=localhost
DB_PASSWORD=SuperSecret123
AWS_KEY=AKIA...

Step 2: Code deploy kiya server pe:
git push → Server pe sab files gayi!
.env bhi chali gayi! 😱

Step 3: Web server publicly serve kar raha hai:
https://company.com/.env
→ Browser mein open karo → Poori file! 🔴

Rahul ko pata bhi nahi!
```

**Yahi hai Backup/Config File Exposure!**

## PART 1: File Types Sabhi Samjho

## Type 1: .env Files GOLDMINE!

```
# .env file mein kya hota hai:
APP_NAME=MyApp
APP_ENV=production
APP_DEBUG=true           ← Debug mode on!
APP_KEY=base64:abc123... ← Laravel secret key!

DB_CONNECTION=mysql
DB_HOST=db.internal.company.com
DB_PORT=3306
DB_DATABASE=production_db
DB_USERNAME=root
DB_PASSWORD=SuperSecret@123  ← Database password! 🔴

REDIS_PASSWORD=redis123

MAIL_USERNAME=noreply@company.com
MAIL_PASSWORD=mailpass123    ← Email credentials!

AWS_ACCESS_KEY_ID=AKIAIOSFODNN7
AWS_SECRET_ACCESS_KEY=abc123xyz  ← AWS Keys! 🔴

STRIPE_SECRET=sk_live_abc123    ← Payment keys!
STRIPE_PUBLISHABLE=pk_live_abc

TWILIO_SID=ACxxx
TWILIO_TOKEN=abc123

GITHUB_TOKEN=ghp_abc123    ← GitHub access!

# Ek file mein poori company ki secrets! 💀
```

## Type 2: .git Directory Exposure

```
.git folder = Poora source code history!

https://target.com/.git/
→ Git repository accessible!
→ Source code download kar sakte hain!
→ Commit history mein old passwords!
→ Developer emails!
→ Internal URLs!
→ Hardcoded credentials!
```

## Type 3: Backup Files

```
Common backup extensions:
.bak → filename.php.bak
.old → config.php.old
.orig → settings.orig
.backup → database.backup
.copy → config.copy
.tmp → upload.tmp
.swp → vim swap file (index.php.swp)
~   → index.php~ (text editor backup)

Example:
https://target.com/config.php.bak  → Source code!
https://target.com/wp-config.php~  → WordPress DB pass!
```

## Type 4: Config Files

```
# PHP configs:
config.php, configuration.php, settings.php
database.php, db.php, conn.php, connect.php

# Web server configs:
.htaccess, .htpasswd  ← Basic auth credentials!
web.config            ← .NET connection strings!
nginx.conf, apache.conf

# Application configs:
config.yml, config.yaml
config.json, settings.json
appsettings.json      ← .NET secrets!
application.properties ← Java/Spring!
secrets.yml

# Database files:
dump.sql, backup.sql
database.sql, db.sql
*.sqlite, *.db
```

## Type 5: Log Files

```
# Log files kya expose karte hain:
error.log      → Stack traces, file paths, internal IPs
access.log     → All user requests, session IDs!
debug.log      → Verbose app information
application.log → Business logic, user data

URLs:
/logs/error.log
/log/debug.log
/var/log/app.log
/logs/
```

## Type 6: IDE / Editor Files

```
.DS_Store     → Mac folder structure expose!
.idea/        → IntelliJ project files
.vscode/      → VS Code settings
*.swp         → Vim swap files (source code!)
.project      → Eclipse project
thumbs.db     → Windows thumbnail DB
```

## PART 2: Kahan Dhundhen Complete URL Checklist

```
# ─── .ENV FILES ───────────────────────────
/.env
/.env.local
/.env.development
/.env.production
/.env.staging
/.env.backup
/.env.old
/.env.example    ← Sometimes real values!
/.env.bak
/api/.env
/backend/.env
/app/.env
/src/.env

# ─── GIT DIRECTORY ────────────────────────
/.git/
/.git/config     ← Remote URLs!
/.git/HEAD
/.git/COMMIT_EDITMSG
/.git/logs/HEAD  ← Commit history!
/.git/refs/heads/master

# ─── CONFIG FILES ─────────────────────────
/config.php
/config/database.php
/wp-config.php       ← WordPress!
/configuration.php   ← Joomla!
/settings.py         ← Django!
/appsettings.json    ← .NET!
/application.properties ← Spring!
/config/config.yml
/config/secrets.yml

# ─── BACKUP FILES ─────────────────────────
/backup/
/backups/
/backup.sql
/dump.sql
/database.sql
/db.sql
/backup.zip
/site.tar.gz
/www.tar.gz

# ─── LOG FILES ────────────────────────────
/logs/
/log/
/error.log
/debug.log
/access.log
/application.log
/laravel.log        ← Laravel!
/storage/logs/      ← Laravel storage!

# ─── HTPASSWD ─────────────────────────────
/.htpasswd
/.htaccess
/admin/.htpasswd
```

## PART 3: Automated Tools Elite Use

## Tool 1: Dirsearch Best Directory Bruteforcer

```
# Install karo
pip3 install dirsearch

# Basic scan — sensitive files ke liye
dirsearch -u htt...