---
title: 关于黑产团伙批量搭建高仿真钓鱼网站大规模传播银狐木马的风险提示
url: https://mp.weixin.qq.com/s/cKDK_cFaFA7qfsSMbNXn_Q
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:36:38.381147
---

# 关于黑产团伙批量搭建高仿真钓鱼网站大规模传播银狐木马的风险提示

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aoXpXT1UJRiak9ldjahStHomKe5tg6NzwS4c8hDTrFsenNiawWbkEa1bic8Po00cPHV9Y9caEiaQjogoMx2UUYfnD3jLNeFhdx5ibhrbxH3RSb0s/0?wx_fmt=jpeg)

# 关于黑产团伙批量搭建高仿真钓鱼网站大规模传播银狐木马的风险提示

原创

CNCERT
CNCERT

国家互联网应急中心CNCERT

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

感谢北京微步在线科技有限公司（微步在线）在本报告的样本分析工作中做出的重要贡献。

一、事件概述

近期，CNCERT监测发现银狐远控木马通过批量生成的高仿真钓鱼网站大规模传播，样本落地后将Shellcode注入系统关键进程执行远控，与境外C2服务器建立持久化连接，实现对主机的隐蔽控制。黑产团伙疑似利用AI工具大幅提升钓鱼页面制作效率，结合域名批量注册、仿冒网站访问流量精细化监测等手段，形成“网络钓鱼→木马下载→进程注入→远控控制”的完整攻击链。

二、钓鱼网站特征分析

对2026年2月6日-5月4日注册的439个钓鱼网站域名分析，这些网站的主要特点如下：

1）钓鱼网站主要围绕办公软件、浏览器和通讯/代理类软件进行仿冒，其中wps、chrome合计340个，占77.4%。

2）注册行为具有明显的批量化特征，发现最高峰一分钟内注册15条letsvpn相关域名。

3）域名后缀策略高度集中，hl.cn 占42.6%，com.cn占30.8%，二者合计73.4%。

4）命名模板复用明显，常见关键词包括zh、cn、apps、web、office并大量使用字母重复、缺字、错拼等手法。

5）钓鱼网站在bing搜索网站上通过SEO投递，确保网站能在bing.com网站搜索到；钓鱼网站会检测refer头信息，确保访问必须来自搜索引擎，若直接通过域名访问，这些钓鱼网站会跳转bing.com或者其他不可访问的网站，防止钓鱼网站被分析。

6）钓鱼页面并未对官方网站进行原样仿造，而是呈现出高度标准化的前端结构、清晰规整的 HTML 注释，且大量采用通用化前端技术栈。针对同一仿冒主题（如 Chrome 浏览器），不同时间注册的页面在布局与内容上均不统一。综合判断，此类钓鱼页面疑似由AI 编码快速生成。

被仿冒软件占比分布：

|  |  |  |
| --- | --- | --- |
| **相似软件** | **数量** | **占比** |
| google/chrome | 179 | 40.80% |
| wps | 161 | 36.70% |
| telegram | 24 | 5.50% |
| letsvpn | 18 | 4.10% |
| whatsapp | 12 | 2.70% |
| kuailian | 11 | 2.50% |
| youdao | 10 | 2.30% |
| bitbrowser | 5 | 1.10% |
| clash | 4 | 0.90% |

顶级域名占比分布：

|  |  |  |  |
| --- | --- | --- | --- |
| **顶级域名** | **数量** | **占比** | **含义** |
| hl.cn | 187 | 42.60% | 中国黑龙江地域二级域名 |
| com.cn | 135 | 30.80% | 中国商业机构二级域名 |
| cn | 102 | 23.20% | 中国国家顶级域名 |
| ac.cn | 8 | 1.80% | 中国科研/学术机构二级域名 |
| hk.cn | 5 | 1.10% | 中国香港地域二级域名 |
| hn.cn | 1 | 0.20% | 中国湖南地域二级域名 |
| ah.cn | 1 | 0.20% | 中国安徽地域二级域名 |

