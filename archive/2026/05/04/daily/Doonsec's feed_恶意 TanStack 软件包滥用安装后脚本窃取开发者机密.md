---
title: 恶意 TanStack 软件包滥用安装后脚本窃取开发者机密
url: https://mp.weixin.qq.com/s/hcD-2Fvo0eP9vbIkHMKX3g
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:57:34.986756
---

# 恶意 TanStack 软件包滥用安装后脚本窃取开发者机密

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zdwoicOrrJb33bibWyUb7K9Gnk83nXXFGElwGOn2dPhQWu63iaQfWmIA17yxIbTZ9u8wl4WSz6z8Y1thcicujicDAXb3OFASGNhia0jcibDEPaDvC8/0?wx_fmt=jpeg)

# 恶意 TanStack 软件包滥用安装后脚本窃取开发者机密

原创

ZM
ZM

暗镜

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

一个名为“tanstack”的恶意 npm 包被发现正在部署一项隐蔽的数据泄露活动，该活动通过欺骗性的命名策略和隐藏的安装后脚本来针对开发人员。

该软件包模仿了著名的 TanStack 生态系统，被恶意利用来窃取安装后立即出现的敏感环境文件。

攻击者在 npm 上注册了无作用域的 tanstack 包名，利用了与合法的 @tanstack 组织（维护着 TanStack Query 和 TanStack Table 等广泛使用的库）的混淆。

通过将该软件包包装成“TanStack Player”SDK，并配以精美的文档和逼真的品牌宣传，威胁行为者为毫无戒心的开发者设置了一个极具说服力的陷阱。

## **攻击时间线和行为**

2026 年 4 月 29 日 17:08 至 17:35 UTC 期间，攻击者发布了四个快速更新：版本 2.0.4 至 2.0.7。每个版本都包含一个 postinstall hook，这是一个在安装过程中自动执行的脚本 `npm install`。

3 月份发布的 2.0.3 版本此前并未表现出任何恶意行为。安装后脚本的突然引入标志着攻击的开始。

一旦触发，该脚本会静默地从开发人

被盗数据被发送到 Svix 的 webhook 端点，这是一个合法的 webhook 即服务平台。通过可信提供商路由数据泄露，攻击者降低了被网络安全工具检测到的几率。

有效载荷包括：

* 环境文件内容。
* 系统元数据，例如 Node.js 版本、操作系统和架构。
* 软件包版本和时间戳。

有趣的是，该脚本将敏感数据伪装在“readme”和“agents”等误导性字段名称下，掩盖了泄露内容的真实性质。

快速的发布周期表明攻击者正在积极地实时测试和改进恶意软件：

* 2.0.4：初始文件定位 `.env` ，无退出机制。
* 2.0.5：暂时切换到无害文件（可能是为了测试数据泄露管道）。
* 2.0.6：最危险的版本，扫描所有 `.env.*` 变体，包括生产文件。
* 2.0.7：恢复目标定位，但增加了不寻常的自我依赖性。

这种模式表明，在软件包保持公开可用状态期间，会进行实时调试和优化。

## **哪些数据面临风险**

环境文件通常包含高度敏感的凭据，包括：

* AWS 访问密钥。
* GitHub 和 npm 令牌。
* 数据库连接字符串。
* Stripe、Twilio 和 OpenAI 等服务的 API 密钥。
* OAuth密钥和其他私有配置。

如果该 `.env.production` 文件存在，则生产级别的机密信息可能已经泄露。

开发人员应立即检查锁定文件中是否存在受影响的版本（2.0.4–2.0.7）  `node_modules`。如果发现，则假定系统已遭入侵，并轮换所有暴露的凭据。

主要应对措施：

* 撤销并重新生成 API 密钥和令牌。
* 查看云日志（例如 AWS CloudTrail）是否存在可疑活动。
* 审核 CI/CD 流水线，因为在自动化构建期间会执行安装后脚本。
* 监控 `api.svix.com` 安装前后一段时间内的出站流量。

虽然没有发现持久化机制，但数据窃取一旦执行便是永久性的。

此次事件凸显了开源生态系统中持续存在的风险，尤其是域名抢注攻击。一个简单的拼写错误，例如安装时输入了 `installation` `tanstack` 而不是 `installation`， `@tanstack/query`就可能导致所有凭证泄露。

为了降低风险：

* 安装前请验证软件包范围和发布者
* 使用锁文件完整性检查和依赖关系扫描工具
* 考虑使用安全的软件包管理器或能够阻止已知恶意软件的工具。

此次攻击事件凸显了攻击者能够多么迅速地利用热门生态系统中的信任漏洞，将例行安装命令变成悄无声息的数据泄露。

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