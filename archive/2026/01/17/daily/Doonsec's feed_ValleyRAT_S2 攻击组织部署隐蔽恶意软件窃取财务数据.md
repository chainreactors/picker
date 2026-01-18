---
title: ValleyRAT_S2 攻击组织部署隐蔽恶意软件窃取财务数据
url: https://mp.weixin.qq.com/s/6LkZcf8lUoXOeNWY5OlZ8Q
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:34:57.527934
---

# ValleyRAT_S2 攻击组织部署隐蔽恶意软件窃取财务数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atfricsIJAGsUYHK6hFoLnHx4O7YKY9GWXthib3Zn3BeHZ8XSHLT1Pa6OA/0?wx_fmt=jpeg)

# ValleyRAT\_S2 攻击组织部署隐蔽恶意软件窃取财务数据

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9attuSHibsxH6iafPZlNTqhJ6O82fIQcic1LWeXCZU1m1bCYjJj9jotHJZ1A/640?wx_fmt=png&from=appmsg)

新一轮网络攻击正利用 ValleyRAT\_S2 恶意软件悄无声息地侵入组织机构，长期潜伏并窃取敏感财务信息。作为 ValleyRAT 家族的第二阶段有效载荷，这款采用 C++ 编写的恶意程序具备完整远程访问木马功能，使攻击者能强力控制受感染系统并建立稳定数据外传通道。

**Part01**

## ****攻击传播途径****

当前攻击活动主要通过以下方式传播：

* 伪装成中文版生产力工具的虚假软件
* 经过篡改的破解软件
* 冒充基于 AI 的电子表格生成器的木马化安装程序

技术分析显示，恶意软件常通过 DLL 侧加载技术投递——诱骗合法签名程序加载名为常规库文件（如 steam\_api64.dll）的恶意 DLL。网络安全团队 APOPHiS 追踪确认，ValleyRAT\_S2 是驱动这些入侵活动的核心第二阶段后门。此外，攻击还通过鱼叉式钓鱼附件和遭滥用的软件更新渠道进行传播。

恶意文档和压缩包通常将载荷释放至 Temp 目录，例如：

```
C:\Users\Admin\AppData\Local\Temp\AI自动化办公表格制作生成工具安装包\steam_api64.dll
```

第一阶段载荷专注于规避检测，而 ValleyRAT\_S2 则负责长期系统控制、环境侦察、凭证窃取及财务数据收集。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atVE1dDCjj9G7ddSrqOKMoy7iaRXApZ4KlMg3uelDfMH4w6ibANWtjRbNA/640?wx_fmt=jpeg&from=appmsg)

**Part02**

## ****恶意功能分析****

激活后，ValleyRAT\_S2 会执行以下操作：

1. 扫描运行进程、文件系统和注册表键值
2. 通过自定义 TCP 协议连接硬编码 C2 服务器（如 27.124.3.175:14852）
3. 实现文件上传下载、Shell命令执行、载荷注入和键盘记录功能

这些能力使其特别适合窃取：

* 网上银行凭证
* 支付数据
* 内部财务文档

**Part03**

## ****持久化与看门狗机制****

ValleyRAT\_S2 最危险的特征在于其分层持久化设计和看门狗机制，可抵御系统重启和手动清理。恶意软件首先在用户 Temp 和 AppData 路径暂存文件，并创建以下标记：

```
%TEMP%\target.pid%APPDATA%\Promotions\Temp.aps
```

其持久化技术包括：

* 通过 COM API 滥用 Windows 任务计划程序实现开机自启
* 使用注册表运行键作为备用启动路径
* 生成监控脚本 monitor.bat 构成看门狗循环

![看似合法的进程（来源 - Medium）](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icGlTT0kUBTLu3ic7yrfq9atJrQYjOhXcDwploJ3jgiaFfB19BWbjWwNIib9iaPia11mSa1AZxNp2mk9RA/640?wx_fmt=jpeg&from=appmsg)

监控脚本逻辑如下：

```
@echo offset "PIDFile=%TEMP%\target.pid"set /p pid=<"%PIDFile%"del "%PIDFile%":checktasklist /fi "PID eq %pid%" | findstr >nulif errorlevel 1 (  cscript //nologo "%TEMP%\watch.vbs"  exit)timeout /t 15 >nulgoto check
```

该机制使 ValleyRAT\_S2 能在主进程被安全工具终止后自动恢复。结合以下技术，恶意软件可保持隐蔽而顽固的驻留：

* 结构化异常处理
* 沙箱检测
* 注入可信进程（如 Telegra.exe 和 WhatsApp.exe）

防御建议：单纯终止进程无法彻底清除，必须同时处理：

* 计划任务
* 批处理/VBS 监控脚本
* 暂存文件
* 后门进程

**参考来源：**

ValleyRAT\_S2 Attacking Organizations to Deploy Stealthy Malware and Extract Financial Details

https://cybersecuritynews.com/valleyrat\_s2-attacking-organizations/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3icIRaltrZVKxHyDE18c4IRVw3NnALmIwxqOb5mKhbDhBIRRU7MLD2zkbPgnNPvhyk5ibAhhLAavEIA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

内容含AI生成图片

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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