---
title: 【恶意文件】Magniber勒索软件借助微软的漏洞实施攻击
url: https://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247518031&idx=1&sn=a9c4f1bdf8ed2470f7edbed8332cf551&chksm=ce460c5ff93185499a43aead7d9648228455f99496161249743e76c9a233de2d2267c781c9ca&scene=58&subscene=0#rd
source: 深信服千里目安全技术中心
date: 2023-03-31
fetch_date: 2025-10-04T11:18:16.665890
---

# 【恶意文件】Magniber勒索软件借助微软的漏洞实施攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1PjO9Z7cIoFtNIvhiahlVIRkBiaZMfia3UsOeE4otUagI5wicTWciavzhKuQ/0?wx_fmt=jpeg)

# 【恶意文件】Magniber勒索软件借助微软的漏洞实施攻击

深盾研究实验室

深信服千里目安全技术中心

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1kuw175o6KBYESQtM1yvkPORRiaXelrAJBPhDticQGTsqcz303jcHEwaw/640?wx_fmt=gif)

**恶意家族名称：**

Magniber

**威胁类型：**

勒索软件

**简单描述：**

Magniber勒索家族的前身是Cerber，至少从2021年10月已经开始活跃，最初主要针对韩国，从今年年初开始，该组织日益活跃，攻击范围开始遍布全球，包括中国大陆、中国台湾、中国香港、马来西亚、新加坡和欧洲等。

**恶意文件分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1sibqLX2ibgZqR5sNbKEgVqCjVJzDHQ42vUerGzG4Szd6Qm3jve42uiaBw/640?wx_fmt=gif)

**恶意事件描述**

深信服深盾终端实验室在近期的运营工作中，捕获了的Magniber勒索家族的最新变种，此次捕获的样本通过MSI进行传播，同时使用微软的漏洞CVE-2023-24880（注：3月14日官方已发布补丁）来绕过 SmartScreen从受感染的网站下载和安装Magniber勒索软件，CVE-2023-24880漏洞由CVE-2022-44698漏洞未完全修复引起的。

CVE-2023-24880 利用了Windows SmartScreen 安全功能的绕过。SmartScreen是Windows版本 10 和 11中的一项安全功能，主要用于检测和阻止网络钓鱼和恶意软件的下载和安装。绕过该功能即代表允许攻击者在没有任何安全警告的情况下下载Magniber勒索软件。

该漏洞已在今年3月15日进行及时响应，相关链接如下所示：

https://mp.weixin.qq.com/s/f4uA3Loc2ooG\_1\_tcvxnUA

![](https://mmbiz.qpic.cn/mmbiz_gif/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1sibqLX2ibgZqR5sNbKEgVqCjVJzDHQ42vUerGzG4Szd6Qm3jve42uiaBw/640?wx_fmt=gif)

**恶意事件分析**

在所有的勒索家族中，Magniber绝对是最独树一帜的存在，样本本身使用了大量的混淆、解码，通过采用新的混淆技术和规避方法不断更新其策略，极度干扰研究人员的分析工作。其次使用漏洞，Magniber Ransomware 近年来一直通过 IE (Internet Explorer) 漏洞传播，但自 IE 停止支持后，Magniber Ransomware 在 Microsoft Edge 和 Google Chrome 浏览器中以 Windows 安装包文件 (.msi) 的形式分发。

样本启动后，会加密系统中的部分文件，并释放勒索信以诱使受害者通过勒索信中的联系方式与攻击者进行沟通及缴纳赎金，其中被加密文件添加扩展“mhkgchqs”，勒索信文件名为“README.html”，勒索信中并未表明赎金金额及支付方式。

**README.html勒索信文件内容如下所示：**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE14QMGpiaHx9loJ8iaUiagDpxcvzQVrRGHAKcrz50jDibAwQhR055rRvTmJQ/640?wx_fmt=png)

**被加密后文件系统情况：**

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1T3llTTGGYQa7B73YMnAIrJguB3SptJiaxHiaXdkVvkeo02mZJ75O7ahw/640?wx_fmt=png)

**MSI文件分析**

攻击者正在使用无效但自制的验证码签名的 MSI 文件。格式错误的签名会导致 SmartScreen 返回错误，当不受信任的文件包含 Web 标记 （MotW） 时，该错误会导致不会向用户显示安全警告对话框，实则已经从 Internet 下载了潜在的恶意文件。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE117yhiavY0WTfl4DFaYZnXttF5Pe4D54rCBYkgTWBlFBJHW9ZbShMnUQ/640?wx_fmt=png)

使用Orca打开MSI文件查看表的结构和内容。发现MSI会调用CustomAction属性执行MSI内嵌DLL的导出函数j6tow27o。

SetProgramFilesFolder：将该程序的文件夹设置为LocalAppData目录，即“C:\Users\用户名\AppData\Local”。

Ucjvnpaclba：获取二进制文件ilzwngaiyktz，type为65表示该文件为dll类型，Target表示导出函数为j6tow27o。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1dcQxmPKbNbr2mhb1W3Fp627oy5If5uXTIL1gse4MwSXlYibmzZmo3Zw/640?wx_fmt=png)

**DLL文件分析**

Ilzwngaiyktz文件为勒索功能模块，下面对该文件进行详细分析：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1O7ptWm7sUaLibC4dl12ZELmU1PhvFFhsXc5TUrOicYMnpibKHia8L3AZ9Q/640?wx_fmt=png)

**Windows系统版本判断**

查看Windows系统版本，只针对Windows10、Windows11、Windows Server 2022系统进行加密

该代码通过XOR解码过程遍历循环语句 (do-while)，并将勒索软件shllcode注入当前正在运行的白进程中。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1TUYyc0HdJ6QOfM6KPEYvsPkh3xibxC4zTAxIe2oE8sDxumxtI9Kktfg/640?wx_fmt=png)

该病毒会释放DLL格式的文件，该文件导入表、执行主体在DLL主函数中，释放shellcode到内存并执行，无文件加载能够降低自身被内存代码检测引擎发现的风险，同时Magniber并不直接通过调用API实现相应功能，而是模拟相应API在ntdll中的行为，传入参数，然后指定syscall ID，直接调用syscall，同样可以实现直接调用系统API的作用。

**反调试**

Magniber 使用 NtDelayExecution 以随机间隔休眠以逃避分析。随机休眠间隔可能会阻止沙盒或防病毒检测成功。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1albP8Cs0n4dRSS2o7egBVCABxfl1g6NOaJNQ2D1jq40xnlnFPB0TgA/640?wx_fmt=png)

**持久化**

在HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 注册表中添加一个键值，其中ouPBdEoNXxUS.3fr文件为密钥文件

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1ibmG9oR1NNqAmEXIsHDm3ntB6UicvFVLkTFyjyDQPuLYCUocFW4gCSZg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1ZXicyLSO9iaiblbUqibibf4AdTlk0cdwj6bHpIlNKSuF8iaaDx7FpznPzlNw/640?wx_fmt=png)

**绕过UAC**

在注册表中写入下载Magniber勒索软件的命令

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1IOxguKSnVhwZe9SDM48l9WqBxe1OO6jvVKibjpV2WjKlLqia1s2rlRmQ/640?wx_fmt=png)

上述写入注册表的内容能够实现，当系统重新启动时，注册到 Run 键的 .3fr 文件扩展名与指定同时激活的注册表一起执行，导致每次系统重新启动时都会下载Magniber勒索软件并实施加密活动。

**高级远程线程注入**

blackbox.dll可用于绕过软件安全措施,一般用于注入恶意代码或执行其他非法操作。fwcwsp.dll 文件是 Windows 操作系统中的一个 DLL 文件，它是 Windows Firewall 的一部分，用于提供网络连接的安全性。

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1LXiamT4AueRBxJVFdnb0ico58wicHcCOnn3jicRqCYFNXtz6LiaOVNxbFvg/640?wx_fmt=png)

**1、遍历进程**

解密代码后，首先会枚举受感染系统上所有正在运行的进程以识别勒索软件可以在其中注入shellcode的进程,Magniber将解压后的shellcode注入满足以下条件的进程

进程名是否大于6字节

该进程未在WoW64环境中运行。WoW64 是 Windows 操作系统的一个子系统，可以在 64 位 Windows 操作系统上执行 32 位应用程序

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE153b2OPOibicTPXaNPdnoibIPyXIa0UDhqqcbW3EkA1kaqQPMOvUY3d0rg/640?wx_fmt=png)

**2、远程注入**

注入过程如下所示：

NtOpenProcess：打开目标进程

NtAllocateVirtualMemory：在目标进程中为即将写入的shellcode分配内存空间

NtWriteVirtualMemory：将shellcode写入分配的内存区域。

NtProtectVirtualMemory：修改内存保护属性

NtCreateThreadEx：创建远程线程，执行shellcode

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1LSNcjpiawDx9sjjjcAaWMmIiahmGh9E00DLX7m5wqicibkgL2NsgzconCQ/640?wx_fmt=png)

随后将带有勒索加密功能的shellcode注入到符合条件的进程中（如：sihost.exe）RWX属性的内存中。但由于它使用系统调用，因而无法直接通过调试器监控内存写入来跟踪注入的shellcode。相反可以直接通过运行msi程序，然后使用procexp等进程监视器挂起进程然后dump写入的shellcode。

