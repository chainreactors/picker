---
title: V8 torque函数PromiseAllResolveElementClosure 相关的issue和POC的探索
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563554&idx=1&sn=cf5419ad49285034ace2d1512bd65162&chksm=b18d836886fa0a7e63e222f572dc596580d1d91e05735516b5a02370c78ea295f2ffb56db249&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-13
fetch_date: 2025-10-06T17:43:05.477089
---

# V8 torque函数PromiseAllResolveElementClosure 相关的issue和POC的探索

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6v02R45MosLaOltFibMfAQUbpRSNQticwsxXjT8TBTohmibxIVpapxLK0oQ/0?wx_fmt=jpeg)

# V8 torque函数PromiseAllResolveElementClosure 相关的issue和POC的探索

苏啊树

看雪学苑

```
一

写在前面
```

最近无意刷到看到一篇v8CTF的文章，原本想看一下学习下v8沙箱绕过的姿势，看了作者的slides却是第一时间被作者圈起来的这个PromiseAllResolveElementClosure builtin函数所吸引，查了下是v8处理Promise对象相关的torque函数。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6vHftT6XNpskRSN2VQWZH5WcgkcxoFEWp4HomQZDJnBK0UQQ3CicwZxnQ/640?wx_fmt=other&from=appmsg)

图   1.1

原slide

https://kaist-hacking.github.io/pubs/2024/lee:v8-ctf-slides.pdf

印象中在以往的漏洞报告上看到这个builtin的次数不少，随手google查了下就看到搜索记录显示：

◆CVE-2020-6537

◆chrome issue 40068417

还有这个CTF slide所用的：

◆CVE-2023-6702

都和这个PromiseAllResolveElementClosure有关联。

由于之前对这一几个问题都没有仔细的分析过，这次索性一起调试一遍，顺便尝试通过CVE-2023-6702的POC构造出issue 40068417和CVE-2023-6702的POC。

```
二

CVE-2023-6702
```

故事的源头从一个补丁开始：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6vmRkGdZjftrBqpwXoBYR9ZXVia8iclVxE9TlLxzBFR6ZibEOwLyXOBHMTg/640?wx_fmt=other&from=appmsg)

图 2.1

## **2.1：补丁分析**

如图2.1绿字的补丁注释，大意是说在闭包指向NativeContext作为marker调用之后，我们不能再访问reject element context。补丁修在了CaptureAsyncStackTrace函数。

同时2.1图上还有红字，提示是在Promise.all()函数调用时发生的。

根据查阅资料能得知CaptureAsyncStackTrace就是捕获Async函数调用的异常堆栈，发生在Async函数出现错误的时候，捕获到异常后能够访问到其堆栈的情况，这个函数就是v8对这个JS情景的处理。

作者构造的POC：

```
var closure;
    function Constructor(executor){//1：按照ECMAScript标准创建Promise构造器
        executor(v=>v,e=>e);
    }
    Constructor.resolve=function(v){//2：定义构造器resolve方法，这里只是简单的return参数。
       return v;
    }
    let p1={//3：创建参数对象，对象内的then方法将onFul内部对象传递给closure
        then(onFul,obRej){
            closure=onFul;
            closure(1);//4：将closure赋值为onFul对象，然后对closure闭包调用，也就是到达补丁注释的情况。
         }
     };
     async function foo(){
     await Promise.all.call(Constructor,[p1]);//5：将构造器和构造好的p1对象传入到Promise.all.call，为了确保closure能够调用完成，这里用了await等待调用结束。
     await bar(1);
    }
    async function bar(x){
         await x;
         throw new Error();//6抛出异常，让之后的catch能够捕获到异常，然后访问错误堆栈。
    }
    foo().then(a).catch(e=>console.log(e.stack))//7：接收异常，访问异常e的堆栈e.stack，触发漏洞。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6vIXwD4dpCPtbcAsIic6P1O5PGSiaSEoHx38QAucOx6afmdQtWQfr2ugmQ/640?wx_fmt=other&from=appmsg)

图  2.1

##

## **2.2：崩溃分析**

◆作者使用了一个和ECMAScript标准上Promise相同的构造函数写了一个构造器Constructor，然后重写了该注册器Constructor的resolve方法，resolve方法只是简单的把接收到的对象返回。

◆创建了一个对象p1，在p1里重写了then方法，在then方法里用闭包变量closure获取v8内部的fullfill对象(onFul)，然后把闭包变量Closure作为函数进行调用。

◆创建一个async函数，将p1对象作为Promise.all.call的参数，并且调用Promise.all.call函数，然后使用await确保Promise.all.call调用中p1重写的then，完成闭包变量Closure解惑v8内部的fullfill对象，并且当成函数进行完成，并且随后抛出一个异常。结果在抛出的异常的堆栈的访问的时候，意外的能访问到内置fulfill(onFul)对象使用的NativeContext，造成数据结构的混淆，触发了v8 Debug版本下的Assert。

## **2.3：原因小结**

◆onFul对象使用的是v8内部的builtin对象，然后使用的context为NativeContext。

◆使用onFul这个内部对象作为函数调用的时候，v8内部会调用PromiseAllResolveElementClosure这个builtin函数。

◆而在CaptureAsyncStackTrackt这个函数中的处理中，原本期待处理的数据结构为当前JS所处的GlobalContext，然而漏洞版本的v8却意外的使用了原本不应该访问的内置的builtinPromiseAllResolveElementClosure所使用的NativeContext，造成了数据结构混淆使用，引起了内存破坏。

```
三

