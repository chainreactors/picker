---
title: 4h入门PHP代码审计之反序列化
url: https://buaq.net/go-136921.html
source: unSafe.sh - 不安全
date: 2022-11-24
fetch_date: 2025-10-03T23:37:00.126855
---

# 4h入门PHP代码审计之反序列化

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

![](https://8aqnet.cdn.bcebos.com/11e75445163fbfeee446dab5cbecd523.jpg)

4h入门PHP代码审计之反序列化

代码审计顾名思义就是对源代码进行检查，寻找代码中的bug和安全缺陷，检查PHP源代码中的缺点和错误信息，分析并找到这些问题引发的安全漏洞。序列化就是把实体对象状态按照一定的格式写入到有序字节流，当要用
*2022-11-23 18:4:8
Author: [mp.weixin.qq.com(查看原文)](/jump-136921.htm)
阅读量:26
收藏*

---

代码审计顾名思义就是对源代码进行检查，寻找代码中的bug和安全缺陷，检查PHP源代码中的缺点和错误信息，分析并找到这些问题引发的安全漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5NOyDG7AHPPSlMl1DdVNVuWsJbQI683LpFdj7boY1Kbfd5xj7RiaGeySCszam7AvMVmKLWdVm95Q/640?wx_fmt=jpeg)

序列化就是把实体对象状态按照一定的格式写入到有序字节流，当要用到时就通过反序列化来重建对象，恢复对象状态，这样就可以很方便的存取数据和传输数据。

但是这对我们小白来说，可能就是一个“代码审计之从入门到放弃”的悲惨故事，为了满足广大用户的需求，我们最新推出《4h入门PHP代码审计之反序列化》在线课程，帮你快速掌握PHP的调试技巧及反序列化EXP的编写，实战中“避坑”！

