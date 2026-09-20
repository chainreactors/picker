---
title: Claude 打穿 OpenAI细节：一张 HEIC 图，撬开私有代码库
url: https://mp.weixin.qq.com/s/76CCR5J4dbpGB1Xv6ja9JA
source: Doonsec's feed
date: 2026-09-19
fetch_date: 2026-09-20T07:14:57.678634
---

# Claude 打穿 OpenAI细节：一张 HEIC 图，撬开私有代码库

# Claude 打穿 OpenAI细节：一张 HEIC 图，撬开私有代码库

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

安全圈这两天最炸的瓜：

Hacktron 团队拿 **Anthropic 的 Claude**，在 OpenAI 漏洞赏金计划里，把 OpenAI 内部代码库摸了一遍。全程不到 72 小时，OpenAI 最后发奖金 **6500 美元**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicJmP3yrmtR7iageybQco4Zg6SDMLqYu4qgMJtNSvNUyJZ6aicZsDRBBxzYcIVHSKFb1u0RpNVQ30nkfic5z3LrRTwk68tg1IcgXiaM/640?wx_fmt=jpeg)

### 一、起点：一张 HEIC 图片

###

7 月 23 日，研究员发现 OpenAI 社区论坛（Discourse）传 HEIC/HEIF 图时，FastImage 不认，转交 ImageMagick + libheif 解码。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKyiciaaiaCUqeXr7p7pWEwmQ1mqnosR4UxsJlPSvic688Sjuhu0N2NKJqkDiapodPic42eoBOhUQfZzGJdXj97vbW06Zawt6vibrftR0/640?wx_fmt=jpeg)

打穿细节

Claude Opus 4.8 一查 Docker 镜像：libheif 1.19.7 缺上游安全补丁，特制图片能触发**堆溢出**。

上游修了的提交没打 CVE，Debian 没 backport，漏洞顺着 `libheif → Debian → Discourse 镜像 → OpenAI 论坛` 一路进生产。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIQruFfyo5UDE0UwVQS03gMm3ibiaAIHzU7FnjsQbMZGUrkoaqKrTTGLzSVibG5iaI2Oic189pwic4qL5JSgBd68S9XTKt7bia1Ey7M34/640?wx_fmt=jpeg)

）

### 二、拐点：Opus 5 把利用链跑通

###

一开始利用代码只能在关 ASLR 的环境跑。

7 月 24 日晚 Anthropic 发 Opus 5，团队换模型：3 小时写出 ARM64 利用，再移植到 Discourse 的 x86-64 + jemalloc。

第二天，传图 = 在论坛服务器上执行代码。

**AI 不是自动黑客，是“漏洞利用开发加速器”**——人定方向，Claude 写壳、调内存、适配环境。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKvSMv6Mx3ZFjf6bBSaRYXuwjMg5QbTP73e7HrbuHkSA7fKjwYibY7WLlCY3iaD2dobrWqPUfRkYCib6qJW8cwicR6SEfU0qoCIEBo/640?wx_fmt=jpeg)

### 三、破防点：论坛 Token 能进 ChatGPT

###

进 Discourse 后拿到登录态。重点来了：

OpenAI 的 SSO 配错了——**社区论坛的认证令牌，能直接访问 ChatGPT / Codex**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicI2sFV6EBZUMdYXYNFBHFDH5S6C8KkGbpm9XA6OPC6YsbqsGyY2n5tPKoU6WPyibib4Yib0hpKgQ74Gwiagfu2Cib9NbrZhKmutjKTA/640?wx_fmt=jpeg)

有个员工把 Codex 连了公司 GitHub，研究者借这道跳板，向 OpenAI 私有 Monorepo 提了个无害 PR：「Hacktron AI Team PoC」。

### 四、收尾：14 小时修，6500 刀了事

###

* 25 日 05:00 拿 RCE
* 约 14 小时后 OpenAI 确认修复
* 收紧社区令牌、撤会话、修 SSO
* 6500 美元赏金**只认 OpenAI 侧问题**，Discourse 走 HackerOne 另算
* Discourse 后续加图片处理沙箱，要求重构建镜像
* ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKkItEQ3XeFricg8tJvrvfr8wJHRGibBO2Tzr1a1GXsm9KmDk0xEkNKwyY2Wick2ntIibufocKB8xs9Hlywiaic1NaaphR9KU2dKQe0M/640?wx_fmt=jpeg)

### 五、甲方该记的三句话

> ① 第三方论坛/工单系统，别和主业 SSO 互通
>
> ② Agent（Codex/ChatGPT）的 GitHub Token 按“最蠢实习生”授权
>
> ③ 没打 CVE 的上游补丁，才是真正的供应链地雷

OpenAI 都被“友商模型 + 一张图 + 错配 SSO”轻轻掀了门。

你家那个“论坛账号能跳生产库”的链路，今晚不查，明天谁用 Claude 来查？

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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