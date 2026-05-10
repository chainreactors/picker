---
title: 黑客利用谷歌广告窃取 GoDaddy ManageWP 登录信息
url: https://mp.weixin.qq.com/s/18nnVFyYSDgbWr3h9hzNcg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:36:12.203165
---

# 黑客利用谷歌广告窃取 GoDaddy ManageWP 登录信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zdwoicOrrJb3m4ndibNRPYsLBo5fiboicflwUFW4LuvwAxe5w0vqgAf2srQIsLypJc9QicDfTnSvh7dPm8FI0eLLVUvDzdcsQ9iaGiaoccKoPZAsFw/0?wx_fmt=jpeg)

# 黑客利用谷歌广告窃取 GoDaddy ManageWP 登录信息

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

黑客滥用 Google Ads，通过在合法的 ManageWP 搜索结果上方放置看起来很像的钓鱼广告，窃取 GoDaddy ManageWP 凭据，并通过中间人攻击 (AiTM) 设置实时代理受害者的登录信息。

攻击者购买了模仿 ManageWP 品牌的 Google 赞助广告，该广告出现在搜索结果的顶部，而合法域名则被挤到其下方。

当用户点击恶意广告时，他们会被重定向到一个克隆的 ManageWP 登录页面，该页面与真正的界面几乎无法区分，这增加了受害者在不怀疑的情况下输入凭据的可能性。

ManageWP 被代理商、开发人员和企业广泛使用，用于从单个控制面板管理数百个 WordPress 网站，因此每个被盗用的帐户都极其宝贵。

Guardio Labs 的研究人员发现了一起针对搜索“managewp”（GoDaddy 旗下的集中式 WordPress 管理平台）的用户的网络钓鱼活动。

## **黑客利用谷歌广告漏洞**

根据研究人员引用的 WordPress.org 统计数据，ManageWP Worker 插件已安装在超过 100 万个网站上，这扩大了成功的网络钓鱼活动的潜在影响范围。

与传统的钓鱼页面仅收集用户名和密码不同，此活动在受害者和合法的 ManageWP 服务之间使用实时 AiTM 代理。

当用户在虚假页面上提交凭据时，后端会立即将这些详细信息转发到真正的 ManageWP 登录端点，从而有效地代表受害者实时登录。

被盗凭证还会被转发到攻击者控制的 Telegram 频道，使操作员能够立即看到每个被入侵的会话。

为了绕过双因素身份验证，代理会显示一个伪造的 2FA 提示，该提示模仿合法的 ManageWP 质询。

受害者无意中输入一次性代码，就等于直接把代码交给了攻击者，攻击者会将代码注入到活动会话中，从而获得对 ManageWP 帐户的完全访问权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zdwoicOrrJb2C766nFbwOnjfG3ZLT2UcBmyOnn2zfFKHUzI0QWnaD2NZ4icEIT4KxUFNweDvSTsUnbJO1F7md7u8xhiblibDAl9v8nNOCFnjMdw/640?wx_fmt=png&from=appmsg)

此 AiTM 流程允许威胁行为者绕过多因素身份验证保护，并保持一个实时身份验证会话，他们可以利用该会话来控制连接的 WordPress 站点。

Guardio Labs 的研究人员渗透到攻击者的命令与控制基础设施中，并观察到一个由操作员驱动的面板，该面板带有下拉命令，用于控制每个网络钓鱼会话。

该界面使攻击者能够以交互方式逐步完成网络钓鱼流程，请求更多信息，并动态处理双因素身份验证挑战，而不是依赖全自动工具包。

该平台似乎是一个定制的私有框架，而不是一个通用的网络钓鱼服务工具包，这表明其运营更加先进且管理更加严格。

小组提供的代码资料包括一份俄语协议，其中作者声明不对非法使用承担责任，将该框架描述为“教育性的”，并明确禁止将其用于针对俄罗斯境内的目标，这种模式在东欧网络犯罪工具中很常见。

根据最新分析，研究人员已确认至少有 200 名受害者，但考虑到 ManageWP 在全球网站管理员中的流行程度，实际数字可能更高。

## **GoDaddy ManageWP 登录**

攻破一个 ManageWP 帐户即可让攻击者集中访问大量WordPress 站点，包括更改内容、部署恶意插件、窃取数据或进一步入侵托管环境。

由于此次攻击依托于谷歌的广告和搜索生态系统，许多用户可能会认为赞助结果值得信赖，从而提高了攻击活动的有效性。

这一事件也凸显了“恶意广告”这一更广泛的趋势，即威胁行为者利用付费搜索广告位大规模传播网络钓鱼和恶意软件。

ManageWP 和GoDaddy 用户应避免使用搜索引擎作为登录页面的快捷方式，而应将官方 URL 添加到书签并直接访问。

管理员应检查其 ManageWP 帐户日志，查看是否存在可疑登录，如果怀疑帐户已被盗用，则应轮换密码，并重置 API 密钥或访问令牌。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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