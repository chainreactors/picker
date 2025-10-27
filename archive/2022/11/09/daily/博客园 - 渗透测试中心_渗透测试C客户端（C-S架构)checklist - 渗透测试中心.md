---
title: 渗透测试C客户端（C-S架构)checklist - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/16868895.html
source: 博客园 - 渗透测试中心
date: 2022-11-09
fetch_date: 2025-10-03T22:05:52.597483
---

# 渗透测试C客户端（C-S架构)checklist - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [渗透测试C客户端（C-S架构)checklist](https://www.cnblogs.com/backlion/p/16868895.html "发布于 2022-11-08 10:47")

## 0x00 前言

本项目主要针对pc客户端（cs架构）渗透测试，结合自身测试经验和网络资料形成checklist，如有任何问题，欢迎联系，期待大家贡献更多的技巧和案例。

## 0x01 概述

PC客户端，有丰富功能的GUI，C-S架构。

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104634024-1259424875.jpg)

## 0x02 开发语言

C#(.NET)，JAVA，DELPHI，C，C++......

## 0x03 协议

TCP、HTTP(S)，TDS......

## 0x04 数据库

oracle，mssql，db2......

## 0x05 测试工具

//相关工具下载：<https://github.com/theLSA/hack-cs-tools>

dvta： pc客户端靶场

ida pro： 静态分析工具

ollydbg：动态分析工具

CFF Explorer：PE文件分析

PEID：查壳工具

exeinfope/studype：pe文件分析

wireshark：观察流量

tcpview：观察tcp流量

echo Mirage：可拦截tcp流量

burpsuite：http(s)抓包

proxifier：全局代理流量

procmon：文件和注册表监控

regshot：注册表变化对比

process Hacker：进程分析

RegfromApp：注册表监控

WSExplorer：岁月联盟进程抓包工具

strings：查看程序的字符串

.net[反]编译：

dotpeek

de4dot

dnspy

ilspy

sae

ildasm

ilasm

Java反编译

jad

jd-gui

jadx

dex2jar

在线版：
[javare.cn](https://github.com/yaoxiaodai/CS-checklist/blob/master)

[www.javadecompilers.com](http://www.javadecompilers.com/)

Reflexil：组装编辑器（可以作为ilspy插件）

Vcg：自动化代码审计工具

BinScope：二进制分析工具

## 0x06 代理设置

大部分客户端没有代理配置功能，需要自行设置全局代理，如下两种方法：

1）IE-internet设置-连接-局域网设置。

2）proxifier --> proxy server/proxification rules

//http的流量可以结合burpsuite方便测试（proxy server设置为burp代理地址）。

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104634768-958814794.jpg)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104635462-1302757946.jpg)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104636140-1382229849.jpg)

## 0x07 测试点

### 0. 信息收集

编译信息，开发环境/语言，使用协议，数据库，ip，混淆/加密，是否加壳等。

案例0-CFF查看客户端信息（如编译环境）

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104636932-933767068.jpg)

### 1. 逆向工程

反编译，源代码泄露，硬编码key/password，加解密逻辑，角色判断逻辑（0-admin，1-normaluser），后门等。

案例0-反编译获取加解密逻辑并编写解密工具

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104637715-765430904.jpg)

通过该逻辑和获取的信息

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104638416-2062982296.jpg)

Encrypted Text: CTsvjZ0jQghXYWbSRcPxpQ==

AES KEY: J8gLXc454o5tW2HEF7HahcXPufj9v8k8

IV: fq20T0gMnXa6g0l4

编写解密工具

using System; using System.Collections.Generic; using System.ComponentModel; using System.Data;

using System.Drawing;

using System.Linq;

using System.Text;

using System.Threading.Tasks;

using System.Windows.Forms;

using System.Security.Cryptography;

namespace aesdecrypt

{

 public partial class aesdecrypt : Form

 {

 public aesdecrypt()

 {

 InitializeComponent();

 }

 private void decrypt(object sender, EventArgs e)

