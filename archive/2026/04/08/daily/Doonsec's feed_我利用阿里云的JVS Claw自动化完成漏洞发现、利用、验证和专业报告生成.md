---
title: 我利用阿里云的JVS Claw自动化完成漏洞发现、利用、验证和专业报告生成
url: https://mp.weixin.qq.com/s/q9ORxsure0LM3CLr-zThIg
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:26:55.566740
---

# 我利用阿里云的JVS Claw自动化完成漏洞发现、利用、验证和专业报告生成

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lLNNhhDrAC4JibFIapFlMvdvft3ciaVwYGd8ApUPW4JYYD28arFwSicS9I72ULoWHfzfGFFQd0IztzwhVHU9drQjCG2fRGiacbsjRCicDyWV3nCA/0?wx_fmt=jpeg)

# 我利用阿里云的JVS Claw自动化完成漏洞发现、利用、验证和专业报告生成

原创

suntiger
suntiger

二进制空间安全

![]()

在小说阅读器中沉浸阅读

### 产品背景

###

  JVS Claw(Just A Rather Very Intelligent Steward)是阿里云旗下新推出的一款集成了AI智能助手与云端独立环境的创新产品,JVS Claw的核心目标在于“执行”，用户可通过简单的自然语言指令,驱动Clawbot在隔离、专属、安全的CloudSpace云端环境中操作应用、处理文件、完成复杂的任务。

### JVS Claw支持云端和本地两种模式自由选择。云端免装即用, 彻底释放本地算力。环境安全隔离, 支持随时随地远程观察与实时干预; 本地支持一键极速部署,数据完全留存本机, 深度接管终端环境，安全高效处理私密本地文档。

### 产品官方URL:https://jvsclaw.aliyun.com/, 用手机验证码直接登录到控制台界面如下:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC4Z7qE9IicAEHE5sWLYvYmibD6PKcIR9RXrlM5TGkrzOibZzIPDKBVK6x5p18sjt0ibbe9gmsCibelXZ0mNxpkIgECqWQOwIa1GZdGc/640?wx_fmt=png&from=appmsg)

### 在该界面中, 我创建了一个云端Clawbot, 今天的任务主要用来做代码安全审计, 看看能否自动化帮我检测出一些安全问题或漏洞。

###

### 云端分析环境操作

###

### 点击已创建的Clawbot对话, 便进入到下面这个界面:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC4UV3Vf8gPiaDfMoVg7QrX4B2Mpdqt486ZAV0cmlVnTJoZ4lHD7jsyqTqog5ymCJtYoqj8brFA5ry0Wicycjqhf340fDLG92LU7E/640?wx_fmt=png&from=appmsg)

### 在该界面中分为两个部分,左边可以用自然语言进行指令下发, 右边是一个可视化的云桌面。点击右边云桌面顶上的绿色长条,可以看到有三项互动功能,包括:状态检测、虚拟键盘和文件传输, 如图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6nlazJtB9qD2TMFCiaN0Ib2TMEt1hia9naa8sltldpUuic2yeTFuu7nxiaicUGvLicESE9bvUHib88FdGUJ6x7uNEt1jQIYnVMFdnVr0/640?wx_fmt=png&from=appmsg)

### 在这里的虚拟云端环境中,实际上是一个可以直接使用的OpenClaw环境, 可以在界面上直接点击操作, 但不需要用户进行任何安装和配置,只需要关注自己的工作内容即可,如图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC7BkLbicA3ibpn4MfW9IvNao5RYodcuhg19vONZ3PLicpkeB4wkpicxwO3cMsaL2KeVTB0OM1Y5icRhE3J4XJCCZbBIzp7Xp6aicE30Y/640?wx_fmt=png&from=appmsg)

### 因为在云端环境无法直接操作我本地的文件,所以我要将审查的文件通过文件传输功能上传到云端虚拟环境, 以下是文件传输界面：

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC5LFy7TI3fGyxOaI3NMrSveBmQibktAENHvV5dPu9NlhibeOF2Uc4NdibjKlR6FGTy8VCw330Z6Yqs8kR8zMOStKksd90tTOGgtjU/640?wx_fmt=png&from=appmsg)

### 文件传输这里主要提供了上传和下载文件的功能。

###

### 默认支持技能

###

### 点击控制台左侧的"技能",可以看到默认支持的技能,如图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC53z1ibzSrQMaicDbMicQiatRkP5VLkicvDBQz40ou6H4oicgbkyEvic4icXVJOSbLwDf2goQdtkFicibib2BsoGryIykSqzDvcBiaVmVtxAa0/640?wx_fmt=png&from=appmsg)

### 点击每一个技能, 可以发现里面比较贴心的告诉你如何使用自然语言来使用技能,如图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC4hUVHtoqibLnQXOtdqH8IicQ16nUEVX3cX3cAGFTyDqkyZ19Q6UyvECRa8aI7xlNLwzVgZvcYc6JYgRfqZrgBwbcHAjE9Pibdicp4/640?wx_fmt=png&from=appmsg)

###

### 工程代码安全审计准备

###

### 代码安全审计是一项系统化的安全评估工作,通常遵循一套完整的流程,包括:准备阶段、静态分析阶段、人工审查阶段、动态验证测试阶段、风险评估阶段、报告编写阶段、修复验证阶段和持续改进阶段。下面我将利用JVS Claw来协助实现从准备阶段到报告阶段的全过程。

### 首先利用文件上传功能将需要审计的代码文件上传到远程环境, （注意:如果是单位文件或重要保密资产,无论使用什么方式,都不要喂给大模型进行操作。）目前文件上传功能还无法支持文件夹上传,先打成一个tar压缩包上传, 如图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6O7ib3wSIbzw7Lry9OUpxKxqZckvd7h98hmMtKlnW7gbiaNMvdX96LHbFBApicJ9uAicXvT7fT9w9uZzrmAOMibzdIs7hNgeavKdRM/640?wx_fmt=png&from=appmsg)

### 将tar压缩包上传之后,在界面中将其解压成文件夹,到此待审计的工程文件准备就绪,下一步将利用JVS Claw帮我分析这个未知工程究竟是干什么用的。

###

### 工程结构自动化分析

###

### 工程结构化自动分析,实际可以替代代码审计准备阶段中的诸多工作,包括:确定审计范围、收集工程相关资料、确定审计方案等。

### 围绕上面的工作思路,打开JVS Claw聊天对话框,输入以下语言指令:

```
请分析一下/home/Downloads/vuln-bank这个工程是做什么的?工程的结构是怎样的?源代码量在什么级别?用什么语言开发?请用树状图表示出每个功能模块之间的结构和功能作用批注。
```

### 在经过一小段时间的分析后, JVS Claw给出了分析结果,首先是项目概述和技术栈,如下图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC7M2gxy9iaNYLJ6ZkdAVON7zApaZayPflVM0fWhqibshHzicoO3Y0EKBJ1t5HjEzgPos4duhGbppJHzt2VjTdwPtXG5lNu5qNHhno/640?wx_fmt=png&from=appmsg)

### 由此我可以快速掌握一些关键信息,例如:这是一个基于Python源码的审计工程,由于是故意设计存在安全漏洞的Web程序, 预计检出的漏洞不会少。下面继续看一下源代码规模：

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC45wQtV9VPlo0Kia6WvaHEnSIM3yTjFJbYMPYSO4K61OCu4kH32oWgAiciarQrTAAA4e0OHrCo86L8ia1XoQRxic6y2xhPnkicvqftks/640?wx_fmt=png&from=appmsg)

### 源码的规模不到4000行, 属于一个短小精悍的小型项目级别, 最后是关键的系统架构图和源码功能树分析:

### [系统架构图]

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC4bhF0Iia7J2E8UtxhzgHMQMGfXotcibbZtdLnned5djiacuDs19AdmtibOKTPndfZFJVp6gRM8deEIsibSH75yVKVxmt5jhgbdwQ0s/640?wx_fmt=png&from=appmsg)

### [源码功能树(截取部分)]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC6NneuEp2vstFqUTQJibUCjIibHjX1MLYvdgQjVAPkMDQlmjm9bTjCds0vJsLp5kntJykQ4MVb0AGiay6hwhZrdkJg9DuUhlISxIs/640?wx_fmt=png&from=appmsg)

### 至此,在不到30秒的时间里,我已经将该工程的系统架构、源码功能、代码规模、技术栈等信息全部掌握。下面将可以快速进入漏洞分析和评估阶段。

###

### 漏洞分析和评估阶段

###

### 在传统的代码审计流程中,静态分析、人工审查、动态验证、风险评估这四项工作缺一不可,而如今在JVS Claw的加持下, 这四个阶段可以合并为漏洞分析和评估, 所有中间细节将被自动完成。继续在聊天对话框中下达以下任务指令:

```
分析工程/home/Downloads/vuln-bank中所有可能存在的源码安全问题给出漏洞信息;所在源码位置、行数;漏洞原理和利用方法;给出漏洞利用的POC;给出漏洞补丁方案。
```

### 这个任务总共包含了6项需求, JVS Claw通过对整个工程的源码扫描,给出了以下结果。首先是漏洞分析概览信息,如下图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC76qpzkibBsEh742dOQkw16m6iaw9zyvzjIEDbh2IJNdgljjibW2f9FibpTsVbgF8Rq2mwYgzomYsFrrS68TVjmYvaZ3VbdKM92es0/640?wx_fmt=png&from=appmsg)

### 包括每种漏洞类型的数量和风险等级都用不用颜色进行了标记, 总共从源码中发现了超过85个独立漏洞点。

### 下面从其中摘出一个SQL注入漏洞查看一下详情:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC72lM7ZmRI6X81aArNCy9ia0vC9HR9aONGNuLEjKup38xEibpT4mkuGXKibS1Y6AyLwuRpImhB6rbJOeJ82aww8BiarG6pV0qMR47s/640?wx_fmt=png&from=appmsg)

### 不仅给出漏洞所在文件的行号,还准确的定位到漏洞代码,并给出漏洞产生的原理,下面是JVS Claw给出的三个POC:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC5RYEzuKwUiaGjt4Az2iaY0tMOJaXWf1O1icU1EQXPLr0oUunLdsb0xJaF2RFsu422JG5GOWRiaUL9zmXLRUXEnWpZEQuGj6Pe5iaCs/640?wx_fmt=png&from=appmsg)

### 最后是修复方案:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6lLL8icYJX7PW8jrpib3GobHx5mM05ibau9riangHgYoHDG4FbsdMozw3xzpTJicprse7MdyIXWzECrE5ScSGQfCxSKsI9u2uibUpeI/640?wx_fmt=png&from=appmsg)

### 短短不到2分钟时间,我凭借自己一个人, 完成了85个漏洞的分析、评估、POC编写和修复方案的制定, 单从效率上看,已经远超一个团队的效率。下面将进入最关键的POC动态验证阶段。

###

### POC动态验证

###

### POC动态验证意味着要将目标项目跑起来,如果连这件事也不想自己花费时间做怎么办?没关系,试着交给JVS Claw来完成,下发如下任务指令:

```
项目能跑起来，并验证其中一个poc是否有效吗?
```

### 短短的一句话,JVS Claw开始尝试自动化部署项目,通过跟踪发现,JVS Claw首先解决了Docker不可用问题,如图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC6KqibO0tl97LCKiaS7CibkLkDOlWOFGKGQ3ibho2KicBJUsKtxwibxlPcMfApYIjphksWy84ulg9cNqSuwsBHd38bXt6V6Aicxhav26o/640?wx_fmt=png&from=appmsg)

