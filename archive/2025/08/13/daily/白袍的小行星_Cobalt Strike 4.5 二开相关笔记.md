---
title: Cobalt Strike 4.5 二开相关笔记
url: https://red-team.tips/post/KbHZkszOlP/
source: 白袍的小行星
date: 2025-08-13
fetch_date: 2025-10-07T00:13:16.771121
---

# Cobalt Strike 4.5 二开相关笔记

[![](https://red-team.tips/images/avatar.png?v=1754980891100)](https://red-team.tips)

# 白袍的小行星

**Once a hacker, always a hacker!**

[首页](/)
[归档](/archives)
[标签](/tags)
[关于](/post/about)
[友链](/post/friends)

## Cobalt Strike 4.5 二开相关笔记

2025-08-12

15 min read
[# 红队研究](https://red-team.tips/tag/f5G6oBVmo/)

近期有人已经把beacon源码公布了，所以也把之前自己的一些研究笔记汇总发一下。

另外想说下自己的观点：已经2025年了，所谓二开 Cobalt Strike 对绝大部分人来说都是伪需求，你能有官方团队写的好么？学习一下就行了。

# 0x1 环境搭建

## Java端

可能部分人还没有Java的原生源码，所以介绍下反编译的方法。

先把jar包反编译了，利用IDEA自带的`java-decompiler.jar`：

```
java -cp java-decompiler.jar org.jetbrains.java.decompiler.main.decompiler.ConsoleDecompiler -dgs=true cs_original/cobaltstrike.jar cs_src
```

`cs_original/cobaltstrike.jar`是原包，`cs_src`是反编译后的输出目录，得到一个jar后缀文件，解压缩即可得到源码。

IDEA新建项目，将反编译后的所有源码放入`decompiled_src`目录，原包放入`lib`目录，再在`File-Project Structure-Modules-Dependencies`中添加原包：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142156200.png)

在`File-Project Structure-Artifacts`中添加JAR，主类为`aggressor.Aggressor`：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142228000.png)

需要修改相应文件时，右键选择`Refactor-Copy file`，`To directory`选择`src`目录里新建的目录：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142239827.png)

修改完成后就可以进行编译，选择`Build-Build Artifacts`，在`out`目录下得到重新打包好的jar包。

## Beacon端

beacon源码是纯C的，为了兼容性，需要使用`Visual Studio 2012`来开发，并且要安装`Update 1`补丁，否则无法满足平台工具集`Visual Studio 2012 - Windows XP (v110_xp)`的设置。

另外还有几个地方需要修复下，不然无法通过编译。

`ReflectiveLoader.c`中，会出现一个`fatal error C1017: 无效的整数常量表达式`错误，代码如下：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142252797.png)

编译时`RefLoadSize`没初始化，就会导致错误，这个实际上会在预处理器里初始化，所以这里定义一下就行，我用的`100`:

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142316273.png)

还有在`parse.c`中，`bool`标识符会报错，因为C99标准里没有`bool`只有`_Bool`，我换成了`BOOL`。

另外**后期生成事件**里，要把命令改下，否则有可能会因为找不到路径导致失败。

如果报`tomcrypt.lib`是用旧版本编译的，那就在这里把全程序优化设为否：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142347148.png)

另外一个情况是，替换掉原来的sleeve下的dll然后生成exe，client端会报一个错误：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142418292.png)

这是因为cs生成exe木马的逻辑是：先把回连地址等信息`patch`进`beacon.dll`，然后根据你需要的类型（exe、service exe、dll）再把`beacon.dll` `patch`进`artifact.xxx`里，这里的错误就是因为重新生成的`beacon.dll`太大导致原来的模板放不下了，所以生成出来的exe也会直接无法运行报访问冲突的错误。

解决办法就是用Artifacts Kit重新生成一下即可：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142429582.png)

记住，生成出来的东西不能直接用来替换掉resources目录下的exe，得用给的cna脚本去加载，这个b问题折磨了我好几天，问了`@evilash`才解决。

# 0x2 去除特征和修复漏洞

这里的内容参考了很多网上的文章，时间久远忘了有哪些，只列举记得的：

* https://blog.qwqdanchun.com/CobaltStrike\_Modify/

## 去除暗桩

这个版本有一堆暗桩，Java端和beacon里都有，Java里基本就是两种：

1. 检验某个`.class`文件是否被篡改（对比哈希），如果被篡改就退出

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142442160.png)

2. 检验是否用 Java Agent 方式启动，是则退出

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142453778.png)

还不少，全局搜索再耐心去掉就行。

beacon端也有一处：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142505198.png)

这两个方法的返回值都要改为`FALSE`，因为会用 teamserver 端发过来的水印值进行校验，不符合就退出，所以全部改掉。

## CVE-2022-39197修复

这个漏洞就是 Cobalt Strike 的 XSS 漏洞，可以导致 RCE ：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142518949.png)

修复方式，在`aggressor.MultiFrame`中添加：

```
try{
    ClassPool pool = ClassPool.getDefault();
    CtClass cc = pool.get("javax.swing.plaf.basic.BasicHTML");
    CtMethod method = cc.getDeclaredMethod("isHTMLString");
    method.setBody("return false;");
    cc.toClass();
}
catch (Exception e){
}
```

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142537266.png)

