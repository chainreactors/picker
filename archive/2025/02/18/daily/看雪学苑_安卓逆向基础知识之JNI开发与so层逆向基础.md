---
title: 安卓逆向基础知识之JNI开发与so层逆向基础
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589660&idx=1&sn=9c24e599e745690540cea12e895e0b47&chksm=b18c295686fba040d523ff63966cc023ba78134367eaa4fe01e4eee8c785eb1bcc281aadf141&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-18
fetch_date: 2025-10-06T20:39:42.982472
---

# 安卓逆向基础知识之JNI开发与so层逆向基础

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbOxduibEYYPZYdSZMVrBDU8s913hEzamica0LmFrJEFCla9JHcyOiakY4g/0?wx_fmt=jpeg)

# 安卓逆向基础知识之JNI开发与so层逆向基础

黎明与黄昏

看雪学苑

什么是NDK呢？什么是JNI呢？

NDK（Native Development Kit）是一个允许开发者使用C和C++编写Android应用程序的工具集。它提供了一系列的工具和库，可以帮助开发者将高性能的原生代码集成到Android应用中。

NDK的主要目标是提供一种方式，让开发者能够在需要更高性能或更底层控制的情况下使用C和C++编写部分应用程序，而不仅仅依赖于Java。

JNI（Java Native Interface）是一种编程框架，用于在Java代码和原生代码（如C和C++）之间进行交互。通过JNI，开发者可以在Java代码中调用原生代码的函数，并且可以将Java对象传递给原生代码进行处理。

JNI的主要作用是提供一种标准的接口，使得Java代码能够与原生代码进行通信。开发者可以使用JNI定义Java和原生代码之间的函数接口，并在Java代码中调用这些接口。同时，JNI还提供了一些函数来处理Java对象和原生数据类型之间的转换。简单来说就是JNI相当于JAVA和C/C++之间的翻译官，不管是JAVA转C/C++，还是C/C++转JAVA都需要依靠于JNI进行桥接、转换。

Java的保密性相对于C/C++来说并不算安全，有的开发者为了安全就也会去调用C/C++的代码来增加其项目的安全性，想要调用C/C++代码就需要通过jni接口调用，而要使用jni接口那就需要配置NDK。在配置NDK之前需要创建一个项目，调用C/C++代码建议创建Native C++项目类型。

创建Native C++项目类型的项目可以参考以下方式创建：

一、在向导的**Choose your project**部分中，选择**Native C++**项目类型：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYb0PLuYqKfzuuRhjNR9u7YwQc2KL5quOjJiaIUzXibVicma6lgPDjW9sbNw/640?wx_fmt=other&from=appmsg)

二、填写向导下一部分中的所有其他字段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbZB7MB6WEN0SHFTKHYSRGLkjcB6pllKVUDVZiaj2YQOaIibIJt9v8E49w/640?wx_fmt=other&from=appmsg)

Minimum SDK选项选择您希望应用支持的最低 API 级别。当您选择较低的 API 级别时，您的应用可以使用的现代 Android API 会更少，但能够运行应用的 Android 设备的比例会更大。当选择较高的 API 级别时，情况正好相反。

三、自定义C++支持：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbP5NRjxoBFKcOdN5WAVb6QKoiaKR2CIAU2HibrDLTOZ4dnDamSibNnNjYQ/640?wx_fmt=other&from=appmsg)

使用下拉列表选择您想要使用哪种 C++ 标准化。选择**Toolchain Default**，将使用默认的 CMake 设置。

最后点击Finish，项目创建成功。

```
一

Android Studio NDK的安装与配置
```

如需在 Android Studio 中安装 CMake 和默认 NDK，请执行以下操作：

◆打开项目后，依次点击**Tools > SDK Manager**。

◆点击**SDK Tools**标签页。

◆选中**NDK (Side by side)**和**CMake**复选框。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8G3Nu6SHaVPVZzOYUrYZMYbj41pjFnyjOMRRo53yXnBoD4nd17LFGLNNiaNydaY7iaf8KCpmd4Xn4sw/640?wx_fmt=other&from=appmsg)

