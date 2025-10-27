---
title: 书生大模型实战营闯关 第一关：Linux 基础知识
url: https://mp.weixin.qq.com/s?__biz=MzAwMTMzMDUwNg==&mid=2650889118&idx=1&sn=54feaaad6f76548dbf584d26f72a5f4e&chksm=812ea7bbb6592ead7a101fad7d21fe843d90c1ab7da3a0c58b4321a75bba90bd2bdb4343f214&scene=58&subscene=0#rd
source: 网安杂谈
date: 2024-10-30
fetch_date: 2025-10-06T18:53:29.410520
---

# 书生大模型实战营闯关 第一关：Linux 基础知识

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg790rmDaiasJ5Fg5gTqppf3DGljqRt8kRnJxTDU2KqSiaibzias2bib8T0AQ/0?wx_fmt=jpeg)

# 书生大模型实战营闯关 第一关：Linux 基础知识

网安杂谈

网安杂谈

背景：因为项目需要，要使用多模态大模型进行落地应用，经过调研发现，书生·万象多模态大模型（InternVL）是国内最优秀开源多模态大模型之一，正好书生也提供了训练营这个非常好的学习机会，还给免费算力，那就抓紧开始吧。别忘了扫描海报上的二维码报名哦！

InternVL 介绍:https://github.com/InternLML

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgichzau3fnMFSic2pFIVamY8HovMFlCENmnN2MCbEs1yyoVdzUKXBAicZg/640?wx_fmt=jpeg)

书生大模型实战营闯关 第一关：Linux 基础知识

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgg1Vn9JvW0EJdMjMQgSrVxW3UXeOzHhILebMWuyF038MZnGErllcGtQ/640?wx_fmt=png)

1. InternStudio

InternStudio 旨在为开发者提供一个先进、高效、易于使用的云端机器学习平台。基于强大的 InternLM 算法库，InternStudio 不仅与 🤗 HuggingFace 开源生态完美兼容，还提供了多种便捷工具和资源，以助力开发者在大语言模型领域的探索和创新。

官网地址：https://studio.intern-ai.org.cn/

注册并登录后就进入控制台，可以创建开发机

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgzLmQoJKlqEgRWicr1VrsRFiaE1UicYG4HtM8a0s2uAEBuU4z9JIjGLqfA/640?wx_fmt=png)

选择默认参数，很快就可以创建成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgUWXDTib5FckYpAlYDFkvhbX3hd4Mvr4OeWLEHH0l6qfcBpnjwZSeOJQ/640?wx_fmt=png)

选择进入开发机有三种不同视图可以选择：VScode、JupyterLab、Terminal。可以选择自己习惯的模式进行开发，这里就不赘述了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgovVPDsAz8uzrOJyPuwQZfqy56PEdu1C6Ex1cOTfNtnDSFRBEsd2QCA/640?wx_fmt=png)

2. SSH连接开发机

SSH全称Secure Shell，中文翻译为安全外壳，它是一种网络安全协议，通过加密和认证机制实现安全的访问和文件传输等业务。SSH 协议通过对网络数据进行加密和验证，在不安全的网络环境中提供了安全的网络服务。

SSH （C/S架构）由服务器和客户端组成，为建立安全的 SSH 通道，双方需要先建立 TCP 连接，然后协商使用的版本号和各类算法，并生成相同的会话密钥用于后续的对称加密。在完成用户认证后，双方即可建立会话进行数据交互。

 InternStudio提供了SSH方式连接开发机。点击SSH连接，就弹出SSH连接登录命令和密码，当然也可以添加公钥建立本地与开发机的安全连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhguic4L78PiaXtIvVb9PcRTrK8wqFDLZ1yy0LOw4gwyKNZ7wERQXrX44XA/640?wx_fmt=png)

在这里我们使用VScode SSH连接开发机。选择远程连接，输入登录命令和密码，打开要浏览的文件夹就可以进行文件浏览了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgq3zqDyfLNAE2hYeZpNexRw7tsjcZc5ic2MRykCicNdtXSy1kjiaOvvfsA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgvFkhjsfmHuFTdf81TCg23Ik0RKHs8aqwfSvJJzLXMBkibjabLn2384w/640?wx_fmt=png)

开发机的目录结构和注意事项：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgNuU9CEZFMVARJQvpyNGRgv04HUkFlP1DQ2x9xHHTgMfKmIpHXOZWsg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgXTYxdg7oLhGjWEIaiaXZmzBtmQFhQib0AeSicN5sJnkRUbwwX1kMfURBw/640?wx_fmt=png)

