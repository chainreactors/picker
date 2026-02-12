---
title: 开源库 Libpng 漏洞已存在30年，可导致数百万系统遭代码执行攻击
url: https://mp.weixin.qq.com/s/uyH8XoiOHygvgC_mH4vESw
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:19:45.105197
---

# 开源库 Libpng 漏洞已存在30年，可导致数百万系统遭代码执行攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfXCB7HsoJJPKR470LZdhib5mF1g89GM48U7ReL62ohUK7h4n4EG88iajriazcdahfaOHQDujEn0QAsNAKibHlR2VKQ3p0JaKfp6Iuc/0?wx_fmt=jpeg)

# 开源库 Libpng 漏洞已存在30年，可导致数百万系统遭代码执行攻击

Guru Baran
Guru Baran

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**几乎所有操作系统和网络浏览器都在使用的官方****PNG****参考库****libpng****库中存在一个严重漏洞****CVE-2026-25646****，且该漏洞已存在****30****年之久。**

该漏洞是位于png\_set\_quantize() 函数中的堆缓冲区溢出问题，可导致应用程序崩溃或使攻击者执行任意代码。该漏洞自从函数png\_set\_quantize() （此前被命名为 png\_set\_dither()）诞生之日起就已存在，影响该库之前的所有版本。维护人员已发布 libpng 1.6.55 修复该漏洞，并建议直接升级。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUdrtFzY2LPsPplPxg8F0VZfdE8VxFic8xeDNWEa8ZhEbTswpOKFU8wFO1BhCnfMTjp8xogrkJgInicdibwBquYoXSkHks98SW3eE/640?wx_fmt=gif&from=appmsg)

**已存在30年之久的“遗留” Libpng 漏洞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfV2lTeaibJ0UUbnR5ATFY4QH8wJeLdM366d6R2fh0G2SGRXic8mb8cK4gjQmGvUXj0sAEUMOicicMS3C76nj9icoVrqsMVYibH1S9zNM/640?wx_fmt=gif&from=appmsg)

该函数是一个底层API接口，用于减少图像颜色数量（色彩量化）以匹配显示设备性能。由于一处特定的逻辑错误，攻击者可诱导该函数陷入无限循环，最终读取超出内部堆分配缓冲区末端的数据。

虽然该漏洞的触发条件严格，但在PNG规范下完全有效：

* 图像必须包含PLTE（调色板）数据块，但不能包含hIST（直方图）数据块。
* 应用程序必须请求进行色彩量化处理。
* 调色板中的颜色数量需超过用户显示设备最大支持颜色数的两倍。

该漏洞源于“最近邻颜色”量化算法在处理颜色索引时存在的细微匹配错误。为优化调色板缩减过程，png\_set\_quantize()函数采用“色彩距离”度量标准（RGB通道绝对差值之和）对相似颜色进行分组。它会构建一个哈希表——本质上是一个由链表组成的数组，将这些距离映射到调色板中的颜色对。

该漏洞的核心在于该哈希表的填充方式与访问方式之间存在冲突：

* 填充阶段：构建哈希表时，代码存储的是中间调色板中颜色的当前索引值。
* 剪枝阶段：在调色板缩减循环中，代码遍历该表以寻找可删除的颜色。然而，循环逻辑错误地假设表中存储的是原始调色板索引。它尝试通过index\_to\_palette查找表将这些存储的索引转换为当前位置，以验证颜色是否仍然存在。

由于代码将“当前”索引误解为“原始”索引，导致有效性检查全部失败。算法因此无法识别可删除的颜色，造成循环无限持续。变量max\_d（最大搜索距离）在尝试寻找更多候选颜色时会不断递增，最终超过哈希表的固定大小（769个指针），迫使程序读取到远超出已分配缓冲区的内存区域。在最可能发生的场景下，该漏洞会导致确定性崩溃（拒绝服务），因为应用程序会尝试读取未映射的内存。然而安全公告警告称，其影响可能更为严重。

修复方案涉及修改哈希表的填充逻辑，使其存储原始颜色索引，从而确保与函数其余部分的逻辑保持一致。该补丁已包含在libpng 1.6.55版本中。由于libpng的应用广泛，因此是漏洞利用开发的高价值目标，强烈建议开发者和用户立即升级至1.6.55版本。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Libpng修复已存在20多年的漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485606&idx=2&sn=9812ad153a7ffa76b1d7489fd20bcd91&scene=21#wechat_redirect)

[Fortinet 修复可导致未认证代码执行的严重 SQLi 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247525085&idx=1&sn=446f5400a46600a37f24df299ba852d2&scene=21#wechat_redirect)

[Anthropic MCP Git 服务器漏洞可用于访问文件和执行代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524939&idx=2&sn=a0b5639d3c077f9d7f283ee4872d5c0d&scene=21#wechat_redirect)

[n8n严重漏洞可导致任意代码执行](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524734&idx=1&sn=7accfa41ad8e25a3c0a292eb451552af&scene=21#wechat_redirect)

[Ivanti提醒注意 EPM 中严重的代码执行漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524630&idx=1&sn=f3a9316989486371722d9656c43f333e&scene=21#wechat_redirect)

**原文链接**

https://cybersecuritynews.com/libpng-vulnerability-exposes-millions-apps/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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