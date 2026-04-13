---
title: 【代码审计】WebGoat靶场全关卡审计教程
url: https://mp.weixin.qq.com/s/G45kZWkKqv70fJEBsq463g
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:19.820314
---

# 【代码审计】WebGoat靶场全关卡审计教程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1uNK9ibK0YFT6nbhYYAtmtXtqeorO3om73iceg2OJoThEG2YZsaXcS8bnVZQ08W9bXViaHql01pJbjOGJVI3M50jKjDgngd5Gic778/0?wx_fmt=jpeg)

# 【代码审计】WebGoat靶场全关卡审计教程

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 以审计的角度走遍全关卡

## 目录

1. (A1) Broken Access Control（访问控制失效）

* 1.1 会话劫持
* 1.2 不安全的直接对象引用
* 1.3 缺失功能级访问控制
* 1.4 伪装认证Cookie

2. (A2) Cryptographic Failures（加密失败）
3. (A3) Injection（注入）

* 3.1 SQL注入(介绍)
* 3.2 SQL注入(高级)
* 3.3 SQL注入(缓解措施)
* 3.4 跨站脚本
* 3.5 跨站脚本（存储）
* 3.6 跨站脚本（缓解措施）
* 3.7 路径穿越

4. (A5) Security Misconfiguration（安全配置错误）

* 4.1 跨站请求伪造
* 4.2 XXE

5. (A6) Vuln & Outdated Components（易受攻击的组件）

* 5.1 易受攻击的组件

6. (A7) Identity & Auth Failure（身份认证失败）

* 6.1 认证绕过
* 6.2 不安全的登录
* 6.3 JWT tokens
* 6.4 密码重置
* 6.5 安全密码

7. (A8) Software & Data Integrity（软件和数据完整性故障）

* 7.1 不安全反序列化

8. (A9) Security Logging Failures（安全日志故障）

* 8.1 日志安全

9. (A10) Server-side Request Forgery（服务器端请求伪造）

* 9.1 服务器端请求伪造

10. Client side（客户端安全）

* 10.1 绕过前端限制
* 10.2 客户端过滤
* 10.3 HTML 篡改

11. Challenges（挑战关卡）

* 11.1 管理员丢失密码
* 11.2 无密码
* 11.3 管理员密码重置
* 11.4 没有账户

12. 本文涉及的所有代码和文件

本文的环境配置：

靶场地址：https://github.com/WebGoat/WebGoat

环境版本：webgoat-2025.3.jar

JDK版本：jdk25

## (A1) 一、Broken Access Control（访问控制失效）

### 1.1 会话劫持

第一关，定位请求接口。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uy00azibe5Mjr9Jk5zfXjCvfh3hj3duUNmHG7ibLrflFdSh5jHax3P4veJ4rxqFiaeicgEibUiahskbTUzZCuOcxIibnawFAvpvsykE0/640?wx_fmt=png&from=appmsg)

定位代码位置。![4](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uwIyibd4JdWEGGchPzjzpiaAQbDBWl7We10Djbt1de69d57e3yqEFXlLkc3WDaQx4EcwMByb5Mvhpw1OWJq5eBeN2bVHHZAH1Tc/640?wx_fmt=png&from=appmsg)

```
authentication = provider.authenticate(Authentication.builder().id(cookieValue).build());

//认证通过就过关
if (authentication.isAuthenticated()) {
      return success(this).build();
}
```

`Authentication.builder().id(cookieValue).build()`中`cookieValue`未认证用户不存在`hijack_cookie`，因此该代码创建了一个`Authentication`实例并未初始化任何值。定位类`HijackSessionAuthenticationProvider`的`authenticate`方法。![7](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uMX39j3brHWZTvSfpRJR6Cfoic6Mibf60lmoh0Briavv9k1suqBrVDycdDe3loQWyQDzL6GR11r0yP4mpkbX4uticjKEngM5Q42fQ/640?wx_fmt=png&from=appmsg)重点分析如下代码即可。

