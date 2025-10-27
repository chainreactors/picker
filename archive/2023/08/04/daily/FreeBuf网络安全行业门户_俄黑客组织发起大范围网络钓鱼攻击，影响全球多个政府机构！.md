---
title: 俄黑客组织发起大范围网络钓鱼攻击，影响全球多个政府机构！
url: https://www.freebuf.com/news/373728.html
source: FreeBuf网络安全行业门户
date: 2023-08-04
fetch_date: 2025-10-04T12:03:14.174075
---

# 俄黑客组织发起大范围网络钓鱼攻击，影响全球多个政府机构！

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

俄黑客组织发起大范围网络钓鱼攻击，影响全球多个政府机构！

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

俄黑客组织发起大范围网络钓鱼攻击，影响全球多个政府机构！

2023-08-03 10:52:14

所属地 上海

![1691030649_64cb14791e00b03fe2d8b.png!small](https://image.3001.net/images/20230803/1691030649_64cb14791e00b03fe2d8b.png!small)

近日，微软称有一个与俄罗斯对外情报局有关的名为APT29的黑客组织，针对全球数十个组织包括政府机构等进行了网络钓鱼攻击。

微软方面透露，根据目前调查显示，此次攻击活动影响了全球约40个组织。并且此次攻击活动表明该黑客组织将政府、非政府组织(ngo)、IT服务、技术、离散制造业和媒体部门等设置成了特定间谍目标。

黑客利用被入侵的 Microsoft 365 租户创建了新的技术支持主题域并发送技术支持诱饵，试图利用社交工程策略欺骗目标组织的用户。

他们的目的是操纵用户批准多因素身份验证（MFA）提示，最终窃取他们的凭证。

攻击者利用被入侵的 Microsoft 365 租户创建了以技术支持为主题的新域。这些新域是 "onmicrosoft.com "域的一部分，而 "onmicrosoft.com "域是一个合法的微软域，在没有创建自定义域的情况下，Microsoft 365 会自动将其用作备用域。

然后，他们利用这些域发送技术支持诱饵，欺骗目标组织的用户批准多因素身份验证 (MFA) 提示。

![1691031082_64cb162a121a8514fc6bc.png!small](https://image.3001.net/images/20230803/1691031082_64cb162a121a8514fc6bc.png!small)

APT29团队网络钓鱼消息，图源：微软

由于这些信息均来自合法的 onmicrosoft.com 域名，这使得这些假冒的微软支持信息看起来很值得信赖。

根据雷德蒙德的公告，威胁行为者的最终目的是窃取目标用户的凭证。

微软方面补充称：在某些情况下，行为者试图通过微软 Entra ID（前身为 Azure Active Directory）将设备添加到组织中作为受管设备，这很可能是为了规避为限制受管设备访问特定资源而配置的条件访问策略。

该公司报告称，已成功阻止俄罗斯威胁组织在其他攻击中使用这些域，目前正在积极应对并降低该活动的影响。

## Jumpsec安全研究人员上个月发现一个安全问题

上个月，Jumpsec安全研究人员发现Microsoft Teams中存在一个安全问题，该问题可让任何人使用由美国海军红队成员 Alex Reid 开发的名为 TeamsPhisher 的 Python 工具绕过对来自外部租户的传入文件的限制，但微软拒绝解决此问题。

JumpSec 在 6 月份报告该漏洞时，微软表示该漏洞 "不符合立即提供服务的标准"。

BleepingComputer 也联系了微软，询问是否有计划修复这个问题，并被告知客户应该注意可疑信息。

但微软发言人告诉 BleepingComputer：他们已经注意到这个报告，并确定它是依靠社会工程学而成功的。一直以来微软都鼓励客户养成良好的上网计算习惯，包括在点击网页链接、打开未知文件或接受文件传输时保持谨慎。

不幸的是，APT29的社会工程攻击也影响了政府机构，这凸显了这种攻击可能产生的巨大影响，即使是对保护良好的实体。

## 黑客组织APT29已成功隐蔽多年

APT29 是俄罗斯对外情报局 (SVR) 的黑客部门，三年前曾策划过 SolarWinds 供应链攻击事件，导致多个美国联邦机构遭到入侵。

自那次事件后，这个黑客组织还利用隐蔽的恶意软件（包括 TrailBlazer 和 GoldMax Linux 后门变种）渗透到其他组织的网络中，成功隐蔽了多年一直未被发现。

最近，微软披露，该黑客组织正在使用新的恶意软件，夺取活动目录联盟服务（ADFS）的控制权，以 Windows 系统中任何用户的身份登录。

他们瞄准了北约国家实体的 Microsoft 365 账户，试图获取与外交政策相关的信息。同时，他们还发起了一系列网络钓鱼活动，明确针对欧洲各国政府、大使馆和高级官员。

> 参考来源：[Russian hackers target govt orgs in Microsoft Teams phishing attacks](https://www.bleepingcomputer.com/news/security/russian-hackers-target-govt-orgs-in-microsoft-teams-phishing-attacks/)

# 钓鱼攻击 # 黑客组织 # 俄罗斯黑客

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

Jumpsec安全研究人员上个月发现一个安全问题

黑客组织APT29已成功隐蔽多年

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