![](https://mmbiz.qpic.cn/mmbiz_png/ZN1xiarzMc8oCQowagb1nlL3nRfaHW67eickDGd25WCMxw3oNKouamvCg1Hg1J88CX0g7WO1qcoiaQWwnhXibibqcKQ/640?wx_fmt=png)

课程简介

![](https://mmbiz.qpic.cn/mmbiz_png/t8HEWljw1E7dMrqROMVthRC4Xic9NUPnS7d3Uh4X7T8aiaLpcsHyT6gTYBQdibgSAJn92ibia0oSmvTu60bg5roBt6w/640?wx_fmt=png)

很多人难以入门PHP代码调试、难以入门的Thinkphp5框架反序列化或是在学习的过程中走弯路，本课程可以解决这些问题。从0到1的反序列化，通过此课程，学员可以入门代码审计，并掌握PHP代码审计的技巧。

![](https://mmbiz.qpic.cn/mmbiz_png/ZN1xiarzMc8oCQowagb1nlL3nRfaHW67eickDGd25WCMxw3oNKouamvCg1Hg1J88CX0g7WO1qcoiaQWwnhXibibqcKQ/640?wx_fmt=png)

技术储备

![](https://mmbiz.qpic.cn/mmbiz_png/t8HEWljw1E7dMrqROMVthRC4Xic9NUPnS7d3Uh4X7T8aiaLpcsHyT6gTYBQdibgSAJn92ibia0oSmvTu60bg5roBt6w/640?wx_fmt=png)

（1）了解本地网站的搭建

（2）简单理解PHP语言

（3）了解Web安全

![](https://mmbiz.qpic.cn/mmbiz_png/ZN1xiarzMc8oCQowagb1nlL3nRfaHW67eickDGd25WCMxw3oNKouamvCg1Hg1J88CX0g7WO1qcoiaQWwnhXibibqcKQ/640?wx_fmt=png)

讲师介绍

![](https://mmbiz.qpic.cn/mmbiz_png/t8HEWljw1E7dMrqROMVthRC4Xic9NUPnS7d3Uh4X7T8aiaLpcsHyT6gTYBQdibgSAJn92ibia0oSmvTu60bg5roBt6w/640?wx_fmt=png)

张登旸(Yang\_99)

0RAYS战队主力web手，曾获D^3CTF第五名，XCTF-final优胜奖，全国大学生信息安全竞赛二等奖等。

![](https://mmbiz.qpic.cn/mmbiz_png/ZN1xiarzMc8oCQowagb1nlL3nRfaHW67eickDGd25WCMxw3oNKouamvCg1Hg1J88CX0g7WO1qcoiaQWwnhXibibqcKQ/640?wx_fmt=png)

课程目录

![](https://mmbiz.qpic.cn/mmbiz_png/t8HEWljw1E7dMrqROMVthRC4Xic9NUPnS7d3Uh4X7T8aiaLpcsHyT6gTYBQdibgSAJn92ibia0oSmvTu60bg5roBt6w/640?wx_fmt=png)

**第一章 环境安装**

课时一  vscode

课时二  phpstrom

**第二章  PHP反序列化漏洞讲解**

课时一  原生类

课时二  trick

课时三  PHP魔术方法

课时四  POP链挖掘

课时五  反序列化字符串逃逸

课时六  Phar反序列化

**第三章  含有命名空间的POP链**

课时一  CL4（1）

课时二  CL4（2）

课时三  CL4（3）

课时四  CL4（4）

课时五  Thinkphp1

课时六  Thinkphp2

课时七  Thinkphp3

课时八  Laravel

![](https://mmbiz.qpic.cn/mmbiz_png/ZN1xiarzMc8oCQowagb1nlL3nRfaHW67eickDGd25WCMxw3oNKouamvCg1Hg1J88CX0g7WO1qcoiaQWwnhXibibqcKQ/640?wx_fmt=png)

立即报名

![](https://mmbiz.qpic.cn/mmbiz_png/t8HEWljw1E7dMrqROMVthRC4Xic9NUPnS7d3Uh4X7T8aiaLpcsHyT6gTYBQdibgSAJn92ibia0oSmvTu60bg5roBt6w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HDfaqP4l84ybEibzX7bZ1vJ5SyQ9S7qYCE7D0wq2rVgnLibnfSH7zAra4FLEDicGD9jgwckAzrRTQmQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HDfaqP4l84ybEibzX7bZ1vJflhibajOwLHewm4OsQp3WcucaTqajXwA8KbZtnvw7zpRDRJ6SsvtA5g/640?wx_fmt=png)

**扫一扫，128元即可解锁精品课程**

注意：报名成功后请添加工作人员微信：kanxuecom，发送订单截图，进入课程学员交流群。

摸索不到PHP代码调试技巧？

4h带你快速入门，实战中避坑

实现思维方式+动手能力的跃迁

![](https://mmbiz.qpic.cn/mmbiz_png/KLoTw1Op24K7bYlV0ty3cYaXKEJ4LukvDSWzMiawENwjkzichAIcDuC1uBxuMfSj29gpevgLGPPeMeHCwKyGiaZ5w/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HDfaqP4l84ybEibzX7bZ1vJflhibajOwLHewm4OsQp3WcucaTqajXwA8KbZtnvw7zpRDRJ6SsvtA5g/640?wx_fmt=png)

快来加入课程学习吧～

**一步一步****积累技能后，你总会无坚不摧的**

![](https://mmbiz.qpic.cn/mmbiz_gif/b96CibCt70iaa8r7PJoyAtlfHAKe8RosE3wYVKBac55p1HPBJHZS42ywnG4yYtD3jo9A9e5kawBZs4IE6R1C4wibw/640?wx_fmt=gif)

- End -

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Faib6UHFjZOMX904fAH74mNU5Xc7bhic2ygvHS2FEiazKAVHdhiaibI9R07vf5zibyDrPoOicPGy9R3W4PA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458440719&idx=3&sn=f781bb3022d0d8f99b52aa83143576a3&chksm=b18fe48586f86d934b32c02366d14492baf9d0106d5407d836936d8250f882c64c4f239ca9b3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_png/fvdn3AaxR6sldoK7VdUhCXiaQdAvKhF8APVg8MqccDc4t8UicH8bMiaeklzxeqlVicwMWxghHlG0OH6pDHV2ibk5iaQQ/640?wx_fmt=png)

点个在看你最好看

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaa62yRh8ZMicGSoozvuoh0ibFegWJkDHwgsiaiayAQzSOLMlK8Lcs7qAU4DwpqibFRiaLH3PDicXdMrO4hibw/640?wx_fmt=png)

点击阅读原文即可购买

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MjM5NTc2MDYxMw==&mid=2458484895&idx=3&sn=26677dbd86c59221bccee0b96cb81f11&chksm=b18eb01586f93903d5a72a8ae08b5119b5233e6a40211815b11a5c593726922e84b20dba09c1#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)