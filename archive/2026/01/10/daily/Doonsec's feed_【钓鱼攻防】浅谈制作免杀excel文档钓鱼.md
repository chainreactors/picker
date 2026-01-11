---
title: 【钓鱼攻防】浅谈制作免杀excel文档钓鱼
url: https://mp.weixin.qq.com/s/9tKAq_76r9yXCeHPr92LlQ
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:36:50.377600
---

# 【钓鱼攻防】浅谈制作免杀excel文档钓鱼

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/v94hWOZcBpxf5ujLrIwurOt7k2PHrAOyJRyhBDFQeYrKic1DL3rEpMA4MVpqqVzP47D8x11X9kOUicOre8VIwgXQ/0?wx_fmt=jpeg)

# 【钓鱼攻防】浅谈制作免杀excel文档钓鱼

原创

平凡安全

平凡安全

![]()

在小说阅读器中沉浸阅读

**「上班让人感到最可怕的地方是，它居然让我因为盼着退休而期待衰老，而不是好好珍惜剩余人生里最年轻的每一天。」**

## **「前言」**

网络安全技术学习，承认⾃⼰的弱点不是丑事，只有对原理了然于⼼，才能突破更多的限制。

拥有快速学习能力的安全研究员，是不能有短板的，有的只能是大量的标准板和几块长板。

知识⾯，决定看到的攻击⾯有多⼴；知识链，决定发动的杀伤链有多深。

## **「1、CSV注入之RCE」**

CSV公式注入(CSV Injection)是一种会造成巨大影响的攻击向量，攻击这可以向Excel文件中注入可以输出或以CSV文件读取的恶意攻击载荷，当用户打开Excel文件时，文件会从CSV描述转变为原始的Excel格式，包括Excel提供的所有动态功能，在这个过程中，CSV中的所有Excel公式都会执行，当该函数有合法意图时，很易被滥用并允许恶意代码执行。

在Office的"文件->选项->信任中心"处开启"启用动态数据交换服务器启动"功能：

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibkse2lXBxQNicuPC7w1ibZldqsiaWsDOAEdc4Buiar4tfo4qHDe4vI546icRNQ/640?wx_fmt=png&from=appmsg)

之后构造以下恶意载荷：

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksMJJ1bu1nwcvyUWIGRq4xmNXIfwptnAALAPZeVbTX3nRl9J1gOSfia8Q/640?wx_fmt=png&from=appmsg)

之后模拟用户打开Excel文件：点击更新

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksgicTlUKg4q628QRZAs19ZjMZNGyCHUASnTBVRaEC10dQQ5G4ficHJnOQ/640?wx_fmt=png&from=appmsg)

点击是

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksiatQd2MbvuAmBGZg7vSXJ5sInPJG2WbRGCFzAugeLY166Tmo8TIxRcg/640?wx_fmt=png&from=appmsg)

成功执行攻击载荷弹出计算器

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksgSqGcs9wj5P15zb9zicdb5d7o7CzzcgHBDtOa695r3k2g97DzuiaL6NA/640?wx_fmt=png&from=appmsg)

反弹Shell

这里使用cs框架来实施攻击：

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksamMwItWNoTJShZSV25Bd3vvdXPC2W4eIdh6D7bRlc1P15r9kwJ2tNw/640?wx_fmt=png&from=appmsg)

选择配置

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksHTVYW1tibKVGpnZ1aR3QPQLXYrolhdn1YplY875JScQjiaUFFdww7Jbg/640?wx_fmt=png&from=appmsg)

使用文件下载功能

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksaQEDlEaCoZOc249qzWKm3nsS0xPnicFchSLcg977cPr7VibTsG33mUHA/640?wx_fmt=png&from=appmsg)

选择刚才生成的木马

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksHRCMhTfkRSoYRtT561qL7nqWlEsSIGb5kvsNml13Bydic88UibAGV0ow/640?wx_fmt=png&from=appmsg)

构造恶意链接

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksicZKMeGHp1wFVjrCkibhvnPpS10SEfyrvtA4BdaGYjdvNE44hhYzjeLg/640?wx_fmt=png&from=appmsg)