从CVE-2023-6702到CVE-2020-6537
```

##

## **3.1：CVE-2020-6537 POC构造**

从2023年的POC倒推2020年的POC，现实工作和学习肯定不会有这种需求，听起来非常的无厘头。但是最近漏洞研究经历让我感觉，很多时候找漏洞只是在不同的地方反反复复的找相似而又遗漏掉的情况，前人会找到这个东西作为研究，肯定是这个点地方集合了很多要素，有鸡有篮球，有中分也有背带裤，你如果能发现新的要素就又可以玩之前的烂梗。大部分问题的发现不用需要覆盖得多么全面，对原本问题的理解更深更细致好像现实漏洞研究中更为重要。多做一些尝试能理解到的点就会多起来，由于我先看到的是这个v8CTF的paper，之前也从没看过CVE-2020-6537的POC，就想着尝试一下由这个paper作者构造的POC和之前本人知识的基础上，能否构造出CVE-2020-6537的POC。

### **3.1.1：CVE-2020-6537 bug Issue分析**

看CVE-2020-6537的bug issue里面的这段描述，

https://issues.chromium.org/issues/40052834

In function `PromiseAllResolveElementClosure`, it will read {remainingElementsCount} from {context}'s slot firstly, subtract 1, and save it back to {context}. {remainingElementsCount} represents the number of pending promise and when it becomes to zero, the function will return an array of objects that each describes the outcome of each promise.

根据上述的issue描述，貌似这个漏洞和remainingElementCount这个变量有非常大的关系。将v8切换到漏洞版本的commit以后，利用关键字搜索一下v8源码，发现这个变量remainingElementCount出现在PerformPromiseAll和PromiseAllResolveElementClosure这两个torque函数里面，表示的是一种计数。

这里对这两个torque函数打了补丁，Print出remainingElementCount的的计数。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6v86ZMNUw4ntoxGIiasuYDuo37x2SiaB0rgoYD2KpNGPyxxiaaZLryOX9SQ/640?wx_fmt=other&from=appmsg)

图 3.1.1

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6vTo0ianqjDMAw0atXa8yC4KnPXS3qg25DBPqfDFohuTrfzyicuiavbTnxg/640?wx_fmt=other&from=appmsg)

图 3.1.2

如图3.1.1，3.1.2，所示的位置打上补丁后，重新编译v8，将v8CTF的POC简单的修改为以下POC：

```
function Constructor(executor)
 {
   executor(v=>v,e=>e);
 }
 Constructor.resolve=function(v){
   return v;
 }
 let p1={
   then(onFul,onRej){
       onFul();
   }
 }
 async funcrion foo()
 {
    await Promise.all.call(Constructor,[p1]);
 }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYXjic4EichcVGNsHQxXqO6vkUoFgrRC5sn5CVT9moicphUuv7AJfmoU4SbXZxm43t53OyGCTqXI7dA/640?wx_fmt=other&from=appmsg)

图 3.1.3

###

### **3.1.2 ：控制台输出分析**

如图3.1.3所示，成功进入PerformPromiseAll和PromiseAllResolveElementClosure这两个torque函数，并且使用了这个计数变量remainingElementCount。通过控制台的输出信息我们可以推测：

v8执行这个POC的时候，调用了PerformPromiseAll这个torque函数，增加了一次remainingElementCount，然后调用了PromiseAllResolveElementClosure，减少了一次remainingElementCount变量是平衡的，这里如果把onFul注释掉再运行POC，v8是不会使用PerformPromiseAll和PromiseAllResolveElementClosure这两个torque函数，那么这里我们可以得出PerformPromiseAll和PromiseAllResolveElementClosure这两个torque函数和onFul(fullfill)对象作为函数调用的情况有关，那么和onRej(reject)对象作为函数使用的时候有没有关系呢，现在并不能知道。

根据另一段漏洞描述：

Normally, either `resolveElementFun` or `rejectElementFun` should only be called once at most, which means turning a pending promise to fulfilled or rejected state. However, user can get `resolveElementFun` and `rejectElementFun` through some user defined js functions. Once both of them are called, {remainingElementsCount} will be substracted twice but only one promise has been processed. So the result of Promise.allSettled will be returned to user in advance. An attacker may use this vulnerability to cause type confusion, and achieve arbitrary code execution.

通常情况下`resolveElementFun` 和 `rejectElementFun情况是只调用1个，然后在用户JS劫持的情况下可以调用2次，稍微对JS Promise有过了解的都知道Promise返回的时候有resolve和reject 2种情况，全部成功的时候执行resolve回调，有错误的时候执行reject回调，只会出现resolve和reject其中1个回调调用的情况。`

`这里却说在用户JS劫持后能实现同时调用了resolveElementFun 和 rejectElementFun两个函数的情况，这里我的理解就是调用了2次PromiseAllResolveElementClosure这个torque函数，导致导致出现安全问题，但具体的怎么出现所谓的resolveElementFun 和 rejectElementFun两个函数调用的情况呢，还不得而知。`

##

## **3.2：分析总结：**

目前能知道按照v8CTF slide给我们的信息，如果重写了then方法，并且将其中内置的onFul对象当成函数调用，就会进入PromiseAllResolveElementClosure这个builtin，通过输出日志，我们能看到可以走到PerformPromiseAll这个torque，并且会把remainingElementCount这个计数+1，同时接下来会走到PromiseAllResolveElementClosure这个torque，然后把remainingElementCount这个计数-1，变量remainingElementCount的数字是平衡的。

## **3.3：如何让remainingElementCount计数出现错误**

◆第一种尝试，如果截获onFull后，重复调用onFul()，会不会出现减两次remainingElementCount变量的情况呢，结果通过打印显示，只对remainingElementCount计数改变了一次。也就是说即使拦截了onFul然后多次onFul调用，也只是调用了一次PromiseAllResolveElementClosure这个torque函数。

◆第二种尝试，分别重写onFul和onRej，然后调用onFul和onReg，但是结果还是只调用了一次PromiseAllResolveElementClosure这个torque函数。

仔细的研究了下Promise和then的资料，发现ECMAScript标准下规定then接管以后，无论调用onFul和onRej这情况本质都是相同的，简单来说，结果有两种情况：

第一种情况是全部处理正确，这时候由内部的resolve，也就是这里的onFul回调处理。

第二种是出现了错误，返回第一个错误，交给内部的reject，也就是这里的onRej处理。这样的话在返回then的时候同时调用onFul,onRej是不会成功的，因为这两个对象在这个时候，只有其中一个在ECMAScript标准下是有意义的。

##

## **3.4：修改构造器resolve方法**

通过一段时间对标准的研究和尝试，我发现如果我们通过直接重写注册器Constructor的resolve方法，在这个注册器的resolve方法中获得对象的then方法，就能第一时间接管到onFul和onRej(resolve和reject)对象，这个时候其实v8还没有对结果进行判断，所以onFul和onRej都还是”有意义的“的对象，如果是在这时候劫持那很就能直接调用onFul()和onRej()，这样就能可能触发两次对PerformPromiseAll和PromiseAllResolveElementClosure torque函数的调用，将remainingElementCount减1两次。

把POC改为：

```
function Constructor(executor)
 {
   executor(v=>{console.log('haha')},e=>console.log('hehe'));
 }
 Constructor.resolve=function(){
   then(onFul,onRej){
       onFul();
       onR...