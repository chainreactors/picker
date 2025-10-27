---
title: 新型僵尸网络正对路由器、摄像头等设备发起大规模DDoS攻击
url: https://www.freebuf.com/news/420383.html
source: FreeBuf网络安全行业门户
date: 2025-01-22
fetch_date: 2025-10-06T20:09:28.733886
---

# 新型僵尸网络正对路由器、摄像头等设备发起大规模DDoS攻击

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

新型僵尸网络正对路由器、摄像头等设备发起大规模DDoS攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

新型僵尸网络正对路由器、摄像头等设备发起大规模DDoS攻击

2025-01-21 11:04:23

所属地 上海

趋势科技的一项新研究发现，自 2024 年底以来，一个新发现的物联网 （IoT） 僵尸网络一直利用路由器、IP 摄像头和其他连接设备等物联网设备中的漏洞，在全球策划大规模分布式拒绝服务 （DDoS） 攻击。

![](https://image.3001.net/images/20250121/1737428755_678f0f130e34f01ede788.png!small)

安全研究人员警告说，该僵尸网络利用源自另外两个僵尸网络Mirai 和 Bashlite 的恶意软件，对全球工业和关键基础设施构成了重大威胁。

该僵尸网络通过利用远程代码执行 （RCE） 漏洞或弱默认凭据来感染 IoT 设备，感染过程涉及多个阶段：

1. **初始利用**：恶意软件通过漏洞或暴力破解弱密码渗透到设备中。
2. **负载传递**：加载程序脚本从分发服务器下载主要的恶意软件负载。有效负载直接在内存中执行，以避免在受感染设备上留下痕迹。
3. **命令和控制（C&C）：**一旦被感染，设备就会连接到C&C服务器以接收攻击命令。

该僵尸网络使用各种 DDoS 攻击媒介，包括：

* **SYN 泛洪**：TCP 连接请求使服务器不堪重负。
* **UDP 泛洪**：使用 UDP 数据包使网络饱和。
* **GRE 协议漏洞**：使用通用路由器封装以路由器为目标。
* **TCP 握手泛洪**：建立大量虚假 TCP 连接以耗尽服务器资源。

趋势科技安全专家指出，这些命令的结构为文本消息，前缀为两个字节长度的字段，从而可以精确控制攻击参数，例如持续时间和目标 IP 地址。

通过对僵尸网络的技术分析，发现已实现了广泛的地理覆盖范围，北美和欧洲受到严重影响，美国占已确定目标的 17%。日本也面临重大攻击，尤其是针对其金融和运输行业的攻击。 大多数受感染的设备是无线路由器 （80%），其次是 IP 摄像头 （15%），其中包括 TP-Link 和 Zyxel等知名但又容易遭受到攻击的品牌。

为了增强隐蔽性，僵尸网络利用恶意软件在受感染的设备上禁用了看门狗计时器，从而防止在 DDoS 攻击引起的高负载期间自动重启，并且还操纵基于Linux的iptables规则来阻止外部访问，同时保持与C&C服务器的通信。

安全专家推荐了几种措施来降低 IoT 僵尸网络感染的风险：-

* 在设备安装后立即更改默认密码。
* 定期更新固件以修补已知漏洞。
* 将 IoT 设备隔离在单独的网络中。
* 使用入侵检测系统 （IDS） 来识别异常流量模式。

同时建议企业组织与服务提供商合作，过滤恶意流量，并考虑部署 CDN 以在 DDoS 攻击期间进行负载分配。

**参考来源：**

> [New IoT Botnet Launching Large-Scale DDoS Attacks Hijacking IoT Devices](https://cybersecuritynews.com/new-iot-botnet-launching-large-scale-ddos-attacks/#google_vignette)

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