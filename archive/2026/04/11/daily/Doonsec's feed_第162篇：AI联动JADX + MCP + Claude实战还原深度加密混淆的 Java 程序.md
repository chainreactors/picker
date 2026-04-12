---
title: 第162篇：AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序
url: https://mp.weixin.qq.com/s/ZUCA_i0U45WJ4palHaMBjw
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:42:20.278426
---

# 第162篇：AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2Y8QlzyOaWhBya9ylq7Dz5aMp42ezk3BU2AzSsbiaHn3NcUD7HeP7p5DSbKMsBQTKtdK4fYCcPA8WzqNL8Or6dIJZjJpvyTdZGo/0?wx_fmt=jpeg)

# 第162篇：AI联动JADX + MCP + Claude实战还原深度加密混淆的 Java 程序

原创

abc123info
abc123info

希潭实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450ATcz6jUJnFNeOxRzVZ9Lbc0INLwTJTZT1GaNutZrfDn6csvjBoS2ox0efLUEexXqPEcVbYfbLo8w/640?wx_fmt=png)

Part1 前言

大家好，我是ABC\_123。前面几篇文章我讲解了XGhost机器学习分类法、卷积神经网络识别验证码、AI的MCP等，今天我们继续研究AI在解Java混淆方面的不可替代的作用。ABC\_123有过几次处理加密混淆内存马的经验，也搞过加密混淆的java程序的逆向去看看别人的代码思路，但每一次对抗加密混淆都很烧脑，但是现在AI的MCP出来，我试了一下AI联动JADX，一个深度加密混淆的Java程序，被还原得让人难以置信。

![](https://mmbiz.qpic.cn/mmbiz_png/uPOMOKjLe2aSrrFtI5259NPOqfK7yzKpB8TQVkJFclAY9Ulom70TA8cKybkkhHVh4DVjB7edf4vsMBwvMtSWTgS7lKtib6YvLKmBYzDlhV5g/640?wx_fmt=png&from=appmsg)

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

1.  AI联动JADX和MCP可以快速还原深度加密混淆的Java代码，大幅提升可读性。

2.  欢迎大家扫码加入知识星球，一起学习进步。

![](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2YAHvuDg7rlIK2g84Y2mmKxXxMib2ac8xLzeXrMuSIc1T95hsjfKK58Hia7KW59tPIuSib9pg3sOTy1Thrj53cqKzKqSFuicAiajUMI/640?wx_fmt=jpeg&from=appmsg)

知识星球分为以下几个板块：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2bfdTZmTSibnZNTJvQgQvCEFTc2nqSTBCd1vHGaAgThwDHcZfKibiaMP2KD1omzQ5DHZqLy7UnGs4fMqicOgRmBVr48n9WgfIqeZmU/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=19)

知识星球的每一篇PDF文档、PPT文档都细心整理，配有3到9张关键截图。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2asOuDN4oUOteG005XfBSKeHicvaPJVKv679ywAYOaeicyLNYk2y2JotQS6jnxzPrOPzFmxk6qLzpGN9MxkBxiacjjQ7pV40kUZhg/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)

知识星球的每一个工具都是精心筛选，都附带有实测评价及使用说明。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/uPOMOKjLe2ZWpO3Ao3P5kIoiaUiamEfZ7WbYBZzgR5pRgWgFMMRUCjvfuxibNEeIfIftokxL0QtH2rhR903lYbn5xMCUv2QVticXhuX6gico0gXw/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)

欢迎大家扫码加入知识星球，一起学习进步！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/uPOMOKjLe2bgaavcGNZASQ8d78cQDOVlaO8Fgg2w2zTrDNjuECzZ1FQeic1kbY4RPjcbNFCAysuCWJPlp0A22JRl84qz5MOdjhj5tD0ZHfcM/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16)

![图片](https://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450A5qqg2iaK6KIYYR8y6pF5Rh3JHDibOKOop204nXz618iawdRb8dABicMPtHb2PkJE8x6koJO5HyuwZJQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

**公众号专注于网络安全技术分享，包括APT事件分析、红队攻防、蓝队分析、渗透测试、代码审计等，每周一篇，99%原创，敬请关注。**

**Contact me: 0day123abc#gmail.com**

**OR 2332887682#qq.com**

**(replace # with @)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

希潭实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/OAz0RNU450BdnvpJibA3tSJeDb0OXXOT6kIw73PgKhWOibfMUWNHQrU1khmjEj6WmWUBLTzIurHUxfJScUyEcTicQ/0?wx_fmt=png)

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