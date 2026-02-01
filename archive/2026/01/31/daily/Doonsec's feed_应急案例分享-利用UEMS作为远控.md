---
title: 应急案例分享-利用UEMS作为远控
url: https://mp.weixin.qq.com/s/n8MJtEs74aphAVu6G99DRA
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:24:58.659366
---

# 应急案例分享-利用UEMS作为远控

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG7333Jro1wICDQnnK70JfX2bxvibNKvziaibj6364x8l7iatsQtj49vSHE8ANQ/0?wx_fmt=jpeg)

# 应急案例分享-利用UEMS作为远控

原创

happy
happy

Desync InfoSec

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733AuZXu7mJKwUQus9cvLRoP7sOqD4VlMPQ4iaYUQldJd8hia9eyK1a7o6g/640?wx_fmt=png&from=appmsg)

**点击蓝字 关注我们**

**事发**

某同事突然在微信工作群里发送关于补助办理以及二维码的通知。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733ZzVtxqdAUtT6XsIOmXPqxX50iaanmbCAnedoVkKJSYh1tKzZJj6OZ2w/640?wx_fmt=png&from=appmsg)

随后群里的同事以及受害者本人看到消息，判断出可疑并立刻通知到安全团队。遂上机排查。

**分析与排查**

**受害者A记录**

同样是从网络外联入手，发现受害电脑存在与123.182.162.200、220.181.181.58外联，经情报中心判断俩IP命中恶意情报。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733nJkzIU1Nt2TE2jzuknEA3ckV4icERoWCiaUu6RXJQibW55s4ibPicgf1hzQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG7339FQvgkIZnYYbSPxTMyX0IWVQOfm1GsShxtx4Oal9KI5es1mCS0RWiaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733hx7pAPwdCAcrwr5bBCkDjmSgF1HXibxLwmhxr1icFPayfJyo0GicHK96g/640?wx_fmt=png&from=appmsg)

定位到由SearchHost.exe进程发起的外联，该进程为一个关键的、合法的系统进程，主要用于支持开始菜单和任务栏中的搜索功能，此处猜测黑客使用进程注入技术，但经过工具dump出dll文件并进行排查，无恶意行为产生。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733GQdT93uIwusiaUia2A6qTAiaSfrFvDKk8RqbSEePYnR9iaXAIia9wt7ibaWg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733Cw2xqttynkoapMgvA1eYsmkcdEQIL4QsnjOmgunUFoJkEGatYaAibZA/640?wx_fmt=png&from=appmsg)

后续经确认，Windows操作系统进行网络通信时，会使用到微软的一些CDN，这些CDN会被威胁情报识别为扫描类型的恶意IP，属预期行为。

网络外联的线索中断后，再根据事发的这个时间点作为线索对文件排查，无果。尝试根据常规后门分析排查，同样无果。至此所有排查线索中断。

但在文件排查的过程中，发现受害电脑存在UEMS\_Agent程序。

这是一款由印度Zoho集团开发的企业级“桌面与终端统一管理系统”（远程管理类软件）。据该公司官网介绍，该软件有远控软件常用的功能，例如，远端档案传输、多监视器支持、录制远端会话等功能。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733TMrk2yujLsZcn62iagkoibOCIdeibQdI5MiaGDQz3IYRBHak0fRzkkPI2g/640?wx_fmt=png&from=appmsg)

根据对该程序的历史连接记录进行查询，发现黑客首次远程受害电脑时间，并确认进行远程控制的时间段，符合黑客操作受害电脑，通过微信进行群发钓鱼信息操作的时间范围。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0Fkeict7X0ibeq68TictmnJWUGEOwvqaWLl6emywVibTM0wmVAhAUYzVL2Mk6ZWTN6HmaQia3J355Aibxr5hw/640?wx_fmt=png&from=appmsg)

另外，内部组织未对全员要求安装该厂商的桌面管理软件，因此和受害者确认了该软件并非本人安装后，确认了黑客是通过一个合法桌管软件对受害电脑进行远程控制且作为权限维持的手段。

同时，通过对Windows的Prefetch文件进行分析，确认了在UEMS\_Agent安装之前运行的程序有TINYDL.EXE等，均在“啊啊”目录下。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG73325ZB1L82Kcksy5LiadWXU5UHzniaaEKoicYFJ7eeWMtWCtSMXYCK2oYQw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733fia78I2qeZkZxTXqHMK8yPay0JWAjFUpzJN0tyaaiaO7rQiaOokoSWdlQ/640?wx_fmt=png&from=appmsg)

对该“啊啊”文件夹丢进沙箱进行分析，发现标记为木马程序，并且里面的11.zip文件被密码加密，判断该文件夹存在异常。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG73372dHiaPJq7et2vicBCT9icGq99G0pwBQTRWyNYFKOwjuYhwiaDYGwdXKWw/640?wx_fmt=png&from=appmsg)

通过对系统的$MFT文件进行取证分析，确认“啊啊”文件夹落地时间。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733PcXibCELY2whmPYOpE8q4d5yibZH96nkeMKRR9tciaBP8sT3PDiaICdlbg/640?wx_fmt=png&from=appmsg)

