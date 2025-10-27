---
title: 同源异梦：JWT 泄露后从主站到旁站的渗透曲线
url: https://forum.butian.net/share/4443
source: 奇安信攻防社区
date: 2025-07-03
fetch_date: 2025-10-06T23:16:27.080159
---

# 同源异梦：JWT 泄露后从主站到旁站的渗透曲线

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

### 同源异梦：JWT 泄露后从主站到旁站的渗透曲线

* [渗透测试](https://forum.butian.net/topic/47)

在测试过程中，常常会遇到jwt的泄露，但是在测试时，无论加什么header，如何改uri，最后的结果不是401，就是404。不妨试一下同IP站点或者相似站点。

### \*\*发现过程\*\*
测试时第一步肯定是访问网站，然后点开熊猫头看是否有泄露，很凑巧这里只泄露了jwt。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-e5ddb71fbb3596d444f7f72a86b21830121e2a3c.png)
开始拼接口，拼路径，但是最后得到的也仅仅是401。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-2fd5843838c2268958eb061d87096db59371c587.png)
走到这一步肯定是登录框爆破，或者fuzz看是否有未授权，都试过一无所获，那只能再回头信息收集，开始对ip进行收集，发现还存在其他系统。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-41df80d6a49ffca3f25a9f7a2810c0fef82dc242.png)
访问以后进行登录测试时，发现虽然是两个系统但是接口似乎有点像，尝试将先前的jwt放入第二个系统进行测试。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-aa7fac3656dc979311f1a49fa25fe00a2a8ec69e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-a78db19f3b0a468fc260e99bf66f1141537001b7.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-8788d6321c1a32f0607f1435657789bc8323939e.png)
### \*\*测试过程\*\*
登录框中随意输入账号密码，抓取该登录数据包，放入重放模块进行构造，在header中加上token:{发现的jwt},在上图中，我对list接口比较感兴趣，f12查找与该接口有关的参数。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-ed627d1b0f2b115e92c0811a44ead7f140cdee37.png)
拼接后得到的信息还是缺东西，这时我们只需要将body中的参数放到uri中即可。成功得到相关数据，这代表这个token可以用。
![QQ\_1750599167953.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-c3ca5d04d56a32c4fb26430903b11305059d9dd1.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-2c5b47da5bfac2efbce04f2aa82caafa8b6c033c.png)
此时已经有个账号相关的信息，并且还有一个重置密码的接口，继续拼接，显示账号id不能为空，我们刚才拿到了账号相关的信息中有一个platAccountId字段，直接加入，显示密码不能为空，在登陆时密码字段就是password,加入后修改成功。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-00fcf25fa8e57f4642c3293d8c422cb9a33dfdd2.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-09be4b71d030cbbad2b2ccced769049b2d3d44d5.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-d07386b00d3a2c5189fad0b6dc7b750d2c2efc5f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-cbb2d68fd5183890658cd3860827486686383405.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-36c046dd18b2681d1fb0f401dc75fff0017b605b.png)
到此肯定是要修改管理员的账号密码，成功后进行登录，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-511d4c9564e417f0fb36cdd470a9e5079174ef0d.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-b08c9d64e4368520911743ca86c7b0a7386f5002.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-df049f672432128d259e3b12b9239b10ba68856c.png)
#### \*\*sql注入\*\*
在加入单引号以后发现会报错，仔细看发现是druid防火墙的报错，druid防火墙是可以使用报错函数进行注入的，这里使用的payload为/0 or updatexml(1,concat(0x7e,user(),0x7e),1)=1，也成功得到用户名，数据库名当然也是可以的。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-94c68ae29b04bf3b42317e46833d7995b9eb531c.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-b539349ab73f8d750dc53307c0195dbf6f33ec4a.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-afc608fe611a85f263fa2ac275071b94aed42399.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-6a747b9ffffdd4921cc18c802572b139a4320a85.png)
### \*\*XSS\*\*
由于该系统使用的是vue框架，它内部会存在一些过滤机制，f12看上去是写上了，但是已经被实例化了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-6de04e2565c192da75c2197335c22ea4bde882dc.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-c4af25843f9fb129ec97c80390991a3aa577b63e.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-bad5bb3d268d47a1433fddd6bb33eaf0ddb3f141.png)
像绕过此类限制通常是找开发者误用v-html 的地方或者是编辑器，通常编辑器是最最无脑的方法。要不是上传html等等文件，要不然就是内容加入各种标签。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-26a29e70cc1c32cc16c9587064eaba61b4a52c4f.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-d6d06ab25272347389bb529dad1d3ea1622a4fdd.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-1d44a82a5011f1b0b19f92a52be2af4702cb44de.png)
### \*\*敏感信息泄露\*\*
由于现在很多网站通常不会直接接受上传的文件，通常会放在存储桶中，虽然防止了一些代码执行等漏洞，但同样会在设置上传权限是泄露相关的aksk以及临时STS,上传文件是发现返回包中存在aksk，使用obs浏览器成功接管其五十多个存储桶。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-872bc729b4c51218f7ab7a741d5d4bd33367b945.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-dcd2489c76c2e11326b295da45e457081af8a874.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-f75554d53c958cd95e76330fef2d42f39e502908.png)
由于现在是admin账户登录的，可能危害并没有很严重，直接将一开始得到的jwt进行替换，同样也成功了，这应该就又可以水一个洞了。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-0e06691810a10a8e36f2cd2a4d2aafbf21731083.png)
### \*\*越权漏洞\*\*
由于已经拿到后台权限，完全可以使用不同的账号测试越权，直接重置密码，然后使用其他浏览器进行登录。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-cba1c8e41be0205d4e09b5dba89bb9035f6ba3a9.png)
可以看到该用户的权限很少，但并不代表真的很少，有些网站只是会对显示的菜单权限进行验证，并不会对功能点进行验证。f12找到该用户的token值，将burp中admin的token进行替换。获取aksk，可以，获取所有租户信息，也可以。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-77cccd858f642fb05b5ad2fc66d908078c1ef9fc.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-592afcf4350bee4ad9737749d77820c18c2ebb14.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-e1875a11b9e578cf501a65762e7d157da1651c35.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/06/attach-81df032aec017544a87dedc578b34adf84bfdb21.png)
### 总结
```txt
这些漏洞可能在各位大佬眼里洒洒水啦，新手刚上路，轻点喷。如果有一些欠妥的地方还请各位大佬指教，把社区当一个博客也不错，希望以后能挖到更多有趣的漏洞。
```

* 发表于 2025-07-02 09:43:33
* 阅读 ( 4071 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

13 推荐
 收藏

## 2 条评论

[![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b35f9ec5dd87bbfd70f4490a6eab00aec5adc8e.jpg)](https://forum.butian.net/people/16588)

**[爸爸的爸爸](https://forum.butian.net/people/16588)**
2025-07-03 11:59

学到了 厉害

* [0 条评论](#comment-2574)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

[![](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/21522)

**[胆如猫](https://forum.butian.net/people/21522)**
2025-07-04 10:35

值得学习

* [0 条评论](#comment-2582)
* 0

请先 [登录](https://forum.butian.net/login) 后评论

请先 [登录](https://forum.butian.net/login) 后评论

[![_7](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b3847ff00022e5b215aa903c3fdfaa8d1e4817f.jpg)](https://forum.butian.net/people/43057)

[\_7](https://forum.butian.net/people/43057)

技术爱好者

2 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![_7](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/b3847ff00022e5b215aa903c3fdfaa8d1e4817f.jpg)

如果觉得我的文章对您有用，请随意打赏...