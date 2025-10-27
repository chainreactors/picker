---
title: 安卓协议逆向 cxdx 分析与实现
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458499198&idx=1&sn=a16261bef71086a0eee931d5709f294f&chksm=b18e88f486f901e22359f08e9668b7e9348d8c8e15caf535774bc4ac637c0dec6e384005bb55&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-24
fetch_date: 2025-10-04T10:29:59.373227
---

# 安卓协议逆向 cxdx 分析与实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEfichqOxlF2GCU9biczTKYA4PiaibggPwzuKxBuBCmlzUS2nmGXfL155IYA/0?wx_fmt=jpeg)

# 安卓协议逆向 cxdx 分析与实现

行简

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GbQvhTibRqum43S5vS4kHrEpVp158fQCEBaGKQwwVQCLXqC7DxpW2OrqfeDjeNMSufKsdPjmiacdrw/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：行简

#

```
一

## Kit
```

##

app 版本：5.0.0
设备：K40 刷 piexl 11 rom
抓包工具：Charles
反汇编工具：JEB、JADX、IDA
inject：frida

##

```
二

## 抓包
```

##

```
POST /v1/api/app/login/doLogin HTTP/1.1X-OsVersion: 30User-Agent: Mozilla/5.0 (Linux; Android 11; M2012K11AC Build/RQ3A.211001.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 CSDNApp/5.0.0(Android)wToken/0.0.1X-RandomNum: 54736X-Access-Token: 00871d5df0d4f51efb5883b3b2fd2359platform: androidX-Ca-Signature-Headers: X-Ca-Timestamp,X-Ca-Key,X-Ca-NonceAuthorization:X-OS: Androidc_appVersion: 5.0.0X-App-ID: CSDN-APPX-App-Theme: daycontent-type: application/json; charset=UTF-8X-Ca-Signature: BqhPpXbobBOndykiyCtOVK06GHLkfLbs1y4B3Ek0gnY=X-ConnectionType: WIFIUserToken:X-TimeStamp: 1671939318488Cookie: UserName=;UserToken=X-Ca-Key: 203789067Accept: application/jsonX-Device-ID: aid0f0fef992b53479187546b3c621157f0wToken: e447_5rU5WWYQegPo5EMOZSnKzF4YPtJSetwo+lGrEUrtZaKEe73GkiTOoE83PLp0yivsi4pZV7HySc+lbsebppMqHlXmQwVLx0vrlQpYC0b99vOYBRZWnVbeMhLZ4WUuAAKH/V07WkNSNXORUsgHumLj1BZZ7x1riK8beahdp9ctmSwP3AdA/sZA4OkzEVF4rJ+G6nwyyGcI/JLoRH0/1hPUT91sdBKKA64yj1QKRAZuJjsX9WRcqo9xYgfcJDnpqVnhObGQD96CfSok8z8d9otv+Fl6ULZrddvcnvzs6cJhjuW3ryBn151Xat/2CU/9EXUEKG3e0g4/K9rEaDRb2JhDGEDwIj+Qd5RU1uaBKxS/7jlSVq8wQ7x3qVVN1tHqS4AXhVow6eMABT6PArcEfkFm42bwXOFWsAUd5C7uGvHGIlTGytU6Vx/CJPwPvCuSffef5mQL7daszEzN+zQJ9VjxgOrjKXkDVkt6O6UpyA+1u3lowOqUaSPK6u2vND/Xqus7&ff4b_85475962D8E15A4E7AE60ED42FF3568E8EDB86EE620E495591X-DeviceModel: Redmi M2012K11ACversion: 5.0.0X-Ca-Nonce: be0eca5c-e959-4b0f-b4e7-22e00118157eX-Ca-Timestamp: 1671939318489X-Sign: 70B21B02FD0EFD2353F0D7F4F2E7CDB6FC1C3C42Host: passport.csdn.netConnection: Keep-AliveAccept-Encoding: gzipContent-Length: 95{"pwdOrVerifyCode":"123456","loginType":"1","userIdentification":"17750659921","checkAli":true}
```

