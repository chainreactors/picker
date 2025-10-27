---
title: 【安全圈】可绕过安全防护！EDR Silencer红队工具遭黑客利用
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065278&idx=3&sn=bc5b1bf29ad416c8769d53bc5ad0a5a1&chksm=f36e61bec419e8a8507b9227e71141e2c883e704928a1d03fbf4d674f0462819da89fa7f1db7&scene=58&subscene=0#rd
source: 安全圈
date: 2024-10-17
fetch_date: 2025-10-06T18:52:24.309031
---

# 【安全圈】可绕过安全防护！EDR Silencer红队工具遭黑客利用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4U2H20GakzRKxPCG4k9vH2OakpOplEGkR6rzLZVD4XYqRfOkX2DlMzA/0?wx_fmt=jpeg)

# 【安全圈】可绕过安全防护！EDR Silencer红队工具遭黑客利用

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

网络攻击

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4YAToqxIZ5094NNvXncCfv5gYnBMDs9ia9Ardp5DX1r4fCKwd654rzAg/640?wx_fmt=jpeg&from=appmsg)

近日，研究人员在恶意事件中观察到一种名为 EDRSilencer 的红队操作工具。EDRSilencer 识别安全工具后会将其向管理控制台发出的警报变更为静音状态。

网络安全公司 Trend Micro 的研究人员说，攻击者正试图在攻击中整合 EDRSilencer，以逃避检测。

## 被“静音”的EDR 产品

端点检测和响应（EDR）工具是监控和保护设备免受网络威胁的安全解决方案。

它们使用先进的分析技术和不断更新的情报来识别已知和新的威胁，并自动做出响应，同时向防御者发送有关威胁来源、影响和传播的详细报告。

EDRSilencer 是受 MdSec NightHawk FireBlock（一种专有的笔试工具）启发而开发的开源工具，可检测运行中的 EDR 进程，并使用 Windows 过滤平台（WFP）监控、阻止或修改 IPv4 和 IPv6 通信协议的网络流量。

WFP 通常用于防火墙、杀毒软件和其他安全解决方案等安全产品中，平台中设置的过滤器具有持久性。

通过自定义规则，攻击者可以破坏 EDR 工具与其管理服务器之间的持续数据交换，从而阻止警报和详细遥测报告的发送。

在最新版本中，EDRSilencer 可检测并阻止 16 种现代 EDR 工具，包括：

* 微软卫士
* SentinelOne
* FortiEDR
* Palo Alto Networks Traps/Cortex XDR
* 思科安全端点（前 AMP）
* ElasticEDR
* Carbon Black EDR
* 趋势科技 Apex One

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4LxywKibdGs9JDS1ZZic24gDG4MCDevwsMRlYpm0qkOsTWgYNBHGnt6og/640?wx_fmt=jpeg&from=appmsg)

阻止硬编码可执行文件的传播，来源：趋势科技

趋势科技对 EDRSilencer 的测试表明，一些受影响的 EDR 工具可能仍能发送报告，原因是它们的一个或多个可执行文件未列入红队工具的硬编码列表。

不过，EDRSilencer 允许攻击者通过提供文件路径为特定进程添加过滤器，因此可以扩展目标进程列表以涵盖各种安全工具。

趋势科技在报告中解释说：在识别并阻止未列入硬编码列表的其他进程后，EDR 工具未能发送日志，这证实了该工具的有效性。

研究人员说：这使得恶意软件或其他恶意活动仍未被发现，增加了在未被发现或干预的情况下成功攻击的可能性。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4cBic2UO1dCjia1q7PElknRutJP3gm6iav8A8iadn6H66n4CXnGC7yA7wew/640?wx_fmt=jpeg&from=appmsg)

EDRSilencer 攻击链，来源：趋势科技

趋势科技针对 EDRSilencer 的解决方案是将该工具作为恶意软件进行检测，在攻击者禁用安全工具之前阻止它。

此外，研究人员建议实施多层次的安全控制，以隔离关键系统并创建冗余，使用提供行为分析和异常检测的安全解决方案，在网络上寻找入侵迹象，并应用最小特权原则。

参考来源：EDRSilencer red team tool used in attacks to bypass security (bleepingcomputer.com)

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt4CXVmRwO0HzswbGreUgwkHmAEC93T7DmNgBK449saQaiaKc0tNY9JJ2Q/640?wx_fmt=jpeg)[【安全圈】揭秘美国政府机构实施的网络间谍和虚假信息行动](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=1&sn=085b852f0b04266b8ba28e0b651a0bf4&chksm=f36e61a8c419e8be214d26a2f67be192a532f1876d65421950e658ca8c9951daa71cd8d375cf&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XvnzjMsl2uqO3khdTVNxlYGBrTle1mMLwCD83I7ZYFicUuK2IctqgOlaCibU2XZoHA3Aw9GxHFM0Gkmzw41fkrWA/640?wx_fmt=other)[【安全圈】乡镇公交车系统信息泄露漏洞复现](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=2&sn=980220c27c207e4156417e7e6a6c2657&chksm=f36e61a8c419e8beda8644a1da99eb23c6b4b5bc49fe59673a854f6c38bdd77c924120e00ea7&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljhP5K1N0lvmFx8KzoW6LVPBWOsH7O11ryx7HIN1yiactgrH6lGpB0q0pZ0X18dibMX9R3BhZs4sicHw/640?wx_fmt=jpeg)[【安全圈】TrickMo 安卓银行木马新变种利用虚假锁屏窃取密码](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=3&sn=db9a05a7cb472260591425ee387b49ef&chksm=f36e61a8c419e8be43d4f3953b52b2ac31136bd4bd05c846f86a8083c861da3244bea490f740&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljqzribiaIKEDg4u7Ma3veMt45eUsqWTUVGEG69AnDyJzSBKdkic5jNGZYcJ5sQnyXuLwE6lFdKofjCA/640?wx_fmt=jpeg)[【安全圈】思科再遭数据泄露，数家大厂跟着遭殃](http://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652065256&idx=4&sn=7ab2859ef0f27a3bc8c16d699d7af1e8&chksm=f36e61a8c419e8bed1286695e270c19e4657f32c0a8ad0ff3c1f3e364bd783d3bbd6a8bdfab6&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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