---
title: 新一代Webshell 管理与后渗透平台 | 去除通信流量强特征，支持自定义流量格式实现流量伪装
url: https://mp.weixin.qq.com/s/pOYf-uu8u0oP5kCBaeaoXQ
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:56.752654
---

# 新一代Webshell 管理与后渗透平台 | 去除通信流量强特征，支持自定义流量格式实现流量伪装

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0HzRK0YM77gJCQEGI8TO9B0lfcFiaIg1Z0sZ3xPGVCsGr9fxFX33eGtw/0?wx_fmt=jpeg)

# 新一代Webshell 管理与后渗透平台 | 去除通信流量强特征，支持自定义流量格式实现流量伪装

HeNrY4396

无影安全实验室

![]()

在小说阅读器中沉浸阅读

免责声明：本篇文章仅用于技术交流，请勿利用文章内的相关技术从事非法测试，由于传播、利用本公众号无影安全实验室所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号无影安全实验室及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！所有工具安全性自测！！！**VX：smile62157**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把"**无影安全实验室**"设为星标，这样更新文章也能第一时间推送！

![](https://mmbiz.qpic.cn/mmbiz_gif/3GHDOauYyUGbiaHXGx1ib5UxkKzSNtpMzY5tbbGdibG7icBSxlH783x1YTF0icAv8MWrmanB4u5qjyKfmYo1dDf7YbA/640?&wx_fmt=gif&tp=webp&wxfrom=5&wx_lazy=1)

安全工具

## 0x01 工具介绍

MatouWebshell 是一套基于 Vue 3 + Python 的 Webshell 管理与后渗透平台，面向授权的安全测试/红队演练。内置 Webshell 生成与连接能力，支持 Linux 目标下的 PHP、JSP、JSPX，并可自定义加密方式与请求/响应封装（form/json/xml/png 等），便于按业务流量形态进行伪装与兼容。提供命令终端、文件管理（大文件分块上传下载、编辑、压缩解压、权限/时间属性修改）、数据库管理等常用模块，并集成内网穿透（SOCKS 代理、端口映射、反向 DMZ/JSP）及 JSP 内存马加载/卸载与组件信息查询。

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv06iaqdKyriajMcZGHALjD8sicVoPdz3icTn1QFib2qrXuLuVcvaapL8ibfRxg/640?wx_fmt=png&from=appmsg)

## 0x02 工具功能

### 基础配置

生成webshell的基础配置参数如下：

* 参数名：在初始化阶段，客户端需将加密的payload以form格式发送至webshell服务端，post请求参数如：`{参数名}={encryptedPayload}`
* webshell类型：支持php、jsp和jspx
* CookieName：你可以理解成webshell的密钥，用于激活webshell功能的开关
* 标识符替换功能：替换指定前缀的变量标识符，支持“随机生成”和“变量池文件”（变量池文件为位于`router_modules/webshellmanager_router/webshell`目录，用户可自行修改变量池文件的标识符）

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0P3QWosk0zOxe7ibFswZDaxbXNnSysLyGFO9ge6ice0LfVNtLqPXV07jA/640?wx_fmt=png&from=appmsg)

高级选项

不同webshell类型对应的高级选项功能也不一样。

在php类型立，有个模拟正常业务功能，启用后可选择对应的业务模板（会将基础配置的payload嵌入到业务模板中）

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0yCInXFAib7ZuYXXicCnLJ4455RA1icm4UpWOLD3HCjvy9bWnbIRPCtO0A/640?wx_fmt=png&from=appmsg)

jsp和jspx类型都支持关键字混淆功能，jsp仅支持Unicode编码混淆，而jspx则支持Unicode编码、CDATA拆分、HTML实体编码、HTML+Unicode编码、CDATA+Unicode编码和CDATA+HTML编码

比如这里演示对关键字`getAttribute`进行CDATA+Unicode编码混淆，下方可选择Unicode编码的比率

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0J1WnpTmn9AKhvcQe8y2mfNGwu2vc9gRznsaiahcZHuMsBceIbf9TQjQ/640?wx_fmt=png&from=appmsg)