意料之中一大堆参数，反复几次总结需分析的参数应该为以下几个：

```
X-Sign、wToken、X-Ca-Signature、X-Access-Token、X-Ca-Timestamp
```

##

##

```
三

## 分析
```

##

先搜索 X-Sign，就一处。

跟进得：

```
public static Map<String, String> z(String url, Map<String, String> requestMap) {    String str;    String a2 = wo3.a(CSDNApp.csdnApp);    HashMap hashMap = new HashMap();    hashMap.put("platform", "android");    hashMap.put("version", xn3.u());    hashMap.put("c_appVersion", xn3.u());    if (!TextUtils.isEmpty(it3.g())) {        hashMap.put("JWT-TOKEN", it3.g());        no3.a("==JWT-TOKEN==", it3.g());    }    hashMap.put("Authorization", StringUtils.isEmpty(it3.g()) ? "" : "Bearer " + it3.g());    hashMap.put("X-Device-ID", a2);    hashMap.put("X-OS", "Android");    hashMap.put("X-App-ID", "CSDN-APP");    hashMap.put("X-Access-Token", MD5.md5(a2 + "AndroidCSDN-APPb85fF96d-7Aa4-4Ec1-bf1D-2133c1A45656"));    hashMap.put("X-OsVersion", Build.VERSION.SDK_INT + "");    String str2 = Build.BRAND + Operators.SPACE_STR + Build.MODEL;    int length = str2.length();    for (int i = 0; i < length; i++) {        char charAt = str2.charAt(i);        if ((charAt <= 31 && charAt != '\t') || charAt >= 127) {            str2.replace(charAt, ' ');        }    }    hashMap.put("X-DeviceModel", str2);    hashMap.put("X-ConnectionType", yp3.b(CSDNApp.csdnApp));    hashMap.put("UserToken", StringUtils.isEmpty(it3.q()) ? "" : it3.q());    hashMap.put("X-App-Theme", CSDNApp.isDayMode ? "day" : "night");    int c2 = xn3.c(10000, 99999);    String str3 = new Date().getTime() + "";    try {        str = mq3.a(a2 + c2 + str3 + zf1.o);    } catch (DigestException e2) {        e2.printStackTrace();        str = "";    }    hashMap.put("X-Sign", str);    hashMap.put("X-RandomNum", c2 + "");    hashMap.put("X-TimeStamp", str3);    StringBuilder sb = new StringBuilder();    sb.append("UserName=");       sb.append(it3.p());    sb.append(";UserToken=");    sb.append(StringUtils.isEmpty(it3.q()) ? "" : it3.q());    hashMap.put(IWebview.COOKIE, sb.toString());    if (!StringUtils.isEmpty(url) && requestMap != null && requestMap.containsKey("category")) {        hashMap.put("X-PageKey", "blog." + requestMap.get("category"));        hashMap.put("X-Path", "app.csdn.net/blog/" + requestMap.get("category"));    }    if (!StringUtils.isEmpty(url) && url.equals(s22.G0)) {        hashMap.put("X-PageKey", vr3.Q6);        hashMap.put("X-Path", "app.csdn.net/blog/detail");        if (requestMap != null && requestMap.containsKey("from")) {            hashMap.put("X-Referer", "blog." + requestMap.get("from"));        }    }    hashMap.put("User-Agent", CSDNApp.csdnApp.userAgent + " CSDNApp/" + xn3.u() + "(Android)wToken/0.0.1");    try {        hashMap.put("wToken", TigerTallyAPI.vmpSign(1, str3.getBytes("UTF-8")));    } catch (UnsupportedEncodingException e3) {        e3.printStackTrace();    }    return hashMap;}
```

pretty nice，很多参数都在这里，那就从上往下分析：

