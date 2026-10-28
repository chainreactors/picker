---
title: 高危预警｜海莲花组织发起多行业定向攻击！科研、航运、交通均被盯上
url: https://mp.weixin.qq.com/s/pqTaUKLH_PN5WwJwnUB47w
source: Doonsec's feed
date: 2026-10-27
fetch_date: 2026-10-28T07:46:28.331249
---

# 高危预警｜海莲花组织发起多行业定向攻击！科研、航运、交通均被盯上

# 高危预警｜海莲花组织发起多行业定向攻击！科研、航运、交通均被盯上

威胁情报团队
威胁情报团队

电信云堤

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/Dh3fqSPAOWekCSIf3ffuFuiaBPl4BSArBsDhFEMSOTbeIfb7mdz4D0mDExZesv4PPicUdsOTxfRUx8QntAMTmTBA/640?wx_fmt=gif&#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/Dh3fqSPAOWePMu18J3qdm7D4DgerZrtmzfZ2ThoQZZl4WAHJScyL4c59NPZcjXgnP2YL4HnUicxRibjtBZmqJW8A/640?wx_fmt=png&#imgIndex=1)

近期，天翼安全科技有限公司威胁情报中心监测到一起瞄准科研教育行业的定向网络攻击。通过对攻击载荷、代码结构多维度研判，确认攻击者为海莲花组织。本次攻击利用镜像文件作为载体，运用 “白加黑” DLL 侧加载手段，叠加多重反调试、EDR 规避技术，隐蔽落地恶意程序、建立持久化驻留，最终投放其专属 Shellcode 木马。

情报拓线分析显示：除科研教育领域外，该组织同步将魔爪伸向海事航运、交通运输等多个重点行业，多领域目标均在攻击范围内，相关单位务必提高警惕，做好防护排查！

***组织介绍***

海莲花组织，又称APT32、OceanLotus，是一支具有东南亚国家背景、长期活跃的境外网络攻击组织，自2012年起持续针对东亚、东南亚地区开展攻击活动，主要目标包括政府部门、科研机构、海事航运、交通基建及工业制造等领域。该组织擅长利用鱼叉式钓鱼、水坑攻击、漏洞利用及恶意软件植入等手段实施渗透，通过定制化后门窃取敏感信息。

***攻击流程***

海莲花组织本次攻击流程如下图所示。攻击者通过投递携带恶意文件的镜像，诱导用户执行LNK快捷方式，进而释放诱饵文档，并利用DLL侧加载技术加载恶意DLL。该DLL随后读取MANIFEST-000001文件，经内存解密后执行HiveSwarming.exe，以规避EDR检测并实现持久化驻留；同时读取BrowserMetrics-spare.pma文件，经内存解密后加载shellcode木马，与C2服务器进行通信。

![01.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MiaAVo4Q3P7ibMKkib3ib76Fm071A5aTF4DWoUUGrD5KibyB0QETg0IiagMp4XRczzk6mriaDIbqmKLBFIv5cgpN75yic7haVgwHEDlPYo/640?wx_fmt=jpeg&from=appmsg)

***样本分析***

**样本基本信息**

本次捕获的海莲花组织攻击样本采用镜像文件形式进行投递，样本基本信息如下表所示。

![02.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5Mh10eylV7G8Iwoe7mr4mjEcP16op56dlp16aO2o9B3GTrzbQLRhWiaRFLoF8KZn58icU0XtasV0y7JIKgPWuCoQapaWkcKy04Xco/640?wx_fmt=jpeg&from=appmsg)

镜像文件解压后的内容如下图所示。该镜像文件包含多个文件，其中《通讯录.pdf.lnk》为攻击入口，用户点击后将触发执行“ ·”目录下的 xlejiwyntedmqy.vbs 脚本文件。

![03.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MgS1pHWibS14eLyicxfnTpiaX1YRmwsU6sEC3C1ibOxrPibeEateEDMgA6lhmwcXjJvLUTHB82jp3kkJ6hsdSN8Th8H4KzOutFmrxjQ/640?wx_fmt=jpeg&from=appmsg)

