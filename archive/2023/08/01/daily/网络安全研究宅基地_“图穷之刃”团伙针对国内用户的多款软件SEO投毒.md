---
title: “图穷之刃”团伙针对国内用户的多款软件SEO投毒
url: https://mp.weixin.qq.com/s?__biz=MzUyMDEyNTkwNA==&mid=2247494995&idx=1&sn=73f89273b92c9cd86ea316a91df104a6&chksm=f9ed81ecce9a08fa29d867c7ffceb7e1766a654d53a264a945ea06ab4f638c9c94e5ac18f9b2&scene=58&subscene=0#rd
source: 网络安全研究宅基地
date: 2023-08-01
fetch_date: 2025-10-06T17:02:35.823612
---

# “图穷之刃”团伙针对国内用户的多款软件SEO投毒

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AvAjnOiazvnfwKia3E6ic6Ag7qVQnmeBjP1uxktnPoJLfWtSQr8CHNyy84d2QYsJpVs5SHGCEnNRBAxAAfp6SAamA/0?wx_fmt=jpeg)

# “图穷之刃”团伙针对国内用户的多款软件SEO投毒

原创

猎影实验室

网络安全研究宅基地

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHXFzlHWs49fNGMdcoT4myEWTXg5f0BXazicrqIVqetIxaF3qMF62U63icibOiafcVA7x33kwJibcS6fw/640?wx_fmt=png)

|  |  |
| --- | --- |
| **“图穷之刃”团伙针对国内用户的多款软件SEO投毒** | |
| 内部编号 | DBAPP-LY-23072701 |
| 关键词 | 黑灰产、SEO投毒、GRP-LY-1003 |
| 发布日期 | 2023年7月27日 |
| 更新日期 | 2023年7月27日 |
| 分析团队 | 安恒信息猎影实验室 |

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvndHXFzlHWs49fNGMdcoT4my7Q4MBolzTevVUyvftdPAP6pd4wfcWzLLOibAwPfQriaBUr0hPnlGSONA/640?wx_fmt=png)

**01**

**事件概述**

近期，安恒信息猎影实验室监测发现某黑灰产团伙针对国内用户进行SEO投毒攻击。

该团伙通过购买搜索引擎广告，将多个伪造的软件下载页面置顶于指定关键词的搜索结果中。下载链接对应的文件是恶意软件与正常软件捆绑在一起的msi安装包，安装包运行后在显示正常的安装程序的同时，还会执行恶意软件。

经分析发现，该团伙投递的恶意软件回连C2更新频繁，执行流程复杂，采用多种手法对抗检测和调试，最终将加载FatalRAT窃取用户敏感信息。

由于该团伙的样本执行过程最终都会通过读取一个图片文件数据得到最终的远控模块，猎影实验室以成语“图穷匕见”之意将该团伙命名为“图穷之刃”，内部追踪代号“GRP-LY-1003”。

|  |  |
| --- | --- |
| **“图穷之刃”团伙组织画像** | |
| 团伙性质 | 黑产团伙 |
| 活跃时间 | 2022年4月至今 |
| 攻击动机 | 信息窃取 |
| 攻击来源 | 未知 |
| 攻击目标 | 包括国内 |
| 常用工具 | FatalRAT |
| 攻击动机 | 搜索引擎广告、钓鱼网站 |
| 技术流程 | 初始样本为msi文件，包含一个正常的安装包和一个木马加载器，木马加载器通过多种方式加载木马，最终都会通过读取图片文件，通过base64解码+LZNT1或者与指定字节异或+加和运算解密出FatalRAT。 |

**02**

**攻击手法分析**

目前，安恒信息猎影实验室监测发现“图穷之刃”团伙的伪造下载网站的软件包括WPS、Potato、Skype和Whatsapp等，搜索相关软件，搜索引擎结果如下：

