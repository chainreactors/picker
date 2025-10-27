---
title: REST-Attacker - Designed As A Proof-Of-Concept For The Feasibility Of Testing Generic Real-World REST Implementations
url: https://buaq.net/go-144574.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:46.107836
---

# REST-Attacker - Designed As A Proof-Of-Concept For The Feasibility Of Testing Generic Real-World REST Implementations

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

![](https://8aqnet.cdn.bcebos.com/fd7bbeb8a1b2df72a4e409711e22a638.jpg)

REST-Attacker - Designed As A Proof-Of-Concept For The Feasibility Of Testing Generic Real-World REST Implementations

REST-Attacker is an automated penetration testing framework for APIs following the REST arch
*2023-1-7 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-144574.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgBGVUcKGEiLkMggf88qYq11YpDLH6_K7gzp-bsz1GBgRxVb7HaJCIXTqllJw5hmpJJ1CnSGjyRQbL9o2qGBEgrgkuA4YzaVTytJHQuWajXJ1vBA-pKBChLyZqgx79aD7yECFKNXqXpimCywbQqo2tjjIHxHAhZSTj0y0Jk56zFzR8ujnK56A9Rpg7KQ/w640-h288/REST-API.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgBGVUcKGEiLkMggf88qYq11YpDLH6_K7gzp-bsz1GBgRxVb7HaJCIXTqllJw5hmpJJ1CnSGjyRQbL9o2qGBEgrgkuA4YzaVTytJHQuWajXJ1vBA-pKBChLyZqgx79aD7yECFKNXqXpimCywbQqo2tjjIHxHAhZSTj0y0Jk56zFzR8ujnK56A9Rpg7KQ/s843/REST-API.png)

REST-Attacker is an [automated](https://www.kitploit.com/search/label/Automated "automated") [penetration testing framework](https://www.kitploit.com/search/label/Penetration%20Testing%20Framework "penetration testing framework") for APIs following the REST architecture style. The tool's focus is on streamlining the analysis of generic REST API implementations by completely automating the testing process - including test generation, access control handling, and report generation - with minimal configuration effort. Additionally, REST-Attacker is designed to be flexible and extensible with support for both large-scale testing and fine-grained analysis.

REST-Attacker is maintained by the [Chair of Network & Data Security](https://informatik.rub.de/nds/ "Chair of Network & Data Security") of the Ruhr University of Bochum.

## Features

REST-Attacker currently provides these features:

* **Automated generation of tests**
  + Utilize an OpenAPI description to automatically generate test runs
  + 32 integrated security tests based on [OWASP](https://owasp.org/www-project-api-security/ "OWASP") and other scientific contributions
  + Built-in creation of security reports
* **Streamlined API communication**
  + Custom request interface for the REST security use case (based on the Python3 [requests](https://requests.readthedocs.io/en/latest/ "requests") module)
  + Communicate with any generic REST API
* **Handling of access control**
  + Background authentication/authorization with API
  + Support for the most popular access control mechanisms: OAuth2, HTTP Basic Auth, API keys and more
* **Easy to use & extend**
  + Usable as standalone (CLI) tool or as a module
  + Adapt test runs to specific APIs with extensive configuration options
  + Create custom test cases or access control schemes with the tool's interfaces

## Install

Get the tool by downloading or cloning the repository:

```
git clone https://github.com/RUB-NDS/REST-Attacker.git
```

You need Python >3.10 for running the tool.

You also need to install the following packages with pip:

```
python3 -m pip install -r requirements.txt
```

## Quickstart

Here you can find a quick rundown of the most common and useful commands. You can find more information on each command and other about available configuration options in our [usage guides](https://github.com/RUB-NDS/REST-Attacker/blob/main/doc/usage "usage guides").

Get the list of supported test cases:

```
python3 -m rest_attacker --list
```

Basic test run (with load-time test case generation):

```
python3 -m rest_attacker <cfg-dir-or-openapi-file> --generate
```

Full test run (with load-time and runtime test case generation + rate limit handling):

```
python3 -m rest_attacker <cfg-dir-or-openapi-file> --generate --propose --handle-limits
```

Test run with only selected test cases (only generates test cases for test cases `scopes.TestTokenRequestScopeOmit` and `resources.FindSecurityParameters`):

```
python3 -m rest_attacker <cfg-dir-or-openapi-file> --generate --test-cases scopes.TestTokenRequestScopeOmit resources.FindSecurityParameters
```

Rerun a test run from a report:

```
python3 -m rest_attacker <cfg-dir-or-openapi-file> --run /path/to/report.json
```

## Documentation

Usage guides and configuration format documentation can be found in the [documentation](https://github.com/RUB-NDS/REST-Attacker/blob/main/doc "documentation") subfolders.

## Troubleshooting

For fixes/mitigations for known problems with the tool, see the [troubleshooting docs](https://github.com/RUB-NDS/REST-Attacker/blob/main/doc/troubleshooting.md "troubleshooting docs") or the [Issues](https://github.com/RUB-NDS/REST-Attacker/issues "Issues") section.

## Contributing

Contributions of all kinds are appreciated! If you found a bug or want to make a suggestion or feature request, feel free to create a new [issue](https://github.com/RUB-NDS/REST-Attacker/issues "issue") in the issue tracker. You can also submit fixes or code ammendments via a [pull request](https://github.com/RUB-NDS/REST-Attacker/pulls "pull request").

Unfortunately, we can be very busy sometimes, so it may take a while before we respond to comments in this repository.

## License

This project is licensed under **GNU LGPLv3 or later** (LGPL3+). See [COPYING](https://github.com/RUB-NDS/REST-Attacker/blob/main/COPYING "COPYING") for the full license text and [CONTRIBUTORS.md](https://github.com/RUB-NDS/REST-Attacker/blob/main/CONTRIBUTORS.md "CONTRIBUTORS.md") for the list of authors.

REST-Attacker - Designed As A Proof-Of-Concept For The Feasibility Of Testing Generic Real-World REST Implementations
![REST-Attacker - Designed As A Proof-Of-Concept For The Feasibility Of Testing Generic Real-World REST Implementations](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhgBGVUcKGEiLkMggf88qYq11YpDLH6_K7gzp-bsz1GBgRxVb7HaJCIXTqllJw5hmpJJ1CnSGjyRQbL9o2qGBEgrgkuA4YzaVTytJHQuWajXJ1vBA-pKBChLyZqgx79aD7yECFKNXqXpimCywbQqo2tjjIHxHAhZSTj0y0Jk56zFzR8ujnK56A9Rpg7KQ/s72-w640-c-h288/REST-API.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/rest-attacker-designed-as-proof-of.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)