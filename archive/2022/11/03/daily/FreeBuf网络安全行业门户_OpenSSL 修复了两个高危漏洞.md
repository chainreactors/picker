---
title: OpenSSL 修复了两个高危漏洞
url: https://www.freebuf.com/news/348558.html
source: FreeBuf网络安全行业门户
date: 2022-11-03
fetch_date: 2025-10-03T21:39:55.811355
---

# OpenSSL 修复了两个高危漏洞

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

OpenSSL 修复了两个高危漏洞

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

OpenSSL 修复了两个高危漏洞

2022-11-02 11:48:12

所属地 上海

Bleeping Computer 网站披露，OpenSSL 修补了其用于加密通信通道和 HTTPS 连接的开源密码库中两个高危漏洞。漏洞分别追踪为 CVE-2022-3602 和 CVE-2022-3786，主要影响 OpenSSL 3.0.0 及更高版本，现已在 OpenSSL 3.0.7 中得到解决。![1667360930_6361e8a2bf52a126f5bf2.jpg!small?1667360930776](https://image.3001.net/images/20221102/1667360930_6361e8a2bf52a126f5bf2.jpg!small?1667360930776)

据悉，CVE-2022-3602 是一个任意 4 字节堆栈缓冲区溢出漏洞，可能导致拒绝服务或远程代码执行。CVE-2022-3786 可以被攻击者通过恶意电子邮件地址利用，通过缓冲区溢出触发拒绝服务状态。

OpenSSL 团队表示，虽然目前没有证据表明这两个漏洞已经被利用，但鉴于其具有很高的危险性，希望受影响用户尽快安装更新升级补丁，以免遭受网络威胁。此外，OpenSSL 还提供了一些其它缓解措施，例如直到应用新补丁前，要求操作 TLS 服务器的管理员禁用 TLS 客户端认证。

## ****CVE-2022-3602**** ****漏洞危险指数下降****

值得一提的是，OpenSSL 最初发布的漏洞警告促使了管理员立即采取行动缓解漏洞，但之后鉴于 CVE-2022-3602 已被降级为高度严重，况且它只影响 OpenSSL 3.0 及更高版本，另外与 OpenSSL 密码库早期版本相比，最近发布的版本也尚未大量部署到生产中使用的软件上，因此造成的实际影响可能很有限，

尽管一些安全专家和供应商将此漏洞的危险性等同于 Apache Log4J 日志库中的 Log4Shell 漏洞，但在Censys 在线发现的 1793000 多个主机中，只有大约 7000个暴露在互联网上的系统正在运行易受攻击的OpenSSL 版本，Shodan 也列出了大约 16000 个可公开访问的 OpenSSL 实例。

此外，云安全公司 Wiz.io 也表示，在分析了主要云环境（AWS、GCP、Azure、OCI和阿里巴巴云）中的部署后，发现只有 1.5% 的 OpenSSL 实例受到这一安全漏洞的影响。![1667360939_6361e8ab3c400f8fa4c3e.jpg!small?1667360939154](https://image.3001.net/images/20221102/1667360939_6361e8ab3c400f8fa4c3e.jpg!small?1667360939154)

流行 CSP 中存在漏洞的 OpenSSL 实例

最新的 OpenSSL 版本包含在多个流行的 Linux 发行版中，其中 Redhat Enterprise Linux 9、Ubuntu 22.04+、CentOS Stream9、Kali 2022.3、Debian 12 和 Fedora 36 被网络安全公司 Akamai标记为有漏洞，荷兰国家网络安全中心目前也正在确认一份受 CVE-2022-3602 漏洞影响的软件产品清单。

**参考文章：**

> https://www.bleepingcomputer.com/news/security/openssl-fixes-two-high-severity-vulnerabilities-what-you-need-to-know/

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

CVE-2022-3602 漏洞危险指数下降

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