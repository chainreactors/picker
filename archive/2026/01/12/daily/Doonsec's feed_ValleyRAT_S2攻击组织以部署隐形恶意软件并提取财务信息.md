---
title: ValleyRAT_S2攻击组织以部署隐形恶意软件并提取财务信息
url: https://mp.weixin.qq.com/s/KXHpC7mJzNQ3_N77FZt15g
source: Doonsec's feed
date: 2026-01-12
fetch_date: 2026-01-13T03:28:33.670920
---

# ValleyRAT_S2攻击组织以部署隐形恶意软件并提取财务信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dzJiaU8Wt1qymwc9dIK1ZGnBfOia0iaeFZicfmMxTHhXJYHaia6qcjZJ5X7Sq5ZxF5KCvYaFqjxmdpnSexicAVu5G0MQ/0?wx_fmt=jpeg)

# ValleyRAT\_S2攻击组织以部署隐形恶意软件并提取财务信息

原创

O安全研究员

O安全研究员

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qymwc9dIK1ZGnBfOia0iaeFZic7NVAfrIyyxp5QMoS4d4BbzEThnT05N9VFK2YJN3jg6HeDezunbqpVg/640?wx_fmt=png&from=appmsg)

新一波攻击利用ValleyRAT\_S2恶意软件悄然入侵组织，长时间隐藏并窃取敏感的财务信息。

ValleyRAT\_S2是ValleyRAT家族的第二级有效载荷，采用C++编写。一旦进入网络，它就像一个完整的远程访问木马，为攻击者提供了对被感染系统强有力的控制，并提供了可靠的数据传输方式。

当前的运动主要通过假冒的中文生产力工具、破解软件以及伪装成基于AI的电子表格生成器的木马安装程序传播。

在许多情况下，恶意软件通过DLL侧载传递，即通过诱骗一个合法签名的应用程序加载一个名为普通库（如steam\_api64.dll）的恶意DLL。

APOPHiS追踪这些行动后，确定ValleyRAT\_S2是驱动这些入侵的核心二级后门。

该恶意软件还通过鱼叉式网络钓鱼附件和滥用的软件更新渠道传播。

恶意文档和归档会将负载投放到像临时文件夹这样的位置，例如：

C：\Users\Admin\AppData\Local\Temp\AI自动化办公表格制作生成工具安装包\steam\_api64.dll。

从第一阶段开始，重点是规避，而ValleyRAT\_S2则负责长期控制、系统发现、凭证盗窃和财务数据收集。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qymwc9dIK1ZGnBfOia0iaeFZicB5Q3MiawS4aBBeicqrf0leX1H2rTedLRaicMjPhVY4FCJ3iaFaluibghzAA/640?wx_fmt=png&from=appmsg)

激活后，ValleyRAT\_S2扫描进程、文件系统和注册表键，然后通过自定义TCP协议向硬编码的命令控制服务器（如27.124.3.175：14852）发送信号。它可以上传和下载文件，运行shell命令，注入负载，并捕获按键记录。

这使得它非常适合收集网上银行凭证、支付数据和内部财务文件。

## **持续性与监督行为**

ValleyRAT\_S2最危险的部分之一是其分层的持久性和看门狗设计，这帮助它在重启和手动清理中存活下来。

恶意软件首先在用户的 Temp 和 AppData 路径中设置文件，创建诸如 %TEMP%\target.pid 等标记，并在 %APPDATA%\Promotions\Temp.aps 下设置配置路径。

它还通过 COM API 滥用 Windows 任务调度器，在启动时重运行自己，并可能使用注册表运行密钥作为备份启动路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dzJiaU8Wt1qymwc9dIK1ZGnBfOia0iaeFZicibtKEPFzYiamibxNumezXUF3S33HsWB051nqJD6LicMiaiakNeQ6UKfficSbA/640?wx_fmt=png&from=appmsg)

一个关键功能是生成的批处理脚本monitor.bat，它作为看门狗循环。

脚本读取target.pid存储的进程ID，检查主恶意软件进程是否仍在运行，必要时静默重启。

简化版如下：

```
@echo offset "PIDFile=%TEMP%\target.pid"set /p pid=<"%PIDFile%"del "%PIDFile%":checktasklist /fi "PID eq %pid%" | findstr >nulif errorlevel 1 (  cscript //nologo "%TEMP%\watch.vbs"  exit)timeout /t 15 >nulgoto check
```

这个循环允许ValleyRAT\_S2在安全工具或管理员终止主进程时恢复。结合结构化异常处理、沙盒检查以及向Telegra.exe和WhatsApp.exe等可信名称注入进程，恶意软件保持了安静但强大的存在感。

对于辩护者来说，这意味着简单的进程终止还不够;完全移除必须同时针对调度任务、批处理和VBS看门狗脚本、分级文件以及后门进程。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

O安全研究员

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/dzJiaU8Wt1qwqJgvgiaEEbM4iaLlwQUhMic3TfI1ibRVlBcl7tiblcrRxgzBrF0UMhRtHtSuVfKdgVibQjjB7OoUYIU5w/0?wx_fmt=png)

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