|  |  |  |
| --- | --- | --- |
| **搜索关键词** | **搜索引擎结果** | **钓鱼网站** |
| WPS | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOtkHyHKdDnJ0y5WcmuljhK1DguzmGtf7GGj5IaKcUib4VXFv5ict8LSUg/640?wx_fmt=png) | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMO81jrqeVBPiazT50uMNUKdSetBGBRuIELkXYjMbUDChf5bJnCJt4wicfQ/640?wx_fmt=png) h\*\*ps://wp.whkoyhns[.]club/ ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMObLP6AUflsC7acdU8y9sGySdks0RbLNia8E3SekYO1TicDwryTKsR40lw/640?wx_fmt=png)  h\*\*ps://wps-office-hua[.]com/  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOSAPhSgFcibMOPtwAbUzDy0w6ERe6tW2GAALpsiakUqBafTTONWiatticzQ/640?wx_fmt=png)  h\*\*ps://vvtele.my.canva[.]site/wpsoffice?gclid=Cj0KCQjw756lBhDMARIsAEI0AgnvaNXtdZ4zAM7f2N5J8OORfijkbIymn\_luc71bxTBRb8m9P9G25UcaAmNdEALw\_wcB  ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOTtaSNF3tNKiae8MO4cRnURrrVzPop2k2ORIxwI9ribsBvicdEAmN7t6Qg/640?wx_fmt=png)   h\*\*ps://office.wps-pc[.]cc/index.html |
| Potato | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOC9p6XQtwx4OtHcibOfmibAce7ibibKHnNculPEtVoP74AYwJ1jfxqFWh9A/640?wx_fmt=png) | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOUgZ1HCDpeGQialmKbhSMujtpHSZceHzNevGWnmyaR17S4icXyek4ibpkQ/640?wx_fmt=png) h\*\*ps://web-potato[.]com/ |
| Skype | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOZTKW7vvlaXkiboiavicBEfKYjTySUxMyogJrVOly43snBg4cPNaA5CSCg/640?wx_fmt=png) | ![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOGEkeibWNZ6cbV1kpbC9XxXPSwrFmNeFcZqynzfGCibEXJy2OIpCkBM9A/640?wx_fmt=png) h\*\*ps://sk23.my.canva[.]site/?gclid=CjwKCAjw5MOlBhBTEiwAAJ8e1gdpjET6aDtjKF6QTDCDNRiR\_zfcVVydm39lQaQOgBv5-PgNotUoHBoCInIQAvD\_BwE |

**03**

**样本分析**

**类型一**

类型一样本加载流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMO4vbtiaNH8MXorJcMFGzpqeRVIJozzgwORuosicAEZngnPM1SZUicdfSzA/640?wx_fmt=png)

样本下载后将运行正常的WPS安装包和木马加载器，木马加载器首先读取资源节数据，使用自定义异或算法将资源数据解密。

并在C:\Users\Public\Videos\study06目录下分别写入并调用1.dll、2.dll和3.dll，其中1.dll和2.dll使用vmp加壳保护，1.dll运行后将通过调用IpRealeaseAddress释放主机ip，使得主机无法联网，2.dll将检测主机是否联网，如果联网则进入循环直至再次无法联网，无法联网时将释放并运行恶意文件，随后3.dll通过IpRenewAddress恢复主机网络。

这一过程既能触发沙箱的防断网机制，使其在沙箱中无法继续运行，又能够绕过杀毒软件的云查杀。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOZ28gmaibicZnFrnIVB0UhUDpnYibs9szhHOU8xDPJItzDFBQMRo6LIMfA/640?wx_fmt=png)

2.dll首先通过连接https://www.baidu.com/检查主机的联网状态，若主机处于非联网状态，则向主机的C:\Users\Public\Music\CCTV【三个随机字母】\【三个随机字母】文件夹下释放文件Agghosts.exe、CheckDX11Support.dll、Enpud.png、msvcp120.dll和msvcr120.dll。并通过COM对象启动进程Agghosts.exe，否则将一直循环连接https://www.baidu.com/直到主机进入非联网状态。

Agghosts.exe通过白加黑加载方式加载CheckDX11Support.dll的KuGouBeautyInitialize函数，该函数将Agghosts.exe写入Run注册表键，并读取Enpud.png数据，将数据经过base64解码和解压缩处理后得到dll形式的FatalRAT加载器。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOj69op892ibGpR7JUZ2GlKeXnlkPG5kc9rC4sAUc65MN7x5vKXu3zFsw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOHTvWk5hehrwGciblEonJreQ34M1yGK8BAUsibwSv799yFabCbm99oibRQ/640?wx_fmt=png)

解密后调用dll的andleCallback函数，该函数将一段加密的数据解密为dll后调用SVP7函数，这个解密的dll为FatalRAT。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOH7OegXIKl0Lv1RcQicB5CacDIOUjJokDNPBJKbCfcAmpEUzG3ClGUicw/640?wx_fmt=png)

在FatalRAT的初始化过程中，设置的回连ip和端口为103.151.44.22:8081，其通讯特征能够被安恒云沙箱识别。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOloNJwfrqwVcWKBPVbHPyh4YBWGPmSqG7as0ACvKJBz2icFRCT0JYPLg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOXHTZAo9F8wXafpickOqn6DicuuVnHianccI5X3R0qia1ReRG8B1hbEFEIg/640?wx_fmt=png)

经分析该FatalRAT支持屏幕截图、键盘记录、清除各种浏览器缓存、文件上传下载、命令执行和运行插件等多种功能，具体如下：