利用Prefetch文件中，排查加载过“啊啊”文件夹下的相关文件进行反查，确认出受害者运行9120251114081341.EXE程序的时间，且该程序为初始感染木马载体。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733kw7H4Y3ic6wxYGXGsYicBXLr5ThvCCmiaiboyWGg9icvmzXYwCia3oGkeFJA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733TgFuJbxFYkFd5o4TcRTGOtjUjCUwwIheeOsk6uibQgxPhxiaC5iat579A/640?wx_fmt=png&from=appmsg)

全局检索“9120251114081341”相关文件，在微信相关的临时文件夹找到，推断9120251114081341.EXE木马文件来源于微信。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733eJwyafnecemzRzQrib6RM4puw3xRvEv78KgKGiaricntNGI6xFA9tG5cg/640?wx_fmt=png&from=appmsg)

在微信进一步排查确认来源，另一位受害者同事B存在向公司工作群里群发木马文件行为。（图略）

最后，清理该受害者A电脑所有发现的木马文件以及UEMS\_Agent服务和计划任务。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733H6uO2GB7FZL957PFDILZ8icZM6ybe1e4jKEDQReSalu9rr8ZbI7QS8g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0Fkeict7X0ibeq68TictmnJWUGEOkzMaicDQnkQIOhMYCf0WfRbk5jIP9vaGb4h2jGTblGtpxVRM4cVW4kQ/640?wx_fmt=png&from=appmsg)

**受害者B记录**

联系受害者B并于其受害电脑进行分析排查。根据在受害者A电脑排查得到的线索，直接在受害者B电脑上全局检索初始感染木马载体，发现微信相关的多个文件夹中存在该压缩包，意味着黑客同样利用受害者B电脑进行大量群发，并且在回收站发现木马程序“9120251114081341.exe”。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733icu3LP7Vibia4VekIbObyiavIBMNjMNqfCXibGOIpg7UAGVHYq1u9EtvtTg/640?wx_fmt=png&from=appmsg)

同样在受害电脑中发现黑客同样使用UEMS\_Agent作为远控以及后门，

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733ZEbOVu2myIJY9c1iaveT0qXeG1fibXFHLCJpaSscr6L5k31FA4gWicvaQ/640?wx_fmt=png&from=appmsg)

并且在文件中发现一键安装该Agent的脚本，可以确认黑客安装UEMS\_Agent时间。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733SiaYpXtgib92p34UkmibvJ0E3RsWcnwUrUn54bED2wGwIfpmnKtyLicicuQ/640?wx_fmt=png&from=appmsg)

另外在服务排查过程中发现一个名为“Micros”的服务，指向的程序名为“LGHelp.exe”。一台联想电脑有一个LG助手的程序，明显存在异常。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733ubF2YnOETggUhNGnUSicIlEysN3fzxKyJp47zQSwY4f8ia7h0stpVyCw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG7339HO8X7X5YgFCedXcln0VKX044Gvru0nFKqZPuhJy2TuUbwKJNOCdmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733LqYK7CWKFhuM2Ud1MibRicGdYicx3Tbko6QRSCPd8cUbeZNCJq9V5JeRg/640?wx_fmt=png&from=appmsg)

同样扔进云沙箱进行分析，确认为木马文件

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733CmgXN3ic6ItEM0b7n3mD56NicF65gBn36mhWspq2pK95nYj0H52LMic7Q/640?wx_fmt=png&from=appmsg)

受害主机上装有360安全卫士，顺理查看查杀记录，发现受害者分别下载名为“client\_setup\_S2597546138\_.exe”恶意文件以及执行"projone"文件夹中的木马文件的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733hAheakWtGUs3x7JDqUbqLb8Uu8ajBdQicCU4tHH7iaJbstWcVksMJRIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733DvGicbwdUFygYOp8REFiaj6uqws8I6RibibmMOdqicjCu5s0r0wB7J3XbKA/640?wx_fmt=png&from=appmsg)

最后根据木马程序“9120251114081341.exe”在社交软件进行溯源，发现受害者B收到来自外部受害者群发的木马文件，判断受害者B因此中招。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733Pibq14FibwuDHr4J0szsw7z225n9EyPnaJabVs6s8DQN9WrYEY0ibwV9g/640?wx_fmt=png&from=appmsg)

最后同样清理所有木马文件、后门服务以及计划任务。

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733Zvv8ZueMXutlwoZc5LCamC6AvG2zic80ZDEbFs4nVMS5f9XMF458Bhg/640?wx_fmt=png&from=appmsg)

**UEMS\_Agent配置文件分析**

通过分析受害A电脑和受害B电脑的UEMS\_Agent配置文件DCAgentServerInfo.json，确认黑客控制服务器分别为206[.]238.179.188:8383和154[.]91.64.91:8383

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733aLic3kH7V5Pu7IjyHU2yghgNjLlYz37UG4pOnbFnGTBibQsI4HuHkUDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkfT4FgDmJcxvJjMfrAHG733FQF6icsQwdKH3gCrl9klk2IDef5LLqiaEBGvhDnEJGg4pvDw9qryuX0A/640?wx_fmt=png&from=appmsg)

**IoC**

206[.]238.179.188

154[.]91.64.91

3541dcb232ec3682b6405dbfbdec7aa3

832b5d4362b9ee2f9db6c0c65587f1ea

6615332a36e97c8f947bab3a88741950

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

Desync InfoSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/9DhkvTR0FkeFpGrKMFU4NyWgYxhTTtARibcgd8y7msMIlZEicN5zxiahgsxzNcOurtGuBkTJYdp1ZFEN1lDF8EbDw/0?wx_fmt=png)

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