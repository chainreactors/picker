---
title: JAVA代码审计之-反编译与SQL审计
url: https://mp.weixin.qq.com/s/jStchq5yli0B4isAxiovag
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:39:00.896268
---

# JAVA代码审计之-反编译与SQL审计

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AeRibicS5bN3cjueGf85kOyKnpOOzrzAUGsclUib2vx8V5M0OdzEdINavA/0?wx_fmt=jpeg)

# JAVA代码审计之-反编译与SQL审计

原创

secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

反编译与SQL审计SQL注入案例JDBC：mybatis：组件利用durid组件利用struts2组件框架利用

# 反编译与SQL审计

> 进入项目，在web.xml中，如果无法跳转到对应的文件当中去，间接手动添加 lib 目录为库，右键添加即可

![image-20250602192825291](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AgrqGIQ3s6X3qxcPficUxqOicE7Ypm54BeiaibuLw1Cp0ssSjwI0cGFibJEg/640?wx_fmt=png&from=appmsg)

![image-20250602193302391](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AFpaJTx6VqyrLKbqQQoSoppSXnByueEGky2wMiafmib1pbtAN2Tvd31Kg/640?wx_fmt=png&from=appmsg)

## SQL注入案例

java中操作数据库的方式

### JDBC：

```
 jdbc:mysql://127.0.0.1:3306/woniunote?user=root&password=*********&useUnicode=true&characterEncoding=UTF8
```

我们看一下如下代码：

![image-20260110145836583](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AkMNC3EDlK14e5wDr1INrjeUmwO0Ky22vXuCuZoKpgDQJlMVxM0iaZUQ/640?wx_fmt=png&from=appmsg)

运行访问一下：

![image-20260110145953603](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4Ae9htaIdcBsMfzjuSWO7ETxD95QmaAOtI02sZZEdHfjVEaKiapyOk5VQ/640?wx_fmt=png&from=appmsg)

案例详情：

亿赛通

![image-20250602205741394](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4A8TE6O0zljKfbJeN9adfqyf8Jciaj1HyhNGOK8ebkxfNwyMAxzeCFUhg/640?wx_fmt=png&from=appmsg)

我们进入这个类去看看具体实现的代码，进去首先找生命周期函数，要么doGet doPost 要么 service，这里就是service

![image-20250602210018683](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AOIadj5CTnkLZJF1iabkrWrP2kukbnAfnfczEsuPsCOFnuUpUj2iapA5A/640?wx_fmt=png&from=appmsg)

我们发现，他首先接收一个用户可控参数 command，然后如果command的值与upPriority相同，那么就调用 upPriority 方法，我们进入该方法看看

![image-20250602210316434](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AwxYgBPwSQ2shqcD2ibjw9ShHHZiafX9Y0siaowfqecT5Q2n0FLicDibdfiaA/640?wx_fmt=png&from=appmsg)

该方法又接收一个用户可控的参数 id ，并在下面传递给 updateNetSecPolicyPriority 方法的第一个参数，我们再进入这个方法进去看看

![image-20250602210458190](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4Aa9pygUF0jsBLsxKVlgcrOibyicG2EsduEJWxZ0n22gypydDkLbvvnyPA/640?wx_fmt=png&from=appmsg)

发现什么都没干，只是把 id 的值传入了 findById 方法，再进入这个方法来看看

![image-20250602210551097](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AVYnfk291CW8TNm4aAHUoibMiaqicicp7u3UdEIRBw38WAJicEorJnSEthQQ/640?wx_fmt=png&from=appmsg)

直接sql注入

```
 String sql = " select * from " + tableName + " where id='" + id + "'";

 id = root
 select * from admin where id=' + id + '
 select * from admin where id=root

 id = xxx' or '1'='1
 select * from admin where id=' + id + '
 select * from admin where id='xxx' or '1'='1'
```

