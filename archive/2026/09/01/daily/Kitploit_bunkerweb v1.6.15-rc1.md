---
title: bunkerweb v1.6.15-rc1
url: https://kitploit.com/en/posts/github-bunkerity-bunkerweb-v1615-rc1
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:07.168576
---

# bunkerweb v1.6.15-rc1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/255/54acb3a1c8ef4d4e4c2acc18cb088e754f3da7926daab2d5d24dd3a22cf0e454.png)

New releaseSep 1, 2026

# bunkerweb v1.6.15-rc1

🛡️ Open-source and cloud-native Web Application Firewall (WAF)

Share

![BunkerWeb logo](https://raw.githubusercontent.com/bunkerity/bunkerweb/v1.6.14/misc/logo.png)

![](https://img.shields.io/github/v/release/bunkerity/bunkerweb?label=stable)
![](https://img.shields.io/github/v/release/bunkerity/bunkerweb?include_prereleases&label=latest)

![](https://img.shields.io/github/last-commit/bunkerity/bunkerweb)
![](https://img.shields.io/github/issues/bunkerity/bunkerweb)
![](https://img.shields.io/github/issues-pr/bunkerity/bunkerweb)

![](https://img.shields.io/github/actions/workflow/status/bunkerity/bunkerweb/dev.yml?branch=dev&label=CI/CD%20dev)
![](https://img.shields.io/github/actions/workflow/status/bunkerity/bunkerweb/staging.yml?branch=staging&label=CI/CD%20staging)

[![](https://www.bestpractices.dev/projects/8001/badge)](https://www.bestpractices.dev/projects/8001)
[![GitRated rating](https://gitrated.com/bunkerity/bunkerweb/badge)](https://gitrated.com/bunkerity/bunkerweb)
[![Plumber CI/CD security score](https://score.getplumber.io/github.com/bunkerity/bunkerweb.svg)](https://score.getplumber.io/github.com/bunkerity/bunkerweb)

[![Star History Rank](https://api.star-history.com/badge?repo=bunkerity/bunkerweb)](https://www.star-history.com/bunkerity/bunkerweb)

🌐 [Website](https://www.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
🤝 [Panel](https://panel.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
📓 [Documentation](https://docs.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
👨‍💻 [Demo](https://demo.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
📱 [Demo UI](https://demo-ui.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
🧩 [Templates](https://github.com/bunkerity/bunkerweb-templates)
|
🛡️ [Examples](https://github.com/bunkerity/bunkerweb/raw/v1.6.14/examples)

💬 [Chat](https://discord.com/invite/fTf46FmtyD)
|
📝 [Forum](https://github.com/bunkerity/bunkerweb/discussions)
|
📝 [Community](https://community.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
🗺️ [Threatmap](https://www.bunkerweb.io/threatmap/?utm_campaign=self&utm_source=github)
|
📊 [Status](https://status.bunkerweb.io/?utm_campaign=self&utm_source=github)
|
🔎 [Feedback](https://forms.gle/e3VgymAteYPnwM1j9)

> 🛡️ Make security by default great again!

# BunkerWeb

![Overview banner](https://raw.githubusercontent.com/bunkerity/bunkerweb/v1.6.14/docs/assets/img/intro-overview.svg)

BunkerWeb is a next-generation, open-source Web Application Firewall (WAF).

Being a full-featured web server (based on [NGINX](https://nginx.org/) under the hood), it will protect your web services to make them "secure by default." BunkerWeb integrates seamlessly into your existing environments ([Linux](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#linux), [Docker](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#docker), [Swarm](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#swarm), [Kubernetes](https://docs.bunkerweb.io/1.6.14/integrations/?utm_campaign=self&utm_source=github#kubernetes), …) as a reverse proxy and is fully configurable (don't panic, there is an [awesome web UI](https://docs.bunkerweb.io/1.6.14/web-ui/?utm_campaign=self&utm_source=github) if you don't like the CLI) to meet your own use cases. In other words, cybersecurity is no longer a hassle.

BunkerWeb contains primary [security features](https://docs.bunkerweb.io/1.6.14/advanced/?utm_campaign=self&utm_source=github#security-tuning) as part of the core but can be easily extended with additional ones thanks to a [plugin system](https://docs.bunkerweb.io/1.6.14/plugins/?utm_campaign=self&utm_source=github).

## Why BunkerWeb?

<https://github.com/user-attachments/assets/c3fed740-28d8-4335-ab05-113a9e815b4f>

* **Easy integration into existing environments**: Seamlessly integrate BunkerWeb into various environments such as Linux, Docker, Swarm, Kubernetes, and more. Enjoy a smooth transition and hassle-free implementation.
* **Highly customizable**: Tailor BunkerWeb to your specific requirements with ease. Enable, disable, and configure features effortlessly, allowing you to customize the security settings according to your unique use case.
* **Secure by default**: BunkerWeb provides out-of-the-box, hassle-free minimal security for your web services. Experience peace of mind and enhanced protection right from the start.
* **Awesome web UI**: Take control of BunkerWeb more efficiently with the exceptional web user interface (UI). Navigate settings and configurations effortlessly through a user-friendly graphical interface, eliminating the need for the command-line interface (CLI).
* **Plugin system**: Extend the capabilities of BunkerWeb to meet your own use cases. Seamlessly integrate additional security measures and customize the functionality of BunkerWeb according to your specific requirements.
* **Free as in "freedom"**: BunkerWeb is licensed under the free [AGPLv3 license](https://www.gnu.org/licenses/agpl-3.0.en.html), embracing the principles of freedom and openness. Enjoy the freedom to use, modify, and distribute the software, backed by a supportive community.
* **Professional services**: Get technical support, tailored consulting, and custom development directly from the maintainers of BunkerWeb. Visit the [Bunker Panel](https://panel.bunkerweb.io/?utm_campaign=self&utm_source=github) for more information.

## Security features

A non-exhaustive list of security features:

* **HTTPS** support with transparent **Let's Encrypt** automation
* **State-of-the-art web security**: HTTP security headers, prevent leaks, TLS hardening, ...
* Integrated **ModSecurity WAF** with the **OWASP Core Rule Set**
* **Automatic ban** of strange behaviors based on HTTP status codes
* Apply **connection and request limits** for clients
* **Block bots** by asking them to solve a **challenge** (e.g., cookie, JavaScript, captcha, hCaptcha, or reCAPTCHA)
* **Block known bad IPs** with external blacklists and DNSBL
* And much more...

Learn more about the core security features in the [security tuning](https://docs.bunkerweb.io/1.6.14/advanced/?utm_campaign=self&utm_source=github#security-tuning) section of the documentation.

## Demo

<https://github.com/user-attachments/assets/6fc0e3c1-d353-4a84-bad0-15bf9b6623a5>

A demo website protected with BunkerWeb is available at [demo.bunkerweb.io](https://demo.bunkerweb.io/?utm_campaign=self&utm_source=github). Feel free to visit it and perform some security tests.

## Web UI

<https://github.com/user-attachments/assets/a3ed56f8-c124-4ca9-b8b3-4be0913b3078>

BunkerWeb offers an optional [user interface](https://github.com/bunkerity/bunkerweb/blob/HEAD/web-ui.md) to manage your instances and their configurations. An online read-only demo is available at [demo-ui.bunkerweb.io](https://demo-ui.bunkerweb.io/?utm_campaign=self&utm_source=doc), feel free to test it yourself.

## BunkerWeb Cloud

Don't want to self-host and manage your own BunkerWeb instance(s)? You might be interested in BunkerWeb Cloud, our fully managed SaaS offering for BunkerWeb.

Order your [BunkerWeb Cloud instance](https://panel.bunkerweb.io/store/bunkerweb-cloud?utm_campaign=self&utm_source=doc) and get access to:

* A fully managed BunkerWeb instance hosted in our cloud
* All BunkerWeb features, including PRO ones
* A monitoring platform with dashboards and alerts
* Technical support to...