通过查看该shellcode的字符串发现被混淆后的勒索信内容

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1tDqFO4APbklanhvqkOG8B9gCdfQ7sBesDZrK7amIxpMXSPr7EEibcIA/640?wx_fmt=png)

解除混淆后，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1TWMFVibKLUnueBYGuAA3icvAyWdhWc3bzXbejPHbic8LG6wBFMHYtS6Dw/640?wx_fmt=png)

使用shellcode加载器加载注入的shellcode，然后使用x64dbg继续调试，发现在“C:\Users\Public”目录下释放RDTBADQ.xarh文件。

**删除卷影**

执行VBS脚本，删除卷影副本，禁用Windows系统恢复功能。

Wscript.exe /B /E:VBScript.Encode ../../Users/Public/RDTBADQ.xarh

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1WjQNW3xt67BxaTQpC72z5xvMJXFXLINGTD3iaMnhC1JvBby4ICOEhAw/640?wx_fmt=png)

在执行RDTBADQ.xarh文件时，文件被编码了，编码后文件内容如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE115RP1HMxiaBOmaxLW9PAKeopxktQibFOxUlITnquE1lU3zqS9PIKDYtA/640?wx_fmt=png)

对VBS进行解码，解除一层混淆后

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1NoPibTYicQuMdMz2hibhTCVfLz6bSrVicByYSvnicaRZ6JrwlHicwyUa7mHg/640?wx_fmt=png)

解除二层混淆后

![](https://mmbiz.qpic.cn/mmbiz_png/w8NHw6tcQ5w1DEJPGanlE1YaM3oK7NE1gV185GIzjOxmx0jQ5ZnFN5tiaeqvUfic7TPrK7CKerBkicKvliaJaquEfw/640?wx_fmt=png)

**加密**

避免加密的目录和文件

documents and settings/appdata/local settings/sample music/sample pictures/sample videos/tor browser/recycle/windows/boot/intel/msocache/perflogs/program files/programdata/recovery/system volume information/winnt/README.html

**加密的文件后缀**

.abm/.abs/.abw/.accdb/.act/.adn/.adp/.aes/.aft/.afx/.agif/.agp/.ahd/.ai/.aic/.aim/.albm/.alf/.adn/.adp/.aes/.aft/.afx/.agif/.agp/.ahd/.ai/.aic/.aim/.albm/.alf/.ans/.apd/.apm/.apng/.aps/.agif/.agp/.ahd/.ai/.aic/.aim/.albm/.alf/.ans/.apd/.apm/.apng/.aps/.apt/.apx/.arc/.art/.arw/.aim/.albm/.alf/.ans/.apd/.apm/.apng/.aps/.apt/.apx/.arc/.art/.arw/.asc/.ase/.asf/.ask/.asm/.apm/.apng/.aps/.apt/.apx/.arc/.art/.arw/.asc/.ase/.asf/.ask/.asm/.asp/.asw/.asy/.aty/.avi/.arc/.art/.arw/.asc/.ase/.asf/.ask/.asm/.asp/.asw/.asy/.aty/.avi/.awdb/.awp/.awt/.aww/.azz/.asf/.ask/.asm/.asp/.asw/.asy/.aty/.avi/.awdb/.awp/.awt/.aww/.azz/.bad/.bak/.bay/.bbs/.bdb/.asy/.aty/.avi/.awdb/.awp/.awt/.aww/.azz/.bad/.bak/.bay/.bbs/.bdb/.bdp/.bdr/.bean/.bib/.bmp/.awt/.aww/.azz/.bad/.bak/.bay/.bbs/.bdb/.bdp/.bdr/.bean/.bib/.bmp/.bmx/.bna/.bnd/.boc/.bok/.bay/.bbs/.bdb/.bdp/.bdr/.bean/.bib/.bmp/.bmx/.bna/.bnd/.boc/.bok/.brd/.brk/.brn/.brt/.bss/.bean/.bib/.bmp/.bmx/.bna/.bnd/.boc/.bok/.brd/.brk/.brn/.brt/.bss/.btd/.bti/.btr/.c/.ca/.bnd/.boc/.bok/.brd/.brk/.brn/.brt/.bss/.btd/.bti/.btr/.c/.ca/.cals/.can/.cd/.cdb/.cdc/.brn/.brt/.bss/.btd/.bti/.btr/.c/.ca/.cals/.can/.cd/.cdb/.cdc/.cdg/.cdmm/.cdmt/.cdmz/.cdr/.btr/.c/.ca/.cals/.can/.cd/.cdb/.cdc/.cdg/.cdmm/.cdmt/.cdmz/.cdr/.cdt/.cf/.cfu/.cgm/.cimg/.cd/.cdb/.cdc/.cdg/.cdmm/.cdmt/.cdmz/...