---
title: 安全警报 | 紧急预警！黑客组织密集发布多款针对我国平台高危漏洞工具，涉及政务、游戏、民生等多个平台
url: https://mp.weixin.qq.com/s/jttkuPDAOV3-MC2XkOaY2w
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:54:44.935862
---

# 安全警报 | 紧急预警！黑客组织密集发布多款针对我国平台高危漏洞工具，涉及政务、游戏、民生等多个平台

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/m7SEcCOKaqZyIenFDoqwXZWdc5IDrR02E9U2nbicRxnwiakUDnE8ibLdRBhhTicvOOn7mHGrXp28mBleUcZg8F7a4nljfcN0kNe6HBict1fDJYKM/0?wx_fmt=jpeg)

# 安全警报 | 紧急预警！黑客组织密集发布多款针对我国平台高危漏洞工具，涉及政务、游戏、民生等多个平台

原创

懒虫零信噪
懒虫零信噪

懒虫零信噪

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一、事件概述

5月1日，懒虫零信噪威胁情报中心监测到，某黑客组织在暗网论坛及电报群组中密集发布多款针对中国境内平台的漏洞利用工具。这些工具涉及政务服务、游戏平台、民生应用、身份验证等多个领域，利用API接口缺陷、身份验证绕过、信息泄露等高危漏洞，可能导致用户姓名、身份证号、手机号、健康证信息、游戏账号等敏感数据被批量获取，甚至被用于精准诈骗、身份冒用、黑产交易等恶意行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqZwGdeIaiaia2ypFWmkyyQoE29pZibD3ickyQHJzbhibeE1Rgd9MRWbBKo0vWxDkKBskcwXfSL4622mTzX8ZgMCPdJMIJwXD6aWiaunI/640?wx_fmt=png&from=appmsg)

二、漏洞分类与风险详情

1.政务与民生平台

广东省政府服务平台：黑客利用“健康API”接口的访问控制失效漏洞，可通过姓名+身份证号查询注册手机号及身份确认信息，无需验证码、无速率限制，威胁广东地区数千万用户个人信息安全。

海南省健康证数字平台：利用“不安全的直接对象引用”漏洞，攻击者无需身份验证，仅通过修改URL中的证书ID，即可直接访问他人健康证信息，包括姓名、健康证号、体检单位、体检日期及有效期，甚至健康证头像（可解码为JPG图片）。

水驿蓝就业小程序：实名认证接口存在逻辑漏洞，攻击者可伪造身份载荷，绕过实名认证流程，获取服务器完整响应（含匹配状态、个人档案数据），仅需姓名+身份证号即可查询就业档案、联系方式等敏感信息。

2.游戏平台

7723游戏API平台：利用“弱身份验证/JWT滥用”漏洞，攻击者可通过硬编码的JWT Bearer令牌和设备ID，枚举有效身份组合，提取游戏账号关联信息，甚至绕过身份验证。

3DM游戏平台：实名认证接口存在“弱双因素身份验证/会话重用”漏洞，攻击者可通过捕获的会话Cookie和硬编码的用户ID，批量验证泄露的身份组合，绕过实名认证要求，测试身份数据集的有效性。

3.身份验证与信息查询

多平台身份验证绕过工具：针对阿里云、腾讯云、中国联通等多家服务商的身份验证API，利用AES-256-GCM等加密技术绕过验证，可批量验证身份组合，跨库比对政府数据库，寻找有效身份信息。

QQ号关联手机号查询工具：利用某私人查询服务（avsov.com）的内部数据库漏洞，通过QQ号即可查询关联手机号及身份信息，用于去匿名化QQ账号、关联社交账号与手机号，为社工攻击提供数据支持。

4.其他高危工具

短信轰炸/OTP洪水工具：针对某中国移动应用认证API，利用短信网关缺失速率限制的漏洞，可通过目标手机号发起无限短信/OTP代码洪水攻击，请求间隔可调整至0.3秒，无验证码、无冷却期，导致用户手机被垃圾短信淹没，甚至被用于恶意注册、撞库攻击。

三、风险预警：四大隐患需高度警惕

精准诈骗升级：攻击者可利用泄露的姓名、身份证号、手机号、健康证信息等，冒充“政务客服”“公检法”“体检机构”等实施定向诈骗，诱导受害者转账或泄露银行卡、验证码等敏感信息。

身份冒用与黑产交易：姓名、身份证号、手机号是个人身份的“核心三要素”，一旦泄露，可能被用于注册虚假账号、办理贷款、实施网络暴力等，对受害者的信用、名誉甚至人身安全造成长期威胁。

游戏账号盗用：游戏平台的身份验证漏洞可能导致用户游戏账号被批量枚举、盗用，甚至被用于非法交易、外挂作弊等，影响游戏生态安全。

信息“裸奔”与社工攻击：健康证头像、就业档案、QQ关联手机号等信息的泄露，可能被用于职场歧视、恶意举报、人肉搜索等，对受害者的隐私和安全构成严重威胁。

四、紧急应对建议

立即核查漏洞：请相关平台技术团队紧急排查上述漏洞，修复API接口权限控制、身份验证逻辑、速率限制等关键问题，关闭不必要的公开接口，加强数据加密与访问审计。

加强安全监测：部署WAF、IDS等安全设备，实时监测异常请求，及时发现并阻断恶意攻击行为。

用户通知与补救：若确认数据泄露，需第一时间通知受影响用户，提供密码重置、账号冻结等补救措施，并配合公安机关调查。

其他平台：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqaAiakibXOniayQz1IkAvD2R36ZSVVWyXDVEortmkjq0G524GkIyX4iaqdC5uUsRZC7yAPJKn8MMELCclbeMG8hzdjZ63IdpKvsyL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqZ51lO44uFupxVUpXmocSAU4eUqxJOnqETibh5oRPGic5DpbXUTsZ6rp6ibRy6YqeiaWiaWictEzRzowZUuicYa1BUNShz7FKLnlmLUlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqaEIdPQNjKiasahvfI9txr9BXD098jaw0fBkpxzLLqGD7FiaePRftrK9bsfu6Q6Wq3086KY1JjFxOy2bibedwPrQiaO6RTDpf0XDl0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m7SEcCOKaqbp8caHl0jrliaTnlHGDfkNR5XibMoL4WqpR9ss9UQOtficlwGqcJs7rL2c7Tvq4lcyF88jibNU2PqElNoHVDRicNfNGrhUiciaicaJn7M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/m7SEcCOKaqaYWzCEIQI4C1uDy8eWqLSO7ib29XLlUYc0axRpIsNRH8yF16pKasYvmEzg7nG2DsGiamRIiclT213KehcU0Ks7eWgg0jXbPEyesU/640?wx_fmt=png&from=appmsg)

免责声明：本文基于暗网监测信息整理，所涉攻击声明及数据细节均源自黑客单方面宣称，尚未获官方证实；内容仅作安全预警参考，不构成事实认定，请以权威通报为准。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

懒虫零信噪

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vMByMwrmicRJuiblD41h1JXI8fg8OIgE0Doz0GqFMeoGxmZI0q4XfxFmM3YM25Q3mrKy7Up92YOL1XpEI3S3xFgg/0?wx_fmt=png)

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