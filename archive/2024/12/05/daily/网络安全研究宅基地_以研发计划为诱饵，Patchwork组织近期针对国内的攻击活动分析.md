---
title: 以研发计划为诱饵，Patchwork组织近期针对国内的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247497001&idx=1&sn=bf11de770fea2d96d4f3c08dfd7e038f&chksm=f9ed9996ce9a10809b95ac5c33c78c37018b7e17c304560ed687b580dda96459ed8ec5dacfe1&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2024-12-05
fetch_date: 2025-10-06T19:38:38.444608
---

# 以研发计划为诱饵，Patchwork组织近期针对国内的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FVZJndD7xbnNiatNryCIGS5LwnnibXpM9icSUILE9M3hT1noqUKeIjVzGg/0?wx_fmt=jpeg)

# 以研发计划为诱饵，Patchwork组织近期针对国内的攻击活动分析

原创

猎影实验室

网络安全研究宅基地

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F5QPSJohp8eqDUg5GckkzXoI028R5E16ZNFEAIgYBxyfgKP21ErVlBA/640?wx_fmt=png&from=appmsg)

**1**

**概述**

Patchwork组织又名Hangover、Dropping Elephant，最早披露于2013年。最早攻击活动可以追溯到2009年，主要针对中国、巴基斯坦等亚洲地区和国家进行网络间谍活动。在针对中国地区的攻击中，其主要针对政府机构、科研教育领域进行攻击。具有Windows、Android、macOS 多系统攻击的能力。

近日，安恒猎影实验室在日常威胁情报狩猎中捕获了Patchwork APT组织的攻击样本，相关样本以“国家重点研发计划‘工程科学与综合交叉’重点专项 2025项目指南建议表”为话题，针对国内科研相关的工作人员进行钓鱼攻击。

相关攻击活动以LNK文件作为初始攻击负载，引诱目标运行后，将下载PDF文件及EXE、DLL文件到本地，自动打开PDF文件以降低目标防备心理，并设置计划任务运行白文件。白文件运行后加载恶意DLL文件，在内存中多次解密加载执行Patchwork组织特马BadNews。此外我们发现该组织域名仿冒多个正常网站。

**2**

**样本诱饵**

本次捕获样本释放到本地的诱饵文件如下，内容为“国家重点研发计划‘工程科学与综合交叉’重点专项 2025项目指南建议表”

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FNz9beF5iaDyTUoPsBvCFHWia7zPK9BjicMibNiaBvEibicmgCRqm8xRMK2a6g/640?wx_fmt=png&from=appmsg)

关联到的其他样本释放诱饵文件主题如下为巴基斯坦国际航空有限公司伊斯兰堡售票处内部审计情况

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7Fnjtx9hRke2BPR3yuuJgibdOzzw5q5hyGpWwJrEYyVgKnRQoQibNu5ib2A/640?wx_fmt=png&from=appmsg)

另一诱饵文件为：巴基斯坦第一大数据和通信网络提供商Zong的登录ID及密码

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FictY1XY21Em38fE3UIWQ5WtYBjN01iahsmmaziacdsfumfVJ7ZibpKKYibg/640?wx_fmt=png&from=appmsg)

**3**

**攻击流程**

原始样本为LNK文件，执行后攻击流程如下：

1

文件运行后使用Invoke-WebRequest命令分别从指定的URL下载PDF及EXE/DLL文件，并将其保存到指定的本地路径（具体URL见附录IOC）；

2

运行PDF文件并复制PE文件到指定目录，复制PDF文件到当前目录；

3

创建名为WinUpdate的计划任务以运行后续负载；

4

删除运行过程中产生的中间文件。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F9v9QyzukH82pnkeZrGQuj6X17GzfV8jo1k3mS8WbbDO0STv7gCysiag/640?wx_fmt=png&from=appmsg)

下载的可执行文件将通过白+黑的方式加载恶意DLL文件。白文件和恶意DLL文件包含的证书信息分别如下：其中恶意DLL文件的证书早在今年3月的攻击活动就曾被Patchwork组织使用过。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FiaNJ2nToFfdOsaBzANhPZd15NHKe6JDSIwTCnYico6YCDC0sOpTBwsmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FXerw7cPdObHOh0iaKjUiaQ6lhQYOJRtD9182cqPHjOSZjCQd9DFOIzcQ/640?wx_fmt=png&from=appmsg)