```
  private Queue<String> sessions = new LinkedList<>();
  private static long id = new Random().nextLong() & Long.MAX_VALUE;
  protected static final int MAX_SESSIONS = 50;

  private static final DoublePredicate PROBABILITY_DOUBLE_PREDICATE = pr -> pr < 0.75;
  private static final Supplier<String> GENERATE_SESSION_ID =
      () -> ++id + "-" + Instant.now().toEpochMilli();
  public static final Supplier<Authentication> AUTHENTICATION_SUPPLIER =
      () -> Authentication.builder().id(GENERATE_SESSION_ID.get()).build();

  protected void authorizedUserAutoLogin() {
    if (!PROBABILITY_DOUBLE_PREDICATE.test(ThreadLocalRandom.current().nextDouble())) {
      Authentication authentication = AUTHENTICATION_SUPPLIER.get();
      authentication.setAuthenticated(true);
      addSession(authentication.getId());
    }
  }
```

![8](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sbUic726T0vk7bh3qVtMHbqWEwMvUYQZeNTrlnEtar7RBfVFbRDmqWsiaiadiaxSLV6EetbCfguwVkJ83MuIYbz5UZC8gM2kAJVR4/640?wx_fmt=png&from=appmsg)因此我们构造一个脚本，每次发送一个请求后遍历该请求附件的几个`id`以命中有效会话，为了避免本文过长，本文涉及的脚本内容文末一起奉上，结果如下。![9](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1v8JRlkPFTzEBeRcMA47DorXAfHEovo4eFbhzqOGFbaQRETV3MI94sI31AmhldAVH1ribicN0Gdpt5LT03v21o80pJVtiaqCibGZiao/640?wx_fmt=png&from=appmsg)![10](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vWXCib87LDG8iaYTIUtHOXrwbdbCPw42sdTSlLrN8Ria8Oa9AW1tX9ia2xuEDbGqhs8MEZrNPSF8NsMrlzXNbXfVyb5zE5ENLhjzs/640?wx_fmt=png&from=appmsg)

### 1.2 不安全的直接对象引用

第一关，输入`tom`和`cat`直接过。![1](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1u5ibXjjy33YtQmZP6oEhj8bjtnmYp17Rh4rtm7ibk809ukrBMiaV6IQ4NeoicE6IXBcgWGfGFCDSMwVp0MWEs3de7B3ZKMFI5j4icU/640?wx_fmt=png&from=appmsg)第二关，题目说列出服务器响应中存在但在配置文件中未显示的两个属性。![2](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sVsAP3IXicUM8ryJzpATh2H2pv9HuqTkVJKDffRxibbYAf3zNPvwFOIX6rpJIJAJ4ic94aDSzDruz88wcFKZ6lfKVDr0UUPAibXibw/640?wx_fmt=png&from=appmsg)![3](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tOZzZXRMrIZNGpzdFPNfWicZOao0VpTaXXh1dHjXI4ES66ooiadB84ktr9ia8GTAauDFiby7XcsvWA0ROnHqYvAJLt5LkBSwqdAFA/640?wx_fmt=png&from=appmsg)对比一看代码中多了`userId`和`role`,提交过关。![4](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tFTQf9Io1gCsMpfbUZX8gZqrchE5yXMEqxY5ug6cwjhQzicMdosq83yapBzic9Wibd0ibicWy4ibUpZuYUwvt8uic1eMzLT2kGuMgCOA/640?wx_fmt=png&from=appmsg)第三关，定位接口，检索代码。![5](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uqLEEhBl2pW5MvUic55TSgza4wNn3jz49FGvxNeuNUadEfIkdBtZXBLMmfuOnOVU6F0TqNwcEOXGiaBcKxMBxcjFyAcypqWSzDo/640?wx_fmt=png&from=appmsg)![6](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uNHozCGXRteQEI9gWhSl1y376RrhtUtM0ia0iaRF3sibyrjCeyQfURrljd41t9briclCW2a9SAYqk1j2y5ZMCy2xXMhuRjEgdoRr8/640?wx_fmt=png&from=appmsg)拼接请求路径即可，但是你会发现需要`userId`,还记得第二关的`userId`吗？在`burp`构造请求获取即可。![7](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uZKbBAAgzlzacZ94HnZxTIWlgiaYXibUx3HvsribRSDnNgmAJnpicXjxq1OqEdribcTrWrpBH7UI9hwl2Y5vibN9K7S8RlRPora6NQM/640?wx_fmt=png&from=appmsg)拼接`WebGoat/IDOR/profile/2342384`通过。![8](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vIacBGibzJFfiaMNNUpbasgDUmDJK2zG5W6SROFEdmelyrIxePViboOAY5I8rdcEMsrVavXENmd6YJEia1ouZJpibiaTylSDZc0HaKs/640?wx_fmt=png&from=appmsg)第四关，存在两个问题，分别解决。![9](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vp8tSWwsficxxMVLFCkq6eBCWbRHbsxJ9ZBHXBMwgd9CD7pemoicLic1jlXDgSJkRWqEbZ0BKp3y0BSrCZomv5LuicKLyNv6qNuN0/640?wx_fmt=png&from=appmsg)![10](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uu4gvWvGHr1Z3FEgth71APA8f6yCr5kq8JUk1TrBPawVv8jLEvxpfnBrKiajklqCGp37SVzeEGCAEHNSniakzg5X6tUsicQRt9ro/640?wx_fmt=png&from=appmsg)题目让我们查看别人的资料，这里从代码可知，这个别人应该就是`2342388`，当然如果作为黑盒测试您一定会枚举对吧。![11](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uHQdd4xVUsNJPdcawkibTl9AhiaicaFdBV9Ziaa6fRpZepnMHAm68RUYQ1A4Xs22MOaUI6PKy0tB1d2e4NHM5q6rRtnFQD27zY28k/640?wx_fmt=png&from=appmsg)第二小题让我们编辑其他用户的配置文件，这往往涉及到不同的请求方法，定位接口。![12](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1upm9OHwaMhhjCTkbYC8cYicicbicrleViaWPtnpRlnrQKdAPtsCPXS9EghJbVYfMWTBnnp3OSLiaMyv0DeSsBI1qT3QdibgcpNd7KxA/640?wx_fmt=png&from=appmsg)同时你会发现你检索`IDOR/profile/{userId}`似乎没有什么有用的信息，不过题目要求你修改别人的信息这个`userId`此时应该是一个具体的值，会不会就是`2342388`呢？让我们检索一下。![13](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uaRXKJDW11Tibuf7KLLKN0hicdIE06kndibAEQrPqQnP8wyQbCKIgvZGYfMtVjHWY7CQuomtjBicFMV8PN60nCc3Upkd3hVZiboNWc/640?wx_fmt=png&from=appmsg)好吧，你很聪明，你发现了它，让我们构造对应的请求完成题目。当然请注意`Content-Type: application/json`的设置，不要被这小错误而困扰。![14](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uP7KU3uq6zxPTXoBX4lHXdltJdeQwOnbG4cgNb3VOEs5r5ibBzSibZp2dYDEDgU3uAlt6oMsviaWRA7EsSjDia8MC0mHv57PPXwRU/640?wx_fmt=png&from=appmsg)