这种是完全关闭 HTML 标签解析，所以可能对正常显示会造成影响，遇到了再看怎么修复。

## 修复foreign派生错误的bug

该版本无法正常使用`windows/foreign/reverse_http(s)`进行 spawn ，但没有做判断，导致这里的`beaconDLL.customDLL`和`beaconDLL.customFileName`会为空：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142547945.png)

暂时用直接返回原 DLL 的方式来修复，这样无法使用自定义反射 Loader：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142559767.png)

后续再看有没有更好的办法处理。

## 修改winvnc.dll位置

在`server\ManageUser.java`中修改，我放进了 resources 里，这样就不用单独开一个文件夹了：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142611825.png)

虽然 VNC 这个功能几乎用不上。

## 启用Payload Generator(Stageless)

这个是为了方便做自己想要的 Loader，因为 Stage 的 shellcode 特征更多。

修改`scripts\default.cna`：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142622248.png)

## 修复Windows 7下https问题

新版本的 Java 会默认禁用 TLS1.2 以下的协议，这样在无补丁的 Windows 7 上无法用 HTTPS 上线，修改`server\TeamServer.java`：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142644282.png)

## 修复CVE-2022-23317

`CVE-2022-23317`是 Cobalt Strike Webserver 的一个问题，利用不规则的URL访问时会产生特殊回显，导致可以识别该服务器为Cobalt Strike server，所以加个判断就行，在`cloudstrike\WebServer.java`中：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142702279.png)

## 去除服务端信息特征

1. 删除服务端响应字符串

在`cloudstrike/NanoHTTPD.java`里修改回显字符串`This is the default!`为其他的：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142716121.png)

这里直接把`sendError`的第二个参数弃用，所有错误都只返回一个字符串：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142726430.png)

2. 修改socket通信的magic值

`ssl\SecureServerSocket.java`和`ssl\SecureSocket.java`里都把`0xBEEF`改掉：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142735790.png)
![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142747530.png)

## 修改默认异或密钥

这里不再使用原有的单字节异或密钥，而是改为多字节加密：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142757803.png)
![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142807446.png)

## 修改BeaconEye特征

实际就是调用`memset()`时使用了0来填充，导致会有一个位置的值固定呈现为0，这个值又根本用不到，所以直接把`memset()`的参数改为另一个值即可：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142819073.png)

## Sleep Mask未混淆部分的内存特征

<https://codex-7.gitbook.io/codexs-terminal-window/blue-team/detecting-cobalt-strike/sleep-mask-kit-iocs>

这个暂时先不修复，可以靠高版本sleepmask解决。

## 其他

修改默认client配置文件名，在`aggressor\Prefs.java`中：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142850182.png)

这个是为了防止蜜罐读取本地文件，导致接管CS。

## 修复BeaconFormatToString错误

4.6版本更新日志中提到一个修复： 修复了在 BOF 中调用 BeaconFormatToString 时错误地要求传递字符串长度地址的问题。

BeaconFormatToString的功能为将格式化数据提取为一个字符串，并用该字符串的长度填充传入的 size 变量：

```
char * BeaconFormatToString (formatp * obj, int * size)
```

定位一下，发现该函数结果来源于：

```
char * bformat_tostring(formatp * buffer, int * size) {
	DWORD len = bformat_length(buffer);
	if (size != NULL)
		*size = (int)len;

	if (size == 0)
		return NULL;

	return bformat_string(buffer);
}
```

问题很明显，传入的是字符串长度的指针，但是却判断了它是否为0，实际上应该判断的是len：

```
char * bformat_tostring(formatp * buffer, int * size) {
    DWORD len = bformat_length(buffer);

    if (size != NULL) {
        *size = (int)len;
    }

    if (len == 0) {
        return NULL;
    }

    char *str = bformat_string(buffer);
    return str;
}
```

# 0x3 普通功能增加

## 已登录用户显示

用户登录如果使用同一个用户名，会提示该用户已存在，校验点在`server/ManageUser.java`：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142902538.png)

而已登录的用户名数据是存在`server.Resources`里的，所以要从这里面把数据取出来。

这里要理清代码结构还是挺麻烦的，有以下几个问题需要解决：

1. 找到teamserver向client传递数据的方法，然后把已登录用户数据加进来
2. 用户登录和用户退出要自动进行增减

在`server.Resources`里我新加了一个成员变量，用来存储用户的用户名、登录IP、登录时间，这个变量得是`LinkedList`对象，不然后期解析会出问题。

`getOnlineUsers()`就是获取数据的方法：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142909753.png)

用户登录IP在`TeamSocket`对象的`from`字段，加了个方法用来获取它。

之后则是在用户登录和退出的时候，自动将`LinkedList`对象中的`hashmap`进行增删：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142919075.png)

这里最主要把`LinkedList`对象中的格式搞清楚。

之后就是在用户登录和退出的地方调用这两个方法：

![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142931509.png)
![](https://adan0s-1256533472.cos.ap-nanjing.myqcloud.com/uPic/20250812142948655.png)

还有一个问题就是传递数据，也是调试了挺久，最后发现用`broadcast()`方法就可以：

![](https://adan0s-1256533472.cos.ap-nanji...