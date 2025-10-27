---
title: 阿里云边缘安全加速(ESA)产品功能众测 - WAF功能挑战赛
url: https://mp.weixin.qq.com/s?__biz=MzIxMjEwNTc4NA==&mid=2652995540&idx=1&sn=5abc98cb9a564b3209fcfdae4b65951e&chksm=8c9ef083bbe979958c089533ed61e870413cb75d263c3920ce49146982d000aa1069cf2be353&scene=58&subscene=0#rd
source: 阿里安全响应中心
date: 2024-09-24
fetch_date: 2025-10-06T18:28:27.030956
---

# 阿里云边缘安全加速(ESA)产品功能众测 - WAF功能挑战赛

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tCS9QJPdcGc18WR0kr95xiczLkhvOfEnZniaWv9L8AcPziaqOMePrG22nWdYob6ibkK6EzrqOAFliaGabXPmysAHTcA/0?wx_fmt=jpeg)

# 阿里云边缘安全加速(ESA)产品功能众测 - WAF功能挑战赛

阿里安全响应中心

![](https://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc18WR0kr95xiczLkhvOfEnZNjicTAIAITMkC4tgo3cSGg7UYXA71cBnd9pyJ0CmLq9WTiaSFF8zuYOA/640?wx_fmt=png&from=appmsg)

###

**活动简介**

###

本次活动为阿里云新产品边缘安全加速（Edge Security Acceleration，ESA）下WAF功能挑战赛。ESA（产品官网）是新一代的边缘安全加速产品，是DCDN的一次全面升级，集加速、安全、计算为一体。

**WAF**

多引擎驱动，规则引擎、AI引擎等联合决策，最大程度降低误报与漏报。

支持34种解码方式以应对各类攻击变形。

AI引擎实现防护的智能自适应，自动化剔除不适配业务的规则，实现应用防护的“千站千面”。

**BOT管理**

覆盖网页、H5、原生APP、小程序等全场景的BOT防护，满足不同用户的防护需求。

丰富的威胁情报，包括超7000种客户端类型识别以及海量恶意IP信息。

AI加持，内置访问时序、操作轨迹、团伙跟踪、资源异常等多种模型算法，自动化对抗，降低使用门槛。

**DDos防护**

平均每天防护2500次云上DDoS攻击，丰富的攻防对抗经验。

全球13大清洗中心，20Tbps+防御带宽储备。

自研多年的AI防护引擎，分钟级自动下发和调整针对应用层攻击（CC攻击）的多维度组合防护策略，并通过自动回溯分析以快速缓解误伤。

**本次比赛仅测试WAF功能，提供靶场目标，无需自行开通相关产品功能。**

**活动时间**

报名时间：2024.9.12 - 2024.10.12

**比赛时间：2024.9.21 - 2024.10.12**

**限额人数**

不限制

**比赛靶场**

靶场地址：比赛正式开始时在此活动页面和活动群公布，****报名成功后见最下方活动细则处****

说明：测试前需要先到靶场首页简单注册获取专属token，每个靶场地址都需要通过get传入这个token

**比赛赛道**

#### **赛道一：XSS挑战赛**

挑战成功定义：需在 Chrome/Firefox 浏览器最新 Stable 版本下，绕过靶场防御在相关域名环境中成功执行alert/confirm/prompt 函数

注意：若调用URL在非目标域执行函数不在范围

挑战范围：get型、post型、交互类xss均算有效

#### **赛道二：SQL挑战**

挑战成功定义：绕过靶场读取到数据库中的flag内容

注意：仅引发报错，而没有获取到flag的情况，会判定无效

**挑战奖励**

1.每个有效的绕过报告，我们会给予1000元的奖励，同类手法以时间较早的提交者为准

2.最终排名按有效报告数量，Top 3还将获得精美礼品

3.本次活动设立**最高奖励池10万元**，超出后的报告不再提供现金奖励，仅积分奖励

**提交规则**

#### **报名和提交**

请登录ASRC网站，在任务页面报名成功后，在任务页面提交漏洞：

链接：https://security.alibaba.com/online/detail?id=176

报告请务必从此页面提交，若报告内容过多或POC无法方便提交，可通过语雀文档加密分享，并在漏洞详情处提供分享链接和密码

**报告要求**

报告需包含四要素，样例：

1.复现方式：包括但不仅限于工具、脚本

2.PoC：如xxxxx.com/uploadfile、xxxxx.com/injection?cmd=cat /etc/passwd

3.一两句话简单描述原理：如利用xxx方式绕过检测达成OS命令注入绕过、利用xxx方式绕过检测达成OS命令注入绕过

4.执行结果截图证明：（图）

**规则要求**

1.如同时有多个选手提交了重复的绕过手法，奖金以最先提交的选手为准

2.禁止修改靶场环境的代码/配置等信息，一旦发现取消全部绕过奖金

2.一种绕过适用多个靶场的情况，会被判定为同种绕过，如一种绕过通杀2个靶场，那么会按一个有效绕过判定

3.禁止入侵、DDOS、物理入侵靶场站点

4.禁止攻击选手和裁判（如蠕虫/钓鱼等）

5.不能私自公布报告及payload，需与ASRC沟通

6.本次挑战赛最终解释权归ASRC所有

欢迎加入比赛钉钉群，任何答疑可咨询管理员，或搜索钉钉群号：102895002822 加入。

![](https://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc18WR0kr95xiczLkhvOfEnZ4Q24c0yRp7txuY9P7VtSCiagkSQlEHHmHSlBEiasWbUBW9aaV3SIxZLQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

阿里安全响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

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