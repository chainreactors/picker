---
title: 实战 | 记一次邮件系统C段引发的SQL手注和内网渗透
url: https://buaq.net/go-137455.html
source: unSafe.sh - 不安全
date: 2022-11-28
fetch_date: 2025-10-03T23:54:50.428427
---

# 实战 | 记一次邮件系统C段引发的SQL手注和内网渗透

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f17f640e2777aa438a3cc0734b291f81.jpg)

实战 | 记一次邮件系统C段引发的SQL手注和内网渗透

闲来无事，日个站玩玩。要日，就日一波大的。日个小站就结束了也不太好意思（水文章），于是乎就在各种搜索引擎上搜了起来。于是一家叫做 xx 报系的邮件系统吸引起了我的注意力，看样子很好日（？），话不多说，
*2022-11-27 14:42:31
Author: [mp.weixin.qq.com(查看原文)](/jump-137455.htm)
阅读量:63
收藏*

---

闲来无事，日个站玩玩。

要日，就日一波大的。日个小站就结束了也不太好意思（水文章），于是乎就在各种搜索引擎上搜了起来。

于是一家叫做 xx 报系的邮件系统吸引起了我的注意力，看样子很好日（？），话不多说，开整！

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tWYGBMAdKOoXGfd3ILf86oORSj8VMK5tyfd5hsUg7qCAU7tWEUebwibQ/640?wx_fmt=png)

直接对 `https://mail.xxxgroup.com/`，直接对根域名进行一个子域名的探测，上 fofa 或者 hunter 这类东西搜一下，结果并不多，只有 44 条

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tNykZfYib8aSvQBJnmPrEmjJwvDJ9pQBuUhlWAnpu9FEuIeCpQ5JIqEg/640?wx_fmt=png)

但是里面的系统很有意思，

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t5lSIsp7sXcCorITejLfcUJ0L3zZVDeRWBJCUGQsDpxEU3leqm9uVicA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tZCvphP7aXoYodsIp13Tk29U1hpQpt1ub2kBu0j5GBM24dLtrUC22XA/640?wx_fmt=png)

有很多这种没有验证码直接登录的站点。随手试了试 admin/123456 这类超级超级弱口令，没有结果，后台挂着 xray，注入什么也挂着，都没有什么结果。dirsearch 扫了目录，也没有什么结果（指不能 getshell），端口也扫了，都没啥结果，常规的手段都试过了。供应链看样子也没什么可以打的，估计都是自己开发的

同时还有 gitlab，但是并没有什么洞

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7ttLO3Ddtiap2TMudIaPCYj22D2T6NF7aPWicxia8VEWMKqZ9IMic22ZHXQA/640?wx_fmt=png)从 hunter 上的这个域名来看，确实搜不到什么信息。虽然此时可以开始进行一个弱口令爆破，但是不急，一般我回选择把这种有针对性的爆破放到最后做，因为这个步骤流量太大了，十分显眼，并且我们现在也没有合适的用户名字典。

继续把目光看向刚刚的搜索结果，这些结果中，我们可以发现，大多数的站点都处于

* 124.9.11.x
* 124.9.2.x

当中，我们非常有理由他们可能持有这几个 C 段，这几个 C 段上肯定有他们的其他资产信息，上 goby 直接在外网进行一个扫

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t2m79iaSWhfH0WICnfx2oYx1m9tB6347QRVA8iapu2Tut7eTibV2jxnhHg/640?wx_fmt=png)C 段内发现了一堆 zyxel 设备和一个 outllook 的 owa，试了试 Nday，并没有什么结果

但是额外发现了一个看上去有用的论坛系统 vBulletin 3.7.1

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t5naEPBXCvveD4akaibzRyYSjsPKO035kBicrYSkCAIeQ8ExwomxhicNSA/640?wx_fmt=png)并没有什么 Nday，但是可以进行一个注册，注册后可以浏览系统已注册的用户名，然而看不到邮箱。

但是至少给我们的用户名字典（如果有需要的话），增加了一些信息，然而可惜的是注册还没五分钟我的账号就被删除并且被 T 了出来。没截到图，为了不打草惊蛇所以先 pass。

换个思路，直接用 hunter，对他们企业名字进行搜索

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tWnZ5ANaJYoicQFCKlRibBPnsC58Rkdl1Tv6XmzO8EGgs7vEC3ncsDfYA/640?wx_fmt=png)

资产多了起来，但是也多了很多不想干的内容，此时，我发现了一个东西 `https://insightx.xxxmembers.cloud/`。

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t86YvRF0zz0vleicaCXo6aXArFNibia4Us4ceCeDVfr9v3KttznggZic5Pg/640?wx_fmt=png)

他们使用 sso 的登录，用的是之前 xxxgroup.com 的 sso，并且根据域名，感觉像是内部使用的一个域名，并不像是对外商用的，立刻进行一波子域名搜索。上 oneforall，和 hunter 辅助查询，只查到了另外一个域名 `https://datahub.xxxmembers.cloud/`。

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t7cgulOREdNx0mMKaK7lCW82A2B1vFfLv9vC4ibM5Yia1yib803xXmscng/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tELCjAYTIIYuVJia7kiaB3SPZJK5CCs48SCpH3kHxD6TMxZFVgkGpAVsA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tibaFVxJvknLXte9ht1RqiaKq1ZTI1VXRGHlqcLv26iaQG7s9u12e0jHgw/640?wx_fmt=png)

果然，不知提供了 API，甚至提供了 SQL 语句，我严重怀疑这里是不是有注入，正当我兴高采烈的访问的时候。

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7ttAppbxnAq74nxhOcOYXNicOTefs6ic4ylQKibI6HicwE44XhCjThlKheyg/640?wx_fmt=png)。。。。。没事了，但是我还是不甘心，对着目录搜索了一通，

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tgEHZhFC4oic53HZ9pugTzty45FWic0k4QQSgLqURsbIRGCXEkvZicuVyw/640?wx_fmt=png)看到了个 login.jsp，直接对着源码进行一个的看，看到了一堆未授权的页面，但是都是测试页面，继续 pass

此时已经开始有点心灰意冷了，打开了 github，打算开始，啊传统艺能弱口令和数据泄露，甚至看到了这东西

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7twm1rvvaflNVBTSV4vEeXUdC25SrwQTe2GicUJm5tFt7YpJj5V3jg9Mw/640?wx_fmt=png)这不是想睡觉了正好有人给我送枕头吗？整直接准备拿着这份表进行爆破的时候，我发现了它

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tDibVWZ7r7juXLsdAHu5oqg28c1Bpvj4QeNPwe3dcwBL8Z4kxHic6jqpw/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tpNFgXp0qTIX6Fhb5ALT1NoKJcQo8NKbqyLXvT4dgYyyj3KbAotib8dQ/640?wx_fmt=png)

一个完全孤立于其他站点的，甚至除了图片素材没有其他信息有关我们目标的站。

当时我已经心灰意冷了，挂着 xray，于是乎随手试了试 admin/admin，test/test 之类的，然后就去上了个厕所吃了个饭打了把游戏摸了会鱼跑回来（？？？？？），没啥信息，但是我良好的习惯让我随手输了 admin'，报错了

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tFVhzvSHiaiaj66oGnaQseQHxOCAwibfZAcEibvR0nhwjtGUD8T61cOAPyg/640?wx_fmt=png)我：？？？？？？，再次检查了下 xray report。没有啥信息，其实我挂 xray 主要就是用来被动检测 sql 的，不然我也不会挂这东西，流量太大了，但是 xray 的被动扫描 sql 注入确实好用

然而这么明显的报错注入没扫描出来？就十分的神奇，直接套上 sqlmap，结果都是 timeout，换了代理 UA 啥的都不行，怪不得 xray 扫不出来。

于是乎愉快的上了 burp 中转，终于跑起来了

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t8WE9MhWS3473Pfkv9gYZDJIXtMaib6ictLonNQlI5pibTOreKMwjGKCUA/640?wx_fmt=png)但是他只抛出了 timebased 注入，甚至使用 os-shell 还没有回显。

一开始我以为不能堆叠注入，使用 `a';select 1 where 1='a'--`，是不报错的。甚至直接绕过了登陆验证

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t7UM79vmJ2jfeYMibALlHpibHSfa79gkAMlamu5BDro7kbGn9dicWtibOQg/640?wx_fmt=png)

但是如果你再堆叠的第二行语句输入错误的语法，它还是会检查语法正确性的 `a';select asdasdasd--`

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tYUSQibIxOsz1EHNgJpk59aCicfDDVWGhcgllwhekHTEzSnIIYZiagNApA/640?wx_fmt=png)这时候直接进行一个基本信息的看，`select @@version`

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t0cs3KqJ7o6CXlzotHuNuT7kqibog4ZTXhdGmrzSIpuvYUsXKIWeMJYg/640?wx_fmt=png)我看了看这个 `Windows NT 5.0 (Build 2195: Service Pack 4)`，人麻了，这不是 windows 2000 吗？？

