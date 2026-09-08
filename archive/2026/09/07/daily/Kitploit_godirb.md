---
title: godirb
url: https://kitploit.com/en/tools/github/mycode83/godirb
source: Kitploit
date: 2026-09-07
fetch_date: 2026-09-08T06:40:56.902722
---

# godirb

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

godirb — Fast and easy-to-use directory brute-forcer written in Go. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/mycode83/godirb

![](https://assets.kitploit.com/production/public/tools/54323/6e93ddcdab1f674fe6adbdf82e120191afaafce98a2e77c2a77891dbbb592042-display-v1.webp)

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Web Vulnerability Scanners](/en/categories/web-vulnerability-scanners)[Information Gathering](/en/categories/information-gathering)[Web Security](/en/categories/web-security)[Fuzzing](/en/categories/fuzzing)[Penetration Testing](/en/categories/penetration-testing)

![GitHub](/providers/github.png)mycode83/godirb

# godirb

Fast and easy-to-use directory brute-forcer written in Go.

[View Repository](https://github.com/mycode83/godirb)

3295 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# godirb

**Fast, modern directory, file, port and FUZZ brute-forcer written in Go.**

Built for quick scans where you want a modern dirb-like tool: run it, get useful results, tune the obvious flags, and avoid dragging a full fuzzing framework into a simple job.

![License](https://img.shields.io/github/license/MyCode83/godirb?style=for-the-badge)
![Release](https://img.shields.io/github/v/release/MyCode83/godirb?style=for-the-badge)
![Go](https://img.shields.io/github/go-mod/go-version/MyCode83/godirb?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/MyCode83/godirb?style=for-the-badge)

## 📦 Installation

### Go

root@kitploit:~

```
go install github.com/MyCode83/godirb@latest
```

## Homebrew

root@kitploit:~

```
brew install MyCode83/godirb/godirb
```

### Binary

Download the latest release for your platform from the
**Releases** page and add it to your `PATH`.

[Download Tool](https://github.com/mycode83/godirb)

---

## 🚀 Quick Start

Basic scan

root@kitploit:~

```
godirb -u https://example.com
```

Recursive

root@kitploit:~

```
godirb -u https://example.com -r
```

Recursive with a depth limit

root@kitploit:~

```
godirb -u https://example.com -r --depth 2
```

Custom wordlist

root@kitploit:~

```
godirb -u https://example.com -w paths.txt
```

JSON output

root@kitploit:~

```
godirb -u https://example.com --json -o results.json
```

---

## ✨ Why godirb?

godirb is designed for the common case: you want to enumerate directories and files quickly, without configuring a large fuzzing framework.

### Highlights

* ⚡ Fast native Go binary
* 📦 Single executable
* 📚 Embedded wordlists
* 🔄 Recursive scanning
* 📂 Directory and file discovery
* 🎯 Wildcard filtering / response calibration
* 🌐 Port fuzzing (`http://host:FUZZ`)
* 📄 JSON & CSV output
* 🧩 Simple CLI

---

## 📊 godirb vs DirSearch

DirSearch is a mature and feature-rich web path scanner.

godirb intentionally focuses on the most common workflow: install, run and get useful results with minimal setup.

| Feature | godirb | DirSearch |
| --- | --- | --- |
| Find files and folders | ✅ | ✅ |
| Recursive scan | ✅ | ✅ |
| Custom wordlists | ✅ | ✅ |
| Written in Go | ✅ | ❌ |
| Single binary | ✅ | ❌ |
| Embedded default wordlists | ✅ | ❌ |
| Works without runtime wordlist files | ✅ | ❌ |
| Port fuzzing (`http://host:FUZZ`) | ✅ | ❌ |

---

## 📦 Features

### Scanning

* Directory and file brute-forcing
* Recursive mode (`-r`, `--recursive`)
* Recursive depth limit (`--depth`, default: 2)
* Extensions (`-x`, `--ext`)
* Custom wordlists (`-w`, `--wordlist`)
* FUZZ placeholder mode

### Embedded Wordlists

* small
* medium *(default)*
* big
* ports
* payloads
* xss
* lfi

### Output

* Standard text
* Quiet mode
* JSON
* CSV
* File output

### Control

* Threads (`-t`, `--threads`)
* Ignore status codes (`-i`, `--ignore`)
* Default ignored codes: `404,400,405,408`
* Wildcard filtering / response calibration

---

## 💻 Examples

Basic scan

root@kitploit:~

```
godirb -u https://example.com
```

Recursive

root@kitploit:~

```
godirb -u https://example.com -r
```

Recursive with one nested level

root@kitploit:~

```
godirb -u https://example.com -r --depth 1
```

Custom wordlist

root@kitploit:~

```
godirb -u https://example.com -w paths.txt
```

Extensions

root@kitploit:~

```
godirb -u https://example.com -x php,txt,bak
```

FUZZ parameter

root@kitploit:~

```
godirb -u "https://example.com/search?q=FUZZ" -w payloads
```

Port fuzzing

root@kitploit:~

```
godirb -u https://example.com:FUZZ
```

Export JSON

root@kitploit:~

```
godirb -u https://example.com --json -o results.json
```

Export CSV

root@kitploit:~

```
godirb -u https://example.com --csv -o results.csv
```

---

## 📋 Example Output

root@kitploit:~

```
DIR       200      1234 B  https://example.com/admin
FILE      200       842 B  https://example.com/login.php
DIR       403       795 B  https://example.com/uploads
```

---

**📖 Embedded wordlists**

| Name | Purpose |
| --- | --- |
| small | common.txt from SecLists |
| medium | Default raft-medium-directories |
| big | Larger enumeration DirBuster big |
| ports | Port fuzzing |
| payloads | Generic payloads |
| xss | XSS payloads |
| lfi | LFI payloads |

---

## ⚠️ Disclaimer

Use **godirb** only for authorized security testing, labs and CTFs.

You are responsible for obtaining permission before scanning any target.

---

## 📄 License

Licensed under the **MIT License**. See **LICENSE** for details.