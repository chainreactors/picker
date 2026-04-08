---
title: 网络安全正进入“高频攻击、低门槛、强对抗”的新阶段
url: https://mp.weixin.qq.com/s/X8NlifsvlV2hPfZspNoF1g
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:34:56.189594
---

# 网络安全正进入“高频攻击、低门槛、强对抗”的新阶段

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hlXiae3yiayvewufA4jbHakTyoaGz24qGZkGQkqhUmzj78lu4QUeEvNib5FIs2U3eGSmS5CnI21zJTpibrs175RxI1wnR56rk5kC88ATIAn9NtU/0?wx_fmt=jpeg)

# 网络安全正进入“高频攻击、低门槛、强对抗”的新阶段

安小圈

![]()

在小说阅读器中沉浸阅读

以下文章来源于河南等级保护测评
，作者铸盾安全

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6K0EVc7j5pWsAJ9u6w7rYeIAhXFEQq1xNsbnxs8DMtkQ/0)

**河南等级保护测评**
.

等级保护，不只是等级测评！一起探讨更全面的等级保护制度！ 做对用户有真实价值的网络安全服务，等级保护测评、风险评估、网络安全培训、网络安全咨询、网络安全合规。 传播网络安全知识，分享网络安全政策，共建风清气正的网络安全氛围。

---

**安小圈**

第888期

![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMBktbWEsll9n00m9KQoFFQnYPRP1dRSHObx4j1kok6vooVTjicyXxkAO7kUbdNKSb6eePhIUg955w/640?wx_fmt=png)

**1. Chrome 0-Day漏洞被在野利用事件**

2026年4月2日，CISA发布紧急警告，指出Google Chrome存在一个正在被攻击者利用的0-day漏洞（CVE-2026-5281）。该漏洞属于典型的Use-After-Free内存错误，位于WebGPU相关组件中，攻击者可借此实现远程代码执行或绕过浏览器安全机制。该漏洞已被纳入已知被利用漏洞目录（KEV），意味着其已在真实攻击中被使用，风险等级极高。

从攻击角度看，浏览器作为用户最常用的应用入口，一旦存在0-day漏洞，极易成为攻击链的初始突破口。攻击者通常通过恶意网页或钓鱼链接触发漏洞，实现无感知入侵。本次事件再次说明，客户端软件已成为当前攻击的重要切入点。

从防御角度看，补丁管理和快速更新仍是最有效手段。企业应建立浏览器版本统一管控机制，同时结合EDR对异常行为进行检测。该事件体现出：**漏洞利用正呈现“武器化速度快、利用门槛低”的趋势**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjo3KEFSQWwkVsxchBvPdu2Ae2unicVfe0yoP8eb8QexAv1644PucfULXJxtyu6uK5EbwmGHWHZhdk3afQZhZL9OTA7tn9KfHdDE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**2. OpenSSH 10.3修复关键安全漏洞**

OpenSSH发布10.3版本，修复了多个安全问题，其中最关键的是ProxyJump参数中的Shell注入漏洞。此前，如果用户输入的主机或用户名未经过验证，攻击者可能通过构造特殊参数实现命令注入，从而执行恶意指令。

该漏洞的危险性在于其“隐蔽性强”。许多自动化运维脚本或跳板机环境中，会直接调用SSH参数，一旦引用外部输入，极易被利用。此外，SSH作为基础设施级组件，其影响范围极广，涵盖服务器运维、DevOps及云环境。

此次更新不仅修复漏洞，还加强了整体安全机制，体现出基础组件“持续加固”的趋势。对于企业而言，应重点关注：一是及时升级关键组件；二是审计自动化脚本输入来源；三是限制不可信参数传递路径。该事件说明：**传统基础设施软件仍然是高价值攻击目标**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjrX7glNia1JbGs6Eo1W6UQJO2R0wBIDG6rc6t5S2erdicPhomMU8YTA4sR1A4bOehNib2AhMKsmMict5yr9DbfdSTtBtugjWpyumqA/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**3. Nginx-UI备份恢复漏洞PoC发布**

在4月2日披露的另一重要事件中，Nginx-UI存在备份恢复机制漏洞（CVE-2026-33026），并已公开PoC利用代码。攻击者可篡改备份文件，在恢复过程中注入恶意配置，从而实现系统控制。

该漏洞的核心问题在于“信任链断裂”，即系统默认信任备份数据的完整性，而未进行严格校验。这使得攻击者可以通过供应链或存储路径污染备份数据，在恢复阶段实现攻击。

这一类漏洞具有典型特征：

