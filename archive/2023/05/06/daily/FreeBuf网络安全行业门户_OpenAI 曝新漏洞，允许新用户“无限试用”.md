---
title: OpenAI 曝新漏洞，允许新用户“无限试用”
url: https://www.freebuf.com/news/365537.html
source: FreeBuf网络安全行业门户
date: 2023-05-06
fetch_date: 2025-10-04T11:40:42.252735
---

# OpenAI 曝新漏洞，允许新用户“无限试用”

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

OpenAI 曝新漏洞，允许新用户“无限试用”

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

OpenAI 曝新漏洞，允许新用户“无限试用”

2023-05-05 11:22:13

所属地 上海

![](https://image.3001.net/images/20230505/1683254225_64546bd144e507d57c6e2.png!small)

通过该漏洞，用户可以免费获得无限的信用额度来测试不同的OpenAI项目，包括ChatGPT。

不久前，OpenAI 为了让用户尝试其他开放的人工智能项目，特意为新用户提供了免费的信用积分额度（约7美元）。随后网络安全公司Checkmarx表示，目前发现了一个漏洞，允许用户滥用试用，并在新账户上获得无限的信用积分额度。

研究人员表示：通过拦截和修改OpenAI的API请求，我们发现了这一漏洞。该漏洞能够使用同一个电话号码注册任意数量的账户，获得无限的免费积分额度。

为了注册试用，用户必须输入他们的电子邮件地址，点击发送到收件箱的激活链接，输入一个电话号码，然后输入短信验证码。电子邮件和电话号码都必须是唯一的，用户才能获得免费的积分额度。

然而，不法分子为了让同一账户获得更多的信用积分额度。他们对电话号码进行细微的改动，例如在国家/地区代码前面添加前缀。最终，他们通过使用同一电话号码的不同前缀的变化绕过了要求。

研究人员解释说：这一漏洞允许一个恶意的用户拥有多个账户，并获得更多的信用积分额度，而且用的是同一个电话号码。

但这对他们来说似乎还不够，因为他们想将信用积分值提高到一个更恐怖的数额。

然后，研究人员将开源工具REcollapse投入使用。这允许用户模糊输入和绕过验证等。

经过一些初步测试，观察到OpenAI API对一些模式进行了清理。在某些非ASCII（美国信息交换标准代码）字节上使用Unicode编码使我们能够绕过它并注册更多帐户。

目前该公司在收到通知后修复了该漏洞。

> 参考链接：https://cybernews.com/news/openai-flaw-unlimited-credit/

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