三、案例分析

（一）批量搭建钓鱼网站

攻击者疑似使用AI技术批量化搭建钓鱼网站。该黑产团伙批量制作仿冒Chrome、Clash、WPS等主流常用软件的高仿真钓鱼页面，将页面伪装成官方正版下载入口，以此诱导用户点击并下载恶意程序。如下图所示，为仿冒Chrome、WPS、Clash下载的钓鱼页面样例。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgko25KOEGibPIicQX9v5VQ0jeW16Jce86GexEyyZnsAev2jx72mf0vCWA9GGWLUaTsL5ORlVj0dTQm1XoAYq4gib1pX5lcZms2H8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRgfrjOfPC8wYHIY0dkiav9j03uojEic6euwEFBT6VMYT3GbsiczR6IGLWcjI7QRWCksTUXMakWHibjliaYiaiaqfsFMNvY3mHW0PZZp5I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjbUn4tia4FbyJmicTXqcf4ly89oNA2xiblnhDhDbShqT3Wt3tau38ricZuNZSUticoCFacKnNWNXGSlMtufCu40A6b59QOoYZ7hgz8/640?wx_fmt=png&from=appmsg)

这些仿冒网页前端代码有较强的编码固定格式，且对代码段有相对应的注释说明，如下图所示，仿冒有道翻译和Clash的两个网站，其html代码样式高度一致。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRiaiaY854hXzI5LeZE9KJJCfQczwR9HSnrsFbKtrCtFD5qjcLFjHSiaygJiaBb0ygdDXzucrWTQGq6yaaWKBXfRuYuCiaib3MHsplicdM/640?wx_fmt=png&from=appmsg)

（二）恶意木马投递

攻击者通过钓鱼网站完成木马投递。钓鱼网站会向用户提供携带恶意程序的压缩包下载链接，相关恶意资源文件大多存储于境外云存储服务平台或国内云对象存储服务中，通过多层跳转下载的方式迷惑用户，降低早期被检测拦截的概率。

（三）系统进程注入

银狐木马样本执行后实施进程注入行为。样本运行后，在安装真实Chrome、WPS等软件的同时，会将恶意shellcode注入到ctfmon.exe、sihost.exe、svchost.exe、elevation\_service.exe等系统关键进程中，以合法系统进程为掩护，实现恶意代码的隐蔽运行。下图为EDR产品告警，可以看出，被控主机与C2的通信均使用Windows的系统进程。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjE15yiazGS2zr55PSVLGic9ankgkF46QtxxdHl0vnBCicBwnq4t0pTPRI8wIHw2pDNTcD1A2IJNAH0HODz6HfI5uZzWaSeMXwSDE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRgOBAcNNwcEmPySKibrZejRLo3EgRrrfnQe6f9mXZeTicDCclibA1wExPiaQNiab9VtYg0ibISGnEdW9E1vXq6yESeSXKkOmxvpfibRZ4/640?wx_fmt=png&from=appmsg)

（四）远程控制连接

被注入进程主动发起远控连接。被植入恶意代码的系统进程会主动外联境外C2服务器，通信端口主要为443端口与22端口，成功建立连接后接收攻击者下发的远控指令，完成数据窃取、文件操作、持久化驻留等恶意行为。

（五）钓鱼网站访问统计

这些钓鱼页面使用了免费流量统计技术服务提供商51.LA的网站统计来对钓鱼网站的访问量，访问时长，来源页面等来做统计分析。利用这些统计数据，黑产团伙能够专业化的开发钓鱼网站，计算钓鱼网站的ROI（投入产出比），精准优化钓鱼策略，提升攻击成功率。下图为钓鱼网站的统计代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjYxwVaDTgwKPU5SXnBjY5PW0GYEQruqdlgeoxeoqGh3mPXJmWy04VxJCxPJ9PiaLb6KSMPHNnbQc84HvhY8hSGN5QLkWntDMos/640?wx_fmt=png&from=appmsg)

