---
title: Java安全基础（四）Java的反射机制
url: https://www.freebuf.com/articles/web/347440.html
source: FreeBuf网络安全行业门户
date: 2022-10-21
fetch_date: 2025-10-03T20:30:34.804723
---

# Java安全基础（四）Java的反射机制

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

Java安全基础（四）Java的反射机制

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

Java安全基础（四）Java的反射机制

2022-10-20 18:41:48

所属地 上海

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

好长时间没有更新了，今天更新一篇关于java反射机制的文章，初学Java安全，内容如有不恰当的地方，还请各位大佬指正。

## 一、什么是反射

反射（Reflection）是Java的特征之一，C/C++语言中不存在反射，反射的存在使得运行中的Java程序能够获取自身的信息，并且可以操作类或对象的内部属性。那什么是反射呢？

下面是官方的解释：

反射使得Java代码能够发现有已加载类的字段、方法和构造函数的信息，并在安全限制内使用反射的字段、方法和构造函数对其底层对应的对象进行操作

简单来说，通过反射，我们可以在运行时获得程序或程序集中每一个类型的成员和成员的信息。同样的，Java的反射机制也是也是如此，在运行状态中，通过Java的反射机制，我们能够判断一个对象所属的类；了解任意一个类的所有属性和方法；能够调用任意一个对象的任意方法和属性；这种动态获取的信息以及动态调用对象的方法的功能称为Java语言的反射机制。

## 二、反射的用途

在静态语言中，一般对象的类型都是在编译期就确定下来的，二通过Java反射机制，可以动态的创建对象并调用其方法或属性，这也就使得的反射的用途很广泛，在开发过程中使用Eclipse、IDEA等开发工具时，当我们输入一个对象或类并想调用它的属性或方法时，编译器会自动列出它的属性或方法，这是通过反射实现的；载入，JavaBean和jsp之间的调用也是通过反射实现的。反射最重要的用途是开发各种框架，如上文中提到的Spring框架以及ORM框架，都是通过反射机制来实现的。

面向不同的用户，反射机制的重要程度也大不相同。对于框架开发人员来说，反射虽小但作用非常大，它是各种容器实现的核心。对于一般的开发者来说，反射的作用相对较小。但总体来说，适当了解二框架的底层机制对我们的编程思想也是非常有帮助的。

## 三、静态语言和动态语言

在学习反射之前，我们有必要了解一下什么是动态语言和静态语言

* 静态语言（强类型语言）

静态语言是在编译时变量的数据类型即可确定的语言，多数静态语言要求在使用变量之前必须声明数据的类型。如C++、Java、Delphi、C#等

* 动态语言（弱类型语言）

动态语言时在运行是确定数据类型的语言。变量使用之前不需要类型声明，通常变量的类型是被赋值的那个值的类型。如PHP/ASP/Ruby/Python.Perl/ABAP/SQL/JavaScript/Unix Shell等等。

可以在程序运行时改变程序结构和变量类型的语言，比如在程序运行时，新的类和对象可以被加载和创建，新的函数或方法可以被加入或者去除等等。

### 3.1、动态特性

动态语言具有的某些特性即为动态特性

以PHP举例，一段代码，其中变量值的改变可鞥导致这段代码发生功能上的变化，我们将这种现象称为PHP的动态特性

比如下面的这个例子

我们只有当代码运行时，通过变量传入的值才能确定其具体功能

