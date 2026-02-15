---
title: 流氓软件卷土重来？恶意驱动作祟下发DDoS工具包
url: https://mp.weixin.qq.com/s/fa3T9jpeXE_kzeGx6QkdqA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:18:38.496647
---

# 流氓软件卷土重来？恶意驱动作祟下发DDoS工具包

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/u1Oy5xQ01So2RlqQXfusWhTicurJ3FDj5MdEgzPBJUiaib0e66RdzAYrhVqOzvMx6tWKaiaMerh011XlSAhlmUaaoeJQicvACXO3jedHPJRfP5zU/0?wx_fmt=jpeg)

# 流氓软件卷土重来？恶意驱动作祟下发DDoS工具包

原创

火绒安全
火绒安全

火绒安全

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/0icdicRft8tz6h5nbHLqtyUeLADJt7ewgFh6AbCAxQeO9D2y9CcDK7liaJDD5PZGwbqURKywb0SqKeiaCUIgyLTVkw/640?wx_fmt=gif&from=appmsg#imgIndex=0)

近期，火绒威胁情报系统监测到一款DDoS工具包作为恶意组件被下发至数千名终端用户。经火绒工程师分析，该工具包的源头是一个带有有效签名的恶意驱动z\_driver，其通过注册内核回调实现自我保护，并经双重解密释放恶意DLL注入系统进程。随后，该工具包被下载至本地，用于进行DDoS攻击或刷量行为。火绒工程师发现，此组件自2025年2月起便已下发至终端用户，且仍在持续进行版本迭代，部分较新样本已为DDoS工具包添加注册表持久化功能，并已执行多次DDoS攻击和流量刷量行为，严重威胁终端与网络安全。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Srh78cptxAkna800NSkEUJfxdQFSp2vYnBoOVAjk02PrUCyFXPuy5gp4vgKicufPHclaKannTt6luX0E2uTDPAdUvaPicibl6tBDc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoT5ZLpPE3ia8nnubmjrVeP5ankze7JHzic5cWRYelVQKJxd5gJbRbrYNaRp0SQjQjfbW2sR8tuVLH7ndz7LCrneicC1jsTzAa6rA/640?wx_fmt=png&from=appmsg)

查杀图

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SohNH2JCU1xe6O18JJxnricJPepdf321t7dSiarNr2L8Sf8LzfPYwbhUsRrGAmXfMXPmRL17sMibEE6Wx4rf0icgucJIiayK6Kg2wx4/640?wx_fmt=png&from=appmsg)

![流程图.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Srt4OscgRibCmVfhb4WUkej1yZlIN2GicawUDxlxcBWDw9MwMEBXNcGmicvOpCqya3ELlLKfc5sIum0UiccCRH4BZqpgPHfIf3eHibU/640?wx_fmt=png&from=appmsg)

流程图

恶意驱动的签名者信息显示为“山西荣升源科贸有限公司”。从证书链的情况来看，该恶意驱动滥用了经微软交叉签名的第三方Verokey CA证书。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoEA9ibUAOTElQlxWucstcvlgq3bLgkuOtj6xARtUGzYTjgtwBEU4mXa8QgbB1Mkgdr9UYApB86gkXDjTcOqJ8XXFHsDxe3Ribfg/640?wx_fmt=png&from=appmsg)

![第三方Verokey CA证书.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoXmTKJV7Hpx7wy0Gx7YicugISplVlmgES1TyJhnDs9TMibLNNV4Nkb6V2nPGbNia5wlgdvXZHo1OvPvicRO0QyxlQpbmQEmg1DAec/640?wx_fmt=png&from=appmsg)

* 原始文件名: z\_driver.sys
* PDB Path: C:\Users\M\programs\out\z\_driver\x64\Release\z\_driver.pdb
* 签名者信息: 山西荣升源科贸有限公司

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpWb9F4Q5HXynZapnH4SUrFAEib7iaMo99Hyc7oPbibINY3icbpmAkU65xXRnNnMewia8gm5Ds24YouAohticWszbsjPialOLHh9r6KV0/640?wx_fmt=png&from=appmsg)

![云控C2.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SorAS8cJ7FYAXsdvosdVze0qnXztxNQLwMvIVxHAXdib0bU5ddfP3pKeq2F9s5ia5ELyAia409nQFaDeuSgiccqPWlp3yUCEYkVM3M/640?wx_fmt=png&from=appmsg)

攻击者在此次使用的一个域名ddd222[.]xyz曾在2019年被友商披露，该域名曾经属于独狼病毒所使用的云控C2，用于推广流氓软件。

***PART 0****1***

**恶意驱动**

恶意驱动加载后会生成UUID作为机器唯一标识，并记录操作系统版本，用于发送注册信息至攻击者云端：

