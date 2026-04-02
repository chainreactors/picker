---
title: 给 Linux 新手的
url: https://mp.weixin.qq.com/s/-AWL1ZGKenieCttiENHZ-w
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:27:55.845442
---

# 给 Linux 新手的

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/V1icTKBjMOiauQpMxTWTWz5pqJ4UpWeBwZ4iaMhEZvMF4f18jzOibeeYknUBJoibRRCmtiaU1ywPQhYGB5YEHgKR3yZ0GJP6aOqU8A452ogaHaRBU/0?wx_fmt=jpeg)

# 给 Linux 新手的

原创

guowei
guowei

网络安全直通车

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/V1icTKBjMOiavHRXGDXMTdS0UgLPlLS0dNicz30mM6XeFQWx76XbhHGNXF4UQFsOxWPtFmjp2K2qCZR5P4ht40FibNJXDUO3qr4riajlN6nUcsSw/640?wx_fmt=png&from=appmsg)

是教你当“理论派”，而是**手把手教你从 0 到 1 用 Linux**——从装系统、敲命令，到管用户、配权限，全是**企业里真正常用的操作**，学了就能直接上手干活。

### 二、核心内容拆成 5 个“接地气模块”

#### 1. 先搞懂 Linux 是啥（第1-3章）

* **Linux 不是“另一个 Windows”**：

  Windows 靠鼠标点（图形界面），Linux 靠**敲命令**（字符界面）——但命令效率高（比如建用户，Windows 点 10 次，Linux 1 条命令搞定）。

  Linux 安全稳定（不用装杀毒软件，服务器能连续跑 1 年不重启），所以**企业服务器几乎都用 Linux**（比如淘宝、微信的后台）。
* **装系统像“搭积木”**：

  用 VMware 虚拟机（相当于“电脑里的电脑”）装 CentOS/Rocky Linux（企业最常用的系统），步骤是：**建虚拟机→选镜像→配分区→设密码**，和装 Windows 一样简单。
* **CentOS 没了？用 Rocky Linux 替补**：

  因为 CentOS 停止维护，作者推荐用 Rocky Linux（和 CentOS 一模一样，不用重新学）。

#### 2. 必学的 Linux 命令（第5章）

**命令是 Linux 的“语言”**，重点是**高频实用命令**，用“大白话+例子”讲：

* **系统状态**：`top`（看 CPU/内存有没有“累坏”）、`free -m`（看内存剩多少）、`df -h`（看硬盘剩多少空间）。
* **文件操作**：`ls -al`（看所有文件，包括隐藏的）、`cd`（切目录，`cd ~`回家目录，`cd ..`回上一层）、`cp -r`（复制文件夹）、`rm -rf`（删除，**千万别删 `/`根目录！会炸系统**）。
* **看日志**：`tail -f 日志文件`（实时监控日志，比如服务器报错时看“哪里错了”）。

#### 3. Vim 编辑器：Linux 里的“记事本 Pro”（第6章）

* **三个模式要分清**：

+ 命令模式（默认）：用 `k/j/h/l`移动光标，`dd`删行，`yy`复制，`p`粘贴（不用鼠标，手快的人爱死）。
+ 编辑模式（按 `i`进入）：像普通记事本一样打字，底部显示“--插入--”。
+ 末行模式（按 `:`进入）：`:w`保存，`:q`退出，`:wq!`强制保存退出，`:s/旧内容/新内容/g`批量替换（比如把“root”改成“admin”）。

#### 4. 管用户和用户组（第7章）

**Linux 是多用户系统，得“分权限”**：

* **用户类型**：

+ root（超级管理员，权限无限大，删系统文件会崩，**别乱用**）。
+ 系统用户（比如 `sshd`，用来跑服务，不能登录）。
+ 普通用户（比如 `user1`，员工用的，权限受限）。

* **用户组是“批量管用户”**：

  把相同岗位的 user 放进一个组（比如“开发组”“测试组”），改组的权限=改所有人的权限，不用一个个调。
* **常用命令**：

  `useradd user1`（建用户）、`passwd user1`（设密码）、`usermod -G 组名 user1`（把用户加进组）、`groupadd 组名`（建组）。

#### 5. 文件权限：不让“外人”乱改（第8章）

**权限是 Linux 的“防盗门”**，每个文件/目录都有“谁能看、谁能改、谁能执行”：

* **权限符号**：`r`（读，看内容）、`w`（写，改内容）、`x`（执行，运行脚本/进目录）。
* **权限位置**：比如 `-rw-r--r--`：

+ 第一位：`-`是文件，`d`是目录。
+ 2-4 位：属主（文件主人）的权限（`rw-`=能读能写）。
+ 5-7 位：属组（主人的组）的权限（`r--`=只能读）。
+ 8-10 位：其他人的权限（`r--`=只能读）。

* **改权限命令**：`chmod 755 文件`（八进制，`7=rwx`，`5=r-x`），`chown 属主:属组 文件`（改主人）。

### 三、这本书的“隐藏福利”

* **配套资源超全**：有视频教程、在线实验平台、命令速查表，相当于“买书送老师”。
* **避开坑**：比如提醒你“别用 root 删文件”“CentOS 换成 Rocky”“rm -rf 别乱敲”，都是作者踩过的雷。

### 四、总结：这本书适合谁？

* **想进运维/后端开发的新手**：学了能直接上手企业的 Linux 服务器。
* **觉得 Linux 难的人**：用“聊天式”讲解，把复杂概念拆成“生活比喻”（比如把权限比作“防盗门”），不用记硬公式。
* **需要用 Linux 干活的人**：全是**企业实战案例**（比如配服务器、查日志、管用户），学了就能用。

简单来说，这本书就是**“Linux 从入门到能干活”的快速通道**——不用懂内核原理，不用记复杂命令，跟着做就能搞定企业里的 Linux 操作！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

网络安全直通车

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/J8AVIknUyQlKATmLAFibRG7DezjkNIEqbwEYR0fRY4WYibs8SZ8CtNC2NZHEu3nicHJx1rVoe96v4XZDpdRJ2aWbQ/0?wx_fmt=png)

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