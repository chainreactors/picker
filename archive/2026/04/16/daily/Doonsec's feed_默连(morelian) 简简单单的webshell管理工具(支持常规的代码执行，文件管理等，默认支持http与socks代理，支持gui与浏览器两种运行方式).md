---
title: 默连(morelian) 简简单单的webshell管理工具(支持常规的代码执行，文件管理等，默认支持http与socks代理，支持gui与浏览器两种运行方式)
url: https://mp.weixin.qq.com/s/5Qpaw3DFKMO-FYlZctds6g
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:42:44.287377
---

# 默连(morelian) 简简单单的webshell管理工具(支持常规的代码执行，文件管理等，默认支持http与socks代理，支持gui与浏览器两种运行方式)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XfO0XCNPrNqUyz3cDI08DApsG9ZcQL3IYAsVp1pNbL71pBuIHicwS0k87tjg2AnumegiaWPbx6ZJbjlDy7eMvz5icsx4t5FO4o7yM9NG3oedfg/0?wx_fmt=jpeg)

# 默连(morelian) 简简单单的webshell管理工具(支持常规的代码执行，文件管理等，默认支持http与socks代理，支持gui与浏览器两种运行方式)

原创

沐寒
沐寒

渗透云记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azJZJ4pVQHOicqtkQntqLduTfPaVvVnZ4iaGc0DaBeQqNoicYUrzzyOpIsJWbSgNUqV3SodRwKFOIq3Lw/640?wx_fmt=png&from=appmsg)

欢迎关注本公众号，长期推送技术文章

## 前言

好久没有更新公众号了，最近又搓出来一个小工具，**默连**，寓意很简单，就是悄咪咪，静默连接。

**工具支持GUI运行，同时也支持后端运行，通过浏览器进行访问控制**

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNoibFDJGI4q80pR0hGV9JiboLZU2e3P21MA6icYeq5AHOsLdQXRcESl5XsfsOx3TxVzkaNYQDCl2Qbt2V3OAnTGYeARruE6Hdq8og/640?wx_fmt=png&from=appmsg)

## 功能概览

### 目标与连接

* **分组与列表**

  ：按路径式分组管理目标，支持分页、搜索与右键快捷操作。
* **存活检测**

  ：单目标「测试连接」与导航栏「批量测试存活」（可后台进行）。
* **多协议握手**

  ：按目标配置的 Payload、加密器与 URL 建立会话；会话内可切换 **UTF-8 / GBK** 等编码。
* **代理**

  ：支持为单目标配置 HTTP / SOCKS 等代理类型（以界面与配置为准）。

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpuMILuQ5CKtcbvjUcJCWowiaWhzL1YHmKib4VXuicWiahQqGByoG03YJKK0XprY4iaA0bkw7LLEL3msWWhZQLicLOHQJo7iakEOfBtz8/640?wx_fmt=png&from=appmsg)

### 载荷与生成

* **GenerateShell / 生成**

  ：按密码、密钥、载荷类型、加密器生成服务端脚本；可配置 **Header Gate**（指定 Header 名与值）、**浏览器伪装**（模板与变种）、以及与 Tomcat 版本相关的 **javax / jakarta** 等选项。
* **连接脚本导出**

  ：从目标列表生成/导出连接所需脚本（与导航「生成连接脚本」等入口配合）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpuv88WrODqq57Fy6HLiaSeMaKhic59VyMbK7MR5ylicWYylNfahXDxEjD6ib0XYJol45VjDy0TPEas2Uv4wkGeia1mVIvvTHJCiaYIM/640?wx_fmt=png&from=appmsg)

### 会话能力（标签页）

* **命令与终端**

  ：统一执行命令、交互式终端等（合并原「执行 / 虚拟终端」等能力）。
* **文件管理**

  ：远程文件浏览与操作。
* **基础信息**

  ：会话与目标基础信息展示。
* **笔记**

  ：会话侧笔记。
* **数据库**

  ：数据库相关操作面板。
* **网络**

  ：如 `netstat` 等网络信息查看。
* **标签管理**

  ：自定义标签顺序与显示，支持「复制标签配置」等。

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpARzF1Tf7ibQrgh5ISwCxR6M7IHBYyN6DPSMQ8icfX0UFekBG1ljp1VtE184O5eJicJhgWI2n141Uvd4EsXmtUQsAVmfj93SG2LQ/640?wx_fmt=png&from=appmsg)

### 插件（按载荷与配置动态出现）

会话中可按插件类型懒加载，例如（不限于）：

* **压缩 / 端口扫描 / 代理合并 / 进程列表 / 枚举数据库连接**
* **屏幕、Servlet 管理、Jar 加载、FilterShell、PHP 工具、内存马**
* **PHP WebShell 扫描**

  等

