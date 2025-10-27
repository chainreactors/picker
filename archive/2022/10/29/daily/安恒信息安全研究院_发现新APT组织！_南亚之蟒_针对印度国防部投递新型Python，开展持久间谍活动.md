---
title: 发现新APT组织！"南亚之蟒"针对印度国防部投递新型Python，开展持久间谍活动
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247491768&idx=1&sn=feaa2d3edf35804e3aade515dc351fde&chksm=f9ed8c07ce9a051165e1fc83a8075296aebe35632cd408fd018357734929cef2367c1b261bde&scene=58&subscene=0#rd
source: 安恒信息安全研究院
date: 2022-10-29
fetch_date: 2025-10-03T21:14:26.428431
---

# 发现新APT组织！"南亚之蟒"针对印度国防部投递新型Python，开展持久间谍活动

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvnfm8O0049g6ADNiav7micjvXyGQE1xn36M2yE9EkKJfszfH55PsOp3ic7czqt68GU7asjs3043W56ovw/0?wx_fmt=jpeg)

# 发现新APT组织！"南亚之蟒"针对印度国防部投递新型Python，开展持久间谍活动

原创

猎影实验室

网络安全研究宅基地

**点击蓝字关注我们**

**南亚之蟒--APT组织针对印度国防部投递新型Python窃密软件活动分析**

- by 猎影实验室-

**概述**

近日，猎影实验室捕获到南亚地区“网络冲突间谍战”中的恶意文档文件，文件运行后将加载远程模板中的宏代码执行，后续在本地释放PyInstaller打包的文件窃密器。

      此活动主要针对印度国防部下设的CSD部门，与已知APT组织常用的攻击手段有较大差异。猎影实验室将其以内部追踪代号“APT-LY-1004”进行跟踪。活动大致攻击流程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5DpdkNpvxicV2cKOHwRSVgeK9tWTm35xic2mmTRzgwnuxyGGU8U8icajgw/640?wx_fmt=png)

**分析**

**1**

**第一阶段**

样本信息：

|  |  |
| --- | --- |
| **FileName** | Anaya shoot feedback.docx |
| **Hash** | e64399c152f9bedd3ca54cccdab6469e |
| **Submitter** | IN |
| **DownLoadURL** | hxxps://templatesoffices.com/en-us/letters/tm83/csd/flyer.png |
| **FleName** | flyer.png |
| Hash | 8cf97f8f60792dc2c7b9dd0ab55b0bd2 |

文件内容：提示启用宏以查看文档内容

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg53yq3AnA9OrUsibbbmib4eE1nMt07OGiaLYJpBYicAMFophnOUoduoELkXg/640?wx_fmt=png)

**1**

**第二阶段**

远程加载的flyer.png文件包含宏代码功能如下：

|  |  |
| --- | --- |
| \_ | 检测运行环境：通过WMI获取计算机系统信息以及进程信息，若本机系统为VMWARE、VIRTUAL、QEMU、RED HAT或XEN，则函数退出；若本机进程中运行FIDDLER、WIRESHARK、PROCMON、PROCEXP、SURICATA或SNORT，则函数退出  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5Vf7AfebkAHkibyCm3qqmdyQia4SoX89LGbydpn1kz3caAgZFGDIOam5g/640?wx_fmt=png) |
| \_ | 获取本机目录%AppData%\Microsoft\Windows\INetCache\IE\ |
| \_ | 在本机目录%AppData%\Microsoft\Windows\INetCache\Content.Word\{随机字符}路径下创建{随机字符}.zip |
| \_ | 遍历%AppData%\Microsoft\Windows\INetCache\IE\子目录查找flyer[1].png文件  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5iaHgru2wgegHXQaaGttORgVcH2y8bKrlmXr0BIUWMlvT4TgrT33o7Gg/640?wx_fmt=png)  文件flyer.png被远程加载到本机，存放在如下目录  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5DyXS1fZq2IAsat1leYFYJmAA4ibFlAjZou5h33icGspZtovk58xOZbtA/640?wx_fmt=png) |
| \_ | 打开flyer[1].png读取数据，将"@@@===@@@"字符串后的内容截断并写入{随机字符}.zip |
| \_ | 将ZIP文件中的document01.docx解压、theme01.xml释放到本地\System32\spool\drivers\color路径下重命名为sppsvc.exe  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5icu1icmhnV9cPx3owZ0M186IiaS6jwKp2w4tIc1OY1Qg1uc5NuyhXWM7Q/640?wx_fmt=png)  释放文件所在路径如下图所示  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5N12mHq6OiblV78sebDHU3ichdednkBYcfDfsfuw4Rh9cofCKfrlZwtdA/640?wx_fmt=png) |
| \_ | 通过创建计划任务实现持久化操作  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg57Du7AJMtrtTqsicpcl3F7yxmrDzN6K0FNk35RicCV89JEia93N4Jt8iaDQ/640?wx_fmt=png)  创建名为MicrosoftUpdateTaskMachineUA的计划任务，每天下午11:40、每隔15分钟带参数启动程序sppsvc.exe。  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5oXgtV1oicnLXcuKuRr6eJo115sibrtkddvC4n8eibmWW8HZqAJmUokUibg/640?wx_fmt=png) |
| \_ | 删除%AppData%\Microsoft\Windows\INetCache\Content.Word\{随机字符}目录以及%AppData%\Microsoft\Windows\INetCache\IE\目录下文件  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5zWH1lpcYsmialfJLfTibibAonb49aynibtNYiagfxM0jiafd3mSknibIiakNnw/640?wx_fmt=png) |
| \_ | 打开document01.docx诱饵文件迷惑用户，诱饵文档内容为CSD摩托车品牌价格清单  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5nrF2VbAOR8q9O5U7T4qXlgAoyjT68VnBOtVGGJhnIX06qlfVRy02BA/640?wx_fmt=png) |

