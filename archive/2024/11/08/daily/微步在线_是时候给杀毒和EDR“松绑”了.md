---
title: 是时候给杀毒和EDR“松绑”了
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650182521&idx=1&sn=9b0730f7f820bf4782910456741fa7c8&chksm=f44868c5c33fe1d3a20e7754031a9985a96241de3910ef4ebf38d12aabf7a365edf83e1336cb&scene=58&subscene=0#rd
source: 微步在线
date: 2024-11-08
fetch_date: 2025-10-06T19:20:20.973671
---

# 是时候给杀毒和EDR“松绑”了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTTLnPdvCslg6ocJG8MZewjmwVkibvyEltc6wqLGsDLoRYoSuV75r2ibOxpPV3MUk9HPwmyGqKfOSfg/0?wx_fmt=jpeg)

# 是时候给杀毒和EDR“松绑”了

原创

ThreatBook

微步在线

![](https://mmbiz.qpic.cn/mmbiz_gif/Yv6ic9zgr5hRYwmkFFVSsK0fQGJBGqwl6iaBoFgqTpPricWCuX7uIb4Rj7eibLo3ibOiaOtqo7vXEnibKhxuInrceOoibg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

“All in One”部署还是异构部署？使用终端安全软件时，总是面临这样的选择。不过，投资界有一句名言：“不要将鸡蛋放在同一个篮子里。”

类似的，在能力“All in One”的同时，也意味着风险“All in One”。相比之下，将杀毒软件与EDR异构部署，不仅可以分摊失陷的风险，还可以覆盖更多的恶意样本和攻击行为。

**杀毒软件“中毒”了**

前不久，微步终端安全管理平台 OneSEC 捕获到了一起恶意文件投递事件。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTTLnPdvCslg6ocJG8MZewjukvCLric0IwBxIl0eXb2JcJ6q8PUicKpHu7AbJhbxSfiaR5jUw658Dm7Q/640?wx_fmt=png&from=appmsg)

告警信息显示，该恶意文件执行了一系列恶意行为：包括探测机器信息、创建其他恶意文件、搜集浏览器访问凭据并打包回传等。但有趣的是：

1. 恶意文件是由杀毒软件创建并执行的，就像是杀毒软件感染了病毒一样，甚至一度怀疑是误报；
2. 在检测到恶意文件活动前，杀毒软件管理员账户出现异常登录并上传了恶意文件，但排查发现此次登录用户并非管理员本人。

综合上述两点判断，有外部攻击者冒用了杀毒软件管理员账户，并利用软件分发功能投递恶意文件。

**杀毒软件失陷有着更大的危害**

事实上，杀毒软件失陷的案例并不多见。与之相比，钓鱼才是更为直接和普遍使用的投毒方式。

不过，一旦杀毒软件失陷，危害程度也会更大。

其一，与域控等其他集权系统类似，杀毒软件拥有较高的管控权限，攻击者可以同时向同一网段内所有终端分发恶意软件，而不用一台台横移；

其二，攻击者可以利用管理员权限设置白名单或者白路径进行投毒，从根本上无视杀毒软件的查杀能力，这就相当于釜底抽薪。

微步终端安全检测团队判断，随着用户安全意识增强，攻击者除了使用更加精细化的钓鱼攻击方式，借助杀毒软件投毒也不失为一个新的选择。

**EDR是终端高级威胁对抗的核心**

于是一个新问题就产生了：杀毒软件自身应该怎么防范被攻击者利用？

从此次杀毒软件投毒事件可以看出，加强提高安全意识、收敛攻击面的的重要性，包括保护登录凭据、设置多因素认证、限制管理员账户权限等，这是降低失陷概率的关键举措。

**在此基础上，基于EDR的终端高级威胁对抗能力至关重要**。当攻击者利用杀毒软件投毒时，大概率会使用具备免杀能力的恶意文件，EDR可以第一时间检出杀毒软件无法发现的恶意行为。

以本次事件中的恶意样本为例。

样本会通过API将内存属性从RW修改为RX属性，避免触发安全软件内存检查。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTTLnPdvCslg6ocJG8MZewjHCesfC5ibtPZb9KpibFRWu2RmDlyqVZWiaFmmnib63ORiaa1QWADwM53RmQ/640?wx_fmt=png&from=appmsg)

截至目前，VT平台多引擎检出率（6/75）也并不高。即便攻击者没有加白或者失陷的是其他集权系统，杀毒软件也大概率不会产生告警。

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTTLnPdvCslg6ocJG8MZewjeoc3EpITPgWul0VXYWCXXd8ibZBUOds4ib1anQ73iaJO3C9FahLKibOfLw/640?wx_fmt=png&from=appmsg)

相比之下，OneSEC EDR检测到了多个恶意行为，并且通过关联分析定位到了事件的执行源头——杀毒软件，进而帮助安全运营人员发现了本次杀毒软件失陷事件。

从杀毒软件出现异常登录，到完成初步的事件调查，仅耗时不到两个小时。

**异构EDR是更加安全的选择**

需要注意的是，即便是集成了杀毒、桌管、EDR等多项能力的“All in One”终端安全软件，也并不能很好地解决杀毒软件失陷难题。投资界有一句规避风险的至理名言：不要将鸡蛋放在同一个篮子里。与之类似，能力“All in One”的同时，也意味着风险“All in One”。

**第一，同构的安全软件往往具备相似的架构和基础组件，很有可能会受同一安全风险影响**，例如默认弱口令、身份验证绕过、源代码漏洞等，容易被同样的方式全部击穿。

**第二，“All in One”软件一旦失陷，就意味着终端安全能力全部被攻击者接管**，不会对自己加白的文件产生告警，就像医者不能自医一样。相比之下，多个异构安全软件同时失陷的可能性要低得多，相互之间能起到一定的相互制衡的作用。

**第三，除了在应对自身失陷风险之外，同构的杀毒软件和EDR还有着相同的检测能力局限**，这主要是由恶意样本和行为的积累决定的。

众所周知，杀毒软件的查杀能力主要取决于病毒库积累的签名数量，尽管EDR检测并不依赖特定的文件签名，但样本的积累却能够帮助EDR覆盖更多的攻击行为，进而更新检测模型、检测规则。

对于同构的杀毒软件和EDR而言，当面对使用了特定未知恶意行为的恶意样本时，可能会同时出现漏报。

这就好比一个从未见过的人、做出了一系列从未见过的动作，无论是根据样貌特征还是行为特征，都很难判定这个人到底是好是坏。而异构的EDR和杀毒软件，可以覆盖更多的样本和恶意行为。

随着终端对抗强度不断升级，EDR与杀毒软件的异构部署，无疑是一个更为安全的选择。

· END ·

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hSA5A4iaspRVClFku4KVwkOUriclTaohLibE2oQKMTrQ8hvSFFHevq88eibd7mstuZbeNLm5U1tPJT3xQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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