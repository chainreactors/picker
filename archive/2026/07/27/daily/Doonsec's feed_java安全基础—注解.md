---
title: java安全基础—注解
url: https://mp.weixin.qq.com/s/l5CV142Y_Ak7vXy0daSaHw
source: Doonsec's feed
date: 2026-07-27
fetch_date: 2026-07-28T04:57:59.605194
---

# java安全基础—注解

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/goxicFBGKAF4ZZiaTfY8TYAp9sva6HRYGjic8XqE4vgoP5xlgiaicGTRfDRumGQEN3ZOzJraSqiclq1iaNfoxnsH2Re8QlyQD3UqBvDc4gnUXaPtYE/0?wx_fmt=jpeg)

# java安全基础—注解

怪 咖/KimZing
怪 咖/KimZing

绿洲安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/yucJ5603pv6y9MicQevnPpS4CsCLTb4vl1TvOp58mSichNPWK2ibaZVbjg7xCnL6M4RDBu4PpbibwK9NszHvNfvHJA/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/mhIicicHPJQWHJs7GmXyfEYSLiadDbOoO8fdkFSzWf6j1blmwDCmIWqgnzJwkryWsJ6CtOskUMHnnEIuicHtyCq4jQ/640?from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=7)

**由于传播、利用本公众号绿洲安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号绿洲安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

```
参考链接：https://blog.csdn.net/weixin_43888891/article/details/126963074https://blog.csdn.net/KingBoyWorld/article/details/105337011
```

# 一、概念

1.1为什么要学注解？

 在日常开发中，基本都是在使用别人定义或是各种框架的注解，比如Spring框架中常用的一些注解：@Controller、@Service、@RequestMapping，以此来实现某些功能，但是却不知道如何实现的，所以如果想学习这些框架的实现原理，那么注解就是我们必知必会的一个点。其次，可以利用注解来自定义一些实现，比如在某个方法上加一个自定义注解，就可以实现方法日志的自动记录打印，这样也可以展现足够的逼格。所以如果你想走上人生巅峰，更好的利用框架，又或者想要高一点的逼格，从团队中突出，那么学习注解都是前提。

1.2注解是什么？

 在Java中注解其实就是写在接口、类 、属性、方法上的一个标签，或者说是一个特殊形式的注释，与普通的//或/\*\*/注释不同的是：普通注释只是一个注释，而注解在代码运行时是可以被反射读取并进行相应的操作，而如果没有使用反射或者其他检查，那么注解是没有任何真实作用的，也不会影响到程序的正常运行结果。

 举个例子@Override就是一个注解，它的作用是告诉阅读者(开发人员、编译器)这个方法重写了父类的方法，对于开发人员只是一个标志，而编译器则会多做一些事情，编译器如果发现方法标注了这个注解，就会检查这个方法到底是不是真的覆写了父类的方法，如果没有那就是在欺骗他的感情，甭废话，编译时直接给你报个错，不留情面的那种。而如果不添加@Override注解，程序也是可以正常运行的，不过缺乏了静态的检查，本来是想覆写父类的hello方法的，却写成了he110方法，这就会有些尴尬了。

在spring框架中加注的注解会影响到程序的运行，是因为spring内部使用反射操作了对应的注解。

 上面的说法是为了方便理解的，那么下面来个稍微正式一点的：注解是提供一种为程序元素设置元数据的方法，理解起来还是一样的，程序元素就是指接口、类、属性、方法，这些都是属于程序的元素，那啥叫元数据呢？就是描述数据的数据(data about data)，举个简单的例子，系统上有一个sm.png文件，这个文件才是我们真正需要的数据本身，而这个文件的属性则可以称之为sm.png的元数据，是用来描述png文件的创建时间、修改时间、分辨率等信息的，这些信息无论是有还是没有都不影响它作为图片的性质，都可以使用图片软件打开。

元数据是添加到程序元素如方法、字段、类和包上的额外信息，注解就是一种载体形式

注解不能直接干扰程序代码的运行

1.3为什么要使用注解？

 以Spring为例，早期版本的Spring是通过XML文件的形式对整个框架进行配置的，一个缩减版的配置文件 如下

```
<?xml version="1.0" encoding="UTF-8"?><beans xmlns="http://www.springframework.org/schema/beans">    <!-- 配置事物管理器 -->    <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">        <property name="dataSource" ref="dataSource"/>    </bean>    <!-- 配置注解驱动事物管理 -->    <tx:annotation-driven transaction-manager="transactionManager"/></beans>
```

在xml文件中可以定义Spring管理的Bean、事物切面等，话说当年非常流行xml配置的。优点呢就是整个项目的配置信息集中在一个文件中，从而方便管理，是集中式的配置。缺点也显而易见，当配置信息非常多的时候，配置文件会变得越来越大不易查看管理，特别是多人协作开发时会导致一定的相互干扰。

 现在都提倡解耦、轻量化或者说微小化，那么注解就顺应了这一需求，各个包或模块在内部方法或类上使用注解即可实现指定功能，而且使用起来灰常方便，简单易懂。缺点呢就是不方便统一管理，如果需要修改某一类功能，则需要整体搜索逐个修改，是分散式的存在各个角落。

 这里扩充一下，Spring注解替代了之前Spring xml文件，是不是说spring的xml也是一种元数据呢？对的，spring的配置文件xml也是元数据的一种表现形式。不过xml的方式是集中式的元数据，不需要和代码绑定的，而注解是一种分散式的元数据设置方式。

1.4注解的作用

 作为 Java开发几乎都使用过一些框架，相信大家对注解的作用都是有所体会的，这里再啰嗦几句加深印象。根本来说注解就是一个注释标签。开发者的视角可以解读出这个类/方法/属性的作用以及该怎么使用，而从框架的视角则可以解析注解本身和其属性实现各种功能，编译器的角度则可以进行一些预检查(@Override)和抑制警告(@SuppressWarnings)等。

作为特定标记，用于告诉编译器一些信息

编译时动态处理，如动态生成代码

运行时动态处理，作为额外信息的载体，如获取注解信息

## 1.5 什么是注解？

Java注解（Annotation），也叫元数据。一种代码级别的说明。它是JDK1.5及以后版本引入的一个特性，与类、接口、枚举是在同一个层次。它可以声明在包、类、字段、方法、局部变量、方法参数等的前面，用来对这些元素进行说明，注释。

如果要对于元数据的作用进行分类，还没有明确的定义，不过我们可以根据它所起的作用，大致可分为三类：

```
① 编写文档：通过代码里标识的元数据生成文档【生成文档doc文档】② 代码分析：通过代码里标识的元数据对代码进行分析【使用反射】③ 编译检查：通过代码里标识的元数据让编译器能够实现基本的编译检查【Override】
```

```
注解是以‘@注解名’在代码中存在的，根据注解参数的个数，我们可以将注解分为：标记注解、单值注解、完整注解三类。它们都不会直接影响到程序的语义，只是作为注解（标识）存在，我们可以通过反射机制编程实现对这些元数据（用来描述数据的数据）的访问。
```

## 1.2. 什么是元数据？

元数据是一个非常广泛的概念，元数据的定义也非常简单，只要是描述数据的数据都是元数据。很简单，一个数字170，单看数据你肯定不知道这个数据代表什么，这就需要元数据支持，你才能明白数据代表的事实是什么。它可能是一个人的身高，也可能指一个人的体重，这需要数据对应的标题、单位等信息来描述这个数据，这些就是描述这个数据的元数据了

## 1.3. 注解的属性

注解的属性也叫做成员变量。注解只有成员变量，没有方法。注解的成员变量在注解的定义中以“无形参的方法”形式来声明，其方法名定义了该成员变量的名字，其返回值定义了该成员变量的类型。

```
@Target(ElementType.TYPE)@Retention(RetentionPolicy.RUNTIME)public @interface TestAnnotation {    int id();    String msg();}
```

上面代码定义了 TestAnnotation 这个注解中拥有 id 和 msg 两个属性。在使用的时候，我们应该给它们进行赋值。

赋值的方式是在注解的括号内以 value=”” 形式，多个属性之前用 ，隔开。

```
@TestAnnotation(id=3,msg="hello annotation")public class Test {}
```

需要注意的是，在注解中定义属性时它的类型必须是 8 种基本数据类型外加 类、接口、注解及它们的数组。

注解中属性可以有默认值，默认值需要用 default 关键值指定。比如：

```
@Target(ElementType.TYPE)@Retention(RetentionPolicy.RUNTIME)public @interface TestAnnotation {    public int id() default -1;    public String msg() default "Hi";}
```

```
TestAnnotation 中 id 属性默认值为 -1，msg 属性默认值为 Hi。
```

# 二、根据【注解参数】 分类

根据注解参数的个数，我们可以将注解分为：标记注解、单值注解、完整注解三类。

## 2.1. 标记注解

标记注解不包含成员/元素。它仅用于标记声明。

其语法为：@AnnotationName()

由于这些注解不包含元素，因此不需要括号。例如：@Override

## 2.2. 单元素注解

单个元素注解仅包含一个元素。

其语法为：@AnnotationName(elementName = "elementValue")

如果只有一个元素，则习惯上将该元素命名为value：@AnnotationName(value = "elementValue")
在这种情况下，也可以移除元素名称。元素名称默认为value：@AnnotationName("elementValue")

## 2.3. 多元素注解

这些注解包含多个用逗号分隔的元素。

其语法为：@AnnotationName(element1 = "value1", element2 = "value2")

# 三、根据【注解作用】分类

## 3.1. 预定义的注解

这几个注解都是java.lang包下的，也就是Java提供的基础注解，我们在使用的时候是不需要导包的！

### 3.1.1. @Deprecated

此注解可以用在方法，属性，类上，表示不推荐程序员使用，但是还可以使用，示例如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF64baWwHJRb46tr4gRhfoKJPTppBqzpQ50ppGvwktc7ExnGH8icSsaH0Q2PD6acx0qtDP2kSPKBo32KGn9e93XvUgeqHFDmJvbE/640?wx_fmt=png&from=appmsg)

