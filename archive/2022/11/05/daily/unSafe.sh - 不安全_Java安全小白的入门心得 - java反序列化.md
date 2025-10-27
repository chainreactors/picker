---
title: Java安全小白的入门心得 - java反序列化
url: https://buaq.net/go-134213.html
source: unSafe.sh - 不安全
date: 2022-11-05
fetch_date: 2025-10-03T21:42:45.313544
---

# Java安全小白的入门心得 - java反序列化

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/131dd17910cf8cea11df6187d9c004dc.jpg)

Java安全小白的入门心得 - java反序列化

本文为看雪论坛优秀文章看雪论坛作者ID：1manityJava反序列化是java安全的基础，想要学好java反序列化，就不能只看看相关文章，要自己动手实践，看看java反序列化到底是怎么回事。JSON
*2022-11-4 17:58:50
Author: [mp.weixin.qq.com(查看原文)](/jump-134213.htm)
阅读量:22
收藏*

---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6Ddn54b8vpGXbwicibgYbbcuUopmSmWA9uiavtkMhaQOyWc5s6ic0l3W57w/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：1manity

Java反序列化是java安全的基础，想要学好java反序列化，就不能只看看相关文章，要自己动手实践，看看java反序列化到底是怎么回事。

### JSON和XML是通用数据交互格式，通常用于不同语言、不同环境下数据的交互，比如前端的JavaScript通过JSON和后端服务通信、微信服务器通过XML和公众号服务器通信。但这两个数据格式都有一个共同的问题：不支持复杂的数据类型。大多数处理方法中，JSON和XML支持的数据类型就是基本数据类型，整型、浮点型、字符串、布尔等，如果开发者希望在传输数据的时候直接传输一个对象，那么就不得不想办法扩展基础的JSON（XML）语法。

### **快速入门**

Java Serialization(序列化)：将java对象以一连串的字节保存在磁盘文件中的过程，也可以说是保存java对象状态的过程。序列化可以将数据永久保存在磁盘上(通常保存在文件中)。

下面我们就手敲代码，自己实现一个序列化程序！

```
public class main {    private static class innerClass implements Serializable {        String name;        String test;        int years;         public innerClass(){}        public innerClass(String name, String test, int years) {            this.name = name;            this.test = test;            this.years = years;        }         @Override        public String toString() {            return "innerClass{" +                    "name='" + name + '\'' +                    ", test='" + test + '\'' +                    ", years=" + years +                    '}';        }    }    public static void main(String[] args) throws Exception {        innerClass ic = new innerClass();//创建对象        ic.name="123";        ic.test="test";        ic.years=123546;        File f = new File("java_security/1.txt");// 模块名/文件名        if(f.exists()) {            System.out.println("文件存在");        }else{            //否则创建新文件            f.createNewFile();        }        try{            FileOutputStream fos=new FileOutputStream(f);            ObjectOutputStream oos=new ObjectOutputStream(fos);            oos.writeObject(ic);//将ic对象序列化写入文件            oos.flush();            oos.close();            fos.close();        }catch (Exception e) {            System.out.println(e);        }    }}
```

注意点：

```
1、序列化对象需要实现Serializable接口2、序列化需要使用ObjectOutputStream对象创建对象输出流3、ObjectOutputStream对象序列化所用方法writeObject()4、ObjectOutputStream对象需要文件输出流作为输出目标5、FileOutputStream对象需要一个文件对象
```

因此，我们整个实现过程为：创建需要序列化的对象、创建文件对象、创建文件输出流对象、创建对象输出流对象、序列化。

运行程序，我们得到1.txt。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6uNV8nccF1LlFMjzUBgjkmmV61jOibt0Fbib9YuxBdXUzyFPfwBHtCIyA/640?wx_fmt=png)

可以看到，在java\_security模块下生成了1.txt文件，里面包含着innerClass对象（即我刚刚序列化的对象）的序列化字节码。

这些字节码都是我们人为不可看的，很不利于我们在对于java反序列化或者java安全方面的研究，有什么办法能解决这个问题呢？

### **SerializationDumper**

我们可以使用SerializationDumper来将序列化字节码转化为方便阅读的形式，下面我们就一起来装一下SerializationDumper吧。

```
git clone https://github.com/NickstaDB/SerializationDumper.git
```

进入安装路径，执行build.bat 文件。

```
E:\web-Tools\SerializationDumper> build.bat
```

然后就可以在该目录中使用SerializationDumper.jar了，接下来我们就试试使用SerializationDumper。

将SerializationDumper拖入项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6TOZHtgmLia4HQ6CX9zUZXOIF4CAelvFEDjOiat90AKjbKxlP6SwVKcTA/640?wx_fmt=png)

