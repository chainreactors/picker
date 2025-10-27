---
title: Ebury 僵尸网络自 2009 年起已感染 40 万台 Linux 服务器
url: https://www.freebuf.com/news/400974.html
source: FreeBuf网络安全行业门户
date: 2024-05-16
fetch_date: 2025-10-06T17:16:09.698837
---

# Ebury 僵尸网络自 2009 年起已感染 40 万台 Linux 服务器

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

Ebury 僵尸网络自 2009 年起已感染 40 万台 Linux 服务器

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Ebury 僵尸网络自 2009 年起已感染 40 万台 Linux 服务器

2024-05-15 09:54:26

所属地 上海

![Linux_tux.jpg](https://image.3001.net/images/20240515/1715740880_664420d0e285de2376a01.jpg!small)

据ESET 研究人员表示，自 2009 年以来，一个名为 "Ebury "的恶意软件僵尸网络已经感染了近 40 万台 Linux 服务器，截至 2023 年底，仍有约 10 万台服务器受到攻击。

以下是 ESET 自 2009 年以来记录的 Ebury 感染情况，可见随着时间的推移，感染量明显增长。

![volume.jpeg](https://image.3001.net/images/20240515/1715740889_664420d90926ddb26104c.jpeg!small)

Ebury攻击量随时间变化，来源：ESET

在近日发布的最新更新中，ESET报告称，最近的一次执法行动使他们得以深入了解恶意软件在过去15年中的活动。虽然 40万是一个庞大的数字，但这的确是近 15 年来的入侵数量。不过这些并非是在同一时间被入侵的。

ESET解释说：在其他服务器被清理或退役的同时，不断有新的服务器被入侵。研究所掌握的数据并不能说明攻击者何时失去了对系统的访问权限，因此很难知道僵尸网络在任何特定时间点的规模。

## Ebury 的最新策略

最近的 Ebury 攻击表明，操作者倾向于入侵托管提供商，并对租用被入侵提供商虚拟服务器的客户实施供应链攻击。

最初的入侵是通过凭证填充攻击进行的，使用窃取的凭证登录服务器。一旦服务器被入侵，恶意软件就会从 wtmp 和 known\_hosts 文件中渗出入站/出站 SSH 连接列表，并窃取 SSH 身份验证密钥，然后利用这些密钥尝试登录其他系统。

ESET 的详细报告中写道：当 known\_hosts 文件包含散列信息时，作案者会尝试对其内容进行暴力破解。

在 Ebury 操作员收集的 480 万个 known\_hosts 条目中，约有 200 万个条目对其主机名进行了散列。在这些散列主机名中，40%（约 80 万个）是猜测或暴力获取的。

另外，在可能的情况下，攻击者还可能利用服务器上运行的软件中已知的漏洞来获得进一步的访问权限或提升他们的权限。

![compromise.jpeg](https://image.3001.net/images/20240515/1715740895_664420df1d3ed8d9d4a9a.jpeg!small)

Ebury攻击链，来源：ESET

托管提供商的基础设施（包括 OpenVZ 或容器主机）可用于在多个容器或虚拟环境中部署 Ebury。

在下一阶段，恶意软件操作员通过使用地址解析协议（ARP）欺骗拦截这些数据中心内目标服务器上的 SSH 流量，将流量重定向到其控制的服务器。

一旦用户通过 SSH 登录受攻击的服务器，Ebury 就会捕获登录凭证。

![atim.jpeg](https://image.3001.net/images/20240515/1715740900_664420e4e261ffc3948c1.jpeg!small)

中路进攻战术，来源：ESET

在服务器托管加密货币钱包的情况下，Ebury 会使用捕获的凭据自动清空钱包。据悉，2023 年Ebury 使用这种方法攻击了至少 200 台服务器，其中包括比特币和以太坊节点。

不过，这些货币化策略各不相同，还包括窃取输入支付网站的信用卡信息、重定向网络流量以从广告和联盟计划中获取收入、利用被攻陷的服务器发送垃圾邮件以及出售捕获的凭据。

![proc-inj.png](https://image.3001.net/images/20240515/1715740910_664420ee79bcced5539c7.png!small)

注入主要有效载荷的进程，来源：ESET

在 2023 年底，ESET 观察到该软件引入了新的混淆技术和新的域生成算法 (DGA) 系统，使僵尸网络能够躲避检测并提高其抵御拦截的能力。

而根据 ESET 的最新发现，通过 Ebury 僵尸网络传播的恶意软件模块有：

* HelimodProxy： 通过修改mod\_dir.so Apache模块代理原始流量和转发垃圾邮件，允许被入侵的服务器运行任意命令并支持垃圾邮件活动。
* HelimodRedirect： 通过修改各种 Apache 和 nginx 模块，将 HTTP 流量重定向到攻击者控制的网站，从而将一小部分网络流量重定向到恶意网站。
* HelimodSteal： 通过添加一个输入过滤器，拦截并窃取通过网络表单提交的数据（如登录凭证和支付详情），从而从 HTTP POST 请求中窃取敏感信息。
* KernelRedirect： 通过使用挂接 Netfilter 的 Linux 内核模块，在内核级别修改 HTTP 流量以重定向访问者，改变 HTTP 响应中的位置标头，将用户重定向到恶意 URL。
* FrizzySteal： 通过挂钩 libcurl 来拦截和渗透 HTTP 请求，使其能够捕获和窃取被入侵服务器发出的 HTTP 请求中的数据。

![malware-families.png](https://image.3001.net/images/20240515/1715740916_664420f4dfdcc53339bb9.png!small)

Ebury的恶意软件模块，来源：ESET

ESET 的最新调查是与荷兰国家高科技犯罪小组（NHTCU）合作进行的，该小组最近查获了网络犯罪分子使用的备份服务器。

荷兰当局称，Ebury 的行为者使用通过 Vidar Stealer伪造或盗用的身份，有时甚至冒用其他网络犯罪分子的绰号来误导执法部门。

目前，NHTCU 正在调查在该服务器中发现的证据，包括包含历史记录和保存的登录信息等网络浏览痕迹的虚拟机，但目前还没有新发现。

> 参考来源：[Ebury botnet malware infected 400,000 Linux servers since 2009 (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/ebury-botnet-malware-infected-400-000-linux-servers-since-2009/)

# 僵尸网络 # Linux服务器

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

Ebury 的最新策略

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