---
title: 记一次帮丈母娘破解APP，满满的全是思路
url: https://forum.butian.net/share/4382
source: 奇安信攻防社区
date: 2025-05-30
fetch_date: 2025-10-06T22:23:45.345650
---

# 记一次帮丈母娘破解APP，满满的全是思路

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

### 记一次帮丈母娘破解APP，满满的全是思路

* [移动安全](https://forum.butian.net/topic/50)

事情是这样的，家里人从网上买了一个定位器，买之前也没问客服，结果到手之后一看竟然要收费才能使用，由于本来没多少钱后续就没退，然后我听了之后来了兴致，我想着能不能有什么漏洞能白嫖，于是有了本文，虽然最后解决也不难，不过我觉得最重要是满满的全是思路。

记一次帮丈母娘破解APP，满满的全是思路
====================
事情是这样的，家里人从网上买了一个定位器，买之前也没问客服，结果到手之后一看竟然要收费才能使用，由于本来没多少钱后续就没退，然后我听了之后来了兴致，我想着能不能有什么漏洞能白嫖，于是有了本文，虽然最后解决也不难，不过我觉得最重要是满满的全是思路。
主要是下面两个东西
- 定位器，里面有一张它出厂带的卡
- 查询位置所用的app一个
定位器这东西，我是没有lot经验所以就先不用看了，直接看安卓app
0x01 初步研究app
------------
拿出我的测试机，进入到app中会让你登录，登录的账号就是`定位器`的初始id，密码是123，进入后由于没有花钱，会出现一个弹窗，仔细看下图发现在弹窗后边我的设备显示在线，那是不是就意味着我只要让这个倒霉弹窗不再出现，我就可以点到后边我的设备，然后进行相关操作，于是想着关弹窗这种小活这不伸手就来，没想到这么简单，想想还有点小激动
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-752cae7e64dfc44ef7832eef3a933670bbaa5e51.png)
于是有了第一个思路，想着先用`开发助手`定位弹窗组件，然后用`算法助手pro`直接拦截掉，但是当我定位组件的时候发现这个组件没ID，如图这个id名字什么的竟然是空的，神奇。
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-c373d0e1668fdb5f065e6dcb08b60570fb34a3d8.png)
突然灵光一现，会不会是它不是个弹窗，由于后边的背景色是灰色，想着难不成直接弄了个`Activity`放到了前面
正想着，于是就有了第二个想法，直接用`MT`定位Activity，然后直接拦截这个Activity，太聪明了，没想到这么简单，想想还有点小激动
但是当我定位的时候发现，只有一个`MainActivity`这说明我的想法并不成立，难不成它还是个组件，只不过没名字
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-e79b651a29982883236dcdc02872b7b94a1128c9.png)
算了，正想着着实有点头痛，干脆直接看它代码吧，于是第三个思路，通过`待激活`关键字定位到相关代码，于是我下意识的拿出了我的脱壳机，不过没想到这家伙竟然没壳
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-acf79a29861716b4f5d76ceadd3721d602727abe.png)
正想着原来是我高看它了，那不分分钟手到擒来
直接拖到`jadx`搜索`待激活`，结果竟然没有
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-82a1200dc36f3e01d6fd7a7a17837e434d797800.png)
搜索`unicode`编码也没有
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-16baa4cb80f6668da163e38b3407909ca2eb8fd1.png)
这让我百思不得其解，再尝试搜索了其余的几个关键字没有结果后，没有办法的我没了办法，于是想着那干脆从流量层面看看吧
0x02 流量侧心酸突破历程
--------------
直接设置系统代理到我的`Burp`，然后打开发现
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-788ce91280bed0e4c489e7600db533c604742b51.png)
666，竟然还有代理检测，于是直接上`Postern`，走vpn代理到茶杯狐`Charles`的socks端口，结果还是不行
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-dd58e84b642631b153e2e5b517038c2fd60beeab.png)
没办法了，只好拿出了神器`frida`
```shell
adb shell
su
cd /data/local/tmp/
#测试机，启动frida服务
./frida-server-16.0.11-android-arm64
```
在本地新建了一个过代理检测的通杀脚本（来源：阿呆攻防）
```js
function wifi1\_proxy\_bypass(){
Java.perform(()=>{
var systemCls = Java.use('java.lang.System');
systemCls.getProperty.overload('java.lang.String').implementation = function (val) {
var ret = this.getProperty(val);
if (val == "http.proxyHost") {
return ""
}
if (val == "http.proxyPort") {
return "-1" // 这里改""/"0"/"-1"，我这里留的-1是之前金融项目好几家都是-1
}
return ret
}
})
}
function wifi2\_proxy\_bypass(){
Java.perform(function () {
var ConnectivityManager = Java.use('android.net.ConnectivityManager');
ConnectivityManager.getLinkProperties.implementation = function (network) {
var linkProperties = this.getLinkProperties(network);
if (linkProperties) {
var ProxyInfo = Java.use('android.net.ProxyInfo');
var proxyInfo = ProxyInfo.$new(null, null, 0);
linkProperties.setHttpProxy(proxyInfo);
}
return linkProperties;
};
});
}
function vpn1\_bypass(){
Java.perform(()=>{
var ConnectivityManager = Java.use('android.net.ConnectivityManager');
ConnectivityManager.getNetworkInfo.overload('int').implementation = function (networkType) {
var result = this.getNetworkInfo(networkType);
if (networkType === ConnectivityManager.TYPE\_VPN.value) {
return null;
}
return result;
};
})
}
function vpn2\_bypass() {
Java.perform(() => {
// 获取 NetworkCapabilities 类
var NetworkCapabilities = Java.use('android.net.NetworkCapabilities');
// Hook hasTransport 方法
NetworkCapabilities.hasTransport.overload('int').implementation = function (transportType) {
// 如果检测到 TRANSPORT\_VPN，返回 false
if (transportType === NetworkCapabilities.TRANSPORT\_VPN.value) {
console.log("[\*] VPN 检测被绕过");
return false;
}
// 否则调用原始方法
return this.hasTransport(transportType);
};
console.log("[\*] NetworkCapabilities.hasTransport 已 Hook");
});
}
function bypass\_proxy\_main(){
wifi1\_proxy\_bypass()
vpn1\_bypass()
}
setImmediate(bypass\_proxy\_main)
```
然后直接frida进行hook
```shell
.\frida.exe -U [APP进程] -l .\hook.js
```
发现正常请求走的通了，不过这个时候我的茶杯狐还没有抓取`https`流量，也就是说https的流量会经过茶杯狐，不过没有抓取ssl会导致它并不会利用茶杯狐的ssl证书做中转，我也就看不到对应的`http`报文的明文，看到的都是密文，不过好在软件使用的服务器的域名是知道了
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-d7c48943bbfaa61732b6ada191bbb03ddf27e8e9.png)
域名到手
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-0cbf45bfff3c2e93e345f2fe4a8cdcab6bba2212.png)
既然如此直接装好证书并信任，抓ssl，不点开没事，一抓https又完犊子了，这个时候我尝试了别的https请求是能抓到的，就这个app抓不到
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-a8d2410259bae43f292f91aefa7c0613b0700bb8.png)
666，竟然有校验，没关系，盲猜连壳都没有的app，撑死一个单向证书校验，把`LSB`的`JustTrustMe`一开，心想这不就成了，没想到这么简单
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-5a4bf78376ffc94fc8e79d25ebdc821517c7341d.png)
发现还是不行
难不成`双向证书校验`？由于我知道域名了，直接访问对方域名，发现提示400，不过报错信息跟正常的双向证书不一样，我想着一定是对方伪装了一下，兵法有云，实则虚之虚则实之，小小诡计岂能瞒得过我，双向证书校验，绝对双向证书校验
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-188345f83d81d3df0348febbf8f09c37cce82700.png)
然后我尝试搜了一下apk解包后有没有常见后缀`p12`、`cer`、`jks`等等的文件，发现并没有，按理说不能，这时想到难不成是伪装成了某个png文件，然后使用的时候在代码中又还原了出来？于是在代码中一顿找最后也没有。
思路转变一下，既然找不到证书，那么它加载本地证书的时候肯定是要读取本地证书文件的
既然如此废话不多说直接上`r0capture`，具体使用方法不多赘述，直接看它项目首页介绍https://github.com/r0ysue/r0capture
恭喜你猜对了又是0收获，既然如此我又用`objection`尝试HOOK了`java.io.File.$init`想着你总要读文件的吧
```shell
objection -g [app项目名] explore --startup-command "android hooking watch class\_method java.io.File.$init --dump-args
```
结果如你所想又是毫无收获，我彻底麻了，我原本以为一个连壳都不上的app能有多难搞，没想到这么强，于是跟朋友调侃了一下，就像斗地主一样，人家牌太好了直接明牌跟你玩不行吗
0x03 流量侧成功突破
------------
实在没得办法了，于是又冒出一个想法既然java代码搜不到，是不是在`so`层里面，说着看了眼lib目录，正想着这么多我选那个先分析好呢，突然看到`libflutter.so`等会，我记得flutter不是个语言吗？
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-96856a43d48b3b7e068428641d8bbb6a0b0da793.png)
于是直接开启上网冲浪模式，一顿冲浪下来，ok有解了
> 先说一下`flutter`，Flutter 是一个由 Google 开发的 \*\*开源 UI 框架\*\*，用于构建跨平台应用，也就是说，用一套代码可以同时生成 \*\*iOS、Android、Web 和桌面（Windows、macOS、Linux）\*\* 应用。
Flutter使用Dart编写，因此它不会使用系统CA存储，Dart使用编译到应用程序中的CA列表，Dart在Android上不支持代理，所以这就是为什么一开始使用系统代理没有生效的原因
当我们的应用存在`libflutter.so`的时候，其实就可以判断大概率为flutter的
还有一种方法是通过`flutter`的日志，如果有输出不仅可以判断出app是flutter写的，还看到对应的日志
```shell
adb shell
su
logcat |grep flutter
```
可以看到这个应用的所有请求和响应都在日志中
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/05/attach-981ac9d59515bac39c2490bd9e75562066d1d035.png)
下面这个函数是`flutter`的证书校验
```c++
static bool ssl\_crypto\_x509\_session\_verify\_cert\_chain(SSL\_SESSION \*session,
SSL\_HANDSHAKE \*hs,
uint8\_t \*out\_alert) {
\*out\_alert = SSL\_AD\_INTERNAL\_ERROR;
STACK\_OF(X509) \*const cert\_chain = session->x509\_chain;
if (cert\_chain == nullptr || sk\_X509\_num(cert\_chain) == 0) {
return false;
}
SSL \*const ssl = hs->ssl;
SSL\_CTX \*ssl\_ctx = ssl->ctx.get();
X509\_STORE \*verify\_store = ssl\_ctx->cert\_store;
if (hs->config->cert->verify\_store != nullptr) {
verify\_store = hs->config->cert->verify\_store;
}
X509 \*leaf = sk\_X509\_value(cert\_chain, 0);
const char \*name;
size\_t name\_len;
SSL\_get0\_ech\_name\_override(ssl, &name, &name\_len);
UniquePtr<X509\_STORE\_CTX> ctx(X509\_STORE\_CTX\_new());
if (!ctx ||
!X509\_S...