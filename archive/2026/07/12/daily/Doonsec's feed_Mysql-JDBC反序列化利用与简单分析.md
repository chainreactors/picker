---
title: Mysql-JDBC反序列化利用与简单分析
url: https://mp.weixin.qq.com/s/KLOacUxCdWdms_RmA-I9IQ
source: Doonsec's feed
date: 2026-07-12
fetch_date: 2026-07-13T05:25:41.251425
---

# Mysql-JDBC反序列化利用与简单分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVlHWgLRMqdpJWMYgnQznCswHh286UHWI9EibPg1Ke7CSVtyrUzoZM2rXQx1LMLaJmg9Rr74A6Gf3u0a1ehJAloTLictAuunV3afA/0?wx_fmt=jpeg)

# Mysql-JDBC反序列化利用与简单分析

原创

进击的hack
进击的hack

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 前言

渗透测试时，在我们进入管理系统的后台，有时候会遇到连接数据库的功能。

具体的样子，可以参考hl666师傅的文章：

* • JDBC反序列化实战 [https://mp.weixin.qq.com/s/BdpFuTEoYyiBzyJGUlB2wg](https://mp.weixin.qq.com/s?__biz=MzkzMjQzNjg1Nw==&mid=2247484255&idx=1&sn=60357c4eb6705091b26b05b6dd548099&scene=21#wechat_redirect)

## 环境准备

* • https://github.com/4ra1n/mysql-fake-server
* • JDK1.8\_261

## 测试demo

```
public class MysqlJdbc {
    public static void main(String[] args) throws Exception {
        String driver = "com.mysql.jdbc.Driver";
        String DB_URL = "jdbc:mysql://xxxx";
        Class.forName(driver);
        Connection conn = DriverManager.getConnection(DB_URL);
    }
}
```

pom.xml导入com.mysql.jdbc.Driver

```
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.20</version>
</dependency>
```

## 测试

### 命令执行

start server，绑定IP和PORT

![396834cd2480344d8193f93c2809f090.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzLx0w8KP4yKNDgAWls5iaxkxSicK3jlbGWgsDwQQanUEk8U5TyemoZBgQ/640?from=appmsg "null")

396834cd2480344d8193f93c2809f090.png

生成命令

![6dd10094077b5e5364692884f3069b97.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianz9kj5MK9iaRctKDYSEGKnicIT0egxC4JJjIUSTXjuMKBqPJSzFcMFVYew/640?from=appmsg "null")

6dd10094077b5e5364692884f3069b97.png

粘贴，执行

![553bcc136857c38eb0bb5e90e23a2cbb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzOdTcNnpnJAn5ibnYecg7XVgvfbmDWibgejLSMqnDjRzmLz0RbLuicGs5Q/640?from=appmsg "null")

553bcc136857c38eb0bb5e90e23a2cbb.png

### 文件读取

文件读取

![da98b4175288627ee424b8bdc828b225.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzicH8kXraPuq2vcNMzCN1TP5wAjJOb1DSnGc0JXugoSfpzXl87D3pWZw/640?from=appmsg "null")

da98b4175288627ee424b8bdc828b225.png

读完保存在

![39ff44f064fc751150793714c372c483.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzTocCgOBk7LGQhchuUFCY1hQLf7GB92VyQLPSjFd1Q7iaCgPtiaxPyNgQ/640?from=appmsg "null")

39ff44f064fc751150793714c372c483.png

## JDBC URL分析

```
jdbc:mysql://127.0.0.1:3306/test?autoDeserialize=true&queryInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor&user=base64ZGVzZXJfQ0MzMV9jYWxj
```

原型：`jdbc:mysql://<host>:<port>/<database>?<params>`

* • 127.0.0.1：连接的 MySQL 服务器地址，本地地址。
* • 3306：MySQL 的默认端口。
* • test：数据库名称。
* • 后面是多个 URL 参数，用 & 分隔。

**URL参数分析**：

* • autoDeserialize=true

+ • 启用 MySQL JDBC 驱动对序列化对象的自动反序列化。
+ • 当数据库返回字段是 Java 序列化对象（通常是 BLOB），会尝试通过 ObjectInputStream.readObject() 来还原为 Java 对象。

* • queryInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor

+ • 指定一个或多个查询拦截器类，在执行查询前后插入自定义逻辑。
+ • ServerStatusDiffInterceptor 是 MySQL 官方提供的拦截器之一，它用来比较执行前后的 server\_status 变化。

* • user=base64ZGVzZXJfQ0MzMV9jYWxj

+ • 指定用户名。
+ • base64解码后为deser\_CC31\_calc

## 利用链分析

通过构造恶意MySQL协议包，进入反序列化ObjectInputStream.readObject()，执行危险代码。

com.mysql.cj.jdbc.result.ResultSetImpl#getObject(int)
调用栈：

![ebb2c56828fd35190f0153039cc8319d.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianz0YypH3E5hsQiaIhFusdiauAKRIcSneYicJYSOL345zyo6dPp8iakibSSsPQ/640?from=appmsg "null")

ebb2c56828fd35190f0153039cc8319d.png

该函数内部执行：
getObject ——》switch (field.getMysqlType())——》case BLOB ——》objIn.readObject()

其中getObject调用`obj = objIn.readObject();`

![631be9373eacb07fbe13517d993112a6.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzKUYFvM2vhRAY5k0hrHDEgaUdLdmiaxHaiaukJTicDcL5jBqesxf8fYmeg/640?from=appmsg "null")

631be9373eacb07fbe13517d993112a6.png

完整代码

```
ByteArrayInputStream bytesIn = new ByteArrayInputStream(data);
ObjectInputStream objIn = new ObjectInputStream(bytesIn);
obj = objIn.readObject();
objIn.close();
bytesIn.close();
```

## 反向追栈

查看谁调用了`getObject`

com.mysql.cj.jdbc.util.ResultSetUtil#resultSetToMap(java.util.Map, java.sql.ResultSet)

![fb3b002664b35c605ad4359b8b4894c7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzia1ho3OV3sSatej38TKCSKZykEgIWpHt09Ln8tQDC6VFM8Oue6KTIJA/640?from=appmsg "null")

fb3b002664b35c605ad4359b8b4894c7.png

那么谁调用了呢？还记得JDBC中的

```
queryInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor
```

com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor#populateMapWithSessionStatusValues

![4ebace6a8540ce9d562ae4908226df19.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianztx5AYiaZdkquibcKwKrnbz3WbMKYCicmxLV2JiaXiaicGNibjM8UItk9ibaYMA/640?from=appmsg "null")

4ebace6a8540ce9d562ae4908226df19.png

该方法又是有ServerStatusDiffInterceptor中的preProcess调用的

![f3081b6f4daff05ad38fe611104e90eb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzbsL49ia72e9Ap8ZsVm66dJkAe3RWcE2aQoJQ7j1kY3VWOWM676bYRpg/640?from=appmsg "null")

f3081b6f4daff05ad38fe611104e90eb.png

其是 MySQL JDBC 驱动中的一个拦截器方法，它属于 MySQL 查询拦截器机制，用于在查询执行前插入逻辑。

那既然是在查询前会执行，那我们还没传入SQL语句，为什么就执行了呢？
因为MySQL JDBC客户端在连接建立后通常会执行`SET autocommit=1`等SQL语句。

![2dd84fc0373c684027427531e2d7a013.png](https://mmbiz.qpic.cn/sz_mmbiz_png/a1BOUvqnbrjulP51X3VN6icQZ38H5xianzYrNEib6WXcFZicNaX2goQpO4wA7SIWB7CNp2w4TmNoltqJaica5z5TrCw/640?from=appmsg "null")

2dd84fc0373c684027427531e2d7a013.png

## 扩展

* • Mysql-JDBC反序列化 https://forum.butian.net/share/2872

### 不出网的情况

* • JDBC-MySQL驱动不出网攻击总结 [https://mp.weixin.qq.com/s/frZHYc\_uD5o7HdRtkmrSYQ](https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247512182&idx=1&sn=51b05100767165f7de3bae4c7840dee1&scene=21#wechat_redirect)
* • 从JDBC MySQL不出网攻击到spring临时文件利用 https://xz.aliyun.com/news/17830

### 绕过限制

* • Jdbc反序列化[绕过|修复|分析] [https://mp.weixin.qq.com/s/jXKlItva\_OiehIoPgYvcAw](https://mp.weixin.qq.com/s?__biz=Mzg5MDAzMTY5MQ==&mid=2247484476&idx=1&sn=cc7fa49cdcce96b8a23f1cff9e4e3833&scene=21#wechat_redirect)

## 参考资料

* • MYSQL JDBC反序列化解析 https://tttang.com/archive/1877/
* • MySQL jdbc 反序列化分析 [https://mp.weixin.qq.com/s/tOOhDLr0K2l52n7627di4Q](https://mp.weixin.qq.com/s?__biz=MzkyNTY3Nzc3Mg==&mid=2247486280&idx=1&sn=d30437d27aaa53da1fc7c82c848827d1&scene=21#wechat_redirect)
* • JDBC反序列化原理和调用链细节分析 [https://mp.weixin.qq.com/s/Abz0OtOk43JPtzth52nBHg](https://mp.weixin.qq.com/s?__biz=MzUyODkwNDIyMg==&mid=2247545231&idx=1&sn=f8885e0c2eb5b165518a43c1a2210ecc&scene=21#wechat_redirect)
* • https://wiki.wgpsec.org/knowledge/ctf/JDBC-Unserialize.html

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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