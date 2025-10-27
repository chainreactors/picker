---
title: 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247517657&idx=2&sn=2f51956b98579e2d88d0631e9256a236&chksm=ce460ec9f93187df29927440bb9410465012abbeead3fa7c5e55d5d1899bea4ccdc29f8213fb&scene=58&subscene=0#rd
source: 深信服千里目安全实验室
date: 2023-03-07
fetch_date: 2025-10-04T08:49:42.486130
---

# 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0Jb5cdCbTRslGqVBp8y8qdjh5XqolJOn84Kx8BU2hUfkLAo7wEicHX7WA/0?wx_fmt=jpeg)

# 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来

深盾终端实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0J2dcmDSoEKoj2rJbKAr7U71IDgNTA5x5WdPBLNiad0f81UFg8wgyjX8A/640?wx_fmt=gif)

**恶意家族名称：**

AgentTesla

**威胁类型：**

间谍软件

**简单描述：**

2023 年 2 月 13 日，深信服 XDR 捕获新型间谍软件。

**恶意文件分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JxaXVrCo7EdrQPYXickA9QBMUwK90uOIy9vwCJe84xqpPQaQmVM8EAZw/640?wx_fmt=gif)

**恶意事件描述**

2023 年 2 月13 日，深信服 XDR 捕获新型间谍软件，此次事件中的恶意程序通过钓鱼邮件传播，当受害者解压邮件附件并执行其中的恶意程序之后，该程序会通过 PowerShell 添加 Defender 扫描白名单并创建计划任务，之后执行窃密操作。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JxaXVrCo7EdrQPYXickA9QBMUwK90uOIy9vwCJe84xqpPQaQmVM8EAZw/640?wx_fmt=gif)

**恶意事件分析**

通过进程执行链可以发现该样本是通过钓鱼邮件投递，受害者解压之后执行。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0J5ic9qvVhwIza6oDmzdeibIuP4f846wCSWYBPsJbicguFnuz25uwfgwm5Q/640?wx_fmt=png)

该样本是一个 .NET 编写的窃密程序，通过对资源节区的数据进行解密还原出恶意模块，然后使用反射加载的方式执行该模块。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JtyJpHMibgrxZTKicUakKWNnQTxM4ia9NvyvA6qc4pFslrGia606WQo6rSw/640?wx_fmt=png)

调试发现该恶意模块名为 B4000。入口函数为Melvin.White。跟进函数，首先使用Sleep 休眠了 44s，在对一段硬编码的数据进行base64解码后再解压缩，还原出一个 PE 文件。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JAq9NVXIEicImt0vEFvLpopsicEqq2T627EvSkwKCQD7CvVGdgbibA8oLA/640?wx_fmt=png)

同样使用反射加载的方式加载还原出来的 PE，名为 Cruiser，在通过加载模块中的函数从图像中提取出另外一个模块 HIVacSim，同样使用反射加载。找到模块入口函数如下：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JFUzKOPLe0oIjzqPWPPSuJ9YYtmU6yNW9Ud8H2COkXZCSthTJDzPaAg/640?wx_fmt=png)

进入模块之后会执行一系列恶意操作。

**释放文件**

从资源节区中释放文件至 C:\Users\UserNAme\AppData\Roaming\NgsWWESFAPv.exe

，释放的文件与当前文件一致。

**创建计划任务**

通过schtasks.exe从XML文件中创建计划任务，二进制文件指向`C:\Users\UserName\AppDataing\Romaing\NgsWWSFAPv.exe。`

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JJvavfslkqHicZN9Ha2yCia7iaGtJzvIhiaGKQkwJ9ib7cHobAcKCpiaiag57g/640?wx_fmt=png)

**添加Defender白名单**

通过 Powershell 添加 Defender 白名单。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JAUicVM5gpyZUcvqe767I8MgmPMkM5uDhk7ibrYKQk8pxicl5WTWpb9oug/640?wx_fmt=png)

**创建傀儡进程**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JbBv5c6CqLqVsOAREJnDIMFpew1j4m1caWoo7QsOjCHpoeOxuG58OMw/640?wx_fmt=png)

**创建傀儡进程步骤大致如下：**

1. 通过 GetThreadContext 获取线程内容

2. 使用 ReadProcessMemory 读取进程内容

