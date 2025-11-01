---
title: 【病毒分析】MEDUSA LOCKER勒索windows版本分析
url: https://forum.butian.net/share/4601
source: 奇安信攻防社区
date: 2025-10-31
fetch_date: 2025-11-01T03:08:13.933387
---

# 【病毒分析】MEDUSA LOCKER勒索windows版本分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 【病毒分析】MEDUSA LOCKER勒索windows版本分析

1.背景
1.1 家族介绍
MEDUSA LOCKER 家族于 2019 年 9 月出现，MEDUSA LOCKER 家族通常通过有漏洞的远程桌面协议（RDP）配置获取受害者设备访问权限，攻击者还经常使用电子邮件钓鱼和垃圾邮件活...

\*\*1.背景\*\*
========
1.1 家族介绍
--------
MEDUSA LOCKER 家族于 2019 年 9 月出现，MEDUSA LOCKER 家族通常通过有漏洞的远程桌面协议（RDP）配置获取受害者设备访问权限，攻击者还经常使用电子邮件钓鱼和垃圾邮件活动——直接将勒索软件附加到电子邮件中——作为初始入侵渠道。
MEDUSA LOCKER 对受害者的数据进行加密，并在包含加密文件的每个文件夹中留下带有勒索信。勒索信指示受害者向特定的比特币钱包地址提供勒索软件付款。MEDUSA LOCKER 似乎根据观察到的赎金支付拆分作为勒索软件即服务 （RaaS） 模型运行。典型的 RaaS 模型涉及勒索软件开发人员和在受害者系统上部署勒索软件的各种附属公司。MEDUSA LOCKER 家族付款似乎始终在附属公司之间分配，附属公司收到 55% 到 60% 的赎金;以及接收剩余部分的开发人员。
1.2 平台介绍
--------
MEDUSA LOCKER家族提供两个暗网地址：一个是博客，另一个是聊天室。博客中留有Tox联系方式，并会公开受害者的信息，点击特定受害者后，可以查看其详细的泄露数据和赎金要求；聊天室则要求输入ID和联系邮箱，且支持上传一个被加密的文件进行测试。提交后，系统将为受害者生成一个聊天室，供其与MEDUSA LOCKER家族进行私密交流，其他人无法查看该对话内容。
### 1.2.1 博客页
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-556406dcab68de9df1fd5477229f92f84b11d084.png)
博客首页
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-a6e806aa2db4cf70da6f2fb236918c7954ef3c2f.png)
数据详情页
### 1.2.2 聊天室页
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-ff7ed9fc97b852c714689d0d61363c40598ac74a.png)
加载进入聊天室
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-39abd5ebfe77932216a03157a2695182f739dd34.png)
成功创建聊天室
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-46c384489ef0d042767d6f8b15beae98452ab760.png)
聊天室页面
2.恶意文件基础信息
==========
2.1 恶意文件基本信息
------------
| 文件名 | bh538.exe |
|---|---|
| 编译器 | Microsoft Visual C/C++(19.36.34810)\[LTCG/C++\] |
| 大小 | 1.72 MB |
| 操作系统 | Windows(Vista)\[AMD64, 64位, Console\] |
| 模式 | 64 位 |
| 类型 | PE64 |
| 字节序 | LE |
| MD5 | 7d64ffeb603fbe96a4b47982e2a1dd3f |
| SHA1 | f983c9e9216ad026edad6accb8962d90f8230019 |
| SHA256 | ca4dfe28e1f18a1b8e0bcd825abe129ab46031ba4faed8777bc95da67371d83d |
2.2 勒索信
-------
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8af9782d080551fc24d13d0727b45100468860b5.png)
3.加密后文件分析
=========
3.1威胁分析
-------
| \*\*病毒家族\*\* | MEDUSA LOCKER |
|---|---|
| \*\*首次出现时间/捕获分析时间\*\* | 2025/09/9 \| 2025/09/11 |
| \*\*威胁类型\*\* | 勒索软件，加密病毒 |
| \*\*加密文件扩展名\*\* | .blackheart588 |
| \*\*勒索信文件名\*\* | read\\_to\\_decrypt\\_files.html |
| \*\*有无免费解密器？\*\* | 无 |
| \*\*联系邮箱\*\* | [ecovery1@salamati.vip](mailto:recovery1@salamati.vip) <recovery1@amniyat.xyz> |
| \*\*感染症状\*\* | 无法打开存储在计算机上的文件，以前功能的文件现在具有不同的扩展名（例如，solar.docx.blackheart588）。桌面上会显示一条勒索要求消息。网络犯罪分子要求支付赎金（通常以比特币）来解锁您的文件。 |
| \*\*感染方式\*\* | 受感染的电子邮件附件（宏）、恶意广告、漏洞利用、恶意链接 |
| \*\*受灾影响\*\* | 文件都经过加密，如果不支付赎金就无法打开。其他密码窃取木马和恶意软件感染可以与勒索软件感染一起安装。 |
3.2 加密的测试文件
-----------
### 文件名
sierting.txt
### 具体内容：
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-9e53e5a3e7cac1ed36e6089dbd74e1fc8f163e55.png)
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2db21c74dd31194c053c26bc632f349e59cb0d15.png)
### 加密文件名特征：
加密文件名 = 原始文件名+blackheart588 ，例如：sierting.txt.blackheart588
### 加密文件数据特征：
对于文件的加密根据如下配置，条状加密，其中每一条都为1136023字节，当加密字节累计超过3853566字节后就不再加密。
"bytesCryptAndSkip": 1136023,
"bytesForEncrypt": 3853566,
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2e5c3b1874e6389429c192dca286c4131f233395.png)
### 加密算法：
#### chacha密钥生成：
##### KEY：
使用如下函数生成随机的key
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-d00e2f042cbc2df8e5a2593c28a2af0418d55c64.png)
#### RSA密钥生成：
##### 公私钥对：
生成公私钥对
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-073c9f775343a313860d3536900d667220f8d589.png)
### 程序执行流程：
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-7d1bdf9a7da17caa457999461d0290ac64e97435.png)
4逆向分析
=====
4.1加密器逆向分析
----------
### 4.1.1main函数
创建多个线程
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-6d53565400fc33c4d23421ef6317c4b765b92197.png)
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-f3b337c02b6847cddbbb56f39514835e0aa070cc.png)
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b714c5f6b5205a0dd09d63cec8d035ef16bc67a4.png)
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-8167fe33e26d545a6900fdb483a64e094b97394c.png)
执行如下命令
"rem Kill \\"SQL\\"",
"taskkill -f -im sqlbrowser.exe",
"taskkill -f -im sql writer.exe",
"taskkill -f -im sqlserv.exe",
"taskkill -f -im msmdsrv.exe",
"taskkill -f -im MsDtsSrvr.exe",
"taskkill -f -im sqlceip.exe",
"taskkill -f -im fdlauncher.exe",
"taskkill -f -im Ssms.exe",
"taskkill -f -im SQLAGENT.EXE",
"taskkill -f -im fdhost.exe",
"taskkill -f -im ReportingServicesService.exe",
"taskkill -f -im msftesql.exe",
"taskkill -f -im pg\\_ctl.exe",
"taskkill -f -impostgres.exe",
"net stop MSSQLServerADHelper100",
"net stop MSSQL$ISARS",
"net stop MSSQL$MSFW",
"net stop SQLAgent$ISARS",
"net stop SQLAgent$MSFW",
"net stop SQLBrowser",
"net stop REportServer$ISARS",
"net stop SQLWriter",
"vssadmin.exe Delete Shadows /All /Quiet",
"wbadmin delete backup -keepVersion:0 -quiet",
"wbadmin DELETE SYSTEMSTATEBACKUP",
"wbadmin DELETE SYSTEMSTABACKUP -deleteOldest",
"wmic.exe SHADOWCOPY /nointeractive",
"bcdedit.exe /set {default} recoverynabled No",
"bcdedit.exe /set {default} bootstatuspolicy ignoreallfailures"
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2ad3bace310b562b3bb11e202c7cf15c6fb8abe7.png)
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-908124b1996ad25340cd54fecaa3076242941a54.png)
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-0ff4283b1a05df80c4886e020640a442b022d5bc.png)
![20.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-b8fd204812bee7cdf4b1fab9303ecf13fc4de87e.png)
检测输入的参数，如果是-h提供帮助信息
![21.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-0532c03c07917a7e549eb37ce42e2aaf7f854884.png)
### 4.1.2ui\\_status\\_thread函数
显示加密进度窗口
![22.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-54c98222fe2646682ccd64da80c5cfdd941ce30f.png)
![23.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-5215469ebf391dc587f6a066e5cd7f67166efa66.png)
![24.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-9ed0a179805f6b9bd75425051f09e3e96b77ea2c.png)
![25.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-71812a09fc885d9e06d2d5f1e39bc300f2e5a83e.png)
### 4.1.3add\\_to\\_startup函数
权限维持函数，添加自启动
![26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-523adf19d01c1326fa68e668a2468d35b9d4abc9.png)
![27.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-2d23bb4f58f1389297dee4be9cb6fcd1b22ef1de.png)
### 4.1.4clear\\_recycle\\_bin函数
清空回收站
![28.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-3a62eeb75883294e74b83154f7f6f6977b6a7cd2.png)
### 4.1.5set\\_background\\_image函数
更换壁纸，由于该勒索的配置中启用该功能，因为不会更换壁纸
![29.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-9e70f7318cbb74f965c86fbef321c57c3c310979.png)
### 4.1.6file\\_scan\\_thread函数
给扫描到的每个驱动器都分配线程执行目录扫描和加密任务
![30.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/09/attach-36c484991a4ff8b0783f287b5fdf2f8a1b886ecf.png)
### 4.1.7scan\\_directory\\_and\\_encrypt函数
判断路径是否位于排除目录中，排除的目录路径如下：
"C:\\\\perflogs",
"C:\\\\Intel",
"C:\\\\HP",
"C:\\\\AMD",
"C...