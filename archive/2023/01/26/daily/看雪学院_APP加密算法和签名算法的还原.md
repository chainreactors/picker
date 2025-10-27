---
title: APP加密算法和签名算法的还原
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458493150&idx=1&sn=dfbd46ca0236fc3397a104f9956f97bd&chksm=b18e905486f9194289b952a71b7e6985eddf28dc4e3435ffe916e4d35ae7d606cf722d8994f1&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-01-26
fetch_date: 2025-10-04T04:52:46.732755
---

# APP加密算法和签名算法的还原

![cover_image](https://mmbiz.qlogo.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDugpAb0Yt88cALEOS2ZFF9rJde2ack8rVABYsYe8uzGJNOVuv9hma1Mw/0?wx_fmt=jpeg)

# APP加密算法和签名算法的还原

taobluesky

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuOYPXMAssniaIKGibWevNic5hIFVVUnZd13f5Y7PVnYTbIrHDuZu0AWaHQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：taobluesky

最近遇到一个强度还是挺高的壳，跟大家分享一下如何带壳进行调试，纯粹的技术交流，请勿利用此文章做非法用途！

```
一

准备环境
```

frida 12.11.18
jeb-3.24
jadx-gui-1.3.3-1
xcube
android 7.0（真机）

这里说下为什么一定要用真机，这个壳有模拟器检测，再者就是这个app根本就没编译x86指令的so，所以根本无法在x86模拟器下运行起来。下面直接进入正题。

#

```
二

初探
```

挂上http代理，尝试拦截流量，客户端直接报ssl证书错误，很明显有ssl pinning之类的验证。jadx加载apk，manifest解析失败，再拉入jeb分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuxiae13icqpiaaibavEvmiaZMsKicl92Wict3hlPtMFJbUWiahR20ZcMl7H1fCA/640?wx_fmt=png)是否有人遇见过com.vdog.VDogApplication这个壳，知道的还请赐教一下这到底是什么壳哈。粗略看了一下壳的java部分代码：![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuyQSS9cgjrc6ANNzv2giags8GZ7ohK9W0VzKELpJdm43HA4P1jWEmgCQ/640?wx_fmt=png)

壳还原了elf的文件头，这个没啥新意，手动还原一下so的前四个字节为.ELF就行了。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuShQa4eUlzQx20Qllq98IMfGOh53F8yhTAg38BLI3ooEL3EDY7zpElQ/640?wx_fmt=png)

之后把libvdog-x86.so拉入ida反汇编。结果这个so被混淆得相当美妙，尝试了几个去混淆的脚本都无能为力，我就暂时不想分析这个壳了。

那接下来怎么搞，我想了一个办法就是先把dex dump出来，然后利用frida去动态注入调试。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuF0iaKgfLXQCZjticOGxwwDaLywg3CicufibqDPu7QbuBLs7gaxmJl94Cww/640?wx_fmt=png)
然后接下来就跟预想的一样，有检测frida的代码，一旦spwan或者attach上去，app的进程立马就自动中止了。

```
[FRD AL00::com.**.*****]-> Process terminated[FRD AL00::com.**.*****]->
```

接着用xcube来加载脚本发现可行。好吧，那先用FDex2把dex dump出来，一共7个dex被dump出来。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDutqXISoJzStOtcf6AvcAqrQH8rQcusNcF1SO2ia4xk0quunfCazU8lHg/640?wx_fmt=png)

```
三

正式开始
```

首先第一步先要突破http抓包的问题，用fiddler抓包，看到https的握手请求User-Agent: okhttp/4.9.1，确定用的是okhttp库。

试了几个ssl unpinning的脚本无果，自己分析了一下okhttp/4.9.1库，发现网上给出的脚本有个问题,CertificatePinner.check$okhttp的overload的第二个参数不对，正好这个方法也没有重载，直接就把overload去了，这边给出okhttp 4.9.1可用的ssl unpinning脚本：

