---
title: sherlock v0.16.2
url: https://kitploit.com/en/posts/github-sherlock-project-sherlock-v0162
source: Kitploit
date: 2026-09-10
fetch_date: 2026-09-11T06:51:43.404003
---

# sherlock v0.16.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/214/55eaa2dd9dda1c27ea704deb1d28c65952a3fa1d9d9691a0cfc8bc1f5d6eff0a.png)

New releaseSep 10, 2026

# sherlock v0.16.2

Hunt down social media accounts by username across social networks

Share

[![sherlock](https://assets.kitploit.com/production/public/readmes/214/3ef3383c34b9a4e01bd448ac7efb88fc4c6beab966382377cd96968ec07a56af.png)](https://sherlock-project.github.io/)

Hunt down social media accounts by username across [400+ social networks](https://sherlockproject.xyz/sites)

[Installation](https://sherlockproject.xyz/installation)
   •
[Usage](https://sherlockproject.xyz/usage)
   •
[Contributing](https://sherlockproject.xyz/contribute)

![demo](https://assets.kitploit.com/production/public/readmes/214/55eaa2dd9dda1c27ea704deb1d28c65952a3fa1d9d9691a0cfc8bc1f5d6eff0a.png)

## Installation

[![OSINTSearch](https://raw.githubusercontent.com/sherlock-project/sherlock/master/docs/images/osintsearch.jpg)](https://osintsearch.org/go/sherlock-readme)
[![User Search](https://raw.githubusercontent.com/sherlock-project/sherlock/master/docs/images/usersearch.png)](https://usersearch.com/?utm_source=github&utm_medium=referral&utm_campaign=sherlock&utm_content=banner_install)
[![OSINT Industries](https://raw.githubusercontent.com/sherlock-project/sherlock/master/docs/images/osint-industries.jpg)](https://www.osint.industries/)

> [!WARNING]
> Packages for ParrotOS and Ubuntu 24.04, maintained by a third party, appear to be **broken**.
> Users of these systems should defer to [`uv`](https://docs.astral.sh/uv/)/`pipx`/`pip` or Docker.

| Method | Notes |
| --- | --- |
| `pipx install sherlock-project` | `pip` or [`uv`](https://docs.astral.sh/uv/) may be used in place of `pipx` |
| `docker run -it --rm sherlock/sherlock` |  |
| `dnf install sherlock-project` |  |

Community-maintained packages are available for Debian (>= 13), Ubuntu (>= 22.10), Homebrew, Kali, and BlackArch. These packages are not directly supported or maintained by the Sherlock Project.

See all alternative installation methods [here](https://sherlockproject.xyz/installation).

## General usage

To search for only one user:

root@kitploit:~

```
sherlock user123
```

To search for more than one user:

root@kitploit:~

```
sherlock user1 user2 user3
```

Accounts found will be stored in an individual text file with the corresponding username (e.g `user123.txt`).

root@kitploit:~

```
$ sherlock --help
usage: sherlock [-h] [--version] [--verbose] [--folderoutput FOLDEROUTPUT] [--output OUTPUT] [--csv] [--xlsx] [--site SITE_NAME] [--proxy PROXY_URL] [--dump-response]
                [--json JSON_FILE] [--timeout TIMEOUT] [--print-all] [--print-found] [--no-color] [--browse] [--local] [--nsfw] [--txt] [--ignore-exclusions]
                USERNAMES [USERNAMES ...]

Sherlock: Find Usernames Across Social Networks (Version 0.16.0)

positional arguments:
  USERNAMES             One or more usernames to check with social networks. Check similar usernames using {?} (replace to '_', '-', '.').

options:
  -h, --help            show this help message and exit
  --version             Display version information and dependencies.
  --verbose, -v, -d, --debug
                        Display extra debugging information and metrics.
  --folderoutput FOLDEROUTPUT, -fo FOLDEROUTPUT
                        If using multiple usernames, the output of the results will be saved to this folder.
  --output OUTPUT, -o OUTPUT
                        If using single username, the output of the result will be saved to this file.
  --csv                 Create Comma-Separated Values (CSV) File.
  --xlsx                Create the standard file for the modern Microsoft Excel spreadsheet (xlsx).
  --site SITE_NAME      Limit analysis to just the listed sites. Add multiple options to specify more than one site.
  --proxy PROXY_URL, -p PROXY_URL
                        Make requests over a proxy. e.g. socks5://127.0.0.1:1080
  --dump-response       Dump the HTTP response to stdout for targeted debugging.
  --json JSON_FILE, -j JSON_FILE
                        Load data from a JSON file or an online, valid, JSON file. Upstream PR numbers also accepted.
  --timeout TIMEOUT     Time (in seconds) to wait for response to requests (Default: 60)
  --print-all           Output sites where the username was not found.
  --print-found         Output sites where the username was found (also if exported as file).
  --no-color            Don't color terminal output
  --browse, -b          Browse to all results on default browser.
  --local, -l           Force the use of the local data.json file.
  --nsfw                Include checking of NSFW sites from default list.
  --txt                 Enable creation of a txt file
  --ignore-exclusions   Ignore upstream exclusions (may return more false positives)
```

## Credits

Thank you to everyone who has contributed to Sherlock! ❤️

[![contributors](https://contrib.rocks/image?&columns=25&max=10000&&repo=sherlock-project/sherlock)](https://github.com/sherlock-project/sherlock/graphs/contributors)

## Star History

![Sherlock Project Star History Chart](https://api.star-history.com/svg?repos=sherlock-project/sherlock&type=Date)

## License

MIT © Sherlock Project
Creator - [Siddharth Dushantha](https://github.com/sdushantha)

[Read more](/en/tools/github/sherlock-project/sherlock?expand=1)

## Categories

[OSINT (Open Source Intelligence)](/en/categories/osint)[Phishing Tools](/en/categories/phishing-tools)[Reconnaissance](/en/categories/reconnaissance)[OSINT for Social Engineering](/en/categories/osint-social-engineering)[Impersonation Tools](/en/categories/impersonation-tools)[Forensics](/en/categories/forensics)[Information Gathering](/en/categories/information-gathering)[Phishing](/en/categories/phishing)[Digital Forensics](/en/categories/digital-forensics)[Penetration Testing](/en/categories/penetration-testing)[Social Engineering](/en/categories/social-engineering)[Threat Intelligence](/en/categories/threat-intelligence)[Email Harvesting](/en/categories/email-harvesting)[Red Teaming](/en/categories/red-teaming)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories