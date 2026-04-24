---
title: GitHub评论可触发Claude Code、Gemini CLI和GitHub Copilot的提示注入漏洞
url: https://mp.weixin.qq.com/s/HkcUWECi3nwUgglYoUoMhw
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:53:26.511009
---

# GitHub评论可触发Claude Code、Gemini CLI和GitHub Copilot的提示注入漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0AW6rzvqggDzXMQiaHiaDnoqdPdemTlLxvRgLf9xseIjicmD0kEoib75J1q5X0DRAHcXYic2CzF2NQuQz9RM7IibHJY9WWdvvLdfEAk/0?wx_fmt=jpeg)

# GitHub评论可触发Claude Code、Gemini CLI和GitHub Copilot的提示注入漏洞

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hHqMxRIBBYhY9FmjE1ocPuJ3094QYxP88LpdeqTltEHJGW4brTlcuwn96TC7xWw7Iv2819l9loIFib3wTMD7tgrhM0BkzVUaI/640?wx_fmt=png&from=appmsg)

##

**Part01**

## ****新型"评论控制"攻击手法曝光****

研究人员发现一类名为"Comment and Control"（评论控制）的跨厂商关键漏洞，这种新型提示注入攻击利用GitHub的拉取请求标题、议题正文和评论作为武器，能够劫持AI编程Agent并从CI/CD环境中直接窃取API密钥和访问令牌。该攻击名称刻意模仿了恶意软件活动中经典的C2（Command and Control）框架。经确认，Anthropic的Claude Code Security Review、Google的Gemini CLI Action以及GitHub Copilot Agent（SWE Agent）三款广泛部署的AI Agent均存在此漏洞。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX3Sd4nq6btNX1F5lWBEnYHibx1cA8VXzXIIZo7EooImYomFjq4ibJbMUsdLIOpQHK5cmt65PwsoBVsxQHib8eycqia15d6H7Zq87n0/640?wx_fmt=jpeg&from=appmsg)

据研究员Aonan Guan介绍，整个攻击过程完全在GitHub平台内部完成：攻击者编写恶意的PR标题或议题评论，AI Agent将其作为可信上下文读取处理，执行攻击者提供的指令，并通过PR评论、议题评论或git提交将凭证外泄，无需外部服务器参与。与传统需要受害者主动要求AI处理文档的间接提示注入不同，"评论控制"攻击具有主动性——GitHub Actions工作流会在pull\_request、issues和issue\_comment事件时自动触发，意味着仅需打开PR或提交议题就能激活Agent，无需受害者任何交互。

**Part02**

## ****漏洞详情1：****

## ****Claude Code安全审查的PR标题到RCE漏洞****

在Anthropic的Claude Code Security Review中，PR标题未经任何净化处理就直接插入Agent提示。由于调用Claude CLI时未使用--disallowed-tools或--allowed-tools限制，子进程会继承包括ANTHROPIC\_API\_KEY和GITHUB\_TOKEN在内的所有环境变量。攻击者只需创建一个包含恶意标题的PR，突破提示上下文并指示Claude执行whoami、ps auxeww或env等命令，就能以JSON格式的"安全发现"将完整凭证转储到PR评论中。该漏洞通过HackerOne（#3387969）报告，Anthropic将其评为CVSS 9.4分严重漏洞（原为9.3分），并发放了q00奖金。

**Part03**

## ****漏洞详情2：****

## ****Gemini CLI Action的议题评论到API密钥泄露****

Google的Gemini CLI Action在"Additional Content"部分将议题标题、正文和评论纳入Agent提示上下文。攻击者通过在其后注入伪造的"Trusted Content Section"，就能覆盖Gemini的安全指令，导致Gemini将GEMINI\_API\_KEY作为公开议题评论发布。该漏洞由研究员Neil Fendley与约翰霍普金斯大学团队通过Google VRP（#1609699）报告，获得q,337奖金。

**Part04**

## ****漏洞详情3：****

## ****Copilot Agent的三重防御绕过****

GitHub Copilot Agent的漏洞在技术上最为复杂。GitHub原本实施了环境变量过滤、密钥扫描和网络防火墙三层运行时防护措施，但均被绕过：

* 环境过滤绕过：UU()函数仅过滤子bash进程的敏感变量。通过从该子进程运行ps auxeww可读取未过滤的父Node.js进程和MCP服务器的/proc/[pid]/environ，获取GITHUB\_TOKEN、GITHUB\_COPILOT\_API\_TOKEN及另外两个凭证。
* 密钥扫描绕过：GitHub扫描器检测ghs\_/ghu\_令牌前缀。在提交前对输出进行Base64编码可规避所有模式匹配。
* 防火墙绕过：编码后的凭证文件通过标准git push操作外泄至PR——这是白名单操作，与正常Copilot工作流活动无异。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3KDTE4sUdlmticrzqYr16xibs6tQWyQ9fSLJnGr63WfOFyHCMKriau3Uo1t13TyM6ImGukXOZd8cEYu6iavbjX69ZJZPMO3hibVpN8/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX0oKR8xJUaZjdj22dZrzQPw3ySmlqiaEG83ROnM82Nrt7NP8myMftwyz6rzJHdm23zJacG3PnpZxDHq3MOYOL3Azvl2MIRbUas0/640?wx_fmt=png&from=appmsg)

这三个漏洞存在相同的架构缺陷：不受信任的GitHub数据流入持有生产密钥且在同一运行时拥有无限制工具访问权限的AI Agent。研究人员指出，这是首次公开演示单个提示注入模式攻破多个主流AI Agent（包括一个已部署三重运行时防护的Agent）的跨厂商案例。

**Part05**

## ****缓解措施****

* 采用工具白名单而非黑名单：使用--allowed-tools仅授予最低必要权限；黑名单（如阻止ps）很容易通过cat /proc/\*/environ等替代方法绕过。
* 最小权限密钥原则：执行只读任务（如议题分类）的Agent不应持有具有写权限的GITHUB\_TOKEN。
* 设置人工审批环节：在Agent执行出站操作或访问凭证前要求人工批准。
* 审计所有AI Agent集成：检查CI/CD管道中的AI Agent集成，并监控Actions日志中的异常凭证访问模式。

安全专家警告，这种攻击模式不仅限于GitHub Actions，任何处理不受信任输入且能访问工具和密钥的AI Agent（包括Slack机器人、Jira Agent、邮件Agent和部署自动化管道）都可能受到影响。

**参考来源：**

Claude Code, Gemini CLI, and GitHub Copilot Vulnerable to Prompt Injection via GitHub Comments

https://cybersecuritynews.com/prompt-injection-via-github-comments/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1NlibR8DpnkZguk1so3ThwkXScRIP7SKicZdaVeLa1eMHdfLgFsOaFCP6qt2JaDlnDPzLe5MJBV1micoP6YM0SG5C9X1ibsshUiccM/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337140&idx=1&sn=134af642d92b85fc1076a8c83c09945c&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1bKq2xLKwFuy1Yl63ibm7kJUCW7hP4uRIhllVu6icLPkYcerZIx5264cbnPu5uCLCpb0ic16Gm32GC3B6ou34yFia9Nm4YJTGU4iag/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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