**3**

**第三阶段**

释放在本地的sppsvc.exe为PyInstall打包的二进制可执行文件，执行参数为“FE9FC-289C3-FF0AF-142B6-D3BEA”。

**01**

**通过计划任务带参数启动**

|  |  |
| --- | --- |
| \_ | 获取主板品牌、产品型号、UUID、序列号、CPUID、制造商、计算机型号、反病毒软件信息等 |
| \_ | 将UID、用户名、CPUID、序列号、产品型号、主板品牌等进行格式化输出  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5QMOQBicvqV6Uhkh98drJ75u9VU2dWxQcYU15R5aR2wia44kuicj8UhpibA/640?wx_fmt=png) |
| \_ | 获取出口IP以及所在地域 |
| \_ | 将序列号、用户名、主机名、MAC地址、IP、CPUID、操作系统信息、计算机型号、反病毒软件信息、出口IP、所在地域等一系列信息以JSON格式上传至hxxp://149.28.241[.]241/T729D734B881E4336C393BDB056B167FD.php，标识为'T': 'CA'并等待指令回传  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5KazxncOVKq7uax40ibB6Gh1HMDph8wRlwL9icYmtR9PXwJH5vFElnxpg/640?wx_fmt=png) |
| \_ | 若服务器返回值为“-X”，则创建一个无限循环的线程再次上传本机指纹信息，标识为'T': 'CC'并等待指令回传  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg56xlJyc5uf2DQVKxoNuzfoZyibnlq736ZAiaaQnba8WpEWZ7qcDfRJIcA/640?wx_fmt=png) |

可执行的指令及指令功能如下表所示。

|  |  |
| --- | --- |
| **指令** | **功能** |
| DS | ●遍历盘符，创建进程获取.doc、.docx、.odt、.pdf、.csv、.ods、.xls、.xlsx、.odp、.pps、.ppsx、.ppt、.pptx后缀文件路径写入本地..\AppData\Local\ihost\list.log，在..\AppData\Local\ihost\stats.log中记录“Status = 3 ”以及3天后的日期    ●读取stats.log，若存在标识“Status = 3”，则获取uuid、序列号等信息并上传list.log中的本机文件信息，若上传成功，则在stats.log中记录“Status = 4 ” 以及3天后的日期 |
| DU | ●读取list.log，以其中5个文件为一组，上传文件内容至服务器，并记录已上传的文件信息防止重复上传 |
| DX | ●读取stats.log，若存在标识“Status = 3”，则获取uuid、序列号等信息并上传list.log中的本机文件信息，若上传成功，则在stats.log中记录“Status = 4 ” 以及3天后的日期 |
| DSU | 包含以上三种指令功能 |
| EX | 退出 |
| 其他 | 创建管道执行任意指令，并将执行结果记录至..\AppData\Local\xELogs.log，随后上传xELogs.log |

**02**

**不带参数启动**

执行上述指令DSU，相关功能代码如下：

|  |  |
| --- | --- |
| \_ | 遍历盘符，创建进程获取.doc、.docx、.odt、.pdf、.csv、.ods、.xls、.xlsx、.odp、.pps、.ppsx、.ppt、.pptx后缀文件路径写入本地..\AppData\Local\ihost\list.log，在..\AppData\Local\ihost\stats.log中记录“Status = 3 ”以及3天后的日期  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5ERGvcOcVrMm5wr6zNMm8iahY8BibzNdEf0x45tKQQ8d1TicibfYSBcOnfg/640?wx_fmt=png) |
| \_ | 读取stats.log，若存在标识“Status = 3”，则获取uuid、序列号等信息并上传list.log中的本机文件信息，标识为'T': 'FDU'，若上传成功，则在stats.log中记录“Status = 4 ” 以及3天后的日期  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5fchww1BtficauNvQpBcz6V49ZaIqFt8dAx4asCnTtSZckm2E94ibYwEQ/640?wx_fmt=png) |
| \_ | 读取list.log，以其中5个文件为一组，上传文件内容至服务器，并记录已上传的文件信息防止重复上传  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg50R4EZKHlSKgpsSqpZ2dfibhAxCzl96GFA1hql3ia8RvicAnTU14850UXw/640?wx_fmt=png) |

后门窃密上传本机文件及对应的标识如下表所示：

|  |  |
| --- | --- |
| **指令** | **功能** |
| 'T': 'FDU' | 指定文件内容，例如list.log、本机其他文件内容 |
| 'T': 'CC' | 本机指纹信息包括uuid、序列号、主板品牌（制造商）、产品型号、CPUID以及操作系统名称 |
| 'T': 'CA' | 指定json格式数据 |

**思考总结**

**此次捕获攻击活动主要包含以下特点：**

1

活动针对印度国防部下设的CSD部门（Canteen Stores Department，南亚地区多个国家国防部均设此部门，专为武装部队人员、退役军人和国防文职人员购买日用产品所设，提供曲别针、汽车等4千多种产品）；

2

活动通过CVE-2017-0199漏洞利用样本下发后续包含宏代码的远程模板文件；

3

活动最后阶段部署Python后门对目标人群进行持久化文件窃取。

**此次捕获样本主要包含以下特点：**

1

样本需要运行于Windows 8及以上系统。宏代码查找远程模板在本地中的缓存时检索的IE临时文件夹为INetCache，Windows 7中存放IE临时文件的文件夹为Temporary Internet Files；

2

样本对虚拟机环境（VMWare、Virtual、QEMU、Red Hat、Xen）及调试环境（Fiddler、Wireshark、Procmon、Procexp、Suricata、Snort）进行了较为全面的检测；

3

样本中存在用于标识并截断压缩包数据的字符串”@@@===@@@“；

4

样本将后续负载释放在了“非常规”目录：ICC配置文件目录“C:\Windows\system32\spool\drivers\color\”；

5

样本在后续负载释放完成后将删除过程中产生的承载文件；

6

后续负载通过注册表实现每天固定时间、每十五分钟带参数“FE9FC-289C3-FF0AF-142B6-D3BEA”启动；

7

后续负载为PyInstaller打包的窃密器，主要功能为窃取指定后缀文件上传以及执行任意cmd指令。

猎影实验室发现该组织在攻击目标、攻击目的、反病毒检测、持久化操作等方面符合APT攻击活动特点，且与已知APT组织常用手段有较大差异。猎影实验室对其以内部追踪代号“APT-LY-1004”进行跟踪。

**防范建议**

目前安全数据部已具备相关威胁检测能力，对应产品已完成IoC情报的集成：

●安恒产品已集成能力：

针对该事件中的最新IoC情报，以下产品的版本可自动完成更新，若无法自动更新则请联系技术人员手动更新：

（1）AiLPHA分析平台V5.0.0及以上版本

（2）AiNTA设备V1.2.2及以上版本

（3）AXDR平台V2.0.3及以上版本

（4）APT设备V2.0.67及以上版本

（5）EDR产品V2.0.17及以上版本

● 安恒云沙盒已集成了该事件中的样本特征：

用户可通过云沙盒：https://ti.dbappsecurity.com.cn/sandbox，对可疑文件进行免费分析，并下载分析报告。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5hV9KEsXtz0a5ibGU1PDBkQB0PunFEKIwDj3S5Y0F7eN0icnVUTZlQNow/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5M3jqfz0uIQgDCHN2SS4swadzv8ceAYINqTCqSicnhP5jn9vB5L3ux6Q/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5ATevjibznuw1GBEN4dPSpYY3HeAl2EicBrOT7Gkzmib53Dic3GGU2ibPnVg/640?wx_fmt=png)

**安恒信息安全数据部，**下设猎影实验室、零壹实验室、析安实验室和回声实验室，团队以数据分析与技术研究为核心，致力于数据驱动安全创造用户价值。

**猎影实验室**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5JPthzwX1CQexz66Gyna4xd7fc3djibAoEauLXwYLO9IB6lFqshqOXKg/640?wx_fmt=png)

高级威胁研究团队，专注于APT攻击发现、分析、检测、溯源、防御等研究，以及积累了海量的IoC情报数据。

**网络安全研究宅基地**

![](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvnfgibLJN5gwWtADGzCia1kWg5YoKf1EYSsrITibFtGUhVIyiaACq4GzJ9JZEicMowPadgmF...