|  |  |
| --- | --- |
| **指令** | **功能** |
| 0 | 结束指定进程 |
| 1 | 卸载自身 |
| 2 | service注册表下创建Remark键 |
| 3 | service注册表下创建Group键 |
| 4 | 清除应用日志、安全日志和系统日志 |
| 5 | 下载并运行指定文件 |
| 6 | 下载文件至指定目录 |
| 7 | 自身复制到ProgramFile目录下 |
| 8 | 前台打开网页 |
| 9 | 后台打开网页 |
| 0xA | 开启击键记录 |
| 0xB | AppData目录下释放svp7.exe，运行uac.exe |
| 0xC | AppData目录下释放uac.exe |
| 0xD | 弹出消息框 |
| 0xE | 查找指定进程 |
| 0xF | 查找指定窗口 |
| 0x10 | 打开代理 |
| 0x11 | 关闭代理 |
| 0x12 | 加载插件 |
| 0x6B | 开启键盘记录并上传键盘记录信息 |
| 0x6C-0x71 | 加载插件 |
| 0x7c | 窗口和鼠标操作 |
| 0x8A | 上传击键记录信息 |
| 0x8C | 更改分辨率和色彩深度 |
| 0x8E | 切换为管理员权限 |
| 0x8F | 启动谷歌浏览器 |
| 0x90 | 终止explorer.exe进程 |
| 0x91 | 清除Internet Explorer浏览器的历史记录、缓存、cookie等 |
| 0x92 | 删除谷歌浏览器用户数据 |
| 0x93 | 删除Skype用户数据 |
| 0x94 | 删除Firefox用户数据 |
| 0x95 | 删除360浏览器用户数据 |
| 0x96 | 删除qq浏览器用户数据 |
| 0x97 | 删除搜狗浏览器用户数据 |
| 0x98 | 弹出消息框 |
| 0x99 | 下载并安装UltraViewer.exe远程控制软件 |
| 0x9A | 下载安装AnyDesk远控软件设置访问密码为123456 |
| 0x9B | 执行指定cmd命令 |
| 0x9C | 暴力破解弱用户名和密码 |

**类型二**

类型二样本加载流程如下：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOia6QxhxwoLJ93QIsFricoDYWOVvcH0HcPeFDRBzGQgxV1pKmJ53Yib8nw/640?wx_fmt=png)

样本下载后将运行正常的Potato安装包和木马加载器，木马加载器将在目录C:\Program Files\aiwor\下释放文件success.exe、UdpRepot.xml、pcid.dll、UdpReport.dll、ResLoader.dll和DockHelp.dll，并在目录C:\Users\Public\Documents\123\下释放文件Q\_05.exe，其中Q\_05.exe使用Themida/Winlicense加壳，pcid.dll使用Safengine Shielden加壳。随后运行Q\_05.exe并删除自身。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMO4sJ0YaVAoaK4ScQsNxWju5MU67D802r9gngJkSq2YNv7RJYDAr7G3w/640?wx_fmt=png)

Q\_05.exe将运行success.exe进程，success.exe会加载pcid.dll的PCIDGetIdentify函数，该函数主要功能为读取UdpRepot.xml数据解密，并运行，解密算法为数据与指定字节异或、加和、再异或。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOupv9Juu517srV7ySsnTC2tXkIZ63icDHhFmgiaZ0PY6HE5xbjjjNrA2A/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOcNxkqiaiagibuLZYBclVLVclwU0MrkibzHKtXIkMBNwNg6wbicBWM8EavVQ/640?wx_fmt=png)

UdpRepot.xml的数据经过解密运行，首先将success.exe通过Run注册表设置自启动：

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMO3ayTV3pIOjD0DwiaTw3fGKLNtn1G3E8ZC6ia9icnMowH7XjhC0Wo47c4g/640?wx_fmt=png)

然后分别将数据写入文件C:\Users\Public\Documents\t\yh.png和C:\\Users\\Public\\Documents\\t\\spolsvt.exe，并以挂起状态运行进程spolsvt.exe，通过hollowing注入将yh.png文件解密并注入该进程，并恢复线程。

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOxDtM0cZoHzvLFQlRC0JUAdOuXC6a7ibHxJd3gXYTfXWCjoZibO6og9Gw/640?wx_fmt=png)

spolsvt.exe再次解密一段数据，并将该段数据以dll形式加载，并调用其中的“SVP7”函数，该dll为FatalRAT，与类型一样本的功能完全相同。回连地址和端口为hao11.wccabc[.]com:3927

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMO0xBomUUtOmdibQOKzMxObJjB2WkPO2ZOxYg9ZJY5QlEBjemTjcl3FiaA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/AvAjnOiazvncT8qgdYSJzwLTOuxpAeTMOoX8qQicV9Oz1OTMicibTqoibUDONoacwPXAcQ7cLbN3p3Qy0XLUG9ZlFiag/640?wx_fmt=png)

**类型三**

类型三样本加载流程与类型二加载流...