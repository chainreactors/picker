---
title: 【威胁情报】2026年4月7日 APT热点威胁样本采集（含HASH IOC）
url: https://mp.weixin.qq.com/s/_I48_mYveJtZLXyfcRsRLg
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:32.385207
---

# 【威胁情报】2026年4月7日 APT热点威胁样本采集（含HASH IOC）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zNsFJyIuL0FDaSFc0wNGZc0SJicQLiaUaml5Ria9t6SFD9WIVVHUDhRVYaShqrzAdml5oXoDMriaia4lRFyFbMunaITQZSTUE5tE8iccLlBnNYwfY/0?wx_fmt=jpeg)

# 【威胁情报】2026年4月7日 APT热点威胁样本采集（含HASH IOC）

Ots安全

![]()

在小说阅读器中沉浸阅读

**威胁简报**

**恶意软件**

**漏洞攻击**

今日（2026年4月7日）网络安全社区热点中，APT相关威胁样本主要集中在MalwareBazaar新曝光的OilRig组织关联样本，以及近期CISA披露的BRICKSTORM后门和Viettel报告的ToneShell（Mustang Panda新武器）样本。这些样本均与国家背景APT组织活动高度相关，涉及持久化后门、钓鱼投递和虚拟化环境渗透。攻击者通过合法伪装和多阶段加载实现长期驻留，未及时检测的环境面临高风险。

公开情报显示，OilRig样本于4月6日在X平台被威胁情报分析师提及并上传MalwareBazaar，引发社区关注；BRICKSTORM为PRC赞助网络行为体针对VMware vSphere的长期持久化工具；ToneShell则是Mustang Panda替换PlugX的新后门，已在东南亚多国广泛部署。以下基于公开报告和社区讨论，采集并汇总今日热点样本HASH及关联IOC。

事件背景与时间线

* 2026年4月6日：X平台威胁情报账号披露Bangladesh来源OilRig关联样本（0014.docm），快速登上MalwareBazaar，社区热议其与中东APT组织历史TTP的重叠。
* 2026年2月11日（最新更新）：CISA、NSA联合发布BRICKSTORM后门分析报告，确认PRC赞助APT行为体针对政府与IT基础设施的长期攻击。
* 2025年10月-2026年4月：Viettel Threat Intelligence持续追踪ToneShell（Mustang Panda）新变种，通过东南亚地缘政治主题钓鱼包投递，已观察到2025年4月最新版本。

这些样本反映当前APT活动向虚拟化平台、Android/文档伪装和地区热点话题倾斜的趋势。

攻击手法与TTPs分析

OilRig关联样本：典型文档宏/加载器形式，结合历史TTP使用钓鱼文档投递，执行后建立C2通信，实现信息窃取。社区分析指向中东地区APT行为体，行为与OilRig经典Watering Hole或鱼叉攻击一致。

BRICKSTORM后门（PRC赞助APT）：

* 初始访问：通过Web Shell进入（T1505.003）。
* 执行与持久化：修改init文件、复制至/etc/sysconfig/、PATH环境变量劫持、自监视重装机制（T1037、T1574.007）。
* 伪装与规避：进程名伪装（如squid）、XOR字符串加密、AOT编译变种；针对VMware vSphere（vCenter/ESXi）环境优化。
* 凭证访问：复制ntds.dit、RDP横向移动（T1003.003、T1021.001）。

ToneShell（Mustang Panda）：

* 投递方式：压缩包+伪造文档（.zip/.exe伪装地缘政治文件，如南海争端、ASEAN峰会报告）。
* 加载机制：DLL侧加载（jxbrowser-chromium-lib.dll、VFAViewvntfxf32.dll等），RC4加密HTTP POST通信。
* 持久化：辅助组件TonePipeShell实现隔离网持久化；与PlugX/PUBLOAD共享DLL和C2基础设施。
* 演进：2021年首现，2024-2025年多次更新，已替代部分传统武器。

影响范围与受害者画像

* OilRig：主要影响中东及Bangladesh相关政府/企业。
* BRICKSTORM：针对政府服务、IT设施、VMware虚拟化环境，受害者多为关键基础设施运营商。
* ToneShell：东南亚国家（菲律宾、泰国、新加坡、缅甸）政府、外交及国防相关实体，钓鱼主题紧扣地区热点。

高价值目标包括政府机构、国防、科研及关键信息基础设施运营商。

```
OilRig关联 3a787a7b850b92a99d20f52747f1e13428039a149b7dd6295f6ca11995d88e0a0014.docmOilRig（中东APT） MalwareBazaar，4月6日曝光
BRICKSTORM (Go变种) aaf5569c8e349c15028bc3fac09eb982efb06eabac955b705a6d447263658e38vmsrcPRC赞助APTCISAAR25-338A
BRICKSTORM (Go变种) 013211c56caaa697914b5b5871e4998d0298902e336e373ebb27b7db30917eafvnetdPRC赞助APTCISAAR25-338A
BRICKSTORM (Go变种) b3b6a992540da96375e4781afd3052118ad97cfe60ccf004d732f76678f6820aviocliPRC赞助APTCISAAR25-338A
BRICKSTORM (Rust变种) 6a67a9769a55ec889a5dd4199b2fc08965d39d737838836853bc13c81c56a800-PRC赞助APTCISA2025.12更新
BRICKSTORM (AOT变种) 24a11a26a2586f4fba7bfe89df2e21a0809ad85069e442da98c37c4add369a0csupportPRC赞助APTCISA2026.2更新
ToneShell2024e4a4803cb04b58c07230b13682fe1cf7e3aa7ffab434e8914321941cd04d8a5fAssessmentReport...zipMustangPandaViettel报告
ToneShell20242b0882fbcfd8fcbc84cc7c63a22a2ef10900a8addfe7e73b231c32f60ceaf34eDefense_Cooperation... MustangPandaViettel报告
ToneShell04/202598c1527d4b064fcf4a95488c34576e5f443585cb6e385c7b8765e63fa9e83ccc46th_ASEAN_Summit.zipMustangPandaViettel报告
ToneShell (早期) 521662079c1473adb59f2d7134c8c1d76841f2a0f9b9e6e181aa54df25715a09-MustangPanda2021首现样本
```

补充C2 IOC（部分共享）：98.142.251.29、103.27.109.157、202.58.105.38等（ToneShell/PlugX共用）。

总结

2026年4月7日APT热点样本以OilRig复现、BRICKSTORM持久化后门及ToneShell地区针对性攻击为主，体现国家背景组织对虚拟化平台和地缘热点的持续关注。组织应优先验证上述HASH并强化虚拟化及文档投递防御，降低后渗透风险。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zNsFJyIuL0EXfNxnRl4wXXQHXM8pTne04s91KvYkkbTwBIvBuuOhTz4JiaOws6QVa7LFicicI6rP9qEto41p9ulmT3ELRtIMyLhNGbrTPpfMTc/640?wx_fmt=jpeg&from=appmsg)

公众号内容都来自国外平台-所有文章可通过点击阅读原文到达原文地址或参考地址

排版 编辑 | Ots 小安

采集 翻译 | Ots Ai牛马

公众号 | AnQuan7 (Ots安全)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

Ots安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rWGOWg48tadhkzMbpPpSw6NfJHUgsHudwQFGS0EobaB49HVwda7L2eJiaDMvwpakagffpPgepM6gBZzpCncMMHg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过