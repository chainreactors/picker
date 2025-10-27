---
title: 揭秘MuddyWater组织的多款RMM软件攻击
url: https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247500427&idx=1&sn=29a99b3ae418762fdd184f8b82c20d79&chksm=f9c1f182ceb678943a0d6cca3a94f0e7860aca6046e8b7a385ad9c266c7630de225b4bd7dd10&scene=58&subscene=0#rd
source: 360威胁情报中心
date: 2024-08-30
fetch_date: 2025-10-06T18:07:59.353965
---

# 揭秘MuddyWater组织的多款RMM软件攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KYWkvPXB3t2PWqunGJ5ClWhVEoRbuwNFR50JTNIjbmQ0IoVueCliaoqw/0?wx_fmt=jpeg)

# 揭秘MuddyWater组织的多款RMM软件攻击

原创

高级威胁研究院

360威胁情报中心

MuddyWater组织又称Static Kitten、MERCURY，其相关活动可追溯到2017年初，并长期活跃于中东地区，同时也针对欧洲和北美国家进行攻击，主要针对行业包括政府行政机构、军事实体、通信和石油公司等。该组织特别擅长于鱼叉攻击，它们的攻击行为具有高度的隐蔽性，并且拥有多种攻击载荷武器，并在不断更新。

360高级威胁研究院捕获到了MuddyWater组织使用多个远程监控和管理（Remote Monitoring & Management，RMM）软件用于攻击。通过后台大数据关联分析，发现该组织自2020年以来一直依赖合法的RMM软件作为其攻击的有效负载,使用过的RMM软件包括但不限于Remote Utilities、ScreenConnect、SimpleHelp、Syncro、N-Able和最近的Atera
Agent。鉴于该组织近期频繁使用这类具有完整签名的RMM软件进行渗透，因此我们在这里进行详细说明该组织利用此类软件攻击的过程，希望经过曝光披露，相关的企业和个人可以提高安全防范意识，以免遭受损失。

#

# **一、 攻击活动分析**

## **1.  攻击流程分析**

通过分析MuddyWater组织使用过的多款RMM软件，我们发现该组织近几年在攻击中虽然不断在变化RMM类型，但是该组织投递这些RMM载荷过程基本一致，下图是释放RMM软件的常用流程。

#

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KPsByQZwXdYvegtmR5A78nZg52gAkf0FriagUrxEpdqPVK1nJ2Zhibp8g/640?wx_fmt=png&from=appmsg)

需要说明的是，该组织特别擅长利用鱼叉钓鱼邮件进行攻击，其流程基本都是攻击者在邮件中携带恶意压缩包或文档文件，诱导用户打开此类文件时，从而进一步下载后续RMM文件，并且邮件正文、文档名、文档内容这些基本都有阿拉伯文伪装内容，使其具有欺骗性，警觉性不高的用户很容易中招，中招后该组织使用的RMM一般以服务方式启动，并且静默连接其主控端，用户在此过程中更不容易察觉。下面就每款RMM软件的攻击过程进行简要分析，希望用户警惕此类攻击。

## **2. 攻击中利用的RMM软件**

##

## **2.1  Atera Agent**

近期我们多次捕获到该组织利用Atera Agent工具进行攻击行为。MuddyWater组织通过携带恶意RAR样本的方式进行网络钓鱼传播，并且RAR文件进行加密处理以免被安全厂商软件拦截，通过邮件内容诱导用户层层递进，最终运行RMM工具。

##

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KMEn7dsOlnALNOFJoUrrVeaJ65W04ygL2sIoPmPKVtKR2aB3e2ZpuFg/640?wx_fmt=png&from=appmsg)

利用密码“123456”对邮件附件digitalform.rar解压得到Atera Agent工具的msi安装包，安装时会使用内置的账户和相应的ID进行连接至Atera控制端。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KTTfK41V8btCKicFLHrg9S51KBFtYYuCxuBAsEVTeQak9hAT8sGSIa0Q/640?wx_fmt=png&from=appmsg)

安装一旦完成，攻击者可以在受害者电脑上执行任意操作，并提供命令执行、文件下载、上传和监控等各种功能，还可在系统上运行第三方RMM工具如Splashtop、AnyDesk、TeamViewer和ScreenConnect。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798Kic2W26zkialEb1fKVxFcu9TTrfGLnFOAtWNAzumnH5bp6yNkFmlOmWFg/640?wx_fmt=png&from=appmsg)

另外需要说明的是，我们还发现了MuddyWater组织借助受信任的文件共享服务 Egnyte来伪装成中东某国家的一所大学的域名（kinnneretacil.egnyte[.]com）进行分发Atera Agent安装包的攻击活动。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KPWUETMtUD7Op1G7EnndV7xg0Erl402ETHz1DZrh91NibUK8YBB4zx1g/640?wx_fmt=png&from=appmsg)

##

## **2.2  ScreenConnect**

