---
title: Win10 U盘防病毒科普
url: http://blog.nsfocus.net/win10-u/
source: 绿盟科技技术博客
date: 2023-03-18
fetch_date: 2025-10-04T09:57:59.514385
---

# Win10 U盘防病毒科普

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Win10 U盘防病毒科普

### Win10 U盘防病毒科普

[2023-03-17](https://blog.nsfocus.net/win10-u/ "Win10 U盘防病毒科普")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,116

A君在B单位做实验，有些实验数据需要从B单位C机上复制到自己的U盘中。事后B单位同仁们告诉A，C机有病毒，应该用空U盘接入C机。B单位同仁们都是在各自主机上安装某款杀毒软件，U盘插回各自主机时会检查一番。但C机本身未装任何杀毒软件，为什么C机本身不装杀毒软件，原因不明，据说有某些规定，C机上病毒从何而来，不知。A君请我检查U盘，果然中招。

在C机带毒的情况下，是否用空U盘接入，意义有限，但不是全无意义。在本例中，A君U盘中所有exe、xlsm被感染。那些exe只能删了，xlsm本质上是压缩包，可以清除病毒部分而保留数据。假设用空U盘接入，至少不会破坏已有exe、xlsm等文件，发现中招时，可以格式化或全盘删除，不必费心分拣资料。

有个重要安全原则，去打印店、别人电脑、公用电脑插U盘，绝对不能用存放了大量有用资料的U盘，必须得是一个可以随时格式化、全盘删除的过渡型U盘，这是个非常重要的安全原则，很多人图方便、图省事，直接违反。打印店可能容易引起警惕，别人电脑、公用电脑就经常被忽视，对自己来说，这三者是一回事，皆为风险区。所以，IT小白建议始终用空U盘接入非本人主机。

空U盘接入的意义仅限于此，并非用空U盘接入C机就能避免病毒传播至本机。有些病毒会将某个exe的图标刻意改成文件夹图标样式，大多数人的资源管理器并未设置始终显示扩展名、始终显示文件类型，看到这样的exe会以为是目标，双击进入，实际变成双击执行exe，这个中招过程与最初是否用空U盘完全无关。A君电脑已经始终显示扩展名、始终显示文件类型，但这样还不够，要养成先看文件类型再打开的习惯，看到是exe仍然双击打开，这种属于无可求药型。

在资源管理器名称栏上右键，勾选”类型”，将类型列调至名称列右侧。exe的类型列是”应用程序”，目录的类型列是”文件夹”，无论exe的图标怎么变，类型列会暴露它。

————————————————————————–
选项
查看
隐藏已知文件类型的扩展名 (默认是勾选，现在清空)
————————————————————————–

显示扩展名只是辅助手段，有被视觉欺骗的可能。有些特殊字节出现在文件名中时，从视觉效果上看到的可能是另一个让你觉得无害的文件名。这块我没研究过，想来与LRO、RLO序列相关，参看

How to use Unicode controls for bidi text
https://www.w3.org/International/questions/qa-bidi-unicode-controls

还是尽可能检查文件类型为妙。即便上面都做得很好，仍有可能中招，U盘支持接入后自动运行某个程序的功能，放狗搜”autorun.inf”了解更多细节。现代Windows可能从根上对此有预防措施，若不放心，可以手动关动这种自动运行功能。有多种技术方案关闭U盘的自动运行，只说Win10的两种

————————————————————————–
控制面板
所有控制面板项
自动播放
把所有行都调成”不执行操作”
————————————————————————–
设置
设备
自动播放
————————————————————————–

前面说的几点都做到，U盘将病毒传至本机的风险已经很小。对于普通用户，不建议在Win10上安装第三方杀毒软件，Win10自带”Microsoft Defender”，实时保护默认是打开的。U盘接入本机时，实时保护可能起作用，若不放心，右键选中U盘，使用”Microsoft Defender”扫描一下。一般exe有问题，直接就搂中，xlsm这类有问题时，可能第一遍扫描会漏，原因不明，那就多扫一次。无论扫不扫，进入有问题的目录时，实时保护都大概率会搂中，不然为什么叫实时保护呢，所以可以人工遍历一下U盘，尤其是子目录，于是空U盘的优势得到加强。

本次科普面向非IT人士，只聚焦于U盘接入Win10的风险及应对措施。对目标人群而言，前述相关操作还是太复杂，人是靠不住的，得靠软件体系，普通用户千万不要裸奔，杀毒软件必装，实时保护必开，万一发现异常，切勿自行处置，第一时间寻求专业支持。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/microsoftmarch/)

[Next](https://blog.nsfocus.net/adobe-coldfusion/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)