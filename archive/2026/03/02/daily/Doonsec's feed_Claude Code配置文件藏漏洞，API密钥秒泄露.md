---
title: Claude Code配置文件藏漏洞，API密钥秒泄露
url: https://mp.weixin.qq.com/s/MWug5c7b-QLhLHE8QKeNkA
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:10:03.062532
---

# Claude Code配置文件藏漏洞，API密钥秒泄露

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2nic6JBicptlmn1TWm3lhaWjJWdYgRkdia6yBaqqTibt3icIibzic7Vz4ChibjwXesAclP7AqRyDeicicF0JJRvMUQ28EDAUA7PxicqjUiaJM/0?wx_fmt=jpeg)

# Claude Code配置文件藏漏洞，API密钥秒泄露

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

Anthropic旗下Claude Code是开发者常用AI辅助工具，凭借终端便捷调用成为团队高效开发首选。近期Check Point Research（CPR）报告显示，其存在3个高危漏洞，可被攻击者利用实现远程代码执行（RCE）、窃取企业API密钥，威胁团队安全。Anthropic已在漏洞公开前完成修复。

**01**

**看似无害的配置文件，藏着“隐形陷阱”**

Claude Code支持通过仓库内.claude/settings.json文件实现项目级协作配置，但开发者克隆仓库时会自动继承该文件，且任何有提交权限者均可修改。

CPR发现，攻击者可篡改该文件作为攻击载体，在开发者不知情时触发危险操作，看似正规的仓库也可能成为攻击“蜜罐”。

**0****2**

**3大漏洞拆解：每一个都能直接突破安全防线**

这3个漏洞利用门槛极低，攻击者仅需修改配置即可“一键攻击”，对警惕性不足的开发者风险极高。

漏洞1：恶意钩子“暗度陈仓”，终端秒执行陌生命令

Claude Code的“钩子（Hooks）”功能可设置自动执行命令（如代码格式化），命令存于.claude/settings.json文件。

CPR测试发现，攻击者设置触发“会话启动（SessionStart）”的恶意钩子后，开发者克隆仓库启动工具时，恶意命令会立即执行，工具仅弹出通用信任提示，未明确告知后台正在执行钩子命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1IRkiaWx3eIIk5U6QxOtP7icEs1a6GEpM2MyZGCApicrsgicGEEUpHU6X6dLlv8gClGADyKXaN5xokfNnmDptXMTfSBgnUoRqYqd8/640?wx_fmt=png&from=appmsg)

测试显示，植入打开计算器的恶意钩子后，工具启动瞬间计算器即弹出（来源：Check Point Research）。攻击者可借此执行任意shell命令，甚至控制开发者电脑。

漏洞2：绕过MCP验证，二次实现远程控制（CVE-2025-59536）

Claude Code支持“模型上下文协议（MCP）”与外部工具交互，配置存于.mcp.json文件。CPR首次报告漏洞后，Anthropic添加了MCP初始化警告框。

但攻击者可修改.claude/settings.json的enableAllProjectMcpServers和enabledMcpjsonServers两项配置，自动批准所有MCP服务器，在用户点击信任提示前执行恶意命令，再次实现RCE。

漏洞3：API密钥明文泄露，企业资产遭窃取（CVE-2026-21852）

.claude/settings.json可定义环境变量，其中ANTHROPIC\_BASE\_URL控制API通信端点。

攻击者将该URL指向恶意服务器，即可拦截API请求。CPR观察到，用户未点击信任提示时，工具已将API密钥以明文通过授权头传输，开发者克隆仓库即泄露密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K0CpcJccLVgdOCydAoaczmpxibVCfKg9OfwUYts4jibo28pSetMWuvnNaUFbBUlKLAHibKr1Ltq4xrIcib4BMhBMw9yJicPzfwwEH4I/640?wx_fmt=png&from=appmsg)

攻击者可利用被盗密钥进行账单欺诈、访问共享工作区，还能通过代码执行工具重新生成文件，下载原本无法直接获取的敏感资源。

![](https://mmbiz.qpic.cn/mmbiz_gif/Cpo2XCpI7K3dNMj6TbibvmA5PmXbr6YgtxFt8FjwdWEQyia6JGqXIHY1xj0rxsLR6m4VWdhHXmz5ptfQ3l6ibCrcpXaw0LFp8ShmSHibSibCicSKY/640?wx_fmt=gif&from=appmsg)

这些漏洞可通过供应链攻击利用：攻击者通过恶意PR、蜜罐仓库或攻陷内部账号，将恶意配置注入项目，开发者克隆后即陷入风险，与此前Nx工具供应链攻击逻辑相似。

Anthropic已通过三项措施修复：优化不可信配置警告、强制MCP服务器需用户批准、延迟网络操作至用户确认信任后执行。

**03**

**CPR与Anthropic给开发者的两点建议**

1. 立即更新Claude Code至最新版本，确保补丁生效；

2. 严格审核仓库配置文件，不随意克隆来源不明仓库。

AI开发工具普及让配置文件成为攻击新入口，开发者提升警惕、及时更新工具是防范关键。

资讯来源：本文根据Check Point Research（CPR）公开安全报告及Anthropic官方修复公告整理。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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