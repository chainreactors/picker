---
title: 针对程序猿的新型骗局，黑客借招聘Python传播恶意软件
url: https://www.freebuf.com/news/410804.html
source: FreeBuf网络安全行业门户
date: 2024-09-13
fetch_date: 2025-10-06T18:27:48.052796
---

# 针对程序猿的新型骗局，黑客借招聘Python传播恶意软件

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

针对程序猿的新型骗局，黑客借招聘Python传播恶意软件

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

针对程序猿的新型骗局，黑客借招聘Python传播恶意软件

2024-09-12 09:44:47

所属地 上海

![](https://image.3001.net/images/20240912/1726112342_66e262568bf65bf76104c.png!small)

近期，有攻击者利用虚假的求职面试和编码测试诱骗开发人员下载运行恶意软件。该活动被称为 VMConnect， 疑似与朝鲜 Lazarus 集团有关 。

## 针对 Python 开发人员的虚假编码测试

恶意行为者会伪装成知名金融服务公司（包括 Capital One 等美国大公司）的招聘人员，试图诱导开发人员下载恶意软件。

然后利用虚假的求职面试和编码测试诱骗受害者执行恶意软件，恶意软件通常隐藏在编译好的 Python 文件中或嵌入在压缩文件中。恶意软件随后从缓存的编译文件中执行，因此很难被发现。

![1726105508_66e247a4085cf1bba6aac.png!small](https://image.3001.net/images/20240912/1726105508_66e247a4085cf1bba6aac.png!small)

来源：reversinglabs

ReversingLabs 的研究人员发现，攻击者会使用 GitHub 存储库和开源容器来托管其恶意代码。这些代码通常会伪装成编码技能测试或密码管理器应用程序，代码附带的 README 文件包含诱骗受害者执行恶意软件的说明。这些文件往往使用 “Python\_Skill\_Assessment.zip ”或 “Python\_Skill\_Test.zip ”等名称。

他们发现，恶意软件包含在经过修改的 pyperclip 和 pyrebase 模块文件中，这些文件也经过 Base64 编码，以隐藏下载程序代码。这些代码与 VMConnect 活动早期迭代中观察到的代码相同，后者向 C2 服务器发出 HTTP POST 请求以执行 Python 命令。

在一次事件中，研究人员成功识别出一名受到攻击者欺骗的开发人员。攻击者伪装成Capital One的招聘人员，然后通过LinkedIn个人资料和开发人员取得联系，并向他提供了一个GitHub的链接作为一项题目。当被要求推送更改时，假冒的招聘人员指示他分享截图，以证明任务已经完成。

安全研究人员随后访问的 .git 文件夹中的日志目录中包含一个 HEAD 文件，该文件显示了克隆该仓库并实施所需功能的开发人员的全名和电子邮件地址。

研究人员立即与该开发人员取得了联系，并确认他于今年 1 月感染了恶意软件，而该开发人员并不知道自己在此过程中执行了恶意代码。

![1726105521_66e247b18e7b6f5871817.png!small](https://image.3001.net/images/20240912/1726105521_66e247b18e7b6f5871817.png!small)

来源：reversinglabs

虽然此事件已经追溯到了几个月前，但研究人员认为，目前有足够的证据和活动线索表明该活动仍在继续。7 月 13 日，他们又发现了一个新发布的 GitHub 存储库，与之前事件中使用的存储库相吻合，但使用的是不同的账户名。

通过进一步调查，研究人员发现这个“尘封”的GitHub 账户在他们与受害者建立联系的同一天又活跃了起来，并认为威胁行为者可能仍保留着对受感染开发人员通信的访问权限。研究人员还认为，被联系的开发人员可能与恶意活动有关联。

> 参考来源：[Threat Actors Target Python Developers With Fake Coding Tests (thecyberexpress.com)](https://thecyberexpress.com/malicious-recruiters-lure-python-developers/)

# python # 恶意代码 # 恶意软件 # 开发

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

文章目录

针对 Python 开发人员的虚假编码测试

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