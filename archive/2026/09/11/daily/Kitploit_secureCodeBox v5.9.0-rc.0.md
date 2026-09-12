---
title: secureCodeBox v5.9.0-rc.0
url: https://kitploit.com/en/posts/github-securecodebox-securecodebox-v590-rc0
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:04.909951
---

# secureCodeBox v5.9.0-rc.0

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/5452/6b1207aa587a2eba236730ba8b53b8d789c909ddf4acc91f5c51822d229ca9ef.png)

New releaseSep 11, 2026

# secureCodeBox v5.9.0-rc.0

Kubernetes-native security scanning orchestrator that automates continuous vulnerability detection by integrating multiple open-source scanners into a CI/CD pipeline.

Share

# OWASP secureCodeBox

![secureCodeBox Logo](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/resources/securecodebox-logo.svg)
![secureCodeBox Logo](https://assets.kitploit.com/production/public/readmes/5452/8902e5836a324eae0ab281a9be7d62683e025d503ce6778cce6768fb908c1089.png)

[![License Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/secureCodeBox/secureCodeBox?sort=semver)](https://github.com/secureCodeBox/secureCodeBox/releases/latest)
[![OWASP Lab Project](https://img.shields.io/badge/OWASP-Lab%20Project-yellow)](https://owasp.org/www-project-securecodebox/)
[![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/secureCodeBox)](https://artifacthub.io/packages/search?repo=securecodebox)
[![Mastodon Follower](https://img.shields.io/mastodon/follow/111902499714281911?domain=https://infosec.exchange/)](https://infosec.exchange/%40secureCodeBox)
[![Build](https://github.com/secureCodeBox/secureCodeBox/workflows/CI/badge.svg)](https://github.com/secureCodeBox/secureCodeBox/actions?query=workflow%3ACI)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/secureCodeBox/secureCodeBox/badge)](https://scorecard.dev/viewer/?uri=github.com/secureCodeBox/secureCodeBox)
[![](https://app.fossa.com/api/projects/git+github.com/secureCodeBox/secureCodeBox.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com/secureCodeBox/secureCodeBox?ref=badge_shield)

> *secureCodeBox* is a kubernetes based, modularized toolchain for continuous security scans of your software project. Its goal is to orchestrate and easily automate a bunch of security-testing tools out of the box.

![](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/resources/ascii/scb-first-start.svg)

## Overview

* [OWASP secureCodeBox](#owasp-securecodebox)
  + [Overview](#overview)
  + [Purpose of this Project](#purpose-of-this-project)
  + [Quickstart](#quickstart)
  + [Architecture Overview](#architecture-overview)
  + [Upgrading](#upgrading)
  + [License](#license)
  + [Community](#community)
  + [Contributing](#contributing)
  + [Sponsors](#sponsors)
  + [Author Information](#author-information)

For additional documentation aspects please have a look at our [documentation website](https://www.securecodebox.io):

## Purpose of this Project

The typical way to ensure application security is to hire a security specialist (aka penetration tester) at some point in your project to check the application for security bugs and vulnerabilities. Usually, this check is done at a later stage of the project and has two major drawbacks:

1. Nowadays, a lot of projects do continuous delivery, which means the developers deploy new versions multiple times each day. The penetration tester is only able to check a single snapshot, but some further commits could introduce new security issues. To ensure ongoing application security, the penetration tester should also continuously test the application. Unfortunately, such an approach is rarely financially feasible.
2. Due to a typically time boxed analysis, the penetration tester has to focus on trivial security issues (low-hanging fruit) and therefore will probably not address the serious, non-obvious ones.

With the *secureCodeBox* we provide a toolchain for continuous scanning of applications to find the low-hanging fruit issues early in the development process and free the resources of the penetration tester to concentrate on the major security issues.

The purpose of *secureCodeBox* **is not** to replace the penetration testers or make them obsolete. We strongly recommend to run extensive tests by experienced penetration testers on all your applications.

**Important note**: The *secureCodeBox* is no simple one-button-click-solution! You must have a deep understanding of security and how to configure the scanners. Furthermore, an understanding of the scan results and how to interpret them is also necessary.

There is a German article about [Security DevOps – Angreifern (immer) einen Schritt voraus](http://www.sigs.de/public/ots/2017/OTS_DevOps_2017/Seedorff_Pfaender_OTS_%20DevOps_2017.pdf) in the software engineering journal [OBJEKTSpektrum](https://www.sigs-datacom.de/fachzeitschriften/objektspektrum.html).

## Quickstart

You can find resources to help you get started on our [documentation website](https://www.securecodebox.io) including instruction on how to [install the secureCodeBox](https://www.securecodebox.io/docs/getting-started/installation) and guides to help you [run your first scans](https://www.securecodebox.io/docs/getting-started/first-scans) with it.

## Architecture Overview

![secureCodeBox Architecture](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/resources/scb-architecture.svg)

## Upgrading

For the steps required for upgrading your secureCodeBox installation, see [Upgrading](https://www.securecodebox.io/docs/getting-started/upgrading).

## License

Code of secureCodeBox is licensed under the [Apache License 2.0](https://raw.githubusercontent.com/secureCodeBox/secureCodeBox/master/LICENSE).

## Community

You are welcome, please join us on... 👋

* [GitHub Discussions (Questions & Feedback)](https://github.com/secureCodeBox/secureCodeBox/discussions/categories/general)
* [GitHub Issues (Bugs & Feature Requests)](https://github.com/secureCodeBox/)
* [Mastodon](https://infosec.exchange/%40secureCodeBox)

secureCodeBox is an official [OWASP](https://www.owasp.org/index.php/OWASP_secureCodeBox) project.

## Contributing

Contributions are welcome and extremely helpful 🙌
Please have a look at [Contributing](https://github.com/securecodebox/securecodebox/blob/main/CONTRIBUTING.md)

### Thanks to Our Awesome Contributors

![Awesome Contributors](https://contrib.rocks/image?repo=secureCodeBox/secureCodeBox)

### Stargazers over time

[![Star History Chart](https://api.star-history.com/svg?repos=secureCodeBox/secureCodeBox&type=Date)](https://star-history.com/#secureCodeBox/secureCodeBox&Date)

## Sponsors

[![iteratec Logo](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/documentation/static/img/Logo_iteratec_rgb_black_SZ_rz.svg)](https://www.iteratec.com/en/)

[![SDA SE Logo](https://assets.kitploit.com/production/public/readmes/5452/04abf2d5c496f7f1308616882af910e53640a72e031613cd81473df1aa781e6c.png)](https://sda-se.com/?lang=en)
[![Timo Pagel IT Consulting Logo](https://assets.kitploit.com/production/public/readmes/5452/167f563e94269f218ce9f18001bde421189310f68dc1f7f67ee8c4ab3560dbe6.png)](https://pagel.pro/en/)
[![Secura Logo](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/documentation/static/img/sponsors/Logo_secura.svg)](https://www.secura.com/en/)
[![Signal Iduna Logo](https://raw.githubusercontent.com/securecodebox/securecodebox/HEAD/documentation/static/img/sponsors/Logo_signal-iduna.svg)](https://www.signal-iduna.de/)

## Author Information

Sponsored and maintained by [iteratec GmbH](https://www.iteratec.com/) - [secureCodeBox.io](https://www.securecodebox.io/)

[Read more](/en/tools/github/securecodebox/securecodebox?expand=1)

## Categories

[Pen...