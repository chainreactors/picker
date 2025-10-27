---
title: ByteCTF2022 mobile系列
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458489310&idx=1&sn=8d6987a202a5ea5f5f78961121bcfdde&chksm=b18ea15486f9284246383d0ab5a56f3ad8a845f04cc56656c1a069fb99eef1f00732a04c025f&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-12-26
fetch_date: 2025-10-04T02:31:10.515013
---

# ByteCTF2022 mobile系列

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fq1U2eL4icqiajJoQxlP9yIBtyxwlrP5KhdSPMrE0fnMO6VOAJ3CQ576vUDbhgTNbia94U8qLyFW2pg/0?wx_fmt=jpeg)

# ByteCTF2022 mobile系列

e\*16 a

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Fq1U2eL4icqiajJoQxlP9yIBrO4Uialma18OKypyKEl5RPWkFRCESUOtl79qVF1oYlsTJYNjJymwZQQ/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：e\*16 a

9月底就想复现了mobile题目，奈何当时时间有限，太过年轻，不能静下心来看整个题目的布置与攻击，这几天心血来潮，把题目复现了。

#

#

```
一

前置知识
```

##

## **1.WebView**

现在很多App中都会内置html5界面，有时候会涉及到与android进行交互，这就需要用到WebView控件，WebView可以做到：

```
1.显示和渲染web界面2.直接使用html进行布局3.与js进行交互
```

创建WebView拥有两种方法，第一种方法是WebView webview = new WebView(getApplicationContext());创建；第二种是在xml文件内放在布局中；下面以第二种方法为例。

Activity\_main.xml文件

```
<WebView    android:id="@+id/eeeewebview"    android:layout_width="0dp"    android:layout_height="0dp"    app:layout_constraintBottom_toBottomOf="parent"    app:layout_constraintEnd_toEndOf="parent"    app:layout_constraintStart_toStartOf="parent"    app:layout_constraintTop_toTopOf="parent" />
```

MainActivity.java文件

```
public void onCreate(Bundle savedInstanceState) {    super.onCreate(savedInstanceState);    setContentView(R.layout.activity_main);
    // WebView    WebView webView = (WebView) findViewById(R.id.eeeewebview);    webView.loadUrl("https://www.baidu.com");    webView.setWebViewClient(new WebViewClient(){        @Override        public boolean shouldOverrideUrlLoading(WebView view, String url) {            //使用WebView加载显示url            view.loadUrl(url);            //返回true            return true;        }    });
```

写完之后运行，发现报错，无法打开网页(net::ERR\_CLEARTEXT\_NOT\_PERMITTED)， 经过搜索在manifest内设置usesCleartextTraffic为true即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UCNFyDxgt6qlJm4zm0wiaj8LJLeuvYibbmDYmU0HvDduLgbiaA1TmMpOFw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UnuaxiaOR5bo48kwnbXiazb89QsL5tCPKNxuIPVVzy3tVERN9b70Ps0KQ/640?wx_fmt=png)

可以看到百度已经被打开了，啊～因为这个app是我用来测试其他东西的，所以会看到三个奇奇怪怪的按钮。

##

## **2.URI**

Uri代表要操作的数据，Android上可用的每种资源 (图像、视频片段、网页等) 都可以用Uri来表示。从概念上来讲，UrI包括URL。

Uri的基本结构是

```
大致为[scheme:]scheme-specific-part[#fragment]细分为[scheme:][//authority][path][?query][#fragment]
```

path可以存在多个，以"/"连接 scheme://authority/path1/path2/path3?query#fragment

query可以带参数的返回值也可不带 scheme://authority/path1/path2/path3?id = 1#fragment

举例如下

```
http://www.eeeeeeeeeeeeeeeea.cn/about?id=1
```

scheme是在":"之前，所以他匹配的是http。

authority是在"//"之后，所以www.eeeeeeeeeeeeeeeea.cn与其对应。

path自然对应的就是about这个页面。

query对应的是id=1。

