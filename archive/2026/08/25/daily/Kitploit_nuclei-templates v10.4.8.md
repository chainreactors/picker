---
title: nuclei-templates v10.4.8
url: https://kitploit.com/en/posts/github-projectdiscovery-nuclei-templates-v1048
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:09.135983
---

# nuclei-templates v10.4.8

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/41123/98d53b9c4b7403a0defa801e64b2b374878de9ff3c58612aa1107e4c1fc28411.png)

New releaseAug 25, 2026

# nuclei-templates v10.4.8

Community curated list of templates for the nuclei engine to find security vulnerabilities.

Share

# Nuclei Templates

#### Community curated list of templates for the nuclei engine to find security vulnerabilities in applications.

[![](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/projectdiscovery/nuclei-templates/issues)
[![](https://img.shields.io/github/release/projectdiscovery/nuclei-templates)](https://github.com/projectdiscovery/nuclei-templates/releases)
[![](https://img.shields.io/twitter/follow/pdnuclei.svg?logo=twitter)](https://twitter.com/pdnuclei)
[![](https://img.shields.io/discord/695645237418131507.svg?logo=discord)](https://discord.gg/projectdiscovery)

[Documentation](https://docs.projectdiscovery.io/templates/introduction) •
[Contributions](#-contributions) •
[Discussion](#-discussion) •
[Community](#-community) •
[FAQs](https://docs.projectdiscovery.io/templates/faq) •
[Join Discord](https://discord.gg/projectdiscovery)

---

Templates are the core of the [nuclei scanner](https://github.com/projectdiscovery/nuclei) which powers the actual scanning engine.
This repository stores and houses various templates for the scanner provided by our team, as well as contributed by the community.
We hope that you also contribute by sending templates via **pull requests** or [Github issues](https://github.com/projectdiscovery/nuclei-templates/issues/new?assignees=&labels=&template=submit-template.md&title=%5Bnuclei-template%5D+) to grow the list.

## Nuclei Templates overview

An overview of the nuclei template project, including statistics on unique tags, author, directory, severity, and type of templates. The table below contains the top ten statistics for each matrix; an expanded version of this is [available here](https://github.com/projectdiscovery/nuclei-templates/blob/HEAD/TEMPLATES-STATS.md), and also available in [JSON](https://github.com/projectdiscovery/nuclei-templates/blob/HEAD/TEMPLATES-STATS.json) format for integration.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 🚨 Known Exploited Vulnerabilities (KEV) Coverage Nuclei templates provide coverage for vulnerabilities actively exploited in the wild:  | **KEV Source** | **Templates** | **Description** | | --- | --- | --- | | 🔴 **CISA KEV** | **454** | [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | | 🟠 **VulnCheck KEV** | **1449** | [VulnCheck KEV](https://vulncheck.com/kev) - Enhanced vulnerability intelligence | | 🟢 **Both Sources** | **407** | Templates covering vulnerabilities in both catalogs |  💡 **Total unique KEV templates: 1496** - Use `nuclei -tags kev,vkev` to scan for actively exploited vulnerabilities   ---  Nuclei Templates Top 10 statistics | TAG | COUNT | AUTHOR | COUNT | DIRECTORY | COUNT | SEVERITY | COUNT | TYPE | COUNT | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | vuln | 6468 | dhiyaneshdk | 1894 | http | 9281 | info | 4353 | file | 436 | | cve | 3587 | daffainfo | 905 | cloud | 659 | high | 2552 | dns | 26 | | discovery | 3265 | princechaddha | 854 | file | 436 | medium | 2457 |  |  | | vkev | 1394 | dwisiswant0 | 805 | network | 259 | critical | 1555 |  |  | | panel | 1365 | ritikchaddha | 678 | code | 251 | low | 330 |  |  | | xss | 1269 | pussycat0x | 675 | dast | 240 | unknown | 54 |  |  | | wordpress | 1261 | pikpikcu | 353 | workflows | 205 |  |  |  |  | | exposure | 1141 | pdteam | 314 | javascript | 92 |  |  |  |  | | wp-plugin | 1103 | pdresearch | 275 | ssl | 38 |  |  |  |  | | osint | 848 | iamnoooob | 263 | dns | 23 |  |  |  |  |  **873 directories, 11997 files**. |

## 📖 Documentation

Please navigate to <https://nuclei.projectdiscovery.io> for detailed documentation to **build** new or your own **custom** templates.
We have also added a set of templates to help you understand how things work.

## 💪 Contributions

Nuclei-templates is powered by major contributions from the community.
[Template contributions](https://github.com/projectdiscovery/nuclei-templates/issues/new?assignees=&labels=&template=submit-template.md&title=%5Bnuclei-template%5D+) , [Feature Requests](https://github.com/projectdiscovery/nuclei-templates/issues/new?assignees=&labels=&template=feature_request.md&title=%5BFeature%5D+) and [Bug Reports](https://github.com/projectdiscovery/nuclei-templates/issues/new?assignees=&labels=&template=bug_report.md&title=%5BBug%5D+) are more than welcome.

![Alt](https://repobeats.axiom.co/api/embed/55ee65543bb9a0f9c797626c4e66d472a517d17c.svg "Repobeats analytics image")

## 💬 Discussion

Have questions / doubts / ideas to discuss?
Feel free to open a discussion on [Github discussions](https://github.com/projectdiscovery/nuclei-templates/discussions) board.

## 👨‍💻 Community

You are welcome to join the active [Discord Community](https://discord.gg/projectdiscovery) to discuss directly with project maintainers and share things with others around security and automation.
Additionally, you may follow us on [Twitter](https://twitter.com/pdnuclei) to be updated on all the things about Nuclei.

[![](https://contrib.rocks/image?repo=projectdiscovery/nuclei-templates&max=300)](https://github.com/projectdiscovery/nuclei-templates/graphs/contributors)

Thanks again for your contribution and keeping this community vibrant. ❤️

[Read more](/en/tools/github/projectdiscovery/nuclei-templates?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Web Vulnerability Scanners](/en/categories/web-vulnerability-scanners)[Exploit Frameworks](/en/categories/exploit-frameworks)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Code Analysis](/en/categories/code-analysis)[Threat Intelligence](/en/categories/threat-intelligence)[Crawler](/en/categories/crawler)[Curated Resources](/en/categories/curated-resources)[DNS Analysis](/en/categories/dns-analysis)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[P...