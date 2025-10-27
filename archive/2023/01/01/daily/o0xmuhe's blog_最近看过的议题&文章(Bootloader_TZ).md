---
title: 最近看过的议题&文章(Bootloader/TZ)
url: https://o0xmuhe.github.io/2022/12/31/%E6%9C%80%E8%BF%91%E7%9C%8B%E8%BF%87%E7%9A%84%E8%AE%AE%E9%A2%98-%E6%96%87%E7%AB%A0-Bootloader-TZ/
source: o0xmuhe's blog
date: 2023-01-01
fetch_date: 2025-10-04T02:50:36.577800
---

# 最近看过的议题&文章(Bootloader/TZ)

* [Home](/)
* [Articles](/archives/)
* [About](/about/)
* [Categories](/categories/)
* [Tags](/tags/)
* [Search](/search)
* [RSS](/atom.xml)

Previous post
Next post
Back to top
Share post

1. [1. 背景](#%E8%83%8C%E6%99%AF)
2. [2. Security Boot & Bootloader相关](#Security-Boot-amp-Bootloader%E7%9B%B8%E5%85%B3)
3. [3. TZ相关](#TZ%E7%9B%B8%E5%85%B3)
4. [4. 其他](#%E5%85%B6%E4%BB%96)
5. [5. 感想](#%E6%84%9F%E6%83%B3)

# 最近看过的议题&文章(Bootloader/TZ)

muhe

2022-12-31

[阅读笔记](/categories/%E9%98%85%E8%AF%BB%E7%AC%94%E8%AE%B0/)

[Bootloader](/tags/Bootloader/), [TZ](/tags/TZ/)

## 背景

最近看了一些`Bootloader&TZ`以及相关的议题，主要是ARM架构下的内容；正好这几个月我的`Leader`领着我们组一起学习`ARMv8&v9`架构相关的知识，在阅读这些材料的时候给我提供了不少的帮助，让我理解起来更加容易，也算是变相检验学习成果咯。

于是我便有了这样的感慨 :)

![image-20221231181650825](https://my-own-image.oss-cn-beijing.aliyuncs.com/img/image-20221231181650825.png)

## Security Boot & Bootloader相关

没看完的材料就是TBD的状态 :(

* [没钥匙也要拧开BOOTLOADER的锁](https://github.com/hhj4ck/BLUnlock/blob/master/ISC2017.pdf) - Guanxing Wen, ISC, 2017

  > 厂商在ABL里增加unlock bl验证逻辑，针对这部分的安全性研究
* [启动链脆弱性分析](https://github.com/hhj4ck/BLUnlock/blob/master/ISC2018.pdf) - Guanxing Wen, ISC, 2018

  > 三星的安全启动分析，攻击TZ实现绕过锁屏码; reference里 `@NWMonster 三星的分析和利⽤` 我也没找到:( 可惜
* [EL3 Tour: Get The Ultimate Privilege of Android Phone](https://speakerdeck.com/hhj4ck/el3-tour-get-the-ultimate-privilege-of-android-phone) - Guanxing Wen, Infiltrate, 2019

  > 华为的安全启动探究，利用bootrom漏洞实现打破信任链，从而实现拿到EL1、EL3的权限，然后攻击TEE，非常精彩的议题；需要ARMv8架构相关的知识，理解起来会更轻松 :)
* [Checkmate Mate30](https://raw.githubusercontent.com/hhj4ck/checkm30/master/checkm30.pdf) - Slipper & Guanxing Wen, *MOSEC*, 2021

  > 华为Mate30的BootROM漏洞挖掘&利用，和之前EL3 Tour那个类似；但是华为通过OTA修了这个洞也是很神奇，~~不知道是不是用的ARM FPB特性做的~~
* MediAttack - break the boot chain of MediaTek SoC - neoni, MOSEC, 2022

  > MTK安全启动分析以及BootROM漏洞挖掘&利用，打破信任链后可以实现对任意分区读写、解密数据等，配合[mtk-bypass](https://github.com/MTK-bypass/bypass_utility_)阅读体验更好
* [How To Tame Your Unicorn](https://raw.githubusercontent.com/TaszkSecLabs/presentations/main/US-21-Komaromy-How-To-Tame-Your-Unicorn.pdf) - Daniel Komaromy & Lorant Szabo, *Black Hat USA*, 2021

  > 打华为的基带，顺带BootROM的漏洞，配合白皮书阅读体验更佳
* [Test Point Break: Analysis of Huawei’s OTA Fix For BootROM Vulnerabilities](https://labs.taszk.io/articles/post/huawei_kirin990_bootrom_patch/) - Taszk Lab, 2021

  > `How to Tame Your Unicorn`BH议题中BootROM漏洞 OTA fix后的分析，探究华为的修复手法。

  + [CVE-2021-22434: Huawei Arbitrary Write in BootROM USB Stack](https://labs.taszk.io/blog/post/bootrom_head_resend/)
  + [CVE-2021-22429: Huawei Buffer Overflow in BootROM USB Stack](https://labs.taszk.io/blog/post/bootrom_usb/)
* [Your Peripheral Has Planted Malware — An Exploit of NXP SOCs Vulnerability](https://www.youtube.com/watch?v=0_E2NxpCAfw) - Yuwei ZHENG, Shaokun CAO, Yunding JIAN, Mingchuang QIN, Defcon26

  > NXP SOC安全启动的错误实现导致可以打破信任链植入恶意程序
* [Top 10 Secure Boot mistakes](https://hardwear.io/usa-2019/presentations/Top-10-Secure-Boot-Mistakes-v1.1-hardwear-io-usa-2019-jasper-van-woudenberg.pdf) - Jasper van Woudenberg, hardware.io, 2019

  > 这个算是一个总结性质的分享，总结了常见的安全启动的错误实现，已经相关的例子，对于BSP来说是个不错的参考材料？
* [Attack Secure Boot of SEP](https://raw.githubusercontent.com/windknown/presentations/master/Attack_Secure_Boot_of_SEP.pdf) - Xu Hao of Team Pangu, MOSEC, 2020

  > TBD
* [Breaking Secure Bootloaders](https://i.blackhat.com/USA21/Wednesday-Handouts/us-21-Breaking-Secure-Bootloaders.pdf) Iskuri1, BH USA, 2021

  > TBD
* [eshared的pixel6\_bootloader安全研究系列](https://eshard.com/posts/pixel6_bootloader)

  > Pixel6修复了一系列bootloader的漏洞，作者通过bindiff找到，并深入研究了这些漏洞

## TZ相关

没看完的材料就是TBD的状态 :(

* [Attacking your “Trusted Core” Exploiting TrustZone on Android](https://www.blackhat.com/docs/us-15/materials/us-15-Shen-Attacking-Your-Trusted-Core-Exploiting-Trustzone-On-Android.pdf) - Di Shen (@returnsme), BH USA, 2015

  > 华为Mate7的安全研究，从REE打到TEE
* Blue Pill for Your Phone - Oleksandr Bazhaniuk & Yuriy Bulygin, BH USA, 2017

  > Nexus&Pixel EL2的研究
* [BREAKING SAMSUNG’S ARM TRUSTZONE](https://i.blackhat.com/USA-19/Thursday/us-19-Peterlin-Breaking-Samsungs-ARM-TrustZone.pdf) - Maxime Peterlin & Alexandre Adamski & Joffrey Guilbon, BH USA, 2019

  > TBD
* 暗涌2020-小米5c中国产自研手机芯片澎湃S1 - Slipper, MOSEC, 2020

  > 没找到Slide :( 只能结合[evilpan](https://evilpan.com/2020/07/25/mosec2020/)的博客来理解了:) 一套fullchain exploit，从EL0一路打到S-EL1

## 其他

涉及底层的内容，也是上面学习上面内容的时候找到的，归类到这里 :)

* [2212\_huawei-security-hypervisor](https://blog.impalabs.com/2212_huawei-security-hypervisor.html)

  > 详细地分析了华为的EL2实现，这篇详细到什么程度呢？我认为这是一篇生动形象的计算机体系结构课程 :) 非常值得阅读，全搞明白对ARM体系的理解要求很高。
* [Attacking Samsung RKP](https://blog.impalabs.com/2111_attacking-samsung-rkp.html)

  > TBD
* [A Samsung RKP Compendium](https://blog.impalabs.com/2101_samsung-rkp-compendium.html)

  > TBD
* [2212\_advisory\_huawei-secure-monitor](https://blog.impalabs.com/2212_advisory_huawei-secure-monitor.html)

  > 华为EL3 漏洞挖掘&利用，可以配合闻观行的 `EL3 Tour`  议题阅读
* [fred’s notes](https://fredericb.info/archives.html)

  > bootloader、security boot相关的博客都值得阅读
* [**Exploiting Qualcomm EDL Programmers**系列](https://alephsecurity.com/2018/01/22/qualcomm-edl-1)

  + 一共五篇，从网上泄漏的firehose开始研究，探究高通的安全启动、firehose功能，后面利用某些设备实现上的缺陷(开了secureboot的设备的firehose依然实现了peek、poke)实现内存读写，进而在不同设备上实现代码执行等操作。
* [attacking-titan-m-with-only-one-byte](https://blog.quarkslab.com/attacking-titan-m-with-only-one-byte.html)

  > TBD

## 感想

1. 这些内容基本上都是围绕ARM架构做的安全研究，在学习的过程中会不自觉的拿optee来做对比，好让自己更容易理解这些内容
2. 看了这些材料以及大佬分享的时间，这些研究真的太有意思了，我怎么没有早点看到
3. 行业原因自然形成的壁垒，在做底层的研究的时候真的很明显，比如BootROM，如果有个手册的话…MTK那个BootROM我看过，这要没手册也太难分析了😭
4. 持续学习非常重要，正反馈让人觉得很爽 😄

---

恰好今天正好是2022年最后一天，转到IoT组也一年多了，能感受到自己在一点一点进步:

* 技术
* 软技能(沟通协作、写文档)

非常感谢玉伟对我的帮助和指导，在对本篇文章中资料的学习过程中，总能和之前我学习or工作中遇到的东西呼应起来，我也想起了和玉伟`one on one`的时候他给我讲学习方法、以及他个人是怎么做阅读的，醍醐灌顶来形容我现在的感受可能会比较恰当 :)

**希望23年可以进步更多一些，日拱一卒，功不唐捐。**

Please enable JavaScript to view the comments.

* [Home](/)
* [Articles](/archives/)
* [About](/about/)
* [Categories](/categories/)
* [Tags](/tags/)
* [Search](/search)
* [RSS](/atom.xml)

1. [1. 背景](#%E8%83%8C%E6%99%AF)
2. [2. Security Boot & Bootloader相关](#Security-Boot-amp-Bootloader%E7%9B%B8%E5%85%B3)
3. [3. TZ相关](#TZ%E7%9B%B8%E5%85%B3)
4. [4. 其他](#%E5%85%B6%E4%BB%96)
5. [5. 感想](#%E6%84%9F%E6%83%B3)

Menu
TOC
Share
Top

Copyright ©
2015-2024
muhe

* [Home](/)
* [Articles](/archives/)
* [About](/about/)
* [Categories](/categories/)
* [Tags](/tags/)
* [Search](/search)
* [RSS](/atom.xml)