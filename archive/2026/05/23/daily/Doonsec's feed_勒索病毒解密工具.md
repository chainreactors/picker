---
title: 勒索病毒解密工具
url: https://mp.weixin.qq.com/s/BrQDvhtcu3qsQoeumZs8zA
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:54:56.075841
---

# 勒索病毒解密工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJckDT7eIfPbHSFRm93dBuw19ZRWhIBNohMkYp985dHowKVyPgZclJ5uj0ibibaGxQO5GRf0xSIgCbmDyoXQa7C6tfW3sibhYsB38/0?wx_fmt=jpeg)

# 勒索病毒解密工具

原创

网安工具库
网安工具库

网安工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Misc-Galaxysail：一站式 CTF Misc 杂项分析工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487462&idx=1&sn=ffff5623e4f5d4b6770285a48eb73318&scene=21#wechat_redirect)

·[面向 jQuery 生态的跨站脚本漏洞检测工具：jQuery-XSS-Scanner-Pro](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487443&idx=1&sn=f5ebb1459908aedf6d1836ca955c1f73&scene=21#wechat_redirect)

·[ShiroExploit：一款Shiro反序列化漏洞一站式综合测试工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487426&idx=1&sn=975d8221cda0e4e8247a7f1a03c4f6cd&scene=21#wechat_redirect)

·[LovelyERes：AWD适用的蓝队综合工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487409&idx=1&sn=5eb3f39619bce25fdf97836aa4c7c16f&scene=21#wechat_redirect)

·[CialloVOL：一键内存文件提取的全面取证工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487408&idx=1&sn=2e6495f9cb8ec2e6cc4319895cb8bb81&scene=21#wechat_redirect)

·[FTK Imager：内存镜像加载和分析的蓝队必备工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247487365&idx=1&sn=9f9acf15553a78432b7e817858cbfa7b&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

近年来，勒索病毒已从“广撒网”式攻击演变为针对高价值目标的精准打击，工控环境（工业控制系统） 因其业务连续性要求高、系统版本偏旧、补丁滞后、隔离困难等特点，成为勒索病毒的重灾区。一旦工控主机（如操作站、工程师站、数据服务器）被加密，轻则生产中断数小时，重则造成数千万级的经济损失及安全事故。

    在应急响应中，我们经常面对一个现实：并非所有勒索病毒都只能支付赎金。大量勒索家族（尤其是变种出现较早、密钥被安全厂商捕获的家族）存在官方的、免费的、有效的解密工具。这些工具大多由卡巴斯基、Emsisoft、Avast、Bitdefender、趋势科技等安全厂商，以及 No More Ransom、Cisco Talos 等非营利/研究机构发布。

    本文汇总了我们在工控应急服务中真实用过、验证过来源的勒索病毒解密工具清单。目的是帮助一线运维人员、安全工程师、应急响应人员在遭遇勒索攻击时：

```
1.快速识别病毒家族；2.精准找到对应的解密器；3.无需支付赎金，尝试恢复关键文件。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**勒索病毒解密工具清单**

说明：

    资源来自网络，注意自行识别工具的安全性

```
1.每个条目格式为：[勒索病毒名称] 解密器名称 — 说明（下载地址）2.部分解密器可处理多个勒索家族（如 Rakhni / Rannoh / Trend Micro 通用解密器），已分别注明。
```

```
1.[777 Ransom] Trend Micro Ransomware解密器用来解密777勒索软件加密的文件 https://success.trendmicro.com/solution/11142212.[AES_NI Ransom] Rakhni解密器用来解密AES_NI勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip3.[Agent.iih Ransom] Rakhni解密器用来解密Agent.iih勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip4.[Alcatraz Ransom] Alcatraz解密器用来解密Alcatraz勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_alcatrazlocker.exe5.[Alpha Ransom] Alphadecrypter解密器用来解密Alpha勒索软件加密的文件 https://www.bleepingcomputer.com/download/alphadecrypter/dl/329/6.[Amnesia Ransom] Amnesia解密器用来解密Amnesia勒索软件加密的文件 https://decrypter.emsisoft.com/download/amnesia7.[Amnesia2 Ransom] Amnesia2解密器用来解密Amnesia2 勒索软件加密的文件 https://decrypter.emsisoft.com/download/amnesia28.[Annabelle Ransom] BDAnnabelleDecryptTool解密器用来解密Annabelle勒索软件加密的文件 http://download.bitdefender.com/am/malware_removal/BDAnnabelleDecryptTool.exe StupidDecryptor解密器用来解密Annabelle勒索软件加密的文件 https://www.bleepingcomputer.com/download/stupiddecryptor/dl/351/9.[Aura Ransom] Rakhni解密器用来解密Aura勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip10.[Aurora Ransom] AuroraDecryptor解密器用来解密Aurora勒索软件加密的文件 https://www.bleepingcomputer.com/download/auroradecrypter/dl/379/ Aurora解密器用来解密Aurora勒索软件加密的文件 https://decrypter.emsisoft.com/download/aurora11.[AutoIt Ransom] Rakhni解密器用来解密AutoIt勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip Rannoh解密器用来解密AutoIt勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip12.[AutoLocky Ransom] Trend Micro Ransomware解密器用来解密AutoLocky勒索软件加密的文件 https://success.trendmicro.com/solution/111422113.[BTCWare Ransom] BTCWare解密器用来解密BTCWare勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_btcware.exe14.[BadBlock Ransom] Trend Micro Ransomware解密器用来解密BadBlock勒索软件加密的文件 https://success.trendmicro.com/solution/111422115.[BarRax Ransom] BarRax解密器用来解密BarRax勒索软件加密的文件 http://blog.checkpoint.com/wp-content/uploads/2017/03/BarRaxDecryptor.zip16.[Bart Ransom] Bart解密器用来解密Bart勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_bart.exe http://download.bitdefender.com/am/malware_removal/BDBartDecryptor.exe17.[BigBobRoss Ransom] Bigbobross fix解密器用来解密BigBobRoss勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_bigbobross.exe18.[Bitcryptor Ransom] Coinvault解密器用来解密Bitcryptor勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip19.[CERBER V1 Ransom] Trend Micro Ransomware解密器用来解密CERBER V1勒索软件加密的文件 https://success.trendmicro.com/solution/111422120.[Chimera Ransom] Rakhni解密器用来解密Chimera勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip21.[Coinvault Ransom] Coinvault解密器用来解密Coinvault勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/CoinVaultDecryptor.zip22.[Cry128 Ransom] Cry128解密器用来解密Cry128勒索软件加密的文件 https://decrypter.emsisoft.com/download/cry12823.[Cry9 Ransom] Cry9解密器用来解密Cry9勒索软件加密的文件 https://decrypter.emsisoft.com/download/cry924.[CrySIS Ransom] Rakhni解密器用来解密CrySIS勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip25.[Cryakl Ransom] Rakhni解密器用来解密Cryakl勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip26.[Crybola Ransom] Rannoh解密器用来解密Crybola勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip27.[Crypt888 Ransom] Crypt888解密器用来解密Crypt888勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_crypt888.exe28.[CryptON Ransom] Crypton解密器用来解密CryptON勒索软件加密的文件 https://decrypter.emsisoft.com/download/crypton29.[CryptXXX V1/2/3/4/5 Ransom] Rannoh解密器用来解密CryptXXX V1/2/3/4/5勒索软件加密的文件 https://success.trendmicro.com/solution/111422130.[CryptoMix Ransom] CryptoMix解密器用来解密CryptoMix勒索软件加密的文件 https://nomoreransom.cert.pl/static/cryptomix_decryptor.exe31.[Cryptokluchen Ransom] Rakhni解密器用来解密Cryptokluchen勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip32.[DXXD Ransom] Trend Micro Ransomware解密器用来解密DXXD勒索软件加密的文件 https://success.trendmicro.com/solution/111422133.[Damage Ransom] Damage解密器用来解密Damage勒索软件加密的文件 https://decrypter.emsisoft.com/download/damage34.[Democry Ransom] Rakhni解密器用来解密Democry勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip35.[Derialock Ransom] Derialock解密器用来解密Derialock勒索软件加密的文件 http://blog.checkpoint.com/wp-content/uploads/2016/12/Derialock-Decryptor.zip36.[Dharma Ransom] Rakhni解密器用来解密Dharma勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rakhnidecryptor.zip37.[EncrypTile Ransom] EncrypTile解密器用来解密EncrypTile勒索软件加密的文件 https://files.avast.com/files/decryptor/avast_decryptor_encryptile.exe38.[Everbe 1.0 Ransom] InsaneCryptDecrypter解密器用来解密Everbe 1.0勒索软件加密的文件 https://www.bleepingcomputer.com/download/insanecrypt-desucrypt-decrypter/dl/369/39.[FenixLocker Ransom] FenixLocker解密器用来解密FenixLocker勒索软件加密的文件 https://decrypter.emsisoft.com/download/fenixlocker40.[FilesLocker v1 and v2 Ransom] FilesLockerDecrypter解密器用来解密FilesLocker v1 and v2勒索软件加密的文件 https://www.bleepingcomputer.com/download/fileslockerdecrypter/dl/378/41.[Fury Ransom] Rannoh解密器用来解密Fury勒索软件加密的文件 http://media.kaspersky.com/utilities/VirusUtilities/EN/rannohdecryptor.zip42.[GandCrab (V1, V4 and V5 up to V5.2 versions) Ransom] BDGandCrabDecryptTool解密器用来解密GandCrab (V1, V4 and V5 up to V5.2 versions)勒索软件加密的文件 http://download.bitdefender.com/am/malware_removal/BDGandCrabDecryptTool.exe43.[GetCrypt Ransom] 解密器用来解密GetCrypt勒索软件加密的文件 https://www.emsisoft.com/decrypter/download/getcrypt44.[Globe1/2/3Ransom] Globe1/2/3解密器用来解密Globe勒索软件加密的文件 https://decrypter.emsisoft.com/download/globe https://decrypter....