再看了看这个 WEB 的 IIS 8.5，怎么也不相信一个 windows 2000 的机器能跑的动 IIS 8.5，得了，站库分离

想着先注入密码进后台看看先，直接使用万能密码绕过，会出现没权限的问题。

我以为是用户名的问题，可能后续的语句验证了用户名？反正它给了完整 SQL 语句 `select ID from ACCOUNT with (NOLOCK) wheree xxxxx`
，直接用这个对它的语句进行一个用户名的搜索 `a' and 1=(select top 1 ID from ACCOUNT)--`

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t0QhvuMREibM2RDDg7zOMYPACzgxATMl6zicrhE6DLjfXOU5puG8GH2QQ/640?wx_fmt=jpeg)??? 怎么还有人用 `当用户名的。继续万能密码，依旧无权限。我想这可能是这个用户没权限，毕竟哪有人拿` 当用户名的，使用 `a' and 1=(select top 1 ID from ACCOUNT where ID NOT IN (select top 1 ID from ACCOUNT))--`,

接下来查出了个中文用户名，绕过失败，我不信邪，密码，注！

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7t9Mx7KDqyFQPwtjlWKJrAzjRMa2oRndiaDQq0QVFUXbIjYXPqjSA7FvQ/640?wx_fmt=jpeg)人麻了这是什么 hash？好在这个 sql 注入把我们的密码也编码进去了，我随便输入个密码 123456,它语句里我的密码是

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7twam6lOZOzibcQiacMwegeYUQlyTWiaFLG3btwE6DaqRlxlbE7lyVBcUicg/640?wx_fmt=jpeg)十分的规律，一眼顶针，鉴定为 ASCII 凯撒。看了一下，6 位为一个字，前面 6 为 000079 是固定不用管，直接和原本的 ascii 进行相减，知道了密码是 ascii+42，好的，前面 000xxx 知道是什么了，后面的-xxx-xxx 又是什么呢？

看到了中文名，啊，想了下也许是 UNICODE，试了试，好的成了，没事了。验证通过

*就是依旧没有权限进入系统！！！！！！*

我那个气，开始直接注数据库

首先看了下，确定数据库确实有 DBA，使用了 os-shell，whoami 这些都没有结果，但是，ping，dnslog 有回显

确确实实的有回显！！！！！！

这时候，啊，就是考虑传马上去了，首先先探测网络环境，因为 sqlmap 查出来的是 timebased，所以想着可不可以用远程下载

思考 windows 2000 有没有什么东西能远程下载，为此特地装了个 windows 2000 的虚拟机

certutil 肯定是没有的，但是有 ftp 和 hh.exe。直接运行了 hh.exe 上去，发现我服务器并没有 web 请求，冷汗流了下来。

由于堆叠注入实在是没有回显，我真的很怀疑这个 dnslog 的回显到底是不是真的。我心里此时想到了一个很可怕的 BT 防御手法

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tVaYAiaiaXxaLmmnHZqbxaN4gr1kEaoqhadiccQtJiaQkmIoGMKXVmT5DFA/640?wx_fmt=jpeg)世界上怎么会有这么坏的人，气抖冷。

然后使用 sqlmap 自带的上传，，上传的速度过于捉急。经过 powershell 写过一轮，vbs 写过一轮，debug 写过一轮。。。。

太慢了，最后还是选择抛弃了 sqlmap。进行手注入

首先先试着看看能不能读到回显。

使用语句 `a';drop table ccc99;create table ccc99 (dir nvarchar(4000));insert into ccc99(dir) exec master..xp_cmdshell 'whoami';--`

然后用报错注入 `a' and 1=convert(int,(select top 1 * from ccc99))--`，发现并没有回显，心灰意冷百思不得其解，于是乎我在本地试了一下 whoami，发现 windows 2000 并没有 whoami 命令，啊这，得了，没事了。

继续，随手执行了个 dir

![](https://mmbiz.qpic.cn/mmbiz_png/Uq8QfeuvouibE09h8mjGkZnvcCdcutC7tGXNs4Jh7LCUlvvZvtjYZpoOkmQcAJJUnia8nM81YGvwzEAgCw9LjvAw/640?wx_fmt=png)ohhhhhhhh，这玩意是...