---
title: 【漏洞预警】Jenkins公告25个漏洞，其中5个涉及本体的漏洞需要重点关注
url: https://mp.weixin.qq.com/s/00RXUG32GhwIjlzEt4-q-g
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:22:36.793112
---

# 【漏洞预警】Jenkins公告25个漏洞，其中5个涉及本体的漏洞需要重点关注

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LAQpgdWQScut7rbuwdEtM9CwADWNm3SBKnPzeKRvj6yObo77Z5BAB2SyMw9KjZf8DQVb2fS4v472A05RMTo2446d62CtRLNC7FuSMAu9jLk/0?wx_fmt=jpeg)

# 【漏洞预警】Jenkins公告25个漏洞，其中5个涉及本体的漏洞需要重点关注

YGnight
YGnight

night安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctVS8Ps0NsFTqMiasz8uDibcvoib0spt17ORFYGT7Lk8y0JElHpWukiczXboIicO8mrOUut0DwfE4PvMwpuReeibS0yQHqN8Tictdm4Z4/640?wx_fmt=png&from=appmsg)

Jenkins 8 月 5 号公布了25个cve漏洞，除开插件漏洞后主要涉及5个需要注意的漏洞。

一、漏洞清单

**CVE-2026-70426** · Agent Remoting 反序列化绕过

**CVE-2026-70427** · tar 解压符号链接任意文件写

**CVE-2026-70428** · 文件参数路径穿越任意文件写

**CVE-2026-70429** · 用户名 Unicode 大小写冒名

**CVE-2026-70430** · 命名策略配置类型越界

|  |  |
| --- | --- |
| 版本区间 | 状态 |
| weekly ≤ 2.575 / LTS ≤ 2.568.1 | 受影响 |
| weekly 2.576 / LTS 2.568.2 | 已修复 |

二、原理分析

70426 这条最值得拆一下。Jenkins 主控和 agent 之间走  Remoting 库传序列化对象，主控收数据时按 JEP-200 套了一层类白名单挡反序列化攻击。但 Remoting  3384.v60d89463d9e0 及更早的版本里有一条备用解析路径，这层过滤没套上去。能在 agent 上跑代码、或者有  Agent/Connect 权限的人，把对象从这条备用路径送进去，主控照收照反序列化。能触发的范围限在 Jenkins 自带和 Java  平台类，插件自带的依赖不会被反序列化，但这足够在主控上跑代码了。

70427 和 70428 都是任意文件写，路径不同。70427 出在解  tar/tar.gz 包时对符号链接名处理不干净，能控制 agent 的人塞个特制包就能按 Jenkins  跑的那个用户的文件系统权限往任意位置写。70428 出在文件参数名字里的路径穿越识别错，有 Item/Configure 和  Item/Build 权限的人能把文件写到主控任意位置。

70429 是用户名比对前后不一致。Jenkins 给大小写不敏感的用户名建规范  ID 时走 lowercase，但实际比对用的是 String#equalsIgnoreCase，后者会把某些 Unicode  字符当成跟别的字符相等——比如"无点 i" ı 被认为等于普通小写 i。能建用户的人就能起一个跟现有用户撞名的账号顶替别人权限。Jenkins  自带的用户库不让 ASCII 外字符注册，默认摸不到，接了外部安全域的要注意。

三、完整攻击链

简单梳理一下流程，拿70426举例一下，70427/70428 是平行入口，落点都是主控代码执行。

1拿到 Agent/Connect 权限

内部能连 agent 的人，或者已经控制了某台 agent 进程，这一步不要管理员权限。

2从备用解析路径送对象

那条没套过滤的路径直接收下，主控在自家进程里把对象反序列化掉。

3主控上跑命令

落 webshell 或者反向连接都行，主控进程的权限就是 Jenkins 跑的那个用户的权限。

4拿走主控上的东西

凭据、云令牌、构建任务配置都在 JENKINS\_HOME 下，主控代码执行之后想读什么读什么。

这批补丁里 agent 反过来打主控这条路是真的——不是只听话的从节点，一台被控制的 agent 借 70426 就能咬到主控。能跟 agent 通信的人，主控代码执行这个风险就该认下来。

四、自主排查

下面两条都是只读，检查是否存在漏洞范围内。

版本号

```
# 响应头里的 X-Jenkins 字段，不用登录就能读curl -sI https://<你的jenkins>/ | grep -i x-jenkins
```

通信库版本和 agent 权限

```
# 服务器本地看实际加载的通信库版本find $JENKINS_HOME -name 'remoting-*.jar' 2>/dev/null# 后台 Manage Jenkins - Security - Agents# 确认低权限不能连 agent，Agent/Connect 只发给可信节点
```

五、修复防御方案

升级版本，weekly到2.576、LTS到2.568.2

升不了可以暂时将不可信的节点断开

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LAQpgdWQSctTWicwicwovsVtMLAjYPfEB9lMRmJJiaIozWIuicwrbneXZ3pGly4lRNAd1WrP6AKYA925Iz4c1EbnMLCOqWzkCmdCLXDQibsG4VQw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SaibaRNhOjqiaCicRfSc5cJ3oiaCRqb97SmncCWWvuTyytibyIDxB9ZXWOuNaiaGAX2t0DYAAbdJ7aicS6WeCz4wfMoUg/0?wx_fmt=png)

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