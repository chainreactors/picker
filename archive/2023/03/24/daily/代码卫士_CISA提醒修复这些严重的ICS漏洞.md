---
title: CISA提醒修复这些严重的ICS漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516017&idx=2&sn=09318646aeb89a81eeacb8a2b51f9939&chksm=ea948e1bdde3070d895e8c6cea2e67f1eb2a166309fb913b70ade0894f89d12b2f3aefb0b477&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-24
fetch_date: 2025-10-04T10:29:54.255736
---

# CISA提醒修复这些严重的ICS漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIcZUMcD9m7HQcNOXzRDqt6fIGbNFgvkJXuqgdzBbcsT0CkmG6QMA45Q/0?wx_fmt=jpeg)

# CISA提醒修复这些严重的ICS漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIsCcIguWqrfo4ZKoE3LZdk3Sth2557MU3ib4elNocyhNGBZvlblA7FDA/640?wx_fmt=png)

**周二，美国CISA发布八份ICS安全公告，提醒注意影响台达电子 (Delta Electronics) 公司和罗克韦尔自动化 (Rockewell Automation) 公司设备的严重漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTawvfLWEDEbz6tTcTPHPDIS1cw3lN1uhOlCibFTAIMfPkAJSwArquGqJUeJq1dicIWKw7CUnP4v7uw/640?wx_fmt=png)

台达电子公司的实时设备监控软件 InfraSuite Device Master 中存在13个漏洞，所有早于1.0.5的版本均受影响。CISA提到，“成功利用这些漏洞可导致未认证攻击者获得对文件和凭据的访问权限，提升权限并远程执行任意代码。”

其中最严重的漏洞是CVE-2023-1133（CVSS评分9.8），是因为InfraSuite Device Master 接收未认证的UDP数据包并反序列化内容引发的，可导致未认证远程攻击者执行任意代码。两个反序列化漏洞CVE-2023-1139（CVSS评分8.8）和CVE-2023-1145（CVSS评分7.8）可用于获得远程代码执行权限。

Piotra Bazydlo和另外一名匿名研究员发现并向CISA报告了这些漏洞。

另外一些漏洞和罗克韦尔自动化公司的ThinManager ThinServer有关，影响如下版本的瘦客户端和RDP服务器管理软件：

* 6.x – 10.x
* 11.0.0 – 11.0.5
* 11.1.0 – 11.1.5
* 11.2.0 – 11.2.6
* 12.0.0 – 12.0.4
* 12.1.0 – 12.1.5
* 13.0.0 – 13.0.1

其中最为严重的是两个路径遍历漏洞CVE-2023-28755（CVSS评分9.8）和CVE-2023-28756（CVSS评分7.5），可导致未认证远程攻击者向安装ThinServer.exe的目录中上传任意文件。更麻烦的是，攻击者可利用CVE-2023-28755通过木马版本覆写已存在的可执行文件，可能导致远程代码执行后果。CISA提到，“成功利用这些漏洞可导致攻击者在目标系统/设备上执行远程代码或者导致软件崩溃。”

建议用户更新至版本 11.0.6、11.1.6、11.2.7、12.0.5、12.1.6和13.0.2缓解潜在威胁。ThinManager ThinServer版本 6.x-10.x已不再受支持，因此用户应升级至受支持版本。建议将端口2031/TCP的远程访问权限限制到已知的瘦客户端和ThinManager 服务器，作为应变措施。六个月前，CISA提醒用户注意罗克韦尔自动化公司 ThinManager ThinServer 中的一个高危缓冲区溢出漏洞CVE-2022-38742（CVSS 8.1），它可导致任意远程代码执行后果。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[CISA紧急提醒：Adobe ColdFusion漏洞已遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515947&idx=3&sn=76c36938bf1b7401950fc62730020638&chksm=ea948e41dde30757c6826cbbaeba673c04d191b437bd8a20532e2a13614e94562772ade4c057&scene=21#wechat_redirect)

[CISA提醒注意与LastPass泄露事件有关的Plex漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515912&idx=2&sn=9a2496bb8c17bcf9ed8e477367f18001&chksm=ea948e62dde307749ef7616c97efc1c91e680e87bd654e1a1766fae70831f36318fa216354cf&scene=21#wechat_redirect)

[CISA必修列表未收录数十个已遭利用漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515885&idx=2&sn=26d62bc99cdd37f8365bae8a9b94dba5&chksm=ea948f87dde30691fa7f9887c40e755916adb1ef81c320c67bd9cf032e3495edbc2c16f71288&scene=21#wechat_redirect)

[CISA新增3个影响IT管理系统的漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=3&sn=e59b1a83fa85ee490560066b8b39f535&chksm=ea948fbcdde306aa8791fa944d0c5db86f2535cd2381fc0dcc7d846cf5ee4c1686e12f3696d8&scene=21#wechat_redirect)

[CISA 提醒称黑客正在利用 ZK Java 框架中的RCE漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515787&idx=2&sn=833c589738704d28969098a2ddf6b07c&chksm=ea948fe1dde306f765bcebafffd6d83e25e7e661b2d28f2736104a8b44fdda955a5cd746552d&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/cisa-alerts-on-critical-security.html

题图：Pexels License

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