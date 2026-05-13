---
title: 首次发现！AI生成零日漏洞利用工具并实施网络攻击
url: https://mp.weixin.qq.com/s/4OWzmOw1oH11TwmlEmq9jw
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:45:51.841549
---

# 首次发现！AI生成零日漏洞利用工具并实施网络攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wT9KAyOic0NA1AaiaPzYdvDSIJXflmBdicKicswJ8kEwq900tyrRTRHu6mxzuQYooESBjW0coCvq4Q4YDuiaxu5O5E5Qib2QvJ8xqVpywvYfk3BZg/0?wx_fmt=jpeg)

# 首次发现！AI生成零日漏洞利用工具并实施网络攻击

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7vQ0NWEgFIdmPL2ygumbOpekyQFwmric7uyCVVpVaatqHKnQicNeUwLI5gfLWCiaTBibOSsCe05sASlbw/640?wx_fmt=jpeg)

谷歌研究人员披露，首次发现攻击者疑似利用AI，生成了某款流行Web管理工具的零日漏洞利用程序，并实施网络攻击。

前情回顾·AI网络攻击能力动态

* [Anthropic新模型让传统网络防御失效，AI主导网络安全的时代正在降临！](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515780&idx=1&sn=bd0f5e0150a0f2ee41c12e2e737092ff&scene=21#wechat_redirect)
* [AI失控时刻：智能体协同入侵公司内部系统，窃取机密数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515686&idx=1&sn=d090cb4b27db75aa0f588e2e3b84c341&scene=21#wechat_redirect)
* [AI一周开发出高级恶意软件，网络犯罪一人产业链开始出现？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515492&idx=1&sn=b779fd0ab43d8ca40bb858477d1c45e9&scene=21#wechat_redirect)
* [奇点降临？OpenAI宣布新模型将达到高阶黑客水平](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515325&idx=1&sn=403f587ec800975a5ffdc6d3557225f1&scene=21#wechat_redirect)

安全内参5月12日消息，谷歌威胁情报小组（GTIG）的研究人员表示，一款针对流行开源Web管理工具的零日漏洞利用程序，很可能由AI生成。

该漏洞利用程序可用于绕过一款流行的Web开源系统管理工具中的双因素认证（2FA）保护，但该工具名称尚未公开。

尽管此次攻击在进入大规模利用阶段前就被成功阻止，但这一事件表明，威胁行为者正越来越依赖AI辅助开展漏洞发现与漏洞利用活动。

**首次发现攻击者利用**

**AI生成的零日漏洞利用实施攻击**

根据这段Python漏洞利用代码的结构与内容，谷歌高度确信，攻击者使用了AI模型来发现并武器化该漏洞。

谷歌威胁情报小组在今日发布的一份报告中表示：“例如，该脚本包含大量具有教学性质的文档字符串，其中甚至包括一个虚构的CVSS评分。此外，它采用了结构化、教科书式的Python编码风格，这种特征与大模型训练数据的风格高度一致。”

目前尚不清楚攻击者具体使用了哪一种大模型来执行恶意任务，但谷歌已排除Gemini参与其中的可能性。

另一个表明漏洞发现过程中使用了大模型工具的证据，在于该漏洞本身的性质。这是一个高层语义逻辑漏洞，而AI系统尤其擅长识别这类漏洞，相比之下，传统模糊测试或静态分析更常发现的是内存损坏或输入清理问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wT9KAyOic0NCEESnSxjRPFZibzEEgP4iaiawZpfFIEaibm5reCkCQwe9ibbA4ZGicv7BGXnKMLqCg4dKOUtBfE8A3q4YA8wN1uMVz6ym9zjqHYGDzE/640?wx_fmt=jpeg&from=appmsg)

图：漏洞发现工具对比

谷歌已将这一重大威胁通报给相关软件开发商，并及时采取措施阻止了此次攻击。

谷歌威胁情报小组研究人员表示：“这是我们首次发现威胁行为者使用我们认为由AI开发的零日漏洞利用程序。”

**全球APT组织大量使用AI**

**进行漏洞发现和利用开发**

除这一案例外，谷歌指出，包括APT27、APT45、UNC2814、UNC5673和UNC6201在内的朝鲜等国黑客组织，一直在利用AI模型进行漏洞发现和漏洞利用开发。这延续了谷歌在今年2月报告中观察到的趋势。

研究人员还发现，与俄罗斯有关联的行为者正在利用AI生成的诱饵代码，对CANFAIL和LONGSTREAM等恶意软件进行混淆。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NBCGNecvXe5gpicwY6VlO4AA2s7ga7cbAMTVWs8V1W0zVvoZ2KuGias46cyDuP1hYFSAbDQwlIhYTY8amPA2gSxk2I8dsBVp9NeI/640?wx_fmt=jpeg&from=appmsg)

图：CANFAIL中用于诱饵逻辑的代码注释

谷歌还重点提到了一项代号为“Overload”的俄罗斯行动。在该行动中，从事社会工程攻击的威胁行为者使用AI语音克隆技术，在虚假视频中冒充真实记者，以传播反乌克兰叙事。

谷歌的报告还提及ESET今年早些时候披露的安卓后门程序PromptSpy。该程序集成了GeminiAPI，可实现自主设备交互。

此外，谷歌还发现了一个名为“GeminiAutomationAgent”的自主智能体模块。该模块通过硬编码提示词，使恶意软件能够以自动化方式与设备进行交互。

研究人员表示，这些提示词的作用是为系统赋予一个无害的人设，从而绕过LLM的安全机制。其目标是计算用户界面边界的几何信息，而PromptSpy则可利用这些信息，以多种方式与设备进行交互。

此外，谷歌研究人员表示，该恶意软件还利用基于AI的功能，在设备上重放认证信息，无论是锁屏图案还是PIN码都包括在内。

谷歌警告称，威胁行为者如今正通过自动化账号创建、代理中继以及账号池基础设施等方式，工业化获取高级AI模型的访问权限。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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