传输与加密

用户可以自定义数据通信的加密类型、请求格式和响应格式, 例如下面选择加密类型为aes\_base64，请求格式为form，响应格式为json（当选择该格式时会弹出“JSON响应模板”，“PAYLOAD\_DATA”则作为加密数据的占位符）

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0FWIQTjdXD9iczic1c7NXibvXcLoDzAvVicBMcZ75mnzKsPFK29vyo9g2Nw/640?wx_fmt=png&from=appmsg)

支持用户自定义请求内容，目前支持form、plain，json/xml以及png格式，可通过配置json内容来修改请求格式

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0LsjAFniaUhC89sticCwjdQcECticgDNsxtKnLay7picic93Tu4gwk6IdTNA/640?wx_fmt=png&from=appmsg)

如下演示请求格式为xml，响应格式为json

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0dndyJf4C7lQUftiaRgqNiaWPcibqDgDTDzwNcXLl0YWlChWz1By3R3pww/640?wx_fmt=png&from=appmsg)

如下演示请求格式为form，响应格式为png

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0ocB6ZduPZFUibNiaUS6ibJJX2mrtZuI3ic7Nn1ic1euicbFEwRG36eqoXgmA/640?wx_fmt=png&from=appmsg)

命令行终端

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0134N36JWibJxn5CH2fyKT5dZleu1Ciammq9yicpMD89c29B1iaZ1n9Xe6g/640?wx_fmt=png&from=appmsg)

### 文件管理

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0pCZlcCXM0x4SPCWErHhaGERxT3Oibqq5a5hhCia0H4CtP5ic4fV3ibyetw/640?wx_fmt=png&from=appmsg)

数据库管理

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv01UNic7NxmlykmdVRNNTyMCrIjoyHSuNot870kdBcg832AaagkqWBaGg/640?wx_fmt=png&from=appmsg)

### 内网穿透

内网穿透功能允许你通过已控制的 Webshell 服务器访问其内网资源，支持三种模式

* **SOCKS代理**：在本地开启一个SOCKS代理端口，然后将浏览器或扫描器等任何支持SOCKS协议的工具指向该端口，就可以自由访问webshell内网中任意的IP和端口。支持内网白名单ip功能，启用后仅与白名单IP建立隧道
* **端口映射**：将内网端口映射到本地，例如将内网的3306端口映射至本地，再使用本地工具进行连接
* **反向 DMZ（只支持jsp）**：反向代理内网服务，适用于反弹shell

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0JpAJOUhoPdvmrvne8jS7RyPpcLN8xVV7Q604TKogJ8TD5k4lMRP4HA/640?wx_fmt=png&from=appmsg)

### 内存马注入(jsp)

目前支持以下内存马类型：

* **Servlet 内存马**：注册为 Servlet 组件
* **Filter 内存马**：注册为 Filter 组件

![](https://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFERzLq6pHqzBPVzrY60OUYv0G7UrXK3LGGFcE1viarGDtqeC12LHdibuk9U1QsIXJvKSO952FJjemINw/640?wx_fmt=png&from=appmsg)

## 0x03 工具下载

**点****击关注****下方名片****进入公众号**

**回复关键字【260108****】获取****下载链接**

最后推荐一下内部小密圈，干货满满，物超所值，**内部圈子每增加100人，价格将上涨20元，越早进越优惠！！！**

**![图片](https://mmbiz.qpic.cn/mmbiz_jpg/awCdqJkJFET8apEknf7bc6ZR8CyWIBqmV3L88k03ibsUgLfyzvyvuOjkZUfWm9YsK0phQ3owbjBgbhibnWBicgsXw/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&randomid=ebo9tcn3&tp=webp)**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

无影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/awCdqJkJFESkGMPLLYOibsOdiaYUbUGH2ibd832G0h4stN7iacicE62hCJGle1IuVQbgGDx5v5GXjwUuE23xJNJjgTg/0?wx_fmt=png)

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