◆点击**OK**。

◆点击**OK**。

◆安装完成后，点击**Finish**。

◆您的项目会自动同步 build 文件并执行构建。修正发生的所有错误。

◆Android Studio 会将所有版本的 NDK 安装在`android-sdk/ndk/`目录中，我们需要将NDK安装目录添加到`PATH`环境变量中，NDK安装目录如：D:\AndroidStudio\SDK\ndk\25.2.9519653\build

```
二

Android Studio使用Native C++项目类型JNI开发
```

### 静态注册

我们安装好了NDK下面就开始体验JNI开发之静态注册：

刚开始的时候我不知道是不是Android Studio环境的问题，还是什么问题，每次创建好项目都会报错，如：`“No matching variant of com.android.tools.build:gradle:7.4.0 was found. The consumer was configured to find a runtime of a library compatible with Java 8, packaged as a jar, and its dependencies declared externally, as well as attribute 'org.gradle.plugin.api-version' with value '7.5' but:......”`像这样的报错信息，后面我才知道这个其实就是jdk的版本不符的问题，解决方法可以参考以下文章：

解决Android Studio-jdk版本不符问题*（https://blog.csdn.net/m0\_66019257/article/details/130872226）*

我去改变JDK的版本，准确来说并不是JDK11，而是需要JDK17及JDK17以上的版本才不会报这个错误。如果没有这个错误就可以继续使用擅长的JDK版本进行jni开发。

现在我们使用Native C++项目类型进行静态注册，在具体讲之前先讲一下静态注册的流程：

第一步：在Java层使用native修饰符声明一个C/C++的函数；

第二步：Java层调用C/C++的函数；

第三步：生成.c/.cpp文件，并在文件内编写C/C++函数；

第四步：在java代码中添加静态代码块加载指定名称的共享库。

接下来正式讲解JNI开发就需要使用支持C/C++类型的Native C++项目。

我们先在Java层使用native修饰符声明C/C++的函数，然后调用声明的C/C++层函数：

```
package com.example.as_jni_project;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Context;
import android.os.Bundle;
import android.widget.TextView;
import android.widget.Toast;

import com.example.as_jni_project.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {

    // 在应用程序启动时用于加载'as_jni_project'库。
    static {
        System.loadLibrary("as_jni_project");  // 加载模块名称
    }

    private ActivityMainBinding binding;
    public String str = "Hello JAVA!我是普通字段";
    public static String static_str = "Hello JAVA!我是静态字段";

    public static AppCompatActivity your_this = null;

    public void str_method() {
        Toast.makeText(this, "普通方法", Toast.LENGTH_LONG).show();
    }

    public static void static_method() {
        Toast.makeText(your_this, "静态方法", Toast.LENGTH_LONG).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        your_this = MainActivity.this;
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        // 调用本地方法的示例
        TextView tv = binding.sampleText;
        tv.setText(stringFromJNI());

        Toast.makeText(this, stringFromJAVA(), Toast.LENGTH_LONG).show();
        Toast.makeText(this, stringFromC(), Toast.LENGTH_LONG).show();
        Toast.makeText(this, staticFromC(), Toast.LENGTH_LONG).show();
        stringFromMethod();
        staticFromMethod();
    }

    /**
     * 由“as_jni_project”本地库实现的本地方法，该库已打包到该应用程序中。
     */
    public native String stringFromJNI();  // 这个是Native C++类型项目创建时自带的C/C++方法声明，我就没有删除
    public native String stringFromJAVA();
    public native String stringFromC();
    public native String staticFromC();
    public native String stringFromMethod();
    public native String staticFromMethod();
}
```

我的想法是来完整体验一下从JAVA层通过jni调用C/C++层函数，以及从C/C++层调用JAVA层函数，所以我打算做以下几件事：

1、从JAVA层通过jni调用C/C++层函数

2、从JAVA层通过jni调用C/C++层函数，然后从C/C++层修改JAVA层普通字段的值