### 1.3 缺失功能级访问控制

第一关，题目让我们找一些隐藏的东西，不过我们不管直接，整代码(狗头)。![1](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1sNYKsLORribtDArmBe90VadXaNG5xqeKoicCBYIywhVb3q33g0vicAIqWDYNfpBs5jrAiaNrcZILv16PPb6pQPZib46K6R4xicgQ2icE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1t8dK43R2eBtJ8XnQiaHTB7cSe78352tErdjfpXyqDlXUNx1ZkZFgibHj1PBwyKJG77eKshZMc5GKsy20icqzer0hleT4jtZibn1w0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1ucodNDx9HDFpQDcTdmleFfnrWGd8Vo483NicM0nbVmSocVm62J9s3lzlGib0jbR0XmJn64SVCNiaHGQqMD2DCsqnTgdnFoTMEsuI/640?wx_fmt=png&from=appmsg)

第二关，获取`Jerry`账户的哈希值。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1th7ib6zCV47r1CVA7WicxDd44licCGyzBibAEoPibicd1s4WzoyibPRSGeD7ptj0Q0w6icSqiaQibFXnSliafX1Q1aW4B0tRNibykrricay8Rg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uQOS0liczzKZmjsickwBveS5nxfgmIT2s1w0YC04cjh2libNiczooIENm9icXCMf0AzMnNcp4uYFWPkuHWffyGmQ58SIruyBEWxnwQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1toM1koxfsz4SLNRQnLEpkXWUWx42yicncgOComqawMFEZSRefCOjJktxq7FX1bC7f8YOeQ3Jjus0pRoIWqXmw8o0ej6dFkhd7E/640?wx_fmt=png&from=appmsg)

第三关，题目说修复了现在只能管理员才能获取所有的用户列表。

![](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tzj1ibhxn5uhdXHFn4hqOia8OF4VB8Owa6vQmJfPIetzmTWaKFMPhcDGAMA1I5t3kgX...