```
// okhttp4try {    var CertificatePinner = Java.use('okhttp3.CertificatePinner');     CertificatePinner.check.overload('java.lang.String', 'java.util.List').implementation = function(str) {        writeFile('! Intercepted okhttp4 in [check()]: ' + str);        return;    };     try {//.overload('java.lang.String', 'kotlin.jvm.functions.Function0')        CertificatePinner.check$okhttp.implementation = function(str, _) {            writeFile('! Intercepted okhttp4 in [check$okhttp]: ' + str);            return;        };    } catch (ex) {        writeFile("is this Okhttp3 ?!");    }    writeFile('* Setup okhttp4 pinning')} catch (err) {    writeFile('* Unable to hook into okhttp4 pinner')    writeFile(err);}
```

测试后成功抓包，下面是登录接口的请求body：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuibeicHCprZtVx7MoXvichImsqMGbcUVNukialBXcEU489OvbVHVIEqviaAw/640?wx_fmt=png)
可以看到登录接口的密码是加密的, 还有sign字段。首先寻找密码加密的关键代码如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuHCKjsyHG5MiaM7uYib66Z0ciavr1NCvSfEkYV30icK8n1nAsurE3vEq50A/640?wx_fmt=png)
再跟入：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuwwS24NF2KNYibUysuRkXGVJs92ic7S0icLHfPnJKvlt3woWib4NRxCfibaQ/640?wx_fmt=png)
使用rsa对密码进行加密，这个unname方法就是一个绝妙的注入点，编写获取public key的脚本：

```
// 密码加密:输出RSA的pubkeyvar this3 = Java.use("com.**.*****.encrypt.this3");this3.unname.implementation = function(str, str2){    writeFile('unname is called');    writeFile("pubkey:" + str2);    var ret = this.unname(str, str2);    writeFile('unname ret value is ' + ret);    return ret;};
```

用java还原算法：

```
try {    String password = "qed";    String publicKey = "MIGfMA0GCSqGSIb3D********qGWVMv5z6FwIDAQAB";    byte[] decoded = Base64.decode(publicKey, Base64.DEFAULT);    RSAPublicKey pubKey = (RSAPublicKey) KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(decoded));     Cipher instance = Cipher.getInstance("RSA/ECB/PKCS1Padding");    instance.init(ENCRYPT_MODE, pubKey);    String pwdenc = Base64.encodeToString(instance.doFinal(password.getBytes(StandardCharsets.UTF_8)), Base64.DEFAULT);    Log.e(TAG, pwdenc); } catch (Exception e) {    e.printStackTrace();}
```

好了，到此密码加密的算法已经搞定。接下来来看sign算法，在dex中搜索sign找到关键位置:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuVSkQYOtEJRpvX4QBvb0gicaTTIqYhhFRS6Sm8wg1iacYsmVLXcz93XUg/640?wx_fmt=png)
再跟进SignUtil类里面：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuicGze777aSibGD56jiaiajBmezEIu9Lk4Unf1iarrGXLNLkMjqrAc6DLnEw/640?wx_fmt=png)
可以看到关键的方法handle在native-lib里面, 通过hookget方法可以获取传入验签的参数和sign结果：

```
var SignUtil = Java.use("com.**.****.encrypt.SignUtil");SignUtil.get.implementation = function(str, str2, str3, str4){    writeFile('get is called');     writeFile("str:" + str);    writeFile("str2:" + str2);    writeFile("str3:" + str3);    writeFile("str4:" + str4);     var ret = this.get(str, str2, str3, str4);    writeFile('get ret value is ' + ret);    return ret;};
```

