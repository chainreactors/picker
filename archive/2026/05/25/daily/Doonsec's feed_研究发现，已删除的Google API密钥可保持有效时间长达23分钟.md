---
title: 研究发现，已删除的Google API密钥可保持有效时间长达23分钟
url: https://mp.weixin.qq.com/s/5ZdjKzVbQ0zkq5iXN9qjcA
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:01:01.631772
---

# 研究发现，已删除的Google API密钥可保持有效时间长达23分钟

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oPZcPicUADs8TtCYSdTVEPhl3C3lF1FIBoKVmEwySptZ4KElhYacfY618dL7Sc25a0NrZK3QURSicjx7KLd3kZyUjHiaDF6VWoUuNFxQTCEP84/0?wx_fmt=jpeg)

# 研究发现，已删除的Google API密钥可保持有效时间长达23分钟

HackSee安全团队
HackSee安全团队

HackSee安全生活

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

网络安全公司（Aikido Security）进行的一项新研究表明，被删除的谷歌API密钥仍然有效，并且可以在删除后的23分钟内继续成功进行身份验证。结果是在两天内进行了10次对照试验以测量延迟后得到的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oPZcPicUADs9ffEzGWiapv1ia6s6G8QdthHPTadIcXg4QpVbrP2mVqZQ9OIbjQKKEib0S3ksn1UETN4QlUamdQiaQJiaAwVL9OBlfDc2diaa5hHBYc/640?wx_fmt=png&from=appmsg)

### **重要发现**

API密钥是一串数据，用于验证软件应用程序之间的请求。根据研究人员的说法，谷歌云平台（GCP）控制台显示密钥已被立即删除。然而，测试表明，这些按键实际上平均需要16分钟才能完全停止工作，最长的延迟时间接近23分钟。

在此期间，持有泄漏密钥的威胁参与者保留对项目上任何已启用api的完全访问权。这使得他们可以窃取缓存的对话并转储上传到双子座的文件。他们还可以访问BigQuery数据和Maps api。

### **为什么会出现这个问题？**

在今天发布并与Hackread.com独家分享的博客文章中，研究人员解释说，这个问题的发生是因为谷歌身份验证基础设施的最终一致性。在这种分布式系统模型中，更新在全局服务器上逐渐传播，而不是一次全部传播。

这意味着当你删除一个密钥时，消息不会立即到达世界各地的每个谷歌服务器，这给了黑客一个暂时的空隙，可以在尚未更新的服务器上使用密钥。研究人员edward Agavriloae去年在AWS上演示了这类相同的基础设施问题，尽管AWS的撤销窗口只有4秒。

### **跟踪和基础设施差异**

这种攻击方法依赖于黑客连续发送经过身份验证的请求，在同步之前通过谷歌的全球身份验证服务器进行旋转。对不同GCP区域的测试显示出不同的区域差异。在删除后的第一分钟，亚洲-东南亚1地区的虚拟机的成功率中值为22%，而美国-东部1和欧洲-西部1的请求成功率均为49%。

对于事件响应团队来说，在攻击期间跟踪事件的时间轴因GCP流量凭据图而变得复杂。当密钥被删除时，攻击者的任何进一步身份验证尝试都被捆绑到标记为。这使得很难确定攻击者试图滥用的具体凭证。

研究人员指出，谷歌已经解决了其他凭证类型的更快传播问题。例如，谷歌服务账户密钥大约在5秒内撤销，而较新的gemini格式密钥（使用aq前缀）大约需要1分钟。

Aikido Security向b谷歌报告了这些发现，但该公司以“不需要修复”的理由关闭了报告，并表示传播延迟是系统的已知属性，而不是安全漏洞。因此，研究人员建议将谷歌API密钥删除视为一个30分钟的操作，并在该窗口内监视GCP控制台的有效身份验证。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

HackSee安全生活

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/M8pOVgDSPVI7jF9IeH2p6icHIDM6ZMlreAbOiciaoho809sdhhiaE7t8DRlhgSg3h1s7k7eDlfX32AfCLXUnLwXYsw/0?wx_fmt=png)

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