然后我们去网上找资产的时候，需要注意一点，有时候站点是配置的有根路径的，我们在构造请求包的时候是需要加上根路径的，这个根路径到底是多少其实我们多抓取几个流量包就知道了

然后还有就是注意路径校验的绕过方法，多尝试尝试

还有就是如果找不到对应的类，可以去看看调用它的是什么类，从调用它的类入手。

**但是，在亿赛通中还存在一个过滤器 SQLFilter，有该过滤器的存在，我们单纯的构造数据包数请求不出来东西的，为什么呢？我们看下面的介绍：**

![image-20250615150851399](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AEHUCAVaRLpY6E18lIk0iacWmB7C7axMpghg3RiczDZxbeJUZFVhic7h2A/640?wx_fmt=png&from=appmsg)

我们跟进这个类进去看看源代码

![image-20250615160151945](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4ADTfMM7cTVU8vz2xFDh218ibMpPic3VwMtbF0vsSZ2kkhycjeEEybCUYg/640?wx_fmt=png&from=appmsg)

```
 if (clienturl==null||clienturl.indexOf("Service") ==-1&&clienturl.indexOf("PerOrgServlet") ==-1&&clienturl.indexOf("download1") ==-1&&clienturl.indexOf("useractivate") ==-1&&clienturl.indexOf("roleSee.jsp") ==-1&&clienturl.indexOf("/js/") ==-1&&clienturl.indexOf("dojojs") ==-1)
```

只有这个 if 判断通过，才会正式放行 `chain.doFilter(httpRequest, httpResponse);` 否则，就会执行如下代码

![image-20250615160303183](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AOo6k5fWRAyLJG5TtDPRQUiaIrePp68TerQ04etLoqaSD8AXAMfJg53w/640?wx_fmt=png&from=appmsg)

因此，我们就需要来尝试绕过这个if判断，这有一个或的关系，我们不能让结果为真，因此必须要 两者都为 假 才能绕过，因此，第一个 `clienturl == null` 肯定为假，因为要访问 url 就不会为空，然后后面的 `clienturl.indexOf("Service") == -1 && clienturl.indexOf("PerOrgServlet") == -1 && clienturl.indexOf("download1") == -1 && clienturl.indexOf("useractivate") == -1 && clienturl.indexOf("roleSee.jsp") == -1 && clienturl.indexOf("/js/") == -1 && clienturl.indexOf("dojojs") == -1` 只要能匹配其中一个字段，就可以不等于 -1

因此，我们就要用到 ; 绕过的方法，我在这里只是举个例子：

```
 http://ip:port/url-pattern;service?command=xxx&id=1' or sleep(3)#
```

### mybatis：

mybatis 类型如何存在sql注入，当使用 `${}` 方式传参，并且确保参数类型为String的时候，才会有注入，如果是用 `#{}` 方式给传参的话，则不存在注入

## 组件利用

### durid组件利用

这里用 zhjx 这套系统源码，我们进入看到 WEB-INF 直接进去找 web.xml

* 第一眼发现，是采用的 filter 过滤器的拦截方式，可以判断为 Servelt 框架形式

  ![image-20250602222251123](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4ANLJNWcjsPOooCorthl8sdia86RnNsMB10UuvEgRGzbzricnC0WDhWAfg/640?wx_fmt=png&from=appmsg)