每种钓鱼应用会通过不同的ID进行区分统计，各应用对应ID的如下表所示。

|  |  |
| --- | --- |
| **仿冒对象** | **统计****ID** |
| clash | L4rC8E7ISMR5cOyi / L56E7kDSHNvNpfzY |
| 快连 | L4NNnKpJZ0RcW8GY / L4e6WH4KcxTQEsJO |
| chrome | L4eCf0G8oXvab2n7 / L4S9pW46ugZ5HLhW |
| teams | L4ixuUuJi0dA2nYF |
| WPS | L5OOMojcmFzavw26 |
| 搜狗浏览器 | L5MbevAiByh9Bosu |
| telegram | L5TOP7tRWKlFL5Su |

四、恶意样本分析

对仿冒Chrome的应用的安装包进行分析，发现该软件运行后会安装真实的Chrome软件，同时该程序会将恶意代码注入系统进程中隐藏自身。样本相关信息如下表所示：

|  |  |
| --- | --- |
| **属性** | **值** |
| 来源钓鱼网站 | mb-google-chrome.hl.cn |
| 样本下载链接 | https://xgootd.oss-cn-hongkong.aliyuncs.com/ggpc\_win64\_14.zip |
| 样本hash | 2f8cf966b3fc87ba1a8151428a36652e78f2d57005621eecd514629a902e88b5 |
| 样本名称 | ggpc\_win64\_14.zip |
| 样本C2 | sangbiao11.com(137.220.154.107:22) |
| 样本简述 | 样本为Gh0st远控木马，通过VMP加壳以及内存加载的方式规避检测，最终实现远程命令执行和敏感数据窃取等恶意功能。 |

该样本为“Inno Setup”打包的软件安装文件，样本打包于2026年1月2日。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aoXpXT1UJRg2Ngt7O5xpywFr9g7PSLN3UuIBn0h4icdibFbxicAnh8emq2fEiaSp1wLfia6IfRibRPcqwDlrA5ATcQXR5SQ13fcYKTvzWlu13QPpQ/640?wx_fmt=jpeg)

安装文件运行后会在“C:\Drivers\ySCqV\cb3uGF\s6quO\VPUE”目录下释放文件并运行可执行文件Hveuh3.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRh7SsSpzb20CLY4I03VkLdxUAXcsz2nny3ufDmOf7ZSIg8O9VSic3JZEWiaEls8uXldQb2pqhmP0MMJFxT9GyqibnWbs7lqNibKCe4/640?wx_fmt=png&from=appmsg)

Hveuh3.exe具有无效的数字签名，且含有PDB路径：“E:\CC\lab\_release\video\src\client2\GameLiveTool\Release\x64\D3DHook.pdb”。通过该PDB地址分析可执行文件是基于一个游戏录屏、直播、外挂检测项目的正常代码，样本编写者可能具有游戏外挂编写能力，同时做了远控木马的开发。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjuuad7JNX7MB6fZPVx3dMNrY7pgAAMGqAJv8PmdWougL037E6QvlUiaurSPXs2HSL2X1DAAP8TNEfjiaMc7l5oadvXJv1pS1LNg/640?wx_fmt=png&from=appmsg)

可执行文件Hveuh3.exe文件会加载同目录下的可执行文件0C5uqPzO.Uww，该文件为vmp加壳的dll可执行文件，文件信息如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRj4nhE9iaHuJibqNLReb5yKgTnCWxDDMy8Rd5PzePmeGI28hZ2q7cVCicTaFEOlBMSmu74SMRKAcRT2MXwIolOytTicpJQE1e15u3s/640?wx_fmt=png&from=appmsg)

可执行文件Hveuh3.exe文件会导入0C5uqPzO.Uww文件中混淆后的导出函数，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjjatdvQTWMRTgpvYvjW9xU3ibibWnDw8LtvEzRKxj0WoFn3M1KrpM4MvtvZvBH1fMLRb27HjMiaz6kFDM9yZh7DLmFeXmEnhVC4c/640?wx_fmt=png&from=appmsg)

