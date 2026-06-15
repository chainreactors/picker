---
title: 俄罗斯相关攻击者持续利用WinRAR漏洞攻击乌克兰目标
url: https://www.freebuf.com/articles/endpoint/486039.html
source: FreeBuf网络安全行业门户
date: 2026-06-14
fetch_date: 2026-06-15T07:09:32.129568
---

# 俄罗斯相关攻击者持续利用WinRAR漏洞攻击乌克兰目标

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
* [培训站](https://live.freebuf.com)
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

![](https://image.3001.net/images/20260209/1770606290323007_4a7b566114624e94b90bd2fe14b98aab.png) ![](https://image.3001.net/images/20260401/1775023076_69ccb3e4192f3c60ed43b.png)

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

俄罗斯相关攻击者持续利用WinRAR漏洞攻击乌克兰目标

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

俄罗斯相关攻击者持续利用WinRAR漏洞攻击乌克兰目标

2026-06-15 01:40:19

所属地 上海

![banner](https://image.3001.net/images/20260615/1781489086116176_1dbba3bc183f47349e81e7e798810b50.jpg!small)

## 已修复漏洞仍具杀伤力

尽管漏洞修复已近一年，与俄罗斯有关联的攻击者仍在持续利用WinRAR漏洞成功攻击大量乌克兰机构。根据趋势科技最新报告，早在2025年7月WinRAR 7.13版本中修复的路径遍历漏洞（CVE-2025-8088），截至2026年4月仍被多个威胁组织用于针对乌克兰机构的攻击活动。

## 漏洞利用机制解析

该漏洞利用NTFS备用数据流(ADS)特性实施攻击。受害者通常通过邮件收到RAR压缩包，其中包含可见的诱饵文档（如伪造的法院传票）以及隐藏的目录遍历序列。当使用存在漏洞的WinRAR版本解压时，压缩包会静默将文件写入解压目录之外的位置（通常是Windows启动目录），且不显示任何警告，受害者仅能看到诱饵文件。

报告披露了两个独立威胁集群：第一个被追踪为SHADOW-EARTH-066（CERT-UA编号UAC-0226），第二个是Earth Dahu（更广为人知的名称是Gamaredon），该组织自2013年起就持续针对乌克兰开展活动。

![WinRAR漏洞乌克兰攻击链](https://image.3001.net/images/20260615/1781489088364364_f69ced5311084e47a64832cc5ab6ee17.png!small)
SHADOW-EARTH-066从CVE-2025-8088漏洞利用到HTTPS数据外泄的攻击链 | 图片来源：趋势科技

## 从Excel宏到内存驻留恶意软件

SHADOW-EARTH-066的演变令人瞩目。该组织此前依赖包含宏的Excel文件和名为GIFTEDCROOK的基础窃密程序（通过硬编码的机器人令牌将窃取的浏览器数据发送至Telegram）。而最新报告显示，该组织在不到一年时间内，已从使用明文Telegram外传的基础Excel宏，升级为WinRAR漏洞利用链、通过直接NT系统调用实现内存DLL加载，以及加密的命令控制基础设施。

其新版载荷（内部命名为result.dll）完全通过NtAllocateVirtualMemory和NtCreateThreadEx等直接NT系统调用在内存中加载，规避常见API钩子。该恶意软件可窃取Chrome、Edge、Opera和Firefox的凭据，能绕过Chrome的应用绑定加密保护，并扫描35种扩展名的文件（包括文档、电子表格、压缩包甚至KeePass数据库）。在通过RC4加密的HTTPS将数据外传至专用命令服务器后，会彻底清除受感染设备上的所有痕迹。

## Earth Dahu采用不同攻击路径

与SHADOW-EARTH-066开发编译型恶意软件不同，Earth Dahu坚持使用脚本。其CVE-2025-8088漏洞利用版本仅向启动文件夹投放单个HTA文件。系统重启时，mshta.exe会自动执行该文件，通过Cloudflare Workers和动态DNS基础设施加载VBScript，最终投递间谍模块。

该组织使用HTTP基本认证格式伪造URL的伎俩尤为隐蔽——恶意链接会显示ssu.gov.ua等可信域名作为前缀，使受害者误认为正在访问合法的乌克兰政府网站。该活动的鱼叉邮件常来自被攻陷的政府和司法机构邮箱，多伪装成法院传票或财产扣押通知。

## 补丁为何无法根治问题

核心问题不在于漏洞本身，而在于补丁安装率。研究人员指出，WinRAR不支持自动更新和组策略配置，也无法通过WSUS、SCCM或Intune等企业补丁渠道分发，导致其几乎不会出现在标准漏洞管理程序的监测范围内——即使对具备成熟安全体系的机构也是如此。

这种现象并非首次出现。报告指出，2018年发现的WinRAR旧漏洞在修复后仍被用于针对性攻击长达数年，而CVE-2025-8088似乎正重蹈覆辙。趋势科技已发布完整技术分析报告，包含攻击指标(IOC)和检测指南。

## 企业应对建议

鉴于与俄罗斯有关联的威胁组织仍在广泛利用该漏洞，建议所有机构（特别是与乌克兰政府、军队或司法实体有关联者）使用第三方软件清点工具检查终端设备中的WinRAR旧版本（原生补丁管理系统无法识别）。安全团队还应监控启动文件夹中的异常LNK文件、非常规mshta.exe活动以及读取C:\ProgramData的PowerShell进程。考虑到未打补丁的压缩工具往往长期存在可利用漏洞，将其视为一次性修复任务是重大误区。

**参考来源：**

> [Old WinRAR Flaw Still Fuels Attacks on Ukraine in 2026](https://securityonline.info/winrar-vulnerability-ukraine-cve-2025-8088/)

# 终端安全 # 企业安全

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

![](https://image.3001.net/images/20250224/1740390949_67bc4225d82f40f9874cd.png)

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
* [![](https://image.3001.net/images/20260114/1768369539_69672d830bc432e202279.png)](https://www.trustasia.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2026 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)