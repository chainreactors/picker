---
title: SafeLine v9.4.1
url: https://kitploit.com/en/posts/github-chaitin-safeline-v941
source: Kitploit
date: 2026-09-04
fetch_date: 2026-09-05T06:28:23.704759
---

# SafeLine v9.4.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/166/4b67f9d3cf1d79277fd468e698e24de2ffa6bc37db0953b9f4d98739094969c5.png)

New releaseSep 4, 2026

# SafeLine v9.4.1

Self-hosted WAF and reverse proxy that filters malicious HTTP traffic, blocks SQL injection, XSS, and bot attacks, with rate limiting and dynamic HTML/JS encryption.

Share

![](https://assets.kitploit.com/production/public/readmes/166/414bde4c786c371220ace50f957382f7faf80bc1303cbbe392fd2d194dd2695b.png)

#### SafeLine - Make your web apps secure

[🏠 Website](https://ly.safepoint.cloud/laA8asp)   |
[📖 Docs](https://ly.safepoint.cloud/w2AeHhb)   |
[🔍 Live Demo](https://ly.safepoint.cloud/hSMd4SH)   |
[🙋‍♂️ Discord](https://discord.gg/SVnZGzHFvn)   |
[中文版](https://github.com/chaitin/safeline/blob/main/README_CN.md)

## 👋 INTRODUCTION

SafeLine is a self-hosted **`WAF(Web Application Firewall)`** to protect your web apps from attacks and exploits.

A web application firewall helps protect web apps by filtering and monitoring HTTP traffic between a web application and the Internet. It typically protects web apps from attacks such as `SQL injection`, `XSS`, `code injection`, `os command injection`, `CRLF injection`, `ldap injection`, `xpath injection`, `RCE`, `XXE`, `SSRF`, `path traversal`, `backdoor`, `bruteforce`, `http-flood`, `bot abused`, among others.

#### 💡 How It Works

![](https://assets.kitploit.com/production/public/readmes/166/e6fc19ed98dbb1a3ea2f3bff82367a60b4b3ea8026d1fa926c6e579ab1de5621.png)

By deploying a WAF in front of a web application, a shield is placed between the web application and the Internet. While a proxy server protects a client machine’s identity by using an intermediary, a WAF is a type of reverse-proxy, protecting the server from exposure by having clients pass through the WAF before reaching the server.

A WAF protects your web apps by filtering, monitoring, and blocking any malicious HTTP/S traffic traveling to the web application, and prevents any unauthorized data from leaving the app. It does this by adhering to a set of policies that help determine what traffic is malicious and what traffic is safe. Just as a proxy server acts as an intermediary to protect the identity of a client, a WAF operates in similar fashion but acting as a reverse proxy intermediary that protects the web app server from a potentially malicious client.

its core capabilities include:

* Defenses for web attacks
* Proactive bot abused defense
* HTML & JS code encryption
* IP-based rate limiting
* Web Access Control List

#### ⚡️ Screenshots

| ![](https://assets.kitploit.com/production/public/readmes/166/4b67f9d3cf1d79277fd468e698e24de2ffa6bc37db0953b9f4d98739094969c5.png) | ![](https://assets.kitploit.com/production/public/readmes/166/925c7d2b9c3a1050f286c61e37b4dc3c1497f496ac6131080e3c8ea17cd5f707.png) |
| --- | --- |
| ![](https://assets.kitploit.com/production/public/readmes/166/d7ecf0d8d91e470f595b1bcf4279c64e2141b7ae4bafcc974fe7bfbfaebf4c0e.png) | ![](https://assets.kitploit.com/production/public/readmes/166/bcb0bc757ea59eca6d0b14f8b164c4a6e85ed40e56db8aa2272716c4316177e2.png) |

Get [Live Demo](https://demo.waf.chaitin.com:9443/)

## 🔥 FEATURES

List of the main features as follows:

* **`Block Web Attacks`**
  + It defenses for all of web attacks, such as `SQL injection`, `XSS`, `code injection`, `os command injection`, `CRLF injection`, `XXE`, `SSRF`, `path traversal` and so on.
* **`Rate Limiting`**
  + Defend your web apps against `DoS attacks`, `bruteforce attempts`, `traffic surges`, and other types of abuse by throttling traffic that exceeds defined limits.
* **`Anti-Bot Challenge`**
  + Anti-Bot challenges to protect your website from `bot attacks`, humen users will be allowed, crawlers and bots will be blocked.
* **`Authentication Challenge`**
  + When authentication challenge turned on, visitors need to enter the password, otherwise they will be blocked.
* **`Dynamic Protection`**
  + When dynamic protection turned on, html and js codes in your web server will be dynamically encrypted by each time you visit.

#### 🧩 Showcases

|  | Legitimate User | Malicious User |
| --- | --- | --- |
| **`Block Web Attacks`** | ![](https://assets.kitploit.com/production/public/readmes/166/2f6928c11612d2d066721337594832b6b5b250b0d451c7fe0e56c3293b5b466c.png) | ![](https://assets.kitploit.com/production/public/readmes/166/9fb14872031d9700544fc5a356efd6096b632276b154e78f12b73703c32d527e.png) |
| **`Rate Limiting`** | ![](https://assets.kitploit.com/production/public/readmes/166/2f6928c11612d2d066721337594832b6b5b250b0d451c7fe0e56c3293b5b466c.png) | ![](https://assets.kitploit.com/production/public/readmes/166/a970051a2b608f642d6a98c44da5673e9ba6ff374aa288af38658e8a9da54de9.png) |
| **`Anti-Bot Challenge`** | ![](https://assets.kitploit.com/production/public/readmes/166/b0954a13a84aea3f3d424ab66668d364a14a0b5d3891e32bcbf9a3a0f75c26e5.gif) | ![](https://assets.kitploit.com/production/public/readmes/166/a84e1dab258e7e326f4b50d2661b6c3413aece66cf5c8c7ab209513bd4294026.gif) |
| **`Auth Challenge`** | ![](https://assets.kitploit.com/production/public/readmes/166/e697ff3d1de3f1ccd3e5cdf48c86d7e896b5e2bc6543c007a5b6ec88b173c53c.gif) | ![](https://assets.kitploit.com/production/public/readmes/166/234d86b6d475d1b5c2a6538bf596df68ff450723213b7a2d715e6e2ae1785390.gif) |
| **`HTML Dynamic Protection`** | ![](https://assets.kitploit.com/production/public/readmes/166/63d580a12de94a5a2ae580fa347be63fe91700e60e74ad5acf290b6173762939.png) | ![](https://assets.kitploit.com/production/public/readmes/166/c3cba3f319f1bdcfad2f357f3e055610bbda32cb6540777e5d7aedd5bfee4f52.png) |
| **`JS Dynamic Protection`** | ![](https://assets.kitploit.com/production/public/readmes/166/073cd66060bedef0acb62a7606981d1444ad841963b68d13641fcb948d824cde.png) | ![](https://assets.kitploit.com/production/public/readmes/166/1bb0ab3c78db559665d6e2127e82330f6f93a672a8948b87c756dd0df5744564.png) |

## 🚀 Quickstart

> [!WARNING]
> 中国大陆用户安装国际版可能会导致无法连接云服务，请查看 [中文版安装文档](https://docs.waf-ce.chaitin.cn/zh/%E4%B8%8A%E6%89%8B%E6%8C%87%E5%8D%97/%E5%AE%89%E8%A3%85%E9%9B%B7%E6%B1%A0)

#### 📦 Installing

Information on how to install SafeLine can be found in the [Install Guide](https://docs.waf.chaitin.com/en/GetStarted/Deploy)

#### ⚙️ Protecting Web Apps

to see [Configuration](https://docs.waf.chaitin.com/en/GetStarted/AddApplication)

## 📋 More Informations

#### Effect Evaluation

| Metric | ModSecurity, Level 1 | CloudFlare, Free | SafeLine, Balance | SafeLine, Strict |
| --- | --- | --- | --- | --- |
| Total Samples | 33669 | 33669 | 33669 | 33669 |
| **Detection** | 69.74% | 10.70% | 71.65% | **76.17%** |
| **False Positive** | 17.58% | 0.07% | **0.07%** | 0.22% |
| **Accuracy** | 82.20% | 98.40% | **99.45%** | 99.38% |

#### Is SafeLine Production-Ready?

Yes, SafeLine is production-ready.

* Over 180,000 installations worldwide
* Protecting over 1,000,000 Websites
* Handling over 30,000,000,000 HTTP Requests Daily

#### 🙋‍♂️ Community

Join our [Discord](https://discord.gg/SVnZGzHFvn) to get community support, the core team members are identified by the STAFF role in Discord.

* channel [#feedback](https://discord.com/channels/1243085666485534830/1243120292822253598): for new features discussion.
* channel [#FAQ](https://discord.com/channels/1243085666485534830/1263761679619981413): for FAQ.
* channel [#general](https://discord.com/channels/1243085666485534830/1243115843919806486): for any other questions.

Several contact options exist for our community, the primary one being Discord. These are in addition to GitHub issues for creating a new issue.

[![](https://img.shields.io/ba...