攻击者通过携带诱饵文档的方式进行网络钓鱼传播，并诱导用户层层递进，从而最终加载ScreenConnect软件，其捕获的文档内容如下，阐述的是阿拉伯国家之间关系的联合研究。

##

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798K6gTRnsfQbjrkzXDibOM0fNGgJMFGicQuGzL4SDRCyXpnibib6Z0r8y2ibow/640?wx_fmt=png&from=appmsg)

文档中仿冒的超链接实际指向 ws.onehub.com/files/7w1372el，该链接实际上下载的是一个ZIP文件（md5:960594cbdf938bcb03bd0637843d9154）,其文件名为المنحالدراسیة .zip（奖学金.zip）,该ZIP中包含一个同名的EXE 文件，该文件运行后实际上会进行ScreenConnect 软件的安装。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KfKicp1IDBLkU0aQOv5o9ibJpbhSDrU7gn4SGgpiahFHPJ064hMou8SYDA/640?wx_fmt=png&from=appmsg)

安装完成后，会创建ScreenConnect Client服务并启动，这样也让用户难以察觉。如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KRKBWaiaBS3fAPjlbyvbUKibVOk1CpbVU2OXrt1d05Tb09npd6FMzHuBg/640?wx_fmt=png&from=appmsg)

启动参数包括了会话类型、客户端GUID、服务器URL、端口等信息，这样可以主动连接到控制端，其主要参数如下：

```
e=Access&y=Guest&h=instance-sy9at2-relay.screenconnect.com&p=443&c=mfa&c=mfa.gov&c=mfa&c=pc
```

攻击者打开instance-sy9at2-relay.screenconnect.com，就能远程控制受害者电脑、执行各种命令和安装工具等一系列操作。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KDM7YXJ2hOk7tCRjVgmYVgajPdGnhH3hqWaib4DnecPCgJia79bWPC3BA/640?wx_fmt=png&from=appmsg)

##

## **2.3  Remote Utilities**

MuddyWater组织在攻击中释放Remote
Utilities软件的流程与ScreenConnect基本一致，有点细微差别是钓鱼链接是嵌入到PDF文件中，而上述ScreenConnect是在DOC文档中。攻击者通过使用PDF诱饵文件诱导受害者下载携带Remote Utilities安装包的zip压缩包文件。

##

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798Kxo1RV380JmJicetlREKia2wicibXrpT6vlIwjBllwiafX00npISIs13QZ8A/640?wx_fmt=png&from=appmsg)

下载的ZIP压缩包解压出经过UPX加壳的PE文件，执行时会释放出host.msi安装包，安装时创建描述为“Remote Utilities – Host”的服务并启动rutserv.exe程序。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KPnWEFGdXQibo25icqLs2G0WYcmjDRxRqmQLvoklsYylPqd1Xv3W4L4RA/640?wx_fmt=png&from=appmsg)

与此同时，rutserv.exe会将自身生成的Internet-ID等信息发送至攻击者邮箱，攻击者使用该ID进行连接目标主机从而可以进行完全控制，并执行各类命令。

**![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KjB8d20t3ZYdxeibMFVFyIjJA8LQxqibicWDM5sYveIgEWGbG6khFsIhSA/640?wx_fmt=png&from=appmsg)**

## **2.4 N-Able**

通过分析捕获的样本，发现MuddyWater组织于2023年10月转向对N-Able工具的使用，其攻击方式依旧是通过利用钓鱼邮件诱导用户下载其恶意样本，稍微不同的载荷被攻击者托管至storyblok文件共享网站，而不是经常使用的onehub类网站。此外，下载的zip压缩包也不再是直接携带的msi安装包，而是采用lnk启动隐藏目录的方式安装N-Able RMM，如下图所示，通过Attachments.lnk执行隐藏目录Windows.Diagnostic.Document下的Diagnostic.exe文件。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KoX2dlEYBOMuMH1v02dgNBJib6ZjOWGUd8lKfLjFolK4jestXMC2exyA/640?wx_fmt=png&from=appmsg)

Diagnostic.exe功能就是打开诱饵文档和执行N-Able RMM安装程序。相关诱饵如下所示，内容为某中东国家公务员制度委员会的官方备忘录。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KjNaiaDt4lN1jhI4BkjuF43oWEQkPKW9adxe35xNEoWia8ZSgURMAcBfQ/640?wx_fmt=png&from=appmsg)

N-Able客户端程序是由攻击者服务器配置页面生成的Agent程序，然后诱导受害者运行，一旦安装后就会主动连接其控制端。N-Able是一款高级监控的合法远程管理工具，其功能涵盖了远程监控、备份、安全和网络管理等多个方面，其管理页面如下所示。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798K99ka1uZWdbkyrgGnomQcDr1T3Phs436fTjc7mPW0gEZxNsJib6oVNIg/640?wx_fmt=png&from=appmsg)

## **2.5 Syncro**