 {

 String key = “J8gLXc454o5tW2HEF7HahcXPufj9v8k8”;

 String IV = “fq20T0gMnXa6g0l4”;

 String encryptedtext = “CTsvjZ0jQghXYWbSRcPxpQ==”;

 byte[] encryptedBytes = Convert.FromBase64String(encryptedtext);

 AesCryptoServiceProvider aes = new AesCryptoServiceProvider();

 aes.BlockSize = 128;

 aes.KeySize = 256;

 aes.Key = System.Text.ASCIIEncoding.ASCII.GetBytes(key);

 aes.IV = System.Text.ASCIIEncoding.ASCII.GetBytes(IV);

 aes.Padding = PaddingMode.PKCS7;

 aes.Mode = CipherMode.CBC;

 ICryptoTransform crypto = aes.CreateDecryptor(aes.Key, aes.IV);

 byte[] decryptedbytes = crypto.TransformFinalBlock(encryptedBytes, 0, encryptedBytes.Length);

 String decryptedString = System.Text.ASCIIEncoding.ASCII.GetString(decryptedbytes);

 Console.WriteLine(“\n”);

 Console.WriteLine(“##########Decryptig Database password##########\n”);

 Console.WriteLine(“Decrypted Database password:” + decryptedString+”\n”);

 Console.WriteLine(“##########Done##########\n”);

 }

 }

}

//解密代码源自<https://resources.infosecinstitute.com/damn-vulnerable-thick-client-app-part-5/#article>

案例1-反编译修改代码逻辑让普通用户以管理员登录

dvta

1-Isadmin

0-Normaluser

改1为0即可判断为admin

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104639124-63071411.jpg)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104639654-178729771.jpg)

### 2. 信息泄露

明文敏感信息，敏感文件（如安装目录下的xxx.config）。

注册表：利用regshot比较客户端运行（如登录）前后注册表差别。

开发调试日志泄露（如dvta.exe >> log.txt）

process hacker查看客户端内存中的明文敏感数据（如账号密码/key）。

strings直接查看客户端字符串（如ip信息）。

查看源代码（如github,gitee等）

案例0-配置敏感信息泄露

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104640337-185140653.jpg)

案例1-内存泄露数据库账号密码

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104641053-86634704.jpg)

案例2-源代码含有硬编码ftp账号密码

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104641808-1344115235.jpg)

案例3-开发调试日志泄露

dvta

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104642490-566933343.jpg)

案例4-某系统登录后本地保存账号密码

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104643196-1110193214.jpg)

//本案例来源于[https://blog.csdn.net/weixin\_30685047/article/details/95916](https://blog.csdn.net/weixin_30685047/article/details/95916065)[065](https://blog.csdn.net/weixin_30685047/article/details/95916065)

### 3. 传输流量

wireshark/echo Mirage/burpsuite+nopeproxy/fillder/charles

ftp等协议明文传输的账号密码

SQL语句明文传输（如利用构造注入，越权等）

案例0-正方教务系统sql语句明文传输，返回明文数据

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104643906-438017818.jpg)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104644569-294447733.jpg)

//本案例来源于wooyu

案例1-某系统登录处数据包返回数据库帐号密码

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104645325-238625889.jpg)

### 4. 其他漏洞

#### 用户名枚举

案例0

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104646023-1455694132.jpg)

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104646723-650031357.jpg)

#### 暴力破解

如登录功能。

案例0

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104647308-1028946722.jpg)

#### 弱口令

可尝试admin 123456等。

#### 密码明文传输

#### SQL语句暴露

案例0

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104648098-1704429592.jpg)

案例1

![](https://img2022.cnblogs.com/blog/1049983/202211/1049983-20221108104648889-383046263.jpg)

#### SQL注入

如登录处，万能密码

xxx’ or ‘x’=’x

xxx’ or 1=1--

输入框处，构造闭合报错，如’、’)、%’)、order by 100--等。

利用显示位或报错注出数...