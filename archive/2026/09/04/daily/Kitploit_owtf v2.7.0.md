---
title: owtf v2.7.0
url: https://kitploit.com/en/posts/github-owtf-owtf-v270
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:27.725160
---

# owtf v2.7.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/2080/ca2a8b5d58c37eea267c2773c4ebebff1b85f4f0ef83467d7efe1be0cbd68ab7.png)

New releaseSep 4, 2026

# owtf v2.7.0

Modular penetration testing framework integrating multiple tools for automated web application security assessment, aligned with OWASP Testing Guide, PTES, and NIST standards.

Share

# Offensive Web Testing Framework (OWTF)

[![Build status](https://github.com/owtf/owtf/actions/workflows/main.yml/badge.svg)](https://github.com/owtf/owtf/actions/workflows/main.yml)
[![License: BSD 3-Clause](https://img.shields.io/badge/license-BSD%203--Clause-blue.svg?style=flat-square)](LICENSE.md)
[![Python Versions](https://img.shields.io/badge/python-3.11%E2%80%933.12-blue.svg)](https://www.python.org/downloads/)

**OWASP OWTF** helps penetration testers stay efficient and aligned with security standards such as the
[OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/), the OWASP Top 10, PTES, and
NIST so that they have more time to:

* See the big picture and think outside the box.
* Efficiently find, verify, and combine vulnerabilities.
* Investigate complex issues such as business logic flaws or multi-tenant edge cases.
* Perform targeted fuzzing on risky areas.
* Demonstrate meaningful impact despite tight assessment windows.

The tool is highly configurable, and anyone can create simple plugins or add new tests in configuration files without prior development experience.

> **Note**
> OWTF is not a silver bullet. Understanding and experience are still required to interpret tool output correctly and decide where to investigate further in order to demonstrate impact.

# Quick start

Docker Compose is the supported way to run OWTF. It keeps the Python, frontend, PostgreSQL, and security-tool dependencies
isolated from the host system.

Install [Docker](https://docs.docker.com/get-docker/) with the Compose plugin, then run:

root@kitploit:~

```
git clone https://github.com/owtf/owtf.git
cd owtf
make compose-safe
```

When the services are ready, open <http://localhost:8019>.

| Service | Address |
| --- | --- |
| Web interface | <http://localhost:8019> |
| Backend API | <http://localhost:8009> |
| Intercepting proxy | `localhost:8008` |

Press `Ctrl+C` in the Compose terminal to stop OWTF. Native host installation is intended for contributors and is not a
supported end-user installation path; see [CONTRIBUTING.md](https://github.com/owtf/owtf/blob/develop/CONTRIBUTING.md) for the development workflow.

> **Important**
> Only scan systems you own or are explicitly authorised to test.

# Features

* **Resilience**: If one tool crashes, OWTF moves on to the next test and saves the partial output produced so far.
* **Flexible**: Pause and resume your work.
* **Test separation**: OWTF separates its traffic to the target into three plugin types:
  + **Passive** – No traffic is sent to the target.
  + **Semi passive** – Normal traffic to the target.
  + **Active** – Direct vulnerability probing.
* **Extensive REST API**.
* **Standards coverage**: OWASP Web Security Testing Guide, OWASP Top 10, NIST, PTES, and CWE-aligned workflows.
* **Web interface**: Manage large penetration engagements easily.
* **Interactive report**.
* **Automated plugin rankings** from tool output, fully configurable by the user.
* **Configurable risk rankings**.
* **Inline notes editor** for each plugin.

# License

Check out [LICENSE](https://github.com/owtf/owtf/blob/develop/LICENSE.md).

# Code of Conduct

Check out the [Code of Conduct](https://github.com/owtf/owtf/blob/develop/CODE_OF_CONDUCT.md).

# Links

* [Project homepage](https://owtf.github.io/)
* [OWASP project page](https://owasp.org/www-project-owtf/)
* [Development documentation](https://docs.owtf.org/en/develop/)
* [Releases](https://github.com/owtf/owtf/releases)
* [OWASP Slack](https://owasp.org/slack/invite) – join `#project-owtf`
* [YouTube channel](https://www.youtube.com/user/owtfproject)

[Read more](/en/tools/github/owtf/owtf?expand=1)

## Categories

[Penetration Testing Frameworks](/en/categories/penetration-testing-frameworks)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Exploit Frameworks](/en/categories/exploit-frameworks)[Web Security](/en/categories/web-security)[Penetration Testing](/en/categories/penetration-testing)

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