3. 端口映射

端口映射是一种网络技术，它可以将外网中的任意端口映射到内网中的相应端口，实现内网与外网之间的通信。通过端口映射，可以在外网访问内网中的服务或应用，实现跨越网络的便捷通信。

进行端口映射的必要性：因为模型web的部署实践可能遇到web ui加载不全的问题。开发机Web IDE中运行web\_demo时，直接访问开发机内 http/https 服务可能会遇到代理问题，外网链接的ui资源没有被加载完全。

所以为了解决这个问题，我们需要对运行web\_demo的连接进行端口映射，将外网连接映射到我们本地主机，使用本地连接访问，解决代理问题。

回到开发机，选择自定义服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgJaiaVSrD4BgCfZVhmib2w7BSdXow3rYb71vS8BQDaQOXUKibrmicj1PmOA/640?wx_fmt=png)

弹出这个界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg2cVshTo0e82KkIzr0IMX3RuYIUTs1Tczvquc47Cn9ibdoN7YaRVBVQQ/640?wx_fmt=png)

端口映射的两种方法：

（1）可以通过powershell，在终端输入命令和密码进行端口映射。通过添加公钥还可以免输入密码。

（2）使用vscode等工具自动端口映射

我们使用第二种方法。前面我们已经通过VScode连接了开发机，现在我们创建一个hello\_world.py文件，在文件中填入以下内容：

```
import socketimport reimport gradio as gr # 获取主机名def get_hostname():    hostname = socket.gethostname()    match = re.search(r'-(\d+)$', hostname)    name = match.group(1)        return name # 创建 Gradio 界面with gr.Blocks(gr.themes.Soft()) as demo:    html_code = f"""            <p align="center">            <a href="https://intern-ai.org.cn/home">                <img src="https://intern-ai.org.cn/assets/headerLogo-4ea34f23.svg" alt="Logo" width="20%" style="border-radius: 5px;">            </a>            </p>            <h1 style="text-align: center;">☁️ Welcome {get_hostname()} user, welcome to the ShuSheng LLM Practical Camp Course!</h1>            <h2 style="text-align: center;">😀 Let’s go on a journey through ShuSheng Island together.</h2>            <p align="center">                <a href="https://github.com/InternLM/Tutorial/blob/camp3">                    <img src="https://oss.lingkongstudy.com.cn/blog/202410081252022.png" alt="Logo" width="50%" style="border-radius: 5px;">                </a>            </p>
            """    gr.Markdown(html_code)
demo.launch()
```

在运行代码之前，需要先使用pip install gradio==4.29.0命令安装以下依赖包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhg5l0YIURlvbE8MCnSBxUsSFYibnye5DcetMytHibIaAVhrfapHXR2KWww/640?wx_fmt=png)

然后在Web IDE终端中运行hello\_world.py的话，通过浏览器是没有办法正常访问的，需要进行端口映射。

在vscode终端选项卡中运行hello\_world.py后，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgialdSoAtFzYqzCMho4xycPCicP5EX3WKJCibH4ibuTU06VaV3SfHCwYvmQ/640?wx_fmt=png)

可以看到VScode已经自动进行了端口映射

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgeOWMW6NmpVWyhic03tabGqkKhLiaIuE3j2MicSJmsELfo1BHUwiaJsaXtQ/640?wx_fmt=png)

在本机的浏览器中，输入127.0.0.1:7860就可以顺利访问啦

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgNr3JqgQ0EG46b4t4EozrJiau4cD1PSZ2UGbibJexruHqfxgao5xAlnBA/640?wx_fmt=png)

还有其他可选知识比较基础，大家估计都已经做过了，在此略过了。有兴趣学习的可以扫一下文章开头我的专属海报二维码，有兴趣的一起进营学习啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Z4jKmMQicbWNc612bLLP5eSV7Ite6ZMhgDp3fvgNibkTTyBNO0vkuIqIkXIcuA2HmAS5QoLjG9rvgE01H60LV5VA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

网安杂谈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Z4jKmMQicbWP0nM8PnhZtqI4yFWpIJ8KdgxKg1XsbSjljI4kic5C0oAfDRiaXCJmmsl66ro1fY3eDJVUAcoib2PRDg/0?wx_fmt=png)

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