具体是否显示某插件取决于当前 **Payload 类型** 与内置实现策略

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNr6Kz5bJSwrNSjtHzc3pkjZLcTAarzribXGdO6sGgnvWJGTqRFSbhV0Its1tbLw6s0ibplTK1FlYcHFQnkokOlwoNBI3JCrE2yhM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNowohiaQASDE305cCIEn4sp196emHEbajmtkubXqpl6EzSljxwRqHiaa8EHucoyYdM1icr3icO89n3vGibEP32XBtwjdiahNhrkhbjCI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNq1yuadgD8gEmBibnlNQYhnV92EnqicQ72beQBcnFJApVdcoP2GbNpeA6v7c7MwshGb4scmjEQUguXHTLjib4N2O7nN8iaXOPpic9icI/640?wx_fmt=png&from=appmsg)

### 运行模式

* **桌面模式**

  ：默认启动 Wails 窗口，数据存放在用户配置目录下的本地 **SQLite**。
* **Web 模式**

  ：使用命令行 `-web` 在本地启动 HTTP 服务，用浏览器访问界面（适合仅需浏览器、或与其它工具联动）。监听地址可省略（默认 `127.0.0.1:34116`），也可传入端口或完整 URL。

## 如何运行

### GUI运行

直接双击就行

### Web 模式（浏览器）

在已构建的可执行文件或开发构建上，使用例如：

```
1# 默认监听 127.0.0.1:34116

2./morelian -web

3

4# 指定端口

5./morelian -web8801

6

7# 或使用 -web= 形式

8./morelian -web=:8801
```

Windows 下将 `./morelian` 换成 `morelian.exe` 即可。

## 测试效果

### D盾效果：

php 所有版本无感，但是其余版本还是会警告，下一版本优化

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNoibOWnb0aLnlMlzxvoSSnDycVrochQn47dleibPiaImqAhIFWrXc9HXQr9oW2cEicnMmFiarYro1PuSibYK49pHG2dwxjibicBVqXROPE/640?wx_fmt=png&from=appmsg)

### 阿里云效果:

借助ai，目前感觉还是很哇塞的

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqQ0fT651lWeFAjSGrPKiabV3Zu6Q9yhV6RtUEIHCOloggoltNwdse44BXV4malHbap0DJtnIlfJxibxkAgm3Y5zHJeibgvdZd7vA/640?wx_fmt=png&from=appmsg)

## 实战环境演示

光看不练假把式，现在这么多的webshell管理工具了，为什么我还得写一个“默连”呢，其实还是一个执念，想要一个自己的~~~

环境说明

```
宝塔最新版，已开启全部waf等防护，php站点安全防护等
测试站点：https://b.encenc.com
```

为了保证能上传php脚本，这里临时先关闭了php站点安全防护，要不然宝塔默认不让上传php文件（这个暂时没想到好的思路，有师傅研究过的话可以探讨探讨）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpYljjzWrz80aqcyrnTeO8J7Cibq5NmHtaKzaqofDurib99Jb2Hibc3ibXNZYPvtQvtiaPpqIo8q3z7uzMy7iaSjGibnUHnGgcgMYiaAUE/640?wx_fmt=png&from=appmsg)

这里手动创建了一个任意文件上传的测试页面，用来模拟文件上传