通过溯源MuddyWater组织样本，发现该组织可能最早在2022年9月开始使用Syncro远程管理工具。除了使用PDF或Office文件附件的方式，还发现使用过HTML文件进行投递。下图展示的是MuddyWater组织通过伪造同一发件人（magdy.ahmed@eaco.co）发送钓鱼邮件，并通过邮件里面的链接或者借助HTML文件进行攻击的样本。使用HTML进行投递的原因是HTML并不容易引起安全产品的注意。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KH99TBg6y5Wfky3GTBtDlO3dGzGxL7B6Loib2tfZunQbOkekhzictGIkA/640?wx_fmt=png&from=appmsg)

两封邮件分别携带恶意链接和HTML附件，其中HTML网页设计成egyptianabrasives.com内部文件托管网站，引诱受害者点击下载按钮，下载链接为“https://1drv.ms/u/s!Ah4-vpXOyPCGdd1DkLHmbL2qXQU?e=RkaudW”。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KB0K4gS55SOwbBFRI3tvH2JZ3fCza5vdY9Ulwf2DJWkwTMZHNIxV2zw/640?wx_fmt=png&from=appmsg)

另外，邮件正文嵌入的恶意链接为https://www.dropbox[.]com/s/scj6n0l58yyb3f1/Purchase%20Order%20for%20Supplies--no12305570.zip?dl=0。从这两个URL可以看出，攻击者使用的都是公开的文件托管网站，这样能减少被安全防护软件拦截的概率。

通过上述链接下载的载荷是一个Syncro的安装程序，Syncro也是一个RMM程序，也都带有数字签名且本身并不具有恶意行为。通过查看MSI程序的属性配置信息，Syncro安装文件中包含API\_KEY和CUSTOMER\_ID等信息。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KsspEf5QxGtfGDxWCLBWmbdwcWlVlwzQzgOFOxPT50FbUtSkzqrhLLA/640?wx_fmt=png&from=appmsg)

Syncro安装程序通过命令行参数读取配置中的API\_KEY和CUSTOMER\_ID等信息进行身份识别，从而连接指定的控制端。一旦连接，攻击者可以进行全方位的远程监控和管理，并执行多种操作。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KExvIrassZQIPxicyrTKPiaZgsI8sehibA2BArfHmSibPamyeqyzCRk5ZYg/640?wx_fmt=png&from=appmsg)

## **2.6 SimpleHelp**

在2023年底，我们陆续发现了多个与MuddyWater组织相关联的SimpleHelp样本，和以往类似，通过使用公开的文件托管网站（storyblok[.]com），其托管链接为https://a.storyblok[.]com/f/255988/x/5e0186f61d/questionnaire.zip，文件名为questionnaire.zip。通过关联分析，发现MuddyWater使用的Atera远控程序的部分文件名也是questionnaire.zip，因此攻击者大概率使用了相同的方式投递SimpleHelp程序。

questionnaire.zip内包含了一个名为questionnaire.exe的SimpleHelp客户端，运行后该客户端会主动连接服务端。这里特别说明下，SimpleHelp客户端程序是由攻击者在自己的服务器配置页面生成的Agent程序，以便安装后主动连接其控制端。

截止到现在，我们仍能观测到MuddyWater可能存在的基础设施(193.109.120.59)还在被使用，通过http://193.109.120[.]59:8008/welcome还可以下载Technican Console控制端和 Remote Access客户端，一旦该客户端在受害者电脑运行，便会主动连接服务器193.109.120.59，这样攻击者就可以在控制面板完全监控其电脑。通过该IP关联样本发现在2024年4月份该组织的攻击仍然在持续。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798K0MzZ1jYEg5xMZb7IMoQWEH5n4oeoWOdx28c7HUaEO4IvPbKicERW7yw/640?wx_fmt=png&from=appmsg)

下图是攻击者控制台程序，当受害者连接后，攻击者可以实现文件上传下载，执行命令，安装程序等一系列操作。

![](https://mmbiz.qpic.cn/mmbiz_png/6CNEHNicic4PrEwatqdt8D3mibjdIoia798KFIL6pMYzGOticWVXOnoZ5OqJBYpPMuPw5xh1Q5GTv2kN5dic7n6QbJkQ/640?wx_fmt=png&from=appmsg)

# **二、归属研判**

通过对MuddyWater组织攻击活动的相关信息进行深入分析，发现此次披露的RMM攻击符合该组织以往的TTP，具体表现如下：

1. 攻击者释放RMM软件的流程基本一致，都是通过鱼叉邮件，并且邮件内容、主题、附件标题及内容都具有伪装性，诱导用户运行恶意文件或点击其中链接下载下一步载荷，其链接主要以一些文件托管网站为主，如onehub.com，这样在下载过程中不易被安全厂商查杀，这种链接在该组织其他攻击活动中也多次使用，符合该组织一贯作风；

2. 该组织使用的大...