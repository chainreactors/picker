---
title: 【漏洞通告】OpenClaw WebSocket共享令牌权限提升漏洞
url: https://mp.weixin.qq.com/s/3Z7LIkvVeEUlZB-Ykg9VjQ
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:20:26.652349
---

# 【漏洞通告】OpenClaw WebSocket共享令牌权限提升漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/APc6NwjLsxQLymoibHTk5y3CdTKuSvF97dH1UgE1rIcUZ1U1OD8vibcuicVfPkP9DfVibgfvN77sHD0909lKRpMCHEE1s6A2e9MK10qDkxzicSKM/0?wx_fmt=jpeg)

# 【漏洞通告】OpenClaw WebSocket共享令牌权限提升漏洞

深瞳漏洞实验室
深瞳漏洞实验室

深信服千里目安全技术中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTujdiapzfriagZmAhribDVicc21sfDdu4SDC3Il3MWU1Jvl0Eyx5ErLmibD0gh7CqGMSW5JAjNLQDUIsaiacRbr2cp2DSZeHOs7Djrw/640?wx_fmt=gif&from=appmsg)

**漏洞名称：**

OpenClaw WebSocket共享令牌权限提升漏洞

**组件名称：**

OpenClaw

**影响范围：**

OpenClaw ≤ 2026.3.11

**漏洞类型：**

权限提升

**利用条件：**

1、用户认证：需要用户认证

2、前置条件：默认配置

3、触发方式：远程

**综合评价：**

<综合评定利用难度>：复杂，需要有普通用户权限。

<综合评定威胁等级>：高危，可造成权限提升。

**官方解决方案：**

已发布

**漏洞分析**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxQYYMXoUZj8QWxaThtdOVYCG8wwXHKAjhzoplhc6xGPQIYPoC23VBiaHBVIQrqKmCzjt14IjuvpJuMvzqgFyNRAhtkiaffOC9yEA/640?wx_fmt=gif&from=appmsg)

**组件介绍**

OpenClaw是github上的开源个人AI代理项目，通过WhatsApp、Telegram、Discord等聊天工具交互，支持本地/云LLM，具备自主执行能力（如浏览器控制、设备操作、邮件/文件处理、语音对话）。用来打造常驻本地、能真正干活的个人AI助手，用于日常自动化、生产力提升和开发者任务。

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxTgUfaaJy7yaUOeUibhABiakVMYaDVakyhpgCUiaRib0C2ovED2yEAkcIu1tuaZTy9WssVmLALbQVuNMF4hEC2ic6GLoJEY21kV35mU/640?wx_fmt=gif&from=appmsg)

**漏洞简介**

2026年3月17日，深瞳漏洞实验室监测到一则OpenClaw组件存在权限提升漏洞的信息，漏洞威胁等级：高危。

OpenClaw 在使用共享令牌或密码进行 WebSocket 连接认证时，服务端未对客户端自行提交的权限作用域做校验与限制，直接信任并采纳客户端声明的高权限，**导致持有普通共享令牌或密码的用户可非法声明管理员权限，实现权限提升。**

**影响范围**

目前受影响的OpenClaw版本：

OpenClaw ≤ 2026.3.11

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxRcUaUckiaJnlKw55M3GnR3JQGP5oiau0wicXLTZa7iaaBpT9P7xMn2LpmjKnvaGK5Ww1iaTv4Kh1RG4M1ic2e1PzEtKMlC3jLpnGYjc/640?wx_fmt=gif&from=appmsg)

**官方修复建议**

官方已发布最新版本修复该漏洞，建议受影响用户将OpenClaw更新到2026.3.12及以上版本。
下载链接：https://github.com/openclaw/openclaw

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQjuS8iaavSBDkqAOiceIHxreqacia2nP2d7oUdp4tyB3dykH81oGDmhK9bzHm8wuruXcIXODzicOlUtl9S5e7W3T4Y0Gibh43ubHUM/640?wx_fmt=gif&from=appmsg)

**临时修复建议**

l 关闭未使用的功能模块，减少潜在攻击入口。

l 遵循最小权限原则，严控各类敏感操作权限范围。

l 非必要不暴露服务到公网，限制访问源为可信范围。

定期更新系统及各类组件至安全版本，及时修补已知隐患。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxSCfwcpEicsJjvJ07wNttfz9f3GZ48bibOsfVfymRtF2vb9GocKx8ibibBlpicLcxUZtM7gTibxPMvWoGex1SUANNOA4FH7mEdSD2z1g/640?wx_fmt=gif&from=appmsg)

**深信服解决方案**

**风险资产发现**

支持对OpenClaw的主动检测，**可批量检出业务场景中该事件的受影响资产情况****，**相关产品如下：

**【深信服云镜YJ】** 已发布资产检测方案，指纹ID:0032395。

**【深信服漏洞评估工具TSS】**已发布资产检测方案，指纹ID:0032395。

**参考链接**

https://github.com/openclaw/openclaw/security/advisories/GHSA-rqpp-rjj8-7wv8

**时间轴**

**2026/03/17**

深瞳漏洞实验室监测到OpenClaw WebSocket共享令牌权限提升漏洞信息。

**2025/03/17**

深瞳漏洞实验室发布漏洞通告。

点击**阅读原文**，及时关注并登录深信服**智安全平台**，可轻松查询漏洞相关解决方案。

![](https://mmbiz.qpic.cn/mmbiz_png/APc6NwjLsxRDbReZccxibVBZcWhicecAkQmhmhtGD8Lg4rPcFGfGLQDBdhXT6pKtvPjQFyoOmW7ZEliav5egQWeYGLiab2Qz4ic6RbOmtSiaEJvqo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zvcIHbwGGYKbqDVYsVKzNNia1jYtHf49C7133AlDXAgex2W4lFvpia56tjQQDkiauNBrl08YbxqG01A/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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