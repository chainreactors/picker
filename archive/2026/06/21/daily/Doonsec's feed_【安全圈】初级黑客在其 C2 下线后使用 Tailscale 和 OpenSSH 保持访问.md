---
title: 【安全圈】初级黑客在其 C2 下线后使用 Tailscale 和 OpenSSH 保持访问
url: https://mp.weixin.qq.com/s/oKEmicTvF5a8stxb8Xq2lQ
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:15:10.347103
---

# 【安全圈】初级黑客在其 C2 下线后使用 Tailscale 和 OpenSSH 保持访问

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sbq02iadgfyEzkRUWvLAnUzwlVGrO8tTbL3tUFhE7aXA5ggxTqQmEwPD70OnfT5TP9duFuhGnlBwBDzdMtdVzyNqMhnDrxjN55ehcLBRADe4/0?wx_fmt=jpeg)

# 【安全圈】初级黑客在其 C2 下线后使用 Tailscale 和 OpenSSH 保持访问

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

黑客

**一名讲法语的攻击者入侵了一家法国小型汽车企业，植入了键盘记录器，并窃取了银行和电子邮件凭证。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyEaGBnA3oDmTwAFgFIRe5zyOic57bQ9F7RzzC0q8BZN7RibAu2WS0yIPHIkuCiaicIvAjQB3MzhZibqCfmSt4Bp5kd3f2iazQyUpaa0I/640?wx_fmt=png&from=appmsg)

这都是常规操作，直到他在最后阶段做了一件事。

在他的命令与控制服务器下线之前，他在受害者机器上安装了 OpenSSH 和 Tailscale，建立了一条完全不经过 C2 的返回路径。当 Havoc 服务器第二天离线时，他的访问权限并未中断。18 天后，C2 重新上线，他的代理自动重新连接，他继续行动。

Cato Networks 在操作者将其 SSH 密钥和分步操作手册留在开放的存储桶中后，逐条命令捕获了整个操作，33 天内共 339 条命令。Cato CTRL 研究员 Vitaly Simonovich 周二发布的报告，是从操作者键盘而非取证残留物角度观察入侵的罕见视角。

研究人员的教训很直白：如果攻击者已经建立了独立的通道，将 C2 服务器下线并非有效的补救措施。

该行为者，代号 "Poisson"，并非 APT。研究人员描述其是一名初级操作者，活动时间看起来像学校作息——欧洲中部时间下午 3 点后活跃，中午有长时间间隔，全部运行在免费层级工具上：DuckDNS、Backblaze B2 和柏林一台便宜的 IONOS VPS。他的技术手段很粗糙。

他五次泄露了自己的主目录，以他自己的代号命名存储桶，并在键盘记录器包内留下了一个他自己的按键测试文件（重复输入的内容）。他尝试的事情大约有一半失败了。但他仍然入侵了四台机器。

**攻击链**

恶意软件几乎完全在内存中运行。一个带有沙箱规避延迟的 VBScript stager 解密了一个 PowerShell 加载器，该加载器下载了一个 .NET 加载器，运行 Havoc 的 Demon 代理而无需将植入程序写入磁盘。为了提权，他使用了 Start-Process -Verb RunAs，这不是静默 UAC 绕过。它会弹出 Windows 同意提示并等待有人点击“是”。在一台受害者机器上，它花了两天时间尝试了十几次。

之后是巩固访问：一个在每次登录时以最高权限运行的计划任务、注入到 Explorer.exe 中的 shellcode，以及一个作为备用通道的自定义构建 RustDesk。凭证抓取器是一个 70 行的 Python 键盘记录器，将按键记录写入本地文件，没有 beacon 也没有外泄服务器。Poisson 只是登录进去，手动抓取文件，并运行 powercfg 以防止机器休眠，从而确保数据收集永不间断。

**关键举动**

4 月 7 日，在一次五小时的夜间会话中，他安装了 OpenSSH Server 和 Tailscale，将受害者机器加入他的私有 Tailscale 网络，并设置了基于密钥的 SSH 和反向隧道。现在，他可以通过 Tailscale 的加密网状网络访问该机器，无需 C2 也无需暴露端口。

第二天，Havoc 基础设施下线。Cato 没有说明原因，但这几乎无关紧要：Tailscale 路径位于独立的网络上，因此访问权限仍然存在。

当 C2 于 4 月 26 日恢复时，代理自动重新连接，无需重新入侵。在最后五天里，他运行了 145 条命令，探测了智能卡和证书存储（表明他正在关注基于证书的登录），从一个名为 Thales.zip 的文件中运行了两个来历不明的可执行文件（总计约 32 分钟），然后删除了 17 个文件，并于 5 月 1 日销声匿迹。

他的目标很狭窄。没有 Mimikatz、没有横向移动、没有勒索软件，也没有迹象表明他带走了浏览过的文档（从税务记录到保险）。只是人们输入的内容：银行登录信息、电子邮件密码、政府门户网站。对于小企业主来说，这是直接的经济风险暴露。

这些工具都不是新的，这正是关键所在。中国的 APT31 在 2024 年和 2025 年使用 Tailscale 静默隧道化从俄罗斯 IT 公司中传出数据，Scattered Spider 依赖 Ngrok 和 Fleetdeck 等合法远程访问工具，而 Poisson 的备用通道 RustDesk 则出现在最近的 Akira 勒索软件入侵中。

这些二进制文件是签名且合法的，因此止步于恶意文件而非恶意行为的检测会遗漏它们。Poisson 带来的是命令级别的证据，证明这种伎俩能够超越下线的封锁，而且是由一个显然仍在学习的人操作的。

**关注要点**

Cato 的狩猎清单很具体：

* 当 OpenSSH Server 安装在 Windows 工作站上时发出警报（这很少是合法的）
* 监视在没有理由运行 VPN 的机器上出现的 tailscale.exe
* 查找指向外部主机的 ssh -R 反向隧道
* 检查从用户暂存文件夹运行 .vbs 文件的 wscript.exe
* 标记设置为最高权限且启动脚本解释器的计划任务
* 监视使机器保持唤醒状态的 powercfg 待机超时更改
* 阻止 DuckDNS
* 更重要的一点：当您发现一个 C2 时，假设它不是唯一的入口，并去搜寻其背后安静的持久化层。

Thales.zip 中有什么，以及那两个程序在机器上运行的 32 分钟内做了什么，是 Cato 留下的未解之谜。但更重要的答案是：C2 从来都不是入侵本身，只是通往入侵的一种方式。干掉 C2 却留下 OpenSSH、Tailscale、计划任务和键盘记录器，攻击者仍然有办法回来。

这正是补救措施一直忽略的部分。

***END***

阅读推荐

[【安全圈】国际足联后台曝高危漏洞 黑客能随意篡改全球世界杯直播](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077497&idx=1&sn=78843c56369db38734d325ad4542c041&scene=21#wechat_redirect)

[【安全圈】研发软件0.8秒抢票涉案3亿 技术黄牛落网](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077497&idx=2&sn=c184fb024a6e41b289af03d4d7d13e5d&scene=21#wechat_redirect)

[【安全圈】得克萨斯州发生数据泄露事件，超 300 万人驾照、护照信息遭窃](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077497&idx=3&sn=14b5ce28f4895871a11b24744bb9c029&scene=21#wechat_redirect)

[【安全圈】微软安全工具自己"翻车"了？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077485&idx=1&sn=2f82a2ce79a628832be58c403dc20460&scene=21#wechat_redirect)

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

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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