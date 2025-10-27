---
title: 通过配置不当的微软app劫持Bing 搜索结果，获得4万美元漏洞奖励
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516114&idx=1&sn=f5e9f50e1c37ba75e607261b2e912282&chksm=ea948eb8dde307ae2d64f8f3e3672eb57e1d5b5e92d34a87f2ce6162682818039452ffca1697&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-04-01
fetch_date: 2025-10-04T11:23:12.766142
---

# 通过配置不当的微软app劫持Bing 搜索结果，获得4万美元漏洞奖励

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnh6p52Jg61SNUlibRjNYHVGXdRcNqndkWTmKOBJywnC76GasnG8PibiaRw/0?wx_fmt=jpeg)

# 通过配置不当的微软app劫持Bing 搜索结果，获得4万美元漏洞奖励

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQKEJEnEM7hwRM8lW9loTgn0oaLnSCDic88Tjc6F1IJuevcBEibXoaV8EmNdicH6I1QGSRcGJmMnF26A/640?wx_fmt=png)

**一款配置不当的微软应用可使任何人登录并实时修改 Bing.com 搜索结果以及注入 XSS 攻击，攻陷 Office 365 用户的账号。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnicfGeEG8F1VicgsOZkqX4TjewybkfzGrmGhTTU6Lp6y0W6Ie8KbWdukA/640?wx_fmt=png)

Wiz公司的研究人员发现了该问题并将其描述为“BingBang”。该公司在2023年1月31日将问题告知微软，后者证实并在3月28日修复。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnb5Bq7ej2P7H8sQia5fQ45QEOd1aiasWKgYX6qgBNpMgic66zVh4XuGZ6w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnSuasLPmaFBO5o0J20bpAZ4B2o3PenOzssibN6g6WczCnYIxORM7StLw/640?wx_fmt=png)

**配置不当**

研究人员发现，在 Azure App Services 和 Azure Functions 中创建应用时，该应用可被配置不当，从而导致任何微软租户的用户如公开用户都能够登录到该应用。

这一配置设置被称为“支持账户类型”，可允许开发人员指定某个特定租户是否为多租户、个人账户或是多账号和个人账号的混合体，从而有权访问该应用。这一配置选项适用于合法场景，即开发人员必须在组织架构边界内使应用可用的情况。然而，如果开发人员错误地分配了不受约束的权限，则会导致验证和配置错误非常普遍。Wiz 公司扫描发现，约25%的多租户应用存在配置不当问题，从而导致无需正确的用户验证，即可获得无条件的访问权限。在一些案例中，配置不当的应用属于微软公司，说明管理人员很容易在Azure AD 配置时出错。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnb5Bq7ej2P7H8sQia5fQ45QEOd1aiasWKgYX6qgBNpMgic66zVh4XuGZ6w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnSuasLPmaFBO5o0J20bpAZ4B2o3PenOzssibN6g6WczCnYIxORM7StLw/640?wx_fmt=png)

**BingBang 和 XSS 攻击**

研究人员发现一个配置不当的名为 “Bing Trivia” 应用，可使任何人登录到该应用并访问其内容管理系统。不过，他们很快发现该应用直接连接到 Bing.com，从而使他们可以修改 Bing 搜索结果中显示的实时内容。

为了验证对 Bing.com 的完整控制，研究人员成功修改了 “best soundtracks” 搜索条目的搜索结果，在最顶部添加了任意结果。接着，研究员查看了自己能否将同样的 CMS 将 payload 注入 Bing 搜索结果，发现可在 Bing.com 上执行XSS攻击。之后，研究员将问题告知微软，并协助微软判断第二种攻击的准确影响。

XSS攻击测试显示，可攻陷在搜索结果中看到顶部添加结果的用户的 Office 365 令牌，从而能够访问搜索者的账户，如能够访问 Outlook 邮件、日历数据、Teams 消息、SharePoint 文档和 OneDrive 文件。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnb5Bq7ej2P7H8sQia5fQ45QEOd1aiasWKgYX6qgBNpMgic66zVh4XuGZ6w/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQKEJEnEM7hwRM8lW9loTgnSuasLPmaFBO5o0J20bpAZ4B2o3PenOzssibN6g6WczCnYIxORM7StLw/640?wx_fmt=png)

**微软修复**

微软认为该问题并不严重，该配置不当问题可导致外部人员获得读取权限，但仅影响少量应用并立即将该漏洞修复。另外，微软还表示已引入安全增强，阻止 Azure AD 配置不当问题再次发生。最值得注意的是，微软已停止向未在资源租户中注册的客户端发放访问令牌，将权限仅限为注册正确的客户端。

微软在安全公告中指出，“该功能已在超过99%的客户应用中被禁用。对于无需服务原则依靠客户端访问的多租户资源应用来说，我们在Global Admins的 Azure Service Health Security 安全公告和微软365信息中心提供了相关指令。”另外，微软还为多租户应用增加了安全检查，查看多租户 ID 是否匹配允许清单以及是否存在客户端注册（Service Principal）。

建议控制多租户应用的开发人员和管理员咨询微软获得正确的更新指南。Wiz 还发布了另外一份含有修复建议的更详细报告。该公司研究员为此获得4万美元的漏洞奖励。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTBzmfDJA6rWkgzD5KIKNibpR0szmPaeuu4BibnJiaQzxBpaRMwb8icKTeZVEuWREJwacZm3wElt7vOtQ/640?wx_fmt=jpeg)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[学生利用“提示符注入”方法，攻破ChatGPT版必应搜索](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515534&idx=2&sn=e816e0c34f1deae1b5278e39c974e4ff&chksm=ea948ce4dde305f27ad16099811f247a67e25343957dfde04cb07203fa48927237f458d883d4&scene=21#wechat_redirect)

[微软必应后台服务器泄露查询请求和位置等信息](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247495113&idx=1&sn=248d1efd45a70de8e0561727e9dba271&chksm=ea94dca3dde355b5ebe0e636c4916a5958269ae9cc8a731302d721c920027ac9efde1e3a5c39&scene=21#wechat_redirect)

[必应将默认加密搜索流量](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485941&idx=3&sn=80977286c0698f536e1464e02a179429&chksm=ea97389fdde0b18943905844f128fdd7d7288797e98b735711bed69e28dd41b8b521e965794e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/bing-search-results-hijacked-via-misconfigured-microsoft-app/

题图：Pixabay License

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