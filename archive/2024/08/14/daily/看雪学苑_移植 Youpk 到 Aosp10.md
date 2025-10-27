---
title: 移植 Youpk 到 Aosp10
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458567868&idx=2&sn=3b7c2f13d8a255d680fd823e5beb396b&chksm=b18df43686fa7d204933a40a99416268cdab0d9e82e6837cafada85ac169197453ecd2add05a&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-14
fetch_date: 2025-10-06T18:03:36.012319
---

# 移植 Youpk 到 Aosp10

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HRibPOkwehmcuu9aaBv4og62lc9Hribk6wYTyibjEryuVW0nZBTDZgPfaxxJiaTCRg2zPDWl8kj66Ykg/0?wx_fmt=jpeg)

# 移植 Youpk 到 Aosp10

mb\_qzwrkwda

看雪学苑

Youpk是一个很强大的框架，他的模块化组织形式非常新颖，但是随着安卓系统的不断更新，移植难度也非常大，由于使用了大量的api，导致移植有一定的难度，与fart相比，模块化的插桩更加优雅。

已经有大佬做了fart10的移植(见参考文章3），我这里就不和他重复了，来尝试下youpk的移植，并**去除特征指纹**。

测试设备：pixel1

aosp移植版本：**aosp10.0.0\_r2（本来想移植fartext，失败了）**

（aosp11与10的api相关类似，可以自己尝试）

# 移植前需要注意的

需要你有基础的aosp编译修改经验，简单修改能编译成功。

1.需要有趁手的ide修改经验 我使用的是android studio（调试java层） clion（调试native层）。

2.可能你移植全部完成以后，还是过不去企业壳，但是你能了解基本的art修改思想。

3.如果你准备好开始，检测你的内存和硬盘**内存推荐大于32G**（ide要占用10+10左右）。

**硬盘需要大于1TB，我是32G+2TB，编译体验非常差，有条件推荐上4TB+64G。**

如何开启clion和android studio导入项目源码：

编译的时候要注意repo的python版本，最好大于3.7 如果在低版本ubuntu系统，**需要自己编译python。**

repo fatal: error unknown url type: https

原因：python没有设置ssl

./configure --prefix=/usr/local/python3 --with-ssl

解决文档：

https://stackoverflow.com/questions/18317682/android-aosp-repo-init-fatal-error-unknown-url-type-https

解决：在编译的时候配置ssl。

**找到一个趁手的编译环境+IDE环境是成功编译的第一步骤。**

#

# 开始初步移植 JAVA层

由于7.1→8.0→10.0有多版本跨度，我们**选择youpk8的源码**进行移植，来减少api差异。

第一步，导入unpacker类到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyTglrbdBbxDG4yXrZicjdAIIuQbS14jOYG31ibicAvwdBZXfKdUcN6yaDg/640?wx_fmt=png&from=appmsg)

这里我们可以第一步去除指纹，修改包名。

我这里的包名是com.jiqiu。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyVeyCHxA661PE4t9t8w5uAA4FLVt9b1phsm6LGSEORdl9dyFPaGJMRw/640?wx_fmt=png&from=appmsg)

```
package com.jiqiu;
import android.app.ActivityThread;
import android.os.Looper;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;

public class Unpacker {
//    public static String UNPACK_CONFIG = "/data/local/tmp/unpacker.config";
    //	去指纹位置2，修改配置名文件，不一定需要config尾缀
    public static String UNPACK_CONFIG = "/data/local/tmp/gagaga";
    public static int UNPACK_INTERVAL = 10 * 1000;
    public static Thread unpackerThread = null;

    public static boolean shouldUnpack() {
        boolean should_unpack = false;
        String processName = ActivityThread.currentProcessName();
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(UNPACK_CONFIG));
            String line;
            while ((line = br.readLine()) != null) {
                if (line.equals(processName)) {
                    should_unpack = true;
                    break;
                }
            }
            br.close();
        }
        catch (Exception ignored) {

        }
        return should_unpack;
    }

    public static void unpack() {
        if (Unpacker.unpackerThread != null) {
            return;
        }

        if (!shouldUnpack()) {
            return;
        }

        //开启线程调用
        Unpacker.unpackerThread = new Thread() {
            @Override public void run() {
                while (true) {
                    try {
                        Thread.sleep(UNPACK_INTERVAL);
                    }
                    catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    Unpacker.unpackNative();
                }
            }
        };
        Unpacker.unpackerThread.start();
    }

    public static native void unpackNative();
}
```

**类名也完全可以修改**，在修改后要在

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyh6Y5yJ4CnhwHWJ7kQicPvibM8wVxV2xDOYrct4YdeeIiafkiam5iamFpksg/640?wx_fmt=png&from=appmsg)

这个文件里加上自己的包名，否则编译不过。

比如我打的包名是com.jiqiu，在里面就是：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyiaPrQXQmOr24GjDW6rpx5O9SIQMso0ACeJGjUibQhQgRpW4gOaPiaicPTQ/640?wx_fmt=png&from=appmsg)

之后进入

core/java/android/app/ActivityThread.java

导入自己的包名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyqUpOe26hWkibeob0B2c4WJMxBEb3YazYhnjustKAGv5D1aGfR6eicD7A/640?wx_fmt=png&from=appmsg)

