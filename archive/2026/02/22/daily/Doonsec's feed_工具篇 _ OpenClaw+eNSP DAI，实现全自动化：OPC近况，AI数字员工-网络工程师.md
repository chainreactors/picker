---
title: 工具篇 | OpenClaw+eNSP DAI，实现全自动化：OPC近况，AI数字员工-网络工程师
url: https://mp.weixin.qq.com/s/Mk4rRYorInJvPq55aDQs5Q
source: Doonsec's feed
date: 2026-02-22
fetch_date: 2026-02-23T04:15:49.153162
---

# 工具篇 | OpenClaw+eNSP DAI，实现全自动化：OPC近况，AI数字员工-网络工程师

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ib2FcnWGXY7E5nuJ3dkRsnnDD7TtncYeKUticuVK6LejzA5FYQ5Iicic1ZANLPCZms5xB1BFDZ01GWG3heFfvqHsQia194UV5DSzPEWrhYNiayXn8/0?wx_fmt=jpeg)

# OPC | OpenClaw+eNSP DAI，实现全自动化：AI数字员工-网络工程师

原创

零日安全实验室
零日安全实验室

零日安全实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBPh5py6zW2zOqBr3VkB8ibrwQlV2KcNwN1W7hicw0KICVDfP0ZyphWFWHyD1bSAtZWYyW1yrWjGUJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xAgqtlG6owMYpT02bUL7nBLuJeFkfQU6Zo9AA4AKRjYTUWEs9FiakC4UyVK1cfw6WREUrRJY45W1cA/640?wx_fmt=png&from=appmsg)

免责声明！

本公众号所分享内容仅用于网络安全技术讨论，切勿用于违法途径，`所有渗透都需获取授权，违者后果自行承担，与本号及作者无关，请谨记守法``。`

**目 录**

> 前言
>
> 效果演示
>
> 总结

前言

在这个“超级个体”（OPC）崛起的时代，我们常常思考一个问题：创业的终点究竟是规模庞大的组织，还是极致高效的创造与自由？

过去，我们以为增长必须依赖人力堆叠；而现在，代码和算法成为了新的杠杆。当发现一人公司不再是一个概念，政府也悄悄的已经开始颁布了相关的政策以及孵化器时，未来我们的核心竞争力在哪里？下面我们来看OPC第一道门：OpenClaw+eNSP DAI实现全自动化，首个AI数字员工-网络工程师。

效果演示

要达成的效果：

仅用一部手机，以聊天对话的形式完成华为eNSP模拟器上网络拓扑的配置。（无需输入任何命令）

视频：

详细说明：

1.eNSP DAI：

一款接入了AI大模型的网络自动化配置工具。（后续会融入H3C、锐捷、思科等硬件设备的网络自动化配置）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2FcnWGXY7HEfktIggtmWCmukBhiayL4xYFggeib6x75ZSiaJ92Osibw747zEjcDREvntcZY69srXUz79QTA7ZSjfm07Z2cCX52l8ZL4RpoOam8/640?wx_fmt=png&from=appmsg)

2.OpenClaw：

它不是第一个Al Agent，但却是少数真正开始接管系统操作的那一类：读文件、跑命令、改代码，甚至拥有完整系统权限等等。

3.eNSP Bridge：

eNSP Bridge是一个统一的桥接系统，通过Telegram和飞书Bot实现对eNSP DAI网络设备的远程控制和查询。

其采用三层架构设计：底层使用WebSocket服务器（监听18790端口），负责通过Telnet协议与eNSP DAI设备通信，提供设备管理、命令执行、Zero AI助手等API；中间层是eNSP Bridge Core共享核心模块，封装WebSocket客户端、统一API接口并提供事件驱动机制（连接管理、请求-响应模式、自动重连、心跳保活)；上层是openclaw适配器，分别为Telegram和飞书提供格式化输出和交互界面。

