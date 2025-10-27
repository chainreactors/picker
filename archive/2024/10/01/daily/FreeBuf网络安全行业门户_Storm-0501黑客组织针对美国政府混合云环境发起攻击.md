---
title: Storm-0501黑客组织针对美国政府混合云环境发起攻击
url: https://www.freebuf.com/news/412078.html
source: FreeBuf网络安全行业门户
date: 2024-10-01
fetch_date: 2025-10-06T18:51:58.106282
---

# Storm-0501黑客组织针对美国政府混合云环境发起攻击

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

Storm-0501黑客组织针对美国政府混合云环境发起攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Storm-0501黑客组织针对美国政府混合云环境发起攻击

2024-09-30 09:34:47

所属地 上海

![](https://image.3001.net/images/20240930/1727660208_66fa00b00e434d2e23681.png!small)

近日，有一名为 Storm-0501 的威胁行为者以美国的政府、制造、运输和执法部门为目标，发动勒索软件攻击。
微软表示，这种多阶段攻击活动旨在破坏混合云环境，并从内部部署横向移动到云环境，最终导致数据外渗、凭证盗窃、篡改、持续后门访问和勒索软件部署。
微软威胁情报团队人员称，Storm-0501 是一个有经济动机的网络犯罪团伙，其主要使用商品和开源工具进行勒索软件操作。
该威胁行为体自2021年开始活跃，曾利用Sabbath (54bb47h)勒索软件以教育实体为目标，后来发展成为勒索软件即服务（RaaS）联盟，多年来提供各种勒索软件有效载荷，包括Hive、BlackCat (ALPHV)、Hunters International、LockBit和Embargo勒索软件。

Storm-0501 攻击的一个显著特点是利用弱凭据和过度授权账户从企业内部转移到云基础设施。

其他初始访问方法包括使用 Storm-0249 和 Storm-0900 等访问代理已经建立的立足点，或利用 Zoho ManageEngine、Citrix NetScaler 和 Adobe ColdFusion 2016 等面向互联网的服务器中未打补丁的各种已知远程代码执行漏洞。

上述任何一种方法所提供的访问权限都可为广泛的发现操作铺平道路，以确定高价值资产、收集域信息并执行活动目录侦察。随后部署 AnyDesk 等远程监控和管理工具 (RMM)，以保持持久性。

微软表示：威胁者在初始访问时利用了其入侵的本地设备上的管理员权限，并试图通过多种方法访问网络中的更多账户。

威胁者主要利用 Impacket 的 SecretsDump 模块（通过网络提取凭证），并在大量设备上利用该模块获取凭证。

被攻破的凭据随后被用于访问更多设备并提取更多凭据，威胁者同时访问敏感文件以提取 KeePass 秘密，并进行暴力攻击以获取特定账户的凭据。

微软表示，它检测到 Storm-0501 使用 Cobalt Strike 在网络中横向移动被入侵的凭据并发送后续命令。通过使用 Rclone 将数据传输到 MegaSync 公共云存储服务，实现了内部环境的数据外渗。

据观察，该威胁行为者还创建了对云环境的持续后门访问，并将勒索软件部署到内部部署环境中，这是继 Octo Tempest 和 Manatee Tempest 之后，最新针对混合云设置的威胁行为者。

Redmond说：威胁者使用了从早先攻击中窃取的凭证，特别是微软Entra ID（前身为Azure AD），从内部部署横向移动到云环境，并通过后门建立了对目标网络的持久访问。

向云的转移是通过一个被攻破的微软 Entra Connect Sync 用户账户或通过劫持一个内部部署用户账户的云会话来实现的，而这个内部部署用户账户在云中有一个各自的管理员账户，并禁用了多因素身份验证（MFA）。

在获得足够的网络控制权、渗出相关文件并横向移动到云端后，Embargo 勒索软件就会在整个受害组织内部署，从而将攻击推向高潮。Embargo 是一种基于 Rust 的勒索软件，于 2024 年 5 月首次被发现。

微软表示：Embargo背后的勒索软件集团以RaaS模式运作，允许Storm-0501等附属机构使用其平台发动攻击，以换取赎金分成。

Embargo的附属组织采用双重勒索策略，他们首先加密受害者的文件，并威胁说除非支付赎金，否则就会泄露窃取的敏感数据。

尽管如此，根据Windows 制造商收集到的证据显示，该威胁行为者并不总是采用发布勒索软件的方式，而是在某些情况下选择只保留网络后门访问权限。

在披露这一消息的同时，DragonForce 勒索软件组织一直在利用泄露的 LockBit3.0 生成器变种和修改版 Conti 针对制造业、房地产和运输业的公司进行攻击。

这些攻击的特点是使用 SystemBC 后门进行持久性攻击，使用 Mimikatz 和 Cobalt Strike 进行凭证收集，以及使用 Cobalt Strike 进行横向移动。美国的受害者占受害者总数的 50%以上，其次是英国和澳大利亚。

总部位于新加坡的 Group-IB 公司表示：该组织采用双重勒索策略，对数据进行加密，并威胁说除非支付赎金，否则就会泄露数据。2024年6月26日启动的联盟计划向联盟成员提供80%的赎金，以及用于攻击管理和自动化的工具。

> 参考来源：[Microsoft Identifies Storm-0501 as Major Threat in Hybrid Cloud Ransomware Attacks](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html)

# 网络攻击 # 混合云

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