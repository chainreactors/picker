---
title: Lenovo 机器上的 AppLocker 绕过: MFGSTAT.zip 的离奇案例
url: https://mp.weixin.qq.com/s/OaEJZkUELJSOM7TEASVUCA
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:41.095577
---

# Lenovo 机器上的 AppLocker 绕过: MFGSTAT.zip 的离奇案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hoiaQy7WhTCOTqPUDFicfCYa2gB7wg6hlSyGzg6NkYDXdibYQwsmJiblRdxeJ9gs2pvaQ9EBY1HV0pUx3Ynicz0EacA/0?wx_fmt=jpeg)

# Lenovo 机器上的 AppLocker 绕过: MFGSTAT.zip 的离奇案例

ODDVAR MOE
ODDVAR MOE

securitainment

![]()

在小说阅读器中沉浸阅读

这篇博文记录了我在 Lenovo 机器上的一个小发现：`C:\Windows`目录下存在一个可写文件。最初我以为只有少数几款 Lenovo 机型受影响，但后来发现这个问题似乎波及所有型号。由于它可以被利用来绕过 AppLocker，我决定把内容写在这里，而不是发在 TrustedSec 博客上——因为我的个人博客主要围绕 AppLocker 展开。

## 问题

当我运行 accesschk 脚本 时，发现该文件对任何已认证用户都是可写的。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOTqPUDFicfCYa2gB7wg6hlSRV7RmBDUYSNAZosuBFcJUs2cq7hthBF45yxxSuRmyiakSPu2dwrPEqA/640?wx_fmt=png&from=appmsg)

随后我在 Explorer 中查看了 ACL 以再次确认。

![](https://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOTqPUDFicfCYa2gB7wg6hlSBmnbfKVL3rbicu2wd0j9IBBxeCvIanXODeD80pfFZxZcr0IsETb2Xyg/640?wx_fmt=png&from=appmsg)

这进一步证实：标准已认证用户既能写入也能执行该文件。如果你的环境中部署了 AppLocker 默认规则，它会允许执行 **C:Windows**目录下的任何内容；因此 **mfgstat.zip**就成了问题，因为标准用户可以利用它进行攻击。要将其作为绕过手段，用户需要将某个二进制文件的内容写入到 Alternate Data Stream (ADS) 中，然后执行该 ADS。我还没能直接覆盖这个 zip 文件（也许可以）。关于如何添加 ADS 以及执行 ADS 的各种方法，可以参考这里。在这个示例中，我选择执行 Sysinternals 的 `autoruns.exe`。我先把 `autoruns.exe`放到 **c:temp**，然后使用以下命令将它作为 ADS 写入 **mfgstat.zip**：

```
type c:\temp\autoruns.exe > c:\windows\mfgstat.zip:this
```

成功添加后，我使用 **Appvlp.exe**（lolbas 详情见链接）执行它，命令如下：

```
"C:\Program Files (x86)\Microsoft Office\root\Client\appvlp.exe" c:\Windows\mfgstat.zip:this
```

为了更直观，我录制了一段简短的演示视频。

https://www.youtube.com/embed/uIQIMEvwlh4

## 经过

我最早是在 2019 年的一台 Lenovo 机器上发现这个问题的，当时也在 Twitter/X 上发过：https://x.com/Oddvarmoe/status/1126473466235035650。那时候我以为这只是我那台 Lenovo X1 Extreme 的个例；但在 2025 年我在新买的 Lenovo 机器上复查时，惊讶地发现同样的问题依然存在（https://x.com/Oddvarmoe/status/1882026713397522873）。这一次我决定给 Lenovo PSIRT 发邮件，看看他们是否会修复。对方回复很快，但他们选择不发布修复补丁，而是给出了一份移除指南。从企业角度看，这个决定也许可以理解：多数公司都会自行部署操作系统，而不是依赖 Lenovo 出厂预装的系统。使用公司标准镜像重新部署操作系统会移除这个文件，因为它仅存在于 Lenovo 随机出厂的默认系统镜像中。

## 修复

Lenovo 在这里提供了修复指南：https://support.lenovo.com/us/en/product\_security/HT517812。指南的核心很简单：使用文中说明的三种方法之一删除 `C:\Windows\MFGSTAT.zip`。如果你在企业环境中，也可以利用 Group Policy Preferences、SCCM 或其他工具来移除该文件。

## 结论

我的结论是：在部署或已经部署 AppLocker 时，所有人都应该检查自己的文件系统。这类细小但关键的点非常容易被忽略。如果你对 AppLocker 更感兴趣，我之前做过一个 webinar，值得一看。希望这篇文章对你有帮助。

第 1 部分：https://www.youtube.com/embed/582pdWRbhpw

第 2 部分：https://www.youtube.com/embed/JtsgvOLhLJs

---

> APPLOCKER BYPASS ON LENOVO MACHINES – THE CURIOUS CASE OF MFGSTAT.ZIP
>
> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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