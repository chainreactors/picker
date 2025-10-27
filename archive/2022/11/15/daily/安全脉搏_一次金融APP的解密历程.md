---
title: 一次金融APP的解密历程
url: https://www.secpulse.com/archives/190977.html
source: 安全脉搏
date: 2022-11-15
fetch_date: 2025-10-03T22:43:53.751727
---

# 一次金融APP的解密历程

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

# 一次金融APP的解密历程

[内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-14

15,451

**声明：本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。**

**前言：**

客户仅提供官网下载地址给我们测试。但是由于官网的版本不是最新的，APP会强制你升级。而升级后的APP，是进行加固后的，无法使用frida进行hook，注入进程。那同样也无法使用SSL Unpinning进行限制客户端校验证书。新版app使用查壳软件显示未加壳，但是查看源代码明显少了很多代码，且很多都是变量声明而已。

**绕过更新：**

我们要想能对APP渗透测试，一般都是需要抓包和解密的。首先使用burp进行抓包代理，官网版本的APP（以下统称旧版APP），是可以轻松抓到APP的包的（该条请求为检验APP最新版本的请求）。但是内容使用了加密，具体什么加密是不得而知。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405225.jpeg "null")

获取到请求密文：

```
vVAK0jos5eT9gmQJaHOaYbqZ1mgXoBH3bee3MTF3G5wNRHRoPPOYokZLT4MQqaPDN%2BLeEYpIzzDJeErDHcDfhY8muosLfOaw35W3BuCxDNtuNFB86RumMBtOcQXT08qw
```

响应包未json，urldecode后为：

```
{"duration":"0ms","note":"","code":1,"resultDES":"UX/jHk6yqix2yxZIrf0rSIuOjCy6oGxjCPUfBL2avG+DWy/++NW16+YQHVFQ+Nj2w9VOWGcH4OxFtGxbR6K7I6pY0Q9hkP9gc0K0JLZ5O+PwOW72nzissCiLG+cHqadKHzkPOQDdBUuBoa4W1Jz7fQ=="}
```

通过desStr和resultDES，一开始我猜测他为des加密，具体是不是，后续再说。

先进入APP，但是一进入APP就提示更新：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405226.jpeg "null")

img

通过前言，我们知道是不能更新的。（当然不乏某些技术大佬也可以把新版APP搞定，我技术有限，感觉旧版的比较容易搞）。那我们就明确了目标，要先绕过更新校验。

**对于不了解hook****和frida****的同学，我这边推荐先去网上了解下，还有安装之类的，再来看此篇文章。**

首先我们明确一下思路，要怎么绕过这个更新校验呢？

（1）直接反编译，修改APP的版本信息为99.99之类的；

（2）通过修改版本验证请求，使用http层面去绕过；

（3）使用hook，去重写更新函数，或者绕过更新函数；

第一点要app能支持反编译且不存在校验签名。第二点要能知道加密密文的密钥。所以我选择第三种：

通过jadx搜索更新，发现了两处，成功获取到源代码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-16684052261.jpeg "null")

img

类名分别为：com.xxxx.AppUpdate和com.xxxx.WelcomeActivity，通过代码审计可以看到，是先调用的WelcomeActivity，WelcomeActivity再去调用的AppUpdate：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405227.jpeg "null")

img

跟踪进入AppUpdate，调用的checkNativeAppVersion()：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405228.jpeg "null")

img

通过上述代码，我们可以看到，这边就是用于判断是否升级的函数。

```
public void onResponse(Call call, Response response) throws IOException {
    try {
        JSONObject jSONObject = new JSONObject(C.s2(new JSONObject(URLDecoder.decode(response.body().string(), DataUtil.UTF8)).getString("resultDES"), Config.WHITE_KEY, Config.IV.getBytes()));
        if (jSONObject.optInt("code", -1) > 0) {
            JSONObject optJSONObject = jSONObject.optJSONObject("object");
            if (optJSONObject == null) {
                return;
            }
            if (WakedResultReceiver.CONTEXT_KEY.equals(optJSONObject.optString("isUpdate", ChatConfig.CARD_TYPE))) {
                nativeAppVersionInterface.updateApp(optJSONObject.optString("desc", "当前有新版本，是否需要更新"), optJSONObject.optString(ClientCookie.VERSION_ATTR, ""));
            } else {
                nativeAppVersionInterface.noUpdateApp();
            }
        } else {
            nativeAppVersionInterface.showError(jSONObject.optString("note"));
        }
    } catch (JSONException e) {
        e.printStackTrace();
        nativeAppVersionInterface.showError(e.getMessage());
    }
}
```

当JSONObject.optInt("code", -1) > 0时，是会去进行升级的，否则则执行nativeAppVersionInterface.noUpdateApp()。

这边分析完后，其实我们就可以写js进行hook操作了。

我们的hook思路可以这样设置了：

重写checkNativeAppVersion函数，执行执行nativeAppVersionInterface.noUpdateApp()。

Ps：因为我一开始直接重写了checkNativeAppVersion，只执行了console.log(“enter checkNativeAppVersion”)，没有对APP进行启动，这样就会直接卡死在启动页。

附上js代码：

```
if(Java.available){
    console.log('success');
        Java.perform(function(){
        var appUpdate = Java.use("com.xxxx.AppUpdate");
        appUpdate.checkNativeAppVersion.implementation = function(a,b,c,d,e,f){
            console.log("enter AppUpdate");//判断是否进入该hook函数，进入会执行该命令
            f.noUpdateApp();//直接执行不需要更新函数，APP会自动进入
        }
        });
}
```

使用命令：frida -U -l .xxx.js -f 包名 --no-pause

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-16684052281.jpeg "null")

img

成功进入：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405229.jpeg "null")

img

**解密：**

已经成功进入该APP，但是如果想成功进行渗透测试的话，还需要能解开APP的加密。通过des字段，初步判断为des加密，再回头看看刚刚更新的那个请求，是有用c.s2()函数进行操作的，大概率s2就是解密函数。

```
JSONObject jSONObject = new JSONObject(C.s2(new JSONObject(URLDecoder.decode(response.body().string(), DataUtil.UTF8)).getString("resultDES"), Config.WHITE_KEY, Config.IV.getBytes()));
```

可以看到s2的三个参数，即前面响应包中的json字段里面的resultDES参数，然后其次是Config.WHITE\_KEY, Config.IV两个参数，其中Config.IV是以字节数组的形式进行传参的。通过跳转可以看到配置文件的参数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405230.jpeg "null")

img

然后呢，因为获取到密钥和偏移量iv，这样的话des就可以解了。但是问题是解不开。后续的思路就是如果可以直接hook这两个加解密函数的话，是不是就可以不用管他的加解密了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-16684052301.jpeg "null")

img

s1和s2函数不在java层，那我们就需要hook native层的代码。Hook so文件。首先我们先把安装包后缀apk改成zip，然后解压。就可以找到wkb-1.2.2.so的文件了。（路径为lib/arm64-v8a/wkb-1.2.2.so，前面的arm64根据自己测试机的CPU架构进行选择。）直接用ida打开，在导出函数里面搜索des：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190977-1668405231.jpeg "null")

img

里面有很多des的相关函数。可使用以下js进行hook导出函数：

```
if(Java.available){
    console.log('success');
        Java.perform(function(){
        var point = Module.findExportByName("libwkb-1.2.2.so","desDecryptByteArray");
        Interceptor.attach(point,{
            onEnter: function(args){
                console.log("Hook start");
                console.log("args[0]=" + a...