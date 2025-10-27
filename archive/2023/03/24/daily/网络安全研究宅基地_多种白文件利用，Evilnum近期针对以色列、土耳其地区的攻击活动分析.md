---
title: 多种白文件利用，Evilnum近期针对以色列、土耳其地区的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247493745&idx=1&sn=3f7780fa80fe698eb5d95781ad539a51&chksm=f9ed84cece9a0dd87f083fc530279485d904d50d71b27d98a4888e05f3a2b00e7bdc6e198316&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2023-03-24
fetch_date: 2025-10-04T10:31:48.011514
---

# 多种白文件利用，Evilnum近期针对以色列、土耳其地区的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEBPzmV4zA4fUyGTAHoGq80qgfB7p1DiawuDOnW3Z8KsRaic6Uprrkj1cw/0?wx_fmt=jpeg)

# 多种白文件利用，Evilnum近期针对以色列、土耳其地区的攻击活动分析

原创

猎影实验室

网络安全研究宅基地

**点击蓝字关注我们**

**一**

**攻击事件概述**

Evilnum最早是pwncode于2018年5月披露JavaScript恶意软件。2020年，ESET将恶意软件Evilnum背后的运营团伙跟踪为针对欧洲和亚洲地区金融科技公司的APT组织。除金融领域外，Evilnum还针对游戏、电信等其他行业。该组织的攻击手法多样，包括利用各种漏洞、使用恶意软件和钓鱼等手段进行攻击。

      Evilnum组织在攻击活动中部署的恶意软件主要为MaaS恶意软件提供商Golden Chickens的TerraLoader系列：More\_eggs、TerraPreter等，相关代码被另一个出于经济动机的威胁组织Cobalt使用。这些恶意软件具有模块化和灵活的特性，可用于执行各种攻击任务，例如窃取凭据、拦截网络流量、窃取敏感数据等。

      近日，安恒猎影实验室捕获了Evilnum组织针对以色列地区的攻击样本，原始文件为包含有JPG文件与伪装成PNG图片的LNK文件的ZIP文件，其中JPG文件如下图，为英国居民Emily Rose的护照信息，LNK则伪装成PNG图像引导用户点击执行。Evilnum此前常利用居民身份证件信息用作诱饵文件。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEVPovyapJAeXx3xiaIVA14iclKCd6naRstCp0gTiaNcZFicianoI1kaLfR5w/640?wx_fmt=png)

相关攻击流程如下图

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcENzjzoayL1jHBVTHWs6Nxd5YeLvJ65A1Oo0wxozIkHkFoJ0FOHQ5MKg/640?wx_fmt=png)

**二**

**恶意文件执行**

1

LNK文件

LNK文件包含一段经混淆的CMD指令，指令执行后将复制%windir%\System32\ie4uinit.exe文件到%tmp%目录，在%tmp%\ieuinit.inf文件中写入相关配置信息，最后启动%tmp%\ie4uinit.exe。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEbBibJibibibS24C5bHZqnVP0IufVmliby8E6alFutZhaOicoXudkly0C2GXA/640?wx_fmt=png)

安恒云沙箱对LNK文件的进程信息分析如下，LNK文件运行后将启动ie4uinit.exe连接C2获取后续恶意负载。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEGoI89ibZNBanTXZyibHKXciaASEs0AHawdMlJwbQ9sWxXO8apj5BZyQrw/640?wx_fmt=png)

2

Javascript脚本

LNK文件执行后将加载后续Javascript指令。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEQczvkIOcW2nBQhZdK42MYcdiaewZ4bibfXF3G0QlvoS3X6W3ScE2V9Tw/640?wx_fmt=png)

远程Javascript指令运行后，将解密以下3个文件到本地：

1

白文件：%appdata%\Microsoft\msxsl.exe

2

PersPays：%appdata%\Microsoft\{随机字符}.txt (1758 bytes)

3

Pays：%appdata%\Microsoft\{随机字符}.txt (27098 bytes)

其中PersPays文件用于启动白文件msxsl.exe并加载Pays有效负载

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcE5ytlbTvoKfKqkecPw0Jnof0g52eAMG8VHxibZ16UcLCPic8Nd82JqBdw/640?wx_fmt=png)

除了释放文件外，远程Javascript指令还通过修改注册表键值实现恶意代码的持久化驻留。

      最后尝试通过WMI Win32\_Process创建cmd进程，启动白文件msxsl.exe并加载Pays有效负载，若创建失败，则使用WScript.Shell启动相应进程。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEtnB1BoQY5ermkJgONRoeU5Ea2SNQf47WXvgCia1ialWiclibiawo3AXACDQ/640?wx_fmt=png)

释放在本地的Pays文件解密下一阶段有效负载的过程与上一阶段类似，均使用basE91算法[1]。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEhNbUEkf4ib8hKO6JgJrG4VJXV1JeyficO5M1mMxK4ibLgfpw23rYTXYTQ/640?wx_fmt=png)

此外，代码还通过WMI监控进程死亡：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEhs5HVd3KVEJ03OLib35iar6oOGU0q3PJpYaS1qNT2jz9bbiamKmd4qelw/640?wx_fmt=png)

**三**

**持久化驻留**

Javascript脚本运行后将通过注册表HKCU\Environment\UserInitMprLogonScript设置环境变量cscript /b /e:jscript "%APPDATA%\Microsoft\VQKWTAG5IKIFRAUK.txt"，以实现恶意代码的持久化驻留。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEhNntaAnKzu8UXVYwYC9Z9VXDNeWkoZv1pdTv0VZKDln6hibNsdKickRw/640?wx_fmt=png)

**四**

**防御规避手段**

1

原始样本为伪装成PNG图片的LNK文件

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEvxic5ylrGiaUNObquTtAwljWsDC8enia2lgt3JqhHjIIBKH0Lu9qfCOVw/640?wx_fmt=png)

2

恶意文件中包含的cmd指令与Javascript指令等均经过混淆处理

3

cmd指令通过INF-SCT技术执行后续有效负载

INF文件是一个纯文本文件，其中包含在Windows操作系统中安装设备驱动程序和软件应用程序的说明。攻击者通过加载INF文件，可以执行位于远程服务器上的远程脚本组件文件(SCT)，并在目标计算机上执行任意代码。

      本次捕获的Evilnum组织样本通过运行ie4uinit.exe -basesettings成功加载了名为ieuinit.inf的INF文件[2]，从而远程执行了Javascript恶意代码。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEetGCFZLhJLfWZzhj6GewPd7dFic1tcLa3jfB3fTZ0ry31tKRQ5lt2tQ/640?wx_fmt=png)

4

利用msxls.exe绕过AppLocker应用程序控制策略

msxls.exe可以在不启动MicrosoftExcel的情况下解析和执行多种类型的脚本文件，例如：VBScript、JavaScript、PowerShell、Python脚本、Perl脚本等。由于msxls.exe是Microsoft Excel自带的工具，而且在默认情况下被包含在Windows操作系统中，所以攻击者利用了其白文件属性绕过AppLocker的应用程序控制策略。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcECJsUJnrK5k4Aozr7ziaTkSXeXeMicsbckvlkjGYdIZCvX8nzU7N6zJaA/640?wx_fmt=png)

**五**

**信息发现与上传**

Javascript脚本检查本机是否存在注册文件，若存在，则请求telemistry[.]net/get.php?id={文件内容} 以获取后续执行。

      若不存在注册文件，则获取主机计算机名、用户名、用户所在域以及本机反病毒软件信息，以"|"符连接，请求telemistry[.]net/reg.php?g={主机信息} 进行“注册”，并将返回内容写入注册文件。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEOyOic2vdayKLqdlZOck8VpFoIOl6KUfOTJj9EEXSDsg6FTqtnw9iat4Q/640?wx_fmt=png)

**六**

**样本关联分析**

猎影实验室观察到Evilnum组织域名资产上存在多个攻击样本，这些样本均用于同一攻击活动，活动疑似最早开始于2022年12月，持续至2023年3月。

|  |  |
| --- | --- |
| FileName | Hash |
| Axiance\_FullReport\_Volume.png.lnk | 76c84c02b044689e11c71fede9f0b61d |
| screenshots-9201.jpg.zip | cf66be681fa44f6a2ed8dc51cc73d0ad |
| Screenshot-9501.JPG.lnk | cf53baf5ec89b66224d208c64c39eeb3 |
| Screenshot-9502.JPG.lnk | f0dc2c2e01e0a7d1425cab539679927e |
| Screenshot-9501.JPG.lnk | ea896822cbc2f484be9d385c211322c1 |
| Screenshot-9502.JPG.lnk | 772f58a2bbf689c5b6c8daf9e0445b43 |
| Screenshot\_0459159441.lnk | 88101c9a59741278879d3a4d59e96540 |

我们对同批攻击样本进行分析后发现，部分样本后续会下发Cobalt Strike Beacon继续加载后续负载（ukmedia[.]store/static-directory/html.mp3）执行。截至分析时间，后续文件已失活。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEGD0Ywz81kSOB3yGZhG1npEyZE613Dyc7a36MnzGoqPiaBavaMKuY0Dw/640?wx_fmt=png)

**七**

**活动总结**

Evilnum组织在我们最新发现的活动中，使用了混淆cmd指令启动白文件的方式加载初始有效负载，该方式在VT平台上拥有较好的免杀率。同时，该组织还通过另一白文件msxsl.exe绕过AppLocker的应用程序控制策略后加载有效负载。

      为了防止msxls.exe被滥用，安恒猎影实验室建议管理员在系统上实施适当的安全控制措施，例如禁用msxls.exe工具或限制其执行权限，以确保系统的安全性。针对WMI被滥用的情况同理，应限制WMI服务的访问权限。其他防范方式还包括正确配置AppLocker规则，及时更新应用程序等。猎影实验室将持续对全球APT组织进行持续跟踪，专注发现并披露各类威胁事件。

目前安全数据部已具备相关威胁检测能力，对应产品已完成IoC情报的集成：

●安恒产品已集成能力：

针对该事件中的最新IoC情报，以下产品的版本可自动完成更新，若无法自动更新则请联系技术人员手动更新：

（1）AiLPHA分析平台V5.0.0及以上版本

（2）AiNTA设备V1.2.2及以上版本

（3）AXDR平台V2.0.3及以上版本

（4）APT设备V2.0.67及以上版本

（5）EDR产品V2.0.17及以上版本

● 安恒云沙盒已集成了该事件中的样本特征：

用户可通过云沙盒：

https://ti.dbappsecurity.com.cn/sandbox，对可疑文件进行免费分析，并下载分析报告。

**八**

**ATT&CK攻击矩阵 V12**

|  |  |  |  |
| --- | --- | --- | --- |
| Tactic | ID | Name | Description |
| 执行 | T1059.003 | Windows Command Shell | 通过cmd.exe执行命令 |
| T1059.007 | JavaScript | 初始阶段负载获取JavaScript后续脚本执行 |
| T1204 | 用户执行 | 受害者被引诱打开将安装恶意JS组件的LNK文件 |
| T1047 | Windows管理工具 | JS组件使用WMI获取杀软产品信息 |
| 持久化 | T1037.001 | 登录脚本 | JS组件将脚本路径添加到HKCU\Environment\UserInitMprLogonScript注册表项 |
| 防御闪避 | T1574 | 劫持执行流程 | 通过在ieuinit.inf文件写入相关配置使恶意代码被白文件ie4uinit.exe加载 |
| T1553.002 | 代码签名 | Evilnum使用合法（已签名）应用程序msxsl.exe作为防御规避机制 |
| T1036.007 | 双文件扩展名 | Evilnum使用.png.lnk或.jpg.lnk的双文件扩展名伪装文件真实类型 |
| T1112 | 修改注册表 | Evilnum为了在受损系统中持久存在使用注册表的运行键 |
| T1027 | 混淆文件或信息 | Evilnum恶意组件中使用大量了加密、编码和混淆 |
| T1027.009 | 嵌入式有效载荷 | Evilnum在JS脚本中嵌入了下一阶段有效负载 |
| T1220 | XSL脚本处理 | More\_eggs恶意软件使用msxsl.exe从XSL文件调用JS代码 |
| 发现 | T1518.001 | 安全软件发现 | JS组件会搜索已安装的防病毒软件 |
| T1082 | 系统信息发现 | Evilnum将有关系统的信息被发送到C&C服务器 |
| C&C | T1104 | 多级通道 | Evilnum其各种组件使用独立的C&C服务器 |
| T1105 | 远程文件复制 | 从C&C服务器上传/下载文件 |
| T1071 | 标准应用层协议 | HTTP和HTTPS用于C&C |

**参考链接**

[1] https://github.com/Equim-chan/base91/

[2] https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/

![](https://mmbiz.qpic.cn/mmbiz_gif/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEVXvFBYDGMszZ6e2Q91jrFoXlicV6NDVvibAoicsTaNbsXnVrJFPHtBv2A/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcE8HlTC3eBsUgChSU6yqPG6iaIsHJovib6bZk5HVK6A5quE2tGU2McQWSw/640?wx_fmt=png)

是安恒信息的智慧大脑，也是信息安全领域前沿技术研究部门。拥有数百位安全研究员和技术研发。目前设有十大实验室，研究领域涉及数十个方向，为公司产品、服务持续赋能，提供专业的技术能力支撑。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEONOW81Ky6zqwsbHEeJw4yfwb1EXaWwJqaoSdTOWJiaaH5EYwEiaQzvXg/640?wx_fmt=png)

**中央研究院 安全数据部，**下设猎影实验室、零壹实验室、析安实验室和回声实验室，团队以数据分析与技术研究为核心，致力于数据驱动安全创造用户价值。

**猎影实验室**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHw2vGEicZaqBTj33E52xcEv9wqibicVweQbUaibGcFib4xqEkibrqev8VJPJquibzbbcfH8LyyYvovaOvg/640?wx_fmt=png)

高级威胁研究团队，专注于APT攻击发现、分析、检测、溯源、防御等研究，以及积累了海量的IoC情报数据。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvndHw2vGEicZaqBTj33E52xcE99bfHYJT9eFicooO7YYN29cVZQQZjhw25xtG...