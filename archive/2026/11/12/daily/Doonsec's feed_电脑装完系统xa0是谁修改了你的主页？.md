---
title: 电脑装完系统xa0是谁修改了你的主页？
url: https://mp.weixin.qq.com/s/tamLmr2ECTYLMfj77HUmqg
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T08:57:54.143300
---

# 电脑装完系统xa0是谁修改了你的主页？

# 电脑装完系统 是谁修改了你的主页？

原创

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/u1Oy5xQ01SqOibVrO9m8ibSxWyW6dTia06ytM5rguTkovbGJSO6CdoribgX1p2OEiaZdkiaF5v8uwic3ADF4Nze6jrfJejgeeK5buKcFUZfyMjnbfM/640?wx_fmt=gif&from=appmsg)

**0****1**

**概述**

近日，火绒安全实验室接到用户反馈：电脑刚装好系统，浏览器主页就被莫名改成陌生导航站，同时被安装了一款名为“We2新标签页”的推广扩展。经溯源发现，篡改源头并非用户自行安装的任何软件，而是装机环节所用的“系统总裁”SC封装工具——该工具面向装机商与系统维护人员，用于批量封装Windows系统。也就是说，装机商用它封装出的镜像中，就内置了浏览器配置篡改逻辑：系统部署完成进入桌面阶段后，该模块自动执行，对浏览器的首页、新标签页进行静默篡改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SplmbibFdLHlDFXYY06QafWDVpVmwia6lxm3lBXlKYYoLEKlDAKFwzjgvJuwdqkHN49yC0eXl8KlSqC4dXRLf5PXNt8VviaD4NRBM/640?wx_fmt=png&from=appmsg)

**劫持主页安装扩展**

经火绒工程师分析后发现，劫持行为与封装界面的任何用户配置无关：即便不勾选任何附加组件，普通封装方式仍会释放劫持相关组件，且不提供任何关闭或卸载选项。其波及范围也不止一款浏览器——模块可探测并篡改Chrome、Edge、360、QQ、搜狗、夸克等10款主流浏览器，并针对浏览器自带的主页防篡改校验机制重新计算校验值，使篡改悄然生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqRFLS0Q0icZYBOdXGMuHdSSe119BDtHLX8lofIKOwQbP9kgw2gG67wPtfJIfoXA3I2yvS3PbAjExxXY5P31g9K1T0Vicb29gIkY/640?wx_fmt=png&from=appmsg)

**工具页面**

值得注意的是，"防流氓/大客户封装方式"的封装产物无浏览器篡改行为。系统总裁官网在赞助页面中宣称"免费共享不捆绑不流氓"，并提供三种赞助方式，其中方式二为"把电脑主页设置总裁的链接"。然而封装工具在普通封装情况下，完成主页篡改行为，且未提供任何关闭或卸载选项。官方将"设置主页"列为赞助行为，却在工具中将其变为默认静默执行。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01So3MKtvVPKX3u1CZA1hHGWME0zcLeuMkugkEgqf0fqYjjrypRF0nL49OibAMt5gJDpX00ef4zJPE85jqWTw4tpe0ErrY1Qj3pic4/640?wx_fmt=png&from=appmsg)

**工具官网**

同时火绒工程师还发现，该问题并非只存在于官网渠道：从PC下载网、当快软件园等第三方下载站获取该工具的旧版本（v3.0.0.176）进行验证，其版本更新后，主程序与本报告分析的官网样本完全一致。这就意味着，无论用户从官网还是第三方下载站获取该工具，更新后都会变为携带劫持组件的同一版本，即更换下载渠道，并不能避开这一问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqosrBJubfxTlSoXmljuSt4wy2WQIe3o79cMEJTfQY9VFlEOdGIia6We28pfL0hwkdjqvVhvclFeK5ic0lNRtHqDEiciawXHJRtATA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpZhibgTklECicXY8icG2yALHJfxQtR5ZUEhTQn3XZoI16rS2PHHguMqhaicrDT6ib308BqoNQT9Q2gYNY8R4CutUsT6gPzfrvJ7MOU/640?wx_fmt=png&from=appmsg)

事实上，这一问题早在2021年就已有公开反馈（https://www.52pojie.cn/thread-1455126-1-1.html）。多年来，该工具版本几经迭代，而此类劫持行为仍延续至今——这表明它并非某次更新引入的偶发问题，而是长期存在、从未收敛的行为；叠加该工具在装机环节被批量使用的特性，其累积影响的用户规模不容忽视。

目前，火绒安全产品已实现对该行为的拦截与查杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SocuHf1ZkgCYj2CxdFNpVvj9Y7MPdTCgVVwEKTXsHR6wv9xzIDViaydRKKxcBHQTCqONwUIjHuDxUCBicqvITgYvIjfVictLoroV8/640?wx_fmt=png&from=appmsg)

