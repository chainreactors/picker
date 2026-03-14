---
title: OpenClaw安全使用手册：用户必须警惕的四大风险
url: https://mp.weixin.qq.com/s/vD-_5Nj6r_FRKlziPqSRiA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:04:37.000005
---

# OpenClaw安全使用手册：用户必须警惕的四大风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EqS9GE77r0PnIfswtqYB6iaDFcLLSbpDPv3r5LE6wnuj4eYbMOmeushKWPkcicWlzXUkTK2iclibMe5MenvmGAvra3XZobSGt0g7E5icibahgjrJw/0?wx_fmt=jpeg)

# OpenClaw安全使用手册：用户必须警惕的四大风险

长亭安全应急响应中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/EqS9GE77r0PwCrH1QvE2ZVJVJALUHcibwUmBPC86o2NmyZMdAPwfppyZYuqCWoDt9qWAPHicFA7sh4ibO829dfsdblhdz4QdftyicPNBZW2ib55I/640?wx_fmt=png&from=appmsg)

如果你最近关注AI技术，很可能听说过OpenClaw——这款开源的AI智能体工具在GitHub上已经获得了超过30万颗星标，增长速度甚至超越了Linux、React等传统技术标杆。但你可能不知道的是，这款强大的AI助手如果使用不当，可能会给你的电脑和数据带来严重的安全风险。

**一、OpenClaw：从“聊天机器人”到“数字助手”的飞跃**

OpenClaw与传统AI聊天机器人的最大区别在于：它真的能做事。普通AI只能回答问题，而OpenClaw可以：

* 执行系统命令，管理文件
* 操作浏览器，自动处理网页
* 通过微信、钉钉、Slack等通讯工具与人交流
* 定时检查邮件、监控服务器状态

简单来说，OpenClaw给你的AI装上了“双手”，让它从“建议者”变成了“执行者”。但正是这种能力，也让安全问题变得复杂起来。

**二、四大安全风险，你可能正在面对**

### 1. “钓鱼链接”也能黑掉你的AI

2026年初发现的CVE-2026-25253漏洞被称为“ClawJacked”，它有多可怕？攻击者只需要让你点击一个恶意链接，就能完全控制你的OpenClaw智能体。

攻击过程：

1. 你收到一个看似正常的链接，点击打开
2. 链接偷偷修改了你本地的OpenClaw配置
3. 你的AI助手开始连接到攻击者的服务器
4. 攻击者获得了你的所有权限，可以在你电脑上执行任意命令

影响范围：2026年1月29日前所有版本都受影响，许多用户长期处于未修复状态。

复现截图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0NpibJjnS1dDbI5hax4CNNGj43j6T43Ow2hNj95hUicRmrZiciaHnJJgz5EBxq02g5GCnPTSoRjpMUvTftRo96ibwibCvyMgHPawLGbA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0PpKbNKnZ1ibfF2iaZ0gOVnS4uDribtzF1cJlwL7Y6OWheY1dk1EmHp0ic3VhZ3I1POGhHpvYMWZAy4AY8hyTFIoS1gUxqHcoTgyrw/640?wx_fmt=png&from=appmsg)

### 2. “技能市场”里的“毒苹果”

OpenClaw有一个类似App Store的“技能市场”（ClawHub），用户可以下载各种功能扩展。但安全团队发现，超过12%的技能包含恶意代码。

攻击手法：

* 攻击者上传看似实用的技能，如“马斯克思维模式”、“市场洞察助手”
* 这些技能在安装时偷偷下载恶意软件
* 你的加密货币钱包、密码、浏览器记录可能被窃取
* 你的电脑甚至可能被变成攻击者的代理服务器

### 3. AI的“权限过大”问题

当你让OpenClaw帮你“清理邮箱”或“管理云服务器”时，需要给它相应的权限。问题来了：

* 权限继承：AI继承了你的所有权限
* 无差别执行：AI不会像人一样“犹豫”或“怀疑”
* 一旦被黑：攻击者可以访问你权限下的所有资源

### 4. “隐形指令”防不胜防

传统AI安全主要防范用户的直接输入，但OpenClaw面临更隐蔽的威胁：

间接提示词注入：

* 攻击者在网页、聊天消息、日志文件中隐藏恶意指令
* AI在正常工作中无意中读取这些指令
* AI的“性格”被永久改变，后续行为持续异常

**三、个人用户安全使用指南**

### 1. 环境隔离：别在主电脑上直接运行

核心原则：OpenClaw不应该在你的主力电脑上裸奔。

具体做法：

* 使用虚拟机：在VirtualBox或VMware中创建一个专用虚拟机
* 使用Docker：将OpenClaw运行在Docker容器中
* 专用设备：如果条件允许，使用一台独立的旧电脑

### 2. 网络防护：关好“门窗”

将OpenClaw的网络端口直接对外开放，这很危险。

安全设置：

```
# 错误做法：允许任何人连接gateway_url: "ws://0.0.0.0:18789"# 正确做法：只允许本地连接gateway_url: "ws://127.0.0.1:18789"
```

```

```

进阶防护：

* 使用SSH隧道进行远程访问
* 使用Tailscale或WireGuard建立加密网络
* 绝不将OpenClaw直接暴露在公网