DLL文件被加载之后，将从自身读取一段数据解密为Shellcode，通过创建新线程加载

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F8vpwgSsdX3mrAu73aXO29JKyP33lMhkzpGdorQ4kjcAHeMDkMRQ7xw/640?wx_fmt=png&from=appmsg)

Shellcode执行后会在内存中再次解密出一个PE文件

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7Fwzn7j9ibx8FLnsZUoo7Xo0ibJ2xXXVxYeR5hcFpqaBKrwAL9Wyw8hInA/640?wx_fmt=png&from=appmsg)

然后通过复制、抹去文件头等操作，最后在内存中加载

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7Fv4RScGmfsrb0Kz6KlptCtRUTIaspu42tZiaChEAbMzJwR1NHDh9EbQA/640?wx_fmt=png&from=appmsg)

最后在内存中加载的Shellcode实际是Patchwork组织的常用特马BadNews。该负载运行后首先创建名为"gqfffhj"的互斥体

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FjSDrZepojMFa6udqKSf47JsYDgN0NxEUfk1iadFbFqAb0ZrWwjrZ3FA/640?wx_fmt=png&from=appmsg)

获取UUID，根据UUID和文件路径编码生成字符串

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FHPUAgQNicgq47nXGiaF7ic9ZxCoet75ymJk5G5Zlj9lmuxdIXccq8g6dg/640?wx_fmt=png&from=appmsg)

获取操作系统版本，重复上述操作

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FIEDBd1Y7dnr7eglPd0ZkOssgH2XDE4BCexJiatVD7iaIGxH4XDicR8MZA/640?wx_fmt=png&from=appmsg)

获取其他信息，如UserName、内外网IP及IP所在国家，依据获取到的信息+文件路径进行两次编码加密

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F4YBmKpyORg5ufoRzU2fTDpkzvFXZI475z5NqLj2luzvHjSgAia23nFQ/640?wx_fmt=png&from=appmsg)

将所有加密后的信息拼接

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7Ffia7U81nvibs4bebaAGwVtlu7kgLS6X47KdjuDwvtXJevAUXIXicMiahyQ/640?wx_fmt=png&from=appmsg)

以POST的方式发送至C2：hxxps://weixein.info/1WrCVzW4kSDNbNTt/cqWf4vQlofzqFkc7.php

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F6eLDxAkvfo8ibq8jeZH4gz49FjCm8c5AUOgfq4knRreic7IaPCnjSefg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FmJX9704kZfqib29mH0XBMS3fa00sHKccON2iaVnHCyVTuYF351Kq6lZg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FXjJNsicCMmiapEFtXwYU42SCgu8pVcCNgkricB7x1icvoqd8Y8WIEo8jTw/640?wx_fmt=png&from=appmsg)

C2返回指令以"$"符分割，包含的部分指令及功能如下

|  |  |
| --- | --- |
| 指令 | 含义 |
| 3hdfghd1 | 读取指定文件，加密后上传至C2 |
| 3gjdfghj6 | 创建cmd进程执行指定指令，并将执行结果加密上传 |
| 3fgjfhg4 | 遍历文件及目录 |
| 3gnfjhk7 | 从指定URL下载后续负载保存到本地执行 |
| 3ngjfng5 | 仅下载文件 |
| 3fghnbj2 | 屏幕截图，加密回传 |
| frgt45f | 创建线程执行cmd指令 |

● 3hdfghd1：读取指定文件，加密后上传至C2

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FxqKN6CELHibM8wJfhNukvvfTXsMkvYESSEias4QIQ1xtXyC60UPXxxBw/640?wx_fmt=png&from=appmsg)

●  3gjdfghj6：创建cmd进程执行指定指令，并将执行结果加密上传

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FvicZJrNibNdJbwUSHJk0MbHic7G1sMzbvObewEbMthcev2vCHqqZiaia5zQ/640?wx_fmt=png&from=appmsg)

●  3fgjfhg4：遍历文件及目录

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FlAHlkYk7Ebnt77rhEpIVTnCMcSPZoOSvyO0d4fxNw4L1icvfgVMCRRg/640?wx_fmt=png&from=appmsg)

●  3gnfjhk7：从指定URL下载后续负载保存到本地执行

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FZkYhXhicyZGKiap8KJFN0YWB3tEvFpOIehYH9DlqBlFRcIKK0lib6ScWg/640?wx_fmt=png&from=appmsg)

●  3ngjfng5：仅下载文件

