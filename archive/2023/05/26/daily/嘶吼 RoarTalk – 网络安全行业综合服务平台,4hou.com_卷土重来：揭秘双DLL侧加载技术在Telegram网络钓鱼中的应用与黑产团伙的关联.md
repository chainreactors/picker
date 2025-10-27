---
title: 卷土重来：揭秘双DLL侧加载技术在Telegram网络钓鱼中的应用与黑产团伙的关联
url: https://www.4hou.com/posts/JKN9
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-26
fetch_date: 2025-10-04T11:36:51.534122
---

# 卷土重来：揭秘双DLL侧加载技术在Telegram网络钓鱼中的应用与黑产团伙的关联

卷土重来：揭秘双DLL侧加载技术在Telegram网络钓鱼中的应用与黑产团伙的关联 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 卷土重来：揭秘双DLL侧加载技术在Telegram网络钓鱼中的应用与黑产团伙的关联

矢安科技
[行业](https://www.4hou.com/category/industry)
2023-05-25 13:48:27

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)135918

收藏

导语：揭露伪装成国外社交软件“Telegram”官网的钓鱼活动~

**事件概述**

近日，矢安知深攻防实验室在日常威胁狩猎中监测到一个伪装成国外社交软件“Telegram”官网的钓鱼活动。该钓鱼网站可通过访问者的浏览器标识下发不同的恶意后门程序。通过相关溯源分析我们发现本次攻击活动与黑灰产团伙“金眼狗”存在极大关联。

本次攻击活动流程如下图所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922109103073.png "1684921492618832.png")

**组织背景**

金眼狗组织是一个主要针对东南亚地区博彩推广相关人员的黑灰产团伙。该组织最早于2019年由奇安信安全团队披露，且在此后的几年时间里多次作案，作案目标主要以经济利益为驱动力，黑产业务涉及窃密、挖矿、DDoS等多个领域。

**样本分析**

截止本文发稿，伪装成Telegram官网的钓鱼页面仍处于正常访问状态，该页面可向目标用户提供不同版本的中文版Telegram安装程序。这也侧面反映出本次攻击活动主要针对使用中文的用户群体。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922111140757.png "1684921674149564.png")

下载后的Windows安装包不带数字证书签名，且安装完成后会在用户“%AppData%”目录下创建一个以“TG-”开头的文件目录：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922112113405.png "1684921692461004.png")

随后在桌面创建一个虚假的TG快捷方式，诱导用户点击，通过该方式可有效阻止沙箱等非交互系统的检测操作：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922113156431.png "1684921858973799.png")

Telegram.lnk命令行如下所示：

|  |
| --- |
| 混淆：%AppData%\TG-B51AfF8C018c\appU.exe appU.dll,OpenURL appr.lnk  正常：%AppData%\TG-B51AfF8C018c\RUNDLL.EXE URL.DLL,OpenURL appr.lnk |

appr.lnk文件使用相同套路进行混淆：

|  |
| --- |
| 混淆：%AppData%\TG-B51AfF8C018c\appR.exe   /s   /n   /u   /i:appR.dat   appR.dll  正常：%AppData%\TG-B51AfF8C018c\regsvr32.exe   /s  /n  /u  /i:appR.dat  scrobj.dll |

appR.dat是一个包含js混淆脚本的xml文件（通过[jsjiami.com](http://www.jsjiami.com/) 进行混淆）

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922114159227.png "1684921865818637.png")

其主要功能是拷贝TG目录下的“KB1”和“KB2”文件到系统启动目录，实现持久化：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922115152204.png "1684921872192943.png")

每次系统启动时，两个lnk文件都会分别执行%Public%\reloc路径下的利用程序，在该利用链中，金眼狗使用了“双DLL侧加载”技术执行后门程序。相对于传统的DLL侧加载技术，该方式多了一个中间环节，用于延长进程利用链与载荷执行的时间（套娃）。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922117120747.png "1684921877784676.png")

SILan.exe与autorun.exe均属于正常程序。

SILan.exe执行后会以子进程方式调用autorun.exe，然后再加载同目录下的language.dll，该dll文件作为Loader加载templateG.txt文件，在内存中解密出Shellcode，最终反射加载ServerDll.dll后门执行。ServerDll.dll是一个包含多个后门功能的远程控制（RAT），恶意代码由 “Fuck” 导出函数执行。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922118982306.png "1684921884918743.png")

