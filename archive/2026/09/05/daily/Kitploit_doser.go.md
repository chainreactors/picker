---
title: doser.go
url: https://kitploit.com/en/tools/github/quitten/doser.go
source: Kitploit
date: 2026-09-05
fetch_date: 2026-09-06T06:39:14.914077
---

# doser.go

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

doser.go — DoS tool for HTTP requests (inspired by hulk but has more functionalities) | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/quitten/doser.go

![](https://assets.kitploit.com/production/public/tools/54163/213327e4776c49cecdd072c969784b2506a2fb4a446d08e551fac1bdd7ee88c6-display-v1.webp)

[Web Security](/en/categories/web-security)[Network Security](/en/categories/network-security)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)

![GitHub](/providers/github.png)quitten/doser.go

# doser.go

DoS tool for HTTP requests (inspired by hulk but has more functionalities)

[View Repository](https://github.com/quitten/doser.go)

538181272 years ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# doser.go

[![Go](https://github.com/stylish-bear/doser.go/actions/workflows/go.yml/badge.svg)](https://github.com/stylish-bear/doser.go/actions/workflows/go.yml)

DoS tool for HTTP requests (inspired by hulk but has more functionalities) written in Go:

![screenshot](https://assets.kitploit.com/production/public/readmes/54163/213327e4776c49cecdd072c969784b2506a2fb4a446d08e551fac1bdd7ee88c6/c99b0171d32138ac66b55eaa2aba7cddeb0120ef0449f2b61ddc1780987bb75c-display-v1.webp)

## How to use?

1. Compile it

   root@kitploit:~

   ```
   go build doser.go
   ```
2. Use it (For example: 999 threads sends GET requests). P.S: Do not really attack my website pls

   root@kitploit:~

   ```
   ./doser -t 999 -g 'https://stylish-bear.ru'
   ```

## Usage

root@kitploit:~

```
Usage of ./doser: [-h] [-g G] [-p P] [-d D] [-ah AH] [-t T]

optional arguments:

  -h, --help  show this help message and exit

  -g        Specify GET request. Usage: -g '< url >'

  -p        Specify POST request. Usage: -p '< url >'

  -d        Specify data payload for POST request

  -t        Specify number of threads to be used
```

[Download Tool](https://github.com/quitten/doser.go)

## TODO:

* [x]  Rewrite to Golang :)