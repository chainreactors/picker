---
title: GUAC - Aggregates Software Security Metadata Into A High Fidelity Graph Database
url: https://buaq.net/go-146766.html
source: unSafe.sh - 不安全
date: 2023-01-27
fetch_date: 2025-10-04T04:56:42.697775
---

# GUAC - Aggregates Software Security Metadata Into A High Fidelity Graph Database

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

![](https://8aqnet.cdn.bcebos.com/9e35e5622f829b1cfdc7418f1524d6f8.jpg)

GUAC - Aggregates Software Security Metadata Into A High Fidelity Graph Database

Note: GUAC is under active development - if you are interested in contributing, please loo
*2023-1-26 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146766.htm)
阅读量:24
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgEtOzw7jZvX6v0V6NjRX0XDPlWLyEvEHCLiQ5pR6V3WSoZHaec8CDnDQFqUA7YcHWHxPFaEmRBI_qIEyg417P5P2u5Br4e3rVTlj8SzoVZV5cju1uCi1UecMMmRMgv0f9O2NOXYhnt-PmfFStnSt9XeEFS6yslL8fCBUBPGgkf9PCKjBL4yMUemG6d5w=w258-h400)](https://blogger.googleusercontent.com/img/a/AVvXsEgEtOzw7jZvX6v0V6NjRX0XDPlWLyEvEHCLiQ5pR6V3WSoZHaec8CDnDQFqUA7YcHWHxPFaEmRBI_qIEyg417P5P2u5Br4e3rVTlj8SzoVZV5cju1uCi1UecMMmRMgv0f9O2NOXYhnt-PmfFStnSt9XeEFS6yslL8fCBUBPGgkf9PCKjBL4yMUemG6d5w)

**Note:** GUAC is under [active](https://www.kitploit.com/search/label/Active "active") development - if you are interested in contributing, please look at [contributor guide](https://github.com/guacsec/guac/blob/main/CONTRIBUTING.md "contributor guide") and the ["express interest" issue](https://github.com/guacsec/guac/issues/1 "express interest issue")

Graph for Understanding Artifact Composition (GUAC) aggregates software security [metadata](https://www.kitploit.com/search/label/Metadata "metadata") into a high fidelity graph database—normalizing entity identities and mapping standard relationships between them. Querying this graph can drive higher-level organizational outcomes such as audit, policy, risk management, and even developer assistance.

Conceptually, GUAC occupies the “aggregation and synthesis” layer of the software [supply chain](https://www.kitploit.com/search/label/Supply%20Chain "supply chain") [transparency](https://www.kitploit.com/search/label/Transparency "transparency") logical model:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjCOXt8ov6H6LlHg1Im-TtNFlplAFlpYR88jEg4XfgjrsbBEvtvjQDly-fb-6cJi-h9IMIdMqpy42MF-b2VWTkLj6bYjT6vK1dXJUvu91u3pLSdKh4n4R-fI4_qb1gmexfzz1lNUUpxIRCe--C-GO5WCaNJTwJogdXYa9sILVz1k-JOQ__qT_jk0ZmHaw=w640-h500)](https://blogger.googleusercontent.com/img/a/AVvXsEjCOXt8ov6H6LlHg1Im-TtNFlplAFlpYR88jEg4XfgjrsbBEvtvjQDly-fb-6cJi-h9IMIdMqpy42MF-b2VWTkLj6bYjT6vK1dXJUvu91u3pLSdKh4n4R-fI4_qb1gmexfzz1lNUUpxIRCe--C-GO5WCaNJTwJogdXYa9sILVz1k-JOQ__qT_jk0ZmHaw)

A few examples of questions answered by GUAC include:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiJJotPbN2MSCa1bnXRrEWVJm_tPJ9TruIYiTK6yvhmotDWdfkXsVfOVmsbG8PpOXB93OLJDJrtSH0WhhSPs0pfOTBOzSNMNLgXfvCmEbFnzm8bFy0x-4C33IYH4MUq5NCVKv0hIuB8vKvBsIToHtbj36Z3F258SMn6MtDsBUB1y6eowcKoOb4cZxXBcw=w640-h290)](https://blogger.googleusercontent.com/img/a/AVvXsEiJJotPbN2MSCa1bnXRrEWVJm_tPJ9TruIYiTK6yvhmotDWdfkXsVfOVmsbG8PpOXB93OLJDJrtSH0WhhSPs0pfOTBOzSNMNLgXfvCmEbFnzm8bFy0x-4C33IYH4MUq5NCVKv0hIuB8vKvBsIToHtbj36Z3F258SMn6MtDsBUB1y6eowcKoOb4cZxXBcw)

## Quickstart

Refer to the [Setup + Demo](https://github.com/guacsec/guac/blob/main/SETUP.md "Setup + Demo") document to learn how to prepare your environment and try GUAC out!

## Architecture

Here is an overview of the architecture of GUAC:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi5DEW3s8Fs02PYifWaxCs5NZ4morOKYKY96VPr985dzhAEj7hrGkVFKMJFA7ipFjAthiyP5FH1-NRGyF2mIj2roQBe0xLXArZKq4_j1oegbW25a2g4LCsrCsCBE_BLEWzf0ceU8DSXqDQKpJcEIPH7xSmqFqJn0DQNiKX6LF-Ud7jpHTM0n-WeVRQ_Zw=w640-h338)](https://blogger.googleusercontent.com/img/a/AVvXsEi5DEW3s8Fs02PYifWaxCs5NZ4morOKYKY96VPr985dzhAEj7hrGkVFKMJFA7ipFjAthiyP5FH1-NRGyF2mIj2roQBe0xLXArZKq4_j1oegbW25a2g4LCsrCsCBE_BLEWzf0ceU8DSXqDQKpJcEIPH7xSmqFqJn0DQNiKX6LF-Ud7jpHTM0n-WeVRQ_Zw)

## Supported input formats

* [CycloneDX](https://github.com/CycloneDX/specification "CycloneDX")
* [Dead Simple Signing Envelope](https://github.com/secure-systems-lab/dsse "Dead Simple Signing Envelope")
* [In-toto ITE6](https://github.com/in-toto/attestation "In-toto ITE6")
* [OpenSSF Scorecard](https://github.com/ossf/scorecard "OpenSSF Scorecard")
* [SLSA](https://github.com/slsa-framework/slsa "SLSA")
* [SPDX](https://spdx.dev/specifications/ "SPDX")

## Additional References

* [GUAC Intro Slides](https://docs.google.com/presentation/d/1WF4dsJiwR6URWPgn1aiHAE3iLVl-oGP4SJRWFpcOlao/edit#slide=id.p "GUAC Intro Slides")
* [GUAC Design Doc](https://docs.google.com/document/d/1N5x0HErb-kmCPgG9M8TwBEOGIVU54clqp_X4KhtNJI8/edit "GUAC Design Doc")

## Communication

We encourage discussions to be done on github issues. We also have a [public slack channel](https://openssf.slack.com/archives/C03U677QD46 "public slack channel") on the OpenSSF slack.

For security issues or code of conduct concerns, an e-mail should be sent to [[email protected]](http://www.kitploit.com/cdn-cgi/l/email-protection#d8bfadb9bbf5b5b9b1b6acb9b1b6bdaaab98bfb7b7bfb4bdbfaab7ada8abf6bbb7b5 "guac-maintainers@googlegroups.com").

## Governance

Information about governance can be found [here](https://github.com/guacsec/guac/blob/main/GOVERNANCE.md "here").

GUAC - Aggregates Software Security Metadata Into A High Fidelity Graph Database
![GUAC - Aggregates Software Security Metadata Into A High Fidelity Graph Database](https://blogger.googleusercontent.com/img/a/AVvXsEgEtOzw7jZvX6v0V6NjRX0XDPlWLyEvEHCLiQ5pR6V3WSoZHaec8CDnDQFqUA7YcHWHxPFaEmRBI_qIEyg417P5P2u5Br4e3rVTlj8SzoVZV5cju1uCi1UecMMmRMgv0f9O2NOXYhnt-PmfFStnSt9XeEFS6yslL8fCBUBPGgkf9PCKjBL4yMUemG6d5w=s72-w258-c-h400)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/guac-aggregates-software-security.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)