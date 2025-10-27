---
title: Bearer - Code Security Scanning Tool (SAST) That Discover, Filter And Prioritize Security Risks And Vulnerabilities Leading To Sensitive Data Exposures (PII, PHI, PD)
url: https://buaq.net/go-161002.html
source: unSafe.sh - 不安全
date: 2023-04-29
fetch_date: 2025-10-04T11:32:48.105466
---

# Bearer - Code Security Scanning Tool (SAST) That Discover, Filter And Prioritize Security Risks And Vulnerabilities Leading To Sensitive Data Exposures (PII, PHI, PD)

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

![](https://8aqnet.cdn.bcebos.com/189a08cff48434fb7dea6a70894fd3d7.jpg)

Bearer - Code Security Scanning Tool (SAST) That Discover, Filter And Prioritize Security Risks And Vulnerabilities Leading To Sensitive Data Exposures (PII, PHI, PD)

Discover, filter, and prioritize security risks and vulnerabilities impacting your code.
*2023-4-28 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-161002.htm)
阅读量:44
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9eltBq7OLWe3P7CGi4AwaeEI2zoBNJ627RzIEjnHt7mjleaqkF7QBsXanjUWgJDx7bxl2zD3yB6n-W3pakUjDjnazXvHjgIpc0goulTdgWlh8vsw0oATA4YN_SX2kZR5OK0dq4TmVL1S6ln_gwACjMoQyyLRqDQunkG6wfwy71kDw1YysFQvQBy0s1A/s16000/bearer.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9eltBq7OLWe3P7CGi4AwaeEI2zoBNJ627RzIEjnHt7mjleaqkF7QBsXanjUWgJDx7bxl2zD3yB6n-W3pakUjDjnazXvHjgIpc0goulTdgWlh8vsw0oATA4YN_SX2kZR5OK0dq4TmVL1S6ln_gwACjMoQyyLRqDQunkG6wfwy71kDw1YysFQvQBy0s1A/s340/bearer.png)

Discover, filter, and prioritize security risks and [vulnerabilities](https://www.kitploit.com/search/label/vulnerabilities "vulnerabilities") impacting your code.

Bearer is a static application security testing (SAST) tool that scans your source code and analyzes your data flows to discover, filter and prioritize security risks and vulnerabilities leading to sensitive data exposures (PII, PHI, PD).

Currently supporting **JavaScript** and **Ruby** stacks.

## Code security scanner that natively filters and prioritizes security risks using sensitive data flow analysis.

Bearer provides built-in rules against a common set of security risks and vulnerabilities, known as [OWASP Top 10](https://owasp.org/www-project-top-ten/ "OWASP Top 10"). Here are some practical examples of what those rules look for:

* Non-filtered user input.
* Leakage of sensitive data through cookies, internal loggers, third-party logging services, and into analytics environments.
* Usage of weak encryption libraries or misusage of encryption algorithms.
* Unencrypted incoming and outgoing communication (HTTP, FTP, SMTP) of sensitive information.
* Hard-coded secrets and tokens.

And many [more](https://docs.bearer.com/reference/rules/ "more").

Bearer is Open Source ([*see license*](https://github.com/Bearer/bearer#mortar_board-license "Code security scanning tool (SAST) that discover, filter and prioritize security risks and vulnerabilities leading to sensitive data exposures (PII, PHI, PD). (13)")) and fully customizable, from creating your own rules to component detection (database, API) and data classification.

Bearer also powers our commercial offering, [Bearer Cloud](https://www.bearer.com "Bearer Cloud"), allowing security teams to scale and monitor their application security program using the same engine.

## Getting started

Discover your most critical security risks and vulnerabilities in only a few minutes. In this guide, you will install Bearer, run a scan on a local project, and view the results. Let's get started!

### Install Bearer

The quickest way to install Bearer is with the install script. It will auto-select the best build for your architecture. *Defaults installation to `./bin` and to the latest release version*:

```
curl -sfL https://raw.githubusercontent.com/Bearer/bearer/main/contrib/install.sh | sh
```

#### Other install options

**Homebrew**

Using [Bearer's official Homebrew tap](https://github.com/Bearer/homebrew-tap "Bearer's official Homebrew tap"):

```
brew install bearer/tap/bearer
```

**Debian/Ubuntu**

```
$ sudo apt-get install apt-transport-https
```

**RHEL/CentOS**

Add repository setting:

```
$ sudo vim /etc/yum.repos.d/fury.repo
[fury]
name=Gemfury Private Repo
baseurl=https://yum.fury.io/bearer/
enabled=1
gpgcheck=0
```

Then install with yum:

```
  $ sudo yum -y update
  $ sudo yum -y install bearer
```

**Docker**

Bearer is also available as a Docker image on [Docker Hub](https://hub.docker.com/r/bearer/bearer "Docker Hub") and [ghcr.io](https://github.com/Bearer/bearer/pkgs/container/bearer "ghcr.io").

With docker installed, you can run the following command with the appropriate paths in place of the examples.

```
docker run --rm -v /path/to/repo:/tmp/scan bearer/bearer:latest-amd64 scan /tmp/scan
```

Additionally, you can use docker compose. Add the following to your `docker-compose.yml` file and replace the volumes with the appropriate paths for your project:

```
version: "3"
services:
  bearer:
    platform: linux/amd64
    image: bearer/bearer:latest-amd64
    volumes:
      - /path/to/repo:/tmp/scan
```

Then, run the `docker compose run` command to run Bearer with any specified flags:

```
docker compose run bearer scan /tmp/scan --debug
```

**Binary**

Download the archive file for your operating system/architecture from [here](https://github.com/Bearer/bearer/releases/latest/ "here").

Unpack the archive, and put the binary somewhere in your $PATH (on UNIX-y systems, /usr/local/bin or the like). Make sure it has permission to execute.

### Scan your project

The easiest way to try out Bearer is with our example project, [Bear Publishing](https://github.com/Bearer/bear-publishing "Bear Publishing"). It simulates a realistic Ruby application with common security flaws. Clone or download it to a convenient location to get started.

```
git clone https://github.com/Bearer/bear-publishing.git
```

Now, run the scan command with `bearer scan` on the project directory:

```
bearer scan bear-publishing
```

A progress bar will display the status of the scan.

Once the scan is complete, Bearer will output a security report with details of any rule failures, as well as where in the codebase the infractions happened and why.

By default the `scan` command use the SAST scanner, other [scanner types](https://docs.bearer.com/explanations/scanners "scanner types") are available.

### Analyze the report

The security report is an easily digestible view of the security issues detected by Bearer. A report is made up of:

* The list of [rules](https://docs.bearer.com/reference/rules/ "rules") run against your code.
* Each detected failure, containing the file location and lines that triggered the rule failure.
* A stat section with a summary of rules checks, failures and warnings.

The [Bear Publishing](https://github.com/Bearer/bear-publishing "Bear Publishing") example application will trigger rule failures and output a full report. Here's a section of the output:

```
...
CRITICAL: Only communicate using SFTP connections.
https://docs.bearer.com/reference/rules/ruby_lang_insecure_ftp

File: bear-publishing/app/services/marketing_export.rb:34

34     Net::FTP.open(
 35       'marketing.example.com',
 36       'marketing',
 37       'password123'
  	...
 41     end

=====================================

56 checks, 10 failures, 6 warnings

CRITICAL: 7
HIGH: 0
MEDIUM: 0
LOW: 3
WARNING: 6
```

The security report is just one [report type](https://docs.bearer.com/explanations/reports "report type") available in Bearer.

Additional options for using and configuring the `scan` command can be found in the [scan documentation](https://docs.bearer.com/reference/commands/#scan "scan documentation").

For additional guides and usage tips, [view the docs](https://docs.bearer.com/ "view the docs").

## FAQs

### How do you detect sensitive data flows from the code?

When you run Bearer on your codebase, it discovers and classifies data by identifying patterns in the source code. Specifically, it looks for data types and matches against them. Most importantly, it never views the actual values (it just can’t)—but only the code itself.

Bearer assesses 120+ dat...