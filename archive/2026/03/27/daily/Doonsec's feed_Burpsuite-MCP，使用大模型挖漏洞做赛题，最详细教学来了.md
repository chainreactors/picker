---
title: Burpsuite-MCP，使用大模型挖漏洞做赛题，最详细教学来了
url: https://mp.weixin.qq.com/s/FYOdgoWKCIrGWMO4CZja_A
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:14:36.750278
---

# Burpsuite-MCP，使用大模型挖漏洞做赛题，最详细教学来了

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ptxZESUjfTETjo9c3STWe7h6AXERDBLQfvnPm15hfqhUXMkI5OzDibh71tf6531Kbj8usOEUM3RMCQum10SS9LGcl8ic7qianEA6THicWYnF84c/0?wx_fmt=jpeg)

# Burpsuite-MCP，使用大模型挖漏洞做赛题，最详细教学来了

原创

【白】
【白】

白安全组

![]()

在小说阅读器中沉浸阅读

# 前言

burp接入了MCP模块，简要概述核心作用就是用目前带有智能体的工具，调用burp进行各种控制。

我们可以使用大模型帮助我们分析数据包，寻找当前的漏洞和检测部分CTF类型题目实测下来还是不错的，现在直接讲解比较稳妥的安装使用方式。

# 正文

## 一、工具准备

```
1、Cursor2、BurpSuite较新版本3、burp的mcp插件
```

拓展下载直接到官方插件中心即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTH3Ny4X8icrVoM1Ay5JQzyZdPtsJMibhoBxbGd2JzicxG7Uqa6snjRYze97icsvL0OmkjZWweI42kaZCTgnGf88kJsvKQOv1CVAnoY/640?wx_fmt=png&from=appmsg)

安装好之后直接在上面栏目中就打开了，这里不需要配置什么东西，然后我们下载cursor

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTG1SDHEwqqxLFhy4WulUzk8icBpNkx3GQY35MgrQsYEIyojPpP2XOFOc8Gic4X4sJ3QX4hvIYWWPlYuy3hLUXKnACwDcOEmPpPicw/640?wx_fmt=png&from=appmsg)

下载地址：

```
https://cursor.com/
```

下载好之后开始我们的配置工作，有不少教程会让大家使用其他的工具，比如Cherry Studio这些，这个就会出现报错，所以我这里研究了官方文档之后，使用了cursor使用稳妥一些的联动方式。】

## 二、配置联动

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTGKwDWwcwdJIfHaMQ3w7wCpGNdQuntKyexU0ycyhiaXSq39HeIfWSoYgABjlPIicgAFEwYwrwjONSU5oibjuKElFudT9bC5Fia3Cyw/640?wx_fmt=png&from=appmsg)

进入cursor的设置，然后点击左边的MCP栏目

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTEgHKJIZILTn3KuJK3h82K0Hr0Vj4Dxvp1N5UzJIbLkMEG3GRBvkyJpHsWfBQp4cSgOLktrbribNOQMdFriau0xJG48pPLrOcr2c/640?wx_fmt=png&from=appmsg)

新建mcp服务

这里我们填写内容，填写之前我们到bp中下载一个Java文件

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTEXLbIeZW7TSPLl2pltYz9GNhM8DWQQu45LSZzF0OAHn44d1icISJXuFAEblCkyEfiaffp55MF6oT03BjjZawicGSh2ZRiaopjKe2U/640?wx_fmt=png&from=appmsg)

把这个Java文件放到一个文件夹中，路径不要有中文，然后我们复制路径放入下面的json中

```
{
  "mcpServers": {
    "burp": {
      "command": "C:\\Program Files\\Common Files\\Oracle\\Java\\javapath\\java.exe",
      "args": [
        "-jar",
        "D:\\mcp-proxy.jar",
        "--sse-url",
        "http://127.0.0.1:9876"
      ]
    }
  }
}
```

然后上面是我们的Java路径，这两个路径都不能有中文，然后中间的斜杠一定是双斜杠，不然都会报错

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTG9soDaBSRmJZurxxkTCiayA3jQQiaYvywbItzKDkCnCuFibyYPCdyNG3pGMlicMk3BxzjSrolze5Q0xCgdTj1ZicbEE9Owo2JICic4E/640?wx_fmt=png&from=appmsg)

不知道Java路径的可以用where Java命令查询

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFZTFzTav1ZIQNhHZpcicdcPdicXaC6N7rZEspW9wgqJcOMePduS8OnSQkFg5gHYRrzKB7Vk5MQvHT65Sia0AxgVnQs5GTbMNbMjI/640?wx_fmt=png&from=appmsg)

然后我们保存回到上一个目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ptxZESUjfTHj3P9iasMyrom34ialiayHUW25VOfFfahTdBWyIBKxtPdMgaagicJDvssMrtauIWA09s6CPExaGQlkPTCQCib22MGdicv3qg5ppyJ6s/640?wx_fmt=png&from=appmsg)

点击开启之后左边是绿色小圆点就是启动正常，否则会有一些问题。

## 三、使用与测试

我们使用就可以直接在左边对话，让他调用burp访问百度，这个时候burp就会出现一个是否同意的提示，可以选择一直同意即可。

这里我测试了一个web的CTF赛题，这个是往年的一个赛题，大家可以看下测试结果

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTHOPTgX4Q8BS5UAzRs1quBvkCI1tcibHVqdgWgQlgx1bLV5huiaKhlYQh7r9Mf4S66gEHey9nicKECkHvPhqtnRiaErBwvG9SoKicD4/640?wx_fmt=png&from=appmsg)

我开局知识给了她一个这样的话，让他调用burp尝试找思路，然后跑了五分钟左右，他给了我一个思路过程

![](https://mmbiz.qpic.cn/mmbiz_png/ptxZESUjfTFVibJxekpyic7rRMjEicvXLibgJ7NicO643icMY5ibKGjOlXWXtFO6e1TtIXHRmzC1kNvwoKe787AF5DRo6mHXdXv7MaQOpVQ1ODEKUU/640?wx_fmt=png&from=appmsg)

    有耐心的朋友可以仔细看看这个过程，其实从正常解题的角度来看，还是比较复杂的web类型题目，但是他依然是做出了正确的解题过程，不过值得说的是，最后一步命令执行无回显需要自己带数据出网的时候，他就卡住了，一直跑不出来，这种从数据中分析不出来的思路还是有点问题的。

    不过总的来看，能将前面步骤都分析出来，最后只差一步稍微有点经验的师傅就会很容易做出来了，哪怕有一些很难得题目，也可以适当提供一些思路给我们。

    挖洞的实操还需要我再进行测试，后续有测试情况会同步给大家。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

白安全组

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1AUjJ6HpTUZSEBicgombkkXIIVoES3iaEpiaicDuJSgjHcRFuKy7L7Nhs9ib6CrB1p6CEQ0GWATuKoiagCCdSsoFfJ1w/0?wx_fmt=png)

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