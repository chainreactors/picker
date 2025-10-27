---
title: 浅谈常见edu漏洞，逻辑漏洞➡越权➡接管➡getshell，小白如何快速找准漏洞
url: https://forum.butian.net/share/4291
source: 奇安信攻防社区
date: 2025-04-24
fetch_date: 2025-10-06T22:02:44.497931
---

# 浅谈常见edu漏洞，逻辑漏洞➡越权➡接管➡getshell，小白如何快速找准漏洞

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

### 浅谈常见edu漏洞，逻辑漏洞➡越权➡接管➡getshell，小白如何快速找准漏洞

* [渗透测试](https://forum.butian.net/topic/47)

之前闲来无事承接了一个高校的渗透测试，测试过程中没有什么复杂的漏洞，是一些基础的edu常见漏洞，适合基础学习，于是整理一下和师傅们分享。

今年对某高校进行了渗透测试，发现了一些比较经典的漏洞，写一下和师傅们一起分享。
1.教务系统登录处短信轰炸
-------------
![11).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ac50b771efb00fb941438674ee4fb3ba4a90e0ed.png)
学校的教务系统登录处，发现有一个手机验证码认证
![kappfra2).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ca5476997fbfe124faa46cb094cda504485a7fa3.png)
这里会发送一个验证码
正常来说，每发送一次短信验证码，这个校验码就会自动更新一次，然后会报错：“验证码错误”。
但是这里抓包之后，发现能抓到两个数据包
![attach-1e1244475c6dff0e2087e23915db3711aab85810.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-13cc389753d3fbfe0860ad3198fb4b87b1099ef5.png)
这是第一个数据包，可以发现是对验证码的验证，我们把第一个数据包通过之后，拿到第二个数据包：
![3).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-e5cab92e0329ed6b09aaeccae515615f8093bd76.png)
可以看到我们的手机号出现在了第二个数据包中
我们点击放到repeater，然后点击send，可以发现一直发送：
![111.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-636d3a22dbed36bbb194a6b71cf851ec28aa643f.png)
\*\*原理\*\*：正常来说校验码的验证和发送短信应该是在同一个数据包中，这里不严谨的设置，将校验码的验证和发送短信的数据包分成了两个，我们输入正常的验证码，通过第一个验证的数据包，拦截第二个发送短信的验证码，即可实现短信轰炸。
这里分享一下短信轰炸的几种绕过方式：
#### 1.手机号前面加空格进行绕过
这是挖某专属src时遇到的
![213122.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-2028e18aed8821f29c1979397e6bcd9699be9eba.png)
account为手机号，正常情况下，一个手机号短时间内只能发送一条验证码。
在account中的手机号前面每加一个空格可以突破限制进行多发一次验证码，
![attach-d5386ba03170c8b2e6603e5c0ad7bc221338a481.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-4514659c6c520acf4d95f2699facaa7fc705e94a.png)
burp设置两个载荷
第一个载荷用于填充空格，设置为50（这样设置，一个手机号就可以发送成功50条短信）
第二个载荷用于循环遍历手机号，可以设置遍历10万甚至更多的手机号
#### 2.加字母等垃圾字符绕过或者+86
#### 3.伪造XF头
2.校内某实训平台任意用户注册、任意用户登录、修改任意用户密码、验证码爆破
-------------------------------------
![5(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-aa267e3194b775a2e445c17bdc09b1df412aec88.png)
这是校内某实训平台，我们先点击注册功能点。
![111P(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-661a6e92430265220eeea378333fdf7b965aed16.png)
我们点击获取验证码，然后进行抓包：
![12312GR(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-5e4d3af4882f50dd889150e5bac37dac7c156a82.png)
可以看到手机号被编在了url里，我们这里使用“,”去拼接手机号，这样就可以把验证码同时发送给两个手机号，并且收到的验证码相同。好比我知道你的手机号，拿你手机号去注册，我根本不需要知道你的验证码，因为验证码也会发到我手机上。
![1233213123zCywpV(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-36211c99ae86e1f65769b911a2d271093bb6996f.png)
![123321(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-38729cda8025a23cace00e425ebd5a73459f4119.png)
修改密码功能点也是相同，我这里不进行过多赘述
#### 验证码爆破
![ka12332132123123)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b027ff3b296f8c0e1ff9c37a3fb77c8e7a37393d.png)
正常发送验证码，然后在填写验证码的地方，随意输入四位数
![attach-f9667d233ce6573b5439c68f327ddd189343fee5.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-c2707c3b84fe57a2b7f1f0f9f8e5421f0b4b542f.png)
![3213121322131)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-354fbb11097a3246bce2892eb33b72886d0821a2.png)
可以看到在7710的时候，长度不一样，成功登录进去了。
\*\*修复建议：\*\*：对验证码输入次数进行限制
3.越权查看所有学生和教职工个人信息，数万条记录
------------------------
![2222.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ccd69cdb6f2ae9ae5ad8ea83de251607edf37405.png)
教务系统个人中心处有一个查看最近登陆记录的功能点，发现右上角有个查询，我们抓包尝试：
![1322222)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-bf9c6c857f38273aa7167fb8b118930e83fd0520.png)
可以看到这里可以看到我们的登陆情况，我们尝试去修改value的值，看看能不能直接越权查看别人的登录信息。但是发现无论修改成什么都会提示登录信息错误。
修改成0、1、-1都不可以，但经过我的尝试发现，只有一个值可以，那就是null！
我们让value=null
![31232213Vq(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-b10dc5ab1cbc51b7487e257f42736c9ff9996b7c.png)
但是登录的记录明显有点少，而且观察发现好像都是登录失败的记录，这时我发现有个name字段，我把userid改成\\*：
![123312(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-029475fe13937f02ac1e99c2547d65fd72d25f48.png)
拿下所有学生和教职工的个人信息，包括姓名、手机号、身份证号、学号、教职工编号、登录ip等
4.教务系统绕过手机验证码换绑手机号
------------------
![12332132(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-8d8094adaa1a1d7da7928f6d9c25e14d63024223.png)
也是这个教务系统，安全中心有一个换绑手机号的功能点，我们点击发送验证码
![3333.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-375bd6198c0739f78470937aed0f53722f500ba7.png)
这里可以看到是修改195开头的那个手机号，然后我们forward
![123312(1111)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-401f8f403e17c9d95a3cd9cb266c15200c47850c.png)
之后弹出一个验证码，我们输入验证码点击确定
![1231232.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-90b61902006def51f3fda9950299c12bc9d30b0a.png)
这里的验证码就做的很好，和发送短信的验证码数据包放在一起了，杜绝了短信轰炸。但是我们这里把195开头的手机号修改成我自己的手机号。
![1312BtK(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-58dce4edb441a5f37791849a2555b9a27bd257ff.png)
成功让自己的手机号收到验证码，以为皆大欢喜了，结果。
![1111e(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a6e4f79656d06a4acb85ae6a0fce43a077416e20.png)
显示验证码错误，这是为什么呢？
我们继续审一下错误的数据包，也就是我们抓输入完短信验证码，点“下一步”的那个数据包
![111.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-15676325904fc05ea27ef6150240031f695566cb.png)
可以看到居然在“下一步”的地方，对手机号又进行了一次验证，我们将这里的phone改成我自己的手机号，然后forward
![211221O(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-16974fa8de9876d8bee2450b43d54869a6fbeb2d.png)
成功到达绑定新手机的界面，成功绕过了验证码认证，可以换绑任意用户的手机号。
5.校内某平台druid未授权访问，导致泄露用户session，可以实现任意用户接管
------------------------------------------
![111Bc(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-08ea2beb092ca1ac416c0c44401c69dd3bb2fe51.png)
这是校内的一个实习平台，url为“<https://xxx.edu.cn/shixi/>”
然后之前读文章读到了一个druid的未授权拼接，/ \*/ druid /\* /
于是尝试拼接 ：“<https://xxx.edu.cn/shixi/druid/index.html>”
![2221)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-485cdc773b833a89891fcb183aaeb4dfe9e44ba2.png)
可以看到是有druid的未授权访问，这里会泄露很多东西，比如数据库信息，数据库查询语句、访问记录等等。我们这里搞一下session。
可以看到有一个session监控：
![3333hPXD(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-712264b51b91cd9e081cba37b2bc3f37e715ebb4.png)
可以看到这里有登录过系统的用户的session，我们要做的就是把session收集起来。这里我有个比较好用的方法，可以ctrl+a复制全页，然后粘贴到excel里，然后选中session列，就可以快速的把session复制到txt里了。
![44444Zc(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-a109a71ab45901fcc24c02dc3fbec0e6107d1316.png)
可以看到我们把session这样收集到了txt里，然后打开yakit
把txt导入到yakit的pyload里，然后去抓一下登录窗口的数据包：
![5555tPEr(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-ffc78692d0dcc8a3334e4a027119ae08a294cd3f.png)
可以看到cookie有个jessionid，我们把他的值设置成标签，然后去拼接刚才的session的payload去批量访问：
![666666(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-14ed2767f7754fbc53262623c4d7c0e08d6075b2.png)
可以看到有很多200成功访问的，也有一些无法访问的，无法访问的原因主要是因为session是具有时效性的，长时间后这个session可能就会失效，但是只要源源不断的访问这个系统，我们就可以源源不断的盗取新的session。
我们找一个200正常访问的数据包，把里面的session复制下来。
![77777A(1)(1).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-12ae808caafa94a27416f600541a4578b8d30db9.png)
然后回到网页，打开f12里的存储，替换里面的jsessionid
![1231231.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-55f75bb019f0295a50dfe346992ab1c2b2dcd97d.png)
然后刷新页面：
![1111111).png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/04/attach-0dd834f7133b1...