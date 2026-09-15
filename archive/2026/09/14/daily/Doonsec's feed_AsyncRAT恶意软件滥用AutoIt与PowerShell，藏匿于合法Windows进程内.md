---
title: AsyncRAT恶意软件滥用AutoIt与PowerShell，藏匿于合法Windows进程内
url: https://mp.weixin.qq.com/s/oTQW42yJ558vYr9KlfixmQ
source: Doonsec's feed
date: 2026-09-14
fetch_date: 2026-09-15T06:58:04.058991
---

# AsyncRAT恶意软件滥用AutoIt与PowerShell，藏匿于合法Windows进程内

# AsyncRAT恶意软件滥用AutoIt与PowerShell，藏匿于合法Windows进程内

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

感染始于名为 “右键打开发票详情.bat” 的钓鱼诱饵文件，需要用户手动触发执行。
目前尚未确定确切传播途径，这类文件一般通过钓鱼邮件附件、恶意下载链接、被植入木马的软件以及聊天平台诱饵进行分发。

一旦被打开，该批处理文件将启动PowerShell，运行窗口被隐藏，同时禁用用户配置文件加载。
恶意代码从10段Base64片段重建编码载荷，剔除人为插入的无效垃圾字符，再通过循环密钥异或（XOR）算法，解码出下一阶段的攻击数据。

该手法可以绕过静态特征检测：完整Base64内容、有明确含义的文件名以及最终载荷，不会以完整字符串形式暴露，避免被扫描工具直接识别。

PowerShell执行阶段会在 %LOCALAPPDATA%\Temp 目录下创建经过混淆的文件夹，并释放3个文件：经过重命名、带有合法数字签名的AutoIt解释器、AutoIt加载脚本 kojuyn.ini ，以及一个无后缀的加密二进制文件 nloemfbihmhm 。

同时它会在当前用户的启动文件夹生成批处理脚本 h73la8.bat 。用户每次登录系统时，该脚本就会调用重命名后的AutoIt程序，并传入 kojuyn.ini 作为参数。攻击者无需修改注册表Run启动项、无需创建计划任务，也不需要管理员权限，即可实现恶意程序持久驻留。

该行为对应MITRE ATT&CK攻击矩阵技术项：T1547.001 启动或登录自动执行：注册表Run键/启动文件夹。

该持久化手段的特点是：攻击者复用带合法签名的解释器，而非直接投放自定义恶意可执行程序。
PointWild威胁情报研究人员表示：这起攻击活动体现出，普通远控木马攻击者正在结合轻量脚本与内存执行技术，用来对抗基于文件的杀毒检测机制。

AsyncRAT如何藏匿在Windows进程内

AutoIt二进制程序充当了看起来可信的执行载体，恶意逻辑全部写在配套脚本中。
文件夹列表中蓝色圆形图标是AutoIt程序图标，不是普通应用图标。根据版本不同，AutoIt.exe大小约900KB‑1MB。

恶意软件在不同样本之间会变换文件名和XOR密钥。但是它的行为链特征是固定的：隐藏窗口的PowerShell、向用户可写的Temp临时目录写入文件、利用启动文件夹持久化、调用AutoIt执行。这些行为给防御方提供了稳定的检测点，不受文件名变化影响。

加载脚本 kojuyn.ini 通过经过XOR编码的整数数组，动态解析Windows系统API函数名称： OpenProcess 、 VirtualAllocEx 、 WriteProcessMemory 、 CreateRemoteThread 。
脚本读取无后缀的加密载荷，使用单字节XOR密钥 0x36 在内存中完成解密；随后后台静默启动系统程序 %WINDIR%\SysWOW64\charmap.exe （字符映射表），窗口完全隐藏不可见。

加载器使用经典远程线程注入流程，把解密后的恶意代码注入目标进程：
 OpenProcess（打开进程）→ VirtualAllocEx（申请远程内存）→ WriteProcessMemory（写入内存）→ CreateRemoteThread（创建远程线程）

PE‑Sieve工具分析确认： charmap.exe 进程内存中被植入PE可执行镜像，磁盘上并无对应的恶意文件，证实载荷完全运行在内存中。
扫描同时发现CLR公共语言运行库、AMSI反恶意软件扫描模块遭到内存修改，说明.NET运行环境被加载，并且AMSI防护功能可能在进程内部被篡改绕过。

借助微软签名的 charmap.exe 作为宿主进程，恶意软件所有网络通信、系统探测、数据窃取行为对外都表现为由 charmap.exe 发起，而不是来自Temp目录下可疑程序。

后续解密阶段生成混淆的DLL文件 Veukuzmw.dll ，这就是AsyncRAT主体载荷，具备屏幕截图、窃取信息能力。
该远控木马通过.NET图形接口捕获主显示器画面，截图数据在内存中编码，通过命令控制通道回传给攻击者服务器。

研究人员捕获的C2（命令控制服务器）IOC： 158[.]51[.]122[.]136:4944 ，通信使用原始TCP协议，不走普通Web流量。

AsyncRAT本身是开源远程访问工具，被大量恶意攻击滥用；常见能力包含远程命令执行、监控、窃取各类数据。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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