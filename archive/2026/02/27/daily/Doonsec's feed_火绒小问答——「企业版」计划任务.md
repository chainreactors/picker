---
title: 火绒小问答——「企业版」计划任务
url: https://mp.weixin.qq.com/s/Xh70Ih3mpXA-s33EIxoomQ
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:56:04.008256
---

# 火绒小问答——「企业版」计划任务

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/u1Oy5xQ01SrdgYL0YKn9fy231JK07TqVEWhFDgbeL4zMCMqHWspskXf9KCK5Kia6SYaQsto4suGn2kWSREqmCMB5icTfoK3qw99fpxWcuFVhU/0?wx_fmt=jpeg)

# 火绒小问答——「企业版」计划任务

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

**尊敬的用户，您好！**

为协助企业客户进一步降低运维工作量、规避终端安全隐患，提升终端安全管理的自动化与规范化水平，火绒终端安全管理系统内置「计划任务」功能。该功能支持管理员对指定终端或分组，创建定时或按条件触发的自动化任务，可实现终端安全运维的高效管控，助力企业构建更安全、可控的终端运行环境。

**一、**

**功能概述**

计划任务功能允许管理员对指定终端或分组，创建定时或按条件触发的自动化任务。这有助于减少运维工作量，避免因长时间不进行安全扫描而带来的安全隐患。企业版2.0支持的计划任务类型有九种。

![新企业版1.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoHXq4BRtWHbqgib63B15Oouw2rHHoMzdcYB6sicbbQIQpdpkCNPqXeic9WZQd8JGliachU5fGiaCaeUIRZtSfo0P0WN6XDAaYaZ4lQ/640?wx_fmt=png&from=appmsg)

**二、**

**支持的任务类型**

企业版2.0目前支持的计划任务有九种，分别是：

**1.快速查杀**

**2.全盘查杀**

**3.自定义查杀**

**4.漏洞修复**

**5.终端升级**

**6.发送通知
7.垃圾清理
8.关机**

**9.重启**

**三、**

**创建计划任务详细步骤**

创建计划任务时，界面顶端的步骤按钮不可切换，必须按引导顺序完成设置。

**1.******进入创建界面****：

o 登录控制中心，进入【终端管理】->【计划任务】。

o 点击【创建】按钮。

**2.******第一步：********选择执行对象****：

o 可以选择****按终端添加****或****按分组添加****。

o 不支持同时按照终端和分组两个维度下发任务。

o 点击【下一步】，查看执行对象列表，确认无误后再次点击【下一步】。

**3.******第二步：设置名称和备注****：

o 修改计划任务的名称。

o 设置该任务的备注信息，以便于后续管理。

o 点击【上一步】可以返回查看执行对象，点击【下一步】继续。

**4.******第三步：选择执行时间（任务频率）****：

**o******任务频率****：

可选****设置计划、单次任务、开机执行、登录执行****。

**设置计划**：任务将按照用户自定义的时间频率（按天、按周、按月）进行任务执行。

****单次任务****：任务将按照用户设定的时间执行一次。

****开机执行****：任务会在每次开机时自动执行。

****登录执行****：任务会在每次用户登录时自动执行。

o 选择【单次任务】，则该计划任务只会根据执行时间执行一次。

o 选择【按天计划】、【按周计划】、【按月计划】、【开机执行】、【登录执行】等执行任务频率，将会根据任务频率，结合具体执行计划任务的时间，多次执行计划任务。

o 设置好计划任务的【执行时间】后，点击【下一步】。

**5.******第四步：选择任务类型****：

o 从九种支持的任务类型中选择一种。

o 根据所选任务类型（如查杀类），可能还需要进行更详细的设置（如查杀速度、是否扫描网络驱动器等）。

o 设置完成后，点击【下一步】。

**6.******第五步：配置异常处理****：

o 可以根据需求设置计划任务执行过程中出现异常情况的处理方案。

o 此页面设置完成后，点击【完成】。

**7.******任务下发****：

o 点击【完成】后，控制中心将对计划任务选择的【执行对象】下发计划任务。

o 终端将根据计划任务具体的执行时间、频率、任务类型和异常处理设置去执行计划任务。

**四、**

**计划任务的管理**