![](https://mmbiz.qpic.cn/mmbiz_png/ib2FcnWGXY7EQXCLBpG1TKAVOgF7h34IqauYAXTEyEIW6icZkOdTRVKHJdP3DNmwPl0EacvHl9mib4fWJ6Egar8g3djHIZBiadPOArGMlLNyjZw/640?wx_fmt=png&from=appmsg)

4.eNSP DAI命令集成：

整个系统通过适配器模式实现了90%的代码复用，支持12个命令（包括中英文别名），核心技术包括Telnet协议解析、WebSocket双向通信、异步命令执行实时数据订阅推送，以及完善的超时控制和错误恢复机制，构成了一个成熟的企业级网络设备远程自动化配置平台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ib2FcnWGXY7FYmzXYncsqT12GzD9FhDicSkwPGmXwsf4jAbqjBbh9SLy8OQibuNGRXvDBdahqrUzIXNmibN7mSXf3UlywqcQZnVPCLdqhOuwhZo/640?wx_fmt=png&from=appmsg)

**总结**

这是我OPC的起点，第一个AI数字员工。

但这只是开始，后面我将会打破壁垒，融合H3C、锐捷、思科等异构网络设备，实现AI数字员工全自动化配置；面对技术的快速变革，我们不能固守传统模式，我将孵化更多的AI数字员工，把创新置于定位。眼望五年之远，深思三年之策，笃行一两年之实。

`如需咨询了解OPC以及openclaw，自动化的备注“OPC咨询”+V`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBPh5py6zW2zOqBr3VkB8ibr1TXAB8VdYuHITHmf2ibmiaS3G24kSibiaNUdw9pY8dTzpUh8fhibs20wuCw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MicZ6Q9ZW0xBPh5py6zW2zOqBr3VkB8ibrb7O4ic2Hbs6vkpZ0PQFTpgv5JqCEaoMyvWoOzULjXecwq2JtIr7GrAQ/640?wx_fmt=png&from=appmsg)

没看够~？欢迎关注！

往期精彩推荐

