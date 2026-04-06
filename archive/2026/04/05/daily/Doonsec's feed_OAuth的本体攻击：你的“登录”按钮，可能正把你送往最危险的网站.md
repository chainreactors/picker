---
title: OAuth的本体攻击：你的“登录”按钮，可能正把你送往最危险的网站
url: https://mp.weixin.qq.com/s/Wzj9u1bl-fQTaEWnBm8evQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:40:40.155387
---

# OAuth的本体攻击：你的“登录”按钮，可能正把你送往最危险的网站

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibcQnc3swf1MmRaBw6Ewjb9kIib4KqMonKF9fZBBM2fDMT4yXf5DpXLc8aSjovWUxPEuux9HvicMQtibdCDkUmXppSdPE2bY2icic1GY/0?wx_fmt=jpeg)

# OAuth的本体攻击：你的“登录”按钮，可能正把你送往最危险的网站

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 黑客不再只偷你的密码。他们正在利用OAuth协议的合法“重定向”功能，将你从熟悉的微软、谷歌登录页面，直接“空投”到钓鱼网站或恶意软件下载页。微软刚刚详细披露了这种新型攻击手法，它绕过了传统邮件和浏览器的安全检测，专门针对政府与公共部门。这已经不是漏洞利用，而是对协议设计初衷的“合法滥用”。

## 一次点击开始的“信任背叛”

先设想一个日常情景：你收到一封财务部门的邮件，标题是“关于员工报告的紧急审核”，附件里有个PDF，里面是个看似正规的链接，指向公司常用的Microsoft Teams或者Google Drive登录界面。

你觉得没问题，点了进去。

浏览器跳转到了你每天都要见几次的 `login.microsoftonline.com` 或者 `accounts.google.com`，网址开头完全正确，域名也是官方的。但下一秒，页面没有要求你输入密码，只是闪了一下，就把你带到了一个陌生的页面，提示你下载某个“重要文档”，或者需要你“重新确认账户信息”。

整个过程丝滑得让你甚至没时间产生怀疑。

微软的最新报告揭示，一批攻击者正在把上述情景大规模变为现实。他们没有去攻破微软或谷歌的服务器，也没有窃取你的令牌——他们做的，是“劫持”了OAuth身份验证中一个原本用于处理错误的“重定向”机制。

**简单说，他们让微软/谷歌自己动手，把你送到了他们指定的地方。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcEyHKDrY6cpRmxaRzdzzCbM5xwmWjpVJUQg0cGsYDSrLx9hO0VpiamD3Qes30L0DjeVFKHFiaLOCmCQEtRbQeAiaialz5cypjibYwo/640?wx_fmt=webp&from=appmsg)

## 攻击链条：五步舞曲，全程静默

这场攻击就像一场精心编排的舞蹈，利用了用户对正规登录页面的绝对信任。

### 第一步：诱饵投递

攻击者群发钓鱼邮件，主题极具欺骗性：电子签名请求、社会保障、财务通知、政治话题，甚至附上伪造的日历邀请（.ics文件）。他们用上了免费群发工具，有的还用Python和Node.js写了定制程序，并利用云邮件服务和虚拟机来隐藏踪迹。

有的链接直接嵌在邮件正文，有的则藏在PDF附件里，让邮件正文一片空白，进一步躲避邮件安全扫描。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcuVXcjucpQictibPwozIX7SJJiccXu8O9QuqCyjAXyky7GGZEQkRmibMuS0hSG78cdAomhqdQPNaibgKGOHyW52usne7Xiab15KbHwA/640?wx_fmt=webp&from=appmsg)

▲ 文档共享审核类钓鱼邮件样本

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibc7hEpjBVlnrhQHcibDDyJKNDA1l66JbyAuj9KpbOUmuJfGBIFH0sQbnJT6gzibB8dCN2lXT0bLCBtUfsXicp9pHaCkRhMdibqF9nI/640?wx_fmt=webp&from=appmsg)

▲ 社会保障主题钓鱼邮件样本

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6TibeK8Womk453uMytqVrX9yfPFNdr52guL7icSS5BWQQCQWGWH8uht6pmFnd35JP3VcB7MfiavUQJSaqsvusubQAa76vn46Z0nKibzc/640?wx_fmt=webp&from=appmsg)

▲ Teams会议主题钓鱼邮件样本

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcFynic30ib2JjsTWI1eX7rW8zXbGsJojmQoocIMRBwpQNcNro7B1xlpXMUkHSEjqYYKc6eeB2sicXrBk4TZMB4oqLurMmQBficibxg/640?wx_fmt=webp&from=appmsg)

▲ 密码重置主题钓鱼邮件样本

![](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibelNXricia1c8lrPn7aLuRfnY1IGnrXWnSSXHr8CJVP6Tw5mrC44JVkNCH9ADTO8qQXnMpj7S7ndY5BMMxrpMvtYT96qficfkpdiaM/640?wx_fmt=webp&from=appmsg)

▲ 员工报告主题钓鱼邮件样本

### 第二步：静默OAuth探测

链接的核心是一串精心构造的OAuth授权URL。以微软Entra ID为例，攻击者会发出这样一个请求：

https://login.microsoftonline.com/common/oauth2/v2.0/authorize
?client\_id=某个恶意应用的ID
&response\_type=code
&scope=
&prompt=none
&state=错误是由于范围无效而触发的

这个URL的关键在于几个参数的组合：

