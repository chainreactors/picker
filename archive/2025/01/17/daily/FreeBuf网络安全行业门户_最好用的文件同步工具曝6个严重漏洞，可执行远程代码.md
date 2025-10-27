---
title: 最好用的文件同步工具曝6个严重漏洞，可执行远程代码
url: https://www.freebuf.com/news/419987.html
source: FreeBuf网络安全行业门户
date: 2025-01-17
fetch_date: 2025-10-06T20:10:19.322528
---

# 最好用的文件同步工具曝6个严重漏洞，可执行远程代码

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

最好用的文件同步工具曝6个严重漏洞，可执行远程代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

最好用的文件同步工具曝6个严重漏洞，可执行远程代码

2025-01-16 13:56:20

所属地 上海

![](https://image.3001.net/images/20250116/1737006969_67889f7900d9198a5a8b4.png!small)

超过660000台暴露的Rsync服务器可能受到六个新漏洞的攻击，其中包含一个严重程度极高的堆缓冲区溢出漏洞，该漏洞允许在服务器上执行远程代码。

Rsync是一款开源的文件同步和数据传输工具，因其能够执行增量传输而备受青睐，可减少数据传输时间和带宽使用量。它支持本地文件系统传输、通过安全协议如SSH进行远程传输，并可以通过其自身的守护进程直接同步文件。

该工具被诸如Rclone、DeltaCopy、ChronoSync等备份系统，公共文件分发仓库以及云和服务器管理操作广泛使用。

Rsync漏洞由Google Cloud和独立安全研究人员发现，可组合形成强大的利用链，导致远程系统被攻陷。Openwall 发布的公告称：“在最严重的CVE漏洞中，攻击者仅需对Rsync服务器拥有匿名读取权限，例如公共镜像，便可在服务器运行的机器上执行任意代码。”

**以下是六个漏洞的概述：**

1. **堆缓冲区溢出（CVE-2024-12084）**：由于Rsync守护进程对校验和长度处理不当而产生的漏洞，导致缓冲区出现越界写入。影响版本为3.2.7至<3.4.0，可实现任意代码执行。缓解措施是编译时使用特定标志禁用SHA256和SHA512摘要支持。（CVSS评分：9.8）
2. **通过未初始化栈泄露信息（CVE-2024-12085）**：当比较文件校验和时，该漏洞可导致泄露未初始化的栈数据。攻击者可操纵校验和长度来利用此漏洞。影响所有低于3.4.0的版本，通过编译时使用-ftrivial-auto-var-init=zero标志初始化栈内容可实现缓解。（CVSS评分：7.5）
3. **服务器泄露任意客户端文件（CVE-2024-12086）**：该漏洞允许恶意服务器在文件传输过程中，通过操纵校验和值，逐字节枚举和重构任意客户端文件。所有低于3.4.0版本均受影响。（CVSS评分：6.1）
4. **通过--inc-recursive选项实现路径穿越（CVE-2024-12087）**：使用--inc-recursive选项时，由于符号链接验证不足引发此问题。恶意服务器可在客户端的预期目录之外写入文件。所有低于3.4.0版本均存在漏洞。（CVSS评分：6.5）
5. **绕过--safe-links选项（CVE-2024-12088）**：当Rsync未能正确验证包含其他链接的符号链接目标时出现此漏洞。会导致路径穿越和在指定目录之外写入任意文件。所有低于3.4.0版本均受影响。（CVSS评分：6.5）
6. **符号链接竞态条件（CVE-2024-12747）**：由于处理符号链接时出现竞态条件导致此漏洞。利用该漏洞，攻击者可能获取敏感文件并提升权限。所有低于3.4.0版本均受影响。（CVSS评分：5.6）

CERT发布了有关Rsync漏洞的公告，将Red Hat、Arch、Gentoo、Ubuntu NixOS、AlmaLinux OS基金会以及Triton数据中心列为受影响方。更多可能受影响的项目和供应商尚未做出回应。

CERT警告称：“前两个漏洞（堆缓冲区溢出和信息泄露）组合起来，允许客户端在运行Rsync服务器的设备上执行任意代码。客户端只需对服务器进行匿名读取访问，例如公共镜像。此外，攻击者可控制恶意服务器，读取/写入任何连接客户端的任意文件。提取例如SSH密钥的敏感数据，并通过覆盖文件（如~/.bashrc或~/.popt）来执行恶意代码。”

RedHat在关于CVE-2024-12084的公告中指出没有实际的缓解措施，该漏洞在Rsync的默认配置下即可被利用。RedHat 解释道：“请记住，Rsync的默认rsyncd配置允许匿名文件同步，这存在该漏洞的风险。否则，攻击者需要拥有需要认证的服务器的有效凭证。”

建议所有用户都尽快升级至3.4.0版本。

[Openwall安全公告](https://www.openwall.com/lists/oss-security/2025/01/14/3)

[Redhat安全公告](https://access.redhat.com/security/cve/cve-2024-12084#cve-cvss-v3)

**参考链接：**

> <https://www.bleepingcomputer.com/news/security/over-660-000-rsync-servers-exposed-to-code-execution-attacks/>

# 资讯 # 系统安全

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