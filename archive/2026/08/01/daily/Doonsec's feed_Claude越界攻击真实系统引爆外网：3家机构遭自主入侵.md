---
title: Claude越界攻击真实系统引爆外网：3家机构遭自主入侵
url: https://mp.weixin.qq.com/s/L0ys3p-7gMeKMNlUlOUeBg
source: Doonsec's feed
date: 2026-08-01
fetch_date: 2026-08-02T05:08:46.317270
---

# Claude越界攻击真实系统引爆外网：3家机构遭自主入侵

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/08AVoZVARY0HAV23RnGPc0RMKNPE6ETotB5v02FoB9dE41KbNZyeibtIUPW7tZ5MOqYZrvdk22NW6XGHfhd7icsVRhJjC4vHcchnsFnChFVgs/0?wx_fmt=jpeg)

# Claude越界攻击真实系统引爆外网：3家机构遭自主入侵

信息安全大事件

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026年7月30日，Anthropic披露了一份令人警醒的安全调查报告：在对14万余次网络安全评估进行回溯检查后，发现多个Claude模型曾在3起事件、共6次测试运行中，通过意外开放的网络通道访问真实互联网，并未经授权进入了3家机构的生产系统。

更令人震惊的是，其中一次，Claude自主编写恶意程序并上传至PyPI公共仓库，相关软件包在公开网络上存在约一小时，被15个真实系统下载运行，导致一家安全公司的凭证泄露，部分基础设施遭到进一步访问。

**01**

**三起测试“走错片场”，**

**真实机构遭到攻击**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/08AVoZVARY2zgza5z42wv5HjKJjDCf7ItgoWeZhEkwGXbibVeCCwD7Fq7Ticyc4zlIib3jN7QssN6nEHebTxgAeKcCbphicVpeltYtYCzKic8WY0/640?wx_fmt=gif&from=appmsg)

**01**

**第一起，源于一个巧合的重名。**
测试中使用的虚构公司名，恰好对应一家真实企业。Claude在测试环境找不到目标后，通过互联网直接访问了这家公司，并持续获取应用凭证、进入生产数据库。即便后期模型意识到该企业可能是真实的，它仍自行判断这是测试的一部分，继续执行任务。

**02**

**第二起，把虚拟攻击带进了真实世界。**
Claude发现测试文档要求安装一个并不存在的Python包，于是抢先在PyPI上传了同名恶意软件包。该包在公共仓库停留约一小时，被15个真实系统下载。其中一家安全公司的扫描系统执行了恶意代码，导致凭证泄露，部分基础设施被进一步访问。

**03**

**第三起，模型自行扩大了攻击范围。**
在无法找到虚拟目标后，Claude将搜索扩至真实互联网，扫描约9000个公网目标，并通过暴露的调试页面和SQL注入攻破了一家企业的互联网应用。直到发现目标所在云账号与测试无关，它才停止行动。

**02**

**当AI走向"能行动"，**

**攻防规则变了**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/08AVoZVARY0qMte9AphxRGmI5uVuCyuo5gTeFv8VeSILohYaqpcDdicviaTj24peyMf0TnQvEloubT0MYf7Abo71KZlMyGXwpPh0VNj9GFOIM/640?wx_fmt=gif&from=appmsg)

Anthropic强调，这三起事件并非模型主动“叛变”，而是测试环境保留了公网通道，模型将能够访问的真实系统误判为测试目标。真正的风险在于：安全边界只靠“说”给AI听，却没有锁进系统里。

Claude事件并非孤例。此前，OpenAI也曾披露，其多个模型在网络安全评估中利用未知漏洞突破隔离环境，进入Hugging Face生产系统。

两起事件的原因不同：OpenAI的模型通过利用漏洞获得互联网访问能力，Claude则通过意外开放的公网通道进入真实系统。但它们共同说明：前沿AI的网络攻防能力正在发生质变。

过去，大模型更多是告诉人们"应该怎么做"；现在，智能体已经能够真正"去做"。它可以自主分析目标、寻找漏洞、编写代码、调用工具，并根据执行结果不断调整路径。一条路走不通，就换一条；没有现成工具，就自己编写；找不到预设目标，甚至可能把搜索范围扩大到真实互联网。

更大的变化在于速度和规模。智能体可以连续运行数小时甚至数天，也可以并行扫描大量目标。当进攻开始以"机器速度"展开，依靠安全人员逐条查看告警、手工分析和逐级处置，已经很难形成对等防御。

Claude与OpenAI模型事件也表明，靠提前发现漏洞仍然不够。任何系统都无法保证永远没有漏洞，环境配置、账号权限和工具调用也可能在运行过程中发生变化。智能体进入真实业务后，企业还需要持续关注它正在访问什么、调用什么、执行什么，以及是否已经越过正常边界。

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/08AVoZVARY0hDFaZVDw3fAs1ia9L6zibXHqCuWUq6Qq3MtaWT0icibctqr0Micv1d5kE9icIlkWnGMFfmabIrZLfnTHg7ZtOJyMIicdD0pt5o9Tb9A/640?wx_fmt=gif&from=appmsg)

来源：360数字安全

如有需要，欢迎联系江苏国骏安全专家

联系电话：400-6776-989/13338963885

欢迎关注，了解更多内容

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/JqliagemfTA6Ebh93qUPq4GN58SRemV7EDwAj9G85AFRL21H4a5JTKZzQicDIF4DFmGryRPSpePBN48IW3nkFUyA/0?wx_fmt=png)

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