---
title: 11个让你吃惊的Linux终端命令
url: https://www.secpulse.com/archives/192628.html
source: 安全脉搏
date: 2022-12-02
fetch_date: 2025-10-04T00:15:54.212217
---

# 11个让你吃惊的Linux终端命令

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

# 11个让你吃惊的Linux终端命令

[Linux](https://www.secpulse.com/archives/category/articles/system/linux)

[Lemon](https://www.secpulse.com/newpage/author?author_id=5109)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-12-01

40,427

来自：Linux-开源社区

原文：http://linux.about.com/od/commands/tp/11-Linux-Terminal-Commands-That-Will-Rock-Your-World.htm

译文：LCTT  http://linux.cn/article-5438-1.html

我已经用了十年的Linux了，通过今天这篇文章我将向大家展示一系列的命令、工具和技巧，我希望一开始就有人告诉我这些，而不是曾在我成长道路上绊住我。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192628-1669872929.jpg)

**1.命令行日常系快捷键**

**如下的快捷方式非常有用，能够极大的提升你的工作效率：**

●CTRL + U - 剪切光标前的内容

●CTRL + K - 剪切光标至行末的内容

●CTRL + Y - 粘贴

●CTRL + E - 移动光标到行末

●CTRL + A - 移动光标到行首

●ALT + F - 跳向下一个空格

●ALT + B - 跳回上一个空格

●ALT + Backspace - 删除前一个单词

●CTRL + W - 剪切光标前一个单词

●Shift + Insert - 向终端内粘贴文本

那么为了让上述内容更易理解来看下面的这行命令。

```
sudo apt-get intall programname
```

如你所见，命令中存在拼写错误，为了正常执行需要把“intall”替换成“install”。

想象现在光标正在行末，我们有很多的方法将她退回单词install并替换它。

我可以按两次ALT+B这样光标就会在如下的位置（这里用指代光标的位置）。

```
sudo apt-get^intall programname
```

现在你可以按两下方向键并将“s”插入到install中去了。

如果你想将浏览器中的文本复制到终端，可以使用快捷键"shift + insert"。

**2.SUDO !!**

如果你还不知道这个命令，我觉得你应该好好感谢我，因为如果你不知道的话，那每次你在输入长串命令后看到“permission denied”后一定会痛苦不堪。

●sudo !!

**如何使用sudo !!？很简单。试想你刚输入了如下命令：**

```
apt-get install ranger
```

一定会出现“Permission denied”，除非你已经登录了足够高权限的账户。

sudo !! 就会用 sudo 的形式运行上一条命令。所以上一条命令就变成了这样：

```
sudo apt-get install ranger
```

如果你不知道什么是sudo，戳这里。

（警告！主页君强烈反对使用这个命令，因为如果万一上个命令存在一些笔误或者你搞错了哪条是上一条命令，那么有可能带来的后果是灾难性的！所以，千万不要执行这条命令！千万不要执行这条命令！千万不要执行这条命令！重要的事情重复三遍。）

**3.暂停并在后台运行命令**

我曾经写过一篇如何在终端后台运行命令的指南。

●CTRL + Z - 暂停应用程序

●fg - 重新将程序唤到前台

如何使用这个技巧呢?

**试想你正用nano编辑一个文件：**

```
sudo nano abc.txt
```

文件编辑到一半你意识到你需要马上在终端输入些命令，但是nano在前台运行让你不能输入。

你可能觉得唯一的方法就是保存文件，退出 nano，运行命令以后在重新打开nano。

其实你只要按CTRL + Z，前台的命令就会暂停，画面就切回到命令行了。然后你就能运行你想要运行命令，等命令运行完后在终端窗口输入“fg”就可以回到先前暂停的任务。

有一个尝试非常有趣就是用nano打开文件，输入一些东西然后暂停会话。再用nano打开另一个文件，输入一些什么后再暂停会话。如果你输入“fg”你将回到第二个用nano打开的文件。只有退出nano再输入“fg”，你才会回到第一个用nano打开的文件。

**4.使用nohup在登出SSH会话后仍运行命令**

如果你用ssh登录别的机器时，nohup命令真的非常有用。

那么怎么使用nohup呢？

想象一下你使用ssh远程登录到另一台电脑上，你运行了一条非常耗时的命令然后退出了ssh会话，不过命令仍在执行。而nohup可以将这一场景变成现实。

举个例子，因为测试的需要，我用我的树莓派来下载发行版。我绝对不会给我的树莓派外接显示器、键盘或鼠标。

一般我总是用SSH从笔记本电脑连接到树莓派。如果我在不用nohup的情况下使用树莓派下载大型文件，那我就必须等待到下载完成后，才能登出ssh会话关掉笔记本。可如果是这样，那我为什么要使用树莓派下文件呢？

使用nohup的方法也很简单，只需如下例中在nohup后输入要执行的命令即可：

```
nohup wget http://mirror.is.co.za/mirrors/linuxmint.com/iso//stable/17.1/linuxmint-17.1-cinnamon-64bit.iso &
```

**5.‘在（at）’特定的时间运行Linux命令**

‘nohup’命令在你用SSH连接到服务器，并在上面保持执行SSH登出前任务的时候十分有用。

想一下如果你需要在特定的时间执行相同的命令，这种情况该怎么办呢？

命令‘at’就能妥善解决这一情况。以下是‘at’使用示例。

at 10:38 PM Fri

at> cowsay 'hello'

at> CTRL + D

上面的命令能在周五下午10时38分运行程序cowsay。

使用的语法就是‘at’后追加日期时间。当at>提示符出现后就可以输入你想在那个时间运行的命令了。

CTRL + D 返回终端。

还有许多日期和时间的格式，都需要你好好翻一翻‘at’的man手册来找到更多的使用方式。

**6.Man手册**

Man手册会为你列出命令和参数的使用大纲，教你如何使用她们。Man手册看起来沉闷呆板。（我思忖她们也不是被设计来娱乐我们的）。

不过这不代表你不能做些什么来使她们变得漂亮些。

```
export PAGER=most
```

你需要安装 ‘most’；她会使你的你的man手册的色彩更加绚丽。

**你可以用以下命令给man手册设定指定的行长：**

```
export MANWIDTH=80
```

最后，如果你有一个可用的浏览器，你可以使用-H在默认浏览器中打开任意的man页。

```
man -H <command>
```

注意啦，以上的命令只有在你将默认的浏览器设置到环境变量$BROWSER中了之后才效果哟。

**7.使用htop查看和管理进程**

你用哪个命令找出电脑上正在运行的进程的呢？我敢打赌是‘ps’并在其后加不同的参数来得到你所想要的不同输出。

安装‘htop’吧！绝对让你相见恨晚。

htop在终端中将进程以列表的方式呈现，有点类似于Windows中的任务管理器。你可以使用功能键的组合来切换排列的方式和展示出来的项。你也可以在htop中直接杀死进程。

在终端中简单的输入htop即可运行。

```
htop
```

**8.使用ranger浏览文件系统**

如果说htop是命令行进程控制的好帮手，那么ranger就是命令行浏览文件系统的好帮手。

你在用之前可能需要先安装，不过一旦安装了以后就可以在命令行输入以下命令启动她：

```
ranger
```

在命令行窗口中ranger和一些别的文件管理器很像，但是相比上下结构布局，她是左右结构的，这意味着你按左方向键你将前进到上一个文件夹，而右方向键则会切换到下一个。

在使用前ranger的man手册还是值得一读的，这样你就可以用快捷键操作ranger了。

**9.取消关机**

无论是在命令行还是图形用户界面关机后，才发现自己不是真的想要关机。

```
shutdown -c
```

需要注意的是，如果关机已经开始则有可能来不及停止关机。

**以下是另一个可以尝试命令：**

●pkill shutdown

**10.杀死挂起进程的简单方法**

想象一下，你正在运行的应用程序不明原因的僵死了。

你可以使用‘ps -ef’来找到该进程后杀掉或者使用‘htop’。

有一个更快、更容易的命令叫做xkill。

简单的在终端中输入以下命令并在窗口中点击你想杀死的应用程序。

```
xkill
```

那如果整个系统挂掉了怎么办呢？

按住键盘上的‘alt’和‘sysrq’不放，然后慢慢输入以下键：

●REISUB

这样不按电源键你的计算机也能重启了。

**11.下载Youtube视频**

一般来说我们大多数人都喜欢看Youtube的视频，也会通过钟爱的播放器播放Youtube的流媒体。

如果你需要离线一段时间（比如：从苏格兰南部坐飞机到英格兰南部旅游的这段时间）那么你可能希望下载一些视频到存储设备中，到闲暇时观看。

你所要做的就是从包管理器中安装youtube-dl。

**你可以用以下命令使用youtube-dl：**

```
youtube-dl url-to-video
```

你可以在Youtubu视频页面点击分享链接得到视频的url。只要简单的复制链接在粘帖到命令行就行了（要用shift + insert快捷键哟）。

**总结**

希望你在这篇文章中得到帮助，并且在这11条中找到至少一条让你惊叹“原来可以这样”的技巧。

**侵权请私聊公众号删文**

**本文作者：[Lemon](newpage/author?author_id=5109)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192628.html**](https://www.secpulse.com/archives/192628.html)

Tags: [Linux](https://www.secpulse.com/archives/tag/linux)、[sudo](https://www.secpulse.com/archives/tag/sudo)、[快捷键](https://www.secpulse.com/archives/tag/%E5%BF%AB%E6%8D%B7%E9%94%AE)、[终端命令](https://www.secpulse.com/archives/tag/%E7%BB%88%E7%AB%AF%E5%91%BD%E4%BB%A4)

点赞：
7
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Sudo堆溢出漏洞(CVE-2021-3156)复现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1688003832385-300x237.png)

  Sudo堆溢出漏洞(CVE-2021-3…](https://www.secpulse.com/archives/202423.html "详细阅读 Sudo堆溢出漏洞(CVE-2021-3156)复现")
* [![某次演练复盘总结](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1687313516203-300x202.png)

  某次演练复盘总结](https://www.secpulse.com/archives/202339.html "详细阅读 某次演练复盘总结")
* [![【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199280-1681978319-300x158.png)

  【勒索防护】MSI 等多个企业已遭受攻击…](https://www.secpulse.com/archives/199280.html "详细阅读 【勒索防护】MSI 等多个企业已遭受攻击！MoneyMessage 勒索软件突现")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( ht...