3. 使用 VirtualAllocEx 在傀儡进程中分配空间

4. 使用 WriteProcessMemory 往分配的内存中写入数据，

5. 使用 SetThreadContext 设置执行入口。

6. 使用 ResumeThread 恢复傀儡进程的主线程。

在 SetThreadContext 处下一个断点，找到傀儡进程入口点：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JhATOPEt24iacn3DVclJCJMwCgOB6H6LFhhm5q1M8sR5mZSmfrnYw67g/640?wx_fmt=png)

在写完数据并激活傀儡进程之后当前进程就会结束，导出写完数据的傀儡进程继续调试。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JZtpTgkVKZDmqD4LEdjXz8qDgQR31RIqJ5DLjGnv3XdC82GFgcVVKKQ/640?wx_fmt=png)

**信息主机收集**

通过 Win32\_BaseBoard 获取主板信息，之后获取主机和用户名信息等。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JvsIm03grkPDyicKPmFfHb0qcm8UPFxz8A1lDnX0GLyNYHHZ8IT27buA/640?wx_fmt=png)

**获取公网 IP**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JAIORq8ibazAapBctQ1urHmx0Z2X94kXBXve7pLF2FDnnfDqgZjDdMxQ/640?wx_fmt=png)

**收集软件信息**

收集多种浏览器信息。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0Ju7AxMksBkCU0hu5n8IkfM5FxUicn5qSQ1SKKFBotLlgWYKJDRUWPwyg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0J1YUVFE6DGrJClfAWTwTC4EcVJZNEhBAdSIyqU7811qpthbE6jkg7nQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JN4WUn5ibZPuGYNpLmQj7dZKyKdpGzYkgottNvSbCztJ4LbHPrAoQ2icA/640?wx_fmt=png)

在多个 try catch 中收集特定安装程序的数据：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JbOzlJhbqTLE4nlSZT8QhO1JsUfour2sBVEj9kSITdfEm37JUS6QMOw/640?wx_fmt=png)

包括 discord、Claws mail、eM Client、FileZilla、Foxmail、FTP Navigator、WinSCP、RealVNC、MySQL 等程序、以及系统凭证等信息。

**发送数据**

将收集到的数据进行处理之后通过邮件发送到特定邮箱。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JhiasRicWBzBPsdgbyzlmRgtiaq167qO7E8kZEQoIoU5myo0lVMMK6CIlQ/640?wx_fmt=png)

**解决方案**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JxaXVrCo7EdrQPYXickA9QBMUwK90uOIy9vwCJe84xqpPQaQmVM8EAZw/640?wx_fmt=gif)

**处置建议**

1. 删除计划任务

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0Ju4leWpJddI3yh13bicNpb7jbAVAiaESFngUsrVowcO0mjfDSoMRpGotw/640?wx_fmt=png)

2. 取消 Defender 白名单

3. 终结该进程及其子进程并删除对应文件。

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0JxaXVrCo7EdrQPYXickA9QBMUwK90uOIy9vwCJe84xqpPQaQmVM8EAZw/640?wx_fmt=gif)

**深信服解决方案**

**【深信服检测响应平台 XDR】**已支持检测该新型木马的恶意行为，请更新软件（如有定制请先咨询售后再更新版本）和 IOA 规则库、IOC 规则库至最新版本，设置相应的检测策略，获取全方位的高级威胁检测能力；

**【深信服终端检测响应平台 EDR】**已支持查杀拦截此次事件使用的病毒文件，请更新软件（如有定制请先咨询售后再更新版本）和病毒库至最新版本，并接入深信服安全云脑，及时查杀新威胁；

**【深信服安全运营服务】**通过以“人机共智”的服务模式帮助用户快速提高安全能力。针对此类威胁，安全运营服务提供安全设备策略检查、安全威胁检查等服务，确保第一时间检测风险以及更新策略，防范此类威胁。

![](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5zWSibPB7Y20xYB8EOibmiaib0J36BDRJzbJhiad7xC3KxfUZXGOLDHCLEXlabCtpVe1OGpqv5wIMXaZjw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

深信服千里目安全技术中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5xUEmJGibg2JE8nVwwxzibBrJTEzuyfhPTuTZeyvTviay6rzGOGrHkAO45vyyibnV1FZThckmmfFfM6BA/0?wx_fmt=png)

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