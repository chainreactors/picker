---
title: 又一新型恶意软件曝光！已向全球70多家企业发起网络攻击
url: https://www.freebuf.com/news/409960.html
source: FreeBuf网络安全行业门户
date: 2024-09-03
fetch_date: 2025-10-06T18:24:36.129990
---

# 又一新型恶意软件曝光！已向全球70多家企业发起网络攻击

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

又一新型恶意软件曝光！已向全球70多家企业发起网络攻击

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

又一新型恶意软件曝光！已向全球70多家企业发起网络攻击

2024-09-02 09:28:23

所属地 上海

![1725244492_66d5244c15a1623bd258e.png!small?1725244492486](https://image.3001.net/images/20240902/1725244492_66d5244c15a1623bd258e.png!small?1725244492486)

研究人员发现有一个新的恶意软件活动通过冒充美国、欧洲和亚洲的税务机构，向世界各地的组织传播一种名为 “Voldemort ”的后门程序，该后门程序此前从未被记录过 。

根据 Proofpoint 的一份报告，该活动始于 2024 年 8 月 5 日，已向 70 多个目标组织传播了 2 万多封电子邮件，在活动高峰期一天就达到了 6000 封。这其中超过一半的目标组织属于保险、航空航天、运输和教育部门。这次活动背后的威胁行为者尚不清楚，但 Proofpoint 认为最有可能的目的是进行网络间谍活动。

这次攻击与 Proofpoint 在月初描述的情况类似，但在最后阶段涉及不同的恶意软件集。

## 冒充税务机关炮制钓鱼邮件

根据Proofpoint 的一份新报告称，攻击者正在根据公共信息制作与目标组织所在地相匹配的网络钓鱼电子邮件。这些钓鱼邮件冒充组织所在国家的税务机关，声称有最新的税务信息，并包含相关文件的链接。

![1725240102_66d51326da127bec953da.png!small](https://image.3001.net/images/20240902/1725240102_66d51326da127bec953da.png!small)

活动中使用的恶意电子邮件样本，来源：Proofpoint

点击链接后，收件人会进入一个由 InfinityFree 托管的登陆页面，该页面使用谷歌 AMP 缓存 URL 将受害者重定向到一个带有 “点击查看文档 ”按钮的页面。

点击按钮后，页面会检查浏览器的用户代理，如果是 Windows 系统，则会将目标重定向到指向 TryCloudflare 通道 URI 的 search-ms URI（Windows 搜索协议）。非 Windows 用户会被重定向到一个空的 Google Drive URL，该 URL 不会提供任何恶意内容。

如果受害者与 search-ms 文件交互，Windows 资源管理器就会被触发，显示伪装成 PDF 的 LNK 或 ZIP 文件。

URI 最近在网络钓鱼活动中很流行，因为即使该文件托管在外部 WebDAV/SMB 共享上，它也会被伪装成本地下载文件夹中的文件，诱骗受害者打开。

![1725240141_66d5134d71e8ad7877a45.png!small](https://image.3001.net/images/20240902/1725240141_66d5134d71e8ad7877a45.png!small)

让文件看起来就像在受害者的电脑上一样，来源：Proofpoint

Proofpoint 发现，有一种恶意软件会从另一个 WebDAV 共享中执行一个 Python 脚本，而不会在主机上下载该脚本，该脚本会执行系统信息收集，对受害者进行剖析。与此同时，还会显示一个诱饵 PDF 来掩盖恶意活动。

![1725240164_66d51364ef394bda44cf3.png!small](https://image.3001.net/images/20240902/1725240164_66d51364ef394bda44cf3.png!small)

转移受害者注意力的诱饵 PDF，来源：Proofpoint

该脚本还下载了一个合法的 Cisco WebEx 可执行文件（CiscoCollabHost.exe）和一个恶意 DLL（CiscoSparkLauncher.dll），以使用 DLL 侧载加载 Voldemort。

## 滥用谷歌工作表发动攻击

Voldemort 是一款基于 C 语言的后门程序，支持多种命令和文件管理操作，包括外渗、向系统引入新的有效载荷和文件删除。

支持的命令列表如下：

* Ping - 测试恶意软件与 C2 服务器之间的连接性。
* Dir - 从受感染系统中检索目录列表。
* 下载 - 将文件从受感染系统下载到 C2 服务器。
* 上传 - 将文件从 C2 服务器上传到受感染系统。
* Exec - 在受感染系统上执行指定命令或程序。
* 复制 - 在受感染系统内复制文件或目录。
* Move - 移动受感染系统内的文件或目录。
* Sleep - 在指定时间内使恶意软件进入睡眠模式，在此期间不会执行任何活动。
* 退出 - 终止恶意软件在受感染系统上的运行。
* Voldemort 的一个显著特点是将 Google Sheets 用作命令和控制服务器 (C2)，通过 ping 获取在受感染设备上执行的新命令，并将其作为窃取数据的存储库。

每台受感染的机器都会将数据写入谷歌工作表中的特定单元格，这些单元格可以用 UUID 等唯一标识符指定，从而确保隔离和更清晰地管理被入侵的系统。

![1725240464_66d514907a806071f86e1.png!small](https://image.3001.net/images/20240902/1725240464_66d514907a806071f86e1.png!small)

请求从 Google 接收访问令牌，来源：Proofpoint

Voldemort 使用带有嵌入式客户端 ID、秘密和刷新令牌的 Google API 与 Google Sheets 进行交互，这些信息存储在其加密配置中。

这种方法为恶意软件提供了一个可靠且高度可用的 C2 通道，还降低了网络通信被安全工具标记的可能性。由于企业普遍使用 Google Sheets，因此封锁该服务也是不切实际的。

但为了降低这类攻击带来的安全风险，Proofpoint 建议将外部文件共享服务的访问权限限制在受信任的服务器上，在没有主动需要的情况下阻止与 TryCloudflare 的连接，并监控可疑的 PowerShell 执行。

> 参考来源：[New Voldemort malware abuses Google Sheets to store stolen data](https://www.bleepingcomputer.com/news/security/new-voldemort-malware-abuses-google-sheets-to-store-stolen-data/)

# 恶意软件 # 谷歌

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

冒充税务机关炮制钓鱼邮件

滥用谷歌工作表发动攻击

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