后门执行时首先获取计算机名，然后创建注册表键值用于存储配置信息。如果获取计算机名失败则使用“UnKnow”作为路径，随后写入当前系统时间，用于标识后门安装日期。最后通过++运算，创建互斥体保证单实例运行。

|  |
| --- |
| 注册表：HKEY\_CURRENT\_USER\SOFTWARE\[ComputerName or UnKnow] |

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922119598352.png "1684921896119430.png")

除了“Time”注册表键外还有如下键值：

|  |  |
| --- | --- |
| 键名 | 描述 |
| Time | 标识后门安装日期 |
| CopyC | 更新C2地址 |
| ARPD | isARDll、PluginMe、getDllName，以‘|’分隔 |
| ZU | 获取Extensions（以太坊钱包）插件信息 |
| Remark | Hostname |

读取“CopyC”注册表数据，如果成功则使用Base64和Xor 0x5解密C2地址，否则使用硬编码C2地址：“v2.pic447.com:45500”

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922120125493.png "1684921902155896.png")

新建线程执行其余后门操作，该后门程序主要包含如下恶意功能：

|  |  |
| --- | --- |
| 指令 | 功能描述 |
| 0x0 | 关机、重启 |
| 0x1 | 设置全局标识 |
| 0x2 | 设置注册表键值 “Remark” |
| 0x3 | 设置注册表键值 “ZU” |
| 0x4 | 清除事件日志 |
| 0x5 | 获取Extensions（以太坊钱包）插件信息 |
| 0x6 | 在“WinSta0\\Default”桌面下创建指定进程 |
| 0x8 | 使用ShellExecute执行命令（窗口显示） |
| 0x9 | 使用ShellExecute执行命令（窗口隐藏） |
| 0x70 | 获取剪贴板数据 |
| 0x71 | 设置剪贴板数据 |
| 0x7D | 使用ShellExecute执行CMD命令（窗口隐藏） |
| 0x7E | 创建文件数据并执行 |
| 0x80 | 设置注册表键值 “CopyC” |
| 0x23,0x25,0x65-0x6F,0x7F | 检查getDllName、isCSDll、PluginMe、ARPD、isARDll |

**组织关联**

通过多个维度的关联分析，我们以较高可信度将本次攻击活动归纳为东南亚黑灰产团伙金眼狗组织。

例如，在初始载荷投递阶段该组织已经不是第一次利用Telegram网站进行钓鱼活动。此外本次攻击活动中的xml文件与此前金眼狗组织在历史攻击活动中使用的文件内容高度重合，区别是早期样本使用VBScript作为脚本解释语言，且脚本代码未做加密混淆处理。有意思的是XML标识符与描述信息中的“Bandit”内容，可以说是相当直白了。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922121137102.png "1684921908127480.png")

最终阶段执行的后门载荷“ServerDll.dll”，在该组织历史攻击事件中也曾出现过。早期版本使用的是.NET平台。并且两者都有从注册表中存储配置信息，读取C2的操作。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230524/1684922122145301.png "1684921912703208.png")

**IOC**

103.116.15.2

v2.pic447[.]com

https://www.telegramos[.]org/

更多IOC也可联系我们获得~

**防护建议**

目前，矢安科技已全面支持对本类攻击活动的发现与检测能力，客户可通过后台服务对相关资产进行薄弱点检测与风险排查。

个人用户也可根据如下项目进行风险自查：

|  |
| --- |
| 1、检查系统开始启动文件夹中是否存在可疑启动文件  2、查看用户“%AppData%”目录下是否存在以“TG-”开头的文件目录  3、查看“%Public%”目录下是否存在可疑文件夹，以及程序利用链  4、查看设备网络流量，排查可疑C2或IP地址通讯（v2.pic447[.]com:45500）  5、排查是否存在如下注册表项与相关键值内容：HKEY\_CURRENT\_USER\SOFTWARE\[ComputerName or UnKnow] |

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?T3ehx3cq)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/portraits/de620f130a9785bd8fdb5a7d443befa3.jpg)

# [矢安科技](https://www.4hou.com/member/PyV4)

致力于成为新一代智能安全的领跑者。

#### 最新文章

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
  2025-09-29 17:48:04
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
  2025-09-29 14:55:37
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
  2025-09-29 14:23:50
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
  2025-09-28 17:20:40

[查看更多](https://www.4hou.com/member/PyV4)

# 相关热文

* [Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)

  CACTER
* [【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)

  网络伍豪
* [蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)

  梆梆安全
* [聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)

  企业资讯
* [2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)

  企业资讯
* [特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

  RC2反窃密实验室

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www....