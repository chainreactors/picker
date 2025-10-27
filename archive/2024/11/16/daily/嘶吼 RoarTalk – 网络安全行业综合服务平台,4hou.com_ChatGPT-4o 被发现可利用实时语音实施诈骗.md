---
title: ChatGPT-4o 被发现可利用实时语音实施诈骗
url: https://www.4hou.com/posts/l08J
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2024-11-16
fetch_date: 2025-10-06T19:16:28.130016
---

# ChatGPT-4o 被发现可利用实时语音实施诈骗

ChatGPT-4o 被发现可利用实时语音实施诈骗 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# ChatGPT-4o 被发现可利用实时语音实施诈骗

胡金鱼
[新闻](https://www.4hou.com/category/news)
2024-11-15 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)115498

收藏

导语：根据 OpenAI 的越狱安全评估，o1-preview 的得分明显更高，该评估衡量模型在应对对抗性提示时抵抗生成不安全内容的能力，得分为 84%，而 GPT-4o 得分为 22%。

研究人员表明，有恶意分子可以滥用 OpenAI 的  ChatGPT-4o的实时语音 API 来实施从低到中等成功率的金融诈骗。

ChatGPT-4o 是 OpenAI 最新的 AI 模型，带来了新的增强功能，例如集成文本、语音和视觉输入和输出。由于这些新功能，OpenAI 集成了各种保护措施来检测和阻止有害内容，例如复制未经授权的声音。

基于语音诈骗涉及价值数百万美元的问题，而深度伪造技术和人工智能驱动的文本转语音工具的出现只会让情况变得更糟。正如 UIUC 研究人员在他们的论文中所证明的那样，目前不受限制地可用新技术工具没有足够的保护措施来防止网络犯罪和欺诈者的潜在滥用。

这些工具可以通过覆盖语音生成事件的代币成本来设计和实施大规模诈骗操作，而无需人工干预。

**研究结果**

研究人员的论文探讨了各种诈骗，例如银行转账、礼品卡渗漏、加密货币转账以及社交媒体或 Gmail 帐户的凭据窃取。

执行诈骗的人工智能代理使用支持语音的 ChatGPT-4o 自动化工具来导航页面、输入数据并管理双因素身份验证代码和特定的诈骗相关指令。

由于 GPT-4o 有时会拒绝处理凭据等敏感数据，因此研究人员使用简单的提示越狱技术来绕过这些保护。

研究人员没有展示真实的人，而是展示了他们如何与人工智能代理手动交互，模拟容易上当受骗的受害者的角色，使用美国银行等真实网站来确认成功的交易。

将代理部署在常见诈骗的子集上。通过手动与语音代理交互来模拟诈骗，扮演轻信受害者的角色。为了确定是否成功，需手动确认最终状态是否在真实的应用程序/网站上实现。例如，使用美国银行进行银行转账诈骗，并确认资金确实被转移。

总体而言，成功率范围为 20-60%，每次尝试最多需要 26 个浏览器操作，在最复杂的场景中持续长达 3 分钟。

银行转账和冒充国税局代理，大多数失败是由转录错误或复杂的网站导航要求引起的。然而，Gmail 的凭据盗窃成功率为 60%，而 Instagram 的加密传输和凭据盗窃只有 40% 的成功率。

至于成本，研究人员指出，实施这些骗局的成本相对较低，每个成功案例的平均成本为 0.75 美元。银行转账诈骗更为复杂，费用为 2.51 美元。尽管明显较高，但与此类骗局的潜在利润相比，这仍然非常低。

![type-success.webp.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20241104/1730711950920871.png "1730710349159172.png")

诈骗类型和成功率

**OpenAI 的回应**

OpenAI 告诉媒体，其最新模型 o1（目前处于预览版）支持“高级推理”，可以更好地防御此类滥用。

OpenAI 发言人表示：“我们不断地让 ChatGPT 能够更好地阻止故意欺骗它的尝试，同时又不会失去其有用性或创造力。最新的 o1 推理模型是我们迄今为止最有能力、最安全的模型，在抵制故意生成不安全内容的尝试方面明显优于以前的模型。”

OpenAI 还指出，UIUC 的此类论文帮助他们使 ChatGPT 更好地阻止恶意使用，并且他们始终研究的是如何提高其稳健性。

目前，GPT-4o 已经纳入了许多防止滥用的措施，包括将语音生成限制为一组预先批准的语音，以防止冒充。

根据 OpenAI 的越狱安全评估，o1-preview 的得分明显更高，该评估衡量模型在应对对抗性提示时抵抗生成不安全内容的能力，得分为 84%，而 GPT-4o 得分为 22%。当使用一组新的、更严格的安全评估进行测试时，o1-preview 分数明显更高，分别为 93% 和 GPT-4o 的 71%。

威胁者使用其他限制较少的语音聊天机器人的风险仍然存在，此类研究正凸显了这些新工具可能造成的巨大损害。

文章翻译自强：https://www.bleepingcomputer.com/news/security/chatgpt-4o-can-be-used-for-autonomous-voice-based-scams/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WswbQHBK)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)