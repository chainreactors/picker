---
title: 尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本
url: https://www.freebuf.com/news/410154.html
source: FreeBuf网络安全行业门户
date: 2024-09-05
fetch_date: 2025-10-06T18:26:53.314512
---

# 尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本

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

尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

尽快更新！Zyxel 路由器曝出 OS 命令注入漏洞，影响多个版本

2024-09-04 09:23:15

所属地 上海

![zyxel-router.jpg](https://image.3001.net/images/20240904/1725418156_66d7caac4f09ac5cd1d19.jpg!small)

近日，Zyxel 发布安全更新，以解决影响其多款商用路由器的关键漏洞，该漏洞可能允许未经认证的攻击者执行操作系统命令注入。

该漏洞被追踪为 CVE-2024-7261，CVSS v3 得分为 9.8，是一个输入验证故障，由用户提供的数据处理不当引起，允许远程攻击者在主机操作系统上执行任意命令。

Zyxel 警告称某些 AP 和安全路由器版本的 CGI 程序对参数 “host ”中特殊元素的中和不当，可能允许未经认证的攻击者通过向有漏洞的设备发送伪造的 cookie 来执行操作系统命令。

受 CVE-2024-7261 影响的 Zyxel 接入点 (AP) 如下：

* NWA 系列： NWA50AX、NWA50AX PRO、NWA55AXE、NWA90AX、NWA90AX PRO、NWA110AX、NWA130BE、NWA210AX、NWA220AX-6E | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ABYW.2) 及更高版本、NWA1123-AC PRO | 6.28 之前的所有版本易受攻击，请升级至 6.28(ABHD.3) 及更高版本、NWA1123ACv3、WAC500、WAC500H | 6.70 之前的所有版本易受攻击，请升级至 6.70(ABVT.5) 及更高版本
* WAC 系列： WAC6103D-I、WAC6502D-S、WAC6503D-S、WAC6552D-S、WAC6553D-E | 6.28 之前的所有版本易受攻击，请升级至 6.28(AAXH.3) 及更高版本
* WAX 系列： WAX300H、WAX510D、WAX610D、WAX620D-6E、WAX630S、WAX640S-6E、WAX650S、WAX655E | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ACHF.2) 及更高版本。
* WBE 系列： WBE530、WBE660S | 7.00 之前的所有版本都存在漏洞，请升级至 7.00(ACLE.2) 及更高版本

Zyxel 表示，运行 V2.00(ACIP.2)的安全路由器 USG LITE 60AX 也受影响，但该型号已通过云自动更新到 V2.00(ACIP.3)，其中实施了 CVE-2024-7261 的修补程序。

## 更多 Zyxel 修复

Zyxel 还针对 APT 和 USG FLEX 防火墙中的多个高严重性缺陷发布了安全更新。摘要如下：

* **CVE-2024-6343：**CGI 程序中的缓冲区溢出可能导致通过身份验证的管理员发送伪造的 HTTP 请求，从而导致 DoS。
* **CVE-2024-7203：**验证后命令注入允许通过伪造的 CLI 命令执行操作系统命令。
* **CVE-2024-42057：**在 IPSec VPN 中的指令注入，允許未認證的攻擊者在「使用者為本-PSK」模式下，利用偽造的長使用者名稱執行作業系統指令。
* **CVE-2024-42058：**取消引用空指针可通过未认证攻击者发送的伪造数据包导致 DoS。
* **CVE-2024-42059：**身份验证后命令注入允许身份验证的管理员通过 FTP 上传伪造的压缩语言文件执行操作系统命令。
* **CVE-2024-42060：** 認證後指令注入漏洞，令已認證的管理員可透過上載精心製作的內部使用者協議檔案，執行作業系統指令。
* **CVE-2024-42061：**dynamic\_script.cgi "中的反射 XSS 允许攻击者诱骗用户访问伪造的 URL，从而可能泄漏基于浏览器的信息。

上述漏洞中 CVE-2024-42057 值得特别关注 ，它是 IPSec VPN 功能中的命令注入漏洞，无需验证即可被远程利用。

利用漏洞所需的特定配置要求会降低其严重性，包括在基于用户的 PSK 身份验证模式下配置设备，以及用户的用户用户名长度超过 28 个字符。

![1725417958_66d7c9e69d7c41407005b.png!small?1725417958629](https://image.3001.net/images/20240904/1725417958_66d7c9e69d7c41407005b.png!small?1725417958629)

图源：Zyxel 官网

有关其他受影响的防火墙更多详细信息，可具体查看 Zyxel 公告。

> 参考来源：[Zyxel warns of critical OS command injection flaw in routers (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/zyxel-warns-of-critical-os-command-injection-flaw-in-routers/)

# 路由器漏洞 # Zyxel

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

更多 Zyxel 修复

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