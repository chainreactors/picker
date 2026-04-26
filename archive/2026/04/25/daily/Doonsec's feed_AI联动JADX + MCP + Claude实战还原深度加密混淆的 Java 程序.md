---
title: AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序
url: https://mp.weixin.qq.com/s/LW3nIdeJmTwhzunwDFyFQA
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:54:26.783835
---

# AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2Y8QlzyOaWhBya9ylq7Dz5aMp42ezk3BU2AzSsbiaHn3NcUD7HeP7p5DSbKMsBQTKtdK4fYCcPA8WzqNL8Or6dIJZjJpvyTdZGo/0?wx_fmt=jpeg)

# AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于希潭实验室
，作者abc123info

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fmEcY2bcaelEq3UFVKWcPYSM5dibWwP6KNJRapia8tbPQ/0)

**希潭实验室**
.

ABC\_123，2008年入行网络安全，希潭实验室创始人，某工业大学客座教授，某部委授课讲师、省级专家裁判，省评标专家。专注于安全咨询、网络安全培训、APT技战法分析、代码审计、渗透测试。

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

Part1 前言

今天我们继续研究AI在解Java混淆方面的不可替代的作用。有过几次处理加密混淆内存马的经验，也搞过加密混淆的java程序的逆向去看看别人的代码思路，但每一次对抗加密混淆都很烧脑，但是现在AI的MCP出来，我试了一下AI联动JADX，一个深度加密混淆的Java程序，被还原得让人难以置信。

Part2 技术研究过程

* ## 配置AI+MCP+JADX环境

## https://github.com/zinja-coder/jadx-ai-mcp

打开jadx-gui 1.5最新版本，点击安装插件，载入jadx-ai-mcp-6.3.0.jar。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2aZRiaSunvkzL9QiaavVQgcXNoaeOBW4Gund63A64llFOLplw0CoibNEEdIicsXn0cLguic2Wnzf8HejU4lZbFt5kMBTuTE1fj533D4/640?wx_fmt=png&from=appmsg)

下载 `jadx-mcp-server` 压缩包并完成解压，进入项目目录后，安装 Python 所需的依赖插件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZlFf3nK3XP5datLN0UJzFicCjG9r8jjv20vXbrBIbmIf6Mp6E4n2ySjpBBt4Je5b5icGjdODP8XRXibaVhdwibG6wKUs8apjUzt5I/640?wx_fmt=png&from=appmsg)

接下来进行 Claude MCP 配置，需要在项目中生成 `.mcp.json` 和 `settings.local.json` 两个配置文件，分别用于声明 MCP 服务信息及本地运行配置。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bdtjGBh4XmVaCopWdP0UhWaBn0CU4hSic1GYXq4hBrkEOzMKAuPvduCqOiasgiaI5AaqzJouIO7AnzP451cjg6wWbfwt3rFAztZA/640?wx_fmt=png&from=appmsg)

