---
title: 【行业动态】供应链投毒预警 | 恶意NPM包内嵌木马程序开展投毒攻击
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247530401&idx=2&sn=abe290f70d25927968382457bcd759c0&chksm=c144051cf6338c0ab5e6384049d50fe96fc9d1cf5e4f23e540e84642a3a8cb96c391f09db869&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-12-04
fetch_date: 2025-10-06T19:39:17.831810
---

# 【行业动态】供应链投毒预警 | 恶意NPM包内嵌木马程序开展投毒攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqreAJ9dIASyTn5ia3iacnJHNEicTNneiccXNSAW8vSaHDvWBibbgSR8JeE4aPEKAPBll4E2KGZNvFG8oxA/0?wx_fmt=jpeg)

# 【行业动态】供应链投毒预警 | 恶意NPM包内嵌木马程序开展投毒攻击

悬镜安全情报中心

数世咨询

**概述**

近两周（2024.11.10~11.19），悬镜供应链安全情报中心在NPM官方仓库（https://npmjs.com）中连续捕获多起针对Windows NPM开发者的恶意木马投毒攻击事件。来自多个NPM发布者共投放了9个恶意组件包，涉及34个不同版本，这些恶意NPM包代码结构和恶意行为极度相似，属于同一个攻击者所为。恶意包的主要行为都是将内嵌在源代码中的Windows EXE恶意木马程序，解码释放到系统本地并伪造成cmd.exe执行。截至目前，根据NPM官方接口统计，这些恶意NPM包总下载量超过3200次，并且仍托管在NPM官方仓库，NPM开发者可正常下载安装，存在较大安全隐患。悬镜供应链安全情报中心已于第一时间向NPM官方通报该系列恶意组件包。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyXqhpmNcIqrbA257zNabdeeTJR8rzV1jX7VqGehrIs2xFXjf6lzonzQ/640?wx_fmt=png&from=appmsg)

恶意包统计

**投毒分析**

以fixsolara组件包为例，投毒者（kyeeluur@sillyfa.de）连续发布了10个不同版本恶意包，截至目前，该恶意包在NPM官方下载量为1599次。在最新版本（1.0.13）中，其核心恶意代码被混淆保护，以对抗静态扫描分析。当NPM开发者引用加载该恶意组件包时，被混淆的恶意代码将释放出内嵌的Windows木马程序，并植入到受害者系统中执行。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyIy5ASictG5r5ELfk1lZPshXibQx93ops3UzJkdDfTiapnz7MVNulMuP9g/640?wx_fmt=png&from=appmsg)

fixsolara恶意包NPM仓库主页

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyrnEt9H4HXAhTRDb2oouNnodOe6wBfgLbibUxE82zR9590hPlyGndPtg/640?wx_fmt=png&from=appmsg)

fixsolara恶意包总下载量

**Part.1**

**代码混淆保护**

从恶意包 fixsolara 的模块描述文件package.json 可知，恶意包通过postinstall指令在组件安装过程中执行包含恶意代码的js文件index.js。

```
{   "name": "fixsolara",   "version": "1.1.3",   "description": "Fixes any problems with solara.",   "main": "index.js",   "bin": {     "fixsolara": "index.js"   },   "scripts": {     "postinstall": "node index.js"   },   "dependencies": {     "fs-extra": "^10.0.0",     "node-fetch": "^2.6.7",     "sudo-prompt": "^9.2.1"   } }
```

恶意包描述文件

恶意文件index.js 的代码被混淆保护，原始代码如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyghKiajJR7RzES5pnQDEzdfBja7R2s1ty0QSItSGTqruo0Kr1hkSPicuQ/640?wx_fmt=png&from=appmsg)

index.js混淆代码

**Part.2**

**恶意木马释放执行**

对混淆代码进行初步还原并精简后，实际恶意代码如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyicMDOpb8zFwgs4TsaiaXn9Iic5ce5DXcTD3iczt66VxDh7iaHxJ6nNuicWsA/640?wx_fmt=png&from=appmsg)

index.js混淆代码还原

其中绿色方框部分为内嵌在代码文件中的Windows恶意EXE程序的base64编码数据，黄色方框部分负责将编码的Windows恶意EXE程序释放到系统临时目录下，并重命名保存为cmd.exe。红色方框部分负责直接执行该恶意EXE程序。

Windows恶意EXE程序的base64编码数据如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyTYvM0mF6aJUxcd9BLWzSruhdQRYohgZ9SW3z1MHCEdh9chr6pQncQw/640?wx_fmt=png&from=appmsg)

恶意EXE程序base64编码数据