```
https://b.encenc.com/morelian/badfileuploadtest2026.php
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNpWFUxNiaEUziazvsoOzpFkERJX1W2KX1AfUhU9z22M5qf0aGIWygicicDaJdWZTkgeKeia2M6nYFxIGkthwSZkibqaIprHwyqMOyo7s/640?wx_fmt=png&from=appmsg)

使用morelian简单生成一个php的小脚本，并且启用指定header连接与默认nginx404页面模拟

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNpXXthyTNVEgLf69icEysmN6uiak1YGJD5cRQUpM4avEBuo6WicpY0D3GDKIgG0yuYRXEEuotOFh3JtvGeFIhA639EVyzceXEbvRE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNrc5UHxgP1SxZbqa9JS3cCQ0JfURXI2pf2fKoPDscXryKEIHczzNRSRgzG11rZGicVZalmpfNhU34MMd4BYQxguMlCFibavdBlrc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNq62q6umJ3OgSk1KUcCXwib0BWLd7cAgcPxungYibY3PBUNoTOIicLT00fTazg7WT6udRj6ib8icl2zQsibZxicI8po4SXZ7awiaCH1VwQ/640?wx_fmt=png&from=appmsg)

此时咱们的脚本地址

```
https://b.encenc.com/morelian/a4890e6e71_phpdynamicpayload_php_xor_base64_messages.php
```

直接访问就是咱们伪装的nginx404界面

这里已经上传完文件了，此时咱们就恢复刚刚关闭的php安全站点防护

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNrQibg72FUevXJth1JSXcCn1NibicX4je0libiaUyibcZb4Ist2I2c88gnQZCNpQu7SlZzkibib1t8degxp2nyLAiczH0whuS7LxiaQgF3kY/640?wx_fmt=png&from=appmsg)

使用morelian进行连接，刚刚配置了header，这里也需要输入，否则连接失败

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNovPHr9gfJk1DsABgD1f5Kd3y7VyRl5ojwQOzC7oGPUotRGeiatecWNePFZZPvd1jyUU2qSia4fdyeXzLbpK4M8Xj47EdxwZhicmM/640?wx_fmt=png&from=appmsg)

连接之后，查看文件信息

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqO0bKJ5MwGR7uWICC41rY6wxtUme0hIC1ks95tYFrwIr61yuV1kBAgqjZzhvfE68EFKp7s1BLiaRpKEgrQoK1benYmjkw30wWw/640?wx_fmt=png&from=appmsg)

连接数据库

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNoj7nrRaGzBtgYesibIsPIK1aJ3UhpHJFlI8jMibdaUTlRm98icPic4ibQtF9ogzxtriaHN3yEiaZrhfz16uwStSuhGjjRnJSqBDmfHvw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/XfO0XCNPrNr2QwP83K5gqQ9cWEngKxlcEg1QkMHc1qAA5jdqaVrNLbmpjia4j4qM9Xh5ibHpqC96AqKv3dvj6MjgoLV0rKI1pkoiaJdzHdZRQ8/640?wx_fmt=png&from=appmsg)

开启http代理

![](https://mmbiz.qpic.cn/mmbiz_png/XfO0XCNPrNqBqW4zaia1eQZSTuAGbkQYqrFAQUkQNt8NyDcTLxhcickLlLR0D7uY3lWjFbD9HN8iaWTcfrd3ficsRHpUPnHk3FVZlYmACg4ibb54/640?wx_fmt=png&from=appmsg)

**当然因为面板默认禁用了诸多函数，这里执行命令是不行的，需要后续继续研究！！！**

### 获取

### 默连已放在"叮叮当当"圈子与渗透云记博客中，进圈子之后务必请联系鄙人，以保障您的权益享受完整！！！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLbE8HiaQapVkBwypwXhsmWWEwZyOx2Frhw9bDjyRnVSMtubJkZJY9NX2Hw8Igx7fDmuZnYXzPUvDA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK0JBUq0N1g9hpXvZiaWm32V2kibRficfdehadlNxb8ibickibcgHFOr9FXF5qibRy3pDw984iaZP8InvejUQ/640?wx_fmt=png&from=appmsg)

往期精彩：

[EasyTools渗透测试工具箱V2.2.2更新(1.新增云上安全，支持oss存储桶扫描、云存储管理与云服务管理;2. 修复数据库连接bug )](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484786&idx=1&sn=f5e7954a9de25cf2439d2a88de364383&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.1.8更新(1.优化端口扫描规则，提高扫描效率; 2.重新设计ssh、ftp界面; 3.优化各数据库数据展示)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484772&idx=1&sn=80f2b065da342f7f0d7b5553d5cf45a7&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.1.6更新(1. 渗透测试模块新增druid利用功能; 2. 修复密码爆破模块部分协议无法直接执行命令的bug)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484763&idx=1&sn=c2a0dbdee6dcde28d2aa1c5d04009b55&scene=21#wechat_redirect)

[今日时事，一个快捷全面的信息流获取平台，告别信息焦虑，让你一眼看尽天下事](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484750&idx=1&sn=87d33a3442b6fc12fe10f48443efacda&scene=21#wechat_redirect)

[EasyTools渗透测试工具箱V2.1.4更新(优化资源桶遍历功能，支持kkfileview预览，新增空间测绘、AI版域名收集功能等诸多功能)](https://mp.weixin.qq.com/s?__biz=MzkxNDYxMTc0Mg==&mid=2247484743&idx=1&sn=6a427ce97be0e6c2ee8e803edb82ee14&scene=21#wechat_redirect)

---

鄙人的一个小博客 渗透云记，

官网地址：www.encenc.com

博客地址：b.encenc.com

目前已集成EasyTools渗透测试工具箱的登录，Webshell\_Agent AI自动生成平台的登录等，一个账号，多平台联动使用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azK5R6NYcibf6ADO4U7BvUHupNyYDu3RwMYRL9ickjZNUMoHeGcAS7fgF2zcyWaODWcOuqjqkeAibjkPQ/640?w...