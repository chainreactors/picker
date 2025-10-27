---
title: 利用TemplatesImpl执行字节码在实战中的踩坑记录
url: https://y4tacker.github.io/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/
source: Y4tacker's Blog
date: 2023-04-26
fetch_date: 2025-10-04T11:33:01.593967
---

# 利用TemplatesImpl执行字节码在实战中的踩坑记录

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

Previous post Next post Back to top Share post

1. [1. 利用TemplatesImpl执行字节码在实战中的踩坑记录](#%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95)

# 利用TemplatesImpl执行字节码在实战中的踩坑记录

Y4tacker

2023-04-25 (Updated: 2024-08-04)

[Java](/categories/Java/)

[Java](/tags/Java/), [TemplatesImpl](/tags/TemplatesImpl/), [踩坑记录](/tags/%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/)

# 利用TemplatesImpl执行字节码在实战中的踩坑记录

在平时，无论是JNDI注入，还是反序列化，只要涉及到不出网的场景，TemplatesImpl的利用就很广泛，这里记录一个在实战中遇到的踩坑记录，篇幅不多贵在记录。

假设当前服务器存在反序列化漏洞，不出网，当你兴高采烈的拿着工具去打的时候发现怎么也打不通，内存马上不去，回显也没有，这是怎么回事呢？且看下文。

既然需要使用TemplatesImpl加载字节码，那么就需要生成恶意类的Bytecode

这里我们再温习一下，最终在getTransletInstance方法处加载字节码到jvm，并调用newInstance实例化触发恶意代码的加载

![image-20230425223608324](/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/image-20230425223608324.png)

网上的各种工具，基本上都使用了javassist框架进行恶意类的生成，这里以TomcatEcho为例，大多数工具代码都类似下面的写法，创建类，添加方法，生成ByteCode

![image-20230425224758672](/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/image-20230425224758672.png)

问题就出在输出ByteCode的过程中，当调用`ClassPool.getDefault()`的过程中，会初始化ClassFile，根据某些不同版本特定存在的类来判断当前环境的`MAJOR_VERSION`(Ps:这里的反编译有点问题，从上到下ver其实是依次从49到55)，这个`MAJOR_VERSION`其实就是我们java的主版本号从49-55分别为jdk1.5到jdk11

![image-20230425224938019](/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/image-20230425224938019.png)

因此这就很有意思了，这意味着使用javassist生成的字节码的属性信息和当前java运行环境有关

假设当前服务器是一个jdk1.6跑着的tomcat服务，你拿工具打，那很显然jdk1.6并不能运行1.8版本下编译的程序，那怎么办呢？其实很简单修改这个`MAJOR_VERSION`就行，只要这个属性的数值小于或等于当前运行的java环境那就能过检查并运行

而javassist本身也提供了对应的api去帮助我们修改，比如我们需要生成1.6能运行的字节码，我们只需要在原来的基础上加上`clazz.getClassFile().setMajorVersion(50);`即可

![image-20230425230030584](/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/image-20230425230030584.png)

那如果是asm框架怎么办，就更简单了，创建类的时候在第一个输入写上对应主版本号即可

![image-20230425230127178](/2023/04/25/year/2023/4/%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95/image-20230425230127178.png)

Please enable JavaScript to view the comments.

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

1. [1. 利用TemplatesImpl执行字节码在实战中的踩坑记录](#%E5%88%A9%E7%94%A8TemplatesImpl%E6%89%A7%E8%A1%8C%E5%AD%97%E8%8A%82%E7%A0%81%E5%9C%A8%E5%AE%9E%E6%88%98%E4%B8%AD%E7%9A%84%E8%B8%A9%E5%9D%91%E8%AE%B0%E5%BD%95)

Menu TOC Share Top

Copyright © 2016-2025 Y4tacker

* [Home](/)
* [Writing](/archives/)
* [Topics](/tags/)
* [Search](/search/)
* [About](/about/)
* [Friends](/link/)

本站总访问量次 | 本站访客数人