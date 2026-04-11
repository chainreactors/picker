---
title: 一文搞懂内网渗透核心：PTH 哈希传递攻击从原理到攻防
url: https://mp.weixin.qq.com/s/2erzVvknr65tUvvATKbJeQ
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:20:10.589257
---

# 一文搞懂内网渗透核心：PTH 哈希传递攻击从原理到攻防

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EH6KHiaolAFA2mBDAib8NaaboKAu1aIibDk1K7fgicGEVOYibLEwnckSKiaDMNqqFTJR0LlHXXNBnfe7f5EzGH5gsa9GSSGsPOtkeVaVcztLZncsQ/0?wx_fmt=jpeg)

# 一文搞懂内网渗透核心：PTH 哈希传递攻击从原理到攻防

镌远科技
镌远科技

河北镌远网络科技有限公司

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/5xic9OHsHiafbUVg4naibSQnNsuMVRYqdlLLzHovhH9jcrrEaj6ia94y9TTpBJTlQDQBcgwMczFq8BRURR9fJIdeLg/640?wx_fmt=gif&from=appmsg)

PTH（Pass-the-Hash，哈希传递）是Windows内网渗透中极具代表性的攻击技术，其核心是利用NTLM身份认证协议的设计缺陷，让攻击者无需获取用户密码明文，仅通过抓取到的NTLM哈希值，即可冒充目标用户身份，实现内网横向移动与权限提升，是红队攻防演练、HW行动及内网渗透中的核心手段之一。本文将从原理、场景差异、工具实战、哈希碰撞及攻防要点等方面，对PTH攻击进行全面且细致的解析，兼顾理论与实操，适配各类学习与实战场景。

**01**

***PTH攻击核心简介***

PTH（哈希传递）本质上是一种身份伪造攻击，核心利用Windows系统NTLM认证机制的漏洞展开。与传统密码破解攻击不同，PTH攻击无需破解NTLM哈希值以获取明文密码，只需获取目标用户的NTLM哈希，即可直接复用该哈希完成身份验证，进而访问目标系统资源、提升操作权限或实现内网横向移动，大幅降低了攻击者的攻击成本与技术门槛。

**02**

***PTH攻击的底层原理***

PTH攻击能够成功实施，核心根源在于NTLM协议的挑战-响应（Challenge-Response）认证机制存在设计缺陷，具体原理可拆解为以下4点，清晰易懂且贴合实战：

1. NTLM协议的核心设计缺陷：该协议将NTLM哈希视为合法的身份凭证，而非密码明文，攻击者可通过复用哈希值，直接绕过密码明文验证环节，模拟合法用户身份。

2. NTLM认证的核心逻辑：认证过程中，服务端会生成一个随机数（Challenge），客户端需基于自身的NTLM哈希值与该随机数，计算出响应结果（Response），服务端仅验证Response与自身预期结果是否一致，即可完成身份认证。

3. 哈希来源无需追溯：NTLM协议仅校验Response的计算结果，不关注NTLM哈希的生成过程与来源——无论该哈希是通过合法密码派生，还是通过恶意手段抓取，只要Response匹配，即可通过认证，这是PTH攻击能够成立的关键。

4. Challenge的获取无需构造：Challenge由服务端动态生成，攻击者发起认证请求时，服务端会主动返回该随机数，攻击者无需预测、构造，仅需被动接收即可完成后续Response的计算。

**03**

***不同环境下PTH攻击的差异***

PTH攻击的成功率与操作规则，会因网络环境（工作组、域环境）的不同而存在显著差异，明确这些差异是实战中精准实施攻击的前提。

**工作组环境下的PTH规则**

工作组环境中，各主机相互独立，无统一的身份管理机制，PTH攻击的核心依赖“密码复用”：若抓取到A机器某用户的NTLM哈希，且B机器的相同账号（如本地管理员）使用相同密码，则该哈希可直接用于对B机器发起PTH攻击，成功获取B机器的对应权限。

实战示例：

•A机器本地管理员密码为P@ssw0rd，对应的NTLM哈希为31D6CFE0...

•B机器本地管理员密码同样为P@ssw0rd，其NTLM哈希与A机器完全一致（31D6CFE0...）

•攻击者获取A机器的NTLM哈希后，可直接复用该哈希，对B机器发起PTH攻击，顺利获取B机器的本地管理员权限。

**域环境下的PTH规则**

域环境中，所有主机受域控制器（DC）统一管理，域用户的身份凭证（用户名、密码、NTLM哈希）在整个域内通用，这使得PTH攻击的威力大幅提升：只要攻击者获取域管理员账号的NTLM哈希，即可通过哈希传递，横向渗透到域内任意一台主机（包括域控制器），实现全域权限控制。

**04**

***本地账号与域账号的PTH差异***

