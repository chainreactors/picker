---
title: Fastjson反序列化漏洞复现
url: https://yanghaoi.github.io/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/
source: Yang Hao's blog
date: 2024-08-19
fetch_date: 2025-10-06T18:03:31.229866
---

# Fastjson反序列化漏洞复现

[![LOGO](https://cdn.jsdelivr.net/gh/yanghaoi/yanghaoi.github.io/medias/logo.png)
Yang Hao's blog](/)

* [首页](/)
* 文章
  + [标签](/tags)
  + [分类](/categories)
  + [归档](/archives)
* [关于](/about)
* [留言板](/contact)
* [友情链接](/friends)

![](https://cdn.jsdelivr.net/gh/yanghaoi/yanghaoi.github.io/medias/logo.png)

Yang Hao's blog

Yang Hao's blog

* [首页](/)
* 文章
  + [标签](/tags%20)
  + [分类](/categories%20)
  + [归档](/archives%20)
* [关于](/about)
* [留言板](/contact)
* [友情链接](/friends)

# Fastjson反序列化漏洞复现

[Fastjson](/tags/Fastjson/)

[漏洞复现](/categories/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0/)

发布日期:
2024-08-18

更新日期:
2025-01-24

文章字数:
22.6k

阅读时长:
111 分

阅读次数:

---

## 0x01 简介

Fastjson 是阿里巴巴开源的一个高性能 JSON 库，广泛应用于 Java 应用中进行 JSON 数据的解析和序列化。然而，由于其功能强大且支持多种 Java 对象的自动反序列化，Fastjson 在历史上多次暴露出严重的安全漏洞，特别是反序列化漏洞。此类漏洞允许攻击者通过精心构造的恶意 JSON 数据包，实现对目标系统的远程代码执行（RCE），从而在未经授权的情况下控制受害者的服务器。本文通过学习`fastjson`的基础知识，整理了一些公开的Payload，并搭建实验环境进行测试。

## 0x02 Fastjson相关介绍

Fastjson是阿里巴巴的开源JSON解析库，它是由Java语言编写的JSON处理器/解析器。Fastjson提供了一种快速、高效的方式来处理JSON数据，可以将Java对象转换为JSON格式的数据，也可以将JSON格式的数据转换为Java对象。Fastjson具有高性能和低内存占用的特点，在Java开发中被广泛应用于处理JSON数据。

FastJson因为Auto功能存在缺陷的原因，历史上出现过多次安全漏洞，目前官方针对`FastJson`的各种历史问题经过重构将其升级到了[fastjson2](https://github.com/alibaba/fastjson2)，在fastjson2中提到升级的原因之一是安全性的提升:

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/image-20240422111207276.png)

fastjson2中完全删除`autoType`了白名单，且默认关闭`autoType`功能。在fastjson1项目中反序列化漏洞产生的根本原因就是对`autoType`功能利用和限制绕过，攻击者可以通过精心构造的类和数据包进行命令执行。

### 序列化和反序列化

为了理解反序列化漏洞，先来解释下序列化和反序列化。在Java中，序列化是将对象转换为字节序列的过程，这些字节可以被保存到磁盘或数据库，也可以通过流进行发送，序列化通常用于通信（在多个主机之间共享对象）和持久性（将对象状态存储在文件或数据库中）。而从字节序列创建对象的反向过程则称为反序列化。在fastjson中使用序列化和反序列化进行对象和JSON字符串的转换如下:

```
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.ParserConfig;
import java.io.IOException;
public class Main {
    public static void main(String[] args) {
        // 将一个 Java 对象序列化为 JSON 字符串
        Person person = new Person("张三", 40,1);
        String jsonString = JSON.toJSONString(person);
        System.out.println(jsonString);

        // 将一个 JSON 字符串反序列化为 Java 对象
        String jsonString2 = "{\"name\":\"李四\",\"age\":55,\"sex\":1 }";
        Person person2 = JSON.parseObject(jsonString2, Person.class);
        System.out.println("name:" + person2.name + " sex:"+ person2.getSex() + " age:"+person2.getAge());
        return ;
    }
    // 定义一个类
    public static class Person {
        private String name;private int age;private int sex;
        public Person(String name, int age,int sex) {
            this.name = name;this.age = age;this.sex = sex;
        }
        public String getName() {return name;}
        public int getAge() {return age;}
        public int getSex() {return sex;}
    }
}
```

执行代码后，第一次输出将对象转为了JSON字符串，第二次将JSON字符串反序列化为了对象并输出了对象的属性:

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/image-20240423173312776.png)

FastJSON 在序列化和反序列化时，会根据 getter 和 setter 方法来操作对象的属性（在 Java 中，setter 和 getter 是一种常见的编程模式，即通过反射的方式对类的属性进行读取和设置操作），下面的示例可以验证这一点:

```
import com.alibaba.fastjson.JSON;
public class Main {
    public static void main(String[] args) {
        // 创建一个 Person 对象
        Person person = new Person();
        person.setName("Alice");
        person.setAge(30);

        // 序列化对象为 JSON 字符串
        String jsonString = JSON.toJSONString(person);
        System.out.println("Serialized JSON: " + jsonString);

        // 反序列化 JSON 字符串为对象
        Person newPerson = JSON.parseObject(jsonString, Person.class);

        // 打印反序列化后的对象属性值
        System.out.println("Deserialized Person:");
        System.out.println("Name: " + newPerson.getName());
        System.out.println("Age: " + newPerson.getAge());
    }

    public static class Person {
        private String name;
        private int age;

        // Getter 方法
        public String getName() {
            System.out.println("getName");
            return name;
        }

        // Setter 方法
        public void setName(String name) {
            System.out.println("setName");
            this.name = name;
        }

        // Getter 方法
        public int getAge() {
            return age;
        }

        // Setter 方法
        public void setAge(int age) {
            this.age = age;
        }
    }
}
```

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/image-20240424003548130.png)

### Autotype功能

`fastjson` 的 `AutoType` 功能是在 1.2.22 版本引入的。`AutoType` 允许在反序列化过程中自动识别和实例化指定类型的对象，这是通过在 JSON 数据中嵌入类型信息来实现的。然而，这一功能也带来了安全风险，尤其是在未经验证的输入情况下，可能导致反序列化漏洞，允许攻击者执行任意代码。由于这些安全风险，后续版本开发者和安全研究人员对`AutoType`功能进行了多次修复和修复绕过的攻防对抗。

为了理解`autotype`的作用，编写如下代码，代码定义了一个名为 `Person` 的静态内部类，以及一个名为 `City` 的接口和一个实现了 `City` 接口的静态内部类 `Home`，`fastjson`在对这样的类进行序列化和反序列化结果如下:

```
import com.alibaba.fastjson.JSON;
public class Main {
    public static void main(String[] args) {
        // 创建一个 Person 对象
        Person person = new Person();
        person.setName("Alice");
        person.setAge(30);

        Home home = new Home();
        home.setCityname("chengdu");
        person.setCity(home);

        // 序列化对象为 JSON 字符串
        String jsonString = JSON.toJSONString(person);
        System.out.println("Serialized JSON: " + jsonString);

        // 反序列化 JSON 字符串为对象
        Person newPerson = JSON.parseObject(jsonString, Person.class);

        // 打印反序列化后的对象属性值
        System.out.println("Deserialized Person:");
        // 这里转换时，不知道Home类型是哪里来的，强制转换就会失败
        Home newHome =  (Home) newPerson.getCity();
        System.out.println("newHome : " + newHome);
        System.out.println("Name: " + newPerson.getName());
        System.out.println("Age: " + newPerson.getAge());
    }

    public static class Person {
        private String name;
        private int age;
        private City city;

        public City getCity() {
            System.out.println("getcity");
            return city;
        }

        // Getter 方法
        public String getName() {
            System.out.println("getName");
            return name;
        }

        // Setter 方法
        public void setName(String name) {
            System.out.println("setName");
            this.name = name;
        }

        // Getter 方法
        public int getAge() {
            return age;
        }

        // Setter 方法
        public void setAge(int age) {
            this.age = age;
        }

        public void setCity(City city) {
            this.city = city;
        }
    }

    interface City {

    }

    static class Home implements City {
        private String cityname;

        public String getCityname() {
            return cityname;
        }

        public void setCityname(String cityname) {
            this.cityname = cityname;
        }
    }
}
```

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/image-20240424010257053.png)

