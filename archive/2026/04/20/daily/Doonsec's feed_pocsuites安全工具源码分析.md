---
title: pocsuites安全工具源码分析
url: https://mp.weixin.qq.com/s/t8Pi1hhPaNReLwW7BzzTYQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:47:48.502121
---

# pocsuites安全工具源码分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mwFvjeHDLkiaP2DXYq4pEY6FiaiaMQibgasShib34ETpqr1BBtm00SyOfGSgxGhsAAIpXic5Wfuvt4JUTECia0sMY1ffO6QicNoDib1R1O1z7ko1Yicvk/0?wx_fmt=jpeg)

# pocsuites安全工具源码分析

大白
大白

蚁景网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**pocsuite3 是由 知道创宇 404实验室 开发维护的开源远程漏洞测试和概念验证开发框架。为了更好理解其运行逻辑，本文将从源码角度分析该项目的初始化，多线程函数，poc模板等等源码**

# 项目结构

![IMG_256](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9LUVAw0ibVZy0pFtggoUxhckQyotpenOIiahH3Gu7cOE7LQYdGq5FGtgQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

api：对要导入的包重命名，方便后续导入调用 data：存储用户需要使用的文档数据 lib：项目核心代码 modules：存储用户自定义的模块 plugins：存储用户自定义的插件 pocs：存储poc文件 shellcodes：存储生成php，java，python等脚本语言的利用代码，以及反弹shell的利用代码 cli.py：项目的入口 console.py：命令行界面

进入项目入口：/pocsuite3/cli.py

![IMG_257](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9hhP6h1Yr2yALRhibLIx1keOg8MZHZx2gg96ApFGPUU0FicC4SWuEGMbg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

init\_options(cmd\_line\_parser().**dict**) # 命令行参数处理 跟进cmd\_line\_parser()查看：

![IMG_258](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9pYiajcqWiap76GfakbhJ1iaZNiccPBHMGp6VO5Jv5LB4U87crHdFjOxxEQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![IMG_259](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9LibPzusQAtuqdNrcKaDWRvXuBQpqj6IU1KX5ia3JHNOlNtiaXS4uthUZg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

双重跟进init\_options()，找到命令行存储参数：

![IMG_260](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib96XdGLIOb1mWU3xzncN22h7vusdJPn4VmhghUKWCny4upImdicGicicPAA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)可见采用了类似字典的形式存储，避免了重复数据 且还有其它四个参数也采用了该形式存储，五个参数贯穿整个项目

conf：存储基本配置信息 kb：存储了目标地址、加载的PoC、运行模式、输出结果、加载的PoC文件地址、多线程信息等 cmd\_line\_options：是存储命令行输入的参数值 merged\_options：存储输入值与默认值合并后的结果 paths：存储数据、插件、poc等目录地址

参数获取处理完后，进入项目初始化，init()函数，一下对部分函数进行注解分析：

def init():

"""

Set attributes into both configuration and knowledge base singletons

based upon command line and configuration file options.

"""

set\_verbosity() #日志输出级别设置

\_adjust\_logging\_formatter() #调整日志格式器

\_cleanup\_options() #将各个配置项格式化，并校验合法性

\_basic\_option\_validation() #校验seebug,zoomeye等api,token的合法性

\_create\_directory() #检测文件路径是否存在，不存在则创建

\_init\_kb\_comparison()

update()

\_set\_multiple\_targets() #读取目标

\_set\_user\_pocs\_path()

\_set\_pocs\_modules() #动态加载poc

\_set\_plugins() #动态加载插件

\_init\_targets\_plugins()

\_init\_pocs\_plugins()

\_set\_task\_queue() #初始化多线程设置

\_init\_results\_plugins() #初始化输出插件

# AttribDict类解析

前文也提到过以下五个全局变量，它们均通过创建AttribDict类的实例进行使用，现在我们跟进类详细分析：

![IMG_256](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9YqD7OJguA29Io8hibOVAPg0H4Gb86coNuYwaNlrgjDoYoGV9A3oia84Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

AttribDict()类：

![IMG_257](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9YXh8JvwL2Fr36H8akzj31VF0uuY2XTulZ1xPeO92S9qiaLGbt0FPxGQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

自定义类，继承自python内建的OrderedDict类，扩展访问方式，简化了对字典键的访问。主要存在三个方法：**getattr**(),**setattr**(),**delattr**() 这三个方法在if判断逻辑均相同：1:以双下划线 \_\_ 开头（例如，Python 的内置属性，如 **dict**）。2:以 *OrderedDict*\_ 开头（因为 OrderedDict 在内部实现中使用的名称）。3:名字存在于 **exclude\_keys** 集合中（排除的键）。如果任一条件成立，说明这个属性不应该通过 obj.attr 访问，所以跳过使用自定义的 **getattr**处理，直接调用父类对应的方法访问。例：**getattr**()就调用父类的\_\_getattribute\_\_()访问

如果属性名不满足，则通过字典的方式，添加或者删除AttribDict中

![IMG_258](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9icgtHmxhypUkCwBd1zA5jRic1J3g0kTvg1mpuBYHVD615ibyMrjhqBibHA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

# 地址处理代码分析

![IMG_256](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9HKV0yjHj9pIuug15ziawpP6SibrGfchPyAF5oDwqkoy2LiaIFicSEy0qvw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=8)先查看存储初始数据，存在则进行下一步。通过set()创建集合方便去重，再遍历conf.url数据，通过parde\_target()进行对url进行分析处理，并且在不为空的情况下调用集合的add()方法添加，完成后再将，用于临时存储的target集合里面的数据，放到kb这种全局变量内。parde\_target()函数

![IMG_257](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9j5icNgKZPDnibCx3Vnbd3yr6MlyriaX7KiciaMiaZcuNy0hpsuhicXeKEdyhw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

接受参数后先if判断，如果是域名，url，ip:端口形式则直接赋值给target 跟进其中一个判断函数：

![IMG_258](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9okFp1mqxd2xmxAOju3QnWcJ1icaORklhrMHf2EUek4dB1A6f6I3ic1jA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=10)

跟进：

![IMG_259](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9TA2xhRXUKsXnYh8g4RnuRdgDbhiaM8v3mdIBRLrzibZpJgsfcGXLOycA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=11)可见是通过正则进行判断。接着再判断如果为http://ipv6形式，则启动ipv6配置，并进行赋值target，依旧是正则判断。

再判断如果为ipv4则调用python内置ip\_address解析赋值，该方法自动区分ipv4或者ipv6并最后返回对应的对象。再通过else判断，对纯ipv6地址，或者ipv6网络进行解析赋值。

# 动态poc加载

![IMG_256](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9jiaLVrib8AicneXFrGzPkSqibZMWdZiagA96jr2ibRvOlIXFz7wXNA4lYEicA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)Step1：从pocs目录加载 先通过os.listdir读取对应目录，返回一个含有poc的py文件的列表。再通过filter()函数过滤\_\_init\_\_.之类文件，不过此时filter()函数返回的是一个迭代器，所以又通过list()函数将数据处理成列表再赋值。（lambda x: x not in ['**init**.py', '**init**.pyc']：这个匿名函数会检查每个文件名 x 是否不等于 '**init**.py' 或 '**init**.pyc'。）

再从含有类似thinkphp\_poc.py的文件名中，通过x变量循环读取，并通过splitex()函数将其分为"thinkphp\_poc",".py"格式的键值队元组。再次通过dict()字典函数，将x元组的第一个元素作为字典的键，第二个元素作为字典的值。

如果poc是目录，则使用 os.walk() 递归遍历该目录下的所有文件，过滤出 .py 或 .yaml 文件，并将其完整路径添加到 \_pocs 列表中。

Step2：遍历加载 PoC 文件内容并检查，并对加载失败的poc进行日志记录。

Step3：最后从 Seebug 网站加载 PoC。

poc模版 跟据目录找到现存poc：pocsuite3/pocs，thinkphp\_rce为例

![IMG_257](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9QkOqO0y7KE8XPCvO6J9S8IXOWyjMgeUuhTGjwTR9lYzkDsdD8qgjsg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=13)

所有模版均是继承自父类POCBase，跟进：

![IMG_258](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9HPJFKtIADlKWXUDleP19ibvSrHNZY8YIEoiauFTRFib3u11tNV3lOLWAQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=14)父类在初始化时便设置了一系列可能用到的属性，例如自定义headers，目标url，端口等等。这里关注execute()函数

![IMG_259](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9wvW2wQhpktPnxWmYibkyq5Tx8eeRlc8KlyiaLC2ibGecO5yXucRQdJdAQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=15)self.url处采用if判断：如果为http协议则采用parse\_target\_url()解析，else采用build\_url()解析：mode值默认为verify。随后调用\_execute()根据mode值执行。

![IMG_260](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9pziakUkSumBLC80VlGPwFkbGl5sNrQk57E5ib1S5UMRnyGZPTWACaVWA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=16) \_shell()，\_attack()，\_verify()均需自定义重写。回到例thinkphp\_rce例子：\_verify()函数如下：

![IMG_261](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9cnXyicEzTxwYZOUaciaIwF8O3yH3CpMvAUp5T1oibRsic2QVXAXRU3g7fw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=17)调用了\_check()函数进行检验：

![IMG_262](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9ovmPQkmUDJibnwxektiauOrrBZtnmKKrLEZC2wjlDHEaPicoribDHboOYg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=18)

通过request.post()发送设置好payload的请求，根据返回包关键字判断是否成功。（flag自定义） 返回的结果在\_verify()函数又会调用parse\_output()转化为json格式输出。

动态核心load\_file\_to\_module() 继续分析\_set\_pocs\_modules()

![IMG_263](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9Wwjyyc9icMFffExEHo0ibRGPicXEw9PAZvic32U0OlHV4z0UOPkPjKEVMg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=19)将读取文件切割为文件名和后缀名，根据后缀名重构路径file\_pth，if判断file\_path构建成功则进入红框代码处。

![IMG_264](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldydQmSslgMg5at3lUYlTlib9GyvKbB7xOgWpK6mlibS9HKicCicOvaad2VRcZ6rWvTSiaAYKMibNMTFEzQg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

通过get\_filename()从file\_path路径提取文件名，由于wuth.ext=False，则不提取文件名后缀，提取后拼接在pocs\_后并赋值给module，例如：pocs\_thinkphp\_rce。随后三行代码涉及到python中动态模块加...