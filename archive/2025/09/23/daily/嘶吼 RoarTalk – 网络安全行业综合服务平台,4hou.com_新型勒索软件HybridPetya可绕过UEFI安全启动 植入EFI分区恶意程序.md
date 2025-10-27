---
title: 新型勒索软件HybridPetya可绕过UEFI安全启动 植入EFI分区恶意程序
url: https://www.4hou.com/posts/rp16
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-23
fetch_date: 2025-10-02T20:31:03.354300
---

# 新型勒索软件HybridPetya可绕过UEFI安全启动 植入EFI分区恶意程序

新型勒索软件HybridPetya可绕过UEFI安全启动 植入EFI分区恶意程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 新型勒索软件HybridPetya可绕过UEFI安全启动 植入EFI分区恶意程序

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-22 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)33718

收藏

导语：HybridPetya的出现与BlackLotus、BootKitty、Hyper-V后门等案例一样，再次证明具备“安全启动绕过”功能的UEFI引导工具包（bootkit）已构成真实威胁。

近期发现的一款名为“HybridPetya”的勒索软件变种，能够绕过UEFI安全启动（UEFI Secure Boot）功能，在EFI系统分区中安装恶意程序。

HybridPetya的设计明显受2016至2017年间活跃的破坏性恶意软件Petya/NotPetya的启发——后者曾通过加密计算机数据阻止Windows启动，且未提供任何数据恢复途径。

网络安全公司ESET的研究人员在VirusTotal平台上发现了HybridPetya的样本，并指出该样本可能是一个研究项目、概念验证代码（proof-of-concept），或是仍处于有限测试阶段的网络犯罪工具早期版本。

即便如此，ESET强调，HybridPetya的出现与BlackLotus、BootKitty、Hyper-V后门等案例一样，再次证明具备“安全启动绕过”功能的UEFI引导工具包（bootkit）已构成真实威胁。

**HybridPetya的技术特征与攻击流程**

HybridPetya融合了Petya与NotPetya的特性，包括这两款早期恶意软件的界面风格与攻击链；此外，开发者还新增了两项关键功能：可植入EFI系统分区，以及能利用CVE-2024-7344漏洞绕过安全启动。

CVE-2024-7344漏洞由ESET于今年1月发现，该漏洞存在于微软签名的应用程序中——即便目标设备开启了安全启动保护，攻击者仍可利用该漏洞部署引导工具包。

HybridPetya的攻击流程如下：

![execution-logic.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757924742148901.jpg "1757924165133904.jpg")

执行逻辑

1. 环境检测与文件投放：启动后，首先判断主机是否采用“UEFI+GPT分区”架构，随后在EFI系统分区中植入包含多个文件的恶意引导工具包，包括配置文件、验证文件、修改后的引导程序、备用UEFI引导程序、漏洞利用载荷容器，以及用于跟踪加密进度的状态文件。

2. 关键文件替换与备份：ESET列出了已分析的HybridPetya变种所使用的核心文件：

1. \EFI\Microsoft\Boot\config：存储加密标识、密钥、随机数（nonce）及受害者ID；

2.\EFI\Microsoft\Boot\verify：用于验证解密密钥是否正确；

3.\EFI\Microsoft\Boot\counter：记录已加密簇（cluster）的进度；

4.\EFI\Microsoft\Boot\bootmgfw.efi.old：原始引导程序的备份文件；

5.\EFI\Microsoft\Boot\cloak.dat：在“安全启动绕过”变种中存储经XOR加密的引导工具包。

同时，恶意软件会将\EFI\Microsoft\Boot\bootmgfw.efi替换为存在漏洞的“reloader.efi”，并删除\EFI\Boot\bootx64.efi；原始Windows引导程序会被保留，以便受害者支付赎金后恢复系统时激活。

3. 系统中断与加密执行：部署完成后，HybridPetya会触发蓝屏（BSOD）并显示伪造错误信息（与Petya的手法一致），强制系统重启；重启后，恶意引导工具包随之执行，随后勒索软件会从config文件中提取Salsa20密钥与随机数，对所有主文件表（MFT）簇进行加密，同时显示伪造的磁盘检查（CHKDSK）消息（模仿NotPetya的特征）。

![chdck.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757924743170315.png "1757924298191961.png")

虚假CHKDSK消息

4. 赎金索取：加密完成后，系统再次重启，受害者在启动阶段会看到赎金通知，要求支付1000美元比特币；作为交换，攻击者会提供一个32字符的密钥——受害者在赎金通知界面输入该密钥后，系统会恢复原始引导程序、解密已加密簇，并提示用户重启电脑。

![note.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250915/1757924743172264.png "1757924267862466.png")

HybridPetya的勒索信

**风险提示与防御建议**

目前尚未观察到HybridPetya在野外发起实际攻击，但类似项目随时可能将这一概念验证代码武器化，针对未打补丁的Windows系统发起大规模攻击。

目前，微软已在2025年1月的周二补丁日中修复了CVE-2024-7344漏洞，因此安装了该补丁或后续安全更新的Windows系统可抵御HybridPetya攻击。

此外，防范勒索软件的另一重要措施是：定期对核心数据进行离线备份，确保系统可免费且便捷地进行恢复。

文章翻译自：https://www.bleepingcomputer.com/news/security/new-hybridpetya-ransomware-can-bypass-uefi-secure-boot/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?AqMvmuL7)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)