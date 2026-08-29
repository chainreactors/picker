---
title: malvinci
url: https://kitploit.com/en/tools/github/gsoffmarket/malvinci
source: Kitploit
date: 2026-08-28
fetch_date: 2026-08-29T08:30:58.524961
---

# malvinci

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

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/gsoffmarket/malvinci

![](https://assets.kitploit.com/production/public/tools/53456/44f5a1feedc55e0a8511186366be0ab0d13d6dcf6c46342a09bbc3c5f88b4447-display-v1.webp)

[Persistence Mechanisms](/en/categories/persistence-mechanisms)[Data Exfiltration](/en/categories/data-exfiltration)[Command and Control](/en/categories/command-and-control)[Red Teaming](/en/categories/red-teaming)[Payload Development](/en/categories/payload-development)[Remote Access Trojan](/en/categories/remote-access-trojan)

![GitHub](/providers/github.png)gsoffmarket/malvinci

# malvinci

This simple but powerful script will introduce a new type of malware that will turn off the firewall, start an HTTP server, forward its port through ngrok, and send the URL of the server through a Telegram bot.

[View Repository](https://github.com/gsoffmarket/malvinci)

595211 year ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# malvinci

This simple script will introduce a new type of malware that will turn off the firewall, start an HTTP server, forward its port through ngrok, and send the URL of the server through a Telegram bot.

You will need to create a new Telegram BOT. [Follow the steps](https://core.telegram.org/bots#6-botfather) the steps here to create one⚡

# How to setup

Before running this program edit the payload.py file

* Replace "botttoken" with your Telegram Bot API key.
* Replace "chatid" with your Telegram Bot's Chat ID.

## How To Use

root@kitploit:~

```
# Install dependencies
$ python3 , pip
$ py -3 -m pip install -r requirements.txt
# in order to change the drive you accesing use this parameter change_drive?drive=$Drive

# Building the payload

$ Replace the bot token And Chatid Cred in the file
$ Now compile the payload code using pyinstaller
$ pyinstaller --noconfirm --onefile --windowed   payload.py
```

[Download Tool](https://github.com/gsoffmarket/malvinci)