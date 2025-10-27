---
title: 警惕！AI组件ComfyUI易被黑产盯上
url: https://mp.weixin.qq.com/s?__biz=MzA3NTQ3ODI0NA==&mid=2247487713&idx=1&sn=fa29d87c079b8ca435d532d2d473c2e7&chksm=9f6eb56aa8193c7c94e645494dfab54d689828da24f35b0939144c1c74e2329a3638b0df15b5&scene=58&subscene=0#rd
source: 百度安全实验室
date: 2025-02-27
fetch_date: 2025-10-06T20:36:58.845805
---

# 警惕！AI组件ComfyUI易被黑产盯上

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2fvCZicH9HWQYlMBUgojdUzPTL3voXwMwLVH4vQibQDic2ZhjraRjmyhvmQdbz1fhvmzZTXClaCOKkE52riczxZKnQ/0?wx_fmt=jpeg)

# 警惕！AI组件ComfyUI易被黑产盯上

百度安全实验室

随着近几年大模型的迅猛发展，以及安全对抗技术的持续迭代升级，黑产团伙逐渐将攻击目标从传统服务转移到了AI相关服务。

近日，百度安全团队捕获到了一起**针对大模型相关组件ComfyUI的攻击事件**，经过深入分析，该事件背后团伙已实际针对国内不少公网ComfyUI进行了入侵。本文将事件调查细节同步，以期促进整个AI行业威胁态势感知的进步。

百度安全在此建议大家及时排查，同时也将持续进行大模型基础设施的安全威胁狩猎，分享团队在大模型浪潮下的威胁感知与攻防技术思考，与整个行业共同建设大模型生态安全。

***概述***

**关于ComfyUI**

‌ComfyUI是一款基于节点流程的Stable Diffusion操作界面，专为图像生成任务设计。‌它通过将深度学习模型的工作流程简化为图形化节点，使用户操作更加直观和易于理解。

ComfyUI提供了高度的可视化和扩展性，用户可以通过拖放操作来构建和调整图像生成流程，无需编写代码。‌作为大模型图像生成领域的最热门框架之一，其在GitHub斩获了接近7W Star，备受开发者喜爱，根据网络空间测绘数据，全网共有近2700例ComfyUI服务，其中不乏无需密码直接访问的案例。

ComfyUI后台支持加载用户指定的模型文件，同时用户可以方便地管理模型。但给用户带来便利的同时，也存在一些安全隐患。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTibQvOXxT6iaoO53ngXodWQK0smXDdEqeVhge3LibAj7Q3duZlU3BQ8EkQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

百度安全在2月21日捕获的攻击事件中发现，攻击者利用ComfyUI用户错误配置问题，在无需认证的情况下进入到ComfyUI后台，同时利用后台模型加载功能安装攻击者提前上传在Hugging Face的投毒模型文件，以便利用模型加载时的pickle反序列化逻辑，控制受害者机器，进一步渗透目标内网。下文将深入展开分析。

**以下是对该事件的详细分析：**

***0****1***

**投毒活动流程**

本次事件攻击者主要利用了ComfyUI 控制台无身份鉴权的配置错误问题进入控制后台，并通过ComfyUI-Manager插件中的远程下载功能从Hugging Face及其镜像站等相关模型仓库拉取投毒模型（.pth后缀的文件），使得开发者在使用ComfyUI加载投毒模型时会因自身的pickle反序列化逻辑触发恶意的Loader，进而执行恶意Bash脚本，脚本会从攻击者的服务器上拉取C2木马进行远程控制，C2域名为cloudflare.com提供给普通用户使用的隧道服务（用户可以无需外部域名和ip就可以把内网的服务映射到外部），攻击者滥用该服务，达成隐蔽控制的目的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTD6GUfhgcBoMIlJHQhUC8RJiaicuvTZ9iaHXhmZwvA41Q86lQcZZpZs1sA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

据CVE官方披露，ComfyUI历史存在多种漏洞类型，包括：任意文件读取漏洞、远程代码执行漏洞、存储XSS漏洞等。相关漏洞已分配如下CVE编号：CVE-2024-10099、CVE-2024-21574、CVE-2024-21575、CVE-2024-21576、CVE-2024-21577。本次事件主要利用的ComfyUI默认无身份鉴权机制的"特性"，从而直接访问ComfyUI后台。但该“特性”官方并不认为是安全漏洞，归因为用户错误配置，在使用上官方始终认为使用者应自行注意，不要将ComfyUI对公网暴露或应该通过沙箱环境运行，以确保ComfyUI安全。

