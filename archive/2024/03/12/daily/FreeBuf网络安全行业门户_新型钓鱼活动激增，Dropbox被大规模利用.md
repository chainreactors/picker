---
title: 新型钓鱼活动激增，Dropbox被大规模利用
url: https://www.freebuf.com/news/393909.html
source: FreeBuf网络安全行业门户
date: 2024-03-12
fetch_date: 2025-10-04T12:12:32.628810
---

# 新型钓鱼活动激增，Dropbox被大规模利用

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

新型钓鱼活动激增，Dropbox被大规模利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型钓鱼活动激增，Dropbox被大规模利用

2024-03-11 11:16:44

所属地 上海

Darktrace的最新研究表明，威胁行为者利用Dropbox的合法基础设施发起了一场新型的钓鱼活动，并成功绕过了多因素认证（MFA）。

这意味着利用合法的流行服务进行攻击的情况日益增多，以此诱使目标下载恶意软件，导致登录凭证泄露。

Darktrace威胁研究负责人汉娜·达利强调，威胁行为者利用用户对特定服务的信任，通过模仿用户收到的正常电子邮件发起攻击的做法比较常见。但在新型钓鱼活动中，威胁行为者进一步利用合法的 Dropbox 云存储平台进行网络钓鱼攻击，这种做法相对新颖。

![](https://image.3001.net/images/20240311/1710136968_65ee9e8885c099a3dfd6c.jpg!small)

## **威胁行为者利用Dropbox基础设施进行攻击**

2024年1月25日，威胁行为者对Darktrace的一位客户发起了针对性攻击，该组织的软件即服务(SaaS)环境中的16名用户收到了一封来自“no-reply@dropbox[.]com”的邮件，这是Dropbox文件存储服务所使用的官方合法电子邮件地址。

电子邮件中包含了一个链接，此链接会引导用户前往一个存放在Dropbox上的PDF文件，而这个PDF文件的名称似乎是以该组织的一个合作伙伴来命名的。

PDF文件又包含一个指向新域名‘mmv-security[.]top’的可疑链接，此前，这个域名在客户的系统环境中从未出现过。

虽然这封电子邮件被Darktrace的电子邮件安全工具识别并拦截，但是，在1月29日，一位用户收到了另一封来自官方的no-reply@dropbox[.]com邮箱地址的邮件，提醒他们打开之前共享的PDF文件。

尽管这条信息被自动归类到了用户的垃圾邮件文件夹，但该员工还是打开了这封令人怀疑的邮件，并且跟随链接查看了PDF文件。几天后，他们的内部设备连接到了恶意链接mmv-security[.]top。

这个链接引导至一个伪造的Microsoft 365登录页面，其目的是为了获取合法的SaaS账户持有者的登录凭证。

![](https://image.3001.net/images/20240311/1710136990_65ee9e9e38adaf0cde9b2.png!small)

用户点击PDF文件中的链接后被引导至伪造的微软登录页面 来源：Darktrace

## **威胁行为者成功绕过多因素认证（MFA）**

1月31日，Darktrace观察到多个异常地点出现了几次可疑的SaaS登录行为，这些地点以前从未访问过该账户。紧接着在2月1日，又发现了与ExpressVPN相关的异常登录活动，这表明威胁行为者可能利用虚拟私人网络（VPN）来遮掩他们的真实位置。

研究人员指出，通过使用有效的令牌并满足必要的多因素认证（MFA）条件，威胁行为者往往能够避开

传统安全工具的侦测，因为这些工具将MFA视为万能的解决方案。

尽管威胁行为者使用合法凭据绕过了MFA，但在识别到SaaS账户上的异常活动后，该组织的安全团队也会提高警惕。

Darley在接受Infosecurity采访时表示，**这一事件表明，组织不能再把MFA作为防御网络攻击的最后一道防线。**因为MFA绕过作为威胁行为者常用的策略之一，在获取像SharePoint文件这类可被滥用的共享资源的访问权限方面已经取得了成功。

## **威胁行为者表现出持久性**

在绕过多因素认证（MFA）后不久，Darktrace监测到另一起异常登录事件，威胁行为者使用HideMyAss VPN服务进入了SaaS账户。

这次，威胁行为者者在受损的Outlook账户中设立了一个新的邮件规则，该规则会自动将财务团队发送的邮件直接转移到“会话历史”文件夹。

研究人员表示，威胁行为者通过把他们的恶意邮件及其回复转移到不常查看的邮箱文件夹中，以此绕过侦测。

此外，威胁行为者还发送了标题为“合同错误”和“需要紧急审核”的跟进邮件。这表明威胁行为者正在使用被入侵的账户向财务团队发送更多恶意邮件，目的是在客户的SaaS环境中感染更多账户。

## **网络钓鱼攻击既有针对性又复杂**

研究人员指出，与依赖基础设施相比，威胁行为者利用像Dropbox这样的合法第三方解决方案进行钓鱼攻击“相对简单”。

Darley评论道，这个研究案例凸显了威胁行为者在多层次的攻击方面变得越来越高明，他们通过Dropbox的一个官方‘不接受回复’地址（这类地址通常用于向客户发送通知或链接）发出这些电子邮件。而电子邮件中的链接表面上指向一个合法的Dropbox存储点，实际上存放的却是一个恶意文件。该文件被伪装成合作伙伴文档，使电子邮件看上去似乎是合法的。

## **生成式AI助攻黑客**

Darley强调，生成式人工智能技术在帮助威胁行为者编写更精密的钓鱼邮件方面产生了巨大影响。

根据Darktrace在2023年发布的年终威胁报告，在2023年下半年观测到的钓鱼案例中，超过25%的邮件包含了1000个以上的字符，这在很大程度上归功于生成式AI的能力。

“这些邮件不再是仅含简短文本和可疑链接的‘单一载荷’邮件，而是经过精心编写、内容丰富的邮件。还有威胁行为者利用高级社交工程技术，潜入正在进行的对话中，冒充同事或熟人，尝试模仿通信的语调。”Darley解释到，“这些高度复杂的实例正是由生成式AI所赋能，它让威胁行为者有更多时间去策划大规模的攻击。”

> 参考来源：[Dropbox Used to Steal Credentials and Bypass MFA in Phishing Campaign - Infosecurity Magazine (infosecurity-magazine.com)](https://www.infosecurity-magazine.com/news/dropbox-credentials-bypass-mfa/)

# 网络攻击 # DROPBOX # 新型钓鱼邮件

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

威胁行为者利用Dropbox基础设施进行攻击

威胁行为者成功绕过多因素认证（MFA）

威胁行为者表现出持久性

网络钓鱼攻击既有针对性又复杂

生成式AI助攻黑客

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