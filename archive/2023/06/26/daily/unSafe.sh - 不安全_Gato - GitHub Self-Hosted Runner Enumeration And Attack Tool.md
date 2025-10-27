---
title: Gato - GitHub Self-Hosted Runner Enumeration And Attack Tool
url: https://buaq.net/go-170245.html
source: unSafe.sh - 不安全
date: 2023-06-26
fetch_date: 2025-10-04T11:44:41.076939
---

# Gato - GitHub Self-Hosted Runner Enumeration And Attack Tool

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/47c0aeaedb7adcf19a29dd8fa5e1c87b.jpg)

Gato - GitHub Self-Hosted Runner Enumeration And Attack Tool

Gato, or GitHub Attack Toolkit, is an enumeration and attack tool that allows both blue t
*2023-6-25 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-170245.htm)
阅读量:40
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrSybj3mH9kKuf6SoryxrJVROcNdHYesZ8YTHS58VuvB6BGBWFZPONd8Rg4mfjChEQkcv7dDMegB55HJKavruICmdrEy5zXZ9TKqsZwlBexHxrNsnSu_4bWkOZ1IHV4VK_tmi7fqobAgwOzzGZ5UsfuqQGTAh5DNFZolvPn7rZs0Z7QWKCqOQQxgyQkw=w494-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEjrSybj3mH9kKuf6SoryxrJVROcNdHYesZ8YTHS58VuvB6BGBWFZPONd8Rg4mfjChEQkcv7dDMegB55HJKavruICmdrEy5zXZ9TKqsZwlBexHxrNsnSu_4bWkOZ1IHV4VK_tmi7fqobAgwOzzGZ5UsfuqQGTAh5DNFZolvPn7rZs0Z7QWKCqOQQxgyQkw)

Gato, or GitHub Attack Toolkit, is an [enumeration](https://www.kitploit.com/search/label/Enumeration "enumeration") and attack tool that allows both blue teamers and offensive security practitioners to evaluate the blast radius of a compromised personal [access token](https://www.kitploit.com/search/label/Access%20Token "access token") within a GitHub organization.

The tool also allows searching for and thoroughly enumerating public repositories that utilize self-hosted runners. GitHub recommends that self-hosted runners only be utilized for private repositories, however, there are thousands of organizations that utilize self-hosted runners.

## Who is it for?

* Security engineers who want to understand the level of access a compromised classic PAT could provide an attacker
* Blue teams that want to build detections for self-hosted runner attacks
* Red Teamers
* Bug bounty hunters who want to try and prove RCE on organizations that are utilizing self-hosted runners

## Features

* GitHub Classic PAT Privilege Enumeration
* GitHub Code Search API-based enumeration
* GitHub Action Run Log Parsing to identify Self-Hosted Runners
* Bulk Repo Sparse Clone Features
* GitHub Action Workflow Parsing
* Automated Command Execution Fork PR Creation
* Automated Command Execution Workflow Creation
* SOCKS5 Proxy Support
* HTTPS Proxy Support

## Getting Started

### Installation

Gato supports OS X and Linux with at least **Python 3.7**.

In order to install the tool, simply clone the repository and use `pip install`. We recommend performing this within a virtual environment.

```
git clone https://github.com/praetorian-inc/gato
```

Gato also requires that `git` version `2.27` or above is installed and on the system's PATH. In order to run the fork PR attack module, `sed` must also be installed and present on the system's path.

### Usage

After installing the tool, it can be launched by running `gato` or `praetorian-gato`.

We recommend viewing the parameters for the base tool using `gato -h`, and the parameters for each of the tool's modules by running the following:

* `gato search -h`
* `gato enum -h`
* `gato attack -h`

The tool requires a GitHub classic PAT in order to function. To create one, log in to GitHub and go to [GitHub Developer Settings](https://github.com/settings/tokens "GitHub Developer  Settings") and select `Generate New Token` and then `Generate new token (classic)`.

After creating this token set the `GH_TOKEN` environment variable within your shell by running `export GH_TOKEN=<YOUR_CREATED_TOKEN>`. Alternatively, store the token within a secure password manager and enter it when the application prompts you.

For [troubleshooting](https://www.kitploit.com/search/label/Troubleshooting "troubleshooting") and additional details, such as installing in developer mode or running unit tests, please see the [wiki](https://github.com/praetorian-inc/gato/wiki "wiki").

## Documentation

Please see the [wiki](https://github.com/praetorian-inc/gato/wiki "wiki"). for detailed documentation, as well as [OpSec](https://github.com/praetorian-inc/gato/wiki/opsec "OpSec") considerations for the tool's various modules!

## Bugs

If you believe you have identified a bug within the software, please open an issue containing the tool's output, along with the actions you were trying to conduct.

If you are unsure if the behavior is a bug, use the discussions section instead!

## Contributing

Contributions are welcome! Please [review](https://github.com/praetorian-inc/gato/wiki/Project-Design "review") our design methodology and coding standards before working on a new feature!

Additionally, if you are proposing significant changes to the tool, please open an issue [open an issue](https://github.com/praetorian-inc/gato/issues/new "open an issue") to start a conversation about the motivation for the changes.

Gato - GitHub Self-Hosted Runner Enumeration And Attack Tool
![Gato - GitHub Self-Hosted Runner Enumeration And Attack Tool](https://blogger.googleusercontent.com/img/a/AVvXsEjrSybj3mH9kKuf6SoryxrJVROcNdHYesZ8YTHS58VuvB6BGBWFZPONd8Rg4mfjChEQkcv7dDMegB55HJKavruICmdrEy5zXZ9TKqsZwlBexHxrNsnSu_4bWkOZ1IHV4VK_tmi7fqobAgwOzzGZ5UsfuqQGTAh5DNFZolvPn7rZs0Z7QWKCqOQQxgyQkw=s72-w494-c-h640)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/gato-github-self-hosted-runner.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)