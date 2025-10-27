---
title: Sliver C2框架漏洞解析：攻击者可建立TCP连接窃取数据流量
url: https://www.freebuf.com/vuls/422839.html
source: FreeBuf网络安全行业门户
date: 2025-02-26
fetch_date: 2025-10-06T20:37:10.092003
---

# Sliver C2框架漏洞解析：攻击者可建立TCP连接窃取数据流量

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

Sliver C2框架漏洞解析：攻击者可建立TCP连接窃取数据流量

* ![]()
* 关注

* [漏洞](https://www.freebuf.com/articles/vuls)

Sliver C2框架漏洞解析：攻击者可建立TCP连接窃取数据流量

2025-02-25 11:15:14

所属地 上海

![image](https://image.3001.net/images/20250225/1740488516248295_a89c75257d0b4442b037a4383f429d24.webp!small)

近期，Sliver C2框架的团队服务器（teamserver）实现中被发现存在一个严重的服务器端请求伪造（SSRF）漏洞（CVE-2025-27090）。该漏洞允许攻击者通过受影响的服务器建立未授权的TCP连接，可能导致IP泄露、横向移动和流量拦截。

## **漏洞影响范围**

该漏洞影响Sliver C2框架的1.5.26至1.5.42版本，以及在Of340a2提交之前的预发布版本。尽管Sliver的架构通常会将团队服务器置于保护性重定向器之后，但该漏洞允许攻击者通过精心构造的植入物回调绕过这些保护措施。

![](https://image.3001.net/images/20250225/1740488518999102_a90189d3e92b419bb7e7b37da3f30eac.webp!small)
*Sliver的架构（来源：Chebuya）*

## **漏洞利用机制**

该漏洞利用链涉及Sliver Go代码库中的两个关键处理函数。首先，`registerSessionHandler`函数通过Protobuf反序列化为新植入物创建一个会话对象：

```
`// server/handlers/sessions.go
session := core.NewSession(implantConn)
core.Sessions.Add(session) // 将会话添加到团队服务器跟踪`
```

攻击者随后利用`tunnelDataHandler`，发送包含`CreateReverse`设置为true的特制TunnelData消息：

```
`// server/handlers/session.go
if rtunnel == nil && tunnelData.CreateReverse == true {
    createReverseTunnelHandler(implantConn, data) // 触发SSRF
}`
```

这将强制团队服务器通过`defaultDialer.DialContext`调用建立出站连接：

```
`remoteAddress := fmt.Sprintf("%s:%d", req.Rportfwd.Host, req.Rportfwd.Port)
dst, err := defaultDialer.DialContext(ctx, "tcp", remoteAddress)`
```

通过Sliver的隧道管理系统，该漏洞实现了双向通信。如下Python概念验证（PoC）代码所示，攻击者首先注册一个虚假会话，然后发起反向隧道：

```
`registration_envelope = generate_registration_envelope()
ssock.write(registration_envelope_len + registration_envelope)
reverse_tunnel_envelope = generate_create_reverse_tunnel_envelope(target_ip, port, data)
ssock.write(reverse_tunnel_envelope_len + reverse_tunnel_envelope)`
```

## **修复建议**

该漏洞已通过提交3f2a1b9修复，改进了会话验证和隧道创建检查。管理员应立即更新至Sliver v1.5.43及以上版本，并审核所有暂存监听器是否存在未授权的shellcode生成能力。

此SSRF漏洞突显了在C2框架处理双向网络通信时，严格输入验证的重要性。随着红队工具本身成为攻击目标，团队服务器组件的坚固隔离对于操作安全仍然至关重要。

**参考来源：**

> [Sliver C2 Server Vulnerability Let Attackers Open a TCP connection to Read Traffic](https://cybersecuritynews.com/sliver-c2-server-vulnerability/)

# 漏洞 # 网络安全

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