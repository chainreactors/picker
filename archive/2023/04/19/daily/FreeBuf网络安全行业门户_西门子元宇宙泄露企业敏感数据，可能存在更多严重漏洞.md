---
title: 西门子元宇宙泄露企业敏感数据，可能存在更多严重漏洞
url: https://www.freebuf.com/news/363957.html
source: FreeBuf网络安全行业门户
date: 2023-04-19
fetch_date: 2025-10-04T11:35:27.739171
---

# 西门子元宇宙泄露企业敏感数据，可能存在更多严重漏洞

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

西门子元宇宙泄露企业敏感数据，可能存在更多严重漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

西门子元宇宙泄露企业敏感数据，可能存在更多严重漏洞

2023-04-18 17:09:13

所属地 上海

如今，元宇宙已经不再是一个流行词，但随着近期ChatGPT和其他类似的人工智能工具又开始流行起来，虚拟世界的概念重新进入人们的视线内。同时也引起了一些威胁行为者的注意。

西门子，作为一家收入超过71万亿美元、在全球拥有30万名员工的德国跨国公司，也赶上了元宇宙的红潮。2022年，它与美国跨国技术公司NVidia合作建立了工业元宇宙。

最近，Cybernews研究团队发现，一个由西门子工厂和办公室创建的数字平台泄露了一些敏感信息。这些信息一旦被那些攻击者拿到，很可能会对该公司和其他使用其服务的大公司产生毁灭性的后果，包括勒索软件攻击。

不过西门子表示，这个问题目前已经得到解决。

## **研究人员怀疑该网站或存在其他更严重的漏洞**

3月1日，Cybernews研究团队发现一个托管在metaverse.siemens.com域名上的环境文件，里面包含了ComfyApp的凭证和端点。另外，研究团队还发现西门子泄露了WordPress里的四组用户信息，以及系统中的三套后台和身份验证端点URL。

WordPress虽然只暴露了用户名和头像图片信息，但四个基于西门子WordPress的子域都有漏洞。早在2017年，WordPress就曾修复过一个漏洞，因此研究人员怀疑这个网站可能还存在其他更严重的漏洞。

一般来说，用户访问网站前，需要通过后台和认证端点URL验证，所以攻击者极有可能通过漏洞窃取信息并加以利用。

此外，研究人员发现西门子办公管理平台ComfyApp的用户凭证也被曝光，这十分令人担忧。因为西门子公司的应用程序是专门用于工作空间管理的，所以这意味着该应用程序会获取一些敏感数据，包括平面图、物联网（IoT）设备的信息、员工日历和内部图片等。不过目前还不能确定如果仅使用ComfyApp凭证能获取到多少上述的数据信息。

网络新闻研究人员希望西门子能在那些威胁者发现前修复这个漏洞，因为西门子的信息中涉及到很多关键基础设施使用的技术和机器，因此一旦信息被入侵，极可能造成大量敏感数据泄露。

Cybernews团队还表示：西门子的客户中包括一些资产数十亿（美元）的公司，有时会协助这些客户处理一些极其敏感的数据，这对于那些攻击者来说是非常有价值的。

## **目前尚无法判断攻击者入侵元宇宙数据的获益方式**

如果有人走进你的办公室，偷看你放在桌子上的工作计划和照片，甚至是你的日历，你会怎么做？员工应该都知道问题的答案，那就是直接不让陌生人进入他们的办公室。但如果是在虚拟的数字办公室呢，规则会有什么不同?

Cybernews研究人员表示，一旦攻击者窥探过数字办公室后，他就可以知道办公室内所有的空间布局，甚至可以熟练操作任何办公设备、比如智能空调，熟练程度堪比在那工作了好多年的老员工一样。他们可能会直接在办公室电脑里插入一个感染病毒的USB驱动器，然后通过勒索软件实施勒索企业的目的。

由于元宇宙的构建方式要求其必须包含最新的工厂数据，所以攻击者一旦攻入，就能直接提取到一些商业机密，如制造技术。这里有很多威胁行为者的机会。研究小组还表示，由于这是首批通过元宇宙泄露现实敏感数据的案例，还没有什么过往经验，所以到底这些威胁者会用什么方法获益，目前还尚不清楚。

## **预计到2026年，元宇宙的市场规模将达到7600亿美元**

在之前元宇宙炒作的巅峰时期，扎克伯格甚至将其 Facebook更名为Meta，成为一家“元宇宙优先，而非 Facebook 优先”的公司。但毫无疑问，很多火爆营销的元宇宙项目都在亏损。这似乎在告诉大家，围绕元宇宙这个概念的炒作期似乎已经告一段落了。

所以专家担心的到底是什么?首先，这涉及到了隐私问题和犯罪问题，因为它确实代表了一个前所未有的攻击面。

元宇宙的早期用户此前就曾报告过与骚扰、欺凌、仇恨言论等恶劣行为相关的问题。而且像钓鱼网络这样的攻击方式在日常中可能更难预防，因为在元宇宙中，攻击的载体可能会扩展到你的大脑。

趋势科技的研究人员曾预测过“黑暗宇宙”的兴起，这里指的就是元宇宙中的暗网，这些威胁者正在执法部门无法触及的地方暗自生长。

相比最近爆火的ChatGPT和它的竞争对手，元宇宙的话题可能已经有点黯然失色，但这个概念并没有消亡。比如：

韩国首尔最近推出了全球首个元宇宙官方商务、娱乐平台。去年，迪拜也曾推出了一项雄心勃勃的元宇宙发展战略，称2030年将在元宇宙创造4万余个虚拟工作岗位。此前欧盟也曾花费40万美元创建了一个专门面向青年的元诗式数字会场，以通过这种方式让年轻人更加了解欧盟在世界舞台上的一些辉煌事迹。

以上列举的是最近几个与元宇宙发展关系紧密的案例，这个进展速度可能比人们比预期慢了不少。但这对于企业来说，是以元空间为重点的网络安全的重要一环。

预计到2026年，元宇宙的市场规模将达到7600亿美元。

参考链接：[Siemens Metaverse exposes sensitive corporate data | Cybernews](https://cybernews.com/security/siemens-metaverse-data-leak/)

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

研究人员怀疑该网站或存在其他更严重的漏洞

目前尚无法判断攻击者入侵元宇宙数据的获益方式

预计到2026年，元宇宙的市场规模将达到7600亿美元

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