[工具篇 | eNSP接入AI大模型，实现网络自动化配置，解放双手！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485871&idx=1&sn=0772ddcc173f66efa091f02ca6046ff8&scene=21#wechat_redirect)

[工具篇 | Windows11 26H1 增强版&游戏版！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485856&idx=1&sn=cf8a3e69d57dc53fba67b4db482480d8&scene=21#wechat_redirect)

[Web篇 | 密码重置漏洞挖掘指南：从原理到实战的完整路径](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485837&idx=1&sn=895b89abbf1aff17912bba8bc16afc07&scene=21#wechat_redirect)

[工具篇 | 精选MCP服务器列表，建议收藏！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485794&idx=1&sn=821a2fa8578147b21e519935cb45a43d&scene=21#wechat_redirect)

[工具篇 | 从0一文读懂MCP：精选MCP服务器，干货！建议收藏！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485782&idx=1&sn=5faf45e7fce9c948d7f4d9ceb68d904d&scene=21#wechat_redirect)

[工具篇 | Claude Code攻具：MCP服务接入、自定义命令！他山石可攻玉](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485746&idx=1&sn=6b00bb636e4c95b49f8d2d7e12d6f41f&scene=21#wechat_redirect)

[工具篇 | WPS Office Pro一键安装，免手动激活！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485731&idx=1&sn=8eb5d5ba370efe6cfe62ab8da08fa647&scene=21#wechat_redirect)

[如何评价公众号零日安全](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485718&idx=1&sn=007c908afbbb73c8fc6a88cfd6f5a8d5&scene=21#wechat_redirect)

[Web篇 | 手把手拆解：小程序/Web端加密鉴权绕过案例全复现](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485707&idx=1&sn=56666237fcc15697b46d744be43d6c48&scene=21#wechat_redirect)

[内网篇 | 魔改Mimikatz，成功抓取win11哈希&明文密码！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485643&idx=1&sn=2868544ed4f543dae978f6144aa73292&scene=21#wechat_redirect)

[工具篇 | 两大顶尖AI模型免费用！Gemini3和Claude Sonnet 4.5（Thinking）全开放！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485574&idx=1&sn=d9dd48023cd02cf0e7281bbbd457adb9&scene=21#wechat_redirect)

[工具篇 | Cursor全面封杀：wf，Claude code，Claude codex，qoder和Augment怎么选？](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485564&idx=1&sn=4c50c7465d3f16401fb820e08749c089&scene=21#wechat_redirect)

[工具篇 | Cursor最强限制接触，活动仅剩最后三天！三天！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485543&idx=1&sn=3749e282e96c179347ee7507eab9de8e&scene=21#wechat_redirect)

[直播预告 | 快来，有料！！！【今晚21:30】](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485525&idx=1&sn=59e11199ef485be7adec95eaa16df4ec&scene=21#wechat_redirect)

[来项目了，来项目了！！！ 🔴【需求】：某高校网络安全实训，需要初级渗透讲师一位，大专以上就行，下周一进场 项目周期预计一个月，到十月中旬 📍【base】：西安 💰【工资】：400-600/天（只上一早上）](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485513&idx=1&sn=325d11820155700b38009d24f9a6b446&scene=21#wechat_redirect)

[工具篇 | 终于找到满血版Cursor的正确打开方式！Claude-4-sonnet MAX直接拉满](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485511&idx=1&sn=c43aefbd4e053c12f156ea66c1fd51cb&scene=21#wechat_redirect)

[Web篇 | 从防御到绕过：剖析长亭雷池WAF防护机制与SQL注入绕过测试](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485463&idx=1&sn=fcff1fc7cec09f4a4904d2901369bed0&scene=21#wechat_redirect)

[逆向篇 | 把原神设为微信头像，别人点开30秒微信闪退：30秒微信闪退消息 “炸弹” 背后原理揭秘！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485359&idx=1&sn=a3dc73eebed17bd60b89a2e1d766b442&scene=21#wechat_redirect)

[工具篇 | 全网第一：实测有效，一招解锁cursor无限续杯无限次数，速看！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485269&idx=1&sn=67405503506412f43f378fade88cb98c&scene=21#wechat_redirect)

[工具篇 | 必看！！！一招打开微信开发者调式窗口：小程序逆向必备](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485211&idx=1&sn=74a280ce28bbbbbd747475d7cab8722b&scene=21#wechat_redirect)

[漏洞复现篇 | CraftCMS 任意命令执行漏洞，CVE-2025-32432](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485175&idx=1&sn=c1bd499d39af1bf38c006d5dfaabd0f1&scene=21#wechat_redirect)

[工具篇 | 超绝！漏洞盒子一键自动提交脚本，效率飞升秘籍](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485157&idx=1&sn=65599d4007c0db1a60a54ca2689c1fbe&scene=21#wechat_redirect)

[内网篇 |【干货】探秘高版本系统：密码抓取技术与方法解析，建议收藏！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485131&idx=1&sn=d7167f5bc26a5a0814f6338117181bcb&scene=21#wechat_redirect)

[面试篇 | 网安春招大厂面试题精选：看这一篇就够了，必看！！！（2）](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485023&idx=1&sn=a608bd16bd38eef31e0aff94b1247a7c&scene=21#wechat_redirect)

[工具篇 | 热点！AI赋能网安技术：一文解锁全新操作方式](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247485005&idx=1&sn=424cde7ac0c6726f6ccba9b48efe33ba&scene=21#wechat_redirect)

[面试篇 | 网安春招大厂面试题精选：看这一篇就够了，必看！！！（1）](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484973&idx=1&sn=1031ca1a9e1d3e4a932f6bdc08097a0d&scene=21#wechat_redirect)

[工具篇 | MuMu模拟器安装证书+burpsuite抓包，APP&小程序渗透必备！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484601&idx=1&sn=93a52940fb9cda679eb4bf39e136d369&scene=21#wechat_redirect)

[内网篇 | 巧妙使用CDN隐藏CobaltStrike特征，红队必备！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484564&idx=1&sn=77f57d3bbac771e588a78da0e62d3349&scene=21#wechat_redirect)

[Web篇 | Fastjson反序列化漏洞深度剖析：成因、挖掘思路与防范攻略（上）](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484531&idx=1&sn=7b7d08f7213874ca293011ef8cc98a7d&scene=21#wechat_redirect)

[内网篇 | 干货！一文秒懂Kerberos认证：全面剖析与实践指南](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484502&idx=1&sn=eaaddf2829d976f510d578bd585ee122&scene=21#wechat_redirect)

[内网篇 | CobaltStrike：深入探索本地信息收集技巧，干货！！！](https://mp.weixin.qq.com/s?__biz=Mzk3NTQwMDY1NA==&mid=2247484422&idx=1&sn=fac04db65...