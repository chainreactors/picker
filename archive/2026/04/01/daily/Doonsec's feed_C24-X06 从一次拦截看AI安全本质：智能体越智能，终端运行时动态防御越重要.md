---
title: C24-X06 从一次拦截看AI安全本质：智能体越智能，终端运行时动态防御越重要
url: https://mp.weixin.qq.com/s/9zwJHQ2QbW25N9O5OVDhjw
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:55.184399
---

# C24-X06 从一次拦截看AI安全本质：智能体越智能，终端运行时动态防御越重要

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/j1hpA7GJeRCYPDq0GW9GSLBwvrgw5reXUSiaY7BTBPyDqW6BP5kBgtayiacLxibHYIPWAgltMYI3rxckcdJL1J3wdlDjzOQAYbp9kDLk5dwTwk/0?wx_fmt=jpeg)

# C24-X06 从一次拦截看AI安全本质：智能体越智能，终端运行时动态防御越重要

启明星辰集团

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j1hpA7GJeRA7rPC6xzLxicmyVPXZAldgy6YRpibdyibDYGfkMdMaTwPjQSxP94UX8nzbvIx0jXIHQtFHZPuQ0e2BXJGjZLg1dxkuvP7bIGDibt4/640?wx_fmt=gif&from=appmsg)

**为智能时代立信，为创新价值护航。**

**—— 启明星辰**

随着AI工具在办公场景中的普及，越来越多的员工开始借助智能体提升工作效率：从文案润色到PPT生成，工作方式正被重塑。与此同时，一类新型安全风险也在悄然浮现。

一次看似平常的AI协作

触发“AI建议”背后的风险

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/M82cWMKlQSWMEjjCJ4FNarnfJReg2azvU157e6mF8TNjFmKSxxJ9y3wEMvib4zDdZnKhtn8r23v1Zx3ib1L5UpsNqhZwnCFrxcVwiaosZevT3M/640?wx_fmt=gif&from=appmsg)

近日，某部门员工为准备“产品演示”所需的材料，使用VS Code添加扩展Claude Code for VS Code插件对PPT内容进行润色与优化。在多轮对话调整后，AI生成了完整的PPT方案，并提示需要安装相关Python扩展以完成PPT生成功能。员工根据提示，在开发环境中安装了相关扩展组件。然而，正是在这条看似正常的交互链路中，潜在威胁悄然启动。

在同意安装后，Claude Code开始在后台静默执行Python脚本，尝试从网络下载所谓的“python扩展插件”并进行安装。整个过程未出现任何弹窗或警告信息，完全在用户无感知的情况下执行。

就在脚本运行、文件落地的瞬间，终端安全产品实时防护模块成功拦截两个后门程序型病毒文件。风险内容如下：

· 检测类型：HEUR:Backdoor/PHP.WebShell天珣EDR For Claw

· 涉及文件：php\_deserialization.md、php.md

· 文件路径：VS Code 扩展目录

· 触发进程：code.exe

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRCCyRHBDt4ZsNYrTF6DMPUnGUlIOSox9DzQNORBiaWmthzoSz0GkIZJ5EAKZFbwfX1deTsF2icEMtWiaxOsolSD3fJw88BcLSdL3g/640?wx_fmt=png&from=appmsg)

这两个文件虽以普通“.md文档”格式命名，但实际包含WebShell后门代码。一旦成功安装，攻击者即可远程控制该终端，进而横向渗透至公司核心系统。

**天珣EDR For Claw的关键防护**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/M82cWMKlQSWMEjjCJ4FNarnfJReg2azvU157e6mF8TNjFmKSxxJ9y3wEMvib4zDdZnKhtn8r23v1Zx3ib1L5UpsNqhZwnCFrxcVwiaosZevT3M/640?wx_fmt=gif&from=appmsg)

本次案例正是最好的警示：一个看似正常的扩展插件，险些将病毒带入系统。这充分说明，只要智能体仍在与系统交互、仍在联网运行，运行时的动态防御就绝不能缺失——危险往往藏在“正常操作”背后。此次事件之所以未造成实际影响，关键在于天珣EDR For Claw在以下三方面的能力支撑：

* 实时风险监测能力：天珣EDR For Claw基于行为特征识别异常代码，而非仅依赖传统特征库，提升风险响应速度及抗干扰能力。
* 恶意行为分析能力：还原文件真实形态及串联异常行为路径，即使文件伪装为".md文档"，仍被识别出潜在WebShell行为。
* 环境防护覆盖：全局布防监控所有文件落地行为，风险往往并非来自“下载木马”，而是来自工具链中的关联调用。

**面向AI场景的终端安全演进**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/M82cWMKlQSWMEjjCJ4FNarnfJReg2azvU157e6mF8TNjFmKSxxJ9y3wEMvib4zDdZnKhtn8r23v1Zx3ib1L5UpsNqhZwnCFrxcVwiaosZevT3M/640?wx_fmt=gif&from=appmsg)