* **prompt=none**：要求“静默认证”，不向用户显示任何界面。
* **scope=**：或者直接留空，或者填一个无效值。这摆明了就是让请求失败。
* **/common/**：表示面向所有租户，不用单独指认。

这个请求的目的**根本不是认证成功**。它是为了触发身份提供商（微软/谷歌）去检查用户的登录状态和条件访问策略，然后在**静默失败后**，按照OAuth协议的规定，将用户重定向到应用程序注册时指定的“重定向URI”。

没错，那个“重定向URI”，在攻击者的控制之下。

### 第三步：错误重定向

微软Entra ID处理这个不合法的请求，发现scope无效，静默登录失败，于是执行标准操作：向浏览器返回一个包含错误信息的重定向，目标正是攻击者预先设置好的那个钓鱼域名。

用户会看到网址瞬间从官方的`login.microsoftonline.com`切换到了类似`https://malicious-site.com/download/xxxx?error=interaction_required...`这样的地址。

### 第四步：从钓鱼到恶意软件投递

一些攻击者在这里就展示常规的钓鱼页面，比如仿冒的Outlook或公司内网登录框（可能会使用EvilProxy等中间人钓鱼工具包）。

但更危险的变种来了。部分攻击者直接利用这个重定向进行恶意软件投递。用户被重定向后，一个ZIP压缩包会自动下载到本地。

### 第五步：终端沦陷与持久化

压缩包里装的是精心设计的恶意LNK快捷方式。一旦用户打开它（通常因为好奇这是个什么“文档”），就会执行一个复杂的PowerShell脚本。

脚本首先进行主机侦察，然后利用Windows内置的`tar`工具解压出三个文件：一个合法的`steam_monitor.exe`，一个恶意的`crashhandler.dll`，和一个加密的`crashlog.dat`配置文件。

接下来是典型的DLL劫持：PowerShell启动合法的`steam_monitor.exe`，这个程序会去加载同目录下的`crashhandler.dll`，而这个DLL正是恶意载荷。最终，解密后的恶意代码在内存中执行，建立出站连接，与攻击者的指挥控制（C2）服务器成功接头。一次完整的终端沦陷就此完成。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tbTbtBE6Tibf3MzyyvhLKC2e6HF0Of0rAuAhOC6v96KGYUEjPWQAk2QSC47IngribCk2rvTk8ICtKbteutxhXb3q5w2wEk8TqGkF877tRRvVY/640?wx_fmt=webp&from=appmsg)

▲ 完整的攻击链条图示

## 这不是漏洞，是设计被“玩坏了”

这才是这次攻击最让人头疼的地方。它利用的不是软件漏洞，而是OAuth 2.0协议（RFC 6749）白纸黑字定义的行为。

协议规定，授权服务器（如微软、谷歌）在遇到错误时，**应该**将用户代理重定向到客户端注册的重定向URI，并附上错误参数。这个设计的初衷是为了给用户流畅的错误处理体验。

攻击者只是钻了这个“设计空子”。他们用`prompt=none`和无效`scope`故意触发错误，然后“合法”地利用了这个重定向流程。

2024年发布的OAuth安全最佳实践RFC 9700中，第4.11.2节“授权服务器作为开放重定向器”就明确警告了这种风险：“攻击者可以通过故意触发OAuth错误……迫使授权服务器将用户重定向到攻击者指定的URI。”报告证实，这种理论上的风险，现在已经成了活跃的攻击武器。

## 防御建议：信任不再可靠，监控必须加强

面对这种“本体攻击”，传统的基于特征码的防御会显得力不从心。微软和报告给出的核心建议，指向了**更严格的治理和更广泛的监控**。

* **收紧OAuth应用管理**：限制用户自行同意 OAuth 应用的权限，定期审计并移除闲置或权限过高的应用。
* **利用条件访问策略**：不要只依赖登录成功与否做判断，要结合设备合规性、地理位置、风险信号等多种因素。
* **开启增强型日志记录**：全面收集身份、邮件、终端的日志，进行跨域关联分析。
* **警惕异常OAuth参数**：培训安全团队关注邮件中的OAuth链接，特别是包含`prompt=none`参数的链接。检查`state`参数是否被用于编码电子邮件地址。

// 示例高级搜寻查询：查找与无效OAuth范围参数相关的URL点击事件
UrlClickEvents
| where ActionType == "ClickAllowed" or IsClickedThrough == true
| where isnotempty(Url)
| where Url startswith "https://" or Url startswith "http://"
| where Url has "scope=invalid" or UrlChain has "scope=invalid"

微软也给出了相关的威胁指标供各组织自行排查：

> **攻击者使用的微软客户端ID（部分）**：9a36eaa2-cf9d-4e50-ad3e-58c9b5c04255, 89430f84-6c29-43f8-9b23-62871a314417, 440f4886-2c3a-4269-a78c-088b3b521e02...
> **初始重定向URL（部分）**：hxxps[:]//dynamic-entry[.]powerappsportals[.]com/dynamics/, hxxps[:]//login-web-auth[.]github[.]io/red-auth/, hxxps[:]//westsecure[.]powerappsportals[.]com/security/...

## 写在最后：身份信任的边界正在模糊

这份报告清晰地标示了一个趋势的转变：当强密码和多因素认证（MFA）越来越普及，直接偷凭证的难度变大时，攻击者开始把矛头对准了**信任关系本身**。

他们不再试图成为你，而是**欺骗系统，让系统亲自把你送到他们面前**。这比伪造一个登录页面要高级得多，也有效得多。

对我们安全从业者来说，这意味着防御思维需要升级。不能再把微软、谷歌的登录页面无条件地视为“安全区”。每一次认证请求，即便是流向这些可信域名的，也需要被置于更严格的审视之下。身份安全、邮件安全和终端安全之间的数据壁垒必须被打破，因为攻击链本身已经将它们无缝衔接。

这或许是一个令人不安的启示：在最基础的信任构建环节，攻防的较量已经进入了更深的协议语义层。安全，从来都比我们想象的要复杂一个维度。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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