---
title: hvv 2026 - 钓鱼邮件不需要你点链接了：ZimReaper 证明，\"看见\"就够了
url: https://mp.weixin.qq.com/s/-o9GDvtu7z69007vYjPFXw
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:56:55.393415
---

# hvv 2026 - 钓鱼邮件不需要你点链接了：ZimReaper 证明，\"看见\"就够了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8qOq10zFicMBiawuT7kAhmq9ph3oXbRB0z2TyEaNjSDx9UsTicHQxV9dKEXgmA13VC4AgicGspPIqxxDic6UVPTVCF360JicaxkDumN8hEhViaLZ88/0?wx_fmt=jpeg)

# hvv 2026 - 钓鱼邮件不需要你点链接了：ZimReaper 证明，"看见"就够了

天黑说嘿话

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于MessFreeSecurity
，作者messfree

![](https://wx.qlogo.cn/mmhead/VNMic85jx3X5dte5sgSqnGasCCFV3OXmqyy7yLfibj8bsjFmqwTxibmHhEHxI9jhMW1muwyfFicibvHU/0)

**MessFreeSecurity**
.

提供社区优质咨询服务

![封面：ZimReaper 把攻击放在 2FA 之后](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMDPowNQqmsf9DSCvdv0CiaeKfG6icM6A1ucibYbQ5DB8tfrTVM9uXf4hlQrtKVQVn9DsAEDjq6sP4aJnsCUI0lPE5MsLfr30Biag3A/640?wx_fmt=png&from=appmsg)

如果一封钓鱼邮件里有链接，我们会提醒用户别点；如果带附件，我们会让沙箱先跑一遍；如果登录入口开了 2FA，很多人心里还会再踏实一点。

这一次，这三层经验都没有接住问题。

用户没有继续点击链接，没有打开附件，也没有在假页面里重新输入密码。他只是在已经登录的 Webmail 里打开，或者预览了一封邮件。随后，恶意 JavaScript 继承了这段登录会话：读取 CSRF token，尝试拿浏览器自动填充的密码，获取 2FA scratch codes，创建应用专用密码，枚举组织通讯录，再把近 90 天邮件打包外传。

我第一次把多国联合通报和 Proofpoint 的技术细节对在一起时，真正让我停下来的并不是“又一个存储型 XSS”。

而是这句话：

> **攻击者没有先绕过 2FA。它把代码放到了 2FA 之后。**

这才是 CVE-2025-66376 和 ZimReaper 最值得写的地方。

## 这件事为什么站得住

7 月 23 日，多国政府机构联合发布了针对 Zimbra Collaboration Suite 的安全通报。通报把这轮活动关联到俄国家支持背景的 LAUNDRY BEAR，称相关攻击自至少 2025 年 7 月开始，核心目的不是勒索，而是长期、隐蔽地获取邮件与身份数据。

同一天，Proofpoint 公开了更细的利用链，把这组活动跟踪为 TA488，把恶意 JavaScript 命名为 ZimReaper；Unit 42 则以 CL-STA-1114 跟踪相关活动。不同机构的命名并非严格一一对应，但在漏洞、时间、目标和窃密动作上能够互相印证。

![多国联合通报：事件、时间与影响](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMCQN2bL4lz9piadoMyP8lOAicVFUKYG3Vks2icdIQOQKg9GoVsZQkhfnSBiceHy0R60rfd5RkjVjd1xJpS1Hc6iadlOlxqL9ib3rj1PU/640?wx_fmt=png&from=appmsg)

官方修复记录也能把时间钉死：Zimbra 在 2025 年 11 月 6 日发布 10.0.18 和 10.1.13，明确修复 Classic UI 中可借 CSS `@import` 触发的存储型 XSS。

所以，这不是一篇靠“疑似”“网传”撑起来的故事。联合通报负责确认事件与影响，厂商研究负责还原攻击路径，补丁记录负责解释漏洞根因。三层证据刚好闭合。

不过，“零点击”三个字必须说准确。

Unit 42 使用了 zero-click；联合通报称它为 view-based exploit；Proofpoint 更谨慎，叫 half-click。三种叫法指向的是同一件事：**用户通常仍要打开或预览邮件，但不必再点链接，也不必打开附件。**

它不是“邮件一到服务器就必然自动失陷”。真正发生的事情是：邮件一旦在存在漏洞的 Webmail 里被渲染，攻击代码就获得了执行机会。

这个边界看似只是术语，实际上决定了整篇文章应该把镜头对准哪里。

不是钓鱼链接。

是邮件渲染器。

## 用户没有做错那一步

Proofpoint 公布的诱饵没有什么惊人的地方：合作邀请、活动会面、新闻摘要，都是情报活动里常见的主题。

![Proofpoint 披露的诱饵邮件，正文区域已经放大](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMDWibnzm4EvPYM7FJfv4NEqSRdjx1cKTyT7S2zLKbYUIDvl1N9jeEIicribfB5QUZtrMvUKytpGrCJM76xia95CyIKBIGH00822oxU/640?wx_fmt=png&from=appmsg)

如果只看这封信的文字，它甚至有些普通。

但这次的社工并不承担“把人骗去另一个页面”的任务。它只需要让收件人产生一个最轻微、也最正常的动作：看看对方写了什么。

过去我们拆钓鱼链路，常把邮件当成运输工具：

**邮件 → 链接或附件 → 第二个攻击面。**

这次不是。

**邮件正文自己就是攻击面。**

这意味着一个已经用了很多年的安全提醒突然少了后半句。用户没有点错，他只是看信；可在脆弱的 Webmail 里，**“看见”已经足够接近“执行”。**

half-click 不是在给 zero-click 降级。这个词反而把问题说得更精确：攻击者仍然需要人的注意力，却不再需要人的失误。

安全培训可以减少误点，但很难要求员工不要阅读工作邮件。到了这一步，风险已经从“用户会不会判断”退回到“产品会不会安全地渲染”。

## 一段被清洗掉的代码，为什么又活了

CVE-2025-66376 的根因不是服务端直接执行系统命令，而是 Classic UI 对邮件 HTML 的清洗与浏览器最终解析之间出现了语义差。

攻击者把原本连续的危险标签拆开，在关键字符之间插入 CSS `@import` 片段。清洗器看见这些片段后会删除它们，以为危险内容已经被处理；可删除动作完成后，前后残留字符又连到了一起。

最终，浏览器拿到的已经不是几段无意义的碎片，而是重新拼好的 `<svg onload=...>` 与解码执行逻辑。

![CVE-2025-66376 根因：清洗器与浏览器理解不同](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMCbYdEvB9xS10EeSKEMkyHVFVvttaFoGjd3naBtlP4937vMERZdFcTB4vdhmH7qmf4Ib38ez4XsqMQumaianUkYKalKKUmSjgp4/640?wx_fmt=png&from=appmsg)

![Proofpoint 无损源码证据：标签拆分与重新成形](https://mmbiz.qpic.cn/mmbiz_png/8qOq10zFicMAiabMOPHKiayAyiaQG2Z4qVGsicnGCODZklIJEPajKTxeqHG2yjnicAW6r5iajG1uqNyqnM5pjR6v1gFl1yoL8MvyT8sgaYErbhJSm4/640?wx_fmt=png&from=appmsg)

这里最容易被一句“消毒绕过”带过去。真正要琢磨的是：

> **安全组件检查的是处理前的字符串，浏览器执行的是处理后的语义。**

两边都做了自己认为正确的事，危险恰好出生在两者之间。

我见过不少类似问题。WAF 与后端对同一请求的理解不同，代理与应用对路径归一化的结果不同，上传检查器与解析库对文件格式的判断不同。表面上是不同漏洞，底层却是同一种失配：**负责放行的组件和负责执行的组件，没有在看同一个对象。**

这次，它发生在邮件正文上。

恶意代码随后还会再解码、加载第二阶段，后期样本又增加 XOR 混淆。可这些只是增加分析成本，真正的门已经在浏览器重新拼出可执行标签时打开了。

所以，XSS 本身不是新闻。新闻是这次 XSS 跑在哪里。

## 真正危险的不是 XSS，而是 XSS 在哪里运行

“存储型 XSS”很容易让人产生一种熟悉感：弹个框、偷个 Cookie、做一次会话劫持。

ZimReaper 把这个印象彻底打碎了。

脚本运行时，用户已经通过登录和 2FA，浏览器里有当前会话，有 Webmail 能调用的接口，也可能保存着自动填充信息。攻击者不是从门外撞进来，而是让一段代码出现在门内。

![恶意代码位于 2FA 之后的已认证会话](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMBCSxavyzwUicXARVmpBmOp349DJA3AleESC7CEa3Dt9Uh8YqfYbAzTL8OjXf1Dh0TLgYfsrKcmicrc4jx3HoWpK5YiacY1vSJNsA/640?wx_fmt=png&from=appmsg)

接下来的动作因此一气呵成：

* 从页面与会话中获取 CSRF token；
* 构造隐藏登录字段，诱使浏览器回填已保存的用户名和密码；
* 调用 Zimbra API 获取 2FA scratch codes、系统版本等信息；
* 创建一个名为 `ZimbraWeb` 的应用专用密码；
* 枚举 Global Address List；
* 搜索并导出目标用户近 90 天内的邮件。

应用专用密码尤其关键。它原本是为了让 IMAP、POP3、SMTP 等客户端在不反复走交互式认证的情况下工作。ZimReaper 调用现成接口创建它，相当于从当前会话里再开一扇门。

这里也要把证据边界说清：Proofpoint 观察到了应用密码的创建和外传，但没有直接确认攻击者后来是否实际使用了这组密码。可从能力上看，它已经把一次浏览器内执行，变成了可以脱离当前页面继续访问邮箱的凭据。

**过去说 2FA 被绕过，往往是攻击者从认证流程外面想办法。ZimReaper 展示的是另一种路径：先借用已经通过 2FA 的会话，再从里面生产一个不必重新经历交互式 2FA 的入口。**

写到这里，“2FA 之后”才真正有了分量。

## DNS 只搬小件，系统接口负责搬家

ZimReaper 的外传设计并不追求一种通道包打天下。

密码、2FA scratch codes、邮箱地址、版本信息、应用专用密码，这些数据体积小、价值高，被编码后塞进 DNS 查询。Proofpoint 公开的结构里，可以看见会话标识、字段类型、编码数据和外传域名被依次拼进子域。

![DNS 与 HTTPS 两条外传通道的分工](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMA68K3ZZz5pu0ialWLMD3mA5GmN8egK2fZpAb1LxU7qvzsggJhKDvAMrMA8XWab2MZXNDmcicicJk0bJXBaPabeiavUiaBYa4MW0Kbo/640?wx_fmt=png&from=appmsg)

可近 90 天邮件不是“小件”。脚本直接调用 Webmail 的搜索与导出能力，按时间窗口收集邮件，生成 TGZ 归档，再经 HTTP POST 送走。

![Proofpoint 无损源码证据：近 90 天邮件批量导出](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMBamd7BAJibP6Va4voMYCl5DrfiaNl6iaMMFY6C11TaM3aWrSMC7tYOVctoEVuMA7Zte251mIXqZmu1uiak94Y35aibicodevoxXz1bY/640?wx_fmt=png&from=appmsg)

这也是整条链里第二个容易被低估的地方。

攻击者没有重新实现一套邮件读取器，也没有在终端落一个笨重的采集工具。它借用的都是系统已经提供给正常用户的能力：搜索、导出、通讯录查询、应用密码创建。

> **恶意脚本真正做的，不是“攻破每一项功能”，而是把一组合法功能按攻击目标重新编排。**

单看每一步，都像正常业务；连起来，才是一条完整的窃密流水线。

这对安全运营提出了一个麻烦的问题：如果检测只盯恶意文件、异常进程和落地木马，这条链会留下多少传统终端告警？

Proofpoint 特意指出，脚本运行在已认证的浏览器上下文里，终端侧可见痕迹可能很稀薄。真正有价值的线索反而分散在别处：邮件渲染、Webmail API 调用、应用密码创建、异常 DNS 子域、批量归档和外联 POST。

换句话说，攻击链已经跨过了很多团队的工具边界。

## 邮箱不只是通信工具，它还是一份组织关系图

ZimReaper 不满足于偷当前用户的几封信。

它用双字符组合查询 Global Address List，试图遍历组织目录；拿到通讯录后，又能从已经失陷的真实邮箱继续发送带利用代码的邮件。

第一封信也许来自陌生地址，下一封却可能来自同事、合作方，甚至一段真实往来中的账号。此时，攻击者偷走的不只是内容，还有组织内部最难伪造的东西：关系、语境与信任。

我一直觉得，邮箱在很多政企环境里被低估了。它表面上是通信工具，实际上同时保存着：

* 谁在和谁协作；
* 哪些项目正在推进；
* 组织内部怎样称呼一件事、下一封钓鱼信应该以谁的口吻发出。

所以“近 90 天邮件”不是一个简单的数据量指标。对长期情报活动而言，那是一段仍然鲜活的组织记忆。

**通讯录告诉攻击者下一步找谁，历史邮件告诉攻击者下一封信怎么写。**

这比一次口令泄露更难收尾。密码可以改，过去三个月暴露出去的关系和语境却收不回来。

## 补丁上线之后，还剩三件事

官方补丁已在 2025 年 11 月发布。使用相关版本的组织，第一步是升级到包含该修复的受支持版本，而不是把“暂时没看到告警”当成安全证明。

![从零日利用到联合通报的时间线](https://mmbiz.qpic.cn/sz_mmbiz_png/8qOq10zFicMA1hgXyHzvC0aictT799MfyR7ENItrALcaSic4jdxzMzcoKyOXwKLSDqkAyEiaQYiaq3j0yYzvRpanfoIoQFVniccLicYWnqUeFV5qHA/640?wx_fmt=png&from=appmsg)

但升级只能阻断新的渲染利用，已经生成的凭据不会因此自动消失。真正的收尾至少还包括三件事：

**查入口。** 回看可疑邮件、Classic UI 使用情况、异常 Webmail 请求和联合通报给出的检测线索，判断恶意正文是否曾被渲染。

**查持久化。** 在审计日志中关注 `CreateAppSpecificPassword`，核对异常创建、命名为 `ZimbraWeb` 的应用密码，并撤销不明应用凭据和 2FA scratch codes。

**查外传。** 联合核对 DNS、代理与邮件系统日志，追踪长子域查询、异常归档导出、批量 GAL 查询和面向外部地址的 POST。

如果确认受影响，再做密码轮换与会话清理。顺序很重要：只改主密码，却留下应用密码；只打补丁，却不追已经导出的邮件；都可能让处置看起来结束，实际上只完成了一半。

公开材料里还有一个看似矛盾、其实应该保留的细节：Proofpoint 表示其直接遥测在 2026 年 2 月后没有再观察到 TA488 活动；Unit 42 与联合通报仍强调未修补实例面临持续风险。

这两句话可以同时成立。前者描述一家厂商看见了什么，后者描述暴露面还允许什么。**没有继续看见，不等于对手失去了继续利用的条件。**

## 当“别点链接”只剩半句话

写到最后，我又回到那封看起来很普通的邮件。

收件人没有下载附件，没有把密码交给假登录页，也没有无视浏览器的红色警告。他只是点开一封与工作有关的信。

页面开始渲染。

清洗器删掉了它认为危险的碎片，浏览器把剩余部分重新拼好；代码继承登录态，拿到能调用的接口，把 2FA 后面的身份材料、通讯录和近 90 天邮件一点点搬走。

这一次，用户没有做错什么。

真正失守的，是我们长期默认安全的那条边界：**只要没有继续点击，阅读本身就是安全的。**

当邮件正文不再只是内容，而可能是一段运行在已认证会话里的程序，安全团队下一次再对员工说“不要点可疑链接”时，后半句话应该由谁补上？

---

### 资料来源

* 多国联合网络安全通报 AA26-204A（PDF）
* 英国 NCSC：多国合作披露相关行动
* Proofpoint：TA488 Targets Zimbra Mailservers with Half-Click Exploits
* Unit 42：Russian Global Webmail Espionage
* Zimbra 官方 CVE 修复提交记录

> 说明：本文公开截图均来自上述一手资料；为便于公众号阅读进行了裁切和中文标注，具体账号、外部链接与攻击基础设施已遮蔽。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/X0IJicBiaSvwUndPM1oiaUlc9LFiccxcQqRhqic4mIR6vPGOkM5pEVp8wrP7YUwDSYB0a97thV89Axdv6Xehuk9rJKw/0?wx_fmt=png)

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