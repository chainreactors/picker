---
title: 安全养虾日记:完全离线部署OpenClaw(内附详细搭建步骤)
url: https://mp.weixin.qq.com/s/pMZF42A3YLZ9WbS8dfRr_g
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:17.216414
---

# 安全养虾日记:完全离线部署OpenClaw(内附详细搭建步骤)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/b34oV9VTkcG30lUOJMTfEW1xbPW4TTrzV5M8ZdDbSoVrBVOUHsIPicJN1c32yXheO5JKlPsbLdjAkcriafOXNLBqmIicYywuTXgVGibTVMVs3rU/0?wx_fmt=jpeg)

# 安全养虾日记:完全离线部署OpenClaw(内附详细搭建步骤)

原创

小谢
小谢

小谢取证

![]()

在小说阅读器中沉浸阅读

点击上方蓝字“小谢取证”一起玩耍

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/b34oV9VTkcH5ZhowXpKVYZgVwdWSKGfrUDdoQD3d2yHHFj2GXPQQu1j0MTkrfm37RKiaO9NeO1y2uxsfTEscBBGiaVdZNbszqXxUg2suyaUpU/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEMKjUHP5L9Z10Jg7at21ptDrayCxyPlaIsFCnNQGDtGQGhzScZBwYdHs9wibCI34FiakuribDBuvLL62xgvHgxSCJr5nAovhNZ1E/640?wx_fmt=png&from=appmsg)

在上篇文章详细介绍了OpenClaw的搭建步骤及在警务当中的应用。

[OpenClaw在警务当中的应用 打造你的警虾！（附详细搭建流程）](https://mp.weixin.qq.com/s?__biz=Mzg4MTcyMTc5Nw==&mid=2247491213&idx=1&sn=1666bb3690398b6be479bfe7ea555c29&scene=21#wechat_redirect)

感谢各位老铁的点赞和评论。有评论区有的老铁提出关于数据的安全问题，毕竟可能会涉及到敏感的数据，这一点小谢确实没有在上篇文章当中提及到。除此之外，还是会再有其他的需求：
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcG43rzwxrRTbAxy600NGqgQWRcqbt6NaiaOZCRZhINyDAWjyF2jQNXXXxErS5pzak4DUUicqllIAGyxBlib8DPfeGZyiaEsYuhaG9I/640?wx_fmt=png)

  有一些电脑是完全没有网络环境的，所以这期就推出完全离线部署的教程，完全没有网络环境的状态下部署OpenClaw，赋能实战工作。

无网络环境完全离线部署OpenClaw的好处是不涉及到大模型的Token消耗，且不需要网络环境，直接安装包进行安装，简单易用，还能将OpenClaw的服务共享给局域网的其他机子，也在隐私数据上最可控。但建议需要部署的内网机性能好一点。
  所以这期我们来讲解一下在无网络环境完全离线的状态如何搭建OpenClaw。
  但搭建之前也要与大家声明安全问题，大多单位是直接不允许搭建的内网机子，本文章只是作为完全离线部署搭建技术的探讨，不具备现实工作的指导意义。各位老铁也要根据实际情况出发。
  如果大家自己搭建在自己本地电脑，想要做到相对的安全，想稳妥用 OpenClaw，可以按这个来：

1.只从 GitHub 官方仓库 / 官方可信渠道 下载源码或编译包

2.下载后校验哈希值（SHA256），确保没被篡改

3.运行前用杀毒软件全盘扫描一次

4.重要资料、密钥不要放在同一台机器

5.满足这些，再加上离线，豆包给出的答案是基本可以认为足够安全。

  本文适用于Windows 10/11系统（内附Mac和Linux的安装包，可以后台回复“离线部署”自取），手把手教你利用LLM-Studio进行大模型的本地部署及OpenClaw的本地部署和加载大模型、局域网服务配置及对接，只需三步，步骤简洁无坑，新手也能上手！

  前期准备

 系统：Windows 10/11（64位）
   硬件最低要求（必看）

CPU：4核+

内存：16GB+最好

   存储：固态硬盘20GB+（模型+系统）

      显卡：无强制，但如果有独显（8GB+显存）最佳

      网络：完全无需网络环境，只需安装包进行安装（需要安装包资源，后台回复“离线部署”即可）

安装包列表（全离线安装包且免费安装运行）

1. LM-Studio（本地模型运行器）
2. 离线大模型.gguf文件（可使用LM-Studio进行导入）
3.  Clawx（基于开源框架OpenClaw开发的图形化桌面应用）

小谢自己搭建的是Qwen3.5 9B模型。效果在文末有展示。配置如下
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGeZV7JKd8Yt0HXgyQSZ15hrn3MBV8nvT2vndBIQfn0QJIr24gbZAEb5vMAs9RHpz5JVyoLEDzXbeuLnjxwwlibyrVzezKLY3Lk/640?wx_fmt=png)

  有了上述的前期准备之后，接下来我们来进入实操。只需简单的三步，即可搭建完成。

  第一步:一键安装LM Studio

（1）双击运行安装包

