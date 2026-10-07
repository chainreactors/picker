---
title: 红队工程师的盲区： 你手里的C2，可能正在反控你
url: https://mp.weixin.qq.com/s/Kjpdg7DuWLdGxURJaktUtA
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:53:34.002686
---

# 红队工程师的盲区： 你手里的C2，可能正在反控你

# 红队工程师的盲区： 你手里的C2，可能正在反控你

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 红蓝对抗 · 漏洞复盘

// 红队基础设施 · 安全盲区

# 红队工程师的盲区： 你手里的C2，可能正在反控你

一个存储型XSS怎么把C2主控端连锅端，外加红队框架这几年的"集体翻车"清单

C2安全红队基础设施XSS到RCE

> 🔑 **一句话精华**
> 红队工具自己也有洞：C2 主控端一沦陷，所有"被控端"都成了别人的。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9a0Wicv5zFqHUrZrd4sW1ks0cF0xf0bNicjZ1mTP6bibh7OVezltxibzr8Jc3iaJyzXj4kicPbhSk64pVAfmPEicFhChAJaSo9XCKJE8/640?wx_fmt=png&from=appmsg)

## 00这个漏洞，最吓人的不是RCE

2026-09-30，「荧惑安全」的惑灵发了一篇代码审计，主角是开源红队平台 CyberStrikeAI C2（1.7.11 及以下），两个漏洞，一个存储型 XSS 链式 RCE，一个 /result 端点任意文件写入，结论一句话：主控端服务器被反控。这不是又一篇"某某产品爆洞"的通告，它戳中的是红队工程师最不愿面对的事实——我们天天拿 C2 打别人，可 C2 自己一旦被攻破，拿下的不是一台机器，是整个演习里所有已控制的机器和攒下的全部战果。

先说原文还原的那条链。CyberStrikeAI C2 的 Web 控制台，在渲染 Beacon 会话和文件列表时，把后端返回的、攻击者可控的字段（ImplantUUID、InternalIP、文件名）塞进 HTML 的 `onclick` 属性，中间只过了 `JSON.stringify()`，没做 HTML 转义。问题就在这：stringify 只转义 JS 双引号，不碰 `<` 和 `>`，而 HTML 属性解析里反斜杠不是转义字符。攻击者拿任一 Beacon 二进制（里面带着 Token 和 AES Key），伪造一个"假上线"，在 UUID 里埋一段 `<img src=x onerror=...>` 的 payload，等管理员在控制台点开会话详情，代码自动执行。

接下来才是要命的地方。这段 JS 从 `localStorage` 里读出管理员认证 Token（明文存的，没设 HttpOnly），再调用 C2 平台自带的 `POST /api/terminal/run` 接口——这个接口直接在服务端本地 `exec.Command("sh","-c",命令)` 执行。于是攻击者拿到反弹 shell，身份是 C2 主控端的 root，原文复现里 `whoami` 返回的就是 root。

![反控：被控端反过来接管主控端](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibbgGA4PeTuwY8MrSN5B1LX45fYlFQ3to5EQr18kclYTgibeJicgCE8Wwb94B2R6W0J329iaib6hz7oticJOqXSjUXD8ibxPUKEiaIIok/640?wx_fmt=png&from=appmsg)

⚠️ 注意：RCE 的目标不是那台被渗透的目标机，是 **C2 主控端本身**。这把"一个 XSS"升级成了"整个红队基础设施沦陷"。漏洞已修复，升级最新版即可。

第二个洞更省事：/result 端点有个明文 JSON 回退机制——AES-GCM 解密失败就当明文解析，再叠加 `blob_suffix` 路径穿越，攻击者只要有一个监听器级 Token（从任意 Beacon 就能提取），就能往服务端任意路径写任意后缀的文件，写 authorized\_keys、写 cron 任务、写 webshell 都行。两个洞，四个环节，漏掉任意一个都断不了，可它偏偏全漏了。这不是手滑，是一类设计缺陷的集中爆发。

## 01这不是孤例，红队工具自己全是洞