### 3. 权限管理：给AI“最小权限”

不要把你的所有账号密码都交给AI。

安全准则：

* 专用账户：为OpenClaw创建专门的邮箱、云服务账户
* 最小权限：只授予完成任务所必需的最低权限
* 定期更换：定期更新API密钥和访问令牌
* 使用OpenClaw 2.26+：新版增加了凭证审计功能（`openclaw secrets audit`）

### 4. 技能安装：谨慎再谨慎

ClawHub上的技能良莠不齐，需要严格把关。

安装前检查清单：

1. 查看评分和评论：优先选择高评分、多用户的技能
2. 阅读代码：打开SKILL.md文件，检查是否有可疑命令
3. 警惕“一键安装”：特别是包含`curl | bash`或`wget | bash`的命令
4. 沙箱测试：先在隔离环境中测试新技能

### 5. 保持更新：及时打补丁

安全漏洞被发现后，开发团队会快速修复，但需要你主动更新。

更新策略：

* 关注OpenClaw的GitHub仓库
* 订阅安全公告邮件
* 定期运行`openclaw update`命令
* 重要安全更新应在24小时内应用

### 6. 日常监控：留意异常行为

你的AI助手突然“行为异常”可能是被攻击的信号。

危险信号：

* AI突然尝试连接陌生网站或IP地址
* 大量认证失败记录
* AI试图访问`.env`、`config.json`等敏感文件
* AI的功能突然改变（如从“文档总结”变成“浏览器控制”）

监控方法：

* 定期查看OpenClaw的日志文件
* 关注系统的网络连接情况
* 使用`openclaw status`检查运行状态

**四、企业用户注意事项**

如果你是企业的安全负责人，还需要考虑：

### 1. 建立内部技能库

不要允许员工随意从ClawHub下载技能。

企业级方案：

* 建立经过安全审核的内部技能仓库
* 所有技能必须经过代码审查
* 使用数字签名确保技能完整性

### 2. 制定使用策略

明确员工使用OpenClaw的规则。

政策要点：

* 禁止使用OpenClaw访问核心业务系统
* 禁止将公司敏感数据交给AI处理
* 所有OpenClaw实例必须由IT部门统一管理
* 定期进行安全审计

### 3. 部署安全护栏

在OpenClaw中设置强制性的安全规则。

护栏示例：

* 文件访问限制：只能访问特定目录
* 命令白名单：禁止执行`rm`、`curl`等高危命令
* 操作审批：发送外部邮件、修改配置等操作需要人工批准

**五、常见问题解答**

### Q：我在自己电脑上用，也需要这么麻烦吗？

A：需要。CVE-2026-25253漏洞证明，即使是在本地运行，恶意链接也能通过浏览器攻击你的OpenClaw。个人电脑上的数据（密码、文件、加密货币）同样有价值。

### Q：我只是用OpenClaw处理日常事务，风险大吗？

A：风险与使用方式相关。如果你只是让它总结文档、安排日程，风险较低。但如果涉及文件操作、网络访问、第三方服务连接，就需要严格的安全措施。

### Q：有没有“一键安全”的方案？

A：没有。安全需要持续的关注和适当的工作量。但遵循本文的建议，你可以用合理的投入获得足够的安全保障。

### Q：除了OpenClaw，其他AI智能体工具安全吗？

A：所有具备“执行能力”的AI工具都面临类似挑战。OpenClaw因为开源和流行，安全研究较多，问题暴露得也更充分。其他工具可能隐藏着未被发现的风险。

**六、总结：安全使用AI的三条黄金法则**

1. 隔离运行：不要让AI直接接触你的核心环境和数据
2. 最小权限：只给AI完成任务所必需的最低权限
3. 持续关注：保持更新、监控日志、留意异常

OpenClaw等智能体代表了AI技术的未来方向——从被动的“回答者”变为主动的“执行者”。这种转变带来了巨大的生产力提升，但也引入了新的安全挑战。

2026年的安全事件给我们敲响了警钟：强大的工具需要配以严谨的使用方法。通过采取适当的安全措施，我们既可以享受AI助手带来的便利，又可以有效控制风险。

记住：安全不是一次性的设置，而是一种习惯。花一点时间配置好安全措施，你就能长期安心地使用这款强大的AI工具。

### 附录：OpenClaw近期超危漏洞列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/EqS9GE77r0MAzEuwCygFSQSeiaKYib1icpDJDRolO9xNYGYBsp7MAoBnZ0cK8qzhJS7D9ibdnIRL5Pctxl836ID7odMHcEFrXvjbrarzyj9jAR4/640?wx_fmt=png&from=appmsg)

**长亭应急响应服务**

全力进行产品升级

及时将风险提示预案发送给客户

检测业务是否受到此次漏洞影响

请联系长亭应急服务团队

7\*24小时，守护您的安全

第一时间找到我们：

邮箱：support@chaitin.com

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

长亭安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/FOh11C4BDicRRVzLmQjSLiavxtAic7KOwrG3LmOSNQjmWlwYtZXgu57OV1t9yic9E4GkU2noIicAq1nGlNT0MRiaBCMg/0?wx_fmt=png)

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