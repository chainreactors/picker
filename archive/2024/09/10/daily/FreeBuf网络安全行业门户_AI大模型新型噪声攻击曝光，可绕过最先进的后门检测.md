---
title: AI大模型新型噪声攻击曝光，可绕过最先进的后门检测
url: https://www.freebuf.com/news/410518.html
source: FreeBuf网络安全行业门户
date: 2024-09-10
fetch_date: 2025-10-06T18:27:45.860411
---

# AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

AI大模型新型噪声攻击曝光，可绕过最先进的后门检测

2024-09-09 10:34:53

所属地 上海

> 罗德岛大学的研究人员在一篇论文中提出了一种新颖的后门攻击方法，利用白高斯噪声的功率谱密度作为触发器，不仅提高了攻击的可行性和普遍性，在模型中都取得了很高的平均攻击成功率，而且不会对非受害者造成显著干扰。

据Cyber Security News消息，研究人员提出了一种噪声攻击（NoiseAttack） 的新型后门攻击方法，该攻击被称为是一种用于图像分类的后门攻击，针对流行的网络架构和数据集实现了很高的攻击成功率，并能绕过最先进的后门检测方法。

实验结果表明，该攻击能有效对抗最先进的防御系统，并在各种数据集和模型上实现较高的攻击成功率。它利用白高斯噪声（White Gaussian Noise）作为触发器，创建了一种针对特定样本的多目标后门攻击，可灵活控制目标标签。

与通常针对单一类别的现有方法不同，该攻击使用具有不同功率谱密度的白高斯噪声作为触发器，并采用独特的训练策略来执行攻击，因此只需最少的输入配置就能针对多个类别进行攻击。

![](https://image.3001.net/images/20240909/1725853216_66de6e205dbd2acfe3614.png!small)不同数据集和模型的攻击性能

这种噪声攻击在研究中被称为是一种用于图像分类的新型后门攻击 ，利用白高斯噪声（WGN）的功率谱密度（PSD）作为训练过程中嵌入的触发器。这种攻击涉及在精心制作的噪声水平和相关目标标签构建的中毒数据集上训练一个后门模型，从而确保模型容易受到触发，导致所需的误分类。

![](https://image.3001.net/images/20240909/1725853152_66de6de0b5eae45fe7732.png!small)NoiseAttack 后门训练准备的中毒数据集概览

这种攻击为创建具有多个目标标签的后门提供了一种通用方法，从而为试图破坏机器学习模型的攻击者提供了一种强大的工具。

该框架能有效规避最先进的防御措施，并在各种数据集和模型中实现较高的攻击成功率。 通过在输入图像中引入白高斯噪声，该攻击可以成功地将图像错误分类为目标标签，而不会明显影响模型在干净数据上的性能。这种攻击对 GradCam、Neural Cleanse 和 STRIP 等防御机制的较强鲁棒性表明，它有可能对深度神经网络的安全性构成重大威胁。 此外，该攻击执行多目标攻击的能力也证明了它的多功能性和对不同场景的适应性。

参考来源

> [Noise Attack: A New Backdoor Exploiting Power Spectral Density for Evasion](https://cybersecuritynews.com/noiseattack-a-novel-backdoor-evasion/)

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)