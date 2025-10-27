---
title: 英伟达发布 GPU 驱动更新，修复25个漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514853&idx=2&sn=aa7edf1c528ee030b826738933440806&chksm=ea948b8fdde3029958ce600f79ba636a4b31e5e7bd11dbda3eca72604cd5ebe9f8c54899f257&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-12-02
fetch_date: 2025-10-04T00:18:06.301983
---

# 英伟达发布 GPU 驱动更新，修复25个漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIBvjzLaPe2hE7iaMvWzkLrUvh7iaXz7vJnbPLx0uuBAiaicoXEmjLdjXicWQ/0?wx_fmt=jpeg)

# 英伟达发布 GPU 驱动更新，修复25个漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMSXU3yX3JfkwE20YdSXMFEIrIkntER4Tr90Zhj3SLRHO8EwI0rmzhQiavicAGEMsVwk4Jy5d3nPiaf9g/640?wx_fmt=gif)

**英伟达发布 Windows 版本的 GPU 显示驱动安全更新，修复了25个漏洞，含7个高危漏洞，其中1个高危漏洞可导致攻击者实现代码执行和权限提升等。**

最严重的两个漏洞是：

* CVE-2022-34669（CVSS 8.8）：位于 Windows GPU 驱动中的可本地利用的用户模式下的漏洞，可导致无权限的普通用户访问或修改应用的关键文件，可能导致代码执行、权限提升、信息泄露、数据篡改和拒绝服务等。
* CVE-2022-34671（CVSS 8.5）：位于Windows GPU驱动中的可远程利用的用户模式下漏洞，可导致无权限的普通用户引发界外写，可能导致代码执行、权限提升、信息泄露、数据篡改和拒绝服务。

CVE-2022-34671的严重等级更低的原因在于其复杂度高但可利用性角度。CVE-2022-34669 对于已经具有Windows 设备访问权限且旨在提升权限或执行代码的黑客和恶意开发人员更有用。

鉴于英伟达产品的热门程度，查找易受攻击GPU 驱动的行为有较高概率发生。攻击者可利用这些漏洞获得更多权限并在网络上进一步传播。英伟达目前尚未发布更深入的技术详情，从而为用户修复漏洞留下更多时间。

英伟达在安全公告中提到了所有25个漏洞的修复方案以及本月更新中提到的所有软件和硬件产品。

建议用户下载最新可用GPU驱动版本，应用这些安全更新。英伟达同时也通过自身服务自动推送更新。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[继英伟达、三星后，育碧也遭攻击，员工密码重置](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510883&idx=2&sn=f393b8f5430d29951a2db1657466ad6e&chksm=ea949a09dde3131f788b175727969c896d47c896c8128815dd13a95456c373ed6008e033313f&scene=21#wechat_redirect)

[黑客泄露DLSS源代码，逼英伟达开源GPU驱动](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510769&idx=1&sn=33b36edc7756b13e979de35013a06c34&chksm=ea949b9bdde3128db9913820d0af32ba947169d140309d9a5414308a4214561bce3c4fdab159&scene=21#wechat_redirect)

[英伟达GPU打破了谷歌Chrome的隐身模式](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485815&idx=4&sn=ccf137adebfe5dcd197e6cfacdce5e2e&chksm=ea97381ddde0b10b2724962a591bbfa8c4bb4c074ff112188fda6ed79e9b19dc1c67c51f1a4f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/nvidia-releases-gpu-driver-update-to-fix-29-security-flaws/

题图：Pexels License‍

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