* 找全站过滤的 filter

  按照之前所说的，去搜索 `url-pattern` ，为神马这里不搜索呢，因为搜索这个发现内容非常多，我们不可能真的每一个都去看，因此，这里有个思路，我们进来之后，先去找全站过滤的 filter

  ![image-20250602222748380](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AY4ThflUjbAUeibFfDiaVdIRXdj15tqDjPAF0JQy0YNIRveoibbibichrB5w/640?wx_fmt=png&from=appmsg)

  ![image-20250602222830317](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AfrXbeDv8GpKtv2vL9EICV3spibYpZDlxAxFeLTliczGwR7icnyCYfRIHQ/640?wx_fmt=png&from=appmsg)

  所以，差距显而易见

  我们找一个全站拦截器进去看看具体实现

  ![image-20250602222921093](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4A5WdA6seracDX9sYOMtMwiaKFOk4RD86k0N0fWFjnJsFp4c5pBiaAggww/640?wx_fmt=png&from=appmsg)

  ![image-20250602222940121](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AZuwmsudzUA19D4yuTgTMjYFbt8ZJXs1PyfBBuCz1R9C0zO7NRcstFg/640?wx_fmt=png&from=appmsg)

  OK，没什么价值，为神马呢，因为这一看就是属于 common 类型的代码，是通用类型的，看起来很复杂，我们去找那种具体实现的

  ![image-20250602223230936](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AQ08M11sYkibvddyKRyFffPfIlmUgDibAsyo1ib9MHtQmDm9IdxA1mMzibw/640?wx_fmt=png&from=appmsg)

  ![image-20250602223256254](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4Ad8N4r3MDjg1wg5iaiaMlSYp7Gk8IHuWhL1f6ko8doMmy3TARayKClibfA/640?wx_fmt=png&from=appmsg)

![image-20250602224357930](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4ApXekicQ0kGpLlzDXThzsHuIncnuwRkxIuq5I58N5s926ibkZUdRrPXOA/640?wx_fmt=png&from=appmsg)

我们发现，既对请求的URL做了校验，又对session做了校验，因此，想通过这样的方法绕过是很困难的，但是在寻找过程中，我们发现了另一个点：druid

![image-20250602224552044](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AJRGdTEt0y7VT853E4rQFTEicThesKpZPH0mukicdePFBlx5ePXUjQrcg/640?wx_fmt=png&from=appmsg)

这是一个存储 session 的组件，它可以被绕过，从而访问到存储session 的那个文件，然后通过内部已登陆的session 再结合 路径绕过，从而实现登录。我们去 web.xml 文件中查找该druid/

![image-20250602224957867](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4Ax05AsqR9cEJgMrau0HiaRQGalnydiaDX2iberZGtMntSQoYZwosQ9GibXg/640?wx_fmt=png&from=appmsg)

他将用户名和密码都给出来了，然后我们就可以开始查找一个真正的案例网站去测试了

但是怎么找呢，哪里来的指纹信息呢？我教你

在本系统的 index.html 文件中找信息，然后作为 fofa 搜索的指纹信息

![image-20250602225506493](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AUqkLeegpc6eaPODX1AEEP12Mtobq74UW78ueFN1xgJSmFEibib1zV3yw/640?wx_fmt=png&from=appmsg)

根据指纹测绘一下

![image-20260110151027725](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4A68dYa6KhbRXVD9GS0r66eMfRP4s8QHXuXjyCZNQE2X7op3eHvciauSg/640?wx_fmt=png&from=appmsg)

只有35条结果，说明准确度很高了，我们再去找找具体的站点，每一个都进去看一看

![image-20260110151112790](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AKypibuqdqbhssODQB0qQodtyE7kQsv6JrMCtxhM12HwyqNW6nvSZeRw/640?wx_fmt=png&from=appmsg)

我选择了第一个站点点进去，可访问

然后我们去访问 /druid/123，后面这个123是可以随便输入的，他都会跳转到对应的登陆页面

如果直接访问 `https://ip:port/druid/123` 是不行的，会重定向到这个登陆首页，但是，我们可以尝试，再根目录的基础上去访问，比如访问 `https://ip:port/zhjx/druid/login.html`

![image-20260110151223212](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSYXVQWufYsdPjHuFiay6S4AKC0zxu2ULictN1J7CDTcmaMiap6yczCuQ0Y1tVZ9wyVTFRhC2kU4kpEw/640?wx_fmt=png&from=appmsg)

成功访问到登陆点，使用默认账密登录，发现登陆不了，点击登录直接没反应，放弃直接登录的方式

**druid存在一种通过请求的方式可以讲s...