如下图所示，通过API动态监控可清晰发现fixsolara 组件在安装过程中产生的恶意行为日志，包括释放EXE程序文件，并最终调用sudo-prompt模块执行EXE程序。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvy7DL8JOzSoC74icFm3HAlqJw5SiaYAibEsIaPbeAhV5aChvibXjYYicDeczw/640?wx_fmt=png&from=appmsg)

fixsolara 组件恶意行为日志

从文件属性可知，释放出的恶意EXE程序（cmd.exe）实际文件名为XClient.exe。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvybpFeddB0QrUB2AL2iaUZM3MWQgmx4nkYe3UBqhlk6wxHdKVQIMZGiaUA/640?wx_fmt=png&from=appmsg)

cmd.exe恶意程序

在VirusTotal上进行检测，该cmd.exe被多款杀毒引擎检出为trojan.msil/xworm恶意木马（如下所示）。

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyJCuHFmaoOOelWG1WHxPekjc2gqrmkicn2CNnHR490Tn0UrpPiaMsqdJw/640?wx_fmt=png&from=appmsg)

VirusTotal检测结果

**Part.3**

**IoC数据**

此次该系列投毒组件包涉及的恶意IoC数据如下表所示：

![](https://mmbiz.qpic.cn/mmbiz_png/KOWJ2ib68IGiajeiaWibXdF3WGt3luBvXRvyIOeVrMpHkpUXB7NRZrJRR7piaqZeJ8UOkO2t00vAHNBcslbpMIYXib5w/640?wx_fmt=png&from=appmsg)

**排查方式**

开发者可在NodeJS项目根目录下通过命令 npm list {package\_name}或者npm list{package\_name}-g 快速排查是否误安装该恶意NPM组件包，若命令运行结果显示已经安装该恶意组件，则可通过命令 npm remove{package\_name} 或npm remove{package\_name}-g进行卸载，同时还需关闭系统网络并排查系统是否存在异常进程。

此外，开发者也可使用OpenSCA-cli，将受影响的组件包按如下示例保存为db.json文件，直接执行扫描命令（opensca-cli -db db.json -path ${project\_path}），即可快速获知您的项目是否受到投毒包影响。

```
 [   {     "product": "fixsolara",     "version": "[1.0.4, 1.0.5, 1.0.6, 1.0.7, 1.0.8, 1.0.9, 1.0.10, 1.0.11, 1.0.12, 1.0.13]",     "language": "javascript",     "id": "XMIRROR-MAL45-C39C7090",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-19"   },   {     "product": "fixexec",     "version": "[1.0.0, 1.1.0, 1.0.7, 1.0.8, 1.0.9]",     "language": "javascript",     "id": "XMIRROR-MAL45-90973A51",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-14"   },   {     "product": "spoofdownload",     "version": "[1.7.6]",     "language": "javascript",     "id": "XMIRROR-MAL45-49F0FEB4",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-14"   },   {     "product": "solarafixer",     "version": "[1.8.6, 1.7.6]",     "language": "javascript",     "id": "XMIRROR-MAL45-3306789E",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-13"   },   {     "product": "eacfix",     "version": "[1.7.6]",     "language": "javascript",     "id": "XMIRROR-MAL45-DC9A9909",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-13"   },   {     "product": "nlhybridfixer",     "version": "[1.0.4, 1.0.0, 1.0.9, 1.1.0, 1.1.1, 1.8.6, 1.4.6]",     "language": "javascript",     "id": "XMIRROR-MAL45-305A21C0",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-13"   },   {     "product": "spooferdownload",     "version": "[1.8.6, 1.7.6]",     "language": "javascript",     "id": "XMIRROR-MAL45-69628325",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-13"   },   {     "product": "solarafix",     "version": "[1.0.0, 1.0.1, 1.0.2, 1.0.3, 1.0.4]",     "language": "javascript",     "id": "XMIRROR-MAL45-28CDF944",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-10"   },   {     "product": "rootkitfix",     "version": "[1.0.4]",     "language": "javascript",     "id": "XMIRROR-MAL45-D358C09A",     "description": "恶意NPM组件包开展Windows木马后门投毒",     "release_date": "2024-11-10"   } ]
```

悬镜供应链安全情报中心是国内首个数字供应链安全情报研究中心。依托悬镜安全团队强大的供应链SBOM管理与监测能力和AI安全大数据云端分析能力，悬镜云脉XSBOM数字供应链安全情报预警服务通过对全球数字供应链投毒情报、漏洞情报、停服断供情报等进行实时动态监测与溯源分析，可为用户智能精准预警“与我有关”的数字供应链安全情报，提供情报查询、情报订阅、可视化关联分析等企业级服务。

— 【 THE END 】—

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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