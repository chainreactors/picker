---
title: Java静态分析框架Tai-e的简单使用
url: https://y4er.com/posts/simple-use-of-the-java-static-analysis-framework-tai-e/
source: Y4er的博客
date: 2023-01-19
fetch_date: 2025-10-04T04:16:11.136327
---

# Java静态分析框架Tai-e的简单使用

[Y4er的博客](/ "Y4er的博客")

[归档](/posts/) [专栏](/series/) [分类](/categories/) [标签](/tags/) [笔记](/note/) [朋友](/friends/) [作品](/showcase/)

浅色深色跟随系统

[Y4er的博客](/ "Y4er的博客")

取消

[归档](/posts/)[专栏](/series/)[分类](/categories/)[标签](/tags/)[笔记](/note/)[朋友](/friends/)[作品](/showcase/)

浅色深色跟随系统

## 目录

* [前言](#前言)
* [配置tai-e](#配置tai-e)
* [运行参数](#运行参数)
* [使用tai-e分析javase程序](#使用tai-e分析javase程序)
* [分析java web](#分析java-web)
* [文末](#文末)
* [参考](#参考)

## 目录

* [前言](#前言)
* [配置tai-e](#配置tai-e)
* [运行参数](#运行参数)
* [使用tai-e分析javase程序](#使用tai-e分析javase程序)
* [分析java web](#分析java-web)
* [文末](#文末)
* [参考](#参考)

# Java静态分析框架Tai-e的简单使用

![Y4er avatar](/img/avatar.jpg)[Y4er](https://github.com/Y4er "Author")
 收录于  类别 [代码审计](/categories/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/) 和 系列 [静态软件分析](/series/%E9%9D%99%E6%80%81%E8%BD%AF%E4%BB%B6%E5%88%86%E6%9E%90/)

2023-01-18  2023-01-18  约 5011 字
 预计阅读 22 分钟

系列 - 静态软件分析

* Java静态分析框架Tai-e的简单使用
* [Doop学习 part 1](/posts/doop-1/)
* [ByteCodeDL 学习](/posts/bytecodedl/)

目录

* [前言](#前言)
* [配置tai-e](#配置tai-e)
* [运行参数](#运行参数)
* [使用tai-e分析javase程序](#使用tai-e分析javase程序)
* [分析java web](#分析java-web)
* [文末](#文末)
* [参考](#参考)

警告

本文最后更新于 2023-01-18，文中内容可能已过时。

# # 前言

在做代码审计的时候，总是遇到一些批量垃圾洞，或者是遇到需要自动化批量找调用链验证的工作，一直想着解决这个问题，后来发现tabby，用了一段时间，总觉得不太舒服，配置不足oom异常加上非人的neo4j的语法，加上太多的toString、equals等无用调用关系，配合上杂乱的neo4j的图，有点扰乱审计思路。

自己照着tabby抄了一个poop出来，发现自己的问题并没有解决，只是熟悉了一下soot的基础用法，会抽取类信息了而已，在此期间狠狠补了一下soot，逐字逐句翻译啃完了英文的《soot存活指南》 <https://www.brics.dk/SootGuide/sootsurvivorsguide.pdf> 然后发现soot出了一个新版本的sootup，自己试了试ifds污点分析。

对于指针分析、污点分析还是一知半解，中间尝试过bytecodedl、doop这种声明式的分析工具，然后发现suffle语法更变态，鬼画符，加上没有详细的文档和对应的规则，自己想要进一步拓展过于困难。

思考很久，发现还是自己底子不扎实，于是学了很长一段时间的静态软件分析，看了很多的论文（~~折磨~~）和视频，其中包括南京大学谭添、李樾两位老师的课，北大熊英飞老师的课等等，今天就简单写一下谭添、李樾两位老师开发的tai-e指针分析框架的简单使用。

防喷：我只是看了课，并不代表我会了，很惭愧的是两位老师的课我看了第二遍有些地方还是不太理解，但是每看一遍总有新收获，所以本文有错实属正常不过，望读者赐教。

# # 配置tai-e

GitHub的wiki给了[配置教程](https://github.com/pascal-lab/Tai-e/wiki/Setup-Tai%E2%80%90e-in-IntelliJ-IDEA)

bash

```
git clone https://github.com/pascal-lab/Tai-e
cd Tai-e
git submodule update --init --recursive
```

idea打开 需要jdk17

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/77924cd9-2058-f7a8-0b19-ed05ac84fa1d.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/77924cd9-2058-f7a8-0b19-ed05ac84fa1d.png "image.png")

image.png

gradle也需要jdk17

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/67eacb8e-1eef-f602-4f53-e96563b6b38a.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/67eacb8e-1eef-f602-4f53-e96563b6b38a.png "image.png")

image.png

然后运行`pascal.taie.Main`，配置下主类，加一个jvm options `Xmx`防止oom异常

[![image.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bf2b83d8-cdfd-9ca3-c5bc-15a944bd3370.png)](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/593424/bf2b83d8-cdfd-9ca3-c5bc-15a944bd3370.png "image.png")

image.png

输出

text

```
Tai-e starts ...
Writing options to output\options.yml
Usage: Options [-gh] [-ap] [--[no-]native-model] [-pp] [--pre-build-ir] [-cp=<classPath>] [-java=<javaVersion>]
               [-m=<mainClass>] [--options-file=<optionsFile>] [-p=<planFile>] [-scope=<scope>]
               [--world-builder=<worldBuilderClass>] [-a=<String=String>]... [--input-classes=<inputClass>[,
               <inputClass>...]]...
Tai-e options
  -a, --analysis=<String=String>      Analyses to be executed
      -ap, --allow-phantom            Allow Tai-e to process phantom references, i.e., the referenced classes that are
                                        not found in the class paths (default: false)
      -cp, --class-path=<classPath>   Class path. Multiple paths are split by system path separator.
  -g, --gen-plan-file                 Merely generate analysis plan
  -h, --help                          Display this help message
      --input-classes=<inputClass>[,<inputClass>...]
                                      The classes should be included in the World of analyzed program (the classes can
                                        be split by ',')
      -java=<javaVersion>             Java version used by the program being analyzed (default: 6)
  -m, --main-class=<mainClass>        Main class
      --[no-]native-model             Enable native model (default: true)
      --options-file=<optionsFile>    The options file
  -p, --plan-file=<planFile>          The analysis plan file
      -pp, --prepend-JVM              Prepend class path of current JVM to Tai-e's class path (default: false)
      --pre-build-ir                  Build IR for all available methods before starting any analysis (default: false)
      -scope=<scope>                  Scope for method/class analyses (default: APP, valid values: APP, REACHABLE, ALL)
      --world-builder=<worldBuilderClass>
                                      Specify world builder class (default: pascal.taie.frontend.soot.SootWorldBuilder)
--------------------
Version 0.1
--------------------
```

# # 运行参数

列举几个关键参数，或者直接[看文档](https://github.com/pascal-lab/Tai-e/wiki/How-to-Run-Tai%E2%80%90e%3F-%28command%E2%80%90line-options%29)

| 参数 | 示例 | 用途 |
| --- | --- | --- |
| `-ap` | `-ap` | 允许虚引用，等同于soot的`--allow-phantom` |
| `-java` | `-java 8` | 指定java版本为jre8 tai-e会从`java-benchmarks/JREs`加载对应的jdk lib |
| `-pp` | `-pp` | 将当前jvm的类路径添加到分析类路径中 和`-java`选项冲突 |
| `-m` | `-m com.example.demo.Main` | 指定主类 表示程序入口 必选参数 |
| `--input-classes` | `--input-classes=com.example.demo.controller.TestController,javax.servlet.ServletRequestWrapper` | 当main函数无法调用到TestController时，可以用这个参数把TestController强制加进来，类似于强制分析？ |
| `-cp` | `-cp E:\demo5\target\classes;.\lib\test.jar` | 类路径 和soot差不多 支持jar文件或者`.java`、`.class`文件目录 **在Windows中多个jar以`;`分隔，unix以`:`分隔** |
| `-g` | `-g` | 仅生成选项配置文件`output/options.yml`不执行分析 |
| `--options-file` | `--options-file=output/options.yml` | 解析配置文件作为选项配置 |
| `--pre-build-ir` | `--pre-build-ir` | 分析之前为所有的method构建IR |
| `-scope` | `-scope=APP` | 指定分析类和方法的分析范围APP, REACHABLE, ALL |
| `-a` | `-a <id>[=<key>:<value>;...]` | 指定分析选项，`-a`可重复指定多个分析，选项会保存在`output/tai-e-plan.yml`文件中 |
| `-p` | `-p output/tai-e-plan.yml` | 用文件指定分析选项 yaml语法 |

举一个污点分析的例子

text

```
-cp
E:\tools\code\demo5\target\classes;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-aop-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-beans-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-boot-2.7.4.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-boot-autoconfigure-2.7.4.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-boot-jarmode-layertools-2.7.4.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-context-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-core-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-expression-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-jcl-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-web-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\spring-webmvc-5.3.23.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\tomcat-embed-core-9.0.65.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\tomcat-embed-el-9.0.65.jar;E:\tools\code\demo5\target\demo5-0.0.1-SNAPSHOT\BOOT-INF\lib\tomcat-embed-websocket-9.0.65.jar
--input-classes=com.example.demo.controller.TestController,javax.servlet.ServletRequestWrapper,javax.servlet.ServletResponseWrapper,org.apache.catalina.connector.Request
-java
8
-m
com.example.demo.Main
-ap
-a pta=action:dump;action-file:result.txt;taint-config:src\test\resources\pta\taint\taint-config.yml
```

直接配置在idea的参数中就行，表示在给定的几个jar包和class中做pta，指定了`taint-config`文件表示做p/taint污点分析，强制指定`com.example.demo.controller.TestController`控制器和几个引用类，允许虚类，使用的污点配置文件为`src\test\resources\pta\taint\taint-config.yml`，结果导出到result.txt文件中。

需要重点讲一下`-a`参数，tai-e有三大类参数

1. Program ...