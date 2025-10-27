---
title: 可绕过安全防护！EDR Silencer红队工具遭黑客利用
url: https://www.freebuf.com/news/412912.html
source: FreeBuf网络安全行业门户
date: 2024-10-17
fetch_date: 2025-10-06T18:52:09.561939
---

# 可绕过安全防护！EDR Silencer红队工具遭黑客利用

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

可绕过安全防护！EDR Silencer红队工具遭黑客利用

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

可绕过安全防护！EDR Silencer红队工具遭黑客利用

2024-10-16 09:58:42

所属地 上海

![hacker.jpg](https://image.3001.net/images/20241016/1729049080_670f31f838285c7395ac6.jpg!small)

近日，研究人员在恶意事件中观察到一种名为 EDRSilencer 的红队操作工具。 EDRSilencer 识别安全工具后会将其向管理控制台发出的警报变更为静音状态。

网络安全公司 Trend Micro 的研究人员说，攻击者正试图在攻击中整合 EDRSilencer，以逃避检测。

## 被“静音”的EDR 产品

端点检测和响应（EDR）工具是监控和保护设备免受网络威胁的安全解决方案。

它们使用先进的分析技术和不断更新的情报来识别已知和新的威胁，并自动做出响应，同时向防御者发送有关威胁来源、影响和传播的详细报告。

EDRSilencer 是受 MdSec NightHawk FireBlock（一种专有的笔试工具）启发而开发的开源工具，可检测运行中的 EDR 进程，并使用 Windows 过滤平台（WFP）监控、阻止或修改 IPv4 和 IPv6 通信协议的网络流量。

WFP 通常用于防火墙、杀毒软件和其他安全解决方案等安全产品中，平台中设置的过滤器具有持久性。

通过自定义规则，攻击者可以破坏 EDR 工具与其管理服务器之间的持续数据交换，从而阻止警报和详细遥测报告的发送。

在最新版本中，EDRSilencer 可检测并阻止 16 种现代 EDR 工具，包括：

* 微软卫士
* SentinelOne
* FortiEDR
* Palo Alto Networks Traps/Cortex XDR
* 思科安全端点（前 AMP）
* ElasticEDR
* Carbon Black EDR
* 趋势科技 Apex One

![blocks(1).jpg](https://image.3001.net/images/20241016/1729049083_670f31fbd05f1b7d972e7.jpg!small)

阻止硬编码可执行文件的传播，来源：趋势科技

趋势科技对 EDRSilencer 的测试表明，一些受影响的 EDR 工具可能仍能发送报告，原因是它们的一个或多个可执行文件未列入红队工具的硬编码列表。

不过，EDRSilencer 允许攻击者通过提供文件路径为特定进程添加过滤器，因此可以扩展目标进程列表以涵盖各种安全工具。

趋势科技在报告中解释说：在识别并阻止未列入硬编码列表的其他进程后，EDR 工具未能发送日志，这证实了该工具的有效性。

研究人员说：这使得恶意软件或其他恶意活动仍未被发现，增加了在未被发现或干预的情况下成功攻击的可能性。

![EDRSilencer-Fig10.jpg](https://image.3001.net/images/20241016/1729049087_670f31ff65a57272d4491.jpg!small)

EDRSilencer 攻击链，来源：趋势科技

趋势科技针对 EDRSilencer 的解决方案是将该工具作为恶意软件进行检测，在攻击者禁用安全工具之前阻止它。

此外，研究人员建议实施多层次的安全控制，以隔离关键系统并创建冗余，使用提供行为分析和异常检测的安全解决方案，在网络上寻找入侵迹象，并应用最小特权原则。

> 参考来源：[EDRSilencer red team tool used in attacks to bypass security (bleepingcomputer.com)](https://www.bleepingcomputer.com/news/security/edrsilencer-red-team-tool-used-in-attacks-to-bypass-security/)

# 安全攻击 # 红队工具

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

被“静音”的EDR 产品

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