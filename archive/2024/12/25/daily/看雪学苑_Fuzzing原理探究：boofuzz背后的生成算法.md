---
title: Fuzzing原理探究：boofuzz背后的生成算法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587741&idx=1&sn=0b451de82671954d27622c11080a1879&chksm=b18c22d786fbabc17eb157aff259d4b3ce71ca71ad3b5c49af79713d62a8e162782dd69f36e9&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-25
fetch_date: 2025-10-06T19:38:32.313476
---

# Fuzzing原理探究：boofuzz背后的生成算法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicDRLt2Xs2zKswyibh5Ahaic3gveUf6wDxSdickY6D3mk9WMF7FTvxLl0kA/0?wx_fmt=jpeg)

# Fuzzing原理探究：boofuzz背后的生成算法

是气球呀

看雪学苑

来看看基于生成的boofuzz吧，虽然后面实现了持续生成的方案，但没有任何反馈调整变异机制，所以其实还是基于生成的。

> 基于生成和基于变异的模糊测试区别在于，基于生成的方法一次性生成所有样例，在生成初始输入后不会根据输入继续变动，实现起来很简单，无需插桩等；
>
> 而基于变异的方法则会一直运行，根据现有结果，不断地修改已有输入，可以说基于变异的模糊测试更为灵活和有效。

#

# boofuzz目前的大致架构

本文基于boofuzz 0.4.2代码进行其变异算法的分析，为了对比前篇afl、afl++的变异算法的优异，暂且不关注boofuzz的网络请求、线程调度之类的代码，重点还是怎么生成、变异、靠什么引导的。即下图蓝框包含部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicfJH59zUL7afGGJMhkXDDjzMFwuFZTMrOKSRoqgE5Vw7T05AXkzoMPA/640?wx_fmt=jpeg&from=appmsg)

#

# 直观感受：boofuzz脚本案例

首先直观感受一下boofuzz是怎么回事，来看一个简单的boofuzz脚本的一部分，比如想要fuzz这个数据包的特殊字段：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicnqRMNXzPdtsNxaG1xhKtFsGxwEyFSK880pf9XAoI7wenUy9Uia5q5Eg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicGaVhlPxG2lXBJ6gg3MXl5WDHmDN6pejuicn0ssN0BFJpkfERULNGoqw/640?wx_fmt=jpeg&from=appmsg)

直观地看有什么感受？会觉得以上的代码其实就是把一个数据包请求拆出来好多块了，然后除去static静态值部分，实现了对SESSION\_ID、uid的fuzz。而且大多数的地方都是static的，表示在测试样例的生成过程中照搬就好，不会进行改动。

那么，s\_string发生了什么？还有什么类似的生成方式？接下来尝试跟着用户手册和实现代码看看。

测试样例的生成分为以下几种，实现代码位于boofuzz/primitives下。

在这里要引入一个概念——boofuzz原语。诸如上面示例的s\_string、s\_byte、s\_dword、s\_static等，其实就是boofuzz的原语。查看其中的实现，就可以知道boofuzz是怎么对数据进行生成的。

# python前置知识

python真的好灵活啊omg，好多“语法糖”，来尝一下吧。需要了解一下python迭代器、生成器以及装饰器的知识，因为boofuzz的代码实现用到了。

关于python迭代器、生成器、装饰器可以看这篇总结，比较详细
*https://stonewiki.su-cvestone.cn/zh/program/basement/pyhon#%E8%BF%AD%E4%BB%A3%E5%99%A8*

## 迭代器(Iterator)

Iterator(迭代器)对象是一个数据流，这一概念需要与list区分开，它们的区别有：
Iterator对象可以被不断使用next()函数进行下一个数据的返回，且只有当下一个数据被请求时才会进行计算，故与list相比，其具备“惰性”。

但是Iterator对象理论上可以无限返回下一个数值，而list显然不可以，当然，如果Iterator没有数据时，会抛出StopIteration错误。

一个简单的案例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicD0JVGiaia4rEXIvczLvjrCdFI4ekqdNlIbzRWXdGfFdRsTxpy272T41g/640?wx_fmt=jpeg&from=appmsg)

预先定义了一个Iterator对象，然后在循环中不断调用next获取下一个值，达到迭代1,2,3,4,5的效果。

总的来说，迭代器仅仅只能通过next来导出下一个值。

## 生成器(Generator)

创建一个简单的生成器，仅需将列表的[]包裹方式，改为()包裹方式即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HiccqsaiaDC8z1pdsMtOQb2S4Uq3QpO9UqicmOmcQ4FukpiaXVYzNaV1ZeQw/640?wx_fmt=jpeg&from=appmsg)

然后，就可以通过for循环的方式读取里面的值。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hichda2AZxH7Akn13FnyDqTm3bibmmTqZc6cFkzaGYuNBT72dl5Rgm7syA/640?wx_fmt=jpeg&from=appmsg)

但是，更常用的生成器写法是，使用yield(中文是生成的意思)自动使用生成器来返回值，比如斐波那契数列的计算中，我们可以使用yield来进行返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hic3dKicYYKnHeascZjeXZX1Iyulk8fsYHhkuDajmoW3QLiacxBrxtZTk6g/640?wx_fmt=jpeg&from=appmsg)

与迭代器相比，生成器属于是迭代器的容易使用的版本，故有跟迭代器完全相同的用法，可以使用next()导出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicXxfzPfibwBecjXd8rhOme9z7cy1hXNFHJ7oSWxoD8MTyTme7DEkOQdA/640?wx_fmt=jpeg&from=appmsg)

但是这一点都不简洁，更为常用的是下面这一种方法：使用时仅需使用for循环，把fib(6)返回的，generator对象里的值逐一导出，这种写法比迭代器的写法简洁好多。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicOXsqf0k6dvvqqzG1uwFKRiapqffQDvdxr97mdUeiaH6krvz0oRJX0MrQ/640?wx_fmt=jpeg&from=appmsg)

此处注意：yield和return同样会返回值，但请注意它们的行为不同！

yield：返回当前值，记录停止执行的位置、状态，下次继续从上次返回值时的状态开始执行。

return：返回当前值，下次执行时一切都重新开始了。

## 装饰器(Decorator)

装饰器，简单来说就是，在不修改被装饰器的前提下，实现对其功能的增强。

首先，需要定义一个以函数为参数，并最终返回该函数及其参数，其中，wrapper类似于一个中间层的概念，输入的是该函数及其参数，返回的也是该函数及其参数，如以下示例。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicqcBRWHibWfnXhR012PibZSZA3ug8chuuibslRYYDcLLhqfQz8lBj0aPAA/640?wx_fmt=jpeg&from=appmsg)

然后使用这一装饰器"log"，去"装饰"now方法，now方法本身不会有call与func.\_\_name\_\_等字样，仅仅会输出日期。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicibFX8Ju5S06YiaickzDf1e7e1w6qNZWEqqmRVAme7dO9Z3ljSV5blqrcA/640?wx_fmt=jpeg&from=appmsg)

此时如果调用call：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicS37HzfqLXia16raCSTfZhW5fs3ib9mQHHg7g7ObcAkELicicKOd2lqhicZw/640?wx_fmt=jpeg&from=appmsg)

会发现now()不仅输出了日期，还输出了call与func.\_\_name\_\_等字样，这样就使用log完成了对now的装饰，了解到这一步就ok。

然而，实际上由于具体实现的原因，装饰器装饰后的函数本质上是另外一个全新的函数了。

为了消除其负面影响，boofuzz使用了wraps模块，其确保被装饰的函数保留原始函数的各属性。

来看一个案例：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HiciaWzAWxiccNfiaDSRXXibECNzQO43xQIHHH9Pzibia3nfLwYkEhyRJX3Krhg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicxWeoWbVibm34ckghHTa66YG2t785b9eOpoGvMg59cy6iaFgQDoic0x2cQ/640?wx_fmt=jpeg&from=appmsg)

#

# 如何进行持续变异：MutationContext与协议树

曾经有人提过issue说能不能进行持续的fuzzing，https://github.com/jtpereyda/boofuzz/issues/328，以实现fuzzing一直跑而不是生成以后达到最大测试次数就停止了，于是在第499次pull的时候https://github.com/jtpereyda/boofuzz/pull/499。

其引入了持续的无引导变异fuzzing，而非先前一次性的基于生成fuzzing
查看对应补丁发现。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicjCPuqQI3wVeLPGbOUFLVia1FjUOgib8P3SgdmD1jnQWOlntvtuicjfdLA/640?wx_fmt=jpeg&from=appmsg)

在这个补丁https://github.com/jtpereyda/boofuzz/commit/71f69bf829f98114100d3c7815caa5e827980d1a

中加入了是否进行组合fuzz的判断值，如果是，则最大深度为none，否则1。

然后在session类的fuzz方法里，看到了其被应用：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicNIM6FsJcia2khEicnpWGx7tx9GnaLLbFpoDeQOEHOPukfiaKfrdEewAVA/640?wx_fmt=jpeg&from=appmsg)

查看sessions

/session.py的fuzz方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hic2NDKJkaNTicoonf4b5ic4yVokOAunYpB8LRfzdEXAF64G6q62uddQTPQ/640?wx_fmt=jpeg&from=appmsg)

跟进\_generate\_mutations\_indefinitely，发现有个or的循环条件，这里正是决定了无限突变的判断。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicNhXFvicoURktbWMwoes0ibk9uhGVUJicgO73dAJRXQe6zqLagIdmmIPNA/640?wx_fmt=jpeg&from=appmsg)

要了解接下来boofuzz是怎么进行无限变异，首先来了解一下协议树，比如以下就是协议树，其中，request的方式和路径，与响应的状态码，是这一棵简单协议树的两个节点，这两个节点到根节点，就是两条路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicldUTqtsODPuyOaILsiaek1eFXIiam85UFP3rNjvV0a4ibexlH9HZEw1dw/640?wx_fmt=jpeg&from=appmsg)

\_generate\_n\_mutations即核心的反复生成变异算法，其会基于以上协议树对每个节点之下的内容进行变异并发现新的路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicNfHrbHZiaO9U2h91g57lXcY0PxGzC8aoAj8l0ZibDQOSDRW1ibUfzXiaHg/640?wx_fmt=jpeg&from=appmsg)

首先，在boofuzz v0.4.2上会将初始节点id和末尾节点id作为边(edge)的识别符号。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicNwTMkRA6ZNvrpV61xB4xz4enaqXZdL34pvSjoHKtPAxqEYdO2q8jcw/640?wx_fmt=jpeg&from=appmsg)

\_iterate\_protocol\_message\_paths

然后将边逐一加入到路径(path)里。框架通过 \_iterate\_protocol\_message\_paths 方法遍历某个节点下(this\_node)所有消息路径，每个路径由多个节点组成，每个节点又有各自的id以供识别。于是就迭代完整个协议树了，生成了很多条路径。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicqB3XcibohFJ980icYCyfFpLBjX8Rd0THl0gpUrbynacAHaWY4T9glxCQ/640?wx_fmt=jpeg&from=appmsg)

当然还有一个\_iterate\_protocol\_message\_paths\_recursive ，其实功能大同小异，就是反复地递归调用自己，由\_iterate\_protocol\_message\_paths在path为空的情况下调用起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicUicPjCqEonjZlWFDBfC12UicQuup41s6Rtlhr6rGVenvCpibM4tBcGb5g/640?wx_fmt=jpeg&from=appmsg)

\_generate\_n\_mutations\_for\_path在每个路径上，框架通过 \_generate\_n\_mutations\_for\_path 方法为路径上的每个节点生成突变。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicAQHthe94ANbgVLDO4HMpgV8LuTmtMCWhYJaHWGHLyddVpVHNbTEvFw/640?wx_fmt=jpeg&from=appmsg)

到这里看出来了。这个看起来是boofuzz从sulley上继承的方式。

当然也有一个\_generate\_n\_mutations\_for\_path\_recursive ，其实功能大同小异，就是反复地递归调用自己，\_generate\_n\_mutations\_for\_path在path为空的情况下调用起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47HicgricLc7dv26Jrmdn3TgBkKkTETqrXkbrE3wsUQHTPHCuI3QnpxtNZqw/640?wx_fmt=jpeg&from=appmsg)

从此，其自根节点自上而下，完成了对每一个不同的情况（对应不同的树形）不重复的变异，就这样直到爬完整棵树的每一种情况为止，当然其情况空间非常巨大。

# 从boofuzz原语看生成算法

简单来说，每个原语主要是有mutation和encode步骤，据说这是为了将来实现覆盖率引导反馈和多重的变异，所以在v0.3.0明确地分开了原来同属与mutate的职能。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Gibqj6bU5uB7PiaBMHyL47Hict2ibhW2v7uCAsWh4AKD9YSib4HXuNeIXBWZTuZ2GSCxAyTiap9f6YPHaA/640?wx_fmt=jpeg&from=appmsg)

无论什么原语，最终引向的父类会是，Fuzzable类，从中...