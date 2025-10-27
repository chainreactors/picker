---
title: 逆向分析Office VBS宏类型文档
url: https://www.secpulse.com/archives/205567.html
source: 安全脉搏
date: 2024-12-25
fetch_date: 2025-10-06T19:36:03.543973
---

# 逆向分析Office VBS宏类型文档

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

# 逆向分析Office VBS宏类型文档

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-24

12,977

该题目贴合实际，在实战中经常遇到此类宏病毒。

将Office文档中嵌入以VBA(Visual Basic forApplications)编写的宏代码脚本，当运行Office文档时，便可以执行各种命令。

VBA脚本文件重定向能够将脚本默认文件vbaProject.bin进行替换，在打开文本时加载其他文件，增加分析者的分析复杂程度。

## 1、初步分析

> 在 Office 2007 之后的 Office 文档格式采用的是 OOXML 标准格式。那什么是OOXML 标准？这里的 OOXML 的全称是 Office Open XML File Formats或被称为 OpenXML 格式，这是一个基于 zip+xml定义的文档格式。简单的说就是Office文档是一些xml文档压缩文件，因此我们将一个word文档进行zip解压，可以获得一些xml文件

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525118.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525119.png)

打开发现是一堆乱码，此时就需要借助大佬们的工具了。

## 2、oletools

oletools对该文件进行分析，oletools将宏源码完整的还原了出来。

官网：<https://github.com/decalage2/oletools/releases>

这里采用pip安装模式

```
pip install -U oletools
```

运行命令

```
olevba -c protected_secret.docm > code.vbs
```

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525120.png)

## 3、分析vbs代码

直接搜索：`AutoOpen`

里面有太多垃圾代码了

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525121.png)

首先将输入的flag异或7

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525122.png)

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525123.png)

有点意思了，解码exe的base64编码，然后运行exe执行操作，最后再删除exe程序

## 4、运行Vbs得到exe

将重要的代码拿出来，然后生成exe

```
Set fso = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("WScript.Shell")

/*
省略了一大堆 base64赋值串
*/

tempPath = "D:\temp11\temp"
Set tempfile = fso.CreateTextFile(tempPath, True)
fso.GetFile(tempPath).Attributes = 2
tempfile.WriteLine xpkdb
tempfile.Close

batPath = "D:\temp11\temp.bat"
Set batFile = fso.CreateTextFile(batPath, True)
fso.GetFile(batPath).Attributes = 2
batFile.WriteLine "@echo off"
batFile.WriteLine "certutil -decode temp1 temp|certutil -decode temp temp.exe"
batFile.Close
Set objExec = objShell.Exec(batPath)
```

保存为vbs运行，但是我电脑有点小问题没跑运行起来

因此我们采取另一种方法，直接将base64提取出来

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525124.png)

代码很简单，将提取出来的代码放进Cyberchef进行提取即可

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525125.png)

[download.exe](https://www.yijinglab.com/assets/download-20240908163140-1jiyyj2.exe)

## 5、分析exe

![image](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410281525126.png)

很简单的代码，就是位移

## 6、解密

```
v9 = [0]*54
v9[0] = 4288
v9[1] = 4480
v9[2] = 5376
v9[3] = 4352
v9[4] = 5312
v9[5] = 4160
v9[6] = 7936
v9[7] = 5184
v9[8] = 6464
v9[9] = 6528
v9[10] = 5632
v9[11] = 3456
v9[12] = 7424
v9[13] = 5632
v9[14] = 6336
v9[15] = 6528
v9[16] = 6720
v9[17] = 6144
v9[18] = 6272
v9[19] = 7488
v9[20] = 6656
v9[21] = 7296
v9[22] = 7424
v9[23] = 2432
v9[24] = 2432
v9[25] = 2432
v9[26] = 5632
v9[27] = 4416
v9[28] = 3456
v9[29] = 7168
v9[30] = 6528
v9[31] = 7488
v9[32] = 6272
v9[33] = 5632
v9[34] = 3520
v9[35] = 6208
v9[36] = 5632
v9[37] = 4736
v9[38] = 6528
v9[39] = 6400
v9[40] = 7488
v9[41] = 3520
v9[42] = 5632
v9[43] = 5184
v9[44] = 3456
v9[45] = 7488
v9[46] = 7296
v9[47] = 3200
v9[48] = 6272
v9[49] = 7424
v9[50] = 2432
v9[51] = 2432
v9[52] = 2432
v9[53] = 7808

flag = ''
for i in range(54):
    flag += chr(v9[i] >> 6 ^ 7)

print(flag)
```

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205567.html**](https://www.secpulse.com/archives/205567.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![记一次有点抽象的渗透经历](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/VCG41N1195673150.png)

  记一次有点抽象的渗透经历](https://www.secpulse.com/archives/205044.html "详细阅读 记一次有点抽象的渗透经历")
* [![浅谈内联钩取原理与实现](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/06/VCG211415001580-210x140.jpg)

  浅谈内联钩取原理与实现](https://www.secpulse.com/archives/205124.html "详细阅读 浅谈内联钩取原理与实现")
* [![浅谈进程隐藏技术](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/vcg.png)

  浅谈进程隐藏技术](https://www.secpulse.com/archives/205188.html "详细阅读 浅谈进程隐藏技术")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://www...