---
title: GoDaddy 源代码被盗，遭多年持续攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515674&idx=3&sn=05b7c5d5d66547fe3eea1e4f74014282&chksm=ea948f70dde306663e145b649cac0f572cd90b81eef0cba19213e7bcea90a6b433c606a1f1e2&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-23
fetch_date: 2025-10-04T07:51:43.334240
---

# GoDaddy 源代码被盗，遭多年持续攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTApbSMdKg73M9onzoWPcTvlmpiaBQEsoyCRkKqwt8PntZj8WKO2JFEKoZBmF0vLb0Pzu2eibnAM8Yw/0?wx_fmt=jpeg)

# GoDaddy 源代码被盗，遭多年持续攻击

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**web托管巨头GoDaddy 披露称，不明攻击者窃取公司源代码并在多年来攻陷其 cPanel 共享托管环境后在服务器上安装恶意软件。**

GoDaddy 在2022年12月收到客户报告后发现了这起攻击。客户报告称该公司的多个站点被用于重定向到随机域名，而攻击者多年来对公司网络都具有访问权限。

GoDaddy 在一份美国证券交易委员会文件中提到，“从调查来看，我么认为这些事件是某威胁组织持续多年的攻击活动的一部分，该组织还在我们的系统上安装恶意软件并获得与GoDaddy 某些服务相关的代码。”

GoDaddy 指出，在2021年11月和2020年3月披露的攻击事件也和该这次持续多年的攻击活动之间存在关联。2021年11月的攻击事件中，攻击者通过受陷密码攻击GoDaddy 的WordPress托管环境，影响120万名Managed WordPress 客户。他们能够访问所有受影响客户邮件地址、WordPress Admin 密码、sFTP和数据库凭据以及活跃客户端子机的SSL私钥。2020年3月攻击事件后，GoDaddy向2.8万名客户称，一名攻击者在2019年10月利用web 托管账户凭据通过SSH连接到其托管账户。

GoDaddy 公司目前正在和全球外部网络安全取证专家和执法机构协作，调查这起事件的根因。

**其它托管公司也遭攻击**

GoDaddy 公司还发现，该威胁组织多年来还攻击其它托管公司，“我们有证明，而且执法机构已证实，这起事件是由一个专门针对向GoDaddy这样的托管服务的攻击组织发动的。从所收到的信息来看，他们的目标显然是通过恶意软件感染网站和服务器以发动钓鱼攻击、分发恶意软件以及执行其它恶意活动。”

GoDaddy 是最大的域名注册商之一，向全球超过2000万名客户提供托管服务。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[Reddit 的源代码和内部数据被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515523&idx=1&sn=eb73653f2d84d7d6a4a56964563ed577&chksm=ea948ce9dde305ff879e53a77e5dded451ffd8b2bb0109e094f5acf8a3cc88f01b47f7d24284&scene=21#wechat_redirect)

[俄罗斯版“谷歌”Yandex源代码遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515387&idx=3&sn=28fb6538b4b168c8a79d6bace6795343&chksm=ea948d91dde30487738e1f1b496baddad423bc371bc08e152dd0dc1ceba25187f0f0c81d9a38&scene=21#wechat_redirect)

[Dropbox公司的源代码和个人信息被盗](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514392&idx=3&sn=a29064daa69c5c07deee1d6964bd826d&chksm=ea948872dde30164363475e82c2a87cb63d2f0a59b3fbc20c39144d2c012042f76a42cc24102&scene=21#wechat_redirect)

[丰田承认外包开发误将源代码上传至GitHub公开库且已泄露五年](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514172&idx=2&sn=0fb1816d6e9903c2ce310381d6841a3f&chksm=ea948956dde30040ff072e904e012909ec0b339d074b71c629fb5e6f7749a9af196f5cda19fd&scene=21#wechat_redirect)

[Apache开源项目 Xalan-J 整数截断可导致任意代码执行](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513963&idx=4&sn=8f7f84190a33593bda1e3d6c86470af6&chksm=ea948601dde30f178f02bdcc42ac15f052526722f31417ec3cc51f2b92cde6a84be7894c8fe8&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/godaddy-hackers-stole-source-code-installed-malware-in-multi-year-breach/

题图：Pixabay License‍

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