**1.查看计划任务：**
o 在【计划任务】主界面可以查看所有已创建的任务列表，包括任务ID、名称、类型、频率、下次执行时间等。
o 在【终端详情】页的【计划任务】标签页中，可以查看该终端存在的计划任务信息。

**2.编辑计划任务：**
o 在计划任务列表中，点击任务右侧的【编辑】按钮。
o 在弹窗中，点击上方的步骤按钮可以随意切换查看该计划任务的各项配置。
o 在每个页面修改设置后，都可以点击【保存】按钮保存修改。

**（计划任务的名称在创建计划任务后无法二次更改）**

**3.禁止/启用计划任务：**
o 用户可以禁止执行在执行状态中的计划任务，点击【禁用】，确认后将禁用该计划任务。
o 禁用后，禁用按钮显示为【启用】，点击【启用】将会启用被禁用的计划任务。

**4.删除计划任务：**
o 选中需要删除的计划任务，点击上方导航栏或右侧的【删除】按钮。
o 支持单条删除及批量删除。
o 计划任务删除后终端后续将不再执行此任务。

**五、**

**查看执行情况**

**1.在事件日志中查看：**

在【事件日志】->【终端管理日志】->【计划任务日志】中，可以查看计划任务执行的具体情况。

**2.终端离线时的执行：**

终端同步任务后，即使后续不连接中心也会自动执行计划任务。等终端连接中心后，相关的日志会上传到中心。

**六、**

**重要特性与注意事项**

**1.“过期后立即执行”选项：**

如果设置了定时任务（如10点的病毒查杀），但终端10点没有开机，11点才开机。若勾选了“任务执行时间过期后立即执行”，则终端在11点开机后会立即执行该查杀任务。

**2.终端合并的影响：**

当进行终端合并时，保留终端的计划任务为“保留终端的计划任务+重复终端的计划任务”，但**执行对象为分组的计划任务不支持合并。**

**3.与任务管理的区别：**

【任务管理】记录的是中心对终端下发的任务记录，而计划任务的详细执行日志需要在【事件日志】中的计划任务日志位置查看。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz7xGucUYl8icJicHmKlL1nvMOD1VIU0cQXJ1e93CQZVRIzOibHApq61lNKn3nx1959LbVdTxPOlPH6Bw/640?wx_fmt=gif&from=appmsg)

尊敬的用户：

若您有其他产品使用问题，可通过以下方式联系我们~

****微信公众号******：**主界面---常见问题---人工客服

****火绒官方论坛：****https://bbs.huorong.cn/

****火绒官方服务热线：****400-998-3555（法定工作日8:30-20:30，法定节假日9:30-18:30）

HUORONG

火绒安全成立于2011年，是一家专注、纯粹的安全公司，致力于在终端安全领域为用户提供专业的产品和专注的服务，并持续对外赋能反病毒引擎等相关自主研发技术。多年来，火绒安全产品凭借“专业、干净、轻巧”的特点收获了广大用户的良好口碑。火绒企业版产品更是针对企业内外网脆弱的环节，拓展了企业对于终端管理的范围和方式，提升了产品的兼容性、易用性，最终实现更直观的将威胁可视化、让管理轻便化，充分达到保护企业信息安全的目的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz4K1e9ubHiaGLicyPrL2TGOQUVuzGfhiavltoNEsaCLCyJXChRib3yHaPTI00hV8oFkSsvwgunn2k0wSg/640?wx_fmt=other#imgIndex=11)

求点赞

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN05z6DXwgVYcdZ6RFjwxdDoeAEia9eYdgyJaAJ0LDBJmxTdm2JUhkc4tg/640?wx_fmt=gif&from=appmsg#imgIndex=12)

求分享

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0CbyZz9kNTCKcA0puOEWfAYZnT6v6rr3kdBWIFw4TlSh7AgzSdOfAng/640?wx_fmt=gif&from=appmsg#imgIndex=13)

求喜欢

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz4GYNjvnCrNwdcoKZrWuGN0gBxG1O1Y7YCFGicYGrDUpcBg7iaLgNpCsDzNKcHwHcBgKktMtTSs6ZSA/640?wx_fmt=gif&from=appmsg#imgIndex=14)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

火绒安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/0icdicRft8tz5V9C96RXn1xV11tycAnWHXCicgKqfOS3JOw7jrIJckWH6Hg0bnXibjicPZs1ET2KwtvsRs41ZhCxh2A/0?wx_fmt=png)

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