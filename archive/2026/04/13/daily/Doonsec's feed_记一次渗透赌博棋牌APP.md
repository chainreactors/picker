---
title: 记一次渗透赌博棋牌APP
url: https://mp.weixin.qq.com/s/VIdVFiiLqiop9nju2AeLGA
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:40:16.818747
---

# 记一次渗透赌博棋牌APP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQnJl4IQoK5MPbRA6lxNlpcWAA2afdXibHRaeyVFS8tdHZxfyEgLZdA2YnKrhPX9qJ14etOWDLGLD0PzpeibzcnElabo0tpK73S2k/0?wx_fmt=jpeg)

# 记一次渗透赌博棋牌APP

安锐信安全攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于星阅安全
，作者星阅安全

![](http://wx.qlogo.cn/mmhead/NoFChqEQomHJVh74UFcpI96bibia1xHhjOMiaj9BD38MuZbhhcvoWMRaExYlkF2toeKdVMbRPgh9CE/0)

**星阅安全**
.

随便发发

![图片](https://mmbiz.qpic.cn/mmbiz_gif/QO6oDpE0HEnGMibdEBOicags5vPicwyeszAiczWiab7e9BhiaNXaT1WIzorBQpRQLE3o8rHySkyNKkLiceRN7uBtzlJ3A/640?wx_fmt=gif&wxfrom=5&wx_lazy=1#imgIndex=9)

利用模拟器安装好APP,然后进行BURP抓包分析

![](https://mmbiz.qpic.cn/mmbiz_jpg/ODpESZtiboQnnL8ubhPAEibuNgib6gx11N7kia7Nh29UqWzAUY7Nh3RqvbC8ia9yIgV3M13slbHE4V9gcZZuM3kiacwUg4owbX3WqA37cywUGCXS4/640?wx_fmt=jpeg)

通过各种手工分析,找到**某处SQL注入漏洞**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQk9zs5dKI9GaYfLNva7QjdPyrsxqlcK4tKOUIFvn8p16qibGP2GaHyzqlCibfVqniaRPTnZYxyDiaElTD1bgmYfdUzZjcxibIkHneFs/640?wx_fmt=jpeg)

之前信息收集的时候已经知道目标开放1433端口(爆破失败) 因此注入的时候,直接 `--dbms=mssql`  加快速度.

注入点类型

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQl3DkTncQXZQpTvAibG6BAry4HgWBJpoPWvyNOY0M7SBuHcbhk38BmcibeSo6QO0UPykKAVF6mNY6lgyicqy8iblfkV9T0w2QCuYCo/640?wx_fmt=jpeg)

SA权限的注入点,原谅我菜,目前还没找到后台地址,数据库实在太特么乱了,虽然只有几个数据表,但是我不想一个一个的去翻,直接读sa密码解密失败,行吧,尝试下`--os-shell` 结果如上图,告诉我不支持,那我们改下类型,指定跑 `stack queries` 试试

![](https://mmbiz.qpic.cn/mmbiz_jpg/ODpESZtiboQltPfCjO0hzQBwzN1wRJnFSjHNB5WZW8ea1O3eXQEImd6n0vxaxXuUbKsqmGa27hlxXA9Dy6Nby494ZhsmPHzYKabzsUuTlcuU/640?wx_fmt=jpeg)

成功跑出,并且没有降权,连提权都省了,我这RP![图片](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9e0NtLFgdeEPjj73BXnmCF311niaQBrkSfdibCbKCzunjAIOiae4eqzw28vrSiavCJVkCuKUtkVZYtlw/640?wx_fmt=png#imgIndex=4)

接下来就是找绝对路径,然后写shell,拿到shell就方便多了,为什么不直接加用户上服务器呢?因为现在的服务器都是各种云警报,我还深刻的记得某天晚上凌晨4点上某服务器,结果管理员3分钟不到开机叫我衮蛋的事,所以呢,能不上服务器还是别上服务器的好.

已知服务器容器为:IIS7.5  08服务器

获取绝对路径方式: `type C:\Windows\System32\inetsrv\config\applicationHost.config`

不过由于注入点变成了延时的,所以速度超级超级慢,我这尿性忍不了,读文件读到一半放弃了.换了个思路

`dir/s/b d:\initial.aspx`  搜索网站的这个文件的路径,得到2个路径,目测不会用中文,所以猜测第一个是绝对路径,然后echo 123试试,发现正确,然后直接写一句话,成功getshell

![](https://mmbiz.qpic.cn/mmbiz_jpg/ODpESZtiboQmVzybdyUWkubVZrmLZXyCffCiaibthdiay84iasFqbNdkWtz4m4WxzLSDd4ttBpxzlW6nGScYI2oLTice3LljORG4bH39KoiccVJJKU/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQmdX4geAs0S4GsKS07orMAiaj2nEtAYQ4EXsdyWgLzYQNrBTJoS8kbyQBJ1fpILtJ6T7aza2hib2Jg7nNBspyiciblqY733ENoDEAw/640?wx_fmt=jpeg)

马在根目录不好,上菜刀第一件事先换个隐蔽点的地方在说别的

然后在获得SA密码

![图片](https://mmbiz.qpic.cn/mmbiz_png/Uq8Qfeuvou9e0NtLFgdeEPjj73BXnmCF7Pr5MKuBAIaKmicSQhVb1WrwNibcohNOJUxassInNDeMnTjROkRibsVyQ/640?wx_fmt=png#imgIndex=7)

得到sa密码之后我只想说,我为什么会天真的想着去爆破? 用脑子想想也能猜到密码肯定是超级复杂的,我也是服了自己,浪费我流量.

然后继续之前的,读取配置文件,获得后台和代理后台地址:

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQm9YVSEMb8DKcjYpDWPWUk04RdJNVBlDJB3d2eqrr7DyorSEhLfdPLelHDGkwoUrnlKTeExeyoR9twRLXGIIU80NF9LBhC7ev0/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQnxxfMbVkb4bEXK1xtMk7hsU2tJPozUt0qDKVCj2f0ElCOOLpiavxRiaHEXZeicOJhCTx6HVN0YaTLseIWFtreFzXygqMKAlGicpdI/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ODpESZtiboQnEwEw37sKg8gWaJzib6wQZkxIWhRHIVz8qehOfmxR8QaUvnwob0MPDicI7jQgEW5gNcqzMe2KBrsT7u2g3kLpibjJGmdI1p4tI1k/640?wx_fmt=jpeg)

接下来通过数据库查到密码登陆进去瞧瞧涨什么鸟样

![](https://mmbiz.qpic.cn/mmbiz_jpg/ODpESZtiboQmXswjc9Iww64PrUvKibUibdKbggU6NO9O637Vj4cicZgwNEWGLJcAfOTFbNQ2PagicUCc5A16IXmicvTePUt2a2RdODhqzqqLJOnBA/640?wx_fmt=jpeg)

三万多用户,赌博有啥好玩的,为什么这么多人玩,这玩意真的能赢钱?

![](https://mmbiz.qpic.cn/mmbiz_jpg/ODpESZtiboQmNKIovLkjt9mSyx60Ujeoy3bSSp4kVuru6SPuGWeFMIlRLdoKNb6PTP95SjMibSKePAZDCbP4b7oTSmEoIKKr1kNksC64C2qVs/640?wx_fmt=jpeg)

钱买排骨它不香吗?

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6CibLpliaRicnInQKulaWAIrlF6GiaAKqGGedAJna0VPyjDuEbc3J1ftfjzic5XjQjX7qKVic11JbLcd1C9I7BYVsHs9rQRP47HTcc9xKyJnBbF3k/0?wx_fmt=png)

安锐信安全攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6CibLpliaRicnInQKulaWAIrlF6GiaAKqGGedAJna0VPyjDuEbc3J1ftfjzic5XjQjX7qKVic11JbLcd1C9I7BYVsHs9rQRP47HTcc9xKyJnBbF3k/0?wx_fmt=png)

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