序列化字符串中的`"city":{"cityname":"chengdu"}`应该是`Home`类型，但是`fastjson`并没有成功转换，抛出了异常。为了解决这个问题，`fastjson`引入了`autotype`功能，利用该功能在序列化时标记类对应的原始类型，指定具体的解析类:

```
import com.alibaba.fastjson.serializer.SerializerFeature;
//使用 SerializerFeature.WriteClassName
String jsonString = JSON.toJSONString(person, SerializerFeature.WriteClassName);
```

这样序列化的JSON字符串就会带上`@type`指定需要转换的类型:

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-jue-he-li-yong-fang-fa/image-20240424093917809.png)

当 autotype 功能启用时，Fastjson会尝试根据 JSON 字符串中的类型信息（即 @type 的值）来自动转换为相应的Java对象类型，同时 Fastjson 基于 setter/getter 的转换方式可以在转换类型时设置对象的参数，这就导致可以引入未经授权的类实例化、执行恶意代码或获取系统权限的安全风险。在FastJson漏洞的利用过程中一般是利用目标类执行JNDI注入、指定字节码加载、文件写入等。

### parseObject和parse

在 Fastjson 中，有两种反序列化接口可供使用：`JSON.parse` 和 `JSON.parseObject`。其中，`JSON.parseObject` 会自动扫描类中的 getter 方法，并根据 JSON 字符串中的属性值自动匹配 setter 方法来设置对象的属性值。因此，使用 `JSON.parseObject` 方法可以方便地将 JSON 字符串转换为相应的 Java 对象，无需手动转换类型。相反，`JSON.parse` 方法不会自动扫描 getter 方法，而是将 JSON 字符串直接解析为一个 `JSONObject` 对象或其他 JSON 数据类型。因此，`JSON.parse` 方法返回的是一个 `Object` 类型的对象，如果需要将其转换为特定的 Java 对象类型，则需要手动进行类型转换。强制类型转换可能会导致 `ClassCastException` 异常。如下代码进使用`JSON.parse`转换数据类型时会导致异常:

![](/2024/08/18/fastjson-lou-dong-chang-jian-wa-ju...