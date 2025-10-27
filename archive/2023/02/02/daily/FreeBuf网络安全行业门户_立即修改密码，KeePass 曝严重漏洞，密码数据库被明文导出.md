---
title: 立即修改密码，KeePass 曝严重漏洞，密码数据库被明文导出
url: https://www.freebuf.com/articles/356226.html
source: FreeBuf网络安全行业门户
date: 2023-02-02
fetch_date: 2025-10-04T05:29:21.245574
---

# 立即修改密码，KeePass 曝严重漏洞，密码数据库被明文导出

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

立即修改密码，KeePass 曝严重漏洞，密码数据库被明文导出

* ![]()
* 关注

立即修改密码，KeePass 曝严重漏洞，密码数据库被明文导出

2023-02-01 14:43:26

所属地 河南省

目前，鉴于各平台对密码的要求越来越复杂，越来越多用户使用密码管理软件统一存储密码，虽然此举可以很好帮助用户管理账户信息，但也意味着一旦此类软件存在漏洞，很容易导致机密数据泄露。

近日，Bleeping Computer 网站披露，开源密码管理软件 KeePass 被爆存在严重安全漏洞 CVE-2023-24055，网络攻击者能够利用漏洞在用户毫不知情的情况下，以纯文本形式导出用户的整个密码数据库。![1675235304_63da0fe82bac8e05be829.png!small?1675235305542](https://image.3001.net/images/20230201/1675235304_63da0fe82bac8e05be829.png!small?1675235305542)

不同于 LastPass 、BitwardenKeePass 等云托管的数据库，KeePass 允许用户使用本地存储的数据库来管理密码，并允许用户通过主密码加密数据库，以避免泄漏，这样恶意软件或威胁攻击者就很难访问数据库并自动窃取其中存储的密码。

但 CVE-2023-24055 允许获得目标系统写入权限的威胁攻击者更改 KeePass XML 配置文件并注入恶意触发器，从而将数据库中所有用户名和密码以明文方式导出。

据悉，当目标用户启动 KeePass 并输入主密码以解密数据库时，将触发导出规则，并将数据库内容保存到一个文件中，攻击者可以稍后将其导出到其控制的系统中。值得一提的是，整个数据库导出过程都在系统后台完成，不需要前期交互，不需要受害者输入密码，甚至不会通知受害者，悄悄导出所有数据库中存储的密码信息。

安全研究人员认为 CVE-2023-24055 漏洞爆出可能使威胁攻击者更容易在受损设备上转储和窃取 KeePass 数据库的内容。部分户要求 KeePass 开发团队在黑客“悄悄”导出数据库之前添加确认提示，或者提供一个没有导出功能的应用程序版本。

## ****KeePass**** ****官方表示暂无漏洞修补措施****

KeePass 官方声明表示，CVE-2023-24055 漏洞不应该归咎于 KeePass，并且这一漏洞不是其所能够解决的，有能力修改写入权限的网络攻击者完全可以进行更强大的网络攻击。

当用户常规安装 KeePass 时，一旦攻击者具有写入权限，就可以执行各种命令，开展攻击活动，就算用户运行可移植版，威胁攻击者也可以用恶意软件替换 KeePass 可执行文件。

上述两种情况表明，对 KeePass 配置文件进行写入意味着攻击者实际上可以执行比修改配置文件更强大的攻击（这些攻击最终也会影响 KeePass，而不受配置文件保护）。因此，KeePass 建议用户只有保持环境安全（使用防病毒软件、防火墙、不打开未知电子邮件附件等），才能防止此类攻击。![1675235313_63da0ff1d8c801e50c13e.png!small?1675235314146](https://image.3001.net/images/20230201/1675235313_63da0ff1d8c801e50c13e.png!small?1675235314146)

最后，KeePass 开发人员指出，即使用户无法获得更新版本，仍然能够通过系统管理员身份登录并创建强制配置文件来保护数据库。

**文章来源：**

> https://www.gamingdeputy.com/the-password-management-software-keepass-has-a-vicious-loopholethe-entire-database-can-be-exported-by-hackers-in-plain-text/
>
> https://www.bleepingcomputer.com/news/security/keepass-disputes-vulnerability-allowing-stealthy-password-theft/

# 漏洞利用

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

KeePass 官方表示暂无漏洞修补措施

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