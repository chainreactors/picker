---
title: APP测试中遇到的一些加密问题
url: https://www.secpulse.com/archives/194675.html
source: 安全脉搏
date: 2023-01-10
fetch_date: 2025-10-04T03:22:39.246060
---

# APP测试中遇到的一些加密问题

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# APP测试中遇到的一些加密问题

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[晚上](https://www.secpulse.com/newpage/author?author_id=48220)

2023-01-09

21,956

### 案例一：Java层存在硬编码密钥

反编译apk，在包com.xxx.xxxx.utils中泄露加密key，同时可知加密方式为AES/ECB/PKCS5Padding

[![1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1-1024x451.png "1-1024x451.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1.png)

对登录请求数据包中，使用加密key进行解密

[![2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/2-1024x500.png "2-1024x500.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/2.png)

也可以使用Wallbreaker 查看类以及对象属性（若app存在双进程守护需先解决双进程守护）

```
objection -g com.xxxx.xxx explore -P ~/.objection/plugins
```

[![3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/31.png "31.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/31.png)

搜索类，根据给的 pattern 对所有类名进行匹配，列出匹配到的所有类名

```
plugin wallbreaker classsearch <pattern>
```

[![4.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/4.png "4.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/4.png)

ClassDump，输出类的结构，获取密钥

```
plugin wallbreaker classdump <classname> [--fullname]
```

[![5.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/5.png "5.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/5.png)

### 案例二：Java层不存在硬编码密钥

通过关键词找到关键方法com.xxx.e.b.d，可以看到该方法没有中没有硬编码的key值，当前知道加密方式为DES，同时没有特殊指定的话默认为ECB模式，方法d传入字节bArr，最终指定秘钥为bArr2，而该方法的作用只是截取bArr的前8个字节（des加密秘钥固为8个字节），因此只需知道传入的bArr即可获取秘钥

[![6.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/6.png "6.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/6.png)

使用objection hook打印d方法调用和返回值

```
android hooking watch class_method com.xxxx.e.b.d --dump-args --dump-backtraces --dump-return
```

转换为字符即可获取密钥

[![7.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/7-1024x451.png "7-1024x451.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/7.png)

也可以编写frida hook脚本，执行脚本即可查看加解密信息

```
function hook() {
    Java.perform(function () {
    var b=Java.use("com.xxx.xxx");
    b.b.overload("java.lang.String").implementation= function(a){
        console.log(a);
        var ret=this.b(a)
        console.log(ret);
        return a;
    }
    });
}
setImmediate(hook);
```

执行查看结果

```
frida -U xxx.xxx.xxx.xxx -l test.js
```

使用spawn的模式启动Frida的一个好处是可以带着HOOK脚本重启应用程序，避免错过hook点

```
frida -U -f com.xxxx.xxx -l test.js   --no-pause
```

### 案例三：HMACSHA签名存在硬编码密钥

抓包发现数据包存在签名，正常请求如下

[![8.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/8-1024x407.png "8-1024x407.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/8.png)

修改数据包内容再次请求提示签名不正确

[![9.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/9-1024x369.png "9-1024x369.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/9.png)

对其脱壳后找到签名算法代码

[![10.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/101.png "101.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/101.png)

使用objection hook打印c方法调用和返回值

```
android hooking watch class_method com.xxx.x.x.c --dump-args --dump-backtraces --dump-return
```

可以知道明文格式：请求方法+&+URI+body，和签名后的结果

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image1-1024x142.png "image1-1024x142.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image1.png)

Java 将参数构造好后传给native函数com.xxxx.x.x.c，带了native关键字的说明java的作用范围达不到了，会去调用底层C语言的库。在最终执行的时候，通过JNI（调用本地方法接口）加载本地方法库中的方法。com.xxxxx.x.x.c的实现位于libhw-s.so 中，因此使用ida逆向libhw-s.so,搜索相关签名算法的关键字符，找到密钥

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image2-1024x285.png "image2-1024x285.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/image2.png)

### 案例四：app使用动态密钥

测试某APP发现请求包和返回包内容均进行了加密

[![11.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/11-1024x286.png "11-1024x286.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/11.png)

使用密码自吐脚本发现每次加密的密钥都会改变，但是iv固定

[![12.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/12.png "12.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/12.png)

[![13.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/13-1024x190.png "13-1024x190.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/13.png)

对APP进行脱壳并分析代码，由于iv是固定的，尝试直接搜索iv找到加密的地方，跟踪m6560CL

[![14.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/14.png "14.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/14.png)

发现加密处理在so层中

[![15.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/15.png "15.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/15.png)

hook decrypt方法发现该方法只加解密了手机号并非完整的数据包内容，看来并非是这里

[![16.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/16-1024x103.png "16-1024x103.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/16.png)

hook genRandomKey方法发现返回值就是AES对应的密钥

[![17.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/17.png "17.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploa...