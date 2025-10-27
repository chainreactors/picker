---
title: 安卓API自动化安全扫描
url: https://www.anquanke.com/post/id/284187
source: 安全客-有思想的安全新媒体
date: 2022-12-15
fetch_date: 2025-10-04T01:29:32.160681
---

# 安卓API自动化安全扫描

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 安卓API自动化安全扫描

阅读量**4962143**

|评论**1**

发布时间 : 2022-12-14 14:30:14

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

## 背景

### 解决的问题

在日常的移动端安全审计，自动化审计一直停留在应用客户端，对于安卓应用中的网络API接口长期处于空白阶段，该方案主要想解决实际工作中移动安审自动化覆盖范围不全遗漏掉API相关内容的问题，同时对公司APP端的资产进行梳理，进一步完善公司移动应用SDL流程缺失的环节。

## API自动化扫描

### 扫描流程

先说整体的扫描流程：

一、业务测试人员提交APK到检测平台;

二、检测平台对APK进行静态分析结合动态监控的方式完成API资产的收集；

* 静态分析获取APK中静态的API信息；
* 动态监控通过模拟点击+VPN代理的方式捕获应用运行时与服务端的交互API信息；

三、检测平台完成API资产收集后开始进行请求数据的清洗，包括去除重复、无效的API信息；

四、将处理过的API资产信息发送给WEB扫描器，进行应用API的自动化扫描。

### 项目框架

框架图：

![]()

在整个过程中，主要需要解决的有以下两个问题：

* 如何实现API资产的自动化收集；
* 如何对应用内业务逻辑自动化触发。

## API资产收集

首先来看第一个问题，对于应用内API资产的收集有两个思路，一个是静态解析应用内的字符串，通过正则表达式的方式来识别出应用内的API资产，另一个思路是对应用的网络通信进行捕获来获取。鉴于一般应用的url链接都是动态拼接出来的，并且纯静态分析很难解析出API请求对应的数据格式，所以这里主要对第二种思路进行实践。

如何实现APP网络通信的捕获？

聊个老生常谈的话题：抓包，相信做过移动安全审计的小伙伴应该知道，App应用抓包不管是在协议分析还是渗透测试中都属于比较重要的一环，在拿到需要审计的应用后，首先会对应用是否加固进行检测，除了加固检测第二步就是对应用与服务端的请求进行抓包然后再根据请求数据包的内容来展开更深层次的审计。根据目的不同分析方向也有些差别，像协议分析主要是去apk中定位相应的处理函数或者其算法逻辑，对于渗透测试更多的则是对数据包中关键字段进行修改来检测服务端是否存在鉴权、越权、SQL注入等问题，但多数情况下渗透测试也会涉及到协议分析相关的工作。

### HTTP介绍

经常听到http协议、https协议，那它们有什么区别？http即超文本传输协议，采用明文的方式去传输数据，而https是http的升级，https在http协议的基础上加上了SSL/TLS功能，http协议负责建立客户端与服务端的网络通信，而SSL/TLS则负责通信的安全，包括传输数据的加密与身份的认证。

SSL与TLS的区别：TLS是SSL迭代的版本，因为HTTP协议传输的数据都是未加密的，所以为了保证这些明文数据能够进行安全传输，网景公司设计了SSL(Secure Sockets Layer)协议用于对HTTP协议传输的数据进行加密，SSL目前的版本是3.0。互联网标准化组织ISOC接替网景公司对SSL 3.0进行了升级，衍生出了TLS1.0(Transport Layer Security)，因此可以理解为TLS1.0=SSL3.1，目前TLS版本支持1.3。

![]()

### 安卓通信框架

对于安卓应用，有以下几种较常见的http通信方式，Apache的HttpClient类、Java提供的HttpsURLConnection类、Android提供的WebView以及第三方库比如OkHttp、Retrofit2。

其中HttpClinet在安卓6.0的时候就已经被废弃，安卓官方推荐使用HttpsURLConnection，但OkHttp和Retrofit2使用起来更方便、功能更多，所以大部分应用都采用OkHttp来实现网络通信。

### 常见抓包方案

#### 抓包原理

即中间人攻击，就是在通信双方的中间建立一个代理服务器。让客户端以为这个代理服务器就是真正的服务端，这样客户端一切的请求都会先发给中间服务器并由中间服务器代理转发给真实的服务端，而真实服务端的响应也都会被中间服务器接收，再由中间服务器转发给客户端。这样这个中间服务器就可对客户端与真实服务端通信的数据进行拦截、监听、篡改、重放等操作。

![]()

#### 抓包工具