* 攻击发生在“恢复阶段”而非运行阶段
* 难以通过传统安全设备检测
* 常被用于持久化或权限提升

该事件表明：**备份系统本身正在成为新的攻击面**。企业需引入备份完整性校验、签名机制及隔离恢复环境，避免“带毒恢复”。

**4. CERT-UA仿冒网站投放远控木马**

攻击者搭建仿冒乌克兰国家计算机应急响应机构（CERT-UA）网站，诱导用户下载携带Go语言编写的远控木马（RAT）。该攻击利用“权威机构信任”进行社会工程欺骗，具有较强迷惑性。

攻击流程通常包括：

* 搭建高仿官网
* 通过邮件或社交渠道传播链接
* 诱导下载工具或补丁
* 实际植入后门程序

Go语言恶意软件近年来增长迅速，原因在于其跨平台能力强、编译后难以分析，增加了检测难度。

该事件本质属于“鱼叉式钓鱼+恶意软件投递”，但通过伪装国家机构显著提高成功率。反映出当前攻击趋势：**技术攻击与心理欺骗深度结合**。

**5. Akira仿冒勒索软件攻击南美地区**

一种仿冒知名Akira勒索软件的新变种在南美地区传播，主要针对Windows系统用户。该恶意软件在外观和行为上高度模仿原始Akira家族，以混淆防御和分析系统。

该攻击的关键点在于“仿冒策略”：

* 利用既有勒索品牌提高威慑力
* 规避基于特征的检测机制
* 降低开发成本

攻击链通常包括钓鱼邮件或漏洞利用作为入口，随后执行加密并索要赎金。尽管是“仿冒”，但其破坏能力与真实勒索软件相当。

这一事件说明：**勒索软件生态正在“品牌化+模块化”发展**，攻击门槛持续降低，更多中小攻击团体可参与其中。

**6. Qilin勒索软件禁用EDR技术**

Qilin勒索软件组织采用恶意DLL（msimg32.dll）实现对300多种EDR产品的关闭或绕过，显著提升攻击成功率。

该技术属于典型的“防御规避（Defense Evasion）”手段，通过加载伪装系统库文件，劫持执行流程，从而终止安全软件进程。相比传统攻击，该方法具有：

* 覆盖面广（多厂商EDR）
* 自动化程度高
* 隐蔽性强

这一能力意味着攻击者在进入系统后，几乎可以“关闭监控再行动”，极大削弱企业检测能力。

该事件反映出当前趋势：**攻击者已将“绕过防御”作为攻击链核心环节，而非附属能力**。

**7. NoVoice安卓Rootkit感染超230万设备**

名为NoVoice的安卓Rootkit被发现隐藏在50多个Google Play应用中，影响超过230万台设备。该恶意程序集成22种漏洞利用技术，具备提权、持久化及远程控制能力。

该攻击的关键特点包括：

* 利用正规应用分发渠道传播
* 多漏洞组合利用提升成功率
* 深度隐藏（Rootkit级别）

一旦感染，攻击者可完全控制设备，包括窃取数据、监听通信甚至远程操控。

该事件说明：**移动端已成为大规模攻击的重要阵地**，且应用商店不再绝对安全。企业需强化移动终端管理（MDM）与应用审计机制。

#

从以上网络安全事件可以看出，当前网络安全威胁呈现三大趋势：一是**漏洞利用持续武器化**，0-day与PoC快速转化为攻击手段；二是**攻击链更加完整化**，从初始入侵到防御绕过再到数据控制形成闭环；三是**攻击对象全面扩展**，从浏览器、服务器到移动设备均成为重点目标。同时，社会工程与技术攻击融合加深，AI与自动化进一步降低攻击门槛。整体来看，网络安全正进入“高频攻击、低门槛、强对抗”的新阶段，企业需构建持续检测与纵深防御能力。

END

**【以上内容****来源自：河南等级保护测评】**

