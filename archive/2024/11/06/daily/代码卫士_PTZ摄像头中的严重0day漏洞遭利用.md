---
title: PTZ摄像头中的严重0day漏洞遭利用
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521392&idx=2&sn=75cd21ca2fe9a85ff4068e97cde7a6cc&chksm=ea94a51adde32c0c617d16fed416a8b1c92c13c260ef7ec42b84c5f4a43aefdd7102fba9a980&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-06
fetch_date: 2025-10-06T19:18:47.705119
---

# PTZ摄像头中的严重0day漏洞遭利用

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRcr7DLhfnx9TwWNonGoZ99GsGXj8WQMTOwFAMHoc9YL0axDxRFfJdBJ6bH5Ps5A7Vj8hIkUOOfibA/0?wx_fmt=jpeg)

# PTZ摄像头中的严重0day漏洞遭利用

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRcr7DLhfnx9TwWNonGoZ996RUkkD93CHViaau6cdO5OhY5jAXpSjjHSBMz3PgibsoBAM5fjGrPOqVA/640?wx_fmt=gif&from=appmsg)

**攻击者正在尝试利用 PTZOptics pan-tilt-zoom (PTZ) 实时流摄像头中的两个0day漏洞。这些摄像头用于工业、医疗、商业会议、政府和法庭等行业和组织机构。**

2024年4月，GreyNoise 的AI威胁检测工具 Sift 在蜜罐网络上检测到与任何已知威胁不批拍的异常活动后，发现了CVE-2024-8956和CVE-2024-8957。研究人员之后发现黑客利用该摄像头基于 CGI 的API 和内嵌的 “ntp\_client” 实现命令注入。

研究员工 Konstantin Lazarev 深入分析了这两个漏洞。CVE-2024-8956位于摄像头的 “lighthttpd” web 服务器中，可使越权攻击者在无需授权标头的情况下实施越权访问，可暴露用户名、MD5密码哈希和网络配置。

CVE-2024-8957因 “ntp\_client” 二进制处理的 “ntp.addr” 字段中的输入清理不充分引发，可使攻击者使用特殊构造的 payload 插入命令，实现远程代码执行后果。

Greynoise 提到，利用这两个漏洞可导致摄像头遭完全接管、遭机器人感染，跳转到在同一个网络上连接的其它设备或者破坏视频推送。该公司报道称，虽然蜜罐攻击后，最初的活动短暂停止，但6月份出现了使用 wget 下载用于反向 shell 访问的 shell 脚本情况。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMRcr7DLhfnx9TwWNonGoZ99G42kxHcFPYaPnSQM9DkhcSkxSicvsF279TJVibE1aRUictKzMKBfz9Qdg/640?wx_fmt=gif&from=appmsg)

**漏洞披露和修复**

发现CVE-2024-8956和CVE-2024-8957后，GreyNoise与 VulnCheck 向受影响厂商进行了负责任的披露。

受这两个漏洞影响的设备是基于 Hisilicon Hi3516A V600 SoC V60、V61和V63，它们运行的 VHD PTZ 摄像头固件版本早于6.3.40，包括来自 PTZOptics、Multicam Systems SAS 摄像头和 SMTAV Corporation 设备的多个型号。

虽然 PTZOptics 在9月17日发布了一份安全更新，但 PT20X-NDI-G2和PT12X-NDI-G2等机型因已达生命周期，因此并未收到固件更新。之后，GreyNoise 发现至少两款更新的机型 PT20X-SE-NDI-G3和PT30X-SE-NDI-G3并未收到补丁，但也受影响。

PTZOptics 在10月25日就通过 VulnCheck 获悉扩大后的影响范围，但截止目前仍未发布为这些机型发布修复方案。

GreyNoise表示，这些漏洞可能影响大量摄像头机型，“我们（强烈）认为，更大范围的设备受影响，可能说明实际的罪魁祸首在于制造商 (ValueHD/VHD Corporation) 使用的SDK中。”话虽如此，用户应与设备厂商确认这两个漏洞的修复方案是否已集成到最新可用的固件更新中。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[AVTECH IP摄像头漏洞已存在多年但未修复 被纳入僵尸网络](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520635&idx=2&sn=1e8f2bedf63ce8086bb68cd736dc6036&chksm=ea94a011dde32907b0700686cb2680a9972ca12693469e2d0e0325fb56e0bb9556a4fbb00726&scene=21#wechat_redirect)

[Abode 家庭安全包存在多个严重漏洞，可导致黑客劫持和禁用摄像头](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514319&idx=4&sn=bb1d931819cef01583083f9eddee4a6d&chksm=ea9489a5dde300b349e85d3bf53d19d161712a5ac99dc81cf9fa3b09e54426e9bedd529d9889&scene=21#wechat_redirect)

[多个Wyze 摄像头漏洞可导致攻击者接管设备并访问视频](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511227&idx=4&sn=6f352ab9a489722b06e9f7b65f2f1ebd&chksm=ea949dd1dde314c7f99397ef312b0074bbd05b5067a602260b54dfcdea9b0b7b511b7d4dc228&scene=21#wechat_redirect)

[很多IP摄像头厂商都在用的固件中存在多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506705&idx=2&sn=04f41c0b13dea970635fab6514fe7035&chksm=ea94ea7bdde3636deb52810ee03ff0888a677d764ef786b112313d13ebcfe1f9ba22129d1954&scene=21#wechat_redirect)

[突发：Verkada安全摄像头失陷，特斯拉Cloudflare等2万多客户受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502161&idx=2&sn=7ef532b3fd469b60e33df1504b2d7bf7&chksm=ea94f83bdde3712db27e04df9695598ce131442395f5af86a33a14c942566934515be3987686&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hackers-target-critical-zero-day-vulnerability-in-ptz-cameras/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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