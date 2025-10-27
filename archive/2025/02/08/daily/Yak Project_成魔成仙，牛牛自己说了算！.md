---
title: 成魔成仙，牛牛自己说了算！
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527654&idx=1&sn=651b97b028d73e0fed91b82072c4373f&chksm=c2d11042f5a699543438737282a2a79b127dc6a9bd549c8c7062919f104b8505ee65d83fb1a3&scene=58&subscene=0#rd
source: Yak Project
date: 2025-02-08
fetch_date: 2025-10-06T20:38:38.915494
---

# 成魔成仙，牛牛自己说了算！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLl3JzwibMlYzLch2TR2bEyXJqqm290xKKSDlbVhuc3HHB318iaOh1hK8w/0?wx_fmt=jpeg)

# 成魔成仙，牛牛自己说了算！

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

我是YAK超级牛，

能抓包来能审计。

漏洞bug一眼有，

调试代码不喘气。

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZdbUQQ4XHENEjzic4cMLR2oX3yIkouebnBO9sPfJzU4PhGqvqGt190OduaaJl2RbmiatE1ILAQkiajCQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZd0VthLJpzgmAAibgKmOtuudic6NWfMSJWFgz2JwxI10Z4Qoxs5YLH3oibnffYlSbojWtzPDMOvPh2ZA/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLPqHdabyT4ibb1a3o31iaRibPgicurHxqcMxJAnMfYzMiarhP0ZJRbLEEtow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLibSth7QIrAVeEFPV2icux0V1zicBVNO3SbqJzZiaQOBtl2bVHAYT3OEyTA/640?wx_fmt=png&from=appmsg)

* 在java中，不一定是和php一样（只要有文件上传就一定有漏洞），比如springBoot中，条件限制非常多。
* 硬编码：在代码审计过程中，我们需要关注硬编码，有时会有意想不到的收获
* SCA：在java SCA中，某些依赖的版本可能会出现很多问题。(shiro)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLr2VdmmBpu8ia9kU7Lib8pAHKwwUe6jckKVte5fH4nek2dOO17xmiagJXg/640?wx_fmt=png&from=appmsg)

针对Shiro来说，Apache官方说是集成了鉴权和访问控制。Shiro的本质就是一个filter过滤器。filter过滤器需要关注两个点。

> 如何进行路径匹配？
>
> 如何进行权限鉴定和访问控制？
>
> 针对filter来说，我们重点关注两个方法。init和dofilter

### **init方法**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLorONTb1RUHLLCKzGAAcUlkaGOAdicsyvFlpWoAS1whIGCYl1kriavdtw/640?wx_fmt=png&from=appmsg)

> 这里进行了一个过滤器的配置。其实就是相当于从ini文件中获取到过滤的内容。

### **doFilter方法：**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLsQRQmcTI187FRkvibA0lZiaJVHMR0wpJjFRu61ot92nYMwTtYv7Vd1EA/640?wx_fmt=png&from=appmsg)

### **shiro过滤流程**