```
/** * 测试Deprecated注解 * @author Administrator */public class DeprecatedDemoTest {    public static void main(String[]args) {        // 使用DeprecatedClass里声明被过时的方法        DeprecatedClass.DeprecatedMethod();    }}
class DeprecatedClass {    @Deprecated    public static void DeprecatedMethod() {    }}
```

### 3.1.2. @Override

它的作用是对覆盖超类中方法的方法进行标记，如果被标记的方法并没有实际覆盖超类中的方法，则编译器会发出错误警告。

```
public interface Test {    public String getStr();}class TestImpl implements Test{    // 假如返回参数和方法参数其中一个不一致，就会警告    @Override    public String getStr() {        return null;    }}
```

### 3.1.3. @SuppressWarnings

我们在写代码的时候，不论是导入的包，还是声明的对象，有时候会出现黄线，感觉就很难受！

@SuppressWarnings注解主要用在取消一些编译器产生的警告，警告对于运行代码实际上并没有影响，但是出于部分程序员具有洁癖的嗜好，通常会采用@SuppressWarnings来消除警告。

#### 示例一：警告如图所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF5BQ3dLsQ8GzJkZMT9TTzAhrQmweEibVlf761OO60PzP6z7uwLoIsics0SZ3hvJeMFnYOJicLlhBDp8AIx1ld5B03oBUjIvtFSy3E/640?wx_fmt=png&from=appmsg)

这只是一个service接口：

```
public interface BannerService {}
```

这时候我们在方法上加上@SuppressWarnings注解就可以消除这些警告的产生，注解的使用方式有三种：

　　@SuppressWarnings(“unchecked”) [^ 抑制单类型的警告]
　　@SuppressWarnings(“unchecked”,“rawtypes”) [^ 抑制多类型的警告]
　　@SuppressWarnings(“all”) [^ 抑制所有类型的警告]

```
通过源码分析可知@SuppressWarnings其注解目标为类、字段、函数、函数入参、构造函数和函数的局部变量。建议把注解放在警告发生的位置。
```

消除警告：

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF5xp1gXSbcFwbia0Kkbfia6DyW6OlarxGib7E0zJ32AJ3icicDdic5XtoDwMROOeeVVh2EPzmdh3O83gqXqYOwuJaUKmALCs3lAYDP3s/640?wx_fmt=png&from=appmsg)

```
这个警告是spring framerwork 4.0以后开始出现的，spring 4.0开始就不推荐使用属性注入，改为推荐构造器注入和setter注入。当然他只是推荐，如果我们想要消除警告也可以直接使用@Resource。尽管他推荐了，但是一般实际开发当中很少会使用构造器注入和setter注入。
```

@Autowired 是Spring提供的，@Resource 是J2EE提供的。

　　@Autowired与@Resource都可以用来装配bean，都可以写在字段或setter方法上

　　@Autowired默认按类型装配，默认情况下必须要求依赖对象存在，如果要允许null值，可以设置它的required属性为false。如果想使用名称装配可以结合@Qualifier注解进行使用。

　　@Resource，默认按照名称进行装配，名称可以通过name属性进行指定，如果没有指定name属性，当注解写在字段上时，默认取字段名进行名称查找。如果注解写在setter方法上默认取属性名进行装配。当找不到与名称匹配的bean时才按照类型进行装配。但是需要注意的是，如果name属性一旦指定，就只会按照名称进行装配。

#### 示例二：警告如图所示

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF52JhkbRPS6OYqib5iaxMWLPg1Y5fYNbHQMzfYJE4yZkd2ZLedkZ1icaZaFh3JE3FkBRjAcUd3tpSY2mPRurFcoYRKYIc5SBjXB4s/640?wx_fmt=png&from=appmsg)

通过添加`@SuppressWarnings("unchecked")`来消除`unchecked`的警告，这个警告实际上主要是集合没有加泛型导致的！

![](https://mmbiz.qpic.cn/mmbiz_png/goxicFBGKAF7pjj9IOoib5osiaBXJWico3vmfJo5HRSdNZdMkGDSic1CIhe293YWl8Tp845YxXeJk4PeQhqUYwsEsgibQ6eibek3bbBLEmhHDDFPAQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/goxicFBGKAF6E4ib0nB3bMImcEMmicHjWibGTgXYJkD3U3WjLhJxkyF3vHiccCiaJXoXLPSvlLwOhhQbCk5mB9FWcnibytfNCFQicKyAQ2CzmnMVj70/640?wx_fmt=png&from=appmsg)

### 3.1.4. @SafeVarargs

在声明具有模糊类型（比如：泛型）的可变参数的构造函数或方法时，Java编译器会报unchecked警告。鉴于这些情况，如果程序员断定声明的构造函数和方法的主体不会对其varargs参数执行潜在的不安全的操作，可使用@SafeVarargs进行标记，这样的话，J...