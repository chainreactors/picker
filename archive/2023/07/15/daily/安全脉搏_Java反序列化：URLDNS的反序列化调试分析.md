---
title: Java反序列化：URLDNS的反序列化调试分析
url: https://www.secpulse.com/archives/202757.html
source: 安全脉搏
date: 2023-07-15
fetch_date: 2025-10-04T11:51:13.971948
---

# Java反序列化：URLDNS的反序列化调试分析

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

# Java反序列化：URLDNS的反序列化调试分析

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-07-14

50,348

URLDNS链子是Java反序列化分析的第0课，网上也有很多优质的分析文章。

笔者作为Java安全初学者，也从0到1调试了一遍，现在给出调试笔记。

## 一. Java反序列化前置知识

> Java原生链序列化：利用Java.io.ObjectInputStream对象输出流的writerObject方法实现Serializable接口，将对象转化成字节序列。

> Java原生链反序列化：利用Java.io.ObjectOutputStream对象输入流的readObject方法实现将字节序列转化成对象。

测试源码如下，此部分源码参考了ol4three师傅的博客：

```
package serialize;

import java.io.*;

public class deserTest implements Serializable {
    private int n;
    public deserTest(int n) {
        this.n=n;
    }

    @Override
    public String toString() {
        return "deserTest2 [n=" + n + ", getClass()=" + getClass() + ", hashCode()=" + hashCode() + ", toString()="
                + super.toString() + "]";
    }

    // 反序列化
    private void readObject(java.io.ObjectInputStream in) throws IOException,ClassNotFoundException{
        in.defaultReadObject();
        Runtime.getRuntime().exec("calc");
        System.out.println("test");
    }

    public static void main(String[] args) {
        deserTest x = new deserTest(5);
        operation1.ser(x);
        operation1.deser();
        x.toString();
    }
}

// 实现序列化和反序列化具体细节的类
class operation1{

    // 将输出字节流写入文件中进行封存
    public static void ser(Object obj) {
        // 序列化操作，写操作
        try {
             // 首先文件落地object.obj存储输出流，绑定输出流
            ObjectOutputStream ooStream = new ObjectOutputStream(new FileOutputStream("object.obj"));

            // 重定向将输出流字节写入文件
            ooStream.writeObject(obj);

            ooStream.flush();
            ooStream.close();

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }catch (IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        }
    }

    public static void deser() {
        // 反序列化，读取操作
        try {
            // 绑定输入流
            ObjectInputStream iiStream = new ObjectInputStream(new FileInputStream("object.obj"));

            // 反序列化时需要从相关的文件容器中读取输出的字节流
            // 读取字节流操作为readObject,所以重写readObject可以执行自定义代码
            Object xObject = iiStream.readObject();
            iiStream.close();
        } catch (IOException e) {
            // TODO: handle exception
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

![image-20230622200428296](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230622200428296.png)

## 二. ysoserial环境搭建

IDE就直接用JetBrains的IDEA就行

直接拿Java安全payload集成化工具ysoserial进行分析，这里面已经有现成的环境了

<https://github.com/frohoff/ysoserial>

注意配置好相应的`JDK`和`SDK`版本：

![image-20230704224019895](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230704224019895.png)

## 三. URLDNS攻击链

* 影响的版本问题：与JDK版本无关，其攻击链实现依赖于Java内置类，与第三方库无关
* URLDNS这条反序列化链只能发起DNS请求，无法进行其他利用，可以作为验证是否有反序列化漏洞的姿势

##### 调试分析

> Gadget Chain：
>
> Deserializer.deserialize() -> HashMap.readObject() -> HashMap.putVal() -> HashMap.hash() ->URL.hashCode() ->
>
> getHostAddress()
>
> 在getHostAddress函数中进行域名解析，从而可以被DNSLog平台捕获

##### URLDNS程序入口

在`ysoserial-master\src\main\java\ysoserial\payloads\URLDNS.java`路径下有`URLDNS.java`文件

【---- 帮助网安学习，以下所有学习资料免费领！领取资料加 we~@x：yj009991，备注 “安全脉搏” 获取！】
① 网安学习成长路径思维导图
② 60 + 网安经典常用工具包
③ 100+SRC 漏洞分析报告
④ 150 + 网安攻防实战技术电子书
⑤ 最权威 CISSP 认证考试指南 + 题库
⑥ 超 1800 页 CTF 实战技巧手册
⑦ 最新网安大厂面试题合集（含答案）
⑧ APP 客户端安全检测指南（安卓 + IOS）

`main`主函数的`run函数`打断点进入

![image-20230704233815765](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230704233815765.png)

这个`ysoserial-master`的`payload`运行结构大致是有一个专门的`PayloadRunner`运行程序，然后统一调用来运行各部分的`payload`

首先是进行序列化：

![image-20230706141716624](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706141716624.png)

![image-20230706142531102](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706142531102.png)

继续往下，生成`command`，由于是分析`URLDNS`攻击链，所以只需要修改将返回值为`dnslog`的临时地址

![image-20230706142701137](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706142701137.png)

创建实例后，进入到`URLDNS`的`getObject`的`payload`函数

![image-20230706143357422](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706143357422.png)

**getObject函数中应该注意的是：声明了HashMap对象和URL对象，并进行put哈希绑定，最后设置作用域**

![image-20230706170830440](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706170830440.png)

![image-20230706204403039](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706204403039.png)

##### 反序列化链子：

在反序列化入口处打断点：

![image-20230706195621770](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706195621770.png)

在反序列化时调用了`readObject`函数

![image-20230706201128369](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706201128369.png)

然后进入`HashMap.java`的`readObject`函数

![image-20230706201250160](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706201250160.png)

在`readObject`中调试到此行，了`putval`，在此处`IDEA`这个`IDE`可以选择进入的函数，直接进入后者`hash`

由于我们读入字节序列，需要将其恢复成相应的对象结构，那么就需要重新`putval`

![image-20230706201454673](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706201454673.png)

传入的`key`不为空，执行`key.hashCode`

![image-20230706211639259](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706211639259.png)

进一步在`URL.java`文件下

![image-20230706203125428](https://icfh-imgs-1313391192.cos.ap-nanjing.myqcloud.com/images/image-20230706203125428.png)

进入`URLStreamHandler`的`hashCode`

![image-20230706203401159](https://icfh-imgs-1313391192.c...