http://tj.ddd222[.]xyz/tongji.php?os=10.0.19043&userid=ttt111&mac=9AAA47EDD009&ver=&xiezai=0&wb=&az=-4&uid=

随后会通过XOR解密和zlib解压从资源中提取出包含32位和64位两种模式的DLL 。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sptvwbp7zC9tDpddNOopC7bt1micbQOt76DfTsEeFvFKnX8CjVVqI2W8cWg1WGn5riaXDRJw3kPWjichoHtBx73fmNfu7ffW2kyR4/640?wx_fmt=png&from=appmsg)

![两种模式DLL.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Srfxkw4S1G8Sm2WvdWz33djsSqxO9kZmibibcPe6VDISd4CyPzcQwC7qh11J0eBoibfy5VNCYJWWsXvG4cZlNbXgc6ck8GoevrM7w/640?wx_fmt=png&from=appmsg)

PDB路径如下：

（1）C:\Users\M\programs\out\z\_driver\Release\dll32.pdb

（2）C:\Users\M\programs\out\z\_driver\x64\Release\dll64.pdb

该驱动通过FltRegisterFilter 和CmRegisterCallback注册多个回调来实现Rootkit功能。恶意驱动还会在Temp目录释放恶意DLL作为中间载荷，并通过rundll32.exe白进程加载，用于注入系统进程svchost.exe。

部分回调如下：

（1）拦截非信任进程对Temp目录下的wdscore.dll访问。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpxbVoTRHQCibnPOgzicfcKW6deryibV9CQqKkQy1RsMtzLPic71AFiblxOHnqibTn0uY9aCiaTTmPcrqEIRXZibyVQbWJpzTqnJpqDHgI/640?wx_fmt=png&from=appmsg)

![拦截非信任进程.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sqnlkbibm3c169v8hXXibaRJQbpkj5OhQ3abdXnvoPwSHicCATr4diahwRjQzicjHzNn6D9PMqxDjQRlJic2kianic8F7rdsyD6jEBYy4o/640?wx_fmt=png&from=appmsg)

（2）拦截驱动目录

该驱动本身在安装后会对Windows驱动目录进行加固。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SptcwoiahS3FkNo1km8x6NuWIwee9DpWo8tPqRlG2Msc9CCsawfIHaQdEibT86vpZ9naOaibtj9o33mc50aL6Anyg0t4CF72mBl8s/640?wx_fmt=png&from=appmsg)

![拦截驱动目录.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SpJTcwVl3BQRTboIuwLOiagVRpHTFDnz5fwviboyN0tHFjVSJa4zwmWFkF3re4ZXX6IWKjrwZ3ZIL7K86kv6iaT9lbzErGwpJye1c/640?wx_fmt=png&from=appmsg)

（3）拦截注册表访问实现版本控制

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Srssyboib8HO8ESKZl4C3qetHotlZl66dqwiaZrs8Vw4YfZxoN99gFmsxQJXSo41OVooFQ7bZKfUqmkxWibHTGdgoGbWNcL7dja0s/640?wx_fmt=png&from=appmsg)

![拦截注册表访问实现版本控制.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoWibVpFfhGrfjxWVCuRcojRqalKhgo5rvTd1iaPXRTrSoiaIlHfm4CTgTX68HibuaLo6N7LfdW7gyQib5jqiclvL4pDIMR3BcW6iaadk/640?wx_fmt=png&from=appmsg)

恶意驱动和中间载荷DLL都使用了自定义加密算法对字符串进行加密，部分字符串解密如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpCaUib79x0Kic3jQa5ibGwtpicGia02NMXiaYEGAkIS4Xic4qHE8yF7zosMextsaMHgiaTMshouxaeeLWLHaFuztx0eSqiag8GlMA5yDzE/640?wx_fmt=png&from=appmsg)

![符串解密.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrSia5F3vm9jYvhoicb0by3mqIq6XqUVhKnGbgdjL4P4ic1UKP9Qx4iaeZL3uG5icjfJZQZRoq1kPibRIO8feZxcVaxQ5gWXKyxHQ9Rc/640?wx_fmt=png&from=appmsg)

其中一个C2通信域名dwav.cose[.]space，此域名可与多个具备相似通信行为的恶意样本建立关联。该类样本用于加载恶意驱动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqznzRFGokyotWJByCgu8dnldYrjnxf2coUZNTW9qVOIbePrFBILlibHAqCAfwicybhxibP1ohAyYzLOYNr74R36mZsdibkXjpXbyo/640?wx_fmt=png&from=appmsg)

![该类样本.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SrA8DJsKvUluia4Niczu0NakByIcQ9qgtMpUcthNzd2vZUZibH55yAfBD6BvyZjVKlJCd88BX80XnrSdmrUoibT9ibwrphtibA6oAKPI/640?wx_fmt=png&from=appmsg)

