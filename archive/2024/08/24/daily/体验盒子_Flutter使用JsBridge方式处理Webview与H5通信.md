---
title: Flutter使用JsBridge方式处理Webview与H5通信
url: https://www.uedbox.com/post/69699/
source: 体验盒子
date: 2024-08-24
fetch_date: 2025-10-06T18:05:07.981231
---

# Flutter使用JsBridge方式处理Webview与H5通信

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# Flutter使用JsBridge方式处理Webview与H5通信

* 发表于 2024年08月23日
* [flutter](https://www.uedbox.com/design/flutter/)

使用Flutter进行项目开发加载H5页面时，打开H5页面需要使用WebView组件。同时，为了和H5页面进行数据交换，有时候还需要借助JSBridge来实现客户端与H5之间的通讯。除此之外，Hybrid开发模式也需要Webview与JS做频繁的交互。下面是实现方法。

目录表

Toggle

* [安装](#%E5%AE%89%E8%A3%85)
* [基本使用](#%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8)
  + [JS调用Flutter](#JS%E8%B0%83%E7%94%A8Flutter)
    - [javascriptChannels方式](#javascriptChannels%E6%96%B9%E5%BC%8F)
    - [navigationDelegate](#navigationDelegate)
* [JSBridge](#JSBridge)

## 安装

本文使用的是Flutter官方的webview\_flutter组件，目前的最新版本是0.3.19+9。使用前需要先添加webview\_flutter插件依赖，如下所示。

|  |  |
| --- | --- |
| 1 | webview\_flutter: 0.3.19+9 |

然后，使用flutter packages get命令将插件拉取到本地并保持依赖。由于加载WebView需要使用网络，所以还需要在android中添加网络权限。打开目录android/app/src/main/AndroidManifest.xml，然后添加如下代码即可。

|  |  |
| --- | --- |
| 1 | <uses-permission android:name="android.permission.INTERNET"/> |

由于iOS在9.0版本默认开启了Https，所以要运行Http的网页，还需要在ios/Runner/Info.plist文件中添加如下代码。

|  |  |
| --- | --- |
| 1  2 | <key>io.flutter.embedded\_views\_preview</key>  <string>YES</string> |

## 基本使用

打开WebView组件的源码，WebView组件的构造函数如下所示。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18 | const WebView({  Key key,  this.onWebViewCreated,  this.initialUrl,  this.javascriptMode = JavascriptMode.disabled,  this.javascriptChannels,  this.navigationDelegate,  this.gestureRecognizers,  this.onPageStarted,  this.onPageFinished,  this.debuggingEnabled = false,  this.gestureNavigationEnabled = false,  this.userAgent,  this.initialMediaPlaybackPolicy =  AutoMediaPlaybackPolicy.require\_user\_action\_for\_all\_media\_types,  })  : assert(javascriptMode != null),  assert(initialMediaPlaybackPolicy != null),  super(key: key); |

其中，比较常见的属性的含义如下：

* onWebViewCreated：在WebView创建完成后调用，只会被调用一次；
* initialUrl：初始load的url；
* javascriptMode：JS执行模式（是否允许JS执行）；
* javascriptChannels：JS和Flutter通信的Channel；
* navigationDelegate：路由委托（可以通过在此处拦截url实现JS调用Flutter部分）；
* gestureRecognizers：手势监听；
* onPageFinished：WebView加载完毕时的回调。import 'dart:async';

使用Webview加载网页时，很多时候需要与JS进行交互，即JS调用Flutter和Flutter调用JS。Flutter调用JS比较简单，直接调用 \_controller.evaluateJavascript()函数即可。而JS调用Flutter则比较烦一点，之所以比较烦，是因为javascriptChannels目录只支持字符串类型，并且JS的方法是固定的，即只能使用postMessage方法，对于iOS来说没问题，但是对于Android来说就有问题，当然也可以通过修改源码来实现。

### JS调用Flutter

#### javascriptChannels方式

javascriptChannels方式也是推荐的方式，主要用于JS给Flutter传递数据。例如，有如下JS代码。

|  |  |
| --- | --- |
| 1  2  3  4 | <button onclick="callFlutter()">callFlutter</button>  function callFlutter(){  Toast.postMessage("JS调用了Flutter");  } |

使用postMessage方式 Toast 是定义好的名称，在接受的时候要拿这个名字 去接收，Flutter端的代码如下。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | WebView(  javascriptChannels: <JavascriptChannel>[  \_alertJavascriptChannel(context),  ].toSet(),  )    JavascriptChannel \_alertJavascriptChannel(BuildContext context) {  return JavascriptChannel(  name: 'Toast',  onMessageReceived: (JavascriptMessage message) {  showToast(message.message);  });  } |

#### navigationDelegate

除此之外，另一种方式是navigationDelegate，主要是加载网页的时候进行拦截，例如有下面的JS协议。

|  |  |
| --- | --- |
| 1 | document.location = "js://webview?arg1=111&args2=222"<em>;</em> |

对应的Flutter代码如下。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11 | navigationDelegate: (NavigationRequest request) {  if (request.url.startsWith('js://webview')) {  showToast('JS调用了Flutter By navigationDelegate');  print('blocking navigation to $request}');  Navigator.push(context,  new MaterialPageRoute(builder: (context) => new testNav()));  return NavigationDecision.prevent;  }  print('allowing navigation to $request');  return NavigationDecision.navigate;    <em>//必须有</em>  }, |

其中，NavigationDecision.prevent表示阻止路由替换，NavigationDecision.navigate表示允许路由替换。

## JSBridge

除此之外，我们还可以自己开发JSBridge，并建立一套通用规范。首先，需要与H5开发约定协议，建立Model。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28 | class JsBridge {  String method; <em>// 方法名</em>  Map data; <em>// 传递数据</em>  Function success; <em>// 执行成功回调</em>  Function error; <em>// 执行失败回调</em>    JsBridge(this.method, this.data, this.success, this.error);    <em>/// jsonEncode方法中会调用实体类的这个方法。如果实体类中没有这个方法，会报错。</em>  Map toJson() {  Map map = new Map();  map["method"] = this.method;  map["data"] = this.data;  map["success"] = this.success;  map["error"] = this.error;  return map;  }    static JsBridge fromMap(Map<String, dynamic> map) {  JsBridge jsonModel =  new JsBridge(map['method'], map['data'], map['success'], map['error']);  return jsonModel;  }    @override  String toString() {  return "JsBridge: {method: $method, data: $data, success: $success, error: $error}";  }  } |

然后，对接收到的H5方法进行内部处理。举个例子，客户端向H5提供了打开微信App的接口openWeChatApp，如下所示。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22 | class JsBridgeUtil {  <em>/// 将json字符串转化成对象</em>  static JsBridge parseJson(String jsonStr) {  JsBridge jsBridgeModel = JsBridge.fromMap(jsonDecode(jsonStr));  return jsBridgeModel;  }    <em>/// 向H5开发接口调用</em>  static executeMethod(context, JsBridge jsBridge) async{  if (jsBridge.method == 'openWeChatApp') {  <em>/// 先检测是否已安装微信</em>  bool \_isWechatInstalled = await fluwx.isWeChatInstalled();  if (!\_isWechatInstalled) {  toast.show(context, '您没有安装微信');  jsBridge.error?.call();  return;  }  fluwx.openWeChatApp();  jsBridge.success?.call();  }  }  } |

为了让我们封装得WebView变得更加通用，可以对Webview进行封装，如下所示。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54 | final String url;  final String title;  WebViewController webViewController; <em>// 添加一个controller</em>  final PrivacyProtocolDialog privacyProtocolDialog;    Webview({Key key, this.url, this.title = '', this.privacyProtocolDialog})  : super(key: key);    @override  WebViewState createState() => WebViewState();  }    class WebViewState extends State<Webview> {  bool isPhone = Adapter.isPhone();  JavascriptChannel \_JsBridge(BuildContext context) => JavascriptChannel(  name: 'FoxApp', <em>// 与h5 端的一致 不然收不到消息</em>  onMessageReceived: (JavascriptMessage msg) async{  String jsonStr = msg.message;  JsBridgeUtil.executeMethod(JsBridgeUtil.parseJson(jsonStr));  });    @override  Widget build(BuildContext context) {  return Scaffold(  backgroundColor: isPhone ? Colors.white : Color(Config.foxColors.bg),  appBar: AppBar(  backgroundColor: isPhone ? null : Color(Config.foxColors.bg),  leading: AppIcon(Config.foxImages.backGreyUrl,  callback: (){  Navigator.of(context).pop(true);  if (widget.privacyProtocolDialog != null) { <em>// 解决切换页面时弹框显示异常问题</em>  privacyProtocolDialog.show(context);  }  }),  title: Text(widget.title),  centerTitle: true,  elevation: 0,  ),  body: StoreConnector<AppState, UserState>(  converter: (store) => store.state.userState,  builder: (context, userState) {  return WebView(  initialUrl: widget.url,  userAgent:"Mozilla/5.0 FoxApp", <em>// h5 可以通过navigator.userAgent判断当前环境</em>  javascriptMode: JavascriptMode.unrestricte...