**vbs脚本分析**

该vbs脚本采用简单的字符串混淆。运行后，首先打开诱饵文档以迷惑用户，随后创建%USERPROFILE%\AppData\Local\gt4t.net目录，并将后续执行所需的程序及相关组件复制至该目录。最后脚本以隐藏窗口的方式启动nw\_gt4t.exe，通过白加黑的方式加载恶意DLL文件nw\_elf.dll。

![04.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5MiaBGCOgcJgcFFswgm0hTZPPnEicwrU9SDekewzQ73Buu1CKGw9TUmZztib87iblHibgV0C8OWROLdz1xC4sRnpbrxlnqmdAkvDyUXw/640?wx_fmt=jpeg&from=appmsg)

**反调试分析**

恶意DLL加载运行后，会通过多种检测手段识别调试环境，以规避安全分析。样本通过检查PEB结构中的调试相关标志、检测进程调试端口及内核调试环境，并检查当前线程的硬件调试寄存器，以识别硬件断点。此外，样本还结合时间差校验，辅助识别潜在的调试行为。一旦检测到异常，样本便会提前返回并中断后续执行流程。

![05.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MgNrNWlicNyPU0bTngsO4yLhsZohNdyp8C9rKG2yU1H4FPJhiaQaiaLGB1h4nxfOSsWXiaXibJyJMgTIdBFUH0E1k6RavZicMGfWXrCw/640?wx_fmt=jpeg&from=appmsg)

**持久化驻留**

在持久化方面，恶意样本通过遍历系统服务，检查目标主机是否存在360杀毒软件相关服务，并根据检测结果采取不同的持久化策略。

![06.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5Mg01OH5qT7z0KicnsGNOTofz99PPqEGC0vUaZ9QqH46UOfZSFbJOxKbGcEJqDG22OdPuHosfxJeEH6LXa4oHXBnMWQMBfsibmXZo/640?wx_fmt=jpeg&from=appmsg)

当未检测到相关杀毒软件服务时，恶意样本通过调用系统API操作注册表，在SOFTWARE\Microsoft\Windows\CurrentVersion\Run路径下创建名为GT4T的启动项，并写入程序启动路径，实现开机自启动。

![07.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5Mh4tX82Mybkqkp3MFCicibzibOEOB95xMIJJK7xb96ibicCOJtmUSvicNQknTIGEAoQt4ZmNfjlCHsW732R039cJrHkOVWcMp1f4FXz8/640?wx_fmt=jpeg&from=appmsg)当检测到相关杀毒软件服务后，恶意样本会采用基于NTUSER.MAN文件的持久化方式。该文件属于强制用户配置文件，用户登录系统时会优先读取并加载该文件中的注册表内容，从而绕过基于函数调用的EDR检测。

首先，样本执行reg export hkcu C:\Users\admin\AppData\Local\Temp\reg /y命令，导出当前用户的注册表数据，并在导出内容中添加启动项。随后，样本读取同目录下的MANIFEST-000001文件，通过RC4解密获取并执行shellcode，在内存中释放开源工具HiveSwarming.exe，并通过 --from reg --to hive参数将修改后的注册表数据转换为二进制注册表配置单元文件NTUSER.MAN。

![08.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5Mia3OlgCpmr544shVyuJFTicJ7xPqdEp4KxozNj7ibRolbxX1lR4GUNVHR1rG5fbkX0nnoUoC68gm5lYfLS6zLCsHgu4halrcjRrA/640?wx_fmt=jpeg&from=appmsg)

**shellcode木马分析**

完成自启动配置后，恶意样本读取同目录下的BrowserMetrics-spare.pma文件，对文件的内容进行Base64解码和RC4解密，还原出原始shellcode，随后分配内存并执行，实现后续恶意代码的加载与运行。

![09.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MhQTAuAvDmUdN3pgAEYv1SgNCr0NzUblgUJgAv6oJnzYuAQHGZOoIxPI94Wtgclf2xQtAsqxwjQiak6iaUuVoYfRTZRLjYh5oEW0/640?wx_fmt=jpeg&from=appmsg)

