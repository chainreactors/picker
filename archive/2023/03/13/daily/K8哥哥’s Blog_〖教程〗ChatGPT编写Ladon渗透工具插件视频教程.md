---
title: 〖教程〗ChatGPT编写Ladon渗透工具插件视频教程
url: http://k8gege.org/p/ChatGPT.html
source: K8哥哥’s Blog
date: 2023-03-13
fetch_date: 2025-10-04T09:25:29.448144
---

# 〖教程〗ChatGPT编写Ladon渗透工具插件视频教程

[![logo](/../k8img/logo.png)

### K8哥哥](/ "K8gege")

## 没有绝对安全的系统

[K8哥哥’s Blog](http://k8gege.org)

* [Home](/)
* [Ladon](/Ladon/)
* [Code](/tags/Code/)
* [Exp](/tags/Exp/)
* [Tool](/tags/Tool/)
* [Music](https://k8music.github.io)
* [Archives](/archives/)
* [Friends](/friends/)
* [Rss](/atom.xml)

# 〖教程〗ChatGPT编写Ladon渗透工具插件视频教程

[Ladon](/categories/Ladon/)

[Ladon](/tags/Ladon/)

2023/03/12

本文于**922**
天之前发表

# 【视频】ChatGPT编写Ladon渗透插件之端口扫描.rar【视频】ChatGPT编写Ladon渗透插件之网页标题获取.rar

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

![使用http访问查看图片](/k8img/Ladon/LadonGUI.png)

### Ladon简介

Ladon模块化网络渗透工具，可PowerShell模块化、可CS插件化、可内存加载，无文件扫描。含端口扫描、服务识别、网络资产探测、密码审计、高危漏洞检测、漏洞利用、密码读取以及一键GetShell，支持批量A段/B段/C段以及跨网段扫描，支持URL、主机、域名列表扫描等。10.9版本内置200个功能模块,外部模块18个,网络资产探测模块28个通过多种协议(ICMP\NBT\DNS\MAC\SMB\WMI\SSH\HTTP\HTTPS\Exchange\mssql\FTP\RDP)以及方法快速获取目标网络存活主机IP、计算机名、工作组、共享资源、网卡地址、操作系统版本、网站、子域名、中间件、开放服务、路由器、交换机、数据库、打印机等信息，高危漏洞检测16个包含Cisco、Zimbra、Exchange、DrayTek、MS17010、SMBGhost、Weblogic、ActiveMQ、Tomcat、Struts2系列、Printer等，密码审计23个含数据库(Mysql、Oracle、MSSQL)、FTP、SSH、VNC、Windows(LDAP、SMB/IPC、NBT、WMI、SmbHash、WmiHash、Winrm)、BasicAuth、Tomcat、Weblogic、Rar等，远程执行命令包含(smbexec/wmiexe/psexec/atexec/sshexec/webshell),Web指纹识别模块可识别135+（Web应用、中间件、脚本类型、页面类型）等，本地提权21+含SweetPotato\BadPotato\EfsPotato\BypassUAC,可高度自定义插件POC支持.NET程序集、DLL(C#/Delphi/VC)、PowerShell等语言编写的插件,支持通过配置INI批量调用任意外部程序或命令，EXP生成器可一键生成漏洞POC快速扩展扫描能力。Ladon支持Cobalt Strike插件化扫描快速拓展内网进行横向移动。

### C#开发Ladon渗透工具插件例子

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` using System; using System.Collections.Generic; using System.Text; using System.Net; using System.Text.RegularExpressions;  namespace LadonDLL {     public class scan     {         public static string run(string ip)         {             if (string.IsNullOrEmpty(ip))                 return "";             else             {                 return "demo: "+ip + "\r\n";             }          }     } } ``` |

Demo的功能为打印存活IP，编译DLL，把DLL放在Ladon目录下，使用以下命令测试，结果将输出ICMP即可Ping通的机器IP，因为Ladon默认先使用ICMP探测存活主机，然后再执行插件内部对应的功能。

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` Ladon netscan.dll  扫描当前机器所在C段 Ladon 192.168.1.1/24 netscan.dll  指定C段 ``` |

工程源码：<https://github.com/k8gege/Ladon/blob/master/Demo_DLL.rar> 使用VS2010或以上版本打开，若是ChatGPT生成的代码建议使用VS2015或之后版本，不然可能有些代码不能直接使用。

### 简单了解ChatGPT回答问题的能力

给它输入Ladon简明教程地址，它给我胡编了一个答案，逻辑能力非常强，简直以假乱真。应该根据很多类似工具参考生成了固定模板，你告诉它Ladon是渗透工具，它就胡编乱写一个简介，不熟悉Ladon的人一看估计以为它说的是真的。甚至我在群里看到有人发的人工智能说k8gege也是一款渗透工具，不知道它是不是用的旧版chatGPT，虽然乱说，但逻辑能力是非常强的。

![使用http访问查看图片](/k8img/Ladon/ai/00.PNG)

![使用http访问查看图片](/k8img/Ladon/ai/0.PNG)

让它把Ladon简介和版本说明做个排版，效果非常棒
![使用http访问查看图片](/k8img/Ladon/ai/info.PNG)

![使用http访问查看图片](/k8img/Ladon/ai/info2.PNG)

### ChatGPT编写Ladon渗透工具插件之获取网页标题

跟它聊天或做个表格，那就太小看它了，对于渗透或开发人员，我们可以让它帮我们写一些简单工具，或者一些功能模块。大家都知道Ladon工具的插件开发非常简单，一是直接配置INI插件，二是LadonEXP一键生成，三是自己编程实现。三的要求相对高一点，需要使用人员有一定编程能力。

我们让ChatGPT参考插件例子源码，让它使用C#编写一个获取网页标题的插件
![使用http访问查看图片](/k8img/Ladon/ai/1.PNG)

没等几秒钟，它立即给出以下代码
![使用http访问查看图片](/k8img/Ladon/ai/2.PNG)

打开demo工程，复制它给的代码，全选粘贴到工程里面去，编译并运行，测试看看

![使用http访问查看图片](/k8img/Ladon/ai/3.PNG)

运行结果报错，原因是我们扫描的是C段IP，即传入参数是IP，但获取网页标题需要的是URL，所以还得让它把IP处理成URL
![使用http访问查看图片](/k8img/Ladon/ai/4.PNG)
经过它的修改，可以成功获取网页标题，由于扫的是C段，我们并不知道哪个IP上面部署了IIS7，所以得让它把结果改下
![使用http访问查看图片](/k8img/Ladon/ai/5.PNG)
很快它又改好代码，再次编译测试
![使用http访问查看图片](/k8img/Ladon/ai/6.PNG)
测试发现除了获取标题外，还回显了很多访问不到的URL
![使用http访问查看图片](/k8img/Ladon/ai/7.PNG)
渗透时，我们不需要对不存在的URL进行分析，或者说存在但是当前IP被目标限制了访问不到，所以探测不到。不管是因为不存在而访问不到，还是IP限制访问不到，都无法对它进行渗透，如果C段存活主机非常多，或者说扫描B段，既然我们不关注不可访问结果，那么没必要让它显示。
![使用http访问查看图片](/k8img/Ladon/ai/8.PNG)
它给出了最终的代码，编译后，使用Ladon扫描C段，就只回显网页标题了
![使用http访问查看图片](/k8img/Ladon/ai/9.PNG)

#### ChatGPT实现Ladon渗透插件获取网页标题代码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 ``` | ``` using System; using System.Collections.Generic; using System.Text; using System.Net; using System.Text.RegularExpressions;  namespace LadonDLL {     public class scan     {         public static string run(string input)         {             if (string.IsNullOrEmpty(input))                 return "";              string url = "";             Uri uriResult;             if (Uri.TryCreate(input, UriKind.Absolute, out uriResult)                 && (uriResult.Scheme == Uri.UriSchemeHttp || uriResult.Scheme == Uri.UriSchemeHttps))             {                 url = uriResult.ToString();             }             else if (Regex.IsMatch(input, @"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(:\d+)?$"))             {                 url = "http://" + input;             }              if (string.IsNullOrEmpty(url))             {                 return "Invalid URL or IP address";             }             else             {                 string title = "";                 try                 {                     WebClient client = new WebClient();                     string html = client.DownloadString(url);                     Regex regex = new Regex(@"(?<=<title.*>)([\s\S]*)(?=</title>)", RegexOptions.IgnoreCase);                     title = regex.Match(html).Value.Trim();                 }                 catch                 {                     return "";                 }                 return url + "\t" + title + "\r\n";             }         }     } } ``` |

#### ChatGPT编写Ladon渗透插件之端口扫描代码

```
using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;

namespace LadonDLL
{
    public class scan
    {
        public static string run(string ip)
        {
            if (string.IsNullOrEmpty(ip))
                return "";

            // 要扫描的端口列表
            List<int> ports = new List<int>() { 21, 80, 443, 22, 445, 135 };

            string result = "";
            // 扫描每个端口并添加结果到字符串
            foreach (int port in ports)
            {
                if (IsPortOpen(ip, port))
                {
                    result += $"{ip}\t{port}\tOPEN\r\n";
                }
            }

            return result;
        }

        // 检查端口是否开放
        static bool IsPortOpen(string ip, int port)
        {
            try
            {
                using (TcpClient client = new TcpClient())
                {
                    client.Connect(ip, port);
                    return true;
                }
            }
            catch
            {
                return false;
            }
        }
    }
}

```csharp

PS：Ladon自带模块WebScan或WhatCMS或PortScan均包含网页标题功能获取，PortScan端口扫描模块也包含很多协议指纹识别，大家有兴趣也可以让chatGPT帮实现更多更好用的插件功能。

### 小结
本文演示如何使用ChatGPT开发Ladon插件，快速扩展Ladon扫描能力，借助ChatGPT，编程新手也可以快速编写POC。有一点大家要注意，使用ChatGPT做一件事最好只在一个chat里操作，不然它会结合上下文，把你的需求搞乱，给多余或混乱代码。你自身的专业能力越强，它和你的对话就越专业，你问得模糊不清，自己一知半解，你的专业术语或表述不对，它给你的结果自然垃圾。甚至有时候它给的很多代码压根就不能用，但是它胡编乱造的能力，让你一眼觉得代码是正确可用的，实际编译发现，不能用，比如某些协议它给的包就压根不对，我测试了十几次，同样问题它随机给了好几次代码，其中有3次重复，但这些不是重点，重点是都用不了，有是发包协议是这个数组有时是另一个，有时是对的，但整个请求代码还有其它错误，导致用不了，你得告诉它教它改，虽然这样，就它目前的能力，也是非常强的，让它写一个Ladon简单功能插件，基本也就5分钟左右，当然如果需求足够清晰，够了解它，让它不要乱改什么，要实现的功能，每一条都写清楚，也有可能一步到位，一问就搞定，加上编译测试，整个过程估计也就一分钟左右。

### 视频教程

https://github.com/k8gege/ChatLadon
【视频】ChatGPT编写Ladon渗透插件之端口扫描.rar
【视频】ChatGPT编写Ladon渗透插件之网页标题获取.rar

### 工具下载

最新版本：http://k8gege.org/Download
历史版本: https://github.com/k8gege/Ladon/releases

<div style="text-align: center; width: 710px; border: green solid 0px;">
<img alt="" src="http://k8gege.org/img/k8team.jpg" style="display: inline-block;width: 250px;height: 300px;" />
</div>
```

### 转载声明

K8博客文章随意转载，转载请注明出处！ © K8gege <http://k8gege.org>

![](../images/k8join2.png)

扫码加入K8小密圈

转载声明：
K8博客文章随意转载，转载请注明出处！ © [K8gege](http://k8gege.org)

[上一篇

〖工具〗LadonGo开源全平台内网渗透扫描器](/p/LadonGo.html "〖工具〗LadonGo开源全平台内网渗透扫描器")
[下一篇

〖key〗VS2022 VS2019 VS2017最新注册码序列号](/p/vsKey.html "〖key〗VS2022 VS2019 VS2017最新注册码序列号")

### Table of Contents

1. 【视频】ChatGPT编写Ladon渗透插件之端口扫描.rar【视频】ChatGPT编写Ladon渗透插件之网页标题获取.rar
   1. [Ladon简介](#Ladon%E7%AE%80%E4%BB%8B)
   2. [C#开发Ladon渗透工具插件例子](#C-%E5%BC...