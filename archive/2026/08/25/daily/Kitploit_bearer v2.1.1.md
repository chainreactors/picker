---
title: bearer v2.1.1
url: https://kitploit.com/en/posts/github-bearer-bearer-v211
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:17.403180
---

# bearer v2.1.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/378/4030c4edcfadafdb8ebdc20e0b71738d7130455a8f1efe564068062b9eb1bfbb.png)

New releaseAug 25, 2026

# bearer v2.1.1

Code security scanning tool (SAST) to discover, filter and prioritize security and privacy risks.

Share

[![Cygives Banner](https://raw.githubusercontent.com/bearer/bearer/HEAD/docs/assets/img/Cygives-lightmode.svg)](https://cycode.com/cygives/)

![Bearer](https://raw.githubusercontent.com/bearer/bearer/HEAD/docs/assets/img/bearer-logo-light.svg)

---

Scan your source code against top **security** and **privacy** risks.

Bearer is a static application security testing (SAST) tool designed to scan your source code and analyze data flows to identify, filter, and prioritize security and privacy risks.

Bearer offers a free, open solution, Bearer CLI, and a commercial solution, Bearer Pro, available through [Cycode](https://cycode.com/).

[Getting Started](#rocket-getting-started) - [FAQ](#question-faqs) - [Documentation](https://docs.bearer.com) - [Report a Bug](https://github.com/Bearer/bearer/issues/new/choose)

[![GitHub Release](https://img.shields.io/github/release/Bearer/bearer.svg?logo=github)](https://github.com/Bearer/bearer/releases)
[![Test](https://github.com/Bearer/bearer/actions/workflows/test.yml/badge.svg)](https://github.com/Bearer/bearer/actions/workflows/test.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

## Language Support

**Bearer CLI (Open Source)**: Go • Java • JavaScript • TypeScript • PHP • Python • Ruby

**Bearer Pro by Cycode**: *All Bearer CLI languages plus:*

* **Advanced Cross-file Analysis**: Java • Python • C# *(alpha)*
* **Additional Languages**: C# • Kotlin • Elixir • VB.Net

[Learn more about language support](https://docs.bearer.com/reference/supported-languages/)

## Developer friendly static code analysis for security and privacy

<https://user-images.githubusercontent.com/1649672/230438696-9bb0fd35-2aa9-4273-9970-733189d01ff1.mp4>

Bearer CLI scans your source code for:

* **Security risks and vulnerabilities** using [built-in rules](https://docs.bearer.com/reference/rules/) covering the [OWASP Top 10](https://owasp.org/www-project-top-ten/) and [CWE Top 25](https://cwe.mitre.org/top25/archive/2023/2023_top25_list.html), such as:

  + A01: Access control (e.g. Path Traversal, Open Redirect, Exposure of Sensitive Information).
  + A02: Cryptographic Failures (e.g. Weak Algorithm, Insecure Communication).
  + A03: Injection (e.g. SQL Injection, Input Validation, XSS, XPath).
  + A04: Design (e.g. Missing Encryption of Sensitive Data, Persistent Cookies Containing Sensitive Information).
  + A05: Security Misconfiguration (e.g. Cleartext Storage of Sensitive Information in a Cookie or JWT).
  + A07: Identification and Authentication Failures (e.g. Use of Hard-coded Password, Improper Certificate Validation).
  + A08: Data Integrity Failures (e.g. Deserialization of Untrusted Data).
  + A09: Security Logging and Monitoring Failures (e.g. Insertion of Sensitive Information into Log File).
  + A10: Server-Side Request Forgery (SSRF).

  *Note: all the rules and their code patterns are accessible through the [documentation](https://docs.bearer.com/reference/rules/).*
* **Privacy risks** with the ability to detect [sensitive data flow](https://docs.bearer.com/explanations/discovery-and-classification/) such as the use of PII, PHI in your app, and [components](https://docs.bearer.com/reference/recipes/) processing sensitive data (e.g. databases like pgSQL, third-party APIs such as OpenAI, Sentry, etc.). This helps generate a [privacy report](https://docs.bearer.com/guides/privacy/) relevant for:

  + Privacy Impact Assessment (PIA).
  + Data Protection Impact Assessment (DPIA).
  + Records of Processing Activities (RoPA) input for GDPR compliance reporting.

## 🚀 Getting started

Discover your most critical security risks and vulnerabilities in only a few minutes. In this guide, you will install Bearer CLI, run a security scan on a local project, and view the results. Let's get started!

### Install Bearer CLI

The quickest way to install Bearer CLI is with the install script. It will auto-select the best build for your architecture. *Defaults installation to `./bin` and to the latest release version*:

root@kitploit:~

```
curl -sfL https://raw.githubusercontent.com/Bearer/bearer/main/contrib/install.sh | sh
```

#### Other install options

Homebrew

Using [Bearer CLI's official Homebrew tap](https://github.com/Bearer/homebrew-tap):

root@kitploit:~

```
brew install bearer/tap/bearer
```

Update an existing installation with the following:

root@kitploit:~

```
brew update && brew upgrade bearer/tap/bearer
```

Debian/Ubuntu

root@kitploit:~

```
sudo apt-get update && sudo apt-get install ca-certificates -y && sudo update-ca-certificates
sudo apt-get install apt-transport-https
echo -e "Types: deb\nURIs: https://apt.fury.io/bearer/\nSuites: /\nTrusted: yes" | sudo tee /etc/apt/sources.list.d/fury.sources
sudo apt-get update
sudo apt-get install bearer
```

Update an existing installation with the following:

root@kitploit:~

```
sudo apt-get update
sudo apt-get install bearer
```

RHEL/CentOS

Add repository setting:

root@kitploit:~

```
$ sudo vim /etc/yum.repos.d/fury.repo
[fury]
name=Gemfury Private Repo
baseurl=https://yum.fury.io/bearer/
enabled=1
gpgcheck=0
```

Then install with yum:

root@kitploit:~

```
  sudo yum -y update
  sudo yum -y install bearer
```

Update an existing installation with the following:

root@kitploit:~

```
sudo yum -y update bearer
```

Docker

Bearer CLI is also available as a Docker image on [Docker Hub](https://hub.docker.com/r/bearer/bearer) and [ghcr.io](https://github.com/bearer/bearer/pkgs/container/bearer).

With docker installed, you can run the following command with the appropriate paths in place of the examples.

root@kitploit:~

```
docker run --rm -v /path/to/repo:/tmp/scan bearer/bearer:latest-amd64 scan /tmp/scan
```

Additionally, you can use docker compose. Add the following to your `docker-compose.yml` file and replace the volumes with the appropriate paths for your project:

root@kitploit:~

```
version: "3"
services:
  bearer:
    platform: linux/amd64
    image: bearer/bearer:latest-amd64
    volumes:
      - /path/to/repo:/tmp/scan
```

Then, run the `docker compose run` command to run Bearer CLI with any specified flags:

root@kitploit:~

```
docker compose run bearer scan /tmp/scan --debug
```

The Docker configurations above will always use the latest release.

Binary

Download the archive file for your operating system/architecture from [here](https://github.com/Bearer/bearer/releases/latest/).

Unpack the archive, and put the binary somewhere in your $PATH (on UNIX-y systems, /usr/local/bin or the like). Make sure it has permission to execute.

To update Bearer CLI when using the binary, download the latest release and overwrite your existing installation location.

### Scan your project

The easiest way to try out Bearer CLI is with the OWASP [Juice Shop](https://github.com/juice-shop/juice-shop) example project. It simulates a realistic JavaScript application with common security flaws. Clone or download it to a convenient location to get started.

root@kitploit:~

```
git clone https://github.com/juice-shop/juice-shop.git
```

Now, run the scan command with `bearer scan` on the project directory:

root@kitploit:~

```
bearer scan juice-shop
```

A progress bar will display the status of the scan.

Once the scan is complete, Bearer CLI will output, by default, a security...