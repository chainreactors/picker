---
title: custom-oscp-tooling
url: https://kitploit.com/en/tools/gitlab/wattocyber/custom-oscp-tooling
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:02.177844
---

# custom-oscp-tooling

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

custom-oscp-tooling — OSCP-focused toolkit for read-only network, SMB, AD, DNS, web, and database enumeration; privesc scanning, hash identification, and payload/credential command generation. | Kitploit

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/wattocyber/custom-oscp-tooling

![](https://assets.kitploit.com/production/public/tools/50584/b05c52ceda73c2399a81df3cad2958f2b2a2a6ad4cbe2814aedc4d8a8633c216.png)

[Privilege Escalation](/en/categories/privilege-escalation)[Reconnaissance](/en/categories/reconnaissance)[Password Attacks](/en/categories/password-attacks)[Hash Analysis](/en/categories/hash-analysis)[Information Gathering](/en/categories/information-gathering)[Post-Exploitation](/en/categories/post-exploitation)[Web Security](/en/categories/web-security)[Network Security](/en/categories/network-security)[Penetration Testing](/en/categories/penetration-testing)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[Payload Development](/en/categories/payload-development)

[DNS Analysis](/en/categories/dns-analysis)

[Database Security](/en/categories/database-security)

![GitLab](/providers/gitlab.png)wattocyber/custom-oscp-tooling

# custom-oscp-tooling

OSCP-focused toolkit for read-only network, SMB, AD, DNS, web, and database enumeration; privesc scanning, hash identification, and payload/credential command generation.

[View Repository](https://gitlab.com/wattocyber/custom-oscp-tooling)[Website](https://gitlab.com/WattoCyber/custom-oscp-tooling)

2 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

# Custom OSCP Tooling

![Cantina - OSCP-legal network recon orchestrator](https://assets.kitploit.com/production/public/readmes/50584/33a98da51e1cc08244ae70a94e6436fd193ca83472c692760579d5a1fa87dc75.jpg)

A consolidated set of **read-only, OSCP-exam-safe custom tools** by Samson Laird. Everything here enumerates, identifies, and advises. Nothing here exploits, sprays, or modifies a target.

## Tools

| Tool | What it does | Class |
| --- | --- | --- |
| `cantina.py` | Network recon orchestrator: port discovery, service classification, enum-plugin dispatch. | Enum / orchestration |
| `ackbar.py` | AD enumeration in one script. BloodHound + PowerView style output, no graph DB. | AD enum |
| `bobafett.py` | Database service enumerator. Auth tests + read-only SELECT only. | DB enum |
| `jarjar.py` | HTTP service scanner with verbose logging + Rich TUI report. | Web enum |
| `jawa.py` | SMB enumeration with clean output (enum4linux replacement). | SMB enum |
| `leia.py` / `leia.ps1` / `leiAD.ps1` | Universal privesc scanner. Detects OS, runs the right checks. | PrivEsc enum |
| `maul.py` | DNS enumeration. Pure Python, no external deps. | DNS enum |
| `obi.py` | Context-aware attack advisor. Reads findings, matches technique library, prints next commands. | Advisor |
| `yoda.py` | Hash identification + hashcat command generation + \*2john wrappers. | Hash ID |
| `jedi.nse` | Nmap NSE script (service enum). | NSE |
| `blaster/` | OSCP payload factory (payload + listener + hosting + download cmds). | Payload factory |
| `chewie/` | On-host Windows domain enumerator (transfer to compromised box). | AD enum |
| `order66/` | Multi-protocol AD credential sprayer (password-first strategy). | Credential logic |
| `vader/` | Port-to-playbook lookup engine. Feed nmap output or ports, get playbooks. | Lookup |
| `xwing/` | ADCS exploitation assistant. Walks Ackbar/Certipy findings. | ADCS assistant |

## Safety contract

Every tool is **read-only** where it claims to be. No tool here:

* Modifies, creates, or deletes AD objects, files, or shares
* Cracks hashes itself (identification + command generation only)
* Auto-runs credential sprays (order66 generates the sequence; you run it)
* Executes system commands against a target

Run against **authorized targets and your own lab / OSCP exam scope only**. You are responsible for scope.

## Requirements

* Python 3.10+
* Kali (or similar) tools when available: `nmap`, plus service tools plugins call
* Soft deps only: missing tools are skipped, not fatal

## Quick start (Cantina)

root@kitploit:~

```
# list plugins (no scan)
python tools/cantina.py --list-plugins

# single host
python tools/cantina.py 10.10.10.5 -t quick

# multi-target concurrent
python tools/cantina.py -T hosts.txt -t all --max-workers 3 --timeout 90
```

## Tests

root@kitploit:~

```
pip install -e ".[dev]"   # or: pip install pytest
python -m pytest tests/ -q
# expect: exit 0
```

## Layout

root@kitploit:~

```
tools/              CLI tools (run with: python tools/<tool>.py)
  cantina.py          CLI + orchestrator
  cantina_plugins.py  discover / select / run
  ackbar.py ...       Star Wars custom OSCP tools
plugins/            service enum plugins
blaster/ chewie/ order66/ vader/ xwing/
assets/banner.txt   CLI terminal banner
banner.jpg          README hero image
tests/              unit tests (stubbed tools)
lab/                optional multi-service lab ground truth
fixtures/           nmap parse fixtures
```

## License

MIT. See [LICENSE](https://gitlab.com/wattocyber/custom-oscp-tooling/-/blob/master/LICENSE).

[Download Tool](https://gitlab.com/wattocyber/custom-oscp-tooling)