### 紧接着灵活的使用SQLite替代项目使用的PostgreSQL数据库,如下图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6xCcuC7dBJ0VM3LEwWP9QYgyAwCWjdPCVCMmpiaVDRgKDsE9Z9ADx0HcLRlB5jP6wLAI9zBe2qEodfV9HzTYopZXSkTiaVHgVls/640?wx_fmt=png&from=appmsg)

### 最终成功自动完成了项目部署, 并可正常登录系统,如下图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC4ZDwZ1iaWkxPavT2HCdjOuX2FYdFpcnruo18EdicagUHVWzEqaqE7cTpkOCPfLe80wCHnrWMmBk08RIskXY1Ef6wE2ePiboVkyHQ/640?wx_fmt=png&from=appmsg)

### 接着,JVS Claw开始自动化做POC动态验证,如下图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6xw3aGtJwcPfR0o4vufI6xI8bCbqiahAZQnUdOP1hERuMcpr0OomnHq6jjnYAKOibsRPmRuZVqriarb0G7GxTaxfZiaX6zMoQVNR8/640?wx_fmt=png&from=appmsg)

### 神奇的是,中途遇到问题也是自己解决,没有任何人工干预。

### 最终,JVS Claw将发送的请求和得到的响应以及结论全部记录下来,如下图:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC7vWMEQuFNCWXrSg4jvwicUhgzGbm5MQLvy0qxukiahobLMCGDebLyXeCgB6clF4QsXl1oLgj5stEJib16Bl2DV5SkYvPbpbaPedI/640?wx_fmt=png&from=appmsg)

### 到这里,我对JVS Claw有了一个全新的认识, 不仅能自己主动解决遇到的问题,而且还能灵活的做一些替代方案,而不是死磕解决某一个固定的技术方向,到这一步,就只剩最后的漏洞审计报告编写了。

###

###

### 专业漏洞审计报告生成

###

### 既然自动化进行了代码安全审计,并检测出多个安全漏洞,总不能让我自己写报告吧？继续下发指令:

```
请按照标准漏洞分析报告格式,生成一份PDF格式的漏洞分析报告。
```

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC6XVchQd6cnJzZD1H0rGOHzK6I4U9QNicKicobGjNgq2HjURJKKXgcw9RCyxVfwtIDF076N5B7fdicabKmuHTCLDXbZibfSuVQGZHk/640?wx_fmt=png&from=appmsg)

### 在生成报告的过程中,我观察了一下云端虚拟机,发现OpenClaw是通过写了一个Python脚本完成了PDF报告的生成, 如图:

![](https://mmbiz.qpic.cn/mmbiz_png/lLNNhhDrAC62OtvJYLj03h5TibE48LVsbAN6eEpACRFu51FFkrCkjlx22OD2lWoicE4BRS8wZYbvlfib5qlEFcTgicsAK2aCwXYPHtuY2pVk0j8/640?wx_fmt=png&from=appmsg)

### 顺便可以学习一下精美分析报告的生成代码:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC75xzxW1Dj35QrAeINfN8BzIRMpdrNGHIFxy6opZQtMaX10XOA3GctkC76yRU0DO7nicDu27NN7eAA5Byj8DpY0rlko2QGjjstU/640?wx_fmt=png&from=appmsg)

### 打开生成的PDF文件,看一下最终分析报告的效果:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC6iaicINuBv5UfINar3UxdPCrSRloafA9LI0K0tiaVpUFXo75BGrqgW5TPSSQrrgGdLL5HhXicCaygdiabUhcv043VZ3dozVxm4g2Po/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/lLNNhhDrAC5wicHKAiat6XTx3WyF0E1nbqU1vfYAiaACIy5Xs4vYxBWVjpR2frY71jukaQ9YkGXmvUlqDBPgic7iaGrjgFlv6PEXdVsmHKflQs64/640?wx_fmt=png&from=appmsg)

![](https://mmb...