shellcode执行后，会在内存中解密并加载以shellcode形式存在的海莲花组织木马。该木马启动后，首先初始化默认配置，包括C2地址、User-Agent等HTTP通信参数。其中，样本配置了两个C2地址，分别为manawatuplumbing.co[.]nz和gowellth[.]com。

![10.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MiaiaSXLwWH9IMCs8o12bDu5ib4Ziajjjic0uppXYKSuribL7cKNpleEG0RiaevBCv89EPKTY2geKflCxbYicCFnqbqfnmeoJRe5T8uxoQ/640?wx_fmt=jpeg&from=appmsg)

随后，恶意样本收集目标主机的计算机名称、当前用户名、操作系统类型、网卡MAC地址、当前进程名称及PID等信息，并以[key]=[value]的形式拼接成如下字段。

c=DESKTOP-JTLCRI2;u=admin;o=Windows;p=1;a=1;b=2;e=1;v=3;g=11679;s=00:0C:29:98:66:59|admin;pn= nw\_gt4t.exe (x64);pi=1408;hi=1

恶意样本随机生成16字节的RC4密钥，对上述主机信息进行加密后发送至C2服务器。如下图所示，通信数据的前16个字节为RC4密钥，其余部分为加密后的主机信息。

![11.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5Mia6BsJdYbFJlMJBjYPzLoj5rJ2Lc4C4gXcpNAVWdqicUXaF5ATvticRbzTgBibDnPTOu9umZRshhZ3iaYajbMg30AYAe47wpv2zb3U/640?wx_fmt=jpeg&from=appmsg)

最后，恶意样本等待 C2 服务器下发攻击指令，并根据接收到的指令调用相应功能模块，执行指定的恶意操作。样本内置了多种功能，具体功能及其作用如下表所示。

![12.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MiarG1jhJ1nVNHMMl6CiaQvkAaD0TxzHCs0LiaANmudfS2qibo5buqMLkibY3ysObjWFichGGicDFofhReD8zAuxCAgpYzicdib3Nicx263A/640?wx_fmt=jpeg&from=appmsg)

***归因分析***

本次捕获的海莲花组织恶意样本与国内安全厂商于今年7月披露的相关攻击样本在攻击手法及代码特征等方面表现出高度相似性，均采用“白加黑”技术，通过合法程序加载恶意组件实施攻击。此外，两个样本在运行过程中的反调试检测逻辑也基本一致，进一步体现出二者在技术实现上的相似性。具体对比如下图所示，左侧为7月份披露样本的反调试检测方法，右侧为本次捕获样本的对应实现。

![13.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5MgtGqGwAwicnto3cFYehtXZf7CHicFaD3CKiatp5EwtnUibvbkDMbzDjwhicztbgZq73394gkPDPJntMt2micYUxkfibh8TMElELnu2vk/640?wx_fmt=jpeg&from=appmsg)

在持久化及规避EDR检测方面，本次捕获的样本与7月份披露的样本也采用了相同的技术手法。二者均利用开源工具HiveSwarming，将导出的注册表数据转换为二进制注册表配置单元文件NTUSER.MAN。

![14.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5Mho6fic43AYLaOhiaUaJpuq6o5TQEWuVm9DniaEmrbKQJnqgsakibGOrGo9XOz1tE0hWYmuRosbYkbqY5lvXyKpUcCbibftoDofpOLk/640?wx_fmt=jpeg&from=appmsg)

***关联拓线***

依据上述恶意样本的文件特征、代码逻辑、载荷加载方式、持久化行为及C2通信特征，对样本开展进一步拓线分析，筛选并比对具有相似技术特征的恶意样本，具体拓线结果如下图所示。从拓线分析结果来看，9月3日至10月13日期间，共发现海莲花组织相关可疑样本12个，投递载体以ISO镜像文件为主，同时涉及ZIP、RAR等压缩文件格式。相关样本通过结合不同业务场景设计诱饵内容，主题涵盖学术研究稿件、电子发票报销凭证、船舶工程技术手册等，攻击目标涉及科研教育、海事航运、交通运输等多个领域。