对于HTTP的抓包工具在PC端的主要有BurpSuitePro、Fiddler4、Charles等工具，客户端主要有HttpCanary(小黄鸟)，对于一些不使用HTTP/HTTPS协议传输数据的app，还可以使用tcpdump来进行抓包，抓到的包可以使用wireshark工具进行解析，最后就是基于frida的r0capture也比较好用。

![]()

#### WIFI代理

1.首先将安装了客户端应用的手机与安装了抓包工具的PC处于同一网段，也就是连上同一wifi；
2.其次将手机的wifi设置为手动代理，代理主机IP设置为PC的IP，端口设置为8888（随便设置，只要和抓包工具一致）；
4.然后打开PC上的抓包工具并配置监听端口开始进行代理抓包工作；
5.最后还需要通过手机浏览器访问以下抓包工具的证书下载地址，进行证书安装，安卓完成后即可进行抓包。

* [BurpSuite\_pro](http://burp)
* [Charles-proxy](http://chls.pro/ssl)
* [Fiddler](http://ipv4.fiddler:8888/)

注意：当应用的targetSdkVersion到28后会发现在Android7.0及以上机型上抓不到包，主要原因是应用不再信任客户端用户自己安装的证书，除非App应用自身明确开启用户证书信任的功能。
来看下7.0之前App的配置与7.0及之后的配置有什么不一样。

6.0的”res/xml/network\_security\_config.xml”文件

```
<base-config cleartextTrafficPermitted="true">
    <trust-anchors>
        <certificates src="system" />
    </trust-anchors>
</base-config>
```

7.0的”res/xml/network\_security\_config.xml”文件

```
<base-config cleartextTrafficPermitted="true">
    <trust-anchors>
        <certificates src="system" />
        <certificates src="user" />
    </trust-anchors>
</base-config>
```

因为我们自己安装的证书属于user域，可以看到配置取消了对user域证书的信任。
想要在7.0及7.0以上的手机上进行抓包，可以从以下几个点入手。
1.最简单的方法，就是重新配置，修改配置文件支持对user域证书的信任。

* 具体配置详情请看官方介绍:<https://developer.android.com/training/articles/security-config>

2.将我们的证书添加到系统证书的目录，这样我们的证书就是系统证书，也就会被信任了。

* 方法一：/system/etc/security/cacerts目录包含每个已安装根证书的问题，在有root的情况下重新挂载/system目录，并将我们的证书拷贝到该目录。
* 方法二：使用Magisk自定义模块[MagiskTrustUserCerts](https://github.com/NVISOsecurity/MagiskTrustUserCerts)，将任何用户证书识别为系统证书。

#### VPN隧道

除了可以通过WIFI设置代理进行抓包还有一种方式就是在安卓设备上创建VPN隧道来配合抓包工具进行抓包，VPN隧道属于七层协议的网络层，设备在开启VPN后会多出一个网络接口，相当于多加了个虚拟网卡，所有流量都会走这个新增的虚拟网卡，这样应用层和传输层的请求数据就都能捕获。
开启VPN可以使用postern应用来完成，然后配置下代理服务器地址以及规则，即可在PC端使用抓包软件进行抓包。

![]()

如果觉得上面的设置流程较麻烦，那么直接选择HttpCanary(小黄鸟)吧，该应用的抓包原理也是基于VPN实现的，安装完即配置完，比较方便，配合[AnLink](https://anl.ink/)投屏工具用起来更丝滑。需要注意的点：有些应用会检测是否存在HttpCanary，所以可以先将目标软件打开后再启动HttpCanary应用进行抓包。

#### 透明代理

最后一种叫透明代理(路由重定向)，顾名思义就是可以让客户端感觉不到代理的存在。该方法主要依赖linux上的iptables命令行工具的流量转发功能，用户不需要设置代理服务器，设置下默认网关即可。当设备访问外部网络时，客户端的数据包会被转发到设置的默认网关上，通过默认网关的路由，最终到达目标服务器。该方案可以适用在设备不支持WIFI代理设置并且不能安装第三方应用的情况下，比如对机车进行抓包时。

首先需要在手机上使用su权限设置将设备所有tcp流量转发到指定IP(172.20.10.9)的电脑上。

```
iptables -t nat -A OUTPUT -d 0.0.0.0/0 -p tcp -j DNAT --to 172.20.10.9   #设置重定向
iptables -t nat -D OUTPUT -d 0.0.0.0/0 -p tcp -j DNAT --to 172.20.10.9   #取消重定向
# 可以将0.0.0.0/0替换成指定IP可以极度精细化控制每一条流。
```

然后再重定向的电脑上开启BurpSuite并配置对HTTP/HTTPS的默认端口80和443进行监听。

![]()

### 抓包防护

根据前面的内容我们可以看到，攻击者想要抓包其实是很容易的，那作为开发者如何去增加应用的防护能力，来避免应用的业务数据被中间人抓包获取呢？这里整理了以下几种方法供大家参考；

* 方法一：使用系统API进行常规检测，包括是否设置了WIFI代理，是否开启VPN等；
* 方法二：通过设置让APP请求时不用系统代理来绕过WIFI代理抓包；
* 方法三：自定义Sooket实现HTTP/HTTPS；
* 方法四：使用证书校验的方式来验证服务端是否为信任的服务端(双向认证和证书锁定)；

实际情况中遇到的比较多的有上面的第一种，第二种和第四种，第三种目前遇到的较少。

#### WIFI代理检测

最基础的抓包就是设置WIFI代理进行抓包，所以就可以从WIFI代理入手，检测当前的WIFI环境是否安全，是否被设置了代理服务器和代理端口，当检测到存在代理时就判定为用户正在使用抓包，这样我们就能采取一些措施，比如退出应用；
WIFI代理的检测代码如下：

```
public static boolean isWifiProxy(Context context) {
    final boolean IS_ICS_OR_LATER = Build.VERSION.SDK_INT >= Build.VERSION_CODES.ICE_CREAM_SANDWICH;    // 判断安卓版本
    String proxyAddress;
    int proxyPort;
    if (IS_ICS_OR_LATER) {
        proxyAddress = System.getProperty("http.proxyHost");    // 获取代理主机
        String portStr = System.getProperty("http.proxyPort");  // 获取代理端口
        proxyPort = Integer.parseInt((portStr != null ? portStr : "-1"));
    } else {
        proxyAddress = android.net.Proxy.getHost(context);
        proxyPort = android.net.Proxy.getPort(context);
    }
    Log.i("代理信息", "proxyAddress :" + proxyAddress + "prot :" + proxyPort);
    return (!TextUtils.isEmpty(proxyAddress)) && (proxyPort != -1);
}
```

#### 设置不走系统代理

对于WIFI代理抓包，除了可以通过检测进行防护，还可以通过网络请求时设置不走系统代理来绕过，检测代码如下：

```
public void run() {
    Looper.prepare();
    OkHttpClient okHttpClient = new OkHttpClient.Builder().
        proxy(Proxy.NO_PROXY).      // 使用此参数，可绕过系统代理直接发包
        build();
    Request request = new Request.Builder()
        .url("http://www.baidu.com")
        .build();
    Response response = null;
    try {
        response = okHttpClient.newCall(request).execute();
        Toast.makeText(this, Objects.requireNonNull(response.body()).string(), Toast.LENGTH_SHORT).show();
    } catch (IOException e) {
        e.printStackTrace();
    }
    Looper.loop();
}
```

#### VPN检测

VPN检测的检测有两种方式，因为创建VPN隧道会新增一个网络接口，一般是”tun0”或”ppp0”，所以VPN的第一种检测原理是对设备网络接口进行检测，当发现存在”tun0”或”ppp0”的接口时，则判定存在VPN抓包。

```
public boolean isInVPN() {
    try {
        Enumeration<NetworkInterface> networkInterfaces = NetworkInterface.getNetworkInterfaces();
        while(networkInterfaces.hasMoreElements()){
            String name = networkInterfaces.nextElement().getName();
            if (name.equals("tun0") || name.equals("ppp0")) {
                return true;
            }
        }
    } catch(SocketException e) {
        e.printStackTrace();
    }
    return false;
}
```

第二种检测则比较简单，直接使用系统服务，获取当前网络的状态来判定是否使用了VPN。

```
@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
private final boolean hasVpnTransport(Network network, ConnectivityManager connectivityManager) {
    NetworkCapabilities networkCapabilities = connectivityManager.getNetworkCapabilities(network);
    return networkCapabilities != null && networkCapabilities.hasTransport(NetworkCapabilities.TRANSPORT_VPN);
}

@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
private final boolean isInVPN(Context context){
    Object systemService = context.getSystemService(Context.CONNECTIVITY_SERVICE);
    if(systemService != null) {
        ConnectivityManager connectivityManager = (ConnectivityManager) systemService;
        boolean isInVpn = false;
        if (Build.VERSION.SDK_INT >= 23) {
            Network activeNetwork = connectivityManager.getActiveNetwork();
            isInVpn = hasVpnTransport(activeNetwork, conn...