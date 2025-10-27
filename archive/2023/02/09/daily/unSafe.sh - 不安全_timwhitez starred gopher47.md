---
title: timwhitez starred gopher47
url: https://buaq.net/go-148517.html
source: unSafe.sh - 不安全
date: 2023-02-09
fetch_date: 2025-10-04T06:05:16.970822
---

# timwhitez starred gopher47

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/cd0170d20184ce6ef6480097bb5402bd.jpg)

timwhitez starred gopher47

A third-party Gopher Assassin for the Havoc Framework it's like the videogame
*2023-2-8 18:31:44
Author: [github.com(查看原文)](/jump-148517.htm)
阅读量:35
收藏*

---

> A third-party Gopher Assassin for the [Havoc](https://github.com/HavocFramework/Havoc) Framework

[![](https://github.com/An00bRektn/gopher47/raw/main/assets/gopher47.png)](https://github.com/An00bRektn/gopher47/blob/main/assets/gopher47.png)

it's like the videogame :D

## What is This? 🤔

This is a 3rd Party agent for the Havoc C2 written in Golang, mainly written as a learning project, but I'm sure it's still useful.

By the time this is out, you can read more about what and why this is at my blog: [here](https://notateamserver.xyz/havoc-implant/)

**Contributions welcome!** I don't plan on updating this all too regularly, but if I have fun making it I might add more stuff over time.

## Commands

| Command | Description | Example |
| --- | --- | --- |
| `checkin` | Returns basic system info | checkin |
| `shell` | Run a command (executed through Go's `os/exec`) | shell netstat -ano |
| `kill` | Kills a process by PID | kill 31337 |
| `ls` | Lists files in a given directory | ls C:\Users\Administrator\Desktop |
| `ps` | Lists currently running processes | ps |
| `upload` | Uploads a file to a remote path | upload /opt/chisel.exe C:\Windows\Temp\Bruh.exe |
| `download` | Downloads a remote file to the loot folder | download C:\passwords.txt pwd.txt |
| `portscan` | TCP portscan on a single target. | portscan common 192.168.13.37 4 |
| `shellcode` | Load shellcode into the implant process using `CreateThread` | shellcode 9090ccc3 |
| `execute-assembly` | Run .NET assemblies in memory | execute-assembly /opt/tools/Seatbelt.exe -group=user -q |
| `o7` | The gopher dies :( | o7 |

## Usage

Once you have your teamserver up, it's as simple as running the following:

* **Attacking Machine**: `python handler.py`
* **Target Machine**: `./gopher47`

You can use the Havoc GUI to compile it, or you can just edit the source code as you please and play with the Makefile, there isn't that much of it.

## FAQ

### Why Go?

I just wanted to have an actual Golang project put together that I can [point to](https://i.kym-cdn.com/entries/icons/original/000/035/627/cover2.jpg). But also, Golang is great for cross-compilation, has a good development ecosystem, and is much easier to write in than C/C++.

### Will it evade AV/EDR?

idk, but grow up. Obfuscate and customize it yourself, stop being a baby.

### Why's the binary so large though?

Golang, along with Rust and other languages, compile **statically**, meaning all of the libraries necessary to run the executable are baked into the binary, which adds up. If you want to reduce the size, I won't do it by default, but check out [this link](https://github.com/xaionaro/documentation/blob/master/golang/reduce-binary-size.md) for some tips. **UPDATE**: I added an option to do some of this, but I'm sure there's more customization you could do :/

### Can I run multiple Gophers?

For now, not really. The current Havoc API only allows for one handler to be handled by one agent, and there really isn't a good, clean way to have multiple up at the same time. Reworks are in-progress but for now, there can only be one Gopher47.

### Is the communication encrypted?

No. As of version 0.4 of Havoc, there is no way to do a secure key exchange without straight up compromising keys. Once the system is reworked in the havoc-py interface, I will get that done. **THEREFORE THIS IS NOT OPSEC SAFE** please do not be stupid and use this in a real engagement, CTFs/labs are fine though

HTTPS will provide encryption, but use at your own risk.

### How's your day going?

I photoshopped a gun into the Golang gopher's hand for this at 1:00 AM.

## Acknowledgements/References/Related Work

* [C5pider](https://github.com/Cracked5pider) and the entire [Havoc Framework](https://github.com/HavocFramework) team for letting me not have to write my own C2 to do some implant development
* [Sliver](https://github.com/BishopFox/sliver) and [Merlin](https://github.com/Ne0nd0g/merlin) for pioneering (or at least innovating) a lot of Offensive Golang
* [SharpAgent](https://github.com/susMdT/SharpAgent/) and [PyHmmm](https://github.com/CodeXTF2/PyHmmm) were great ~~projects to steal from~~ reference material
* [OffensiveGolang](https://github.com/bluesentinelsec/OffensiveGoLang) has some neat Offensive Go work
* [Ne0nd0g's fork](https://github.com/Ne0nd0g/go-clr) of [go-clr](https://github.com/ropnop/go-clr)
* [maldev-for-dummies](https://github.com/chvancooten/maldev-for-dummies) also is a nice starting point for working with not C malware
  I definitely missed some but here's to trying o7

### Disclaimer

There is no way to make an offensive security relevant research tool and release it open source without the possibility of it falling into the wrong hands. This tool is only to be used for legal, ethical purposes including, but not limited to, research, security assessment, education.

TL;DR: Keep it legal y'all.

文章来源: https://github.com/An00bRektn/gopher47
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)