**查杀图**

**0****2**

**执行链还原**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SoubtzYs1OYPichuicnBUh6Pq1U1c3Ue6y55l0bUvGw22Xe9WmfiaOhv5clP0vRiacyyAyib3tFDQC8DXRfnfs0FX1yq2MMWM1c78c0/640?wx_fmt=png&from=appmsg)

**执行流程图**

**0****3**

**样本分析**

系统总裁封装工具解压为——

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SptQf0cic1oLfjdNcAiabzeaStFic58tOvts4RdXibSnaBloL9lHERcnTYKQUhK6LibOicTRR1LBMF0Oic4gcOQawiaib74gykyyiciaW9aibU/640?wx_fmt=png&from=appmsg)

**SC解压目录**

Scpt会根据配置进行封装。

系统封装流程分四段。先是准备阶段，检测运行环境、写初始配置；

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sp0lAaYZBaT1AgeC3yX8nN77BJCdOxZmTkv7HLGC4tibpY1QaibG2emu4TD5XibuLjR6jQoP6YbQ3HIPZQJV7Nr2gu5J6vCXmwCP0/640?wx_fmt=png&from=appmsg)

**环境检测分支、Scdata.sc 写入点**

然后是点击“开始封装”之后的前置校验，检查授权、输出路径和磁盘空间。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqSypnTxl2CWcrH7RGHPdicZia4jPe3bXia1EJWjHq3eW2krAia8X7Bllp626vTMIU5rSxLbria7GuneTbNtnnUhZ0icFmibpicmUWJKfM/640?wx_fmt=png&from=appmsg)

**前置校验**

通过后进入系统准备，使用sysprep进行封装。

最后生成部署文件，封装完成后释放的主要文件。

|  |  |
| --- | --- |
| **落地路径** | **来源资源** |
| %windir%\System32\ScTasks.exe | FUNN/FUNNX64 或 FUNNKR/FUNNKRX64 |
| %windir%\System32\ScDeploy.exe | FUNM/FUNM X64或FUNMKR/FUNMKRX64 |
| %windir%\ScData\Scdata.sc | 配置数据文件 |

ScDeploy.exe在用户尚未登录的部署环境执行，在确认同目录下的ScTasks.exe存在后，将"路径+/DeskTop"写入启动项。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoJ5sibjIR4WWgGicAB8vhQo0H8bgxAjty9YaV9VlKceJ3oAUFI3cDFw7y1I3KoR8j5ibtGuD02cGl6mzpJFhcVS2dpGhvtrE3ibr8/640?wx_fmt=png&from=appmsg)

**写启动项**

封装完成后会重启系统，重启后会执行启动项，Sctasks.exe /Desktop三种模式释放的ScDeploy.exe与ScTasks.exe来自不同资源，逐个资源比对结果如下——

普通模式的FUNN包含三个防流氓/大客户模式没有的资源：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqS2aqLr3leMNJz6chBygoCkojLELU0gTiaLQnkVwEPcQIk9Msad5UAZ9KSAR6DibcLicN94VbRFmvoYL99xd9SRmRqojXnIkztTA/640?wx_fmt=png&from=appmsg)

**不同模式释放的资源的区别**

ScTasks.exe在桌面阶段释放三个文件Crun.exe、broscfg.dll和bener.exe，探测四款Chrome、360Chrome、Quark、Sogou浏览器是否存在，拼出 "Del E G J K S" 形式的命令行。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sp7dz1RYL8pFzP4hkhVRK59kwuVf7iauW5KXxRyHMCrrOiaphmwsjDOvs8CCia2gwpZKFlBn3iaPiaCNH6wGFCrDEDPTWWzYibyYKDu0/640?wx_fmt=png&from=appmsg)

**释放资源**

Crun.exe将broscfg.dll加载，调用broscfg.dll的导出函数rtool

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqlbHE33Q3iafaLLlAABO17HtqzTia9FyGr11aQialRkGnlLT4W45VZYhatbmZgD32ARgvQBkIKVB21QIRA89T3MygbqwnDHFSAIQ/640?wx_fmt=png&from=appmsg)

**加载broscfg.dll**

broscfg.dll按品牌词分派，品牌字符串共 15 个：Google、Edge、Quark、Theworld、2345、Maxthon、Qq、Qqsafe、Jisu、Liebao、360、Sogou、Opera、Iqiyi、360closetk； 将内嵌的11个资源覆盖profile

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpQJeia7jy9ibsp5a71C3EIn9omqyWqicrLicPqIh3GiaUuGr1nqNJ3jjviaKaokKQYicKQHgjpsKkJgMXJwpKH5bz0Hcj16kkPDlPHZg/640?wx_fmt=png&from=appmsg)

**覆盖profile并修改Preferences**

