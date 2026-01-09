---
title: 当AI学会“读屏”：天御助力金融应用守住安全防线
url: https://mp.weixin.qq.com/s/BeFm-XIDzI88BwPWc7XyDw
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:08.629080
---

# 当AI学会“读屏”：天御助力金融应用守住安全防线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/OJbMFMZkdekicZjEhznt3OFiaQ1DHHSKP7hziavazL2juokla6kaT0aJkQg4nX5ju2fMacD9scdrwPqFh6bDf8psw/0?wx_fmt=jpeg)

# 当AI学会“读屏”：天御助力金融应用守住安全防线

腾讯安全

![]()

在小说阅读器中沉浸阅读

系统级AI应用成为“隐形黑客”

伴随智能体技术的持续演进，手机与 AI 的深度融合已成为未来核心发展方向，而具备超高权限的系统级AI应用，其安全问题的重要性也日益凸显。技术测评显示，这类系统级AI应用可截取屏幕、模拟点击、读取短信验证码/图形验证码，甚至更复杂的操作——金融App的“最后防线”正在被颠覆。腾讯云天御团队检测发现，已有数十家银行App因系统级AI应用权限滥用触发风控警报。在这场AI便利与隐私安全的博弈中，金融行业该如何破局？

---

系统级AI应用的“超权限”威胁：

金融级应用的三重危机

1. 数据暴露：你的手机屏幕正在被“实时直播”

系统级AI应用通过高危权限（如READ\_FRAME\_BUFFER）可静默截取任何界面，包括：

• 银行交易界面（余额、转账记录）

• 密码输入键盘（即使开启防截屏标志FLAG\_SECURE，仍存在权限绕过的技术可能）

• 短信验证码/图形验证码（通过OCR识别截图中的文字）

技术实测显示，输入银行卡密码时，系统级AI应用仍能通过视图树获取控件坐标，模拟点击数字区域。

2. 操作越权：AI替你“按下”关键确认键

核心威胁在于INJECT\_EVENTS权限，使得系统级AI应用能够：

• 跨App完成“比价→领券”等流程，甚至拉起支付动作

• 绕过生物识别（通过虚拟摄像头注入预录视频）

• 高频操作触发银行风控，导致用户账号误封

3. 生态失衡：平台与AI的“攻防拉锯战”

• 行业“自防”现象：部分头部应用已主动屏蔽系统级AI应用操作功能

• 银行被迫“一刀切”：部分金融机构检测到系统级AI应用直接禁止登录，影响正常用户体验。

腾讯云天御设备安全解决方案

构筑AI应用时代的安全防线

面对系统级AI应用带来的全新安全挑战，腾讯云天御推出系统级AI应用设备安全方案，依托独家【腾讯图灵盾】技术，基于设备可信ID，综合多维度信息构建AI无感混合专家模型，为每台移动设备生成唯一可信标识。该标识可感知和应对篡改、伪装、批量操控等风险，为金融级应用提供全面防护。

1、天御设备安全核心架构：

四层智能防御体系

天御设备安全方案基于对系统级AI应用自动化操作的深入理解，与传统手机自动化（无障碍辅助功能）相比，系统级AI应用自动化采用了完全不同的技术路径：

![](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdekicZjEhznt3OFiaQ1DHHSKP74dAPhtib4wUkh20NwTrRrSeMbpSXylI5wInuK4BhZWn4oNniak17Az3A/640?wx_fmt=png&from=appmsg)

第一层：构建系统层深度探针

a). 监控虚拟屏幕创建、InputManager.injectInputEvent等底层系统调用

b). 通过内核级行为分析识别系统级AI应用的数字指纹（如特定进程特征、权限组合）

第二层：行为层进行AI对抗

c). 动态轨迹建模：真人操作带有随机抖动，AI操作呈机械路径（精度误差＜0.1mm）

d). 多模态事件校验：结合设备ID、账号、环境、行为和场景等20+参数判断操作真实性

第三层：数据层协议破解

e). 实时解密系统级AI应用通信流量，识别敏感字段（如screen\_capture:true）

f). 基于流量时空特征检测异常上传（如高频截图传输至特定域名）

第四层：权限动态熔断

g). 实时感知高危权限（如CAPTURE\_SECURE\_VIDEO\_OUTPUT）启用状态

2、方案优势

![](https://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkdekicZjEhznt3OFiaQ1DHHSKP73NZRJGeXZ26cWFm8ia0MJ5blFrGInBAhKwK3UYO2jz5KiaibFCtGum6nQ/640?wx_fmt=png&from=appmsg)

某国有大银行实测数据显示，接入后天御方案将AI攻击拦截率从19%提升至96%，误封率趋近于零。

随着系统级AI应用的普及，金融行业需要从被动防御转向主动应对。我们建议金融客户从设备层切入，精准识别系统级AI应用特征行为，建立三重防护：

a)、风险精准识别：监测虚拟屏幕、事件注入等系统级API调用，结合多维特征分析

b）、动态防护策略：实时更新识别规则，应对快速迭代的系统级AI应用威胁

c）、生态联合防御：联动多家互联网生态数据，形成全方位风险画像

同时，建议金融机构立即部署动态令牌、界面混淆等紧急措施，并建立AI操作许可清单，实现分级管控。通过设备可信度评估与持续监测，构建适应AI时代的智能风控体系。

当AI学会“替人操作”时，安全的意义已不仅是防御漏洞，更是守护人与技术之间的珍贵信任。腾讯云天御设备安全解决方案，致力于在享受AI技术带来便利的同时，为金融安全筑起一道坚固的“数字护城河”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkden5qImICHSWibmMCI4FicszTR8S7nlM2YCmuB5GWQtBfqLicRmcu06jzFXmIOgiaeUQheLIDaw8vfpBdw/0?wx_fmt=png)

腾讯安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OJbMFMZkden5qImICHSWibmMCI4FicszTR8S7nlM2YCmuB5GWQtBfqLicRmcu06jzFXmIOgiaeUQheLIDaw8vfpBdw/0?wx_fmt=png)

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