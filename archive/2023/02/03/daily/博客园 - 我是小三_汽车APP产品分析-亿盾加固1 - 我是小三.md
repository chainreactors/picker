---
title: 汽车APP产品分析-亿盾加固1 - 我是小三
url: https://www.cnblogs.com/2014asm/p/17086523.html
source: 博客园 - 我是小三
date: 2023-02-03
fetch_date: 2025-10-04T05:34:53.164598
---

# 汽车APP产品分析-亿盾加固1 - 我是小三

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/2014asm/)

# [逆向与安全](https://www.cnblogs.com/2014asm)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/2014asm/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/%E6%88%91%E6%98%AF%E5%B0%8F%E4%B8%89)
* 订阅
* [管理](https://i.cnblogs.com/)

# [汽车APP产品分析-亿盾加固1](https://www.cnblogs.com/2014asm/p/17086523.html "发布于 2023-02-02 17:14")

```
一、前言
二、加固整体构架
三、壳java层分析
四、壳so静态分析
五、壳so动态分析
六、脱壳二次打包
七、总结
```

## 一、前言

1.1、app加固的本质

代码安全只是表面，核心是帮助客户满足业务不被阻断、关键数据资产不被窃取的安全需求。因为加固自身不创造价值，加固的价值必须和公司业务挂钩，来间接体现。通过安全体系建立为业务服务保障，增加收益与减少了资损率。

1.2、不同视角看加固

切换立场、改变视角来看APP加固，因为对一件事的不同面，每一面都能看到的不同的东西。

用户视角：更多的是关注功能使用与交互体验，看到的是表现层的功能和交互。所以对于C端用户而言，很难感知其存在价值。

产品视角：关注产品本身体验与价值而考量，看到的是需求、方案、价值。

技术视角：关注技术成本和可扩展性与安全性，看到的是架构、实现、可扩展、安全性。能感知到安全加固的重要性，但是更多的是从技术实现角度出发。

业务视角：保障业务正常运营，看到的是成本和收益。

所以，视角不同，观点不同，加固决策不同，安全程度也不同。

有了上面这些铺垫，接下来你看完文章后大概不会觉得这样的方案很奇怪，这是计划的一部分。

## 二、加固整体架构

2.1、加固架构

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202163216986-1336140615.jpg)

2.2、解壳过程

壳加载运行起来后是解密原始dex与启动加载APP Application过程，完成一系列的工作：

**解密原apk的dex集合**

使用加密过程中对应的算法进行解密每个dex文件。

**将解密之后的dex集合添加到dexElements数组**

通过反射将解密的dex集合添加到dexElements数组。

**动态加载原apk的Application**

原apk的Application在加密过程被替换成解密壳的Application，因此需要在加载壳过程中还原该操作。

## 三、壳java层分析

3.1、attachBaseContext

so释放与加载在创建APP进程加载Application之前，完成解压缩释放到lib目录、System.loadLibrary("nesec")加载so到内存并在MyJni类中注册了如下几个jni方法：

```
public static native void cp();
  public static native void d(String arg0);
  public static native void e(String arg0);
  public static native boolean load(Application arg0, String arg1);
  public static native boolean load2(Application arg0, String arg1);
  public static native boolean run(Context arg0, Application arg1);
```

3.2、native load 加载dex

加载完so后调用注册好的native方法load解密dex并加载到内内存，dex加载的过程大到为dex文件解密及将解密的dex集合添加到dexElements数组。

3.3、原Application

加载完dex后要从原APP的Application运行，代码如下：

```
public static String strAppName;

static {
    MyApplication.TAG = "wrapper";
    MyApplication.strAppName = "com.netease.nis.wrapper.MyApplication";
    MyApplication.a = null;
    MyApplication.b = null;
    MyApplication.newApp = null;
    MyApplication.mOfficial = true;
}
private static Application a(Context arg2) {
    try {
    if(MyApplication.newApp != null || MyApplication.strAppName.compareTo("") == 0) {
        return MyApplication.newApp;
    }

    ClassLoader v0_1 = arg2.getClassLoader();
    if(v0_1 == null) {
        return MyApplication.newApp;
    }

    Class v0_2 = v0_1.loadClass(MyApplication.strAppName);
    if(v0_2 != null) {
        MyApplication.newApp = (Application)v0_2.newInstance();
        return MyApplication.newApp;
    }
}
catch(Exception v0) {
    v0.toString();
    return MyApplication.newApp;
}

return MyApplication.newApp;
}
```

通过动态加载原app的Application并执行，具体流程如下：

(1)通过Class.newInstance()创建一个Application实例；

(2)执行Application实例的attach()；

```
Application v0_7 = MyApplication.a(arg13);
MyApplication.newApp = v0_7;
if(v0_7 != null) {
    Method v0_8 = Application.class.getDeclaredMethod("attach", Context.class);
    if(v0_8 != null) {
        v0_8.setAccessible(true);
        try {
            v0_8.invoke(MyApplication.newApp, arg13);
            goto label_224;
        }
        catch(InvocationTargetException v0_9) {
        }

        new StringBuilder("[attachBaseContext] InvocationTargetException:").append(v0_9);
        goto label_204;
    }
}
```

## 四、壳so静态分析

4.1、壳入口隐藏

按照我个人惯例，定位到壳so模块后首先使用ida加载模块静态分析收集下信息(字符串，壳入口、导出方法)等，用ida打开后直接提示如图4-1所示：

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202163638206-69435650.jpg)

　　　　　　　　　　　　　　　　图4-1

不用奇怪，这是节信息被处理过了，防止静态反编译，点击ok继续，查看导出函数时发现一堆乱码，如图4-2所示:

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202164102318-474780761.jpg)

　　　　　　　　　　　　　　　　图4-2

应该是被加密处理了，查看节信息也找不到init\_array节，如图4-3所示:

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202164149121-1155016134.jpg)

　　　　　　　　　　　　　　图4-3

静态不好定位就动态定位壳入口，在内存中一切的隐藏都很难跳系统机制。

## 五、壳so动态分析

5.1、壳入口定位

根据linker加载so流程中主要有两个点可以做为壳入口，init或init\_array是so程序代码可以执行的最早的时机, 然后才加载Jni\_onload，只要在linker执行init进下断点就可以定位壳入口。如图5-1所示：

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202164235477-447830144.jpg)

　　　　　　　　　　　　　　　　图5-1

定位到的init\_array方法中有几个关键的地方，init\_array3，解密Jni\_OnLoad代码。如图5-2所示：

![](https://img2023.cnblogs.com/blog/693524/202302/693524-20230202170123720-1311103562.jpg)

　　　　　　　　　　　　　　　　图5-2

```
.note.gnu.text:000000782421DFD0                               dec_sub_7D26D97FD0            ; CODE XREF: dec_sub_7D26D98040+50↓p
.note.gnu.text:000000782421DFD0 62 03 00 B4                   CBZ             X2, locret_782421E03C
.note.gnu.text:000000782421DFD0
.note.gnu.text:000000782421DFD4 05 00 80 52                   MOV             W5, #0
.note.gnu.text:000000782421DFD8 22 00 02 8B                   ADD             X2, X1, X2
.note.gnu.text:000000782421DFDC E6 03 05 2A                   MOV             W6, W5
.note.gnu.text:000000782421DFDC
.note.gnu.text:000000782421DFE0
.note.gnu.text:000000782421DFE0                               loc_782421DFE0                ; CODE XREF: dec_sub_7D26D97FD0+68↓j
.note.gnu.text:000000782421DFE0 C6 04 00 11                   ADD             W6, W6, #1
.note.gnu.text:000000782421DFE4 C6 1C 00 12                   AND             W6, W6, #0xFF
.note.gnu.text:000000782421DFE8 C4 7C 40 93                   SXTW            X4, W6
.note.gnu.text:000000782421DFEC 03 68 64 38                   LDRB            W3, [X0,X4]
.note.gnu.text:000000782421DFF0 65 00 05 0B                   ADD             W5, W3, W5
.note.gnu.text:000000782421DFF4 A5 1C 00 12                   AND             W5, W5, #0xFF
.note.gnu.text:000000782421DFF8 A7 7C 40 93                   SXTW            X7, W5
.note.gnu.text:000000782421DFFC 08 68 67 38                   LDRB            W8, [X0,X7]
.note.gnu.text:000000782421E000 08 68 24 38                   STRB            W8, [X0,X4]
.note.gnu.text:000000782421E004 03 68 27 38                   STRB            W3, [X0,X7]
.note.gnu.text:000000782421E008 04 68 64 38                   LDRB            W4, [X0,X4]
.note.gnu.text:000000782421E00C 27 00 40 39                   LDRB            W7, [X1]
.note.gnu.text:000000782421E010 64 00 04 0B                   ADD             W4, W3, W4
.note.gnu.text:000000782421E014 84 1C 00 53                   UXTB            W4, W4
.note.gnu.text:000000782421E018 03 68 64 38                   LDRB            W3, [X0,X4]
.note.gnu.text:000000782421E01C 64 7C ...