以 Chrome 为例，模板包含 Preferences、Secure Preferences、Web Data、First Run、Last Browser、Last Version等文件。解包后直接写入%LOCALAPPDATA%\google\Chrome\User Data\Default目录。模板中的Secure Preferences预先构造了篡改后的结构：

```
{
  "homepage": "http://hao.jiaxixi.com/",
  "homepage_is_newtabpage": false,
  "session": {
    "restore_on_startup": 4,
    "startup_urls": ["http://hao.jiaxixi.com/"]
  },
  "protection": {
    "macs": {
      "homepage": "D191357C…8F4145AE",
      "session": {
        "restore_on_startup": "E616250A…44D79DDA",
        "startup_urls": "E909C9E0…4708BB647"
      }
    },
    "super_mac": "F7AA229C…40F5"
  }
}
```

每条MAC为32字节。Chrome、Edge、夸克模板的MAC不能直接沿用，需要重算，重算过程为：先取机器指纹，包括本机SID字符串和系统盘卷序列号；再把指纹与字段路径 + 字段值组成消息，用HMAC-SHA256计算，密钥是硬编码的16个32位常量，经ipad/opad处理；摘要32字节转64位十六进制，逐条写回protection.macs.字段，最后重算super\_mac。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sre9o9V8s0mGyJygsaoF1Jicw5siatexBXkBVBBzWIu4X6EXygyubWDLbDIXzKOFIjfNcGzQXFYyrovm7A0iaIh5A4dgPeXU4pUia8/640?wx_fmt=png&from=appmsg)

**计算MAC**

其资源节内嵌11个7z压缩包，每个对应一款浏览器的整套配置模板（Preferences、Secure Preferences、Bookmarks、Web Data、Top Sites等），解包后整包覆盖用户配置：

|  |  |  |
| --- | --- | --- |
| ****浏览器**** | ****覆盖目标**** | ****改写指向**** |
| Google Chrome | Default\Preferences、Secure Preferences、Web Data、First Run、Last Browser、Last Version | 主页hao.jiaxixi.com、dh.sejai.com、搜索b.jiaxixi.com?wd= |
| Microsoft Edge | Preferences、Secure Preferences、Top Sites、Web Data | hao123.me318.com |
| 360 安全/AI 浏览器 | Preferences、Secure Preferences、Web Data | 主页空、urls\_to\_restore\_on\_startup=hao.360.com/?src=lm&ls=n3fdda5dd9f；baidu→b.jiaxixi.com、so→so.jiaxixi.com |
| 360 极速/X | Preferences、Secure Preferences、Top Sites、Web Data | 主页360.jiaxixi.com；baidu→b.jiaxixi.com、so→so.jiaxixi.com |
| QQ 浏览器 | Preferences、Secure Preferences、Web Data | 主页空、baidu→bd.tao234.com、ai→chat.tao234.com |
| 世界之窗 | Preferences、Web Data | search\_url=b.jiaxixi.com?wd=、urls\_to\_restore\_on\_startup=hao.jiaxixi.com |
| 猎豹 | Preferences、Secure Preferences、Top Sites、Web Data | startup\_urls=hao.vip166.com、baidu→bd.tao234.com、so→so.tao678.com |
| Opera | Preferences、Secure Preferences、Web Data | hao123.3839069.com |
| 搜狗 | commcfg.xml、config.xml、Preferences 等 | homepages=www.baidu.com/?tn=99391883\_hao\_pg |
| 夸克 | Preferences、Secure Preferences、Top Sites | hao123.me318.com、dh.sejai.com |

bener以n参数运行时：把DATA/FUN资源写成临时文件；按g/e/x三种布局把扩展目录投进Chrome、Edge 或通用Chromium的Default\Extensions\<id>\1.3.29\_0。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sp2szBFpetuH2Cia4TYHc8csNBUw3VC00QqtYzVJ9kX18HLauHSEGgYcNFTJZEFVk8IJJ34uHpGZ9jRzRRHX1x5TIojpsRgj0icM/640?wx_fmt=png&from=appmsg)

**根据不同参数安装扩展**

改extensions.settings和protection.macs, 并将浏览器数据目录设为HIDDEN|SYSTEM。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpxC9tZS92zsLyg7jSiaZ2XiaibTcUg73SKNjpjt21hb8W355kJJXcHorKrcpZXaBzCu2hSj8eLqKWJLoIVdgL2MKWPF6GicHMjTMU/640?wx_fmt=png&from=appmsg)

**给Chrome装扩展**

**火绒安全建议**

* 避免使用来源不明的Ghost系统、封装镜像；
* 拒绝"一键安装/快速安装"，逐项取消“设xx为主页”“安装xx导航”“推荐xx工具”等默认勾选项；
* 软件只从官网下载，避开“高速下载器”“绿色破解版”“万能工具箱”这类二次打包渠道；
*...