正在安装
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEJWLEn0HGNNnpFnxyOITIO1L8KLCcQw3dqpeBgdDcPllBepaX8bPVevcdgXa2ic1lOB5sC8SkGwWPib4b05VDicQvF3Z1sGlEc2A/640?wx_fmt=png)

最开始进入界面我们可以在设置处设置为中文
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcHX5ibRcl1K0KIZjmF7Ibf6y4FaznjBUhnpvGsoHcibxHvDiaERiaYRrmSaeicqtuiciakECNwLicQbtLtCpiaQS73zb9p20MZft9YjGJiaA/640?wx_fmt=png)

（2）接下来我们要来导入模型。
先载下所给的资料当中的“0.8b”或者“9b”的文件夹，然后要将他放到模型所在的文件夹当中，也就是默认的路径
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHkktQdbicPicH0uJ4QnQ1ZLjclJY5okibX8j9SLADdZKLQMc2bOt1ANwZzbjXBTN3thIO1TtgJKwSMvDc4kb3OrdQfgt7bVnBQj0/640?wx_fmt=png)

（3）紧接着在这个文件夹当中放入我们的.gguf离线大模型的文件夹。我们以0.8b的为例。可以在LM-Studio的My Models处看到，是没有0.8b的模型。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEBPpCLFYkFgSWxtRAW4yVUibVbicxDxcawx7FAVpNFic15jicK45KutSwuBPBM6PHYrrDzojHQjxTuQWBUbd3J1yI72HEG9z1ZqB8/640?wx_fmt=png)

（4）将其放入C:\Users\lenovo\.lmstudio\models\unsloth文件夹当中。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEWlBKB4ia7gD95AngkyaEg8E4MDGOQ6KIQic6GZs5yZJeUDAqBqEiblXugick3G5wXAj1jaR2ysCnIyZckYxefVHCMdfPFXWiaLLKE/640?wx_fmt=png)

（5）这时再到LM-Studio的“My Models”处就自动更新过来了。可以点击“Use in New Chat”进行测试是否成功。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHRicgzNdaU6TPnOpxWNLg6lN4vG9c7PibxV1ic1AAQ2S93mO0yHg78pTNQj0hljoFAibWOTtVNHPZ28Wia7P6jHWEsmHjeE5R5WXeY/640?wx_fmt=png)

（6）测试成功。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEe5E1Sia0Hy9C4n0YicR5wJ46ib4pTa0ibby1P0k911xgVSNWmDJ16quEPqfy81V7ibR67XBRicV8smo2XhfVzxvzT74CfyHuwoibjM8/640?wx_fmt=png)

（7）如果你要自己的电脑性能比较好，要下载其他的模型，也可以在其他的外网机子直接搜索关键词qwen3.5，进行下载，再按照上述的步骤将.gguf文件导入到离线的电脑当中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEjJib0cia0aWJD90o0grFbjThR4JabHUiaQLDHHmxuXkKHyL2JIJlzkYG5FoOm4RB74D5Eaib42k28A6keriauFdPwHtUR14n2xcxU/640?wx_fmt=png)

这边我们尝试下载Qwen3.5 9B的模型进行下载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcELAISkdianjtxicE9AKIdrn0r0MUqp8zpeVibxWSQH2APzn5FzHrXX39XUv0CPiaOHjHqNwzpa1865AolOQN1yCcicrXbYmTKedHdg/640?wx_fmt=png)

正在下载当中(保留在当前的窗口等待下载完成即可)
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGoIEuLY2UbvqicRtmG2YibVyueGhf6ZnQ5ric32k7alMhA2xtdCEfbfyH2psRmCq5VSiag1MqqNAl7LFRzbCu6XhRib3MeaiaiaibuLB4/640?wx_fmt=png)

下载完成后即可到C:\Users\lenovo\.lmstudio\models\文件夹下看到离线的模型文件。将此文件夹拷贝到离线的电脑上即可配置成功。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEqvUxSOC0Qf3h1pI5m627ehcOCjmiaiade8kP7oFGicOia7eBs03zDQh7gxNcBhicq66H5G2WiadDmCs6qqibCRicSLBIl7Vok2xric4ow/640?wx_fmt=png)

（8）那么接下来，我们如何获取本地本地大模型的API key值呢？
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFHibnYM92D5n0sEwmUicibeopnZ7zPK6UIWCQfLiaKuZCSKUDbiaibOGxGibmV23WYrHjobvvOgsoxGGRyvvprHNrblJYdD8eFx492DM/640?wx_fmt=png)

即可获取到本地的Qwen3.5的类似API Key值。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEqfjx61sh9SoVyNmKsiawf8lYOicibAicHRsN2jV1soYGb4TAj8Jy6PmlwJvM4pMx1WMeRMzY1ibMvHTyuG2lvUoyDmrfAnvfmXY8A/640?wx_fmt=png)

（9）但要注意要在上述地址添加个“/v1”也就是“http://127.0.0.1:1234/v1”，在下述文章当中也会体现出来。这个也将是实现局域网访问大模型的地址。比如大模型的机子的本地地址是192.168.1.10，那么局域网的其他的机子的Clawx就可以设定大模型的地址将可以填写http://192.168.1.10:1234/v1。