我把最近几年红队框架的漏洞翻了一遍，越翻越后背发凉——开源 C2 几乎被扒了个遍，而且漏洞类型惊人地一致。Sliver 是这两年最火的开源 C2 之一，光近两年就连着爆了三个：SSRF（CVE-2025-27090，伪造 implant 回调让 teamserver 主动向外开 TCP，暴露 redirector 后面的真实 IP）、Wireguard netstack 漏 peer 隔离（CVE-2025-27093，拿到一个 implant 密钥就能横向够到同服务器的其他 implant 和操作员端口转发）、已认证 RCE（CVE-2024-41111，能看全部控制台日志、踢掉其他操作员、改任意文件、最后把服务器抹掉）。

|  |  |  |
| --- | --- | --- |
| 框架 | 漏洞 | 问题一句话 |
| Cobalt Strike | CVE-2022-39197 | teamserver XSS：被控端输入直接进操作员 UI |
| Sliver | CVE-2025-27090 / 27093 / CVE-2024-41111 | SSRF 暴露真实 IP / 漏 peer 隔离 / 已认证 RCE |
| Havoc | 多个 | 默认口令 password1234、Service API 鉴权绕过、exec.Command 命令注入 |
| Covenant | CVE-2026-92717 | SignalR hub 漏鉴权检查，未登录就能领合法 JWT（CVSS 9.1） |
| LazyOwn | CVE-2026-68503 | 硬编码默认凭据写在配置里，谁都能登进 C2 控制台（CVSS 9.8） |

Cobalt Strike 更经典，2022 年那个 team server 的 XSS，被控端送一段不可信输入上来，操作员在 UI 里一看，HTML 就执行了——和昨天 CyberStrikeAI 的存储型 XSS，完全是同一个模子刻出来的。再往远看，Ninja 的下载端点未鉴权路径穿越直接 RCE，SHAD0W 把 beacon 上报字段拼进编译命令也是未鉴权 RCE，连 2016、2017 年的 Metasploit、Empire 都有过 RCE 史。Include Security 那篇研究把话说得很直白：C2 框架要处理不可信的被控端输入，天生就是 RCE 温床。

> 📌 **老宋数据**
> 开源 C2 不是"更安全"，是"更透明所以更常被扒"。Cobalt Strike + cs2modrewrite 这两个组合，在 2025 年全球观测到的 OST（攻陷后基础设施）活动里占约 22%，约 67% 的 OST 受害事件都跟它有瓜葛（Recorded Future 2025 年度报告）。

## 02为什么红队工具这么爱"反噬"自己

把上面这些案例摆一块，根因其实就三类，记住这三条，你基本能预判下一个洞出在哪。

第一类：不可信输入喂给了操作员的浏览器。被控端是敌人可控的，它上报的任何字段你都该当恶意处理。可太多框架把这个字段直接 stringify 塞进 onclick，或者原样回显到控制台 UI，结果操作员一查看，XSS 就在自己机器上跑起来了。CyberStrikeAI 的存储型 XSS、Cobalt Strike 的 39197 都是这条线，根子是信任了来自被控端的数据，又没在 HTML 上下文里转义。

第二类：管理接口漏了鉴权。teamserver 的 Web 控制台、Service API、消息 hub，这些本该是红队内部的"金库"，却常有忘了挂授权检查的情况。Covenant 的 hub 漏鉴权、Havoc 的 Service API 绕过、LazyOwn 的硬编码口令，本质都是"进门前没查身份证"。再加上 Token 明文存 localStorage、不设 HttpOnly、没上 CSP——一旦 XSS 触发，Token 就像放在桌上的钥匙。

第三类：用户输入直接进了命令执行。这是最致命的设计失误。CyberStrikeAI 的终端接口直接 exec.Command，Havoc 把"服务名"拼进 exec.Command 调用，SHAD0W 把上报的架构值塞进 shellcode 编译命令。只要攻击者能往这些参数里塞东西，就不再是"能不能看"，而是"能不能跑"。

// 老宋说：这三类缺陷的共同点是，红队框架的作者把精力全花在"怎么绕开蓝队的检测"上，却忘了自己这套基础设施本身也是台联网的服务器，也要按服务器安全的规矩来。安全圈有句老话——你要攻克的"目标"，往往不如你脚下的"阵地"先失守。

## 03对红队：你的基础设施，先把自己锁死

讲完吓人的，给干活的兄弟几条马上能动手的硬规矩。这些都是 Red Team Infrastructure Wiki 和多年实战沉淀下来的，不玄学。