![该类样本1.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sr1eBOQmAKVUa0ibHoK2eP65OsGn6Y1gEetYYWb9zogY6yatvVnrdicrTIXxCsGh5ibM195XtbhxdZPHsYAWN3NlQQfJybXWnsM7k/640?wx_fmt=png&from=appmsg)

***PART 0****2***

**Clinet.dat：功能齐全的DDoS客户端**

系统进程svchost.exe被注入后，会先从ww1.winc789[.]com/down/ttt111.txt拉取配置，随后从dy.winc789[.]com下载两个DDoS客户端：Clinet.dat和ccw.dat。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SqMJMsESvbUDgo9CiaumiatTnaLFRXwyAtaCZI0Evgb5Zjm65vlTXflDlaTHMORibZvpAIbQNFs03HsubVuKaRPpKPQFdTS0puIjo/640?wx_fmt=png&from=appmsg)

![Clinet.dat.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SoBfbNKcFwIljydo3unkicPgEE5eTnadQto4DEsa8XOud5LfsXE8ybBQTOoZlp8ChNOsYpzia82PUpRTTG9Fy6cvxcRFS2nuRvOU/640?wx_fmt=png&from=appmsg)

![ccw.dat.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sp2kUU8v8AJ2szkjylgdwKzvchVWdeWY6geib6GvKCEOmiaMCS6osSQicmiaQ6rMmvBeDG0khPCUs17eicI0y3l60909MibBwMzetUibg/640?wx_fmt=png&from=appmsg)

Clinet.dat系采用Go语言编写的DDoS客户端，文件大小为12MB，**其用途为从服务器接收DDoS攻击指令，且包含多种绕过网站防御的方法。**

根据硬编码的C2地址连接服务器接收指令。

* ww7.topwin10[.]com:53538
* 107.151.212[.]137:53539
* sss.jjycc[.]cc:55777

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01SqQgEMcTOu8Mn37vF1UXwqVqOhxTiak1NM6MCZAwAmN86Ys8KJ9b7mzIIbIVDdsj1cTV3qVGs3ChwsSicx1Qfvfk5TqoYD5VCVvs/640?wx_fmt=png&from=appmsg)

![接收指令.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Srvw5OjicDibunZIiakfaTAj73RzATwTd08WR2GkNkAT7DEibLPQ1ibOEDX7Ys35VKR0ibZ645ww5actCNcMmx6v3PFukgx6y0Wy9BTM/640?wx_fmt=png&from=appmsg)

![接收指令1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01SpryOht9HzNg332NbTgHr66rh6Sdiax5jEdxBJk3IGTWrz4dWqoSe56icedyOzHxZdm0aQ3NAWdTnhaEzd0ORGGzlZEbjC90r9y4/640?wx_fmt=png&from=appmsg)

**0****1**

**上线登录**

运行后请求建立TCP连接，随后进行登录和接收命令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Spfsmg8yEcNBM3DxibVObyz5icjs6D3AYOPgM6ecWnB2kybsyRhjDV1ouMDp0JumutdHjmnqsldVRT2ZmPGPwFgWYapyOr3QP6yE/640?wx_fmt=png&from=appmsg)

![接收命令.png](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sp5xPiaq7vukwepTc7YKm1QnP9ASYZoyd7mtTDqv5f7g8Fpz5FATcP0n8l00nJHTVFGhhabdHr5dyx4XEKj5Dr3Qia6ILmUruV7I/640?wx_fmt=png&from=appmsg)

登录认证通过简单发送3字节数据：0x6B, 0x6F, 0x6A (ASCII: ok\n)。

![](https://mmbiz.qpic.cn/mmbiz_png/u1Oy5xQ01Sq8jyYNVeoqsVDv0icWmiauNiaRLFibwYoHBskGxrdTbnX4SYz8KgrlzSTmYVUbzASAWb2vtaV7IyQC24a84QTK57xuq4GLeReCPCM/640?wx_fmt=png&from=appmsg)

![字节数据.png](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sqib6fgZFJMYfmT2DgtEVOXXxuX3v2ZISiaiaibzia9IzTicveQBE9u7GPdZmUwq33T4iaNHkYDveWK7SZOYous7JyEZGiaibRMZq3uhicH0/640?wx_fmt=png&from=appmsg)

**0****2**

**指令分发**

客户端收到服务器下发的’1337’心跳包刷新TCP连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/u1Oy5xQ01Sorcyoc5txgBatflMzNXhibOuxfeP1SVtNOibAVVB4icXERmBxJgsD4QKrq7WArk1KTIW4puuiaG3G1cUCqJFTEOejG76BWRGOJ7ng/640?w...