（10）但在安装Clawx前，我们对LM-Studio需要进行设置。也就是不限制大模型的文本上限。

第二步：安装Clawx。

（1）双击运行
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcESRldbe0FjVIicqlM78IK6QGLIpuzW1kPES0IMEiaicHIUwohicHtYt6xsDu07tvZJSuaHHlvSIcQHIeELBgZSbtCPZ8lacTSLia9k/640?wx_fmt=png)

正在安装
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEYuK6eX8HQtBDVx0gzER8ozsbwgQPTBYTR4vTkOmh3TkGx8ZC1JWOcpHLVSWNMib2Z9PfQdSjqJybmE5WgPPsKicSG0gib17MP6E/640?wx_fmt=png)

（2）安装完成后，点击完成即可运行
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcEbyUVlettxicXLvPN8hNlxwYfsUsJUYjXL2j6CZVat2vrKXBqicvciafR7JPbl3Ibqd6grW5m9SMFJfNK5kAw3Dbz3VsOPaVhA50/640?wx_fmt=png)

（3）这时可以先点“跳过配置”（截图截错了）

![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcHB53IGD3czQR5ZXEIPPcKAY0htj0eJOvzmEH2JluiazwTElpdic8K2z9bsMT4K3UdAkxibKWuwzoWypfpFRyzjFS4EltyL4lljAs/640?wx_fmt=png&from=appmsg)

第三步：添加本地大模型
（1）在Clawx界面点击“模型”。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGpZcObOVteGZekMyjJxkN93OpLRdzzyYdxiaCOGAHd1aNlRPFzC7lq5XdgrpXBA1X8DtKJJ4jPhCWKsonarsLvtcv8BeoiaSj3A/640?wx_fmt=png)

（2）这边选择自定义
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcGCBIRPnvnC9Mzia0jNibsjsEpsLCGtsFOA7p8WEH8Rv2vgZwX39TtftshaQUYKmDAYFQU2a6YUOxf8TV157DnVh48Akcicgo5wV0/640?wx_fmt=png)

（3）填写如下（基础URL获取可以参考第二步当中的第（8）步）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcENPqwianaiboiaV98uaw4PfSpxFjumvtLNn9xe22EcYIQTNpZu91ibNs1ib8Xld3CQWIibsocqPv4Mv6NFicarx1HfoZNYLBSUq1ZEMk/640?wx_fmt=png&from=appmsg)

（4）至此添加本地大模型完成，如果要切换其他的模型参考下图。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcFicAMZm9RyVa2GcmyuepxKlPgfplDCNnGCytq1xPJZuKyXMpOwicibMnGQhvXWm1Jic0aE15sNSTKTdZ1pAbPGw8mzn2nWzFvAnsc/640?wx_fmt=png&from=appmsg)

第四步：测试

（1）但0.8b效果没有那么好。我们可以看到
![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcGu31om3IrRiaTPqB25PkrYhuUOptlz6d5NtTymu6TKnMVVbjx2D5CBwVWibs0e94RMOjk5m3W5iayBcemMQS8mLJaKyviamzAeKqU/640?wx_fmt=png)

（2）好我们切换一下9b的大模型
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFicnPXTvUF82t6v9FdLWUawgldxdASnTJkQUNUZian0R1Mtyd4HK79XicfRkcNuINGYaf778PLPH5BM0Uq2IWYSnoibg5LWKxkXZQ/640?wx_fmt=png)

（3）再来看一下效果。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFfX61k3KkrLykyWyTng5SNxZDgPKAZiaYClXkL5t1dQDnOqlKg4Ew9Np1eGDBvCQZiaLtJGXv91Vxfw0Stse8ia6HIOaIMA1fEuU/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b34oV9VTkcEgWMbkbkzX8GcPU4Yo1eibp5frAwykNZcdn413yZBYEB9SYK2JWS8s9dWvIwkyGbfOarGtI15nCJuhic8cdKricQbX9Z6UDJA7Rs/640?wx_fmt=png)

  可以看到，结果是可以的，但跑出来的速度比较慢，而本地搭建的精确度还是取决于内存、GPU、大模型这几个因素。当然最终要的安全因素不可忽略，比如：
1.环境隔离：永远不在日常办公机或生产服务器上裸跑
2.危险动作需确认：删除文件、 Shell 等操作必须人工确认
3.最小权限：只授予完成任务所需的权限等。
关于安全养虾策略，我们可能会在下一期推出，谢谢各位老铁的关注。

  如果有需要上述离线安装包的老铁，请先“一键三连”，再到后台回复“离线部署”即可获取到网盘链接。
![](https://mmbiz.qpic.cn/mmbiz_png/b34oV9VTkcFIMz6U7CAhuhicUWQibkiatd3McpBCq4icc57hl36ggDcxe5JueQuMtP4ISicxSqWX7QZVgLAGx3Nw7aicybnE9ibg484zeddXMxiaNXs/640?wx_fmt=png)

##

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/bQS6HX6lflR6KAuv76...