除网络环境外，账号类型（本地账号、域账号）也会影响PTH攻击的成功率，核心影响因素为Windows系统的UAC（用户账户控制）机制，具体规则如下：

核心结论：本地普通用户及非管理员组用户的PTH攻击均会失败；仅本地管理员组中的administrator账号、以及加入本地管理员组的域用户，可成功实施PTH攻击。

**本地账号的PTH规则**

本地账号受UAC远程连接机制的限制，且不同Windows系统版本的规则存在差异：

•Windows Vista之前的系统：无严格的UAC远程限制，本地管理员组内的所有用户，其NTLM哈希均可用于PTH攻击；

•Windows Vista及其之后的系统：UAC机制升级，仅内置的administrator账号的NTLM哈希可成功实施PTH攻击；本地管理员组内的其他非administrator账号，远程连接时会被剥离管理员权限，其哈希无法用于PTH。

**域账号的PTH规则**

域账号不受UAC远程连接机制的限制，适用规则更灵活，适配实战场景：

•普通域机器：若域用户被加入该机器的本地管理员组，即可使用该域用户的NTLM哈希，对该机器发起PTH攻击；

•域控制器：域管理员组内的所有用户，其NTLM哈希均可用于PTH攻击，可直接获取域控制器的最高权限。

**05**

***UAC机制与关键注册表配置***

UAC（用户账户控制）是Windows Vista及以上版本引入的权限管理机制，核心采用“最小特权原则”，用于隔离权限、降低特权滥用风险，同时也是影响PTH攻击的核心因素；此外，两个关键注册表项可直接调控PTH攻击的可行性，是攻防双方的重点关注对象。

**UAC机制核心说明**

UAC通过划分“标准用户”和“受保护的管理员账户”，实现权限的动态隔离，核心要点如下：

•标准用户：可执行日常非特权操作，无需权限审批；

•本地管理员组成员：默认以最小特权模式运行应用，执行需要管理员权限的操作时，系统会通过安全桌面弹出审批提示，确认后才能提升权限；

•令牌差异：本地管理员组成员执行常规操作时，系统会自动生成“受限令牌（Filtered Token）”，仅保留标准用户权限；远程连接时，内置administrator账号可直接获取完整管理员令牌，非administrator的本地管理员账号会被剥离管理员权限，而加入本地管理员组的域用户，可直接获取完整管理员令牌（UAC不生效）。

**关键注册表配置（攻防核心）**

**1.禁用内置administrator账号的PTH能力（防御方常用）**

通过修改FilterAdministratorToken注册表项，可强制内置administrator账号遵循UAC审批模式，阻断其PTH攻击能力：

•注册表路径：HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System

•键值名称：FilterAdministratorToken

•键值说明：
        ￮值为0（系统默认，禁用状态）：内置administrator账号远程连接时，直接获取完整管理员令牌，可正常用于PTH攻击；

￮值为1（启用状态）：内置administrator账号需遵循UAC审批模式，远程连接生成受限令牌，无法用于PTH攻击。

•官方描述：User Account Control: Admin Approval Mode for the built-in Administrator account（用户账户控制：内置Administrator账户的管理员批准模式）。

**2.放开非administrator本地管理员的远程权限（攻击方常用）**

通过LocalAccountTokenFilterPolicy注册表项，可禁用UAC远程连接限制，让本地管理员组内的所有用户，远程连接时均可获取完整管理员令牌，拓展PTH攻击的适用范围：

•注册表路径：HKEY\_LOCAL\_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy

•系统默认：Windows Vista及以上版本，默认无该注册表项，即默认启用UAC远程限制；

•查询命令（管理员权限）：reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy

•禁用UAC远程限制（管理员权限）：reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /t REG\_DWORD /d 1 /f

•恢复默认限制（管理员权限）：reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /f

免责声明：因传播、利用本公众号“河北镌远网络科技有限公司”所提供信息而产生的任何直接或间接后果及损失，均由使用者本人自行承担，本公众号及作者不承担任何责任。本公众号所发表内容中，凡注明来源的，版权归原出处所有；无法查证版权或未注明出处的，均来自网络并系转载，转载旨在传递更多信息，版权归原作者所有。若存在侵权情况，请联系小编，我们将第一时间删除处理。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5xic9OHsHiafYW3QgXBz1b5H4ibkrGDyiaMY9GyomiaWib5oKm6chXCj8uMuZOQMXvUKAic6jfbSG5jKicTdNZia815xQmA/0?wx_fmt=png)

河北镌远网络科技有限公司

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5xic9OHsHiafYW3QgXBz1b5H4ibkrGDyiaMY9GyomiaWib5oKm6chXCj8uMuZOQMXvUKAic6jfbSG5jKicTdNZia815xQmA/0?wx_fmt=png)

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