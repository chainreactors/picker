---
title: Ubuntu系统软件中的5个漏洞潜藏了10年才被发现
url: https://www.freebuf.com/news/415786.html
source: FreeBuf网络安全行业门户
date: 2024-11-22
fetch_date: 2025-10-06T19:16:01.063192
---

# Ubuntu系统软件中的5个漏洞潜藏了10年才被发现

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

Ubuntu系统软件中的5个漏洞潜藏了10年才被发现

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Ubuntu系统软件中的5个漏洞潜藏了10年才被发现

2024-11-21 10:53:40

所属地 上海

Ubuntu系统中的实用程序 needrestart 近日被曝出存在5个本地权限提升 （LPE） 漏洞，这些漏洞不是最近才产生，而是已经潜藏了10年未被发现。

![](https://image.3001.net/images/20241121/1732158891_673ea5ab87bda371d8ee6.png!small)

这些漏洞由 Qualys 发现，并被跟踪为 CVE-2024-48990、CVE-2024-48991、CVE-2024-48992、CVE-2024-10224 和 CVE-2024-11003，由 2014 年 4 月发布的Needrestart  0.8 版本中引入，直到最近的11月19日才在3.8 版本中修复。

这5个漏洞允许攻击者在本地访问有漏洞的 Linux 系统，在没有用户交互的情况下将权限升级到 root：

* CVE-2024-48990： Needrestart 使用从运行进程中提取的 PYTHONPATH 环境变量执行 Python 解释器。 如果本地攻击者控制了这个变量，就可以通过植入恶意共享库，在 Python 初始化过程中以 root 身份执行任意代码。
* CVE-2024-48992：Needrestart 使用的 Ruby 解释器在处理攻击者控制的 RUBYLIB 环境变量时存在漏洞。 这允许本地攻击者通过向进程注入恶意库，以 root 身份执行任意 Ruby 代码。
* CVE -2024-48991： Needrestart 中的争用条件允许本地攻击者用恶意可执行文件替换正在验证的 Python 解释器二进制文件。 通过仔细把握替换时机，可以诱使 Needrestart 以 root 身份运行他们的代码。
* CVE-2024-10224：Needrestart 使用的 Perl ScanDeps 模块未正确处理攻击者提供的文件名。攻击者可以制作类似于 shell 命令的文件名（例如 command|），以便在打开文件时以 root 身份执行任意命令。
* CVE-2024-11003：Needrestart 对 Perl 的 ScanDeps 模块的依赖使其暴露于 ScanDeps 本身的漏洞中，其中不安全地使用 eval（） 函数会导致在处理攻击者控制的输入时执行任意代码。

值得注意的是，为了利用这些漏洞，攻击者必须通过恶意软件或被盗帐户对操作系统进行本地访问，这在一定程度上降低了风险。但攻击者过去也利用过类似的 Linux 权限提升漏洞来获得 root 权限，包括 Loony Tunables 和利用 nf\_tables 漏洞，因此不能因为这些漏洞需要本地访问权限就疏于修补。

除了升级到版本 3.8 或更高版本（包括所有已识别漏洞的补丁）之外，建议用户修改Needrestart.conf 文件以禁用解释器扫描功能，从而防止漏洞被利用。

**参考来源：**

> [Ubuntu Linux impacted by decade-old 'needrestart' flaw that gives root](https://www.bleepingcomputer.com/news/security/ubuntu-linux-impacted-by-decade-old-needrestart-flaw-that-gives-root/)

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