```
{    "mcpServers": {        "jadx-mcp-server": {            "command": "python",            "args": [                "D:\\jadx-mcp-server-6.3.0\jadx_mcp_server.py"            ]        }    }}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bumruzdfatQ4jQAm8aERbcgQ93WVORk5JP45iaXHju9uuw5ZFxRnHfTNgFEWvEvjMta2ToFrfMdjSLjAWb14rmRjfvuofWIb1I/640?wx_fmt=png&from=appmsg)

* ## 开始逆向加密混淆过程

这里我们选取一个早期版本的 Burp Suite 作为样本进行测试，也是为了研究下Burp Suite的发包模块的实现，这个模块非常稳定，有些特定的发包只有它能实现。使用 JADX 打开后可以发现，目标程序的包名、类名和变量名被大量替换为 `if`、`else`、`for`、`static`、`throw` 等 Java 关键字。经过反编译后，这些代码在导入 IDEA 时会触发大量语法错误，既无法直接编译，也严重破坏了代码可读性，并且难以阅读理解。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2ZR96s5AqvVdt1QzMSvc05YdV9iaX2LG70oplRP2vibGZuJMLKDJib5FsurlpuVH9tcudRD7JG5bkzTPJsgrK28zqDeVo4doupX2I/640?wx_fmt=png&from=appmsg)

接下来，我们尝试使用 JADX + MCP + Claude 的联动方案进行分析，首先给出本次实验所使用的提示词如下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bVfQ4ibweeibjiaZAPTuypADGxfs1YibMBpPGWjeJReev2vRLiab5RTM6UDtz1xIKkib3XdlHKdyOx2N84g7l5icxr48j2R9Po6juZ2Q/640?wx_fmt=png&from=appmsg)

代码进行了加密混淆，类名都被替换成了关键字。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2Z3OTpH0exYzz9nicQmvtN5kFRRVAaLibOT20GmxKUNc1IfbjwHtKt5UvWgPA4yrqIbXtMHcqfGYOoLyu1htdKSODqjQ0lCxak10/640?wx_fmt=png&from=appmsg)

调用了JADX的重命名功能来改善代码的可读性：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2YFyvYjxtR5w8WNRyVibibYicqkJazdszKGfic6H8lRwBPnUMXB46dgTaspXMAcxfstxb7Itbzyk0l0Jv7lRNEG0sDaCktJzCdGjzs/640?wx_fmt=png&from=appmsg)

已完成的重命名如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2bU5H1CwcS02AHe1g0Iwf6ZQIGrTU1Vyqm1EWHib3JYedCZITcGiacLJfWiccB3DBAkf2kX6aJv1f1geyvhITBNn19UTdQfdHCK0c/640?wx_fmt=png&from=appmsg)

接下来继续对RepeaterUI这个类进行反混淆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2a0qsyicBic5icR3iaZndYbfp17HkLMWaKUJpHuK7rlHDCGZ1f4T2EX6zFzkTias5VjhjtjZE3zgG7ViaaibdCdHZl8Ag5xyZSjJzad5I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2a0tmmq0ic6txiaYCZic6ibfX9dfCLvJGVibTa0NT1Mx8Gnz0C3aZd9iboDDwPJIgAKlz8wXzf4p0dBNmZLiaTr7h12WUkcwmhPoCPtHY/640?wx_fmt=png&from=appmsg)

反混淆结果如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bqajCLjQtHZzCd7F1m1vUhlfLyoiaKeXr6pd72gq1lLmx5vQmicL90sh8RkRAroicCJMJJyz7cnTO8Uo3viaPypIjUh99TTAWRGAI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ayRLX2w3apOOA5zHNjMIDvsdZXnUxCEU1y8u7AxSqofNpVz0gBozicDTibicGvMwX2gib1URSExQK7U4Tzl4Ct5muic25lSm9h6mDM/640?wx_fmt=png&from=appmsg)

考虑到 Burp Suite 的发包功能很可能依赖底层 Socket 模块实现，接下来我们进一步提问，定位其发包模块所在位置，分析关键实现流程，并对相关代码进行反混淆还原。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2btOuAibnaFkeOk13jsfGMxjqKDmk3np2oc5bibgiaTj8GObpuWhjiaxhcbD9IYicWRQicU86fiboQicNHm00A7PBfbfq4T2a96l6Tmsh4/640?wx_fmt=png&from=appmsg)

到这一步，如下图所示，burpsuite的反编译结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2ZZybUIWgBeMRicx094bOlvuIQSib61H9gIetNdtm0dia2T49pzfLiceBiboUtQcQXamdj9iavBzonhpO2TD7Esnomd6BVtYiaID4xLeY/640?wx_fmt=png&from=appmsg)

如下所示，可以看到原本加密混淆的代码，已经被还原的可读性非常高了，令人惊叹！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/uPOMOKjLe2bpXkH7eR6Oiadv1XZ3Wg9w4bwwhIakUmpfq0bHtXPwKkSibiaojQK7Wl15EnQZoHtrfyQgqcLibFL2W49LgOh3UXRdqhQCYTDFD9M/640?wx_fmt=png&from=appmsg)

Part3 总结

AI联动JADX和MCP可以快速还原深度加密混淆的Java代码，大幅提升可读性。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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