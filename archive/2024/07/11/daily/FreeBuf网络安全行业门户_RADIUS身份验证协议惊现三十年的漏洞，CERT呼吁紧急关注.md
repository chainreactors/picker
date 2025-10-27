---
title: RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注
url: https://www.freebuf.com/news/405650.html
source: FreeBuf网络安全行业门户
date: 2024-07-11
fetch_date: 2025-10-06T17:44:30.283047
---

# RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注

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

RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

RADIUS身份验证协议惊现三十年的漏洞，CERT呼吁紧急关注

2024-07-10 15:47:24

所属地 上海

近日，网络安全研究人员发现RADIUS网络身份验证协议中存在一个安全漏洞，Blast-RADIUS可以利用该漏洞发动中间人（MitM）攻击，并在特定情况下绕过完整性检查，CERT、InkBridge Networks等多个安全机构呼吁积极关注该漏洞。

![](https://image.3001.net/images/20240710/1720597389_668e3b8d68aaa307006f8.png!small)

## 关于Blast-RADIUS

Blast-RADIUS是目前广泛应用的RADIUS/UDP协议中的一种认证绕过技术，可以使攻击者在中间人MD5冲突攻击中攻破网络和设备。

InkBridge Networks的首席执行官、FreeRADIUS项目的创始人Alan DeKok在一份声明中说：RADIUS 协议允许某些访问请求信息无需进行完整性或身份验证检查。

> RADIUS是远程身份验证拨号用户服务的简称，是一种客户端/服务器协议，为连接和使用网络服务的用户提供集中身份验证、授权和记账（AAA）管理。

RADIUS的安全性依赖于使用MD5算法导出的哈希值，由于存在碰撞攻击的风险，截至2008年12月，MD5算法被认为在密码学上已被破解。

因此，攻击者可以在不被发现的情况下修改这些数据包，将能够强制任何用户进行认证，并给予该用户任何授权（例如VLAN等）。

这意味着访问请求数据包可能会受到所谓的选定前缀攻击，使得可以修改响应数据包，以便它通过原始响应的所有完整性检查。

需要注意的是，要使攻击成功，攻击者必须修改在客户端和服务器之间传输的RADIUS数据包。那么，通过互联网发送数据包的组织将面临该漏洞带来的风险。

## 漏洞利用细节

Blast-RADIUS利用了一个新的协议漏洞CVE-2024-3596和MD5碰撞攻击，允许访问RADIUS流量的攻击者操纵服务器响应并添加任意协议属性，这使他们无需暴力或窃取凭证即可获得RADIUS设备的管理权限。

![](https://image.3001.net/images/20240710/1720597485_668e3bed8f704e8af0f1d.png!small)Blast-RADIUS研究人员解释说：Blast-RADIUS攻击允许位于RADIUS客户端和服务器之间的中间人对失败的认证请求伪造有效的“访问接受”响应。攻击者通过向有效的客户端请求中注入恶意的“代理状态”属性来实现这一点。这个“代理状态”属性肯定会在服务器的响应中被回显。攻击者构造“代理状态”，使得有效响应和攻击者希望伪造的响应之间的响应验证器值相同。这种伪造将导致NAS（网络访问服务器）在攻击者不猜测或暴力破解密码或共享机密的情况下授予对手对网络设备和服务的访问权限。

研究人员表示："利用此攻击的攻击者可以将部分网络访问权限升级为能够登录任何使用RADIUS进行身份验证的设备，或为自己分配任意网络权限。”

研究人员的概念验证漏洞（尚未共享）计算了伪造有效 "访问-接受 "响应所需的MD5选择前缀哈希冲突，以表示成功的身份验证请求。然后，利用中间人攻击将伪造的MD5哈希值注入网络通信，使攻击者能够登录。

伪造这个MD5哈希值需要3到6分钟，比RADIUS在实践中常用的30到60秒超时要长。

不过，攻击中使用的碰撞算法的每个步骤都可以有效地并行化，并适合硬件优化，这将使资源充足的攻击者能够使用GPU、FPGA或其他更现代、更快速的硬件来实施攻击，从而实现更快的运行时间，可能快数十倍或数百倍。

![](https://image.3001.net/images/20240710/1720597460_668e3bd4af83506fcf6a6.png!small)攻击流程（Blast-RADIUS 研究团队）

研究团队表示，虽然MD5哈希碰撞在2004年已首次被证实，但当时仍有人对在RADIUS协议中加以利用表示质疑。

## 缓解措施

由于这种攻击不会危及最终用户的凭证，因此最终用户无法采取任何防范措施。

不过，BlastRADIUS是一个基本设计缺陷的结果，据说会影响所有符合标准的RADIUS客户端和服务器，具体来说，PAP、CHAP和MS-CHAPv2认证方法是最脆弱的，建议使用该协议的互联网服务提供商(isp)和组织更新到最新版本。

网络运营商可以升级到RADIUS over TLS (RADSEC)，转而采用 "多跳 "RADIUS 部署，并使用限制访问管理VLAN 或 TLS/ IPsec隧道将RADIUS流量与互联网访问隔离。

另外，还可以通过Message-Authenticator属性提高数据包安全性。

参考来源：

https://www.blastradius.fail/attack-details

https://www.bleepingcomputer.com/news/security/new-blast-radius-attack-bypasses-widely-used-radius-authentication/

https://thehackernews.com/2024/07/radius-protocol-vulnerability-exposes.html

# MD5 # MD5碰撞 # RADIUS认证

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

关于Blast-RADIUS

漏洞利用细节

缓解措施

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