在安卓内，除了authority和scheme必须存在，其他的可以选择性的要或者不要。

将一个url解析成uri对象的操作是Uri.parse(“http://www.baidu.com”)，就是将百度网址解析成一个uri对象，可以对其进行其他的各种操作了。

##

## **3.intent**

###

### （1）intent功能

intent是各大组件之间通信的桥梁，Android有四个组件，分别是Activity，Service，Broadcast Receiver，Content Provider；组件之间可以进行通信，互相调用，从而形成一个app.

每个应用程序都有若干个Activity组成，每一个Activity都是一个应用程序与用户进行交互的窗口，呈现不同的交互界面。因为每一个Acticity的任务不一样，所以经常互在各个Activity之间进行跳转，在Android中这个动作是靠Intent来完成的。通过startActivity()方法发送一个Intent给系统，系统会根据这个Intent帮助你找到对应的Activity，即使这个Activity在其他的应用中，也可以用这种方法启动它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6U5WLPqVK31kdicL9cNlkmwvtPEMriaiaMiaHXhBU7tgcfgvfezo39qib6icSg/640?wx_fmt=png)

###

### （2）显式intent和隐式intent

intent包括两种，一是显式另一个是隐式。显式intent通常是已经知道要启动Activity的包名，多发于同一个app内；隐式intent只知道要执行的动作是什么，比如拍照，录像，打开一个网站。

那么隐式的intent如何启动一个组件呢呢？如果没有约束的话可能会造成一些后果，所以在Manifest文件内定义了intent-filter标签，如果组件中的intentfilter和intent中的intentfilter匹配，系统就会启动该组件，并把intent传给它；若有多个组件都符合，系统变会弹出一个窗口，任我们选择启动该intent的应用(app)。

在intent-filter标签中，我们可以选择三个intent的属性进行设置，包括action，category，data。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6Umwo5aicgia8CY2GttahibV9rsqicWVMpXadSicibmAtcQhhZPGIZVDJsbRgA/640?wx_fmt=png)
上图intent-filter定义的action为MAIN，代表app以这个activity开始。

###

### （3）intent属性

####

#### ① component

该属性是显式intent特有的，表明要启动的类的全称，包括包名和类名。有它就意味着只有Component name匹配上的那个组件才能接收你发送出来的显式intent。

下面代码可以启动另一个app的主页面：

```
Intent intent = new Intent(Intent.ACTION_MAIN);intent.addCategory(Intent.CATEGORY_LAUNCHER);           ComponentName cn = new ComponentName(packageName, className);           intent.setComponent(cn);startActivity(intent);
```

一个activity是否能被其他app的组件启动取决于"android:exported"，true能，false不能。如果是false，这个activity只能被相同app的组件启动，或者是相同user ID的app的组件启动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UO9BbaWq5teSEgyWfIZV2W4icKjqugVfxaRRfCuE3I0FTaXktvfRn3Sw/640?wx_fmt=png)

如果显式设置exported属性，不管这个activity有没有设置intent-filter,那么exported的值就是显式设置的值。

如果没有设置exported属性，那么exported属性取决于这个activity是否有intent-filter。

如有intent-filter,那么exported的值就是true。

如没有intent-filter,那么exported的值就是false。

####

#### ② action

一个字符串变量，用来指定Intent要执行的动作类别（比如：view or pick）。你可以在你的应用程序中自定义action，但是大部分的时候你只使用在Intent中定义的action，你可以通过Intent的setAction()方法设置action。

####

#### ③ data

一个Uri对象，对应着一个数据。只设置数据的URI可以调用setData()方法，只设置MIME类型可以调用setType()方法，如果要同时设置这两个可以调用setDataAndType()。

####

#### ④ category

一个包含Intent额外信息的字符串，表示哪种类型的组件来处理这个Intent。任何数量的Category 描述都可以添加到Intent中，你可以通过调用addCagegory()方法来设置category。

####

#### ⑤ extras

Intent可以携带的额外key-value数据，你可以通过调用putExtra()方法设置数据，每一个key对应一个value数据。你也可以通过创建Bundle对象来存储所有数据，然后通过调用putExtras()方法来设置数据。

####

#### ⑥ flags

用来指示系统如何启动一个Activity（比如：这个Activity属于哪个Activity栈）和Activity启动后如何处理它(比如：是否把这个Activity归为最近的活动列表中)。

#

#

```
二

题目环境布置
```

###

### **1.docker存在问题**

运行run.sh，我自己启动了一遍docker环境，修改了一些部分，最终发现是在server.py文件的setup\_emulator()函数中没有模拟出来手机，只是创建了一个AVD环境，并没有emulator成功。

由于自己能力有限，实在不知道如何修好这个docker环境，便就此搁置，导致后面silver droid利用也不完全；如若后续进步，必定再战一次。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UzNOfTavluFramtFMO7GKOkNUuSgMNor8E8f5aH2NSfB3o1CFJ3wwSA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6Ugv7LEh1axchjVPbYvdwCNfcyb8MuGaPJo1Jib0DLT28rutZdILzeArg/640?wx_fmt=png)

###

### **2.server.py脚本内函数**

####

#### （1）adb\_broadcast

adb broadcast便是将服务器上的flag传给apk的FlagReceiver，通过adb shell进入手机，可以查看到flag被存到了"files/flag"内。

之前有一个疑问，便是manifest文件将Flagreceiver设置为exported为false和设置了intent-filter，防止外界app进行干扰，那么是怎么将flag传递给FlagReceiver呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UY8l1SKgBMPpQGLWibfGBh2zsVKJfTEdOXHOeBqW2UPCb3KWQPwa44Ew/640?wx_fmt=png)
由于root的情况下，是忽略掉exported的，所以可以对其进行广播。

```
am broadcast -W -a "com.wuhengctf.SET_FLAG" -n "com.bytectf.silverdroid/.FlagReceiver" -e 'flag' 'flag{eeeeeeee}'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6Uas2bv4xSkekAJibqQAKQ3icM4jA4xkgzAG93icMX1sMJUmCPFG0KpPmNQ/640?wx_fmt=png)

####

#### （2）adb\_activity

通过intent传递url数据，下面可以通过-d选项来指定Intent data URI。

```
am start -a android.intent.action.VIEW -d  https://www.baidu.com
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UZYtBAdpDf8lB06hnjGAvhf8ELH1iaOkdsaMjSUKdOicsWibJeHHdhbo0Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HtcwKvQZ1N6cj1Tp9s4t6UFM9JDk9rI0GAMkZgMXgic3dhoWGwZfH57K9lBvWEG1cXPURHXjvRwRg/640?wx_fmt=png)

下面的题目介绍，都是以pixel4为环境打的，因为docker我这边模拟不起来

同时记得自己写的apk要在AndroidManifest.xml内加两句话，可以让其有网络访问的权限。

```
    <uses-permission android:name="android.permission.INTERNET"/>

<application    android:usesCleartextTraffic="true"
```

#

#

```
三

Silver Droid
```

##

## **1.server.py分析**

主要由攻击者提供一个url，在url内布置好exp，从而进行达到利用的目的，具体见代码块内分析。

##

```
#!/usr/bin/env python3import os   import randomimport subprocessimport sysimport timeimport requestsimport uuidfrom hashlib import *import zipfileimport signalimport string
isMacos = len(sys.argv) == 2wordlist = string.ascii_lettersdifficulty = 4random_hex = lambda x: ''.join([random.choice(wordlist) for _ in range(x)])ADB_PORT = int(random.random() * 60000 + 5000)EMULATOR_PORT = 36666 if isMacos else (ADB_PORT + 1)EXPLOIT_TIME_SECS = 30APK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app-debug.apk")FLAG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "flag")HOME = "/home/user"VULER = "com.bytectf.silverdroid"

ENV = {}ENV.update(os.environ)if...