```
E:\IntelliJ IDEA 2018.2.7\project\java_security>java -jar SerializationDumper.jarUsage:        SerializationDumper <hex-ascii-data>        SerializationDumper -f <file-containing-hex-ascii>        SerializationDumper -r <file-containing-raw-data> Rebuild a dumped stream:        SerializationDumper -b <input-file> <output-file>
```

按照上述使用方法 使用 -r 处理raw-data文件。

```
E:\IntelliJ IDEA 2018.2.7\project\java_security>java -jar SerializationDumper.jar -r 1.txt > 2.txt STREAM_MAGIC - 0xac edSTREAM_VERSION - 0x00 05Contents  TC_OBJECT - 0x73    TC_CLASSDESC - 0x72      className        Length - 15 - 0x00 0f        Value - main$innerClass - 0x6d61696e24696e6e6572436c617373      serialVersionUID - 0xca 3e 75 e0 69 b7 50 c5      newHandle 0x00 7e 00 00      classDescFlags - 0x02 - SC_SERIALIZABLE      fieldCount - 3 - 0x00 03      Fields        0:          Int - I - 0x49          fieldName            Length - 5 - 0x00 05            Value - years - 0x7965617273        1:          Object - L - 0x4c          fieldName            Length - 4 - 0x00 04            Value - name - 0x6e616d65          className1            TC_STRING - 0x74              newHandle 0x00 7e 00 01              Length - 18 - 0x00 12              Value - Ljava/lang/String; - 0x4c6a6176612f6c616e672f537472696e673b        2:          Object - L - 0x4c          fieldName            Length - 4 - 0x00 04            Value - test - 0x74657374          className1            TC_REFERENCE - 0x71              Handle - 8257537 - 0x00 7e 00 01      classAnnotations        TC_ENDBLOCKDATA - 0x78      superClassDesc        TC_NULL - 0x70    newHandle 0x00 7e 00 02    classdata      main$innerClass        values          years            (int)123546 - 0x00 01 e2 9a          name            (object)              TC_STRING - 0x74                newHandle 0x00 7e 00 03                Length - 3 - 0x00 03                Value - 123 - 0x313233          test            (object)              TC_STRING - 0x74                newHandle 0x00 7e 00 04                Length - 4 - 0x00 04                Value - test - 0x74657374
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6Ps2bHu4CEWgoX4KwZnbqcNnpJXFQsvNQupUOP9RAXRY5kjxDjhDnow/640?wx_fmt=png)

这里就可以很清楚的看到，跟我们之前设定的属性是相符合的。

### **反序列化**

```
try{    FileInputStream fis=new FileInputStream("java_security/1.txt");    ObjectInputStream ois = new ObjectInputStream(fis);    innerClass ic2=(innerClass)ois.readObject();    System.out.println(ic2);    ois.close();    fis.close();}catch(Exception e) {    System.out.println(e);}
```

与序列化的代码片相反，反序列化将文件内的字节流重新反序列化为对象。反序列化流程如上，便不再赘述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6Ftqefiaw0YeKT9Gcq2tceQS3BFvibxrNxHcY6ja0Nq3HB9nsSg0mtqBg/640?wx_fmt=png)

###

### **复写readObject和writeObject**

经过上面简单的案例，大家应该能了解到序列化与反序列化的大体步骤，接下来就开始了解readObject和writeObject的复写。

> 进阶的一些小trick

我们看到类实现的Serializable 接口，它是没有任何内容的，相当于一个标识符。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6DAFynjDBg7DKmQ8PHIZSLr2icVwOnmuiciaK3kkZ1yo4X1QY2gFSNdqIw/640?wx_fmt=png)

那么我们该怎么复写readObject和writeObject呢。分析源码：

```
public final void writeObject(Object obj) throws IOException {    if (enableOverride) {        writeObjectOverride(obj);        return;    }    try {        writeObject0(obj, false);    } catch (IOException ex) {        if (depth == 0) {            writeFatalException(ex);        }        throw ex;    }}
```

首先从writeObject方法进了writeObject0。

```
if (obj instanceof String) {                writeString((String) obj, unshared);            } else if (cl.isArray()) {                writeArray(obj, desc, unshared);            } else if (obj instanceof Enum) {                writeEnum((Enum<?>) obj, desc, unshared);            } else if (obj instanceof Serializable) {                writeOrdinaryObject(obj, desc, unshared);            } else {                if (extendedDebugInfo) {                    throw new NotSerializableException(                        cl.getName() + "\n" + debugInfoStack.toString());                } else {                    throw new NotSerializableException(cl.getName());                }            }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F5V7f1m8kiaIHdr9YtSI0H6hahWfJscias9jUQND4A5XlKBhN3NBJwpGs6odQG5TCEnKQ1uGtwbzPQ/640?wx_fmt=png)

跟踪语句，我们找到了这样一句，若obj或其子类实现了Serializable，则进入这个判断语句，即进入writeOrdinaryObject方法。

> instanceof 是java的保留关...