![](https://mmbiz.qpic.cn/mmbiz_png/BWicoRISLtbMSrNYPzeZSs4X316kGV7UeeR4VInT56J0KCLD3HkiaRxjMLLV6rricOadHohJB1sOtPT02fETAxr4g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/0YKrGhCM6DbI5sicoDspb3HUwMHQe6dGezfswja0iaLicSyzCoK5KITRFqkPyKJibbhkNOlZ3VpQVxZJcfKQvwqNLg/640?wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

* [个人信息保护负责人信息报送系统填报说明（第一版）全文](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547656&idx=3&sn=f7801b06bc94502535fa36eb21d1e129&scene=21#wechat_redirect)

* [高度警惕：不明黑客组织攻击中国国防、能源、航空、医疗、网安等重点行业](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547257&idx=1&sn=d6e54c6135c5d7e78d0e985086824c4b&scene=21#wechat_redirect)

* [2025HVV【技战法】丨0Day漏洞专项篇](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547247&idx=3&sn=1441149c1af904009b997eb107e06de9&scene=21#wechat_redirect)

* [护网—2025｜严守视频会议“安全门”，谨防信息泄露“一瞬间”](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547222&idx=1&sn=7c675c635e6cfe10bfb3d73942f52fad&scene=21#wechat_redirect)

* [疑似国内护网红队攻击样本被捕获并深度分析](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547198&idx=2&sn=4495b434c8f51f3b951bcd517bbb73d7&scene=21#wechat_redirect)
* [蓝队快速识别隐藏恶意文件的 20个文件特征及查找方法总结](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547198&idx=1&sn=a4864a2f90042bfbbc6b29231fee7b16&scene=21#wechat_redirect)

---

* [【新！】CNNVD通报微软多个安全漏洞](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547154&idx=1&sn=ed18dc2a48d5baf054db84d47279fb1b&scene=21#wechat_redirect)
* [2025-07-11 HW情报分享](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547148&idx=1&sn=0ae664aa5bccf7415f3a82722f47d905&scene=21#wechat_redirect)
* [【HVV】护网—2025 | 网警公布适用《网络数据安全管理条例》典型案例](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547133&idx=1&sn=5eeb8ad5cb874ecbcb59397a92b4c74e&scene=21#wechat_redirect)

[微软紧急修复高危蠕虫级RCE漏洞，威胁全网Windows系统](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547132&idx=1&sn=cd484270f0cd9ed5dc17fdeafb2e76dd&scene=21#wechat_redirect)

* [【HVV】护网系列 威胁情报共享7.9](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547108&idx=1&sn=01f68c9cc76760e8e5e0615df3b54c6c&scene=21#wechat_redirect)
* [25HVVRT钓鱼样本，警惕！多家单位已中...](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547104&idx=1&sn=8e06fcde039b325eedcb2eac8ba04f95&scene=21#wechat_redirect)

* [【HVV】护网系列 威胁情报共享7.8](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547054&idx=1&sn=014e2f4baedfea584d880c612e51b884&scene=21#wechat_redirect)

* [【更！】25HVV热点攻击漏洞含0day，各单位自查...](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547053&idx=1&sn=ab425df27b630dfa1c1d59759bf1ad37&scene=21#wechat_redirect)

* [【HVV】护网系列 威胁情报共享7.7](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247547048&idx=1&sn=d943617032f197fb6cb70fff9f8eb3d2&scene=21#wechat_redirect)

* [25HVV最新0day更新，各单位自查...](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546998&idx=1&sn=c3077c2a50dfec80de8f9e21b507ae53&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOz7uoDdfDbDl1qVuwMTJbQYQFjQhVRBR6NbiapDnHRp4pVzLHHzWFzgj8bS4GkC1nuGvK0eWAVZibQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=1&sn=2f16da5665014b4c07bcbd53e3d1c03e&scene=21#wechat_redirect)

* [【HW】8个因护网被开除的网安人](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=1&sn=2f16da5665014b4c07bcbd53e3d1c03e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOz7uoDdfDbDl1qVuwMTJbQXibAIZicQePpVEs53MXqeagXWqAlNNfMSiaN9gGicyte40dxFZ4duWgYbQ/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=2&sn=e9578e62a475ac5c46b95ac81066d2a7&scene=21#wechat_redirect)

* [HW应急溯源：50个高级命令实战指南](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546898&idx=2&sn=e9578e62a475ac5c46b95ac81066d2a7&scene=21#wechat_redirect)

---

* [震惊全球！中国团队攻破RSA加密！RSA加密告急？](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546856&idx=1&sn=11b36f6fabde860e889e4ac2f4797bba&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOugegrykhydnkHibcSWjpibTBZoK6jjGxJiax1BcwwctpA5SBric9aPdQFXsxFnn4LQJWdkYwbtPN0gg/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/BWicoRISLtbOugegrykhydnkHibcSWjpibTic4iaibtMhQibwlciccAMCNhHb6iawZp8ToJ8XoA6jDtJM6qf3RU9GR3YBaA/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg2MDg0ODg1NQ==&mid=2247546815&idx=1&sn=99a4f3228f322ef92c93d23cee01f071&sce...