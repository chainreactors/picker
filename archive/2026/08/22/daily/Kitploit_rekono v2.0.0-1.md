---
title: rekono v2.0.0-1
url: https://kitploit.com/en/posts/github-pablosnt-rekono-200-1
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:05.299717
---

# rekono v2.0.0-1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/5580/1bba2f5c38af7d0bcc12796ed53eaddd07ef5721be6680a97a10b8cd7c515aa4.png)

New releaseAug 22, 2026

# rekono v2.0.0-1

Offensive security platform that automates attack surface discovery and vulnerability management

Share

[![](https://github.com/pablosnt/rekono/actions/workflows/unit-testing.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/unit-testing.yml)
[![](https://github.com/pablosnt/rekono/actions/workflows/desktop-ui.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/desktop-ui.yml)
[![](https://github.com/pablosnt/rekono/actions/workflows/security-sast.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/security-sast.yml)
[![](https://badgen.net/snyk/pablosnt/rekono?label=SCA&labelColor=black&icon=https://snyk.io/wp-content/uploads/patch-white.svg)](https://snyk.io/test/github/pablosnt/rekono)
[![](https://github.com/pablosnt/rekono/actions/workflows/security-secrets.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/security-secrets.yml)
[![](https://github.com/pablosnt/rekono/actions/workflows/security-containers.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/security-containers.yml)
[![](https://github.com/pablosnt/rekono/actions/workflows/code-style.yml/badge.svg)](https://github.com/pablosnt/rekono/actions/workflows/code-style.yml)
[![](https://img.shields.io/badge/Discord-Join-black?style=social&logo=discord)](https://discord.gg/Zyduu5C7M3)
[![](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/pablosnt)
[![Buy Me A Coffee](https://assets.kitploit.com/production/public/readmes/5580/a7e8174c892355a24fbaec083cbef385d097a0b488fd4823dbbb0061643bb5e2.png)](https://www.buymeacoffee.com/pablosnt)

# ![](https://assets.kitploit.com/production/public/readmes/5580/1bba2f5c38af7d0bcc12796ed53eaddd07ef5721be6680a97a10b8cd7c515aa4.png)

**Rekono** combines other hacking tools and its results to execute complete pentesting processes against a target in an automated way. The findings obtained during the executions will be sent to the user via email or Telegram notifications and also can be imported in [Defect-Dojo](https://www.defectdojo.com) if an advanced vulnerability management is needed. Moreover, Rekono includes a Telegram bot that can be used to perform executions easily from anywhere and using any device.

## Why Rekono?

Do you ever think about the steps that you follow when you start pentesting? Probably you start performing some OSINT tasks to gather public information about the target. Then, maybe you run hosts discovery and ports enumeration tools. When you know what the target exposes, you can execute more specific tools for each service, to get more information and maybe, some vulnerabilities. And finally, if you find the needed information, you will look for a public exploit to get you into the target machine. I know, I know, this is an utopic scenario, and in the most cases the vulnerabilities are found due to the pentester skills and not by scanning tools. But before using your skills, how many time do you spend trying to get as information as possible with hacking tools? Probably, too much.

Why not automate this process and focus on find vulnerabilities using your skills and the information that Rekono sends you?

> The `Rekono` name comes from the Esperanto language where it means *recon*.

## Demo

[![Rekono]](https://user-images.githubusercontent.com/69458381/211694917-6738e42a-cb44-4d3a-905d-752b3fe25718.mp4)

### Telegram Bot

[![Rekono Bot]](https://user-images.githubusercontent.com/69458381/211692042-d7c38e41-19e9-44fd-842a-59a16f945b6f.mp4)

## Quick Start

### Rekono Desktop

Rekono Desktop is a standalone app that can be easily installed and executed locally. Install it on **Kali Linux** with this command:

root@kitploit:~

```
apt install rekono-kbx
```

If you are using **Parrot OS**, you can download the Debian package from the Rekono release:

root@kitploit:~

```
wget https://github.com/pablosnt/rekono/releases/download/1.6.6/rekono-kbx_1.6.6_amd64.deb && dpkg -i rekono-kbx_1.6.6_amd64.deb || apt -f install -y
```

> Default credentials are `rekono:rekono`. For security reasons, **password should be changed** the first time you access the account

### Docker

Execute the following commands in the root directory of the project:

root@kitploit:~

```
docker-compose build
docker-compose up -d --scale executions-worker=5
```

Go to <https://127.0.0.1/>

> Default credentials are `rekono:rekono`. For security reasons, **password should be changed** the first time you access the account. Moreover default user details can be changed using [environment variables](https://github.com/pablosnt/rekono/wiki/Configuration#docker).

> The number of workers can be changed using `--scale` option. The number of `executions-worker` determines the number of tools that could be executed at the same time.

Check [**full documentation**](https://github.com/pablosnt/rekono/wiki) for more installation and configuration options, user guides, integrations, Rekono Desktop, Rekono Bot and Rekono CLI details.

## Hacking Tools

Rekono supports the execution of this hacking tools:

* [theHarvester](https://github.com/laramies/theHarvester)
* [EmailHarvester](https://github.com/maldevel/EmailHarvester)
* [EmailFinder](https://github.com/Josue87/EmailFinder)
* [Nmap](https://nmap.org/)
* [Sslscan](https://github.com/rbsec/sslscan)
* [SSLyze](https://nabla-c0d3.github.io/sslyze/documentation/)
* [SSH Audit](https://github.com/jtesta/ssh-audit)
* [SMBMap](https://github.com/ShawnDEvans/smbmap)
* [Dirsearch](https://github.com/maurosoria/dirsearch)
* [Gobuster](https://github.com/OJ/gobuster)
* [GitLeaks](https://github.com/zricethezav/gitleaks) & [GitDumper](https://github.com/internetwache/GitTools/tree/master/Dumper)
* [Log4j Scan](https://github.com/fullhunt/log4j-scan)
* [Spring4Shell Scan](https://github.com/fullhunt/spring4shell-scan)
* [CMSeeK](https://github.com/Tuhinshubhra/CMSeeK/)
* [OWASP JoomScan](https://github.com/OWASP/joomscan)
* [OWASP ZAP](https://www.zaproxy.org/)
* [Nikto](https://github.com/sullo/nikto)
* [Nuclei](https://github.com/projectdiscovery/nuclei)
* [SearchSploit](https://www.exploit-db.com/searchsploit)
* [Metasploit](https://www.metasploit.com/)

Thanks to all the contributors of these amazing tools!

## Reach Us

You can get support, ask questions, solve doubts or solve problems using:

[![](https://assets.kitploit.com/production/public/readmes/5580/1bedd6a1948971f07970414717012503805309f25af0b2c542dbc3524b5880e9.png)](https://github.com/pablosnt/rekono/issues/new?labels=help+wanted%2C+question&template=support.md)
[![](https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a69f118df70ad7828d4_icon_clyde_blurple_RGB.svg)](https://discord.gg/Zyduu5C7M3)
[![](https://assets.kitploit.com/production/public/readmes/5580/6e5d789c6e09c2368d00157c004c764dbc9f6be0119eca9668eb6198b15d49b0.png)](/cdn-cgi/l/email-protection#a9dbccc2c6c7c687d9dbc6c3cccadde9cec4c8c0c587cac6c4)

Rekono is an open source project that we really love to maintain and it's absolutely our pleasure, but we would like to offer the possibility of supporting Rekono's development via donations. At the moment, the project only needs its maintainer's time to stay up to date with new features and fix bugs. However, in the future, it could need more expensive resources like hosting, new web pages for documentation, the inclusion of premium hacking tools, etc. With the help received from our supporters, Rekono will be able to grow fastly and ha...