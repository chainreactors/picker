---
title: Reverse Engineering Tiktok's VM Obfuscation (Part 1)
url: https://buaq.net/go-141281.html
source: unSafe.sh - 不安全
date: 2022-12-25
fetch_date: 2025-10-04T02:29:03.347515
---

# Reverse Engineering Tiktok's VM Obfuscation (Part 1)

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

![](https://8aqnet.cdn.bcebos.com/f02a1d21d3cc1d6667668b14230ebab2.jpg)

Reverse Engineering Tiktok's VM Obfuscation (Part 1)

r/PlantedTankMy 25g high-tech cuber/PlantedTankSometimes you have to lay on the floor in order to di
*2022-12-24 23:10:29
Author: [www.reddit.com(查看原文)](/jump-141281.htm)
阅读量:48
收藏*

---

* [![Subreddit Icon](https://styles.redditmedia.com/t5_2szbf/styles/communityIcon_rgy52e5xhz761.png)

  ![](https://b.thumbs.redditmedia.com/GHB0QSAWHCvuPxSRQMJb-xa9wyMfNO8XB7y8TzcLmjY.jpg)

  My 25g high-tech cube](https://www.reddit.com/r/PlantedTank/comments/abmr6f/my_25g_hightech_cube/)
* [![Subreddit Icon](https://styles.redditmedia.com/t5_2szbf/styles/communityIcon_rgy52e5xhz761.png)r/PlantedTank

  ![](https://b.thumbs.redditmedia.com/9939Rrp8sL2ctk6A4P-xfxE545XvY8lLQiSIP_HB2vc.jpg)

  Sometimes you have to lay on the floor in order to dive...](https://www.reddit.com/r/PlantedTank/comments/aa11yc/sometimes_you_have_to_lay_on_the_floor_in_order/)
* [![Subreddit Icon](https://styles.redditmedia.com/t5_2szbf/styles/communityIcon_rgy52e5xhz761.png)r/PlantedTank

  ![](https://a.thumbs.redditmedia.com/u0o7WWVMqnNzDiL2sFoXG1HmvJxY46UQerjnSIc9aB0.jpg)

  Thank you for your service](https://www.reddit.com/r/PlantedTank/comments/arohq3/thank_you_for_your_service/)
* [![Subreddit Icon](https://styles.redditmedia.com/t5_2rfae/styles/communityIcon_3dfy7vp21qw81.png)r/farscape

  Farscape - Just the right amount of crazy (Possible...](https://www.reddit.com/r/farscape/comments/51op1x/farscape_just_the_right_amount_of_crazy_possible/)
* [Blink is a virtual machine for running...](https://www.reddit.com/r/ReverseEngineering/comments/zp5kje/blink_is_a_virtual_machine_for_running/)
* [Convolutional Neural Network for Reverse Engineering](https://www.reddit.com/r/ReverseEngineering/comments/ztoft6/convolutional_neural_network_for_reverse/)
* [GhidraEmu - a plugin that allows you to easily deal with...](https://www.reddit.com/r/ReverseEngineering/comments/zpwyhh/ghidraemu_a_plugin_that_allows_you_to_easily_deal/)
* [The Hex-Rays plugin repository.](https://www.reddit.com/r/ReverseEngineering/comments/zr4phz/the_hexrays_plugin_repository/)
* [Reverse Engineering UPX with Parallels and OllyDbg on...](https://www.reddit.com/r/ReverseEngineering/comments/zslf83/reverse_engineering_upx_with_parallels_and/)
* [A journey into IoT - Unknown Chinese alarm - Part 4...](https://www.reddit.com/r/ReverseEngineering/comments/zrpmi5/a_journey_into_iot_unknown_chinese_alarm_part_4/)
* [Free Reverse Engineering, Pen-Testing, And Low Level Dev...](https://www.reddit.com/r/ReverseEngineering/comments/zplvyu/free_reverse_engineering_pentesting_and_low_level/)
* [A Reverse Engineering Education Needs Analysis Survey](https://www.reddit.com/r/ReverseEngineering/comments/zp4a4z/a_reverse_engineering_education_needs_analysis/)
* [Android Obfuscation Challenge](https://www.reddit.com/r/ReverseEngineering/comments/zpj8g7/android_obfuscation_challenge/)
* [Capstone disassembly/disassembler framework: Core (Arm...](https://www.reddit.com/r/ReverseEngineering/comments/zr839n/capstone_disassemblydisassembler_framework_core/)

Reddit Inc © 2022. All rights reserved

文章来源: https://www.reddit.com/r/ReverseEngineering/comments/zubos7/reverse\_engineering\_tiktoks\_vm\_obfuscation\_part\_1/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)