恶意dll文件0C5uqPzO.Uww会使用CreateFileW方法读取同目录下的加密Shellcode文件L0PM0o0j.EC，并进行内存加载。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRgUYdia5ejsBcqicHQdhHsEnOMBtibO0Rc03E9KMyDRL4DltIUnrPSjUpZuNIxdHj0vibNvGQOp6glFAXSOTPBBsBwyENm3y7iaxtxg/640?wx_fmt=png&from=appmsg)

样本同时将释放目录“C:\Drivers\ySCqV\cb3uGF\s6quO\VPUE”设置为不可删除和无法访问：

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhoa5upbMXNGaI7bHpsEZPauR1EwE7PWVib2BqJiaSdYlcVpLHwtmRWXz2sDJibUkcC2B60CjK50tKtcibHIB5XEg9ibxtA6rqOJDj0/640?wx_fmt=png&from=appmsg)

动态调试发现该样本会获取system权限，创建服务自启动，并在“sihost.exe/ctfmon.exe”等系统进程中注入gh0st载荷，并加密配置保存在config.ini文件中：

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhVMzkYgYkibx9z7vRxRjYsCwCic7iaumn9vrFXM4BonEt0gwtPl6MAfAZ6zicJdx7dq2REZxWbBlAlB1b1V4cWdj1nJktP3E9cgW8/640?wx_fmt=png&from=appmsg)

config.ini保存在“C:\ProgramData\”下随机生成的目录中，如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRgP40pAKbhYI74TDpNfU5RampLiaW6eB4cz22w7FWCu8tmzf4CBNpx9BuEDK60NygiaJycI1F0v2tgSvHOLbiap5zgXh529AX1KS0/640?wx_fmt=png&from=appmsg)

植入完成后，会与其C2地址进行通信，C2地址为sangbiao11.com(137.220.154.107:22)。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRjE44pqFFIUiadZSsmMBk8yatCaW2YlcRsMWgjibtiaxDs3RwMkybgsU3ictFUng9mKasiaBPOywmj20icC2KxbET87P8bJ14icrER80M/640?wx_fmt=png&from=appmsg)

五、控制规模

通过关联分析已发现17个相关C2恶意域名，和20个C2的IP地址。通过监测分析发现，2026年4月8日-5月7日，相关木马境内肉鸡数最高达2.6万台，累计感染肉鸡数达到18.2万台，每日总上线规模变化趋势如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aoXpXT1UJRjVSCPoiaW4HG7v4fHGA5DibG862eUQY0xyAQKfq2AEsh0cEv5qbZ3z05VwzRYcfuwphNO3WVM5xuhYR5nWLp7zEkLhfzt1Rrmgc/640?wx_fmt=png&from=appmsg)

其中日控制规模超500的恶意IP有9个，其每日被控IP数变化如下图所示。其中，近1个月总控制规模超10000个IP的C2共有6个，分别是185.203.39.134（dd.kmsccedn.com），182.16.88.242（vaeth.cn），103.12.148.80（feiji22.vip），137.220.158.22（www.amdyjl5.com），27.124.2.150（www.w1pf9.com），104.143.33.78（www.vpconn.fit）。

![](https://mmbiz.qpic.cn/mmbiz_png/aoXpXT1UJRhHkjOlQc0OdXUTpfpJZmL9aVUdRBRLZnicnoM6u9xHAXkibibXVSN9srY2CkslZf8PvDsj0QPDg28qbhtu7KeRlaTHnsrCkNDpkU/640?wx_fmt=png&from=appmsg)

六、防范措施

请广大网民强化网络安全风险意识，提高自我防范能力，谨防仿冒软件、恶意程序侵害，避免造成财产和信息损失，主要防范建议如下：

1）优先认准软件官方网站（如www.wps.cn）及手机、电脑官方应用商店；警惕搜索引擎结果中带有乱码前缀、拼接拼凑式的域名链接，例如 kn‑wps.com.cn、www-wps-...