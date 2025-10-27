---
title: JsRpc+Yakit热加载实现明文编辑加密发包
url: https://forum.butian.net/share/4452
source: 奇安信攻防社区
date: 2025-07-15
fetch_date: 2025-10-06T23:16:27.007496
---

# JsRpc+Yakit热加载实现明文编辑加密发包

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

### JsRpc+Yakit热加载实现明文编辑加密发包

* [渗透测试](https://forum.butian.net/topic/47)

引言
在渗透测试过程中，常常会遇到前端对请求数据进行加密的情况，增加了分析与利用的难度。传统方法通常依赖于 JavaScript 逆向工程，不仅可能需要搭建复杂的运行环境，即使完整提取了加密代...

\*\*引言\*\*
======
在渗透测试过程中，常常会遇到前端对请求数据进行加密的情况，增加了分析与利用的难度。传统方法通常依赖于 JavaScript 逆向工程，不仅可能需要搭建复杂的运行环境，即使完整提取了加密代码，也难以在本地准确还原加解密逻辑，严重影响测试效率。
为提升效率，本文将介绍一种基于 \*\*JsRpc + Yakit 热加载\*\* 的实用方法，实现前端明文数据的直接编辑与自动加密发包。通过 JsRpc 的远程方法调用机制，我们无需还原整个运行环境，只需定位加密函数即可调用，从而快速绕过加密层，专注业务逻辑测试。
本文测试环境基于 Yakit 自带靶场，所用工具及项目地址如下：
JsRpc 项目地址：<https://github.com/jxhczhl/JsRpc>
Yakit 项目地址：[https://yaklang.com/products/download\\_and\\_install/](https://yaklang.com/products/download\_and\_install/)
\*\*操作步骤\*\*
========
\*\*安装并启动yakit靶场\*\*
----------------
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-c06548cf5a10aa26bfe73261cc7d33ecf686e5d2.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-48b35aedd1682758226c18f6a6722964b90146c0.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-3faeebc3b7cb558f79a834b1f613c7bbc2896b62.png)
如下图所示，在抓包过程中可以观察到请求中包含名为 `signature` 的参数，即请求的签名字段。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-2edd8a1c645612e1fcbaa388809ba7b414de72f5.png)
如下图所示，通过分析 JavaScript 代码可以确认，签名（`signature`）是对 `username` 和 `password` 两个参数进行加签生成的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0656302f6bec2d2401efa9afc0fc68b6419bede2.png)
当然，靶场中的 JavaScript 加密逻辑相对简单，但实际测试的整体思路是通用的。本文不重点讲解如何定位加解密函数——在实际渗透过程中，常会遇到动态 key、接口返回参与签名的参数等情况，这些问题通过多构造几次 `yak` 函数即可应对。
根据 JavaScript 中的加密逻辑，在浏览器控制台手动执行一次加密操作，生成的 `signature` 与初始抓包结果一致，说明还原无误。
若加解密函数定义在局部作用域中（如某函数内部或模块作用域），在浏览器控制台中可能无法直接访问，此时可通过将函数挂载到 `window` 对象的方式，提升为全局可调用函数。在当前靶场环境中，加解密函数已位于全局作用域，因此无需额外处理
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-6e7d1e4d0fb8270a08d7c5dc7277623c5ea174ba.png)
\*\*JsRpc食用\*\*
-----------
关于JsRpc的详细解释可移步至<https://mp.weixin.qq.com/s/vHoVPINf4GKhR36LSQlDXw>，小天师傅讲的很详细。
### \*\*注入JS，构建通信环境（\*\*[\*\*/resouces/JsEnv\\_De.js\*\*](https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\_Dev.js)\*\*）\*\*
将[https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\\_Dev.js](https://github.com/jxhczhl/JsRpc/blob/main/resouces/JsEnv\_Dev.js)代码复制到控制台
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-55a062933f10fd4bb4a7dbdd4e734a67f0037037.png)
### \*\*远程调用： 浏览器预先注册js方法 传递函数名调用\*\*
`resolve(Encrypt(decoded));` 实际上调用的是 JavaScript 文件中的 `Encrypt(word)` 函数。
```js
// 注入环境后连接通信
var demo = new Hlclient("ws://127.0.0.1:12080/ws?group=Encrypt");
demo.regAction("Encrypt", function (resolve,param) {
var decoded = atob(param);
resolve(Encrypt(decoded));
})
```
如果目标函数需要传递多个参数，JsRpc 项目中（<https://github.com/jxhczhl/JsRpc>）提供了“多参数调用”的示例，可供参考。
运行服务端后，控制台会输出日志，并在有客户端连接时显示上线提示信息，方便实时监控调用情况。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-5517d4f8d16003a13e1569dc4840e83fc961a2b9.png)
通过调用接口并传递参数，可以获取加签后的结果。为了确保参数在传输过程中不被解析异常，建议对其进行 Base64 编码，尤其是在渗透测试过程中频繁修改参数的情况下。如果参数中包含特殊字符，未编码可能导致解析错误或请求失败。
在实际调用中，注入的代码中包含 `var decoded = atob(param);`，会先对传入的参数进行 Base64 解码，然后将解码后的值传入加签函数进行处理。
[http://127.0.0.1:12080/go?group=Encrypt&amp;action=Encrypt&amp;param=dXNlcm5hbWU9YWRtaW4mcGFzc3dvcmQ9YWRtaW4=](http://127.0.0.1:12080/go?group=Encrypt&action=Encrypt&param=InVzZXJuYW1lPWFkbWluJnBhc3N3b3JkPWFkbWluIg==)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0e02503d5560a11f3ef467c0cc647a372fe1dce7.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-37c1e1525b39f44187b80aaf4e2aa2c5446beb57.png)
\*\*yakit webfuzz热加载\*\*
--------------------
### \*\*yak runner运行调试\*\*
我们可以使用 `yak` 编写一个脚本，用于获取加签后的结果。脚本示例如下：
```js
# port scan plugin
yakit.AutoInitYakit()
handleCheck = func(target,port,word){
addr = str.HostPort(target, port)
isTls = str.IsTLSServer(addr)
packet = `
GET /go?group=Encrypt&action=Encrypt&param={{params(word)}} HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Host: {{params(target)}}
`
rsp,req,\_ = poc.HTTP(packet,
poc.params({"target":addr,"word":word}),
poc.https(isTls),
poc.redirectTimes(0),
)
println(req)
if len(rsp) > 0 {
body = poc.GetHTTPPacketBody(rsp)
printf("获取加密结果：\n"+string(body))
jsonObj = json.loads(string(body))
// 获取字段值
sign = jsonObj["data"]
return sign
}else{
println("失败")
}
return
}
func base\_word(name,passwd){
word = "username=" + name + "&password="+passwd
return codec.EncodeBase64(word)
}
word = base\_word("admin","admin")
sign = handleCheck("127.0.0.1",12080,word)
println("\nsign:"+sign)
// signRequest = result => {
// pairs := result.SplitN("|", 2)
// dump(pairs)
// word = base\_word(pairs[0], pairs[1])
// sign = handleCheck("127.0.0.1",12080,word)
// return sign
// }
```
经过运行调试，成功获取到加签结果，验证无误。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-093044fa045f30f7733cf39e249ada79a4dde8b0.png)
### \*\*热加载脚本\*\*
热加载和 Yak Runner 仅有细微差别，脚本可直接按照 Yakit 语法编写。主要加密逻辑集中在 `signRequest` 函数中；如果加密参数需要动态获取，可通过封装多个辅助函数来实现。
```js
# port scan plugin
yakit.AutoInitYakit()
handleCheck = func(target,port,word){
addr = str.HostPort(target, port)
isTls = str.IsTLSServer(addr)
packet = `
GET /go?group=Encrypt&action=Encrypt&param={{params(word)}} HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br, zstd
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Host: {{params(target)}}
`
rsp,req,\_ = poc.HTTP(packet,
poc.params({"target":addr,"word":word}),
poc.https(isTls),
poc.redirectTimes(0),
)
println(req)
if len(rsp) > 0 {
body = poc.GetHTTPPacketBody(rsp)
printf("获取加密结果：\n"+string(body))
jsonObj = json.loads(string(body))
// 获取字段值
sign = jsonObj["data"]
return sign
}else{
println("失败")
}
return
}
func base\_word(name,passwd){
word = "username=" + name + "&password="+passwd
return codec.EncodeBase64(word)
}
// word = base\_word("admin","admin")
// sign = handleCheck("127.0.0.1",12080,word)
// println("\nsign:"+sign)
signRequest = result => {
pairs := result.SplitN("|", 2)
dump(pairs)
//接收两个参数，按照yakit语法写即可 {{yak(signRequest|admin|admin)}}
word = base\_word(pairs[0], pairs[1])
sign = handleCheck("127.0.0.1",12080,word)
return sign
}
```
调试运行通过后，即可修改参数进行发包操作，批量处理同样支持，效率大幅提升。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-53c1c7a891c97966cac01aa64e1def6434c2907b.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-0a2dcc162cfa8d9aa37f184b48f29f81226e5d3f.png)
\*\*参考资料：\*\*
=========
<https://github.com/jxhczhl/JsRpc>
[https://yaklang.com/articles/vulnerability\\_testing\\_after\\_being\\_encrypted\\_by\\_the\\_front-end](https://yaklang.com/articles/vulnerability\_testing\_after\_being\_encrypted\_by\_the\_front-end)
<https://mp.weixin.qq.com/s/vHoVPINf4GKhR36LSQlDXw>

* 发表于 2025-07-14 14:03:47
* 阅读 ( 3642 )
* 分类：[渗透测试](https://forum.butian.net/community/Pen_Testing)

5 推荐
 收藏

## 1 条评论

[![](https://forum.butian.n...