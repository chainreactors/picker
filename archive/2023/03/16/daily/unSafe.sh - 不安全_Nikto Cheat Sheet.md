---
title: Nikto Cheat Sheet
url: https://buaq.net/go-153624.html
source: unSafe.sh - 不安全
date: 2023-03-16
fetch_date: 2025-10-04T09:42:48.257947
---

# Nikto Cheat Sheet

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

![]()

Nikto Cheat Sheet

What is NiktoNikto is an open-source web server scanner that performs comprehensive tests to ident
*2023-3-15 22:37:10
Author: [highon.coffee(查看原文)](/jump-153624.htm)
阅读量:23
收藏*

---

* [What is Nikto](#what-is-nikto)
* [Nikto Installation](#nikto-installation)
  + [Nikto Update](#nikto-update)
  + [Main script is in program](#main-script-is-in-program)
  + [Check out the 2.5.0 branch](#check-out-the-250-branch)
  + [Run using the shebang interpreter](#run-using-the-shebang-interpreter)
  + [Run using perl (if you forget to chmod)](#run-using-perl-if-you-forget-to-chmod)
* [Nikto Scan Cheat Sheet](#nikto-scan-cheat-sheet)
* [Nikto Command Flags Sheet](#nikto-command-flags-sheet)
* [Nikto Example Commands](#nikto-example-commands)
  + [Nikto Scanning](#nikto-scanning)
  + [Nikto Using a Proxy](#nikto-using-a-proxy)
* [Nikto2 Features](#nikto2-features)
* [Document Changelog](#document-changelog)

## What is Nikto

Nikto is an open-source web server scanner that performs comprehensive tests to identify potentially dangerous files/programs, outdated versions of servers, server configuration items, and installed web servers and software. It also supports LibWhisker’s anti-IDS methods to avoid detection. While not every check is a security issue, most are, and there are also info-only checks and checks for unknown items.

## Nikto Installation

```
git clone https://github.com/sullo/nikto
```

### Nikto Update

cd into your nikto git clone directory:

```
git pull
```

### Main script is in program

```
cd nikto/program
```

### Check out the 2.5.0 branch

```
git checkout nikto-2.5.0
```

### Run using the shebang interpreter

```
./nikto.pl -h http://www.foo.com
```

### Run using perl (if you forget to chmod)

```
perl nikto.pl -h http://www.foo.com
```

* list element with functor item

## Nikto Scan Cheat Sheet

The following Nikto command usage for scanning a web application:

| Command | Description |
| --- | --- |
| `nikto -h http://foo.com` | Scans the specified host |
| `nikto -h http://foo.com -Tuning 6` | Uses a specific Nikto scan tuning level |
| `nikto -h http://foo.com -port 8000` | Scans the specified port |
| `nikto -h http://foo.com -ssl` | Scans for SSL vulnerabilities |
| `nikto -h http://foo.com -Format html` | Formats output in HTML |
| `nikto -h http://foo.com -output out.txt` | Saves the output to a file |

## Nikto Command Flags Sheet

The following Nikto commands allow for configuration of a Nikto scan:

| Option | Value |
| --- | --- |
| `-ask+` | `yes` Ask about each (default)  `no` Don't ask, don't send |
| `-Cgidirs+` | "none", "all", or values like "/cgi/ /cgi-a/" |
| `-config+` | Use this config file |
| `-Display+` | 1 Show redirects  2 Show cookies received  3 Show all 200/OK responses  4 Show URLs which require authentication  D Debug output  E Display all HTTP errors  P Print progress to STDOUT  S Scrub output of IPs and hostnames  V Verbose output |
| `-dbcheck` | Check database and other key files for syntax errors |
| `-evasion+` | 1 Random URI encoding (non-UTF8)  2 Directory self-reference (/./)  3 Premature URL ending  4 Prepend long random string  5 Fake parameter  6 TAB as request spacer  7 Change the case of the URL  8 Use Windows directory separator (\)  A Use a carriage return (0x0d) as a request spacer  B Use binary value 0x0b as a request spacer |
| `-Format+` | csv Comma-separated-value  htm HTML Format  msf+ Log to Metasploit  nbe Nessus NBE format  txt Plain text  xml XML Format  (if not specified the format will be taken from the file extension passed to -output) |
| `-Help` | Extended help information |
| `-host+` | Target host |
| `-IgnoreCode` | Ignore Codes--treat as negative responses |
| `-id+` | Host authentication to use, format is id:pass or id:pass:realm |
| `-key+` | Client certificate key file |
| `-list-plugins` | List all available plugins, perform no testing |
| `-maxtime+` | Maximum testing time per host |
| `-mutate+` | 1 Test all files with all root directories  2 Guess for password file names  3 Enumerate user names via Apache (/~user type requests)  4 Enumerate user names via cgiwrap (/cgi-bin/cgiwrap/~user type requests)  5 Attempt to brute force sub-domain names, assume that the host name is the parent domain  6 Attempt to guess directory names from the supplied dictionary file |
| `-mutate-options` | Provide information for mutates |
| `-nointeractive` | Disables interactive features |
| `-nolookup` | Disables DNS lookups |
| `-nossl` | Disables the use of SSL |
| `-no404` | Disables nikto attempting to guess a 404 page |
| `-output+` | Write output to this file ('.' for auto-name) |
| `-Pause+` | Pause between tests (seconds, integer or float) |
| `-Plugins+` | List of plugins to run (default: ALL) |
| `-port+` | Port to use (default 80) |
| `-RSAcert+` | Client certificate file |
| `-root+` | Prepend root value to all requests, format is /directory |
| `-Save` | Save positive responses to this directory ('.' for auto-name) |
| `-ssl` | Force ssl mode on port |
| `-Tuning+` | 1 Interesting File / Seen in logs  2 Misconfiguration / Default File  3 Information Disclosure  4 Injection (XSS/Script/HTML)  5 Remote File Retrieval - Inside Web Root  6 Denial of Service  7 Remote File Retrieval - Server Wide  8 Command Execution / Remote Shell  9 [SQL Injection](/penetration-testing/web-app/sql-injection/)  0 File Upload  a Authentication Bypass  b Software Identification  c Remote Source Inclusion  x Reverse Tuning Options (i.e., include all except specified) |
| `-timeout+` | Timeout for requests (default 10 seconds) |
| `-Userdbs` | Load only user databases, not the standard databases  all Disable standard dbs and load only user dbs  tests Disable only db\_tests and load udb\_tests |
| `-until` | Run until the specified time or duration |
| `-update` | Update databases and plugins from CIRT.net |
| `-useproxy` | Use the proxy defined in nikto.conf |
| `-Version` | Print plugin and database versions |
| `-vhost+` | Virtual host (for Host header) |

## Nikto Example Commands

### Nikto Scanning

The following nikto commands allow you to run basic nikto scans against a web application.

| Command | Description |
| --- | --- |
| `nikto -h [target]` | Basic scan, no HTTP options. |
| `nikto -h [target] -Tuning [tuning]` | Scan with a specific tuning. |
| `nikto -h [target] -mutate [mutate]` | Scan with a specific mutation. |
| `nikto -h [target] -ssl` | Scan using SSL. |
| `nikto -h [target] -nointeractive` | Run the scan non-interactively. |

### Nikto Using a Proxy

Using Nikto with a proxy such as Burp or another intercepting proxy.

| Command | Description |
| --- | --- |
| `-useproxy` | Enable usage of the HTTP/SOCKS proxy |
| `-noproxy` | Specify comma separated list of hosts not to use proxy for |
| `-proxyhost` | Hostname or IP address of the HTTP/SOCKS proxy |
| `-proxyport` | Port of the HTTP/SOCKS proxy |
| `-proxypass` | Password for the HTTP/SOCKS proxy |
| `-proxyuser` | Username for the HTTP/SOCKS proxy |

## Nikto2 Features

* SSL Support (Unix with OpenSSL or maybe Windows with ActiveState’s Perl/NetSSL)
* Full HTTP proxy support
* Checks for outdated server components
* Save reports in plain text, XML, HTML, NBE or CSV
* Template engine to easily customize reports
* Scan multiple ports on a server, or multiple servers via input file (including nmap output)
* LibWhisker’s IDS encoding techniques
* Easily updated via command line
* Identifies installed software via headers, favicons and files
* Host authentication with Basic and NTLM
* Subdomain guessing
* Apache and cgiwrap username enumeration
* Mu...