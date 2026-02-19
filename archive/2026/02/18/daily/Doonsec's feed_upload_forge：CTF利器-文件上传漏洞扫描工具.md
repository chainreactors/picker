---
title: upload_forge：CTF利器-文件上传漏洞扫描工具
url: https://mp.weixin.qq.com/s/wGYkJawYCfh1JKsKxNL8Cg
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:13:03.821860
---

# upload_forge：CTF利器-文件上传漏洞扫描工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicJxZJHGKSzPCu6uEFIq0srg0EHMgnpKnIHUVQydhicQdJWhI6b2yic267ZSWl3TkV2PeOicibEdt26kA3ic20WGwrd57ftiaWNLHna6g/0?wx_fmt=jpeg)

# upload\_forge：CTF利器-文件上传漏洞扫描工具

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Havoc：现代化后渗透命令与控制(C2)工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486375&idx=1&sn=98207489b2de236c7eb471e09875c659&scene=21#wechat_redirect)

·[URLFinder：一款高效网页内部隐藏链接挖掘工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486361&idx=1&sn=763c9b7b0a992c4094efbb6263beeb10&scene=21#wechat_redirect)

·[PCHunter：一款深度检测隐藏恶意代码的扫描工具（兼容win11）](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486351&idx=1&sn=5ad805f6aa58a79e2f21b777849db642&scene=21#wechat_redirect)

·[Web-SurvivalScan：用于快速验证资产存活的轻量化渗透测试扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486350&idx=1&sn=1a4559b375cda713d02d270ae121bc70&scene=21#wechat_redirect)

·[【已复现】最新版微信v4.1出现远程命令执行漏洞：one-click RCE on Linux WeChat](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486318&idx=1&sn=a39e4ceaadd2fcffea08ecdc48319fc9&scene=21#wechat_redirect)

·[xss\_scanner\_mix：一款自动化深度XSS漏洞扫描工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486302&idx=1&sn=08544ff7835ce01fae582f677ad02a98&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**介绍**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicLJybUOicQUZCf7AHzvhtBicqw0ibP6oe95MOlsvIBqw9xdDHCMuVodrrw4VNHiba4l2VwwoHJmrpr79CuglMq5bz9gUTAUa0jNCfo/640?wx_fmt=png&from=appmsg)

    Upload Forge 是一款强大的生产级安全工具，旨在检测和利用网页应用中的文件上传漏洞。它专为渗透测试人员和安全研究人员设计，能够自动化测试文件上传表单的过程，针对各种绕过技术进行测试。

    主要功能：

1.异步扫描：高性能扫描引擎，由 和 驱动。httpxasyncio

2.高级检测逻辑：

    （1）分机旁通：双重扩展（.php.jpg）、大小写敏感性（.pHp）、稀有扩展（.phtml、.php5）。

    （2）魔法字节伪造：生成带有假头部（如PNG、GIF89a）的载荷以绕过内容检测。

    （3）空字节注入：检测较旧的后端漏洞（shell.php%00.jpg）。

    （4）多语种：创建包含可执行代码的有效图像文件。

3.现代图形界面：采用PySide6构建的美丽暗色调图形界面，便于配置和实时监控。

4.Rich CLI：功能丰富的命令行界面，包含进度条、表格和详细日志。

5.报告：生成专业的HTML和JSON报告。

6.验证：通过尝试访问和执行上传文件，自动验证漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**安装**

访问下述网址，即为Upload Forge工具的源文件地址：

```
https://github.com/errorfiathck/upload_forge
```

    在目标文件夹中打开终端后，在网址中复制克隆地址：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicIvia9Avsgy2ibMy2XUMiaZyleia21mfU83MAZolNTC2RBAU7FQPSgDnI6ib9wqJ3WV4tiaeRphklaCu0ELyHZl2BzlLgicWqp69B2gt4/640?wx_fmt=png&from=appmsg)

    在终端中输入：

```
git clone https://github.com/errorfiathck/upload_forge.gitcd upload-forge
```

    即可克隆项目并进入到项目文件夹中。

    检测克隆完成：

```
dir
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicIpuxXqWvwcCDJl9WIpdH8zS3CPRicBSmKJXGerQAZpOmoibtXmefJ4WAQcPh1iciccxP3DR6hFG9sTNpjNyU41RyJyvYyMcbxQzOw/640?wx_fmt=png&from=appmsg)

    然后安装依赖：

```
pip install -r requirements.txt
```

    可开始使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**功能介绍**

一、启动图形界面（GUI）

    启动现代仪表盘：

```
python upload-forge.py gui
```

![](https://mmbiz.qpic.cn/mmbiz_png/x2ibBTFXYHicKkwP7KO3ryfF3AQ4eJOAbrqGj6SyM9xyQcGXx4u8nYsFpsJiayVm90AI6mZibShe2BaIAiaHBZx7kA1Wdg55icb46f8cVcia357ibDQ/640?wx_fmt=png&from=appmsg)

    从图中的请求历史我们可以看到，工具正在对 http://127.0.0.1:5000/upload 进行自动化测试，通过上传不同扩展名的文件并尝试访问，判断是否存在漏洞。

    可以看到，TrafficViewer 标签页显示工具具备完整的HTTP流量分析能力：

1.请求详情查看：可查看每个测试请求的Headers和Body

2.响应分析：显示服务器返回的状态码、响应头

3.对比分析：方便对比成功与失败的请求差异

    也可以通过点击看到特定的测试文件内容。

二、命令行接口（CLI）

    直接从终端运行扫描：

```
python upload-forge.py scan --url http://target.com/upload --param file --upload-dir http://target.com/uploads/
```

    选项：

```
--url： 目标上传网址（必填）。--param： 文件输入参数的名称（默认：）。file--upload-dir： 上传文件存储的网址（用于验证）。--proxies：代理字符串（例如，）。http://127.0.0.1:8080
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJib9aSZDYT2VdvQdban61iaFK6wibGXJLuzA3IqJW15ibaHia6r4A6Uib1nK7SQQWMP7xgFYzpdiczOVqEGmNCDZcwepUJ9BoTgLpRcg/640?wx_fmt=png&from=appmsg)

    可以看到，工具正在对目标进行自动化渗透测试：

第一阶段：基础WebShell测试

Standard PHP Shell - 标准PHP一句话木马

Standard JSP Shell - JSP环境测试

Standard ASPX Shell - ASP.NET环境测试

    结论：服务器同时解析JSP和ASPX文件，可能存在配置错误

第二阶段：PHP扩展名变体测试

.php - 标准PHP扩展

.PHP - 大写绕过

.php5 - PHP5备选扩展

.phtml - PHP嵌入HTML扩展

.php7 - PHP7备选扩展

    结论：服务器允许多种PHP变体扩展名上传并解析

第三阶段：双扩展名绕过测试

.php.jpg - PHP伪装成JPG

.jpg.php - JPG后跟PHP

.php.png - PHP伪装成PNG

.png.php - PNG后跟PHP

.php.gif - PHP伪装成GIF

    结论：服务器仅检查最后一个扩展名，可轻松绕过

    通过这次扫描，upload\_forge 成功发现了目标服务器的多个高危文件上传漏洞。

1.快速检测单个目标

```
python upload_forge.py -u http://example.com/upload -f test.php
```

```
--u：指定上传接口URL--f：指定要上传的测试文件
```

2.使用Payload字典批量测试

```
python upload_forge.py -u http://example.com/upload --payloads payloads.txt
```

3.带Cookie认证的测试

```
python upload_forge.py -u http://example.com/upload --cookie "PHPSESSID=xxx"
```

    可以展示输出报告：

```
python upload_forge.py -u [URL] -o report.html
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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