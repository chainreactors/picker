---
title: faraday_plugins v1.30.0
url: https://kitploit.com/en/posts/github-infobyte-faraday_plugins-1300
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:11.441771
---

# faraday_plugins v1.30.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/40567/0b128b7adf0427b8a2b66dbd3806af72ee60efcbc18807ff279608b8f90a75aa.png)

New releaseSep 4, 2026

# faraday\_plugins v1.30.0

Security tools report parsers for Faradaysec.com

Share

## Install

root@kitploit:~

```
pip install faraday-plugins
```

## Commands

### List Plugins

List all plugins and if its compatible with command or/and report

Optional params:

* -cpf / --custom-plugins-folder PATH: If given will also look for custom plugins on that path

root@kitploit:~

```
faraday-plugins list-plugins
```

### Test autodetect plugin from command

root@kitploit:~

```
faraday-plugins detect-command "ping -c 4 www.google.com"

Faraday Plugin: ping
```

### Test process command with plugin

Optional params:

* --plugin\_id PLUGIN\_ID: Dont detect the plugin, use this one
* -cpf / --custom-plugins-folder PATH: If given will also look for custom plugins on that path
* -dr / --dont-run: Dont run, just show the generated command
* -o / --output-file PATH: send json outout to file instead of stdout
* -sh / --show-output: show the output of the command

root@kitploit:~

```
faraday-plugins process-command "ping -c4 www.google.com"
{
    "hosts": [
        {
            "ip": "216.58.202.36",
            "os": "unknown",
            "hostnames": [
                "www.google.com"
            ],
            "description": "",
            "mac": null,
            "credentials": [],
            "services": [],
            "vulnerabilities": [],
            "tags": []
        }
    ],
    "command": {
        "tool": "ping",
        "command": "ping",
        "params": "-c4 www.google.com",
        "user": "user",
        "hostname": "",
        "start_date": "2020-06-19T17:02:37.982293",
        "duration": 39309,
        "import_source": "shell"
    }
}
```

### Test autodetect plugin from report

root@kitploit:~

```
faraday-plugins detect-report /path/to/report.xml

Faraday Plugin: Nmap
```

### Test report with plugin

Optional params:

* --plugin\_id PLUGIN\_ID: Dont detect the plugin, use this one
* -cpf / --custom-plugins-folder PATH: If given will also look for custom plugins on that path

root@kitploit:~

```
faraday-plugins process-report /path/to/nmap_report.xml

{
    "hosts": [
        {
            "ip": "192.168.66.1",
            "os": "unknown",
            "hostnames": [],
            "description": "",
            "mac": "00:00:00:00:00:00",
            "credentials": [],
            "services": [
                {
                    "name": "domain",
                    "protocol": "tcp",
                    "port": 53,
                    "status": "open",
                    "version": "",
                    "description": "domain",
                    "credentials": [],
                    "vulnerabilities": [],
                    "tags": []
                },
                {
                    "name": "netbios-ssn",
                    "protocol": "tcp",
                    "port": 139,
                    "status": "open",
                    "version": "",
                    "description": "netbios-ssn",
                    "credentials": [],
                    "vulnerabilities": [],
                    "tags": []
                }
            ],
            "vulnerabilities": [],
            "tags": []
        }
    ],
    "command": {
        "tool": "Nmap",
        "command": "Nmap",
        "params": "/path/to/nmap_report.xml",
        "user": "user",
        "hostname": "",
        "start_date": "2020-06-19T17:22:11.608134",
        "duration": 1233,
        "import_source": "report"
    }
}
```

## Plugin Logger

To use it you must call `self.logger.debug("some message")`

root@kitploit:~

```
export PLUGIN_DEBUG=1
faraday-plugins proces-report /path/to/report.xml
2019-11-15 20:37:03,355 - faraday.faraday_plugins.plugins.manager - INFO [manager.py:113 - _load_plugins()]  Loading Native Plugins...
2019-11-15 20:37:03,465 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [acunetix]
2019-11-15 20:37:03,495 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [amap]
2019-11-15 20:37:03,549 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [appscan]
2019-11-15 20:37:03,580 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [arachni]
2019-11-15 20:37:03,613 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [arp_scan]
2019-11-15 20:37:03,684 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [beef]
2019-11-15 20:37:03,714 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [brutexss]
2019-11-15 20:37:03,917 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [burp]
2019-11-15 20:37:03,940 - faraday.faraday_plugins.plugins.manager - DEBUG [manager.py:123 - _load_plugins()]  Load Plugin [dig]
...
```

More documentation here <https://docs.faradaysec.com/Basic-plugin-development/>

[Read more](/en/tools/github/infobyte/faraday_plugins?expand=1)

## Categories

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Penetration Testing](/en/categories/penetration-testing)[DevSecOps](/en/categories/devsecops)

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