●  3fghnbj2：屏幕截图

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FmZYwfwyKnMxFuJXl4EFoK6cnyfdmdZVpib3sTlMibKxBCNdfclYmhFFw/640?wx_fmt=png&from=appmsg)

●  frgt45f：创建线程执行cmd指令

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F5acGtfpyibK0AeQsEla49QzEwF27B8k3zI9ugVVIPmPY3zMWZWJeM8A/640?wx_fmt=png&from=appmsg)

**4**

**关联拓展**

我们的狩猎规则捕获的Patchwork组织近期的其他攻击样本如下

|  |  |
| --- | --- |
| **文件Hash** | **文件名** |
| 36c3aa180b8466d94b34397d786c913cc83bb33dbb1d6cc3bda0c83bd2392122 | SMSAPI\_Gateway.pdf.lnk |
| 30024cadaf9aead441d926132c2a83aa478aa153e02a5b248b4c0dec33fcab94 | Internal\_Audit\_Report.pdf.lnk |

两个LNK文件均上传自巴基斯坦，与本文分析的LNK文件连接的二级域名相同，释放的白+黑文件一致，仅在诱饵文件上有所不同。

此外，我们的狩猎规则还命中到该组织使用AsyncRAT的攻击链与本文相似的其他加载器。其中涉及的证书信息如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F1Im2SCuplfNtXianu5vpCJrGARpw7T6VvFiaEDUXibHNqVZIk17w73dQw/640?wx_fmt=png&from=appmsg)

**5**

**域名分析**

**1**

**weixein.info**

域名注册于2024年11月8日，主页面仿冒加拿大新闻网站Global News，点击任意新闻均会跳转至官方网站globalnews.ca

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7F6odTicYmNqRX8IWsHfeHnJtBpCia2ZJF2mp4sv7XmjrwWOJTvG07GuIA/640?wx_fmt=png&from=appmsg)

该域名解析到的IP：91.245.255.60曾在24年7月绑定域名mingyn.org，经网络资产测绘，该域名同样为Patchwork组织资产。

**2**

**sheicen.info**

该域名是我们捕获的Patchwork众多恶意负载之一连接到的C2域名，我们通过网络资产测绘，发现了该组织于2024年11月25日注册的最新域名youdoa.info，该域名解析到146.70.113.198。目前未发现有关联样本。其主页仿冒北欧航空SAS，点击任意链接即跳转至官网flysas.com

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvneQ9bDln4eD9CWmicYTOtV7FqoFKILt1Undic6J8F0VWWiblraSXqRSZR1laG46VFj5VnNWDszHRbGJA/640?wx_fmt=png&from=appmsg)

**6**

**IOC**

本次攻击活动中的文件Hash

12cf713242ae7eb11eceddbcc535f562f16e5be645f07a87e805e7f4f81b362a

7250c63c0035065eeae6757854fa2ac3357bab9672c93b77672abf7b6f45920a

通过基础设施及样本特征关联到的文件Hash

b66434960ea4669d66ddefa173b10207dd4d6bbc5c46f55b9c9e7706fd16f18e

8143a7df9e65ecc19d5f5e19cdb210675fa16a940382c053724420f2bae4c8bd

858f47433bbbac47ca53e2b525669ab130c460b3f1b2c8269cf1ee8e47477f1e

0dbf54244cb9c115e59f9951c6450f91b684d6d5ec5e1a27be397b3b96ef5430

c01a763ce686f464d2d633f16ddb37e2032b91c10f36e3f187760fb6d7374223

74ce1c5bfdfd095a974b5457aa13cb2912fd2f3fe00558793bdb02907dbfd3ce

报告涉及URL及说明

|  |  |
| --- | --- |
| **URL** | **说明** |
| hxxps://atus.toproid.xyz/klhju\_rdf\_gd/ktdfersfr | 下载文件到本地C:\Users \Public\Project\_Guideline.pdf |
| hxxps://zon.toproid.xyz/pfetc\_ksr\_lo/jyuecvdgt | 下载文件到本地C:\Users\Public\ WerFaultSecure.exe |
| hxxps://zon.toproid.xyz/aewbf\_jsd\_td/ktrgdysvt | 下载文件到本地C:\Users\Public\wer.dll |
| hxxps://weixein.info/1WrCVzW4kSDNbNTt/cqWf4vQlofzqFkc7.php | 窃密信息上传及后续负载下载地址 |

通过基础设施及样本特征关联到的URL及说明

|  |  |
| --- | --- |
| **URL** | **说...