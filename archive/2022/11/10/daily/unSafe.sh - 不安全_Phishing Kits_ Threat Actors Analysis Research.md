---
title: Phishing Kits: Threat Actors Analysis Research
url: https://buaq.net/go-134902.html
source: unSafe.sh - 不安全
date: 2022-11-10
fetch_date: 2025-10-03T22:12:57.595236
---

# Phishing Kits: Threat Actors Analysis Research

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

![](https://8aqnet.cdn.bcebos.com/589249494be5609d5e3626feba6213e1.jpg)

Phishing Kits: Threat Actors Analysis Research

IntroductionPhishing kits are tools that dark side experts provide to the community of
*2022-11-9 18:11:11
Author: [marcoramilli.com(查看原文)](/jump-134902.htm)
阅读量:31
收藏*

---

#### Introduction

Phishing kits are tools that dark side experts provide to the community of criminal phishers to facilitate the construction of malicious Web sites. As these kits

Today I am proud to introduce a long time research that Andrea Venturi, Michele Colajanni, Giorgio Valenziano and myself have done on this specific topic. We began 2 years ago by collecting recent phishing kits in my repository ([HERE](https://marcoramilli.com/2022/04/14/from-a-phishing-page-to-a-possible-threat-actor/)), we carry out an initial deterministic analysis of the source code of
the kits to extract the most discriminant features and information about their
principal authors. We then integrate this initial classification through supervised machine learning models.

Thanks to the ground-truth achieved in the
first step, we can demonstrate whether and which machine learning models are
able to suitably classify even the kits adopting novel evasion and obfuscation
techniques that were unseen during the training phase. We compare different
algorithms and evaluate their robustness in the realistic case in which only a
small number of phishing kits are available for training.

We then develop a killchain toolset able to detect novel phishing kits suitable for Cloud Providers. We also studied threat actors, with their key findings and put toghether their probable collaboration by investigating common functionalities and common structures in kits.

The paper right now is available on arxirv [here](https://arxiv.org/abs/2210.08273)

#### Classification Method (taken from paper)

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/10/Screenshot_20221024_084255.jpg?resize=1024%2C209&ssl=1)

We propose a novel classification method aimed to group phishing
kits according to the offered evasion and obfuscation functions. Our goal is to
design a method capable of keeping pace with the continuous introduction of
new techniques in modern kits and to better understand malicious habits of the
principal authors.
The overall methodology consists of the three main phases that are shown
in the previous figure. Phase I involves a static analysis of the content of the phishing kits
and produces a deterministic classification on the basis of the employed evasion
and obfuscation functions. This analysis is able to recognize known techniques,
but it cannot detect new versions or novel functions that phishing kit authors
might introduce. Phase II aims to extract numerous features which summarize
the structure and the functions of each kit along with authors’ design patterns,
and to label them according to the deterministic results. Phase III exploits
all previous information and obtains a probabilistic classification through ML
algorithms. This last classification aims to detect evasive and obfuscated kits
on the basis of structural information of the phishing kits and authors’ design
patterns. This contribution is important because it allows the ML classifiers
to overcome the typical drawbacks of the deterministic approaches (similarly
to that in Phase I) that cannot chase the authors of phishing kits when they
introduce new evasion and obfuscation techniques or modify existing ones.

If you are interested in more details on this, please read the paper ([HERE](https://arxiv.org/abs/2210.08273)).

#### Threat Actor Stereotype main features

After several ML algorithms runs, it looks like many of them agreed on the most important features to address cluster prototypes. In other words, what are the most interesting characteristics to look for specific threat actor. Or, if you prefer, how to recognize a specific Threat Actor among hundres, thousands of phishing kits. We figured out three main chars sets to be involved in classification: 1. Evasion, 2. Obfuscation and 3.Autor Profiling. Finally we had a definitive attribution matrix based on the following main (not uniques, please refer to paper) features

|  |  |  |
| --- | --- | --- |
| **Category** | **Technique** | **Number (Rate)** |
| Evasion | .htaccess | 494 (53%) |
| Evasion | robots.txt | 433 (47%) |
| Evasion | PHP embedded code | 578 (63%) |
| Obfuscation | url\_decode | 174 (46%) |
| Obfuscation | eval | 292 (77%) |
| Obfuscation | Hexadecimal Assignement | 211 (56%) |
| Obfuscation | base64 | 163 (43%) |
| Obfuscation | Obfuscator tools | 34 (9%) |
| Signature | xbalti | 42 (-) |
| Signature | l33bo-phishers | 33 (-) |
| Signature | venza | 23 (-) |
| Signature | medpage | 18 (-) |
| Signature | ex-robots | 16 (-) |

From

Basing our analyses on these extracted features we figured out families and threat actors cards enabling tracing for future evidences and new threat intelligence scenarios. I will disclose threat actors cards as soon as possible in next weeks.

#### Conclusions

Aim of this “post” is to freeze on my digital-diary a quick overview of my last research experience on PhishingKit threat actors. The research took over two years of observations, tracing activities (available [here](https://marcoramilli.com/2020/07/16/introducing-phishingkittracker/)) and machine learning studies. We came out with a new technology able to classify threat actors based on features and to trace them over the years. I can’t wait to share the results on threat actors cards we redacted. Few weeks from now !

![](https://secure.gravatar.com/avatar/effdb721844d68926dd21998fb960493?s=48&d=blank&r=g)

Ethical Hacking, Advanced Targeted Attack Expert and Malware Evasion Expert [View all posts by marcoramilli](https://marcoramilli.com/author/marcoramilli/)

文章来源: https://marcoramilli.com/2022/11/09/phishing-kits-threat-actors-analysis-research/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)