（参考https://github.com/comfyanonymous/ComfyUI/discussions/5165）。

﻿

***02***

**样本分析**

## **未授权ComfyUI & ComfyUI-Manager 插件后台访问**

##

ComfyUI-Manager插件可提供模型管理功能（远端下载、模型使用管理等），ComfyUI-Manager界面功能如下:

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTedU8rQ2dd3h7qdibJO0icRdnlW8fibOozsrTa8iaA7gsUopia5JUTsibHAug/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

攻击者进入ComfyUI后台后，首先利用该插件从https://0x0.st/8TX8.pth下载了恶意的模型文件，并加载。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTeaKOiaDBA4uicl8FCTQhQgPZJy9HOHo89IIoF23vQsEx75iaE2dP2ibtKg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其中该域名0x0.st为公开匿名文件分享的服务，任意人都可以上传文件到该网站，供其他人下载。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTTeITibd7Zose3Brpsniap4Jw1icicUSyFgJF4tQdM91Fkia8iaghyicdF25oQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

在上面加载恶意的pth模型文件后，攻击者的木马并没有成功上线。几个小时后攻击者再次从https://hf-mirror.com/DSfsdasgaa/shell/blob/main/kcp.pth下载恶意pth文件并加载。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTpph9EicnyOL0YiahJcoYl9Bia8riaDOJ6gKh865bQQicTde9iakbPGcQx9uA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

该恶意模型下载地址为https://huggingface.co/DSfsdasgaa/shell/tree/main的镜像文件地址。该大模型仓库同时还存在**ws.pth、wsc.pth**。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYT2guWEePY0Hyiadic4u20iaToRYXDgTPg99rfW4hUx8Y7yHFW5QVbBJgow/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

针对该 Hugging face 上的投毒用户 DSfsdasgaa 进行分析，该用户仅发布了这一个恶意模型库，无其他行为痕迹，且账号信息中未写任何描述，非常符合一个异常用户的特征。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTGwQaV9PlJ1PuhScg0jEGa6SF8ia3osklE6w3Cj5G2ORNBR1bg1YfqPQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

##

## **8TX8.pth、kcp.pth、wsc.pth等模型文件分析**

大模型里的pth是包含了模型参数和状态的pickle文件，pickle文件为python对象序列化后的文件。当大模型加载模型文件时，模型加载器会对文件进行反序列化操作，若该文件为恶意的pth文件，就会触发其中预先设置的恶意代码，进而导致命令执行漏洞。本次攻击中，攻击者主要使用了8TX8.pth、kcp.pth，这两个恶意的模型文件，都是类似功能，我们分析其中一个8TX8.pth。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTMyVwSk6Z4cBliamA2evMhLgo7pNsSj7m4Jic99kGtJCOr2p3VJvq8QCw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

通过opcode解析：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTqfkvQ7ibI1456clhhBo5yfk1CGskr7oNYesn2h3Tdyf83HAQ6hY5kwQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

我们可以看出该文件被反序列化加载后会通过system执行以下命令。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mMIu6eS7af8Nuc4BicTJCx5xWCO0YeLSk9DdRdNqMfDySsE9KocmtpeM1xSaa6jibv73K3gDhic9eKVQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

上述命令为从 194.34.254.219:10404/slk 下载sh脚本，进行执行。

**其他pth文件**

* **ws.pth文件对应的执行命令为：**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mMIu6eS7af8Nuc4BicTJCx5xvkWCB9Gzhs2fqMQdH1NdCRzZWhV0O67BJPMY6JAeBvPc053Rl5xS4Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTmowQByia9qB1R4AbkfHbB0lsuHvkA5M1fRRlL7cUzfjEICgOoX53aHQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* wsc.pth: 该文件执行的内容和slk样本脚本内容一致

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTWuyNEGUS7IHicC0FgrFabphbM1uAg8E6OMsQIYWicuOkIiaLcMr2DjjnA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