```
hashMap.put("platform", "android"); // 固定值hashMap.put("version", xn3.u()); // 固定值hashMap.put("c_appVersion", xn3.u()); // 固定值hashMap.put("Authorization", StringUtils.isEmpty(it3.g()) ? "" : "Bearer " + it3.g()); // 无用，请求头中为空hashMap.put("X-Device-ID", a2); // a2 在 String a2 = wo3.a(CSDNApp.csdnApp);
```

hook wo3.a看看：

```
function main() {    Java.perform(function () {        var wo3 = Java.use("wo3");        wo3["a"].implementation = function (context) {            console.log('a is called' + ', ' + 'context: ' + context);            var ret = this.a(context);            console.log('a ret value is ' + ret);            return ret;        };    });}setImmediate(main)
```

结果：

```
a is called, context: net.csdn.csdnplus.CSDNApp@dc96acba ret value is aid0f0fef992b53479187546b3c621157f0
```

多次 hook 该值并没有改变，查看不同数据包的内容也是一样的，但在 Java 层仅分析到 aid 复制点，后面数据同一设备都是一样的，怀疑是消息散列值，有可能是 DeviceID 或者 UUID，有在 Java 层看到，但 hook 不到，往下分析：

```
hashMap.put("X-OS", "Android"); // 固定值hashMap.put("X-App-ID", "CSDN-APP"); // 固定值hashMap.put("X-Access-Token", MD5.md5(a2 + "AndroidCSDN-APPb85fF96d-7Aa4-4Ec1-bf1D-2133c1A45656")); // a2 就是上面的 X-Device-ID 再进行加盐处理后进行 MD5 加密复现一下：
```

```
from hashlib import md5 def encrypt_md5(mes):    new_md5 = md5()    # 这里必须用encode()函数对字符串进行编码，不然会报 TypeError: Unicode-objects must be encoded before hashing    new_md5.update(mes.encode(encoding='utf-8'))    # 加密    return new_md5.hexdigest() if __name__ == '__main__':    print(encrypt_md5('aid0f0fef992b53479187546b3c621157f0AndroidCSDN-APPb85fF96d-7Aa4-4Ec1-bf1D-2133c1A45656'))
```

结果 00871d5df0d4f51efb5883b3b2fd2359，校验无误,继续往下：

```
hashMap.put("X-OsVersion", Build.VERSION.SDK_INT + ""); // sdk 版本吧，可随机的样子hashMap.put("X-DeviceModel", str2); // 通过上面获取来的，分析一下就是手机 + 手机名称hashMap.put("X-ConnectionType", yp3.b(CSDNApp.csdnApp)); // 网络连接类型hashMap.put("UserToken", StringUtils.isEmpty(it3.q()) ? "" : it3.q()); // 抓包为空值，放弃hashMap.put("X-App-Theme", CSDNApp.isDayMode ? "day" : "night"); // 主题模式hashMap.put("X-Sign", str);
```

str 是上面计算来的，拿来分析下：

```
int c2 = xn3.c(10000, 99999);String str3 = new Date().getTime() + "";try {    str = mq3.a(a2 + c2 + str3 + zf1.o);} catch (DigestException e2) {    e2.printStackTrace();    str = "";}hashMap.put("X-Sign", str);
```

```
c2：10000 - 99999 之间的随机值；str3：时间戳转字符串；a2：上面分析过为 X-Device-ID 值；zf1.o：跟进查看为定值：public static final String o = "F403F982CA92F73AC142D50FFA69853D";
```

参数搞定，看 mq3.a 方法：

```
public static String a(String decrypt) throws DigestException {    try {        MessageDigest messageDigest = MessageDigest.getInstance("SHA-1");        messageDigest.update(decrypt.getBytes());        byte[] digest = messageDigest.digest();        StringBuffer stringBuffer = new StringBuffer();        for (byte b : digest) {            String hexString = Integer.toHexString(b & 255);            if (hexString.length() < 2) {                stringBuffer.append(0);     ...