---
title: webpack下加密方法提取思路
url: https://mp.weixin.qq.com/s/wKT21GckDCsSpr1fdEjJVA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:07:44.145802
---

# webpack下加密方法提取思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboQ1SBBXwtkeFNCvHCUw7qFr793Z2NBqBpzSoD3x552ZeoIdnl622ebL7gZ1tPk8RXNhbjrUwFPIMZoic6loAPPDsricH08kbzOdc/0?wx_fmt=jpeg)

# webpack下加密方法提取思路

中铁13层打工人
中铁13层打工人

陌笙不太懂安全

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
作者:中铁13层打工人原文链接:https://forum.butian.net/index.php/share/2344
```

前言

webpack下加密方法提取思路

# webpack下加密方法提取思路

## 0x01 js中常规提取思路

### 1.1 找到加密方法位置

常见方法有：

* 搜索加解密关键字，如**encypt**,**encode**等
* 搜索被加密接口或者参数名，如**login**,**password**等
* XHR监听，搜索调用堆栈

这里通过搜索**encypt**找到了加密方法位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSMFcnCMMefKnuYYnAar7dWJgGeDRb5VlTgEKp2vfeyibSEt6jgQ8aDlPR5Q7ulcUhnb0jkYZXdHd9tt91YDAVRJBgQRssXsCJs/640?wx_fmt=png&from=appmsg)

### 1.2 提取加密方法和有关调用函数

我们将加密函数提取到本地后，还需要跟进补齐所有函数定义，比如i，n，s sm2.doEncrypt等方法提取打包下来

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTjfHqCrzMva43CDWEL8fjibKSQPJK8hiba4lZJiaZhbibfs9IQsdIG7MZHNXPJeAS66VOsryHzWku7UdfTyJKajEZk41n0YrYSz4w/640?wx_fmt=png&from=appmsg)

### 1.3.1 递进式补齐所有依赖

补齐调用函数后直接执行发现在在sm2.doEncypt()中出现u对象缺少定义，我们在该处调试进入，发现所需依赖越来越多。
webpack的代码，非常的繁多，一个webpack可能就是几万行代码。在逆向中对于webpack的加解密网站，一般是不建议去扣代码。

### 1.3.2 自实现加密方法

当前面方法难以实现时，我们可以试试阅读加密方法的加密逻辑，自己用脚本模拟实现其加密处理逻辑。
以上面方法为例：
首先该方法传入三个参数，分别是**待加密字符串t，SM2公钥，SM4密钥**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQkT5Lrq57icwB61zVJOhe0KGKaVAnCXFLTzz7yA3XrmudZibawEGtAhrjicPCMvLeibMgAiae7ibY11q9kVjQWUbKlVO4QqMib4KeEgA/640?wx_fmt=png&from=appmsg)

回到上一层，找到该方法的调用，可以看到SM4的密钥是由newGuid方法生成的

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSXbxBgV0MNr6viaeicnOlj6F1ZJvqyWEVicAfDiaJib2gqrDMo6KCoG6RQLibFYjPYvDXic3VzUC3BMFF0d93ziaX8KoFBRSrhPOGHIx8/640?wx_fmt=png&from=appmsg)

而newGuid方法其实是随机生成32位hex字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSJAGibOJKwrYH7MmYPqbPoacdvt8Bs4l6fUL049Xic9rIEo9nXe2iaPf1hNWRWsGUkr8bxe6VGXib6VX36nLqZrXobvB8fwDUACicU/640?wx_fmt=png&from=appmsg)

tips: 对于这种随机生成密钥，可以通过bp修改返回值为固定值，如将return i.join("")改成return "xxxx"，固定其值

具体分析一下加密方法过程，其处理逻辑是：首先用国密2来加密随机生成的国密4的密钥，再用国密4加密待加密的明文字符串，两个加密后的结果再加上其长度进行组合拼接后转base64，作为最终结果

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRdCGUdMicmMGboT0GzewwhtZg9tcRErfibWbrnI8rnib16DWNq0d2uUpJicicHuduqPajHicFfibl7RblhAatvUmh24AguUyYT1Mv6ic8/640?wx_fmt=png&from=appmsg)

其中的i 方法：hex字符串转数组；n 方法：返回8位字符串 t参数前面用0填充；s：方法取数组t元素的ascii码值（此处是8位长度字符串的ascii码，作用是后续数组转base64获取到数字字符）

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQg1YnRTR4JAPGUDHiaHFUA2bhibJ4DveCxyHKL8GoKV2LZ6F1xnic7oEH88nhWWexFqgUxJWKPJBnbLXeiaz8xORBFywTZQ1j5QmI/640?wx_fmt=png&from=appmsg)

我们输出加密结果也证实了我们上面的分析，我们分析完整个加密逻辑就可以自实现其加密算法，或在本例中i，n，s方法本不缺少依赖，我们只需将缺少的国密2和国密4加密算法用第三方库应用代替，成功平提原加密逻辑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQsicxia9aiauY87nHXkDhvDykQuNFNaYKN1ttFeGdFictqPlvfzp6dboTicTD3ZnXgR9bHmDnEbLHyBXo4c0QMGpAtWbG4pU4ztrRI/640?wx_fmt=png&from=appmsg)

我们发现其实上面着两种方案都比较复杂，那么在webpack模式下有没有更好的方式提取还原算法呢，答案是有的。首先我们来了解一下webpack

## 0x02 webpack基础知识

webpack是 JavaScript 应用程序的模块打包器,可以把开发中的所有资源（图片、js文件、css文件等）都看成模块，通过loader（加载器）和plugins（插件）对资源进行处理，打包成符合生产环境部署的前端资源。所有的资源都是通过JavaScript渲染出来的。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQo8W8CjeLZfDoWDWPbjA3MWtc5la7oobSE5bQ5peKvSBlw8iccOppDHr1P7G3jjfUHiam7ZmNiaUd4CT0JocyVzrML3d6FNiavhAs/640?wx_fmt=png&from=appmsg)

## 2.1 基本结构

形如

```
!function(形参){加载器;}([模块1, 模块2…])
```

定义一个自执行函数，里面实现一个加载器方法，函数传入的模块数组，数组中的每个元素都是函数，数组从0下标开始计算

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRxVlFpgOoXTd18zrBkQh3hhjf3eSARKNTyl86oAThlvgWQjZuY2ZgwHjzlF30QRk74N9mQNiaqNvu4lVueqibQeZ6jHmzWYp7sE/640?wx_fmt=png&from=appmsg)

或是：

```
!function(形参){加载器;}({'模块名1':模块1, '模块名2':模块2…})
```

传入一个字典，元素都为函数对象，通过字符串调用对应模块

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSTvhORxDELDcDlaXsAc9GxNu9vrrQgYdtVbqCJfzAKT3Kn7svEM8bdFDo3KoKCnFOsktBBZm5pK1KzsBONGLcLntFC5znc9fo/640?wx_fmt=png&from=appmsg)

当模块比较多，就会将模块打包成JS文件
形如：

```
(window.webpackJsonp = window.webpackJsonp || []).push([[模块ID], {函数对象}, [n, e, t]]);
```

定义一个全局变量 window["webpackJsonp"] = []，它的作用是存储需要动态导入的模块，然后重写 window["webpackJsonp"] 数组的 push() 方法，window["webpackJsonp"].push() 其实执行的是 webpackJsonpCallback();
window["webpackJsonp"].push()接收三个参数,第一个参数是模块的ID,第二个参数是 一个数组或者对象,里面定义大量的函数,第三个参数是要调用的函数(可选)，一般是入口js会传入这个参数来指定首先加载的模块。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBfxiaUFTe6ybdibSwpKDv7tam2h6Gs8YQLbWKO8evmyItH9faO9w8byIOAXupdiarU1ibymGlGxMTo8lX5ubjsDRLHcaV7AxFvws/640?wx_fmt=png&from=appmsg)

## 2.2 加载器基础知识

介绍完webpack基本结构，我们来看看加载器做了什么工作

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRfqFN9r5dGVzs4Ropc6KT2SGL26eR7Z4w5cZSiaUxmssebW9mXIa10fWWxPic7hnUJJmLWzXWBE1oWQLFhgwYBOXSic1RM09r38k/640?wx_fmt=png&from=appmsg)

加载器处理逻辑：

1. 判断模块是否有缓存，
   如果有则返回缓存模块的 export 对象，即 module.exports。
2. 新建一个模块 module，并放入缓存。
3. 执行文件路径对应的模块函数。
4. 将这个新建的模块标识为已加载。
5. 执行完模块后，返回该模块的 exports 对象。

**加载器其实就相当于是python中的import**

### 2.3 webpack识别方法

1、多模块打包webapackJsonp特征

```
(window.webpackJsonp = window.webpackJsonp || []).push([[0], []]);
```

2、加载器实现特征

```
!function(){
functionxx(n){
return x[n].call(**.exports, ***, ***.exports, xx)
    }
}();
```

3、页面有`app.版本号.js`，`chunk-libs.版本号.js`等js文件就能大概猜到是使用了 webpack 打包

## 0x03 Webpack提取加密方法思路

Webpack提取加密方法通用思路主要是：

1. 定位加密方法
2. 找到模块引用，提取加载器方法
3. 提取加密实现模块和引用模块文件
4. 调用加密模块，执行输出

### 3.1 定位加密方法

通过搜索接口名和加密字段找到加密方法

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTG84NdnNxPEcIGjzNLPa3Pmc0fIgA3ntGppZvthNrMxryO6mgv8LSDhhju5crxwRZwzicHk8ePlsicDH4MhY6PsKia7CXtF92t9U/640?wx_fmt=png&from=appmsg)

### 3.2 提取加载器方法

我们向上看到形如n(字符串)的调用，这种形式一般来说就是利用加载器进行模块引用，我们断点进入

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRYnVzAILOmFLpGiaOfH1oQCXE9fNdEcDoicWtPk6mlHKd4n20Wj6RhOFCel1oqW6e8N2Lqo7MILQuU5S4Ivrc8fiaWgDSp3P2zYY/640?wx_fmt=png&from=appmsg)

断点跟进，发现其在index中,看到加载器特征

```
return c[n].call(u.exports,u,u.exports,d),u.l=!0,u.exports;
```

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQHbicf7LMylQMlXND57qjZED9rFV9uBAW9Dk88icb9icT7mTvoHS0yn8faZHibgjtfQ4MvoI0A9nEEKxibibm1f1UKKDjCibWpxDG9wI/640?wx_fmt=png&from=appmsg)

我们把script标签中的js代码全部提取出来,d函数即是加载器函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRuFtMDQX6bMiby3mxbrib5hPG8gfn3EcPFkfXiawpsMqSe5VzZEuJYjQ0ibuUMiatuOHngiaSDCYLQt44R8X979Z9SB6Lw6ibW0AKvuM/640?wx_fmt=png&from=appmsg)

直接执行提示缺少window对象，这是因为window表示浏览器打开的窗口，在客户端JavaScript中window对象是全局的对象，所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员。但在nodejs中直接调用window是不存在的，而代替的是globa;
于是定义全局变量var window = global;解决报错问题

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQPqJnDXJTctOARG0qLIQQgUlteH49TSbbfsH7PzE0Jd6cSZ8Z289Ieu95iav94TlaMUwYiaibbnBlpsa4Hd9xhQk7JtuZgnIVyJo/640?wx_fmt=png&from=appmsg)

### 3.3 提取加密实现模块

提取到加载器方法后，我们还需要找的加密算法实现模块，这里有个技巧，我们前面知道加载器会传入所以模块的数组，我们断点进入提取加载器方法后，控制台可以直接输出模块数组

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTphhRgM3gp3mWZpmRBmTiaEH8HXq77BicsYQzE5h1t3iamdvTbK1vn0gScJJJrhPzleHyoNuY9KArVavmHfHParOrwQxVzkVI6oA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTB8LY7tZKlvb48om8qWTgTfEibYG0KTFamcVb8fTia6LRcwib8bvrHxAyUkibzF1B7oHBibrb1KT6zgvl9wKg202c80trDDrwp7GdE/640?wx_fmt=png&from=appmsg)

前面我们知道加密方法来自“MuMZ”模块，我们利用模块数组直接在控制台打印进入“MuMZ”模块

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQe0qYaflznlflhPJedPdcA8Qibkc1wb9rn3rQ3hU4LibsMUjA2FibrdX5gRG5SXiaj36F6PCZBrOYDvOdhHWFdScudWCQ5UfULF6o/640?wx_fmt=png&from=appmsg)

复制提取加密模块到本地，直接调用发现缺少了"xbrz"模块的定义

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQX6Ghiap5fJKU4UdFAtxxCfz2ibwUF2bgwicQkibhs1yycHf5StPy1VrwTAQhsPHtNALicfb8KkDb0rTp4sGc7xt5ZJK6xr3DQ75XA/640?wx_fmt=png&from=appmsg)

为了方便，可以把"xbrz"模块所在文件整个复制到本地，利用require进行引用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboT66IicNfUrX3PUNXjrSvvPpxRxqs763CAiaJJmU4Np6ANDnsCkaPz6D0aJcgIl8kJ6fDOIvyp9hVlaTK4PSfGfsE5xE36vkbeng/640?wx_fmt=png&from=appmsg)

### 3.4 调用加密模块执行输出

补齐所有代码后，因为!function是立即执行的函数，为了灵活调用和返回值，定义变量导出加载器方法，调用加密模块，返回加密函数结果

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTI5xSyTt1HPr3r0ia3tw8ZGJqG74mDmaKPNHjhUvP3PCPkgrGNSc3gd11bmkjdV0v1KAe8D48N29jd39TSlFRn1R9DqB3L5bCk/640?wx_fmt=png&from=appmsg)

## 0x04 总结

对比三种提取思路，利用webpack的结构特性进行脚本构造其过程较其他两者更简单，只需要复制加载器和加密模块代码，引用...