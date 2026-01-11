---
title: 用友漏洞综合利用工具
url: https://mp.weixin.qq.com/s/o7MKM0mkuwf8-A_HmRbAQw
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:30.658232
---

# 用友漏洞综合利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLxWxB8KTNiaEFPGQ7FpeRqL6ibFCjAqicjEbaB4kuJnPMSIXD2hc2Pd2RA/0?wx_fmt=jpeg)

# 用友漏洞综合利用工具

W小哥

![]()

在小说阅读器中沉浸阅读

以下文章来源于木吉他的鱼
，作者Chave0v0

![](http://wx.qlogo.cn/mmhead/5K48YNcpF3ZoNZTMDlMCIOQ4rMBtWJKswx5ZvwIYVH7M2XO8DVEIZGk1wNyAvIFdNPA3dib3yJzc/0)

**木吉他的鱼**
.

专注渗透测试、漏洞挖掘、CTF竞赛解析等实战内容，深度还原攻防场景，分享一线安全工程师的实战经验。定期发布工具教程、案例复盘及攻防思维训练，助力安全从业者提升技术深度，打造攻防兼备的网络安全能力。

# YONYOU-TOOL

用友漏洞一键探测利用。

学习用友漏洞期间一时兴起，写一款工具记录学习。

工具开发期间，感谢 **SpringKill** 师傅指点。

## 免责声明

本工具仅适用于安全研究学习，严禁使用本工具发起网络黑客攻击，造成法律后果，请使用者自负。

## 支持漏洞

```
ActionHandlerServlet 反序列化
```

```
Lfw_Core_Rpc 文件上传
```

```
BshServlet RCE
```

```
jsinvoke 文件上传
```

```
accept.jsp 文件上传
```

```
DeleteServlet 反序列化
```

```
MxServlet 反序列化
```

```
DownloadServlet 反序列化
```

```
FileReceiveServlet 文件上传
```

```
Fs_Update_DownloadServlet 反序列化
```

```
MonitorServlet 反序列化
```

```
UploadServlet 反序列化
```

```
NCMessageServlet 反序列化
```

```
XbrlPersistenceServlet 反序列化
```

```
ECFileManageServlet 反序列化
```

```
ModelHandleServlet 反序列化
```

```
ResourceManagerServlet 文件上传
```

```
GroupTemplet 文件上传
```

```
LfwFileUploadServlet 文件上传
```

```
IMsgCenterWebService JNDI注入
```

```
uploadChunk 文件上传
```

```
billitem 文件上传
```

## 使用说明

java -jar 启动。

```
java -jar YONYOU-TOOL-[version].jar
```

目前实现功能模块：漏洞探测、一键 getshell、命令执行、文件上传。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLcKtuSAVZGEWrXmFrgptYLgWvVjn2GUF9ic919lsiau4fwG2ptPCIsfOA/640?wx_fmt=png)

### 漏洞探测

以 **ActionHandlerServlet 反序列化** 漏洞为例。

选择漏洞，填写必要信息，点击探测，可自行在 dnslog 平台查看结果。

**经测试，部分站点反序列化漏洞状态码 404、500 均有 dnslog，建议以 dnslog 平台记录为准。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLcycltzeueBosge3PeuTTvoPhNeuynJsmV62btMLmzj1RGWRnVx4UXQ/640?wx_fmt=png)

### 一键 getshell

本工具一键 getshell 功能打入的 webshell 同时打入回显、冰蝎、哥斯拉。请求头与连接密码信息均为下方所示。

**反序列化漏洞打入内存马情况以实际连接情况为准。**

```
Filter 内存马连接地址：http://x.x.x.x/...网站目录.../*
```

```
--------------------------------------------------------------------------------------------
```

```
回显
```

```
添加请求头
```

```
x-client-referer:http://www.baidu.com/
```

```
x-client-data:testzxcv
```

```
testzxcv:
```

```
--------------------------------------------------------------------------------------------
```

```
冰蝎
```

```
添加请求头
```

```
x-client-referer:http://www.baidu.com/
```

```
x-client-data:behinder
```

```
密码
```

```
chaveyyds
```

```
--------------------------------------------------------------------------------------------
```

```
哥斯拉
```

```
添加请求头
```

```
x-client-referer:http://www.baidu.com/
```

```
x-client-data:godzilla
```

```
密钥
```

```
chaveyyds
```

```
密码
```

```
pass
```

以 **Lfw\_Core\_Rpc 文件上传** 漏洞为例。

选择漏洞，输入目标url，点击 getshell。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLd78LVcgVu6pakH2911Q4lxw99FuLHM9YTEyibv7zhDgQWXC5t3c2o0g/640?wx_fmt=png)

根据连接信息连接利用即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcL37s3ZXYQtqOl49OiaCOSW4JtLFFoSFmANGsaU3Qx7BA2bMxmRDlUibWA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLwYKWddlz5oCJ1jY7kVyicvO5ibKw7eBkibYEHgZ4IWUf3JKbYRaRrSNIw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLJzXHDUbhuJCc6Q3LoYbJorPjiazXTZ5scY7icia8lW4RialeMgoggjibMfA/640?wx_fmt=png)

### 命令执行

以 **ActionServletHandler 反序列化** 漏洞为例。

进入 **命令执行** 模块，输入命令，点击执行即可，目前该漏洞已支持 **CC6** 与 **freemarker.template.utility.Execute** 两种命令执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLuKctGbia8bxmJ4FCpVQWZZOicWZb4XUxUhDDOxIDjsA5ocdTzyoaNnBg/640?wx_fmt=png)

### 文件上传

以 **Lfw\_Core\_Rpc 文件上传** 漏洞为例。

选择漏洞，进入文件上传模块，输入文件名，文件内容，点击上传即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLwq3UXvKvd5cPguOzlGWvBwJeMCBgzqbHI2rLLomY3yVEiaL5rJshiayg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/y5xFHTW9iaNXQpfl6EPaAvzVhcIqQOFcLlzpbpxeCFQjHa6hUecSnhCR2gggWurQLB6sbk7paIbVnLMgEKNkFibg/640?wx_fmt=png)

关注公众号回复“20260109”获取工具地址。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

W小哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

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