![15.jpg](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MgCiatKTvC0G3lHBRfrUZ7gDHGiatWdp4OziaicFRrR2T4dewWuvzQaQYevp0BDsbJ3OXV6amMcsAP151a25N7YY6anGtTlXWYEnBU/640?wx_fmt=jpeg&from=appmsg)

***总结***

本次攻击中，海莲花组织通过镜像文件投递、“白加黑”DLL侧加载、多重反调试及针对性持久化等手段，实现恶意载荷的隐蔽执行与驻留。经过进一步拓线发现，相较于今年7月披露的样本，近期部分关联样本除沿用vbs脚本外，还采用hta文件作为执行载体，并在脚本层面加强混淆处理，体现出该组织在既有攻击技术基础上持续调整载荷执行方式与规避检测手段的特点。

中国电信威胁情报中心（ti.ctct.cn）、天翼安全大脑、网站安全专家、云镜CWPP、云堤安全托管服务（MSSP）等已支持对本次海莲花组织攻击事件相关IOC的检测。建议相关企业及用户加强安全风险排查，结合自身安全防护需求，通过中国电信威胁情报平台对可疑IOC进行核查，并加强高危外联行为监测，及时发现潜在威胁，降低网络攻击风险。

![16.jpg](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5MgMLYmeddqR3g90AVUSy4NxWvFiaTgBWQWoVQDsO7Pkz4dTW1opXcCQnhUfHSPvQXOg1iazpZPfmzNgiabZ6KTIKCPOGliaVo0zHoU/640?wx_fmt=jpeg&from=appmsg)

***IOC***

**C2**

tone21.mydns[.]jp

gowellth[.]com

meat-bic-order[.]jp

madarussalamsubah[.]id

manawatuplumbing.co[.]nz

seo.kao-gong.com[.]tw

lensee-automation[.]com

erp.manitech[.]ch

agoras.zapto[.]org

teknois.unbin.ac[.]id

kmaster.com[.]my

**MD5**

951ed7287926666ec48d89cf6f15df32

e41260178bb89e3467d87151ef9bea6c

88f570094907c2250aeda4b85b38e47a

7c4a5b4669acf0c51bf5f8f5247bdb45

e755da13bd07e0ae062fc014de22b1ba

698ac1e66c5e9e305ff38388608860dd

f882aa6704178c005fb7db98ae928282

637e958fbcb5643f842826cf1f6ac38f

80745198aab88ae534ac3276a5e20d78

0579f8613881dd2a6621cb27009e514d

822fae5748c309062aec10a0589b0ec4

5091b44eef46e800748eaa7daaf5a85c

68124f029a5fafc3733fbc7c43db1e07

供稿：威胁情报团队

排版：马子豪

编辑：陈师慧

校对：李雪

执行主编：田金英

主编：冯晓冬

**推荐阅读**

[![](https://mmecoa.qpic.cn/sz_mmecoa_jpg/RiaMmbYzV5MiapeFM4pKpeaDQn5ZGbjWYJicJZWb5TdHTpgApWWcpy9901Klof0GJMbTicRDTb9WlPxA9Q7ZicPwRiaqR2rVLIw3J3IHxXlnSqQvc/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490709&idx=1&sn=6630261b88213c89c59a293193651caa&scene=21#wechat_redirect)

**[Weaxor家族勒索新套路：又有0day漏洞现世了！](https://mp.weixin.qq.com/s?__biz=Mzk2NDIzNTYwOA==&mid=2247490709&idx=1&sn=6630261b88213c89c59a293193651caa&scene=21#wechat_redirect)**

[![](https://mmecoa.qpic.cn/mmecoa_jpg/RiaMmbYzV5Mg8WLAweVSLtG2PqFGgp6xONzHr2KSq64cP87WSicBLFGLHg1FgjzDXOShqkUFMYiaaNbAd...