本次事件反映出一种重要趋势：风险来源正在发生结构性变化。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRBPNU4eC3okiadicLPu5tFnncCBz5u7eeaSy1mM4mKzuravSHKTMIQ2rPIvmo4YicRHLuCR4aHdXpm66l7B5A3VEHlxUia2POqsQPA/640?wx_fmt=png&from=appmsg)

换句话说： 风险不再只来自“你点了什么”，而可能来自“AI让你做什么”。

在AI与终端深度交互的场景下，攻击者不再需要诱导用户点击恶意链接，而是可通过AI的“建议”功能，将恶意代码植入合法的工具链中，因此，办公终端安全防护必须同步升级。天珣EDR For Claw在继承EDR实时监测、行为分析、威胁响应等核心能力的基础上，针对AI新型风险场景进行了专项能力增强：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j1hpA7GJeRBdmLRAxrAathP8ymCJy3sdBU8TC42iagtKdAhtEBH9enFoON8FBmQIn5WKUtrZp4I5z341BibuPH2dibdgDzQA6uyB9ArEG3jO7g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j1hpA7GJeRCPHoR6c4r5na2ogjqVNXiaFWxegHbpDUZr7km6ico0vaezx05OauMp7B1UBd5NE5AV2IqSy8vrbz3wQW2icaiaCmBHo4zoibdeQOFo/640?wx_fmt=gif&from=appmsg)

AI智能体就像一个“黑箱”，无论多么智能、如何进化，我们都难以预判它下一步会做什么、会调用什么资源。天珣EDR For Claw紧跟AI发展趋势，已全面升级以适配智能体运行时检测应用场景，在员工与AI频繁交互、各类插件和扩展不断调用的环境下，为组织提供及时、有效的Claw类终端运行环境安全防护能力，真正做到为AI办公保驾护航，为智能体筑牢运行安全防线。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/M82cWMKlQSXsox9qmIicxXbCjDmZUVPryE9SnKxQ9quGibMA6sGnEUbiaUk8jaFr9z1Kia3NtTvb9DQT4HrsrB91znHWia3wIp3NpgHK3qnrmkZI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=31)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/M82cWMKlQSXsox9qmIicxXbCjDmZUVPryE9SnKxQ9quGibMA6sGnEUbiaUk8jaFr9z1Kia3NtTvb9DQT4HrsrB91znHWia3wIp3NpgHK3qnrmkZI/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=32)

欲了解启明星辰的整体思路和其他关联文章：

[C19-S07启明星辰：龙虾安全六边形（暨OpenClaw类智能应用安全总览0323版）](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736446&idx=2&sn=3db23867f39336bd2b31aef7bf675ca4&scene=21#wechat_redirect)

往期精彩推荐：

[C02-X01启明星辰发布OpenClaw安全风险分析及防护建议（附下载链接）](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736072&idx=2&sn=23d61739aec2769f01b1fc434a03d292&scene=21#wechat_redirect)

[C03-S01启明星辰集团OpenClaw类智能应用安全指引V0.1](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736121&idx=1&sn=b88cab2b24a8187a82f63c17fd6c19e6&scene=21#wechat_redirect)

[C05-X02当AI助手变成“特洛伊木马”：OpenClaw安全危机警示录](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736121&idx=3&sn=a9f35f00fc7a145b28c534b42a133113&scene=21#wechat_redirect)

[C14-S05龙虾专网：用安全域思维化解Claw类智能体toB应用的安全困局](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736265&idx=1&sn=d2ff28e0666f19eafb5ade1f8981b9cf&scene=21#wechat_redirect)

[C18-U07个人养虾不踩雷！启明星辰发布免费个人版OpenClaw安全助手](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651736421&idx=1&sn=ae590ed819caef8073966092e86150f0&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/M82cWMKlQSUSEbcdpH3jVIx8nSiblU30evicY0YvAF0FefQDolHlmtLa4ep9DP3gXrIiaJnVicnDwl2bRrTYx4LaGwHUkNagC2jFn0URpia1fmS8/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=33)

•

END

•

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j1hpA7GJeRC2qhNVuHY3kr3qegdmDibeO5AcyiarxcpiaVuzgD2gCtWVaO31rOnFkP4YGicapbcp9TkZ1hXHwc477BgQOhdib7mciaxrN0yFGuXcU/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzA3NDQ0MzkzMA==&mid=2651688529&idx=1&sn=15ae6574a6aa36aa6b5b871b081a5da6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/j1hpA7GJeRDicRnEJ7UqI0I7hWW0GXslUcq8sX69icv2RsSKOX9AM85mDbiaY66pwHKzZXMlhO4wNCMw2BsXhBZiaEuvib7XXsK2XQmCq222rAJU/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/BwR7Xg3aXhbViaj0gQhCzVicIDc9gtBzytuEmgsDS4EqCtgpyMohatb3ZicDSDtcJJtvuhV9xpiczTpicJjcXkhVPpA/0?wx_fmt=png)

启明星辰集团

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BwR7Xg3aXhbViaj0gQhCzVicIDc9gtBzytuEmgsDS4EqCtgpyMohatb3ZicDSDtcJJtvuhV9xpiczTpicJjcXkhVPpA/0?wx_fmt=png)

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