将libnative-lib.so加载到ida分析，分析结果如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDumf1XiaKnbuEZ74A2gSKUeLhB36Gwot7TkRwqB4Z8uSLHsWn2t83eq0w/640?wx_fmt=png)
sub\_45A40函数：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDugSkevSbubJeHQ2hee0e0eBf4iaib8ibfVquia6CicQXO3FfQyfgOznnHS8w/640?wx_fmt=png)
上图已经对关键的方法和变量做了注释，逻辑已经很清晰了，sign=sha256(\_requestData+\_requestDataList+\_token+\_clientTime+salt\_key)，为了验证拼接得对不对，可以把temp\_str输出，寻找一出合适的hook点：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuNMLxUnt4ibd3szqnhTicofNR1cQ89sXBaNCzQORVjJBicVgTlDrTmicwIA/640?wx_fmt=png)
这处就可以进行hook来输出，对应的asm代码如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuDtVdh5KDziaEYNL6UoHhEJXnyww4j370VwnL3JicBu0umndBLToGPCyw/640?wx_fmt=png)
这边要注意一下这个temp\_str的类型是std::string，要想办法转换成cstring才能打印输出，我们可以利用上面分析出来的string\_to\_cstr函数来转换：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuMfiaQvBrOKDn2nAic28jKG1svh9EMmEn1dL1YggzRHlibeF3MtcFazHMQ/640?wx_fmt=png)
分析完了，我们来写hook代码：

```
var libnative_addr = Module.findBaseAddress("libnative-lib.so")writeFile("libnative_addr is: " + libnative_addr) // 内部一个std::string转cstring方法var str_to_c = new NativeFunction(libnative_addr.add(0x45A85), "pointer", ["pointer"]); // 输出签名字符串try{    var addr_45266 = libnative_addr.add(0x45267);    writeFile("addr_45266: " + addr_45266);     Interceptor.attach(addr_45266, {        onEnter: function (args) {            writeFile("ohwawawa");            var ret = str_to_c(this.context.r2);            writeFile("addr_45266 OnEnter sign string:" + Memory.readCString(ret));        },        onLeave: function (retval) {             //console.log("retval is :", retval)        }    });} catch(err) {    writeFile("[!!!!!!!!!!!!] " + err);}
```

这样一旦执行签名函数, 签名所有的参数、签名字符串拼接和返回结果全部都能完美输出。这个算法就比较简单不再写代码还原了。

app本身的防护手段还是不错的，做了很多校验。还有这个vdog的壳代码量还是比较惊人的,内部大量复杂的加解密操作和校验的操作,而且还做了复杂的混淆，以后有时间了可以来研究一下这家伙是如何对frida进行防护的。

我们巧妙使用xcube来逃过壳对frida的spwan和attach检测，还有一个注意的点就是能看到我写的frida脚本都没法使用console.log输出,都是直接用写文件的方式,这是因为用console.log根本无法输出任何内容, 我猜测这个也是壳做的屏蔽, 极有可能直接hook了底层的log函数，可谓恶心至极。还有像这种体量的app代码量还是很惊人的，而且被拆分成非常多的dex，在分析时必定会在几个dex各种交叉分析，这时候需要的是耐心。收工！

原文附件上传了libvdog，如果有人能把它关键逻辑搞出来，请记得@我来学习！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDuibpSTtQpJEiah2Y3NSCfXrEyRKic7fjK7nia7zpNTwbKpNdcJAOaNAqLrg/640?wx_fmt=png)

**看雪ID：taobluesky**

https://bbs.pediy.com/user-home-65525.htm

\*本文由看雪论坛 taobluesky 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Eqic51RIXYMYyr8uCAmQoDubsFXxyY3Ho3cdR2wngOXH6zbZEVTzspwK7pxktkxv93fmA5Eib7pYlw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458489324&idx=3&sn=3643f4f46671c220cbede17182f292d5&chksm=b18ea16686f9287098b2a18599b60fc790b66c114880203b7956a913ad3e2e1d3cdfc9f8a2e7&scene=21#wechat_redirect)

**#****往期推荐**

1.[CVE-2022-2188...