3、从JAVA层通过jni调用C/C++层函数，然后从C/C++层修改JAVA层静态字段的值

4、从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层普通方法

5、从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层静态方法

在MainActivity.java文件中我添加了以下代码。

在java代码中添加静态代码块加载指定名称模块：

```
static {
    System.loadLibrary("as_jni_project");  // 加载模块名称
}
```

那我们该怎么知道我们要加载的模块名称是什么呢？在native-lib.cpp文件的同一级文件夹下的CMakeLists.txt文件中有定义：

```
# 有关将 CMake 与 Android Studio 配合使用的更多信息，请阅读文档：
# https://d.android.com/studio/projects/add-native-code.html

# 设置生成本地库所需的最低 CMake 版本。

cmake_minimum_required(VERSION 3.22.1)

# 声明并命名项目。

project("as_jni_project")

# 创建并命名库，将其设置为 STATIC 或 SHARED，并提供其源代码的相对路径。
# 您可以定义多个库，CMake 会为您构建它们。
# Gradle 会自动将共享库与您的 APK 打包。

add_library(
        # 设置库的名称。
        as_jni_project

        # 将库设置为共享库。
        SHARED

        # 提供源文件的相对路径。
        native-lib.cpp)

# 搜索指定的预生成库并将路径存储为变量。
# 由于 CMake 默认在搜索路径中包含系统库，因此您只需指定要添加的公有 NDK 库的名称。
# CMake 会在完成构建之前验证库是否存在。

find_library( # Sets the name of the path variable.
        log-lib

        # Specifies the name of the NDK library that
        # you want CMake to locate.
        log)

# 指定 CMake 应链接到目标库的库。
# 可以链接多个库，例如在此生成脚本中定义的库、预生成的第三方库或系统库。

target_link_libraries( # Specifies the target library.
        as_jni_project

        # Links the target library to the log library
        # included in the NDK.
        ${log-lib})
```

可以从CMakeLists.txt文件中的定义看出，将native-lib.cpp文件设置为共享库，库的名称为as\_jni\_project。所以我们在指定加载模块名称时需要设置为as\_jni\_project。

从JAVA层通过jni调用C/C++层函数：

```
Toast.makeText(this, stringFromJAVA(), Toast.LENGTH_LONG).show();
// 通过使用消息框显示C/C++层函数stringFromJAVA()返回回来的值
```

```
public native String stringFromJAVA();  // 在Java层使用native修饰符声明一个C/C++层函数stringFromJAVA
```

从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层普通字段：

```
public String str = "Hello JAVA!我是普通字段";  // 声明一个Java层String类型的普通变量
```

```
Toast.makeText(this, stringFromC(), Toast.LENGTH_LONG).show();
// 通过使用消息框显示C/C++层函数stringFromC()返回回来的值，该值是在C/C++层函数从Java层调用普通字段的值
```

```
public native String stringFromC();  // 在Java层使用native修饰符声明一个C/C++层函数stringFromC
```

从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层静态字段：

```
public static String static_str = "Hello JAVA!我是静态字段";  // 声明一个Java层String类型的静态变量
```

```
Toast.makeText(this, staticFromC(), Toast.LENGTH_LONG).show();
// 通过使用消息框显示C/C++层函数staticFromC()返回回来的值，该值是在C/C++层函数从Java层调用静态字段的值
```

```
public native String staticFromC();  // 在Java层使用native修饰符声明一个C/C++层函数staticFromC
```

从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层普通方法：

```
// 声明一个Java层无返回值的普通方法，通过C/C++函数调用该方法会弹出消息框显示"普通方法"
public void str_method() {
    Toast.makeText(this, "普通方法", Toast.LENGTH_LONG).show();
}
```

```
stringFromMethod();  // 在Java层调用C/C++层函数stringFromMethod
```

```
public native String stringFromMethod();  // 在Java层使用native修饰符声明一个C/C++层函数stringFromMethod
```

从JAVA层通过jni调用C/C++层函数，然后从C/C++层调用JAVA层静态方法：

...