```
doFilter的流程：

（1）获取requestUri
（2）获取过滤链表
（3）根据过滤链表来进行过滤
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLzhwKbQGQxe8UEoWzh6om9MNbIj3bsaXXIRhIu2ec7iaibJkEwQfIsVOQ/640?wx_fmt=png&from=appmsg)

在这里可以看到不同的requestUri获取到的filterChain不同，而在getRequestUri中在normalize函数中处理的有问题，就造成了权限绕过。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLcvL2geibgvpALBLyUIV2hT6M4Hf4kh2MIzryiaFwCnszMP6ic3SHt1Lrw/640?wx_fmt=png&from=appmsg)

可以从github中获取该系统源码，然后进行编译。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLvRL5tNpibicXAVBEeBNsUaCXeiciaW4YShAtwQTbJZ4SEwILmTXv9NxJpw/640?wx_fmt=png&from=appmsg)

### **shiro权限绕过**

经过代码扫描后，发现shiro的版本是1.4.0，处于权限绕过的版本中，进行尝试利用。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLjQaBeHicU4Xr69dYeOEGUic0L1jD2n3mVpicb6ibmeeCNlYmON1Y2snkgA/640?wx_fmt=png&from=appmsg)

这里先查看properties中shiro配置是如何进行定义。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLf4Y1jkB3X2j87frKxzdTRSuncXCzeE16kJJbVR13oKfduOECG9ibzxw/640?wx_fmt=png&from=appmsg)

**正常请求 & 权限绕过**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntL9gKI9iavyYkicQaxSDatqkhDxD7dAMGTDbIqJpiaQkShYXeL4icVPHWWGw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLKCoAdqvxC4MvHn3NjIhD2CsuuqTlVKCeZXhjKamC4VoUFUrjznK9Tg/640?wx_fmt=png&from=appmsg)

### **任意文件删除**

写出这样的一条syntaxFlow规则，含义如下：

（1）找到所有的delete并且条件为：object的全限定名是**java.io.file**作为一个source

（2）在syntaxflow向上寻找的路径中，opcode是param，并且function的注解中有 **RequestMapping||GetMapping||PostMapping**

```
delete?{*<getObject><fullTypeName>?{have: "java.io.File"}} as $source
$source<getObject> as $File$File #{include: <<<CODE*?{opcode: param && *<getFunc>.annotation?{.RequestMapping || .GetMapping || .PostMapping}}CODE}-> as $sink
/*File file = new File(xxx)File.delete()*/
```

在文件删除的过程中，向上寻找的路径中包含param，并且func中含有**RequestMapping、getMapping、postMapping**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLbNPnCneBSVnia2INuR2VCfNSWic3TNGqw2iaqmNa0NziaIUGqxROjZ1AnQ/640?wx_fmt=png&from=appmsg)

找到三个调用点，这里找到调用点之后，直接将传入的内容，进行拼接，然后进行了文件删除。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLz4YdqWyeEUUia3ajuqVd0SFRxFBJaIvWhBswicLl14W84U0iaUnJySUCg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntL7yJt73bRk2FdbVv3szocD45jSkRzrFO92EORGr3tbMwwcMc2QeWxVw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLYQllMKQuZsJY6UxJNFh7qibezZ7hn5eBXmic5LFB38BC9YMicn3ceUdgw/640?wx_fmt=png&from=appmsg)

### **任意文件读取**

```
readBytes?{<getObject><fullTypeName>?{have: "cn.hutool.core.io"}} as $source
$source(* #{    include: <<<CODE*?{opcode: param && *<getFunc>.annotation?{.RequestMapping || .GetMapping || .PostMapping}}CODE}-> as $sink)
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLrGHEte1lkMkffpu6yT5mA6Z5MKOzKtpCugibc69yTAuyibYNHvf27MxA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLOl9qCDBKPDnRp8SQ5aCVfnM1SHCcdau2VnPOA3ax5mBf9vJgUkcmyQ/640?wx_fmt=png&from=appmsg)

### **多处Xss：**

这里写一条syntaxflow规则，大致含义如下：

（1）找到serviceImpl中所有的func，这些func名称中含有add、save、update

（2）找到所有save、update 的object名称中含有ServiceImpl/Service

（3）找到这些函数调用点，并且函数参数向上找的过程中，annotation中含有requestmapping.....

```
/save|update/?{<getObject>?{any: "ServiceImpl","Service"}} as $source1
*ServiceImpl.*?{opcode: func} as $source2
$source1 + $source2 as $source
$source()?{any: "add","save","update"} as $target
$target<getFunc()> as $targetFunc
$targetFunc(* #{     include: <<<CODE*?{opcode: param && *<getFunc>.annotation?{.RequestMapping || .GetMapping || .PostMapping}}CODE,}-> as $sink)
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLy6xucyICHAibXqk26LQMxT2LPiaQFVnHqBsicPia0e0ia3FmT40QqCt3bHQ/640?wx_fmt=png&from=appmsg)

#### **Tip：**

这里看了几处，如果是权限绕过的话，session中不存在用户，那么基本上不能使用添加的功能。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLtDhcLk1fO8UBI3fZia07CNBxK4GepqGjHWuao24b7YYxwRiaVTLL2lWA/640?wx_fmt=png&from=appmsg)

找到一处添加商品功能，可以发送payload对此处进行利用。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntL0GDNcKBvoeVbfOuoxaM0M9QtdwicaWviaKgEbG3qRH1icrwOzbIYaiaxZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLOJicFwerWnMZ1Bw04XOUmlUMzgXK2n5MyD4oT4kzibIo2thxSUeBCuUw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntL5x5NibD3mpRZiclnWQcabCTCgxQ2eOJeLKQUV1hGrMcRp9fSaygHVZeA/640?wx_fmt=png&from=appmsg)

### **其他思路：**

* 在扫描过程中，其实还找到多处的文件上传的利用，但奈何是利用date作为路径名称，虽然有修改文件名的功能，但是限制太大。
* 此项目为热部署，并且使用的是thymeleaf作为模板，如果能控制到html/jar，可以通过thymeleaf来执行命令RCE。

### **演示视频：**

我们都将其作为一个规则组

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZclfsDaLHF9DKwIZM7Y4ntLpg6Zx4ia3bkiabRTulQjAHPeql6eXOtqs1s3rb00H8ctkxpo4l5iaqp0Q/640?wx_fmt=png&from=appmsg)

**END**

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

Yak Project

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZf3Jgic3A1naPbMWx6iaVCOHr8IyqePqDq1X4nJWqOEhuEjp8lwY18DgujicOSoysibVxFwRsMjUkQyYQ/0?wx_fmt=png)

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