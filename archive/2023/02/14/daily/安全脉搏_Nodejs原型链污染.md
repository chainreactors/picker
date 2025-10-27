---
title: Nodejs原型链污染
url: https://www.secpulse.com/archives/195776.html
source: 安全脉搏
date: 2023-02-14
fetch_date: 2025-10-04T06:30:36.444246
---

# Nodejs原型链污染

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

# Nodejs原型链污染

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-13

11,894

## Nodejs与JavaScript和JSON

有一些人在学习JavaScript时，会分不清Nodejs和JavaScript之间的区别，如果没有node，那么我们的JavaScript代码则由浏览器中的JavaScript解析器进行解析，几乎所有的浏览器都配备了JavaScript的解析功能（最出名的就是google的v8）， 这也是为什么我们能在f12中直接执行JavaScript的原因。而Nodejs则是由这个解析器单独从浏览器中拿出来，并进行了一系列的处理，最后成为了一个可以在服务端运行JavaScript的环境。这里看到一个很好的例子，学过java的师傅应该就明白了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267509.png "null")

那么JSON又是什么呢？简单概括一下就是JavaScript的对象表示方法，它表示的是声明对象的一种格式；由于我们从前端接收到的数据基本都是字符串，因此在服务端如果要将这些字符串处理为其他格式；比如对象，就需要用到JSON了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267511.png "null")

、

## 原型对象（`prototype`）与原型连接点（`__proto__`）与原型链

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267512.png "null")

在c++或java这些面向对象的语言中，我们如果想要一个对象首先需要使用关键字class声明一个类，再使用关键字new一个对象出来；但是在JavaScript中没有class 以及类这种概念（为了简化编写JavaScript代码，ECMAScript 6后增加了`class`语法，但`class`其实只是一个语法糖） 在JavaScript有这么两种声明对象的方式，为了好理解我们先引入类的思想。

```
person=new Object()
person.firstname="John";
person.lastname="Doe";
person.age=50;
person.eyecolor="blue";

这种创建对象的方法还有另一种写法 如下
person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};

这种方法通过直接实例化构造方法Object()来创建对象
```

```
function person(firstname,lastname,age,eyecolor)  这里创建了一个“类” 但是在JavaScript中叫做构造函数或者构造器
{
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyecolor=eyecolor;
}
var myFather=new person("John","Doe",50,"blue"); 通过这个“类”实例化对象
var myMother=new person("Sally","Rally",48,"green");

这种方法先创建构造函数 再实例化构造函数 构造函数function也属于Object 如果对这里为什么属于Object而不属于Function有疑问请继续阅读 下面会解释
```

既然是通过实例化Object来创建对象或创建构造函数

在JavaScript中有两个很特殊的对象 Function() 和 Object() 它们两个既是构造函数也是对象，作为对象是不是应该有一个“类”去作为他们的模板呢？

对于Object()来说，要声明这么一个构造函数我们可以使用关键字function来创建 。（在底层 使用function创建一个函数 其实就相当于这个过程）

```
function Object()
{

}
在底层为
var Object = new Function();
```

那么对于Function自己这个对象他是怎么来的呢？如果用Function.`__proto__`和Function.prototype进行比较发现二者是全等的。所以Function创造了自己 也创造了Object 所以JavaScript中 所有函数都是对象，而对象是通过函数创建的，因此`构造函数.prototype.__proto__` 应该是Object.prototype 而不是Function.prototype Function的作用是创建而不是继承。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267513.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267514.png "null")

那么提到了`__proto__`和`prototype`我们就来说说这两个是什么东西，

首先我们要了解以下概念

* • `__proto__`是任何一个对象拥有的属性 `prototype`是任何一个函数拥有的一个属性

比如：

```
person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};
```

那么这个person对象就拥有了`person.__proto__`这个属性，而Object()我们刚才提到了是由Function创建来的一个构造函数，那么Object就天生有了Object.prototype

* • 某一对象的 `__proto__`指向它的prototype（原型对象） 也就是说如果直接访问`person.__proto__` 那么就相当于访问了Object.prototype
* • JavaScript使用prototype链实现继承机制
* • 构造函数xxx.prototype是一个对象 xxx.prototype也有自己的`__proto__`属性，并且可以继续指向它的的prototype
* • Object.prototype.proto最终指向null ，这也是所有原型链的终点
* • 从一个对象的`__proto__`不断向上指向原型对象最终指向Objecct.prototype后接着指向为Null 这一条链子就叫做原型链

有条件的师傅也可以把下面的视频合集看一下，对理解原型和原型链有很大的帮助。

4\_Function与Object的特殊性\_哔哩哔哩\_bilibili

如果我们有如下代码：

```
function Father() {
    this.first_name = 'Donald'
    this.last_name = 'Trump'
}

function Son() {
    this.first_name = 'Melania'
}

Son.prototype = new Father()

let son = new Son()
console.log(`Name: ${son.first_name} ${son.last_name}`)
```

那么按照上述说法 就有如下结构

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-16762675141.png "null")

对于对象son，在调用`son.last_name`的时候，实际上JavaScript引擎会进行如下操作：

1. 1. 在对象son中寻找last\_name
2. 2. 如果找不到，则在`son.__proto__`中寻找last\_name
3. 3. 如果仍然找不到，则继续在`son.__proto__.__proto__`中寻找last\_name
4. 4. 依次寻找，直到找到`null`结束。

## 原型链污染

举个栗子

```
// 这个对象直接实例化Object()
let foo = {bar: 1}

// foo.bar 此时为1
console.log(foo.bar)

// 修改foo的原型（即Object）
foo.__proto__.bar = 2

// 由于查找顺序的原因，foo.bar仍然是1
console.log(foo.bar)

// 此时再用Object创建一个空的zoo对象
let zoo = {}

// 查看zoo.bar
console.log(zoo.bar)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267515.png "null")

这里由于修改了`foo.__proto__.bar` ，也就是修改了Object.bar 因此在后续的实例化对象中，新的对象会继承这一属性，造成了原型链污染

在实际应用中，哪些情况下可能存在原型链能被攻击者修改的情况呢？

我们思考一下，哪些情况下我们可以设置`__proto__`的值呢？其实找找能够控制数组（对象）的“键名”的操作即可。

看下面代码 一个简单的对象clone

```
function merge(target, source) {
    for (let key in source) {
        if (key in source && key in target) {
            // 如果target与source有相同的键名 则让target的键值为source的键值
            merge(target[key], source[key])
        } else {
            target[key] = source[key]  // 如果target与source没有相通的键名 则直接在target新建键名并赋给键值
        }
    }
}
let o1 = {}
let o2 = {a: 1, "__proto__": {b: 2}}
merge(o1, o2)
console.log(o1.a, o1.b)

o3 = {}
console.log(o3.b)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-1676267516.png "null")

这里执行后发现，虽然两个对象成功clone，但是Object()并没用被污染，这是因为在创建o2时 `__proto__`是已经存在于o2中的属性了，解析器并不能将这个属性解析为键值，所以要用JSON去修改代码，（前面我们说了 JSON是JavaScript的对象表示方法 可以将字符串转换为对象） 这样就可以使`__proto__`被成功解析成键名了。

```
let o1 = {}
let o2 = JSON.parse('{"a": 1, "__proto__": {"b": 2}}')
merge(o1, o2)
console.log(o1.a, o1.b)

o3 = {}
console.log(o3.b)
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195776-16762675161.png "null")

## 漏洞复现

### [GYCTF2020]Ez\_Express

进入环境之后是一个登录页面，测试之后发现存在www.zip源码泄露 开始审计index.js

```
var express = require('express');
var router = express.Router();
const isObject = obj => obj && obj.constructor && ...