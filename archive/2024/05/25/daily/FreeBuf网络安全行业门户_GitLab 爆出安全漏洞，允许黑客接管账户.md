---
title: GitLab 爆出安全漏洞，允许黑客接管账户
url: https://www.freebuf.com/news/401772.html
source: FreeBuf网络安全行业门户
date: 2024-05-25
fetch_date: 2025-10-06T17:17:47.540719
---

# GitLab 爆出安全漏洞，允许黑客接管账户

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

GitLab 爆出安全漏洞，允许黑客接管账户

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

GitLab 爆出安全漏洞，允许黑客接管账户

2024-05-24 11:21:48

所属地 上海

近日，GitLab 又爆出一个安全漏洞（被追踪为 CVE-2024-4835），未经认证的威胁攻击者能够利用该漏洞在跨站脚本 (XSS) 攻击中，轻松接管受害者账户。![1716520969_665008093ade99e2b267d.png!small](https://image.3001.net/images/20240524/1716520969_665008093ade99e2b267d.png!small)

> GitLab ：一个基于网络的 Git 存储库，主要面向需要远程管理代码的开发团队，目前共拥有约 3000 万注册用户和 100 万付费客户。

收到 CVE-2024-4835 安全漏洞通知后，GitLab 方面表示，在近期发布的 GitLab 社区版（CE）和企业版（EE）的17.0.1、16.11.3 和 16.10.6 版本中都修复了安全漏洞问题，强烈建议所有 GitLab 用户立即升级到其中一个版本。

> CVE-2024-4835 安全漏洞是 VS 代码编辑器（Web IDE）中的一个 XSS 缺陷，允许威胁攻击者利用恶意制作的页面窃取部分信息。值得一提的是，虽然威胁攻击者可在未经身份验证的攻击中利用该漏洞，但仍需要与用户交互，这就增加攻击的复杂性。

GitLab 公司还修复了其他六个中等严重程度的安全漏洞。其中，主要包括通过 Kubernetes 代理服务器的跨站请求伪造（CSRF）漏洞 CVE-2023-7045 和一个可让威胁攻击者破坏 GitLab 网络资源加载的拒绝服务漏洞 CVE-2024-2874。![1716521014_66500836a2b2f1603fb93.png!small?1716521014821](https://image.3001.net/images/20240524/1716521014_66500836a2b2f1603fb93.png!small?1716521014821)

## GitLab 安全漏洞频出

众所周知，GitLab 存放着包括 API 密钥、专有代码等各种类型的敏感数据，因此早就成为了很多威胁攻击组织眼中的”香饽饽“。一旦有威胁攻击者成功在 CI/CD（持续集成/持续部署）环境中插入恶意代码，破坏组织的资源库，那么被劫持的 GitLab 账户就会面临着重大的网络安全风险，甚至引发严重供应链攻击。

早些时候，CISA 曾经发出警告，威胁攻击者目前正积极利用 GitLab 在 1 月份修补零点击账户劫持漏洞 CVE-2023-7028，漏洞允许未经认证的威胁攻击者通过密码重置接管 GitLab 账户。当时，Shadowserver 发现超过 5300 个在线暴露的 GitLab 漏洞实例（截止到目前仍旧有 2084  个的实例可以访问）。![](https://image.3001.net/images/20240524/1716530637_66502dcd6e8d7e78797a6.jpg!small)2023 年 5月，GitLab 突然发布了 16.0.1 版紧急安全更新，解决了一个被追踪为 CVE-2023-2825 的严重性路径遍历漏洞，该漏洞 CVSS 评分10.0。

据悉，CVE-2023-2825 漏洞源于路径遍历问题，当一个附件存在于至少五个组内嵌套的公共项目中时，未经认证的威胁攻击者便可以在服务器上读取任意文件。不仅如此，一旦成功利用 CVE-2023-2825 漏洞，还可能会非法访问包括专有软件代码、用户凭证、令牌、文件和其他私人信息在内的敏感数据。

好消息是，CVE-2023-2825 漏洞问题与 GitLab 如何管理或解决嵌套在几级组层次结构中的附件文件的路径有关，因此安全漏洞只能在特定条件下才会触发，即当公共项目中有一个附件嵌套在至少五个组中时，好在这并不是所有 GitHub 项目遵循的结构。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/high-severity-gitlab-flaw-lets-attackers-take-over-accounts/

# 漏洞

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

GitLab 安全漏洞频出

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