---
title: 实战】某次演练过程中一个有趣的记录
url: https://mp.weixin.qq.com/s/QTfC7ggfR0_eVeAgLFG56A
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:35:08.486932
---

# 实战】某次演练过程中一个有趣的记录

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTasw3U73yrwIHibHdb2XnSMtUuhaBNsU597C5DBelRPWlffictHYJL5iaVA/0?wx_fmt=jpeg)

# 实战】某次演练过程中一个有趣的记录

低价考证，滴滴→
低价考证，滴滴→

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

**免责声明：**由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，本公众号及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！

记录在某次演练的过程中一个有趣的记录。

文章作者：先知社区（Asen）

参考来源：https://xz.aliyun.com/news/19378

**1**►

**正文**

还是开局一个登录框，先看看是什么指纹发现是Vue的就先偏向去测试接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTacicOJcbeB3n9TXZxrCTUZ1S8WZCqoj5b0hnvn7xR6xoOyDgRibt5VhVQ/640?wx_fmt=png&from=appmsg)

就在findsomething上先看看有没有一些有用的接口,看到这一段接口就有点未授权的味道了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTab105Jic0ZKc0iaynH0Hh7D19sdejv2G8I88EbEsiczTz8jHfQgOLDianpQ/640?wx_fmt=png&from=appmsg)

先用Vue Crack看看有没有一些未授权的路径进去看看还真有东西，这个插件使用起来也是非常的方便，他会自动识别是否未vue，如果有的话他就会自动添加路由。

```
下载地址：https://github.com/Ad1euDa1e/VueCrack
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTa8vEjngKTQzHWOYOzOoffBc8JfExR9xKicg51VqHyibzyeMTKRQCNtJcg/640?wx_fmt=png&from=appmsg)

随机找一个，直接就进来了可能这个时候虽然没有任何信息，但是我们可以点击网站功能点看这些功能点是否有鉴权问题，还可以测试以下sql注入这些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTa4M5ohqO3JTaUJwrgQzVMuA2xwUXbRlFwwrTlIlBicibicpq2DiaAJPyVCg/640?wx_fmt=png&from=appmsg)

这里我简单的点击的一下查询功能，没想到就直接查询成功了还是有点意外第一次遇见这种情况，而且这里的数据量还是非常的大一页有十条一共有四千多条，就是4w+的数据了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaNdYK0Xljmg3tVF66s4wFPNkDVl7q5YbyKM05aj8QCc8X4XEl9vvuHg/640?wx_fmt=png&from=appmsg)

既然他一个点都没有鉴权哪肯定会有很多未授权的地方，重新回到登录口看看接口。插件匹配的接口肯定是不完全的，这里就f12看看前端的源码，然后在刚才的findsomething中看到有/api这个单独的接口这个站应该是一个前后端分离的网站，api应该是后端的接口，所以就直接搜api看看他有没有想关联的接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTa37SAPN8DY4mYGk49Ltttw27icgiaIicDpU4XjnUM7jxYAIpvjo6mntUnQ/640?wx_fmt=png&from=appmsg)

这里果然有东西，也看到了api的前面标出为post请求，而且还有几个list结尾的如果能跑出来估计也能有不少的数据了，但这个地方需要注意一个点就是，不能把这些接口拿出来单独跑，他的前面是一定要加上/api，因为在前面的测试中我在抓取登录口的数据包是发现他的每一个接口前面都是加上了/api的因为路由前缀挂载机制，所有后端接口均被统一绑定到 /api下。因此实际调用接口时必须携带统一前缀。抓包测试！！！我这里就直接抓取刚才的查询接口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaBKcUcXtHAOc3Zic6XkPibBk0X659QqVLSSu8EzZeXaC8aE9kOQM4CAog/640?wx_fmt=png&from=appmsg)

然后先进行一波fuzz，前面几个接口基本上都有数据这里就不做展示了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaprZORxL6icSr8Nmez5ic3uyqwOPclVqRlsTI8p6ovtOwiazHgScIcRTcA/640?wx_fmt=png&from=appmsg)

然后这里有一个特别有意思的点，还是回到刚才的查询的功能点，这个是查询的那个数据包，返回的数据跟在前端的数据是一样的，但他的下面有一段请求参数，这些参数也是可以控制数据的数量，但是有一个很神奇的点是，我想对这个接口进fuzz，把那些参数删掉，他居然重新返回了新的数据，而且体量还非常的大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTa90mYshLicQ5U5mibZicc4GiaBvYbboNhdIj2nibEkYJy6xuwFVWNbSQic9vQ/640?wx_fmt=png&from=appmsg)

我把以上参数删除以后，进行发包，他居然返回了十八万数据，我只能说太神奇了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaiam1DtgoFuvqEJ2m3VicLP9rR3h5ibZmPRXv0UsFC5u1JZoEhakCrp6pQ/640?wx_fmt=png&from=appmsg)

**下面是一则内部学习圈广告😜**

**别着急退，看完的师傅们有福了/doge**

欢迎师傅们加入内部网络安全学习圈子。圈子提供三大板块的内容：

**1**

**网络安全0→1学习路径**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

1. 完整的「30+周安全学习任务路线图」公开，每周任务明确，清晰的学习重点和目标，从入门到进阶，由浅入深，循序渐进；
2. 学习内容涵盖：

* 常见的Web漏洞原理与利用
* 业务逻辑漏洞挖掘
* SRC实战技巧
* WAF绕过、代码审计、免杀钓鱼
* 内网渗透

  （Linux&Windows）提权与权限维持
* 隧道代理、域渗透、云安全、AI安全

3. 每周发布学习任务+参考资料+建议，学员可自主学习+实战练习；

**2**

**SRC漏洞专项挖掘**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

1. SRC漏洞知识库持续更新；
2. SRC挖掘技巧、分析方法、视频教程打包；
3. 分享优质挖矿案例，降低上手门槛，教你赚赏金。

**3**

**常态化内容更新**

![图片](https://mmbiz.qpic.cn/mmbiz_png/dGCYMHZUKeFyRPgswYHs24iaP9QSZr6Of35ichXI6icv5WergQUcNjojdNRRp9CeibzvQHPPNNsxL6aaqVJ8gjQaqA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

日常分享优质学习资源与攻防渗透技巧，包括但不限于：

1. 红队/蓝队安全攻防、免杀、钓鱼技巧、攻防渗透tips；
2. 学习路线推荐，教程、方法、技巧tips打包分享，实战视频、工具、手册一应俱全；
3. 根据网络安全初中级学习者水平，精选最有用的内容，不让你在信息洪流中迷路。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYnqBadHPfYribO0Eh7AO6sZtibP7icnEL1CIv2ibPnlUibbBzpK1lImaQsiawxpEKD4wOE3B9tBMll0HBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=81)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzD6B7ialvhZB0XJtGrrSiawmjIhv4ZRW4gTvdhQ1MkSTNvv530EOqSfKBQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDJKQUZRFgUp7micv32kZwQClN4Nrwjs2M136dAhEJzmbia2bZ17c7jRicw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDnJkibQvVicDW74QWJvoiaWOnsrGbwibCJWEkToaicK45yPzIlvD24jickxWA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/mmbiz_png/HaJr68L1tTSb1XKYzBaSZ12svUicannzDQL6MIsF3Yqiczbczx67Z76BjgaXGGn8anlibtj82icib29ZyuuP3N7s9gw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=8)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYx6e5OYqRUhe5nHp6uuOTaj5Sgo33WiaHyVjXhiaDxpy2Ub3j8RH9oHDdjmiauN7IHrEh4eQHbZYgYw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=50)

此前的一下学习记录：

![图片](https://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuavfHUHVEFOGPwgcIyxvs5JeINcQEBnZT1hY0K4Pw7ya9o9gUkcFgaItIRibaMVQuXrhsthgdXELGQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=84)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYHyEqA6pDb8VLMp8HsIicKjibbR1viclLspl5Yne6f4QnlkOiao0R4iasZ71DOILPUe0XSzqOKuDdPPfw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=85)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuaacJIuOWXhuibQcZiavltCSw4Uce8HJjKUHgQwKLmUyicQ16W3RibjnXgzw6ibRXYSxKeC4XebucKp1lA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=86)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/h8P1KUHOKuYHyEqA6pDb8VLMp8HsIicKjTg4aY5w0eR7nPUKJ9qNEk5Y0COUibDSvmPKiaMVBo8Nrqgex2Gs0h9xA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=87)

### 考证咨询

最优惠报考各类安全证书(NISP/CISP/CISSP/PTE/PTS/PMP/IRE等....)，后台回复"好友位"咨询。

### 关注我们

点个【 在看 】，你最好看

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

Z2O安全攻防

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/h8P1KUHOKuZq5sEo9xMfOVGAKuZWic3dSmVcRnYRDwbJdF39kiaGOrw5ofgicOs4WUH5PBiaq1MXpYDVbfSlCKJ00g/0?wx_fmt=png)

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