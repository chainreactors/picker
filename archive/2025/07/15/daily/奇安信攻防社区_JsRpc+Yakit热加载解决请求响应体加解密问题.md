---
title: JsRpc+Yakit热加载解决请求响应体加解密问题
url: https://forum.butian.net/share/4455
source: 奇安信攻防社区
date: 2025-07-15
fetch_date: 2025-10-06T23:16:24.376690
---

# JsRpc+Yakit热加载解决请求响应体加解密问题

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### JsRpc+Yakit热加载解决请求响应体加解密问题

* [渗透测试](https://forum.butian.net/topic/47)

引言
继上一期（传送门：https://forum.butian.net/share/4452 ）我们探讨了如何利用 JsRpc 与 Yakit 热加载技术，实现对加密请求的明文编辑与自动发包后，本期我们将焦点转向一个更为复杂的场...

引言
==
继上一期（传送门：<https://forum.butian.net/share/4452> ）我们探讨了如何利用 \*\*JsRpc 与 Yakit 热加载\*\*技术，实现对加密加签请求的明文编辑与自动发包后，本期我们将焦点转向一个更为复杂的场景：\*\*请求与响应双向加密\*\*。
当服务器返回的数据也是密文时，传统的测试流程将完全失效。本文将\*\*不再赘述如何定位具体的加解密函数\*\*，而是假定您已找到目标函数。在此基础上，我们将深入演示 \*\*JsRpc 的核心用法\*\*——如何将其作为桥梁，去调用前端页面中的解密函数；并展示 \*\*Yakit 热加载的强大之处\*\*——如何无缝集成 JsRpc 的调用能力，实现对返回流量的自动化实时解密。
本文旨在展示一种高效的工具联动思路，帮助测试人员彻底摆脱加解密的束缚，实现端到端的明文测试。
本文测试环境基于 Yakit 自带靶场，所用工具及项目地址如下：
JsRpc 项目地址：<https://github.com/jxhczhl/JsRpc>
Yakit 项目地址：[https://yaklang.com/products/download\\_and\\_install/](https://yaklang.com/products/download\_and\_install/)
解密前：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-4e7124edb87cac568d77aa466a052e40aa808128.png)
解密后：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-50a7f521620946758f89a5a3888c1cc871e66397.png)
\*\*操作步骤\*\*
========
\*\*安装并启动yakit靶场\*\*
----------------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-4c12faa6ec0021d856943c45920613a89b5a8c83.png)
我们首先需要\*\*定位前端的加解密函数\*\*，然后在浏览器控制台中进行验证，确认这些函数是否能够\*\*正确处理我们抓包得到的\*\* \*\*message\*\* \*\*数据\*\*，实现预期的加密或解密效果。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-cfa64452099cde1b2603b66d0984d4f59d656475.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f18a8b7077a7be4bcb16e9cd716fb4752c771ac4.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-8c9fcf72a084a5ce25342541a840899f2d609dce.png)
\*\*JsRpc食用\*\*
-----------
关于JsRpc的详细解释可移步至<https://mp.weixin.qq.com/s/vHoVPINf4GKhR36LSQlDXw>，小天师傅讲的很详细。
### \*\*注入JS，构建通信环境（\*\*[\*\*/resouces/JsEnv\\_De.js\*\*](https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\_Dev.js)\*\*）\*\*
将[https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\\_Dev.js](https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\_Dev.js)代码复制到控制台
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-bc243c82cbf9f298c8df87a164145cffeb57042f.png)
### \*\*远程调用（加密）： 浏览器预先注册js方法 传递函数名调用\*\*
通过对加密函数的分析可以确认，该加密方式为 \*\*AES-CBC 模式，使用 PKCS7 填充\*\*，其中 \*\*key 和 iv 均为随机生成\*\*。既然是随机生成的，我们完全可以在脚本中\*\*将其固定下来\*\*，以便复现加密过程并实现稳定可控的加解密操作。
由于加密函数只依赖一个 message 参数，\*\*key 和 iv 可以在辅助函数中固定\*\*，因此我们只需在控制台\*\*编写一个辅助函数\*\*，用于接收待加密的 message 并调用原始加密逻辑即可。
```js
//控制台执行
window.myEncrypt = function(data) {
// 1.将 key 和 iv 都从十六进制字符串解析成 WordArray 格式，key与iv是随机生成的自然也能固定。
const key = CryptoJS.enc.Hex.parse("6190987ec48f0394752f09a81ee869a2");
const iv = CryptoJS.enc.Hex.parse("557784509b449b0d67287c1b53571e72");
// 如果传入的是对象，最好先转为 JSON 字符串
const message = typeof data === 'object' ? JSON.stringify(data) : data;
const encryptedResultObject = CryptoJS.AES.encrypt(
message,
key, // 使用解析后的 key
{
iv: iv, // 使用解析后的 iv
mode: CryptoJS.mode.CBC,
padding: CryptoJS.pad.Pkcs7
}
);
// 2.对返回的原始对象调用 .toString() 来获取密文字符串
return encryptedResultObject.toString();
};
```
接下来，我们对刚刚创建的辅助函数进行测试，\*\*验证其加密结果是否与原始加密逻辑一致，确保功能正确\*\*。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-966bbef5abbd100fc58da12205b8c8fb5a53770f.png)
```js
//控制台执行
var demo = new Hlclient("ws://127.0.0.1:12080/ws?group=encrypt");
//写一个传入字符串，返回base64值的接口(调用内置函数atob)
demo.regAction("encrypt", function (resolve,param) {
//这样添加了一个param参数，http接口带上它，这里就能获得
var params = atob(param)
//通过js代码分析formData其实是一个对象，而这里的参数是字符串，我们需要处理下，不然加密结果会不一样。这不是一个符合json的字符串数据所以不能使用JSON.parse，通过eval可解决。
esultObject = eval('(' + params + ')');
resolve(myEncrypt(esultObject));
})
```
在控制台注入辅助 JS 代码后，我们可以进行简单测试：\*\*使用抓包获取的 key 和 iv 对数据进行加密\*\*，然后将加密结果与原始请求中的密文进行对比。\*\*如果加密结果一致，说明函数逻辑无误，可以正常复用\*\*。
如下图所示，加密结果与原始数据一致，验证通过：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f76bea8421088653a78808de0a3b102307031ff8.png)
随后，我们通过 \*\*JsRpc 工具提供的接口\*\*对请求数据进行编码并发包测试。\*\*加密结果与原始请求保持一致，说明流程无误，可正常使用。\*\*
```php
e3VzZXJuYW1lOiAnYWRtaW4nLCBwYXNzd29yZDonYWRhc2Rmc2RmJ30=
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-21d977e4f6725ca2bb41353905300bcbed877884.png)
[http://127.0.0.1:12080/go?group=encrypt&amp;action=encrypt¶m=e3VzZXJuYW1lOiAnYWRtaW4nLCBwYXNzd29yZDonYWRhc2Rmc2RmJ30=](http://127.0.0.1:12080/go?group=encrypt&amp;action=encrypt&amp;param=e3VzZXJuYW1lOiAnYWRtaW4nLCBwYXNzd29yZDonYWRhc2Rmc2RmJ30=)
结果一致，没有问题。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e7312b67d2b0f89219adc3a4d3fd204018abb79c.png)
### \*\*远程调用（解密）： 浏览器预先注册js方法 传递函数名调用\*\*
接下来，我们按照相同的思路编写一个辅助函数，用于对响应体进行解密。由于 AES-CBC 模式下的 \*\*key、iv 和密文（message）每次都会变化\*\*，因此该函数需要同时接收这三个参数，才能正确还原原始数据。
```js
//控制台执行
window.get\_decrypt = function(key,iv,message) {
const decrypted = CryptoJS.AES.decrypt(
message,
CryptoJS.enc.Hex.parse(key),
{
iv: CryptoJS.enc.Hex.parse(iv),
mode: CryptoJS.mode.CBC,
padding: CryptoJS.pad.Pkcs7
}
);
decryptedData = JSON.parse(decrypted.toString(CryptoJS.enc.Utf8));
return decryptedData;
};
```
为了验证加密结果的正确性，我们在控制台中调用解密函数对返回的数据进行还原。需要注意的是，由于 AES-CBC 模式下的 \*\*key 和 iv 每次都会随机生成\*\*，因此 \*\*每次的 key、iv 和 message 都不相同\*\*，这是正常现象。
```js
//解密
const decrypted = CryptoJS.AES.decrypt(
"9BmCEL2x8hRojOyzoqeKY7z5PSuRDtB5jl4e+z0dTEC2+80pmm1VIiOGEcNh349J+nN/1xzYZBchRV3+21ikjY+NrXVdIwVfYbfkbNO8ieHR0KyUkUqtNn7NBsHCU6gqpZifd0IY3LUj0P0pjcWD8Jxs+1Pn2ncj1WW2yhvkQwf3GBoujkv5ylxv6ZCrXCml",
//key
CryptoJS.enc.Hex.parse("43dcc720aaabdb65c39b90cb71e2b8d6"),
{
iv: CryptoJS.enc.Hex.parse("825608c3018f0b8468923d23426caa77"),
mode: CryptoJS.mode.CBC,
padding: CryptoJS.pad.Pkcs7
}
);
decryptedData = JSON.parse(decrypted.toString(CryptoJS.enc.Utf8));
```
测试结果显示，解密过程正常，\*\*密文能够成功还原为原始数据\*\*，验证通过。
认证失败：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-da936a257dbf1d1cac79e5753d964a2ac54a6249.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-63d3999aaf520bc9ea5999c7f1f259e855d16096.png)
认证成功：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1188e04af660fd98524c4c4c74e0f72ea4849222.png)
```js
//注入js方法，多参
var demo = new Hlclient("ws://127.0.0.1:12080/ws?group=get\_decrypt");
demo.regAction("get\_decrypt", function (resolve,param) {
//这里还是param参数
res=get\_decrypt(param["key"],param["iv"],param["message"])
resolve(res);
})
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-772b68cbb06bd57c12d691bbca253b75d8638a34.png)
接下来，我们使用 JsRpc 的解密接口对响应数据进行处理。由于需要传递多个参数，发包操作由 Python 脚本完成，以提高灵活性和可控性。
```py
import requests
import json
url = "http://127.0.0.1:12080/go"
data = {
"group": "get\_decrypt",
"action": "get\_decrypt",
"param": json.dumps({"key":"9ca83c435044b0750777c05dec8df6bd" ,"iv": "fc973c1d2895d89b445989939381b18c","message":"gcCZ3CRVQa7C1ZSTH06+Rfjz7E8x63WKTexphNg9YKcBpcUhW7yRnpMw+115wDO8XEqM12ECpCiP+7vfQDjkj08osdjmZhBw0EDZOv2FEBo=" })
}
print(data["param"])
res=requests.post(url, data=data)
print(res.text)
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f050b2d4f727f7777589cc4f78ff420f4ecebcd6.png)
```php
POST /go HTTP/1.1
Host: 127.0.0.1:12080
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate
Accept: \*/\*
Connection: keep-alive
Content-Leng...