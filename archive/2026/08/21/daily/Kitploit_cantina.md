---
title: cantina
url: https://kitploit.com/en/tools/gitlab/wattocyber/cantina
source: Kitploit
date: 2026-08-21
fetch_date: 2026-08-22T02:51:02.951397
---

# cantina

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

[Tools](/en/tools)/![GitLab](/providers/gitlab.png)GitLab/wattocyber/cantina

![](https://assets.kitploit.com/production/public/tools/50588/a6783378bacd9b10844a10b68440150e9e41e7ec0f07ec6220707af378e13b4e.jpg)

[Reconnaissance](/en/categories/reconnaissance)[Network Mapping](/en/categories/network-mapping)[Port Scanning](/en/categories/port-scanning)[Information Gathering](/en/categories/information-gathering)[Penetration Testing](/en/categories/penetration-testing)

![GitLab](/providers/gitlab.png)wattocyber/cantina

# cantina

OSCP-legal network recon orchestrator for port discovery, service classification, and enum-only plugin dispatch across HTTP, SMB, FTP, SNMP, SSH, and more.

[View Repository](https://gitlab.com/wattocyber/cantina)[Website](https://gitlab.com/WattoCyber/cantina)

2 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Cantina

![Cantina - OSCP-legal network recon orchestrator](https://assets.kitploit.com/production/public/readmes/50588/a6783378bacd9b10844a10b68440150e9e41e7ec0f07ec6220707af378e13b4e.jpg)

**Cantina** is an OSCP-legal network recon orchestrator. Port discovery, service enum, and plugin dispatch. No exploitation. No credential spray auto-run.

---

## What it does

1. Scans targets (`quick` / `full` / `udp` / `vuln` / `recon` / `all` / `deep`)
2. Classifies open services
3. Runs **enum-only plugins** for matching services (HTTP, SMB, FTP, SNMP, SSH, and the rest)
4. Writes per-port artifacts, `_commands.log` audit, optional HTML/JSON

## Requirements

* Python 3.10+
* Kali (or similar) tools when available: `nmap`, and service tools plugins call when present
* Soft deps only: missing tools are skipped, not fatal

## Quick start

root@kitploit:~

```
# list plugins (no scan)
python tools/cantina.py --list-plugins

# single host
python tools/cantina.py 10.10.10.5 -t quick

# recon with full scan + plugins
python tools/cantina.py 10.10.10.5 -t recon \
  --force-services tcp/80/http tcp/445/smb tcp/22/ssh \
  -o ./out -j

# multi-target concurrent
python tools/cantina.py -T hosts.txt -t all --max-workers 3 --timeout 90
```

Quiet CLI (no banner): `python tools/cantina.py TARGET -q`

## Plugins

Drop a module under `plugins/` (or `--plugins-dir`):

root@kitploit:~

```
PLUGIN = {
    "name": "my_enum",
    "services": ["ftp"],
    "ports": [21],
    "enabled": True,
    "replaces_builtin": True,
    "description": "FTP enum (enum only)",
    "legal": "enumeration-only; OSCP-safe; no exploit/spray auto-run",
}

def match(signals):
    return signals.get("svc_type") == "ftp" or int(signals.get("port") or 0) == 21

def run(ctx):
    art = ctx.port_dir / "plugin_my_enum.txt"
    art.write_text(f"enum note for {ctx.target}:{ctx.port}\n")
    return {"ok": True, "artifact": str(art)}
```

`replaces_builtin: True` skips the old monorepo branch for that service so you do not double-run.

## Tests

root@kitploit:~

```
pip install pytest
python -m pytest tests/ -q
```

## Legal

Enumeration only. Authorized targets and own lab / OSCP exam scope only. You are responsible for scope.

## Layout

root@kitploit:~

```
tools/              CLI tools (run with: python tools/<tool>.py)
  cantina.py          CLI + orchestrator
  cantina_plugins.py  discover / select / run
plugins/            service enum plugins
assets/banner.txt   CLI terminal banner
banner.jpg          README hero image
tests/              unit tests (stubbed tools)
lab/                optional multi-service lab ground truth
fixtures/           nmap parse fixtures
```

[Download Tool](https://gitlab.com/wattocyber/cantina)