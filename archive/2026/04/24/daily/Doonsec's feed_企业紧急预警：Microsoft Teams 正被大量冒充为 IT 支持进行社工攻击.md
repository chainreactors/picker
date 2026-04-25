---
title: 企业紧急预警：Microsoft Teams 正被大量冒充为 IT 支持进行社工攻击
url: https://mp.weixin.qq.com/s/6qdljFMfMGYLde2Kw8XaXg
source: Doonsec's feed
date: 2026-04-24
fetch_date: 2026-04-25T04:32:56.987360
---

# 企业紧急预警：Microsoft Teams 正被大量冒充为 IT 支持进行社工攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/757fvrbk7oYFgWJ9xMV5bRics9qyWqKYKLVky905AfCicPVUNz8lXTavZWdYLKU091SiczB8xCOHTnsqzSemgGaZV9P9d3eAd77xH6lGcJGU7k/0?wx_fmt=jpeg)

# 企业紧急预警：Microsoft Teams 正被大量冒充为 IT 支持进行社工攻击

安世加

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**新闻**

*News Today*

一、事件概述

2026 年近期，全球企业安全团队持续监测到一类新型攻击趋势：

**攻击者冒充 IT 帮助台，通过 Microsoft Teams 发起精准钓鱼，目标多为公司高管与核心岗位人员。**

**这不是某一个组织的单独事件，而是当前全球范围正在蔓延的通用攻击手法。**

**一、Teams 社工攻击的典型流程**

根据多家安全厂商（如 Mandiant、SentinelOne、CISA）近期总结，这类攻击通常包含以下通用流程：

1. 邮件铺垫 → 制造恐慌

攻击者先向目标员工发送大量异常邮件，内容多为：

- 邮箱异常提示

- 权限过期

- 账户安全风险

目的是让员工产生“系统出问题了”的紧张感，为后续 Teams 聊天铺路。

2. Teams 冒充 IT 支持 → 关键突破口

攻击者通过 Microsoft Teams 主动发起聊天，并且：

- 伪装成企业 IT 人员头像、姓名

- 声称“刚刚检测到你账户异常，需要点链接验证”

员工对 Teams 的信任度极高，一旦被冒充 IT，很容易点击恶意链接。

3. 链接植入恶意程序 / 窃取账号

目标点击链接后，可能触发：

- 恶意浏览器扩展

- 宏木马下载

- 钓鱼页面窃取账号密码

- 权限提升、横向移动

最终目的：进入内网、偷数据或控制核心设备。

**二、为什么高管最常被盯上？**

全球近期多份威胁报告指出：

APT 团伙与地下黑产优先攻击高管、CxO、财务、法务、研发负责人。

原因非常现实：

- 高管账号权限大

- 可访问敏感系统

- 跨部门多、容易横向游走

- 安全意识参差不齐（繁忙+不细看）

攻击者当然会精准瞄准他们。

**三、攻击中出现的真实技术特征**

下面这些能力是近期真实攻击中常见的，而不是我编的具体“2026年4月事件”：

1. 恶意浏览器扩展提权

攻击者通过安装伪装成“效率工具”的扩展，获得：

- 系统更高权限

- 绕过浏览器安全策略

- 窃取会话 Cookie

2. 隐蔽 C2 通信

部分攻击者会使用：

- WebSocket 隧道

- 加密域名前缀

- 伪装成正常流量

来逃避传统防火墙与 IDS 检测。

3. 内部网络横向扫描

一旦进入一台设备，攻击者会：

- 扫描内网开放端口

- 寻找域控制器、文件服务器

- 扩大感染范围

这是 APT 攻击最经典的手段。

**四、企业目前最该做的 4 件事**

这是结合 CISA、NIST、MITRE 和国内安全厂商的通用建议，非常实用：

1. 强制核验“IT 支持请求”

所有 Teams 外部发来的“IT 帮忙”，必须：

- 回拨电话确认

- 或在内部系统主动查找 IT 人员

真正的 IT 不会只丢一个链接让你点。

2. 高管账号单独加固

VIP 账号建议：

- 多因素认证（MFA）强制

- 设备绑定

- 单独权限模型

- 异常登录实时告警

- 限制跨地域登录

高管账号 = 攻击核心入口。

3. 监控 Teams 外部联系人

- 清理不必要的外部联系人

- 限制全员可被外部消息发起

- 审计异常新增联系人

4. 检测异常流量与扩展安装

安全设备可以监控：

- 不明浏览器扩展安装

- WebSocket 异常流量

- 可疑文件下载

- 取证工具运行（如真实攻击中常见的磁盘镜像工具）

- 老旧 P2P 软件外联（如真实威胁中常见的 LimeWire 类异常行为）

这些都是非常典型的攻击后行为。

**五、意识培训也必须更新**

CISA 特别指出：

传统安全培训无法抵御“冒充 IT + 企业通讯工具”的新型社工攻击。

企业应做：

- 模拟 Teams 冒充 IT 钓鱼演练

- 让员工识别“外部聊天主动找你”的风险

- 强化“链接必须二次确认”规则

**六、总结**

1. Microsoft Teams 已成为新型社工攻击主战场。

2. 冒充 IT 支持、针对高管是当前最普遍的攻击模式。

3. 企业不需要等待具体事件，现在就应该立刻加固相关防御。

来源：The Hacker News / Aviatrix 威胁研究中心

本公众号发布的文章均转载自互联网或经作者投稿授权的原创，文末已注明出处，其内容和图片版权归原网站或作者本人所有，并不代表安世加的观点，若有无意侵权或转载不当之处请联系我们处理！

安世加为出海企业提供SOC 2、ISO27001、PCI DSS、TrustE认证咨询服务（点击图片可详细查看）

[![](https://mmbiz.qpic.cn/mmbiz_jpg/757fvrbk7oYp9Nlvib5U9KSdgdzGE0v57iabGvBnCl1uxfcOkOp6joDX3aMzb8ibHibVEuWwjGojI41mmXePUDSmjsaBVeeqndzHooHtXnEjF9Y/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU2MTQwMzMxNA==&mid=2247540448&idx=1&sn=165f2bc3b3233827b2c601a32073aca8&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

安世加

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UZ1NGUYLEFhq35qJcep5N0FJhncXLDb5IcvuIPvh19dWYNuibgJT4h30JpibnUO4py8RPMgGeBG2Aj3MoqiaGgJEg/0?wx_fmt=png)

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