![](https://image.3001.net/images/20221020/1666261321_6351214977acb667ad54f.png!small)

### 3.2、动态特性与Java反射

正是因为PHP中存在多种动态特性，使得开发人员能通过很少的代码实现非常多的功能，比较经典的例子就是一句话木马，通过一行<?php @eval($\_POST[cmd]);代码即可实现多种多样的功能

但是Java本身是一门静态语言，无法像PHP那么灵活多变。但是通过Java反射机制，可以为自身提供一些动态特性。比如，当我们通过IDE写代码时，敲击点好号“.”，会出现当前对象或类所包含的属性和方法，这里用到的就是Java反射机制。

反射最重要的用途就是开发各种通用框架，很多框架嗾使通过XML文件来进行配置的（如：struts.xml，spring-\*.xml等），即所谓的框架核心配置文件。为了确保框架的通用性，程序运行时需要根据配置文件中对应的内容加载不同的类或对象，调用不同的方法，这也依赖于Java反射机制。

### 3.3、Java反射机制功能点

综上所述，Java反射机制的功能可分为如下几点：

* 在程序运行时查找一个对象所属的类
* 在程序运行时查找任意一个类的成员变量和方法
* 在程序运行时构造任意一个类的对象
* 在程序运行时调用任意一个对象的方法

## 四、Java的命令执行类

### 4.1、java.lang.Runtime类

这个类是一个共有类，每个Java应用程序都有一个Runtime类实例，它允许应用程序与运行应用程序的环境交互。当前运行时可以从getRuntime方法获得。应用程序无法创建自己的此类实例。

**该类的主要方法是：getRuntime()，得到一个和当前程序相关联的Runtime类的对象，解释如下：**

返回与当前Java应用关联的runtime对象。大多数Runtime类的方法是实例方法，所以必须被当前运行时对象调用。

**Runtime对象可以调用exec()方法执行命令，详细文档解释如下**

在一个单独的进程中执行指定的命令。这是一个方便的方法。以exec(command)形式调用与exec(String,Stringp[],file)的表现是相同的。

下面是一段代码示例：

![](https://image.3001.net/images/20221020/1666261429_635121b5e0ad7bad89d6a.png!small)

## 五、获取类对象

获取类对象的方式有很多种，这里提供四种方式

* forName()
* 直接获取
* getClass()
* getSystemClassLoader().loadClass()

### 5.1、获取类对象-forName()

如果要使用Class类中的方法完成，就需要使用forName方法，只要有类名称即可，更为防爆，扩展性更强。这种方法并不陌生，在配置JDBC的时候，我们通常采用这种方法

![](https://image.3001.net/images/20221020/1666261516_6351220c25cefac58b1ff.png!small)

### 5.2、获取类对象-直接获取

任何数据类型都具备一个静态的属性，可以使用.class来获取其对应的Class对象。这种方法相对简单，但还是要明确用到类的静态成员

![](https://image.3001.net/images/20221020/1666261588_63512254e109146f1dd13.png!small)

### 5.3、获取类对象-getClass()

我们可以通过Object类中的getClass()方法来获取字节码对象，不过这种方式较为繁琐，必须要明确具体的类，然后创建对象

![](https://image.3001.net/images/20221020/1666261642_6351228adadc8d934eda7.png!small)

## 六、获取类方法

获取某个Class对象的方法集合，主要有以下几种方法：

* getDeclareMethods
* getDecleardMethod
* getMethods
* getMethod

### 6.1、获取类方法-getDeclaredMethods

getDeclaredMethods方法返回类或接口声明的所有方法，包括：public、protected、private和默认方法，但不包括继承的方法

![](https://image.3001.net/images/20221020/1666261709_635122cda6d6ab7feee29.png!small)

### 6.2、获取类方法-getMethods

getMethods方法返回某个类的所有public方法，包括其继承的public方法

![](https://image.3001.net/images/20221020/1666261756_635122fc786d61c27c2c8.png!small)

### 6.3、获取类方法-getMethod

getMethod方法只能返回一个特定的方法，如 Runtime类中的exec()方法，该方法的第一个参数为方法名称，后面的参数为方法的参数对应Class的对象

![](https://image.3001.net/images/20221020/1666261806_6351232e04b561df4bfaf.png!small)

### 6.4、获取类方法 - getDeclaredMethod

getDeclaredMethod方法与getMethod类似，也只能返回一个特定的方法，该方法的第一个参数为方法名，第二个参数名是方法参数

![](https://image.3001.net/images/20221020/1666261870_6351236e1ab5085de5b3b.png!small)

## 七、获取类成员变量

为了更直观地体现出获取类成员变量的方法，我们首先创建一个Student类，要获取Student类成员变量，主要有以下几个方法：

* getDeclaredFields
* getDeclaredField
* getFields
* getField

### 7.1、获取类成员变量-getDeclaredFields

getDeclaredFields方法能够获得类成员变量数组，包括public、private和proteced，但是不包括父类的声明字段

### 7.2、获取类成员变量-getFields

gteFields能够获得某个类的所有的public字段，包括父类中的字段

### 7.3、获取类成员变量-getDeclaredField

该方法与getDeclaresFields的区别是只能获得类的单个成员变量

### 7.4、获取类成员变量-getField

与getFields类似，getField方法能够获得某个类特定的public字段，包括父类中的字段

## 八、构造任意类的对象

构造任意类的对象最经典的方式：

* 无参数：className.newInstance()
* 有参数：getConstructor().newInstance()

![](https://image.3001.net/images/20221020/1666261976_635123d85657343ded5b3.png!small)

构造任意类的对象两种方式异同

（1）首先两种方式在原始码所在的位置上不同

* Class.newInstance() → 在java.lang包
* Constructor.newInstance() → 在java.lang.reflect包

（2）在使用方法上的不同

* ClassName.newInstance():

  ```
  - Class.forName("com.ms08067.newInstance.newInstanceExample").newInstance();

   - newInstanceExample.class.newInstance();
  ```
* getConstructor().newInstance()

```
- newInstanceExample.class.getConstructor().newInstance();
```

* Class.newInstance() 只能反射无参的构造器
* Constructor.newInstance() 可以反射任何构造器
* Class.newInstance() 需要构造器可见
* Constructor.newInstance() 可以反私有构造器
* Class.newInstance() 对于捕获或者未捕获的一场均由构造器丢掷；
* Constructor.newInstance() 通常会把丢掷的异常封装成InvocationTrageException丢掷

# 九、调用任意实例对象的方法

调用任意实例对象的方法最经典的方式

* 直接调用：objectName.functionName()
* invoke调用：invoke()

invoke方法调用任意实例对象是通过反射实现的，下面是一个示例

![](https://image.3001.net/images/20221020/1666262213_635124c53a665b8d69317.png!small)

## 十、不安全的反射

如前所述，利用Java的反射机制，我们可以无视类方法、变量访问权限修饰符，调用任何类的任意方法、访问并修改成员变量值，但是这样做可能导致安全问题，如果一个攻击者能够通过应用程序创建意外的控制流路径，就有可能绕过安全检查发起相关攻击。假设有一段代码如下：

![](https://image.3001.net/images/20221020/1666262266_635124fac72d0df2c8f95.png!small)

其中存在一个字段name，当获取用户请求的name字段后进行判断，如果请求的是Delect操作，则执行DelectCommand函数；若执行的是Add操作，则执行AddCommand函数；如果不是这两种操作，则执行其他代码。

假如开发者看到了这段代码，他认为可以使用Java的反射来重构此代码以减少代码行，如下所示：

![](https://image.3001.net/images/20221020/1666262317_6351252de105b11eb8e98.png!small)这样的重构看起来使得代码行减少，消除了if/else块，而且可以在不修改命令分派器的情况下添加新的命令类型，但是如果没有对传入的name字段进行限制，则可以实例化实现Command接口的任何对象，从而导致安全问题。实际上，攻击者甚至不局限于本例中的Command接对象，而是使用任何其他对象来实现，如调用系统中任何对象的默认构造函数，或者调用Runtime对象去执行系统命令，这可能导致远程命令执行漏洞，因此不安全的反射的危害性极大，也是我们审计过程中需要重点关注的内容。

# web安全 # Java代码审计 # JAVA安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

一、什么是反射

二、反射的用途

三、静态语言和动态语言

* 3.1、动态特性
* 3.2、动态特性与Java反射
* 3.3、Java反射机制功能点

四、Java的命令执行类

* 4.1、java.lang.Runtime类

五、获取类对象

* 5.1、获取类对象-forName()
* 5.2、获取类对象-直接获取
* 5.3、获取类对象-getClass()

六、获取类方法

* 6.1、获取类方法-getDeclaredMethods
* 6.2、获取类方法-getMethods
* 6.3、获取类方法-getMethod
* 6.4、获取类方法 - getDeclaredMethod

七、获取类成员变量

* 7.1、获取类成员变量-getDecla...