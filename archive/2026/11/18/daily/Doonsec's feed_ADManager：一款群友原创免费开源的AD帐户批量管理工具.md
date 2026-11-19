---
title: ADManager：一款群友原创免费开源的AD帐户批量管理工具
url: https://mp.weixin.qq.com/s/zb8_j1QKDZvKt_V3856izg
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:44:14.774074
---

# ADManager：一款群友原创免费开源的AD帐户批量管理工具

# ADManager：一款群友原创免费开源的AD帐户批量管理工具

原创

群友：长沙金城武
群友：长沙金城武

释然IT杂谈

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文基于群友长沙金城武分享的 ADManager 便携版（v1.2.0）界面截图整理

ADManager 是一款面向 Windows Active Directory（AD 域）的批量账户管理工具，界面标题为"AD 域管理工具 v1.2.0"。它以绿色便携包形式分发，解压后双击 `ADManager.exe` 即可运行，无需安装、不写注册表；底层由 Python 3.14 + PySide6 + pywin32 打包，整个程序约 81MB。

工具主界面由 8 个标签页组成：**连接设置、用户管理、计算机管理、批量移动、分组管理、统计查询、工具、日志**。下面按界面顺序，逐一介绍每个模块能做什么。

01  连接设置：配置域控与全局参数

这是所有操作的前提，页面分三大块。

![ADManager 01-connect 界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhZKmr3MZZbopicWaqwvqibadkXwszr9bWia2KzEdQicTxXdmMMzG58zrPcrMg3zo78SSmicjzcNA9JASEGP6ZqzK49BdGic0OaH30micU/640?from=appmsg)

**域控连接：**

填写服务器（主机名或 URL）、域（如 example.com）、用户名（界面特别注明"不带域前缀"）、密码；认证方式默认 NTLM，并可勾选"使用 LDAPS(636)"启用加密连接。密码框旁有"显示密码"按钮，方便核对输入。

**默认 OU / 参数：**

集中设定 Base DN、用户 OU、计算机 OU、禁用 OU、默认新用户密码，以及"未登录阈值（天）"，默认值为 60。下方三个勾选项很关键：

+ **递归查询子 OU**：查询范围延伸到下级组织单元；

+ **演练模式（只记录日志，不真正执行写入）**：先空跑一遍，只把"打算做什么"写进日志，不改动域内任何数据；

+ **CN 即工号**：按姓名检索账号时匹配显示名，遇到重名可人工确认，避免误操作。

**允许登录主机：**

一个多行文本框，每行填写一个主机名，作为"限制用户可登录主机"的白名单。

页面底部是"测试连接""保存配置""从配置文件加载"三个按钮，右下角显示连接状态，最底部是进度条和"释放界面（任务卡住时）"按钮。

02  用户管理：批量建号、改名与解锁

用户管理页分三个功能区，是日常使用频率最高的模块之一。

![ADManager 02-user 界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhbU1vkVPRbLxvCkaSjRm8Cge0SlWxHh7fkibIeh6hcLlbHg0HVuOXT3APibaRKFylWjqzjoAJ2rpzNWicSnmnu2UupJwGm9Alr8Uo/640?from=appmsg)

**1. 批量创建用户**
按 `users.xlsx` 模板准备文件，列包括"工号 / 姓名 / 密码 / 备注"。选择文件后可执行"预览数据"确认内容，再点"创建用户"批量写入。

**2. 批量操作**
同样基于 users.xlsx（工号 / 姓名），提供"旧词 → 新词"的替换框，配合以下按钮：

+ **限制登录主机**：应用连接设置里配置的主机白名单；

+ **密码过期**：强制用户下次登录修改密码；

+ **禁用并移入禁用OU**：禁用账号的同时移动到配置的禁用组织单元；

+ **批量改名**：按旧词 / 新词规则批量修改；

+ **按姓名匹配工号并写回**：把匹配到的工号回写到表格。

**3. 用户解锁 / 重置密码**
在"姓名或工号"框输入目标（多个用空格或逗号分隔），在"新密码"框填写新密码（留空则使用配置中的默认密码），然后可选"解锁""重置密码""解锁并重置"三个操作。

所有操作结果都显示在下方表格，支持"导出 Excel"留档。

03  计算机管理：批量禁用、移动与登录时间查询

针对计算机对象的批量操作，基于 `computers.xlsx`（计算机名）模板。

![ADManager 03-computer 界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhZchv9EKZ0yumlm9ibYNH20NbqOicVyjjndjHuXykOwMicpeK83Wk2jicDbiaFWxzttgljF1aicrXt5ia2luicDD22YdsqDvI9Ot78sSTY/640?from=appmsg)

+ **计算机列表文件**：选择 Excel 文件并浏览载入；

+ **计算机 OU**：默认取连接设置中配置的计算机 OU；

+ **目标 OU**：移动目标，禁用时默认取禁用 OU。

提供三个操作按钮：**禁用并移入禁用OU、移动到目标OU、查询最后登录时间**。结果表格同样可"导出 Excel"。

04  批量移动：用户与计算机跨 OU 迁移

这个模块专门做组织单元（OU）之间的批量搬迁，分上下两部分。

![ADManager 04-move 界面](https://mmbiz.qpic.cn/mmbiz_jpg/FxDqdf0BMhZHs6GzUKicic1JLy7taods6LVEeNgrBZVjuKOPLrgaV0pFvrffRPWdBz14LsKmdVJTWDZtkVOfBdCqORq1qJ1omNWcvO5QdC0yc/640?from=appmsg)

+ 移动用户：基于 users.xlsx（工号 / 姓名），指定"来源 OU"和"目标 OU"，点击"移动用户"；

+ **移动计算机**：基于 computers.xlsx（计算机名），指定"来源 OU"和"目标 OU"，点击"移动计算机"。

两部分各自独立，结果统一在下方表格展示并可导出 Excel。

05  分组管理：批量增删组成员

用于批量维护 AD 组的成员，成员文件可带一个"类型"列来区分用户或计算机。

![ADManager 05-group 界面](https://mmbiz.qpic.cn/mmbiz_jpg/FxDqdf0BMhaRzVlxducp1h3IL320X6xkKIibiaQ2icGnYwE5ib5GmSRzbfddW6yeYRx57LTGWjayJibdGrrGCrIJIt8qOjeahnaUVCCibQTJomCic8/640?from=appmsg)

+ **分组 DN**：填写目标组的 distinguishedName，如 CN=组名,OU=Users,DC=example,DC=com；

+ **成员文件**：users.xlsx 或 computers.xlsx；

+ **用户 OU**：可指定用户所在组织单元。

提供"添加成员""移除成员""查看成员"三个按钮，结果表格支持导出 Excel。

06  统计查询：账号盘点与僵尸账号清理

这是做安全巡检、账号审计时最实用的模块。

![ADManager 06-query 界面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FxDqdf0BMhbmmiacibCKL2sA3ZWGUQib6RcJIMXBee87wqlxGIWeeglHZJm0DTdcLwicdosvXYOYgATx22tWEQ6IogbHLQ7CsSaOgStUgRVAiay8/640?from=appmsg)

**查询参数：**可指定"查询 OU"（默认为配置中的用户 / 计算机 OU）和"未登录阈值（天）"（默认 60）。

+ 查询用户列表 / 查询计算机列表：基础盘点；

+ 未登录用户 / 未登录计算机：按阈值筛出长期未登录的对象；

+ **禁用未登录用户 / 禁用未登录计算机**：把筛出的对象批量禁用；

+ 导出 BitLocker 恢复密钥：批量导出终端的 BitLocker 恢复密钥。

结果表格可导出 Excel，便于生成报表或留档。

07  工具：模板生成、差异比对与本机加域

这是功能最"杂"但也很见功力的一个模块，分两块。

![ADManager 07-tools 界面](https://mmbiz.qpic.cn/mmbiz_jpg/FxDqdf0BMhZpBvfibevvSB5V2rYyDGHQEBoIjacHVjZFAibKO7uaYLycYKZ1VkPYhwicZd7Zezb3AvTeoicBw0Qiaiaw3RibJLoY1HhcW0x9ULMWLE/640?from=appmsg)

**1. Excel 模板与核对**

· 一键"创建用户列表模板""创建计算机列表模板"，省去手工制表；

· 四个差异比对按钮：**表内有但域控无的用户、域控有但表内无的用户、表内有但域控无的计算机、域控有但表内无的计算机**；

· 通过"比对文件（user 或 计算机）"选择要核对的 Excel 文件。

**2. 本机加域工具**——面向批量把电脑加入域的场景：

· **站点**：每行一个，格式为"名称|IP|OU"，示例 总部|192.0.2.1|OU=Computers,DC=example,DC=com；

· 填写**域名、域管理员**（如 DOMAIN\admin）和**密码**，以及**新计算机名**（如 HQ02）；

· 勾选"完成后重启"可选执行后自动重启；提供"检测网络""执行加域"按钮，并有"站点状态"显示。

结果同样可导出 Excel。

08  日志：全程可追溯

最后一项是日志模块。

![ADManager 08-log 界面](https://mmbiz.qpic.cn/mmbiz_jpg/FxDqdf0BMha0PBcib6Q3EicgNSEahVt8YnyZicUGCymGD31HbKiayWaQaEqVyiaGjFIqCWITJGsGbfDD0ic6SPFzFVoKj62y6dgnXL0H6RRyibEzFU/640?from=appmsg)

· **级别过滤**：下拉框可按级别筛选（默认"全部"）；

· **清空 / 保存日志**：分别清除当前日志和导出保存。

日志内容示例：

12:04:27 [INFO] AD 域管理工具 v1.2.0 启动

12:04:27 [INFO] 配置已保存到 C:\Users\admin\Desktop\config.ini（未写入凭据：username/password/default\_password/join\_admin）

最后一条值得留意：**配置文件不会写入用户名、密码、默认密码、加域管理员密码等敏感凭据**，这是一个贴合企业安全要求的设计。

小结：功能上的三个特点

**1. 覆盖完整闭环**：从连接配置、批量建号 / 改名 / 解锁、跨 OU 移动、分组维护，到统计查询和日志，8 个模块串起了 AD 日常运维的主要流程。

**2. 以 Excel 为操作入口**：几乎每个批量功能都基于 users.xlsx / computers.xlsx 模板，并支持结果导出 Excel，符合网管用表格作业的习惯。

**3. 注重安全与可回退**：演练模式、LDAPS 加密、登录主机白名单、敏感凭据不落盘、操作全程记日志，这些设计让批量操作更可控。

使用建议：涉及域控的批量写入风险较高，正式操作前建议先在测试 OU 中开启"演练模式"空跑一遍，确认日志符合预期后再实际执行。

本文基于群友长沙金城武分享的 ADManager 便携版（v1.2.0）整理，功能描述以界面可见项为准。工具来源与安全性请自行核验，生产环境务必先在测试 OU 演练。

👇👇👇👇👇👇：https://github.com/a87150/AD-Domain

预览时标签不可点

阅读原文

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3heAguJrdPxL46gicFSARTgYJPz3TpN3INITJuS3sblUpVO0tTAX9pkc4ujQxP3KdnVgZHJQU1BJLFK4wiba2WRA/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过