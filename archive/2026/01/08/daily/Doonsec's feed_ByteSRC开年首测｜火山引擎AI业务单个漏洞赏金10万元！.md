---
title: ByteSRC开年首测｜火山引擎AI业务单个漏洞赏金10万元！
url: https://mp.weixin.qq.com/s/fXWXAQePehmW8wCHTWIjXA
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:28:20.614945
---

# ByteSRC开年首测｜火山引擎AI业务单个漏洞赏金10万元！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gAcolpf06WqwgE9XLshoAwUdWqaCLzDAIWGDBO1qvSkO3dH7cB55XicTG3QQibTp2ibhv4Pyicyf65KlfcmqoJ6I7g/0?wx_fmt=jpeg)

# ByteSRC开年首测｜火山引擎AI业务单个漏洞赏金10万元！

字节跳动安全中心

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gAcolpf06WqwgE9XLshoAwUdWqaCLzDAXN4U5h2DSjQeBh7VSp2ibjpAEq5MdiaZXR8w5rD8wEVaFvUIGnFAxe7A/640?wx_fmt=jpeg)

**专测时间**

1月9日-1月23日

报告标题请备注【火山AI专测】

需通过SRC平台“热门活动”模块提交

src.bytedance.com

专测范围

* 大模型服务平台：

  www.volcengine.com/product/ark
* 大模型生态广场：

  www.volcengine.com/mcp-marketplace，火山引擎云原生 MCP Server
* 大模型应用开发：

  Coze、知识库、VikingDB 向量数据库
* 大模型应用：

  www.volcengine.com/product/ai-app-lab，应用广场上线的火山引擎自研AI Agent
* LUMI：

  https://console.volcengine.com/lumi
* 虚拟数字人：

  https://console.volcengine.com/avatar/
* 联网问答Agent：

  https://console.volcengine.com/ask-echo
* AI特效平台（Ebox）：

  https://console.volcengine.com/ebox/home
* 智能创作云：

  https://console.volcengine.com/muse/home/smartRecommend
* 智能推荐平台：

  https://www.volcengine.com/product/rec
* agentkit：

  https://www.volcengine.com/product/agentkit

**专测奖励**

***奖励一 单个漏洞可达100,000元！***

严重/高危漏洞，享有 **2倍**积分

中危漏洞，享有 **1.5倍**积分

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gAcolpf06WqwgE9XLshoAwUdWqaCLzDAtrPZ045of7LtgVmMWFg4R95gpiclgcUFwllN1ngruowtY2lxpNGOu7A/640?wx_fmt=png&from=appmsg)

*（🍗对利用思路巧妙、利用过程描述清晰的报告给予额外1-50分鸡腿分）*

***奖励二 重点漏洞奖励***

**重点漏洞类型（高危及以上）**

**在翻倍基础上额外奖励2000元/个：**

1、容器逃逸（需证明影响其他用户）

2、全回显SSRF

3、批量获取登录后的用户会话数据/高敏AK等涉及核心敏感信息泄漏的漏洞

4、可获取MCP/Agent控制权限的漏洞

5、涉及任意账号接管/登录的漏洞

6、模型投毒、模型污染类可影响其他用户交互的漏洞

***奖励三 重点情报奖励***

**重点情报类型（高危及以上）**

**在翻倍基础上额外奖励2000元/个：**

1、对平台算力资源有重大影响的情报

2、涉及到大量平台用户数据的情报

**补充说明**

1、非信息安全漏洞导致的内容安全风险不收、与模型提示和响应内容相关的问题暂不收取。如这些问题对产品可造成额外的、可直接验证的安全影响（机密性、完整性、可用性），则正常收取。模型提示和响应内容的相关问题举例：

-模型提示：越狱/安全绕过（如 DAN 等相关提示词）

-模型响应内容：大模型输出恶意内容（如违规营销信息、恶意代码等，可向产品帮助中心反馈)

-模型幻觉：让大模型假装成计算机终端并执行命令等

2、非隐私数据泄露相关的AI服务风险暂不收取（jail break，prompt leak等）。

3、个人用户从Coze发布至豆包的智能体及插件所引发的安全漏洞不收取（如UGC 内容中用户自身行为导致的信息泄露不收取）。

4、沙箱环境中的代码执行/命令执行本身是预期的产品功能，如果能逃逸或影响到其他用户容器，则正常评分。（有效条件：逃逸到宿主机/物理机，获取有效敏感信息和权限，或证明通字节内网）

5、客户端漏洞均以最新版为准

6、正在专项排查中漏洞，如某系统**、****某类型漏洞内部展开统一的专项治理时暂不收取，具体情况以平台审核人员回复为准。**

7、活动发奖：漏洞通过后，平台将会先下发基础积分，预计2月30日前下发活动额外奖励积分。请师傅们耐心等待❤️

**测试规范**

**核心原则**

1、合法化原则：所有测试行为必须遵守《网络安全法》《数据安全法》《个人信息保护法》等法律法规要求。

2、无害化原则：禁止进行可能引起用户利益受损、业务异常运行的测试行为。

**通用测试规则**

1、禁止使用可能造成业务影响的测试工具和手法。如：只允许手工低频测试，不允许手工高频发包、或使用自动化工具/插件测试，避免因过度测试导致业务告警、服务中断等问题。

2、禁止进行内网渗透测试行为和任何有害化的测试行为，包括但不限于：获取内网权限后在内网使用扫描器、或横向接触非对外开放系统目标、获取内网应用/主机权限/数据、上传 webshell、反弹 shell等。

3、禁止下载、保存、传播业务数据，包括但不限于业务服务器以及Github 等平台泄露的源代码、运营数据、用户资料、登录凭证等，若存在不知情的下载行为，需及时说明和删除；测试过程中获取的相关代码/数据，务必在SRC漏洞确认后立即删除，不得非法留存及使用（无论数据是否脱敏）。

4、禁止任何类型的网络拒绝服务（DoS 或DDoS）测试，或通过软件、工具自动扫描产生大量数据流量的行为。

5、禁止进行近源攻击或者黑客物理入侵、社会工程学测试或邮件钓鱼等非技术漏洞测试，尤其是禁止使用社工库等非法手段获取用户密码。

6、禁止使用任何违反平台规定或法律法规的文字、图片、视频作为测试素材。

7、禁止以证明漏洞危害为借口，对目标系统进行破坏性操作，如删改数据/配置、植入恶意程序等。

8、禁止用户打扰类测试。包括但不限于向真实用户邮箱、手机、社媒账号等渠道发送测试信息、发起群聊、推送push等干扰信息；或通过电话、即时通讯工具等方式直接联系真实用户进行测试。

9、禁止对未授权厂商/业务、超出测试范围列表进行漏洞挖掘，可与管理员联系确认是否属于资产范围后进行挖掘，否则未授权的法律风险将由漏洞挖掘者自己承担。

10、请将所有测试操作和行为及时、如实、完整上报，因故意瞒报、漏报等造成业务损害或潜在风险，ByteSRC保留追责权利。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/gAcolpf06Wrdliakx1n069Dzc4QQZhfowABgicK9t8tq97xTyx5wAAx3snNqXic5iclBlj4QdvELujkCiceGO5sJYlQ/0?wx_fmt=png)

字节跳动安全中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gAcolpf06Wrdliakx1n069Dzc4QQZhfowABgicK9t8tq97xTyx5wAAx3snNqXic5iclBlj4QdvELujkCiceGO5sJYlQ/0?wx_fmt=png)

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