|  |  |
| --- | --- |
| R1 | **管理接口绝不外暴**Web 控制台、teamserver 管理端口、SSH，iptables 只放行可信来源 IP。控制台只对自己开放，整条反控链从源头就断了。 |
| R2 | **改默认口令，上公钥+多因素**password1234 和硬编码凭据都是出厂裸奔。公钥认证-only、关密码登录、能上 MFA 就上 MFA，这是底线。 |
| R3 | **关键文件上 chattr 锁**teamserver 核心目录 chattr +i 防改，连 root 都动不了，真被进来了也少一层"就地篡改"。 |
| R4 | **网络分权隔离**钓鱼 SMTP、载荷托管、长期 C2、短期 C2 分开部署，跨不同云厂商和地区。一台暴露不影响全局，还能快速重建。 |
| R5 | **日志集中 + 高价值事件告警**新的 C2 会话、凭据捕获、异常登录，实时推到内部频道。你越早知道"主控端被人摸了"，损失越小。 |

![锁住C2基础设施：仅可信IP、多因素、分权隔离](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flicyK9Gn6OiaH1HiasqL8wRCfdm3SFNN2NiccoXWvS90qicuz6pHsxkP5z468RGHnbYtArXeImtQs4f0XYsrxYBdN2Uc8wUkribeTfLM/640?wx_fmt=png&from=appmsg)
> 📌 **老宋数据**
> 基础设施不是部署完就完事，是持续过程。一台只跑必要服务、只对自己开放的 teamserver，被反控的概率，远低于一台图省事开着默认配置暴露在公网的。

## 04对蓝队和甲方：找到敌人的C2，也许你能反手拿下它

最后一节说给防守方听，这也是红队框架满身是洞给防守方的最大礼物。

攻击者的 C2 既然这么多洞，那当你在态势里发现一个可疑的 C2 框架——比如抓到一台主机连着个不知名的 teamserver、或者流量里浮现出 Sliver/Havoc 的特征——别急着只封 IP。先把它当线索，再把它当弱点。既然开源 C2 普遍有未鉴权接口、默认口令、XSS 到 RCE 这类缺陷，你手里的样本完全可以反过来探测：它用的什么版本？是不是那个有洞的版本？能不能用公开 PoC 反手连进去看看攻击者攒了什么。

说白了，攻击者把他的"指挥所"架在网上，指挥所本身可能就是个漏风的帐篷。蓝队以前是被动封堵 beacon 流量，现在多一招：顺着 C2 的洞，反过去看清对方到底摸了你多少、拿了你什么，甚至合法地接管他的基础设施（当然，限定在授权和法律的框架内，取证优先）。这也是为什么甲方做威胁狩猎时，发现 C2 别只加一条封禁规则就完事，多问一句"它的主控端安不安全"，往往能挖出更大的收获。

> 🔑 **一句话收尾**
> 武器是用来打仗的，可最该先护好的，是握武器的那只手。

推荐阅读

这几篇相关的，建议一并看看：

1. 渗透测试从业者的 CTF 大模型CypherMind：6.4GB 离线跑通夺旗赛（护网与实战攻防/红蓝对抗）

https://mp.weixin.qq.com/s/Dm\_bvyKxeemIBUvo\_mS\_QQ

2. 渗透测试从业者的全能工具箱：76,700+ Star、185+工具一键到位（HackingTool 从零到实战）（工具测评/红蓝对抗）

https://mp.weixin.qq.com/s/uGsj9p-8VFLYXHo-fCrQ9Q

3. 渗透测试从业者的新工具 潜影 TraceHarvest（工具测评/红蓝对抗）

https://mp.weixin.qq.com/s/wRyYs\_Mtn22GfKHEQtzexg

4. 他把一台"滴水不漏"的服务器扫出了 17 个秘密（护网与实战攻防）

https://mp.weixin.qq.com/s/9kbAWAzAweEVjDlcw189FA

5. 甲方运维应急排查：银狐木马进内网，3步定位失陷主机（护网与实战攻防/红蓝对抗）

https://mp.weixin.qq.com/s/WdAhKEhLdQktbmt7D7AgVw

网络安全老宋 · 转载请注明出处

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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