之后在Excel中插入恶意载荷

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksBIvia9qncOZ8u0txd9nlsuF0eWLWUn7dTzgYjQDib0Z5pGPTPcZO8T3g/640?wx_fmt=png&from=appmsg)

发送给目标用户打开，点击更新

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksqP3EibSgMG4VxroL2PIPwuk8uzjNibic4NC0O2GxUqIMVmtLDzODbtpeQ/640?wx_fmt=png&from=appmsg)

点击是

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibkspqliaNfGwJK3V1Lzk1pbxXqNweUib5fRVVNhDF33BTwE2ibQqhyfq0keg/640?wx_fmt=png&from=appmsg)

成功上线cs

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibks6KABKiactMPsB94VPKBeibibZx5ZMSMNEdtsqJDxiaOy6jBnGAUwbdSsbw/640?wx_fmt=png&from=appmsg)

CSV注入时常出现在数据导出功能部分，例如：将当前表格数据导出到Excel，此时攻击者可以在当前表格中插入恶意代码，之后当用户导出当前表格数据并保存为Excel，再次打开Excel时便会导致恶意载荷执行，同时CSV注入也可以用于钓鱼，攻击者可以精心构造一个富含大量数据的Excel并插入恶意代码，诱导受害者用户访问并查看，从而触发恶意代码~

## **「2、IQY特性钓鱼」**

可以将IYQ简单的理解成内置在excel中的一种特殊‘web浏览器’（不能加载脚本），通过IQY【即web查询】语句，可以直接将各类web上的列表数据轻松引入到当前的excel中，而正是因为这样，从而给了我们利用excel制作钓鱼邮件的机会，假如你要引入的web数据是入侵者事先准备好的一段payload iqy恶意代码，那结果就不言而喻了。

利用过程：

新建一个excel文件，找到"数据"-->"自网站"-->"地址"，填写要抓取数据的网站url，选中想抓取数据的表单

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksNpe8XAR9axuiczEeMm5TEolV0qfia0P2j0Cwelmk9FAa4u7wGspsawibQ/640?wx_fmt=png&from=appmsg)

在我们自己的服务器的网站目录下放一个rdyx0.html文件，内容是IYQ代码

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksYPoWpaAFb9xpicgcSWZ3MZlic2awGymtRPWnmMoqiaceKrGaLsfrVxASg/640?wx_fmt=png&from=appmsg)

填写网站url为：

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibkszreNTp4jCicOiaI1wJR3xia5NrAibR42tH4cgYyHgNzu4rT8wjlCsQdbPQ/640?wx_fmt=png&from=appmsg)

点击确定

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksOVWkshfNpkVm5WtluwR0ksXicTia5MIwp2ZMFlUBGZbHzqwTRKDjCwPA/640?wx_fmt=png&from=appmsg)

点击是

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksfdFpwUQPgouPyiaibh4sAWUR8thdvWr9nYVEte1ib3aLBVm3Z1SuEtCPQ/640?wx_fmt=png&from=appmsg)

发送给用户，点击启用内容

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksiam3iaen3ntkPqniah5O6XCyUNHdS2WybofkLic6XFqt2jf1w6icb10w27g/640?wx_fmt=png&from=appmsg)

点击是

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksBSDvTLyFWbrlvT22eicESdrZwRYA2suXGJH3oqNmwg22oXXgoTFJ4xg/640?wx_fmt=png&from=appmsg)

成功上线cs

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibkswL4TpdL9z9TuVfnUIOXsXs4JLwC6G6icQg0QFWM6LiaT4ppqp4ibuyWeg/640?wx_fmt=png&from=appmsg)

## **「3、制作基本的excel宏文件」**

Cobalt Strike生成宏代码

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksP3cTR5ukcAvsnVgibYeBE1guTQl29yjTd8ROku0uvukPoPCBc3w7zug/640?wx_fmt=png&from=appmsg)

选择监听器

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksYq5ibGZqUX3Xo1TZlM6ZhnsqjJjIHuJ8V6zCxpibxqBCIOcka7Ria9XvQ/640?wx_fmt=png&from=appmsg)

成功生成宏文件

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksiajktEp66ApMtwmlBXwibQlhxmEVU0KIc6K11C20ib5mXRIJPLYEHFnbw/640?wx_fmt=png&from=appmsg)

新建excel文档，点击视图——宏——查看宏

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksRRrspjmKxHUJ9b6ptHah6WWOxS1h5VeEADYWHNm5plmiaK80vK5OtDA/640?wx_fmt=png&from=appmsg)

选择创建

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksVjNCmDERIh2hx44xqkWWZL4CHr3yrmxA9eU8IaKCjCVky8x6Gxms9w/640?wx_fmt=png&from=appmsg)

选择本文件中ThisWorkbook，将cs生成的文件复制到里面

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksJQEahTRPibd2XpAdWUicrFtHkvibuTdibribG96SmDNWDNl4aMcj1edehWg/640?wx_fmt=png&from=appmsg)

点击否

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksxB0IFDa2wWfvLzA8Iv9sSsqyTeHE65ktibJa7eS9Bp35ia3iaibtQ767mg/640?wx_fmt=png&from=appmsg)

保存为xlsm后缀的文件

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksuK57NqZtV0OTI2ONfA9BcytYpJ1YyqscAklgsJl0W7cHIy7ic5bO1IQ/640?wx_fmt=png&from=appmsg)

打开文件后，点击启用内容

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksyIK9AM4IFXs8KgUdFbkYwslOyYoqaLqRmLFh8lh3u8icBGH5fP9zvow/640?wx_fmt=png&from=appmsg)

cs上线

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksUwQOAjjMqQcxW9DMXJpbmltSVAeyguuyzeRarkva8wWmhhdiarib1xuQ/640?wx_fmt=png&from=appmsg)

## **「4、宏免杀（hot-manchego的使用）」**

### **「4.1 为什么钓鱼附件进不了收件箱」**

随着类似msf,Cobalt Strike工具的出现，钓鱼邮件的制作成本大大降低了。但随之的问题也出现了，因为工具一般是写死的，无法定制化恶意执行代码，导致恶意代码的特征值很容易被抓取，会被发件服务器，收件邮件网关，本地杀毒等一系列防护设备或措施拦截。所以为了邮件能进收件箱，要搞清楚我们的钓鱼邮件在哪一个步骤挂掉了。一般常见的邮件流程如下：

邮件→邮件服务器→防毒→防垃圾→收件箱

### **「4.2 如何进行免杀」**

要搞清楚我们的附件在什么环节被杀了，首先科普一下当下杀软的三种查杀方式：1.静态查杀 2.云查杀 3.行为查杀。邮件服务器为了可用性和隐私性一般只有静态查杀。所以我们只需要规避特征值绕过静态查杀就可以让钓鱼附件进入收件箱了。如何规避静态查杀？最好的办法当然是自己写恶意代码，但大部分云黑客都是脚本小子，这也没关系，现在github上也有很多免杀开源的脚本。这里以hot-manchego作为演示

编译成exe文件

### **「4.3 hot-manchego的使用」**

下载hot-manchego脚本，并运行

这里我们需要将cs生成的宏写入vba脚本

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibks6CE90sic8FNDLUOgIZfvZ9gXzY4kHtJ2kcHFGqF6PiaHwBaM42dGoRVw/640?wx_fmt=png&from=appmsg)

运行hot-manchego，会生成rdyx0.xlsm文档

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksXvHiceymHODNx0CBQunIQEiab5micIEUibPSXpeJbABTxukmGuCmOmUAEA/640?wx_fmt=png&from=appmsg)

手动添加宏报毒

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksqj3d5ibKdGgUDlpQPJMnTicfYfa2UCvywJU8cia4vnSk6euvk9x4uQFFw/640?wx_fmt=png&from=appmsg)

免杀后静态过360和火绒

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibksk8GpUvF4dZxo65TE2GveT8WukOia3wBdfhJVfwt0bDPHmMmGqMnZaTg/640?wx_fmt=png&from=appmsg)

点击启用内容

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibks40NiblugegKdZFI31JicbSTgSk26mKnyts558GGFIwpRhtciciafEhmjicQ/640?wx_fmt=png&from=appmsg)

动态过360和火绒免杀，且不会提醒启用宏

![](https://mmbiz.qpic.cn/mmbiz_png/v94hWOZcBpxsquyvyBEa5cIU3ER29ibkszBlK4xmBrLXQN6ckamKegvEZibibGm...