* **kcp.pth**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTtOwhQmrM6dwRwE3nEzibfOf641WhaXUxcrtkPZD3hmYMVcib2F8jCkzg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTI9bmLWibIynxaibb1TFfUibV24Tb1dI9iagumo9KfxLEzWgVTbXKOTAn3Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**slk分析**

上面利用恶意的pth文件所执行命令都是下载的一个sh脚本，其中拓展关联的ws.pth，在分析时已经失效，未获取后续样本。

* **8TX8.pth(194.34.254.219:10404/slk)**

从0x0.st/8TX8.pth下载的8TX8下载的slk文件，远端下载地址194.34.254.219:10404/slk，slk文件的bash脚本内容：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mMIu6eS7af8Nuc4BicTJCx5xjrpbYpoteWcoVDacew4RbfxdVQV3ZMsFsjSgbiaEGekdQ352W6bnt3w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

该sh脚本为vshell默认生成的上线脚本， 脚本的主要功能如下：

* 从当前会话 SHELL 中加载 PATH 环境变量获取可执行文件路径
* 通过 touch 指令创建 /usr/local/bin、/usr/libexec、/usr/bin三个目录的可写入情况
* 根据电脑32/64位情况从http://194.34.254.219:10404/?h=194.34.254.219&p=10404&t=kcp&a=l64&stage=false&encode=false地址下载文件并命名为c8dfdc4akcp执行。

但因为网络环境原因，后续攻击者无法成功下载该文件，导致了攻击者进行了多次的恶意利用，但最终由于网络环境原因，都未成功进行后续攻击。

* ### ﻿**kcp.pth、ws.pth(194.34.254.219:10410/slk)**

从Hugging face下载pth里面对应的远程命令为，远端下载地址194.34.254.219:10410/slk，slk文件主要是一个bash脚本，内容如下：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mMIu6eS7af8Nuc4BicTJCx5xbLxK7g3U02iajdEUPlxcrFicnu3bCzX7bThmMiaU2tnibVNKzBJk9eQT4w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

该脚本是攻击者根据vshell默认生成的上线脚本中，把其中的原vshell获取木马的下载地址，替换为攻击者放在huggungface上的vshell木马。该sh 脚本的主要功能如下：

* 从当前会话 SHELL 中加载 PATH 环境变量获取可执行文件路径
* 通过 touch 指令创建 /usr/local/bin、/usr/libexec、/usr/bin三个目录的可写入情况
* 根据电脑32/64位情况从 huggingface.co/DSfsdasgaa/shell/resolve/main/ws\_linux\_amd64地址下载 ws\_linux\_amd64文件并执行。

但因为网络环境原因，后续攻击者无法成功下载该文件，导致了攻击者进行了多次的恶意利用，但最终由于网络环境原因，都未成功进行后续攻击。

## **ws\_linux\_amd64样本分析**

针对上述C2木马进行分析，简要信息如下：

|  |  |
| --- | --- |
| Sha256 | 0aa6f668e4a231d2b450f27edc0037513e9f1cbb308e923f79c393e9890d8a73 |
| SHA1 | 24d0d7ff7fa7ee8723f2cb49220170608aa8c579 |
| MD5 | 8b58b07e167aa2bb975a3fce8f6b1b21 |
| 文件类型 | elf类型 |
| 文件大小 | 2.9M |
| 文件名称 | ws\_linux\_amd64 |
| 功能描述 | vshell 远控平台生成的golang混淆远控程序，启动后读取自身加密内容释放并执行C2 控制程序，和远端建立  WebSocket 会话进行远程命令下发和控制 |

﻿

ws\_linux\_amd64,该可执行文件是经过了upx壳压缩，脱壳后为golang编写的程序。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rNy2iaEEC1mPuNveRtOsPXAR2OvWH7ibYTD1YOwGzZ8eib77MvvLjibDj8ic5DicFibMibk6YibzDaLCTRiakP5P8gjBue5A/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

同时该golang样本把自身的部分golang的符号进行了抹除，来干扰分析人员进行分析。根据内存中dump出c2配置，可以确定该样本为曾经国内公开c2平台vshell（https://github.com/veo/vshell，该项目目前已删库）所生成的样本。

![图片](https://mmbiz....