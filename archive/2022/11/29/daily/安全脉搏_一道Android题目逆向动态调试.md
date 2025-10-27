---
title: 一道Android题目逆向动态调试
url: https://www.secpulse.com/archives/192294.html
source: 安全脉搏
date: 2022-11-29
fetch_date: 2025-10-03T23:56:25.305692
---

# 一道Android题目逆向动态调试

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 一道Android题目逆向动态调试

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-28

12,771

题目来源于海淀区网络与信息安全管理员大赛，题目中将加密验证算法打包进.so，在程序中动态调用check。

本题目通过System.loadLibrary("native-lib")加载了libnative-lib.so文件，该文件通过jeb可以实现提取

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606443.png "null")

图1 题目关键代码

**调试环境选择与配置**

* • mumu模拟器 x64位版本，测试后发现sprintf会导致程序崩溃
* • 夜神模拟器x64,x32的版本经过测试后，sprintf均导致程序崩溃
* • 雷电5模拟器测试后,sprintf导致程序崩溃，动态调试libnative-lib.so时，且无法下载libart.so
* • 最终选用 mumu x32位版本可以进行调试
* • 动态调试选用IDA+MUMU x86模拟器对动态库libnative-lib.so调试

  ### **调试环境**

  ### **adb的基础配置**
* • mumu模拟器使用的adb为adb\_server.exe，这里将adb\_server.exe为便于使用重新命名为adb.exe,打开一个cmd终端，adb 接入模拟器中

```
adb connect 127.0.0.1:7555
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606444.png "null")

图2 adb 服务端连接

* • 通过adb 将apk 包安装进安卓的模拟器

```
adb install test.apk
```

* • 通过cmd再打开一个终端，通过adb shell可以直接进入到模拟器shell中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-16696064441.png "null")

图3 adb shell连接

### **应用程序的配置**

* • 在新起的cmd终端，通过动态调试模式来启动app

```
./adb shell am start -D -n com.example.dynamic/.MainActivity
```

* • android包实际的packet以及类如下图所示com.example.dynamic/.MainActivity

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606445.png "null")

图4 adb 启动程序分析

* • 运行 `adb shell am start`命令后，mumu模拟器中如图5所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606452.png "null")

图5 adb 动态调试程序

### **IDA 的配置**

* • 上传IDA的动态服务端android\_x86\_server到模拟器/data/local/tmp中，tmp文件夹是具有可执行权限的

```
./adb push android_x86_server /data/local/tmp
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606456.png "null")

图6 查看tmp文件夹权限

* • 赋予android\_x86\_server可执行权限

```
chmod +x android_x86_server
```

* • 执行android\_x86\_server，会监听23946端口，但是仍需要通过adb进行端口转发转发到本地监听

```
./adb.exe forward tcp:23946 tcp:23946
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-16696064561.png "null")

图7 启动IDA 调试server端

* • 通过以上步骤使启动服务端IDA的监听
* • 配置本地IDA remote linux debug参数，如图8所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606457.png "null")

图8 配置IDA动态调试

* • 通过attach process 打开远程端的进程

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606458.png "null")

图9 IDA远程attach

* • 选择对应的进程，这里选用1535进程

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606464.png "null")

‘

图10 附加到指定进程

* • 通过以上步骤，将IDA 服务端和.so文件关联到一起，仍需要唤醒被调试的程序，此时mumu模拟器中仍旧如图11所示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606472.png "null")

图11 dynamic程序界面

* • 通过jdb来唤醒被调试程序，本机调试的时候jdb使用java sdk自带的jdb，需要两步操作

+ • 通过adb将进程进行转发,进程号是图n中所示的1535

```
./adb forward tcp:8700 jdwp:1535
```

* • 通过jdb唤醒操作

```
jdb -connect com.sun.jdi.SocketAttach:hostname=127.0.0.1,port=8700
```

* • 再回到IDA中，选择F9继续运行程序，会弹出框选择本地程序与远程是否一样选项框，主要匹配的是动态库libnative-lib.so这个名字

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606478.png "null")

图12 IDA提示检测到本地.so

* • IDA中断点断在ptrace前，mumu模拟器中界面未完全同步

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606480.png "null")

图13 附加到调试进程后，dynamic界面

* • IDA中界面如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-16696064801.png "null")

图14 IDA中显示断点

**.so的调试**

### **反调试绕过**

* • 该.so使用了ptrace 反调试，在ptrace处设置断点，下断点的时候有两种方案

1. 1. 一种是设置IDA 的调试调试，设置载入lib的时候suspend

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606482.png "null")

图15 IDA调试选项配置

* • 当看到IDA中载入libnative-lib.so时，通过快捷键Ctrl-S打开加载的段，查找libnative-lib.so所在内存1

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606483.png "null")

图16 查看IDA中的代码段

* • 还可以在模拟器shell中，查看具体的内存信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606484.png "null")

图17 adb shell中查看内存中的数据地址分布

* • 在动态调试的过程中,重置ptrace 的返回值，绕过该处反调试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-16696064841.png "null")

图18 重置eax的值

可以直接右键或者在eax寄存器上使用快捷键0重置

* • 另外一种方式是直接在ptrace上下断点，在调试的时候当IDA弹窗如图17所示时，程序会直接断在ptrace断点处。如果没有弹出该弹窗，直接在IDA中分析该so时下的断点无效。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192294-1669606485.png "null")

image-20221125160753773

图19 重置eax的值

### **注册native的方法**

* • 在 Native文件中代码如下

```
static JNINativeMethod jniMethods[] = {
 {"check", "(Ljava/lang/String;)Z", (void *)hello},
};
boolean xxxx( char* s) {
 // do something
 return JNI_TRUE;
}
#在JNI_OnLoad中调用RegisterNatives方法注册Natives方法到JVM，建立映射关系。
int JNI_OnLoad(JavaVM *vm, void *reserved)
{
    JNIEnv *env；
    if ((*vm)->GetEnv(vm, (void **)&env, JNI_VERSION_1_4) != JNI_OK) {
        return JNI_ERR;
    }

    jclass cls = (*env)->FindClass(env, "LHelloJNI");
    if (cls == NULL)
        return JNI_ERR;

    int len = sizeof(jniMethods) / sizeof(jnimethods[0]);
    (*env)->RegisterNatives(env, cls, jniMethods, len);

    return JNI_VERSION_1_4;
}
```

### **check 函数的定位**

* • 在apk文件中，反编译后可以看到check函数位于libnative-lib.so...