---
title: 微软OpenAI云遭滥用：攻击者绕过安全护栏 对外售卖违规内容生成服务
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513487&idx=1&sn=2bb2b3796dd10a13b4a3bf0ae256a199&chksm=ebfaf2afdc8d7bb93ac0a572afdf222ceb9510b5625e64a2d911f9180ad752d2c00975e60c91&scene=58&subscene=0#rd
source: 安全内参
date: 2025-01-15
fetch_date: 2025-10-06T20:10:52.558811
---

# 微软OpenAI云遭滥用：攻击者绕过安全护栏 对外售卖违规内容生成服务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s1OXaaC0qXyBKhBavW2JxSZbHGaBowhDpJMwgCHBtDRFxn3cPbkvHbXL5jWmDCPm5St7zicuCHCzw/0?wx_fmt=jpeg)

# 微软OpenAI云遭滥用：攻击者绕过安全护栏 对外售卖违规内容生成服务

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s1OXaaC0qXyBKhBavW2JxSVxJdF3mdJlOEe0KOJt9MKIweiaTWiaf55dFo9ZI6ZWXaK6DQM8tv7KEQ/640?wx_fmt=webp&from=appmsg)

**攻击者利用被盗的API密钥，访问微软Azure OpenAI服务中的设备和账号，绕过安全护栏生成了“数千张”违反内容限制的图片，并对外出售这些访问权限。**

前情回顾·**大模型安全动态**

* d[AI Agents越来越火，它可能存在一个严重安全隐患](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513463&idx=1&sn=b35ecbae92733cf9b66597ee744d842b&scene=21#wechat_redirect)
* [向ChatGPT植入恶意“长期记忆”，持续窃取用户输入数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512702&idx=1&sn=183b62e899019269d6a0f8da6b16f22b&scene=21#wechat_redirect)
* [OpenAI反复修补未果的ChatGPT数据泄露漏洞是什么？](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247510652&idx=1&sn=32aae66d172b998bebb5ec073df3c99c&scene=21#wechat_redirect)
* [破解大模型安全护栏，让ChatGPT回答限制级问题](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247509395&idx=1&sn=09a150e2bdf2dedeed15adf5c7def6d7&scene=21#wechat_redirect)

安全内参1月14日消息，微软正在向美国弗吉尼亚法院申请扣押软件，并关闭一组外国网络犯罪分子用于绕过生成式AI系统安全指南的互联网基础设施。

在提交给弗吉尼亚东区法院的文件中，微软起诉了10名个人，指控他们使用被盗凭证和定制软件入侵运行微软Azure OpenAI服务的计算机，生成“有害内容”。

在2024年12月19日提交的投诉中，微软指控该团伙违反了《计算机欺诈和滥用法》、《数字千年版权法》、《兰哈姆法》和《反勒索与受贿组织法》，且违反弗吉尼亚州法律，犯有侵害他人动产罪和侵权干扰罪。

**攻击者绕过安全护栏生成了大量违规内容**

微软称，被告使用被盗的API密钥访问微软Azure OpenAI服务中的设备和账号，随后生成“数千”张违反安全协议的图片。这些安全协议旨在防止滥用行为。微软表示，这种活动首次在2024年7月至8月间被发现，其中一些被盗的API密钥属于位于宾夕法尼亚州和新泽西州的美国公司。

根据微软的说法，被告使用了一种软件工具，可以深入了解微软和OpenAI的过滤系统，从而识别被标记为安全违规的特定短语，并反向工程设计绕过这些限制的语言。该软件还允许用户去除创作的媒体中的元数据，这些元数据用于数字水印和识别AI生成的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7s1OXaaC0qXyBKhBavW2JxSMMqcygEL1Tm6TzN1LR6b9aiaBOsCicSfcBg6vGEicWA0ibDIYYOKNpRhZg/640?wx_fmt=jpeg&from=appmsg)

*图：微软公布的被告使用工具的截图*

在描述这一行动的博客中，微软数字犯罪部门的助理总法律顾问Steven Masada写道，法院的命令和扣押行动“将使我们能够收集有关这些操作背后个人的重要证据，破解这些服务的货币化方式，并中断我们发现的额外技术基础设施。”

微软发言人向外媒CyberScoop证实，公司已获得一项临时限制令，允许扣押投诉中列出的域名。

发言人表示：“该域名的扣押使微软能够将该恶意域名上的通信重定向到我们的数字犯罪部门汇聚点，为调查团队的分析提供可能性。除了初步扣押，我们还得以更快地发现证据，以进一步推进调查，并在我们确认为被告所使用的部分‘基础设施’所在地点保留证据。”

微软使用OpenAI的DALL-E图像生成器，而OpenAI和微软的Azure OpenAI服务都实施了协议和防护措施，防止生成暴力、仇恨图片或真人面孔和公众人物的写实图像。无论是博客还是投诉均未提及生成的图片的具体内容。

**攻击者对外售卖服务访问权限**

微软尚未掌握这10名个人的身份，而是通过特定网站、被盗的Azure API密钥和参与该计划的GitHub工具对其进行识别。投诉称，至少有3人提供这些服务且居住在美国以外，而其他人似乎是终端用户。

这些个人被指控设立了一项“黑客即服务”计划，系统性地从拥有微软生成式AI系统访问权的客户处窃取API密钥，并通过互联网向感兴趣的各方出售这些访问权限。

微软和OpenAI提供的生成式AI系统处于一场关键战役的前沿：企业提供先进的文本和图像生成能力，而恶意行为者则试图加以利用。

网络犯罪分子、诈骗者和外国情报机构一直在寻求使用生成式AI工具来增强或辅助黑客活动，并生成虚假媒体以用于虚假信息宣传。

AI公司已经采取措施缓解其技术可能被滥用的担忧，包括实施多项技术防护措施并加入国际协议。然而，外部研究人员已发现多种方法可以绕过许多这些限制，包括简单的提示技术。

不过，有一些迹象表明，由美国商业公司实施的保护措施可能更有效地阻止外国行为者充分利用这些技术。

去年，美国国家情报总监办公室指出，俄罗斯、中国和伊朗等外国利用生成式AI工具制作虚假媒体，旨在影响2024年美国大选。据一名国家情报总监办公室高级官员透露，然而，这些国家在“克服许多AI工具内置的限制并保持隐身”方面面临挑战，从而部分削弱了这些宣传活动的效果。

**参考资料：cyberscoop.com**

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