在app启动后，注入自己的脱壳线程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyibIBMyUoXzPTdSHLxE6uRoJwDkicqCzDEXde0icMRFcoxrOIbXa77EdRw/640?wx_fmt=png&from=appmsg)

注意：如果你修改了类名，这里的导入和调用也需要修改。

# NATIVE层移植

想比于fart，youpk的主动调用部分在native层实现，java层仅仅是启动一个线程 启动native函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyrCiczTtPQgHnEbbVkn68yuQtFWtW4ehvttYm91qTNCqkT1qbDvpaV8w/640?wx_fmt=png&from=appmsg)

第一步修改dexopt.cc路径如上。

```
--- a/dex2oat/dex2oat.cc
+++ b/dex2oat/dex2oat.cc
@@ -1036,6 +1036,8 @@ class Dex2Oat final {
         CompilerFilter::NameOfFilter(compiler_options_->GetCompilerFilter()));
     key_value_store_->Put(OatHeader::kConcurrentCopying,
                           kUseReadBarrier ? OatHeader::kTrueValue : OatHeader::kFalseValue);
+
+
     if (invocation_file_.get() != -1) {
       std::ostringstream oss;
       for (int i = 0; i < argc; ++i) {
@@ -1089,7 +1091,23 @@ class Dex2Oat final {
       *out = true;
     }
   }
-
+    //patch by Youlor
+    //++++++++++++++++++++++++++++
+    const char* UNPACK_CONFIG = "/data/local/tmp/gagaga";
+    bool ShouldUnpack() {
+        std::ifstream config(UNPACK_CONFIG);
+        std::string line;
+        if(config) {
+            while (std::getline(config, line)) {
+                std::string package_name = line.substr(0, line.find(':'));
+                if (oat_location_.find(package_name) != std::string::npos) {
+                    return true;
+                }
+            }
+        }
+        return false;
+    }
+    //++++++++++++++++++++++++++++
   // Parse the arguments from the command line. In case of an unrecognized option or impossible
   // values/combinations, a usage error will be displayed and exit() is called. Thus, if the method
   // returns, arguments have been successfully parsed.
@@ -1240,7 +1258,14 @@ class Dex2Oat final {
     ProcessOptions(parser_options.get());

     // Insert some compiler things.
+
     InsertCompileOptions(argc, argv);
+    //patch by Youlor
+    //++++++++++++++++++++++++++++
+      if (ShouldUnpack()) {
+          compiler_options_->SetCompilerFilter(CompilerFilter::kVerify);
+      }
+  //++++++++++++++++++++++++++++
   }
```

注意，这里的config路径一定要与java层设置的一致，见去指纹2。

const char\* UNPACK\_CONFIG = "/data/local/tmp/gagaga";

##

## 拷贝youpk项目到art/runtime目录下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQy3tKQBjzHI11wXn9Uwa43uHmnQF7ICWzdbA7CEVWyd53R8CJCXGTiaiaQ/640?wx_fmt=png&from=appmsg)

并且修改Android.bp。

添加目标编译文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyg4F3lzTc1XY7R4Gnlok4fPgnxhNSVyOKNRLxtib7KqFVRQ866AgPibyA/640?wx_fmt=png&from=appmsg)

添加编译文件后我们就可以初步处理youpk的所有不兼容api，附件提供了修改前后的youpk文件夹，在数十次的编译中，已经修改成安卓系统最新支持api。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQykM5OXncErDrq4oZnxBCnduXsSb9Tvogn9umQP9JPhqoPmLQXFQ1eiaA/640?wx_fmt=png&from=appmsg)

在新版系统编译，这个宏定义视为不安全，直接使用math库的同名函数即可过编译，记得注释原来的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQy7Hu6YQ9Cu0bFEDIz30hlD0SaGPibkicTdm0DA1AVNPeGv4tciaNiakVCLw/640?wx_fmt=png&from=appmsg)

在新版系统中，dex相关库文件移动到了libdexfile文件夹下，我们只需改动libdexfile/Android.bp。

导出其依赖的库，并按新版文件调用，即可解决依赖问题。

```
// Check whether the oat output files are writable, and open them for later. Also open a swap
diff --git a/libdexfile/Android.bp b/libdexfile/Android.bp
index 30d1bcd..2ff2f10 100644
--- a/libdexfile/Android.bp
+++ b/libdexfile/Android.bp
@@ -95,7 +95,7 @@ cc_defaults {
         },
     },
     generated_sources: ["dexfile_operator_srcs"],
-    export_include_dirs: ["."],
+    export_include_dirs: [".","dex"],
 }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQy6r1vxLhKfXPHXjT2zrLgzic8l1ibhpsWG6wekDknab6CibianKQ6pKdBkw/640?wx_fmt=png&from=appmsg)

globals位置发生改变。

#include "base/globals.h”

mirror::Class\*指针修改为ObjPtrmirror::Class。

setstatus的状态码发生改变 mirror::Class::kStatusInitialized变为ClassStatus::kInitialized。

删除size\_t Unpacker::getCodeItemSize(ArtMethod\* method)方法 新版有api可以直接实现。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcF...