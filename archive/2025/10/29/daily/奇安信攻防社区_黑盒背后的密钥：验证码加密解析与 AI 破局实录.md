---
title: 黑盒背后的密钥：验证码加密解析与 AI 破局实录
url: https://forum.butian.net/share/4613
source: 奇安信攻防社区
date: 2025-10-29
fetch_date: 2025-10-30T03:10:57.702836
---

# 黑盒背后的密钥：验证码加密解析与 AI 破局实录

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 黑盒背后的密钥：验证码加密解析与 AI 破局实录

* [移动安全](https://forum.butian.net/topic/50)

一个平常不过的app加密竟然如此难搞？一开始不断受阻，不过最后也是破局并且复盘，而且又研究了AI利用的新思路，一键出结果，非常强的可实用性

黑盒背后的密钥：验证码加密解析与 AI 破局实录
========================
0x01 条条大路"不"通罗马
---------------
测试APP的时候发现验证码是4位的，立即就想APP是否存在防爆破机制，如果没有的话4位验证码很容易就爆破出来了
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-759132fec1c2dcde69afbb37d1af23803035cca0.png)
抓包看看，一看人麻了，多么熟悉的Nonce，sign等参数，想着肯定又存在Sign校验了，又得扣加密逻辑好烦
但是不知怎么的可能是懒，胡乱改了改参数和请求头的一些值，发现后端并没有校验，感情你在这跟我玩`虚张声势`呢
不过虽然sign校验是不存在，但是参数的加密，肉眼可见肯定是存在的，不过再开始逆向扣算法之前，为了防止做无用功，所以直接将这个包重发了100次，观察响应体并没有出现`速率限制`、`验证码重置`相关的信息，看来很可能不存在防止爆破限制，还有的搞
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-b311ef8eea11047820e9539206bcabe5c62aa094.png)
于是直接将APP拿去`脱壳`（脱壳这里先不讲，后续想着专门写一篇详细讲讲，目前网上也有非常多优秀文章大家可以学习学习），直接拖进`jadx`，全局搜索接口关键字定位到了，看到它有两个参数，第一个是map，第二个就是一个不知道干嘛用的参数，上图抓包里面也可以看到那个值是空的， 所以这里可以知道其余的值`phone`、`captcha`、`action`都放在了第一个参数map里面
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-4aac795da915e7f1cbb363caaeebeb1813f557e4.png)
按`X`查看函数被谁调用，下图可以清晰的看到参数全部放到了`map`里面，其中验证码的值是将`str2`利用AESutil类里面的m49295b函数处理后放里的，所以这里基本上定位到了加密函数，接着点进`m49295b`
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-60c2a4fe916c28c28c4e8399924ff04ab8cdff2a.png)
嗯呢挺好挺容易，这么快在上面就看到了`key`和`偏移`
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-17883f932bf1895c6ca6f0c4736cf96e27483886.png)
不是这两个值完全不一样啊，怎么回事，难不成不是，这个期间我又回看了很多代码，然后尝试了很多次发现还是一直对不上，浪费了很长时间，栓Q了
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-666d008715651e331cb2e6cee692a962727d178a.png)
差点忘了，我还有神器呢，干嘛新新苦苦手动逆向呢，直接打开算法助手，勾选对应APP，然后将加密打开
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-91cb38fde5f66a2c5a3f6115f55e4dd5a0ebbfc9.png)
重新触发一下对应的功能点，我输入的验证码是6666，搜一下，搜出来很多，但是很明显都不是啊？什么情况这是
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-6256ac16b19ffc5407e0b5ef3dbd20211f35e162.png)
没办法了，用frida hook一下吧，我hook的是下面这个函数，然后直接利用`jadx`的功能一键将frida代码拷贝了过来
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-4fcb220581f51a82abe056c28ae0873fa650272f.png)
放到frida的hook框架代码里面
```js
function hookTest1(){
//放到了这里
}
function main(){
Java.perform(function(){
hookTest1();
});}
setImmediate(main);
```
发现hook到了， 但是参数因为是个枚举类型，所以具体的值不可以见，但是这里其实可以很明确，确实传参就是我们看到的那两个
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-cde7f49a96be71775507bc1f55b899d0e140b8ce.png)
为了进一步证明，于是我这时尝试hook这个`mo50430b`这个函数，还是直接右键复制为`frida`片段
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-0fcf7b4a3b36d990bafe09f24bdb6b6ec49db515.png)
重新触发发现hook不到，人麻了，不是哥们服了啊
0x02 发现问题
---------
这个时候就很无语了，说实话这个东西本来以为很简单，轻车熟路了，没想到浪费了这么久，于是想着细心点，这回细看看，当我仔细看了下面这代码时候茅塞顿开
AESUtil里面调用的加密的函数，我跟进去发现到了`AbsAesAlgorithm`不过这个时候发现它是个抽象函数，没有函数体
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-de3bcb000bec481e500fe7efae2e939d2b2c8e1f.png)
那么也就说真正代码执行不在这里，我们回过来继续看，这里是`f65543a`调用的加密函数，而这个对象哪来的呢，看上面发现一个明显的多态定义，这里真正new的是一个`AesV2Util`，而那个抽象函数所在的`Absxxx`是它的父类而已，所以我们真正要找的是`AesV2Util`
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-b13384dce0b0d3c973187504c15cac2f6ecfce85.png)
代码如下，上面部分大概就是检查缓存判断是否已经创建过加密对象，如果没创建过那就走到`L23`创建一个新的加密对象
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-3e316c348013dcbeb31fde7f45ca1cff5ab6142c.png)
那么具体看这个加密对象怎么创建的，这里三个参数r0、r5、r6、分别是1和key和iv，定位到了这里，不能发现`key`和`iv`这里都不是直接用的，而是分别都被函数调用了
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-136d2bf6563b430f7b393a6e648d1b58ec50ddc8.png)
那我们首先看key是什么情况，对应的是`m50433e`，代码如下，原来如此这个key并不是直接用的，而是用`SHA-256`后的值，怪不得算不出来
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-0a8f440e01f2cb7ad8a1e1675d0d64866f49c39e.png)
那再看一下iv怎么处理的也就是`m50432d`，大概就是这个样子，可以看到最后其实就是将iv变成了字节数组然后作为`IV`，说人话就是直接用了
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-2440aac877834ad0d1737667d70bcc8dd3a2b206.png)
既然如此验证一下，对上了，完美！
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-0f372f6bf424958084b7c8259bbd5d15c5d4f10b.png)
- - - - - -
0x03 问题攻破和复盘
------------
既然如此那么就来复盘一下为什么一开始浪费了那么久说白了就是因为没细看，然后忽略了多态的声明，以及`KEY`在使用前的处理
既然如此那么回过头来再解决一下为什么算法助手Pro和frida都出问题了没成功呢
我又重新触发了一下验证码我输入的是`1234`但是没有hook到，不过因为手机号也做了加密，而且用的一个算法，搜手机号却搜到了，如下图key和iv也是非常准确的，也算是一个平替方案吧
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-7d473ce2184062c25fc41cde9a65815130a383eb.png)
然后就是frida，我回过头又仔细看了眼frida函数，注意由于我是在函数调用那块直接用jadx右键复制的frida代码，由于存在多态，它hook的是父类这个抽象函数，而不是子类重写的具体的函数，所以能hook到东西才怪，而且就算hook到了，这里key还是没处理之前所以也是不准确的，所以这里要改一下
![20.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-7dd4e4bab77b58e7298ac02791f4772e4a0fdcca.png)
所以我最后决定直接hook这个`javax.crypto.spec.SecretKeySpec`的构造函数，因为它的参数第一个是字节型数组就是我们想要的处理后的key，如果hook别的值参数或返回值都是一些对象，非常不方便，
![21.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-7828e370cfbde39d89401f450a63cb59dfc822a8.png)
hook脚本如下
```js
function hookTest1(){
var SecretKeySpec = Java.use("javax.crypto.spec.SecretKeySpec");
SecretKeySpec.$init.overload("[B", "java.lang.String").implementation = function(keyBytes, algorithm) {
// 把 byte[] 转成 hex
var hex = '';
for (var i = 0; i < keyBytes.length; i++) {
var b = keyBytes[i] & 0xFF;
hex += (b < 16 ? '0' : '') + b.toString(16);
}
console.log("[\*] SecretKeySpec key:", hex, "algorithm:", algorithm);
return this.$init(keyBytes, algorithm);
};
}
function main(){
Java.perform(function(){
hookTest1();
});}
setImmediate(main);
```
然后就可以了，不过由于app内部加密不止这一个，所以结果很多，干扰也是非常多的
![22.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-b7ca962e19f514061d5fe41b57e373b0025acd0b.png)
- - - - - -
0x04 AI加持，秒出结果
--------------
对于这种复杂的事情，我非常希望能通过AI解决，所以我之前写过一篇《破译之眼：AI重构前端渗透对抗新范式》，大概就是利用`Gemini2.5`的支持100w上下文的特性，直接让其分析所有js，那么这次我仍然希望通过AI解决，对于研发而言，现在出现了非常多优秀的完全的AI编程IDE，如：Cursor、Trae、CodeBuddy等等
所以我打算尝试一下，而按照我的习惯自然选择了Cursor（大模型用的还是Gemini2.5），首先利用jadx导出
![23.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-d6cab2a9c43f009b178525d34ba85beb24777cea.png)
用cursor打开，然后给出提示词
```php
当前这个文件夹下面有很多文件这是根据一个app反编译过来的里面有大量的代码，现在有个请求/auth/v1/phone\\_auth，你要找到这个请求并且根据链路分析，它的参数存在加密，找到加密函数以及key和iv
```
它执行了一会确实定位到了，而且分析了代码，但是犯了个错误还是没有发现`SHA-256`那步
![24.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-214e7090064ee4bab4b81611cad2742b5266187b.png)
所以我这里提示一下
```php
没有这么简单，它的秘钥确实是xxxx，不过经过了变形
```
（因为我们这里是带着答案用的AI，所以上面的提示词正常情况下我们是不知道有变形的，不过我们大可以猜测，那么真正利用AI进行加密逻辑挖掘的时候，提示次完全可以变成下面这种形式）
```php
应该没有这么简单，我查到了这里，对应的秘钥和偏移我也尝试了，但是得出来的结果并不准确，你再仔细看看，看看是否存在那些遗漏的步骤，这个KEY和IV是否就是最终的，在使用之前是否经过某些变形之类的
```
也是非常牛的分析到了，过程非常快
![25.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-64dcbc72f99fa9a482021c1107ada010194ac3a3.png)
最后让其输出一下变形后的值
![26.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-4c23e7cf02e4173fe1f7f44115d9047c6527fae5.png)
- - - - - -
0x05 后续
-------
然后就这样了呗(￣▽￣)／
![27.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/10/attach-06ff5a731042213da64ad2979c4a0328d728776e.png)

* 发表于 2025-10-29 09:45:48
* 阅读 ( 280 )
* 分类：[WEB安全](https://forum.butian.net/community/Web)

2 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![小惜渗透](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b50fdf6f4d64cde9c52d29595...