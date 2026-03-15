---
title: 注意，这个方法密码也能被找回。
url: https://mp.weixin.qq.com/s/sX8jsbSrtlmvNEeTaVvi9w
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:31:18.349974
---

# 注意，这个方法密码也能被找回。

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QJTLZsy5trGvoib0yBTYWPf39EPhpz7ZwoFw2mVCNKWbH5lek7lrawySGZpDXj31iaf4BjK5Wbd8gP6sOwaFnFArXMrdDTyNzriacjictPicPPtE/0?wx_fmt=jpeg)

# 注意，这个方法密码也能被找回。

原创

建哥聊安全
建哥聊安全

建哥聊安全

![]()

在小说阅读器中沉浸阅读

# **验证机制之找回密码**

## **实验目的**

通过本实验，掌握利用密码重置过程中经常遇见的一些问题，绕过安全验证，从而重置密码。

## **实验环境**

·操作机：Win10
用户名：Administrator
密码：Sangfor!7890

·靶机：Apache + PHP

·实验地址：http://ip/index.php

## **实验原理**

在网站的忘记密码位置进行找回密码的过程中，可以利用密码重置过程中常见的一些问题绕过安全验证，从而实现重置密码。常见密码重置问题：

1、用户名枚举：网站反馈多余信息，可猜测用户信息

2、验码返回前端处理：可截获、修改

3、修改Request：用户名、手机号、邮箱、Cookie等信息可修改

4、修改Response：操作结果成功/失败可修改

5、暴力破解验证码：验证码长度有限，或验证码未设置可靠的失效时间

6、拼凑密码重置链接：重置密码链接有规可循

## **实验步骤**

### **阶段一：管理员安装cms，搭建企业网站**

1、登录"Attack"操作机，打开浏览器，访问http://ip/index.php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHPsFfssdv1RY8EomAMAvuVrTI2BrKKxGzApatrRcU0AzNNZ7KGKpk6XruKDzfE3c2SNv47fO7yF6YarWG8ZoDkAaqicMr8Cl0w/640?wx_fmt=png&from=appmsg)

2、根据提示，点击“点击运行安装向导”，安装cms

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHxU2yuShObD9sL4KIwnj2RoFt22fGBnmhygl8OicDuFa9nUlfNFJEE3lZVXJsA9iaqIAjIjY414gqmPsiaDXCefmCzvkKaV5ZhKc/640?wx_fmt=png&from=appmsg)

3、点击“我同意”，然后一直点击“下一步”

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGBpAYro7ibwJSSxOXjgYKDUZp5ChaChLIo1ScYtk0roWXtjsPEWKIdEVY9fEL5nJuYCicZS7AibVG4OsGe6TZAGdZXGxHUYfGHbI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEMeVst0sMzde1ibvgZSQPzwcr8OzJBW6PLciao1bdianSt76TeibMJLWqYlUZhB1Y7US7jSlmOkyJlfJmZb3DmRq66erwbLJuicPyk/640?wx_fmt=png&from=appmsg)

4、填写必要信息，数据库密码要填写“root”；数据库名任意设置，比如“zzcms”；管理员密码任意设置，比如“123456”

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHNDictTVNlsjJEuWyQCdPniayK1s9hUk2nXfxBmfMEcVPp5utMU6wuRlVoFWdWbgxib8aJk01fgicGCaOLbYSmKRqhrvtTZPjn1F4/640?wx_fmt=png&from=appmsg)

5、然后一直点击“下一步”，直至安装完成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trG8f8KKyPebaUfkNZAdFMGH6gKfmPLjQUkC0qvR6nia2TSlU0aiaMrAibGywf6GZ1ia3teia7Oec5BibF7ssJ68qwRUcQbH1rfib9vyHs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFIicpz1gkKhJH1mltAlGbDNzmT570rqy5uuD1BY0V8yFVA02mVgwicPicq6ISPNtYyxXDSgZfpOYXfpzblMBYBAWWC3hS3PJtriao/640?wx_fmt=png&from=appmsg)

6、点击“网站首页”，跳转至网站首页，至此企业网站搭建完成

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHWxoBpLStxREY4ArmSQnzyHaRfKxnlagowLepa6F8kZWXADQHrRIavrmkYAHo5CicLCDU6ngv3AuTIBKVawSEMiatvToRiaxw268/640?wx_fmt=png&from=appmsg)

### **阶段二：任意用户注册账号**

7、点击右上角的“免费注册”，跳转到注册账号界面

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trEQibHiaMVN0S4570iaUEMRKYtftGDSff8WfAZEC8LmgntwSial0lAj2PzAzoyYsFVc5jsXdlibhofTibTJVf4hcR7RTZqYDEUkto2C0/640?wx_fmt=png&from=appmsg)

8、填写相关信息，点击“提交”，注册账号成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHNZtU8m6KHviaMSP7yiaGXHqMaQMTkCf2D2PT9ZAGgbysxs6wQp6B5JKhKrd0Bj9XKibHHdz65gbF95EFG5I8RedO66oX0k1jaibw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHWLna1TticB6exy5WrfE5XChIYbESc3etcyicdOrL25f3awEojWPYfGoQNicGsH1LZUPmm5oK5j8iadmQicWRl6ibicZNjuAPhWQvpYY/640?wx_fmt=png&from=appmsg)

9、点击“安全退出”，退出登录

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFoSX2T9LTjmfszVFTcYictyARFb46gsVshuak6u4nNe989Y2IO47O2FFbicepI1CZMERvdnlqx0nGhKoC83yJL57ASbM3GsIU8Y/640?wx_fmt=png&from=appmsg)

### **阶段三：攻击者重置用户密码**

10、点击右上角的“请登录”，跳转登录账号界面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHOelKC6NfaIR8Gm4uTNQPhJ8ANh5Vpoc4BfRfxMrTYUialC4I7k8vAMibLyADSuJCrdnhj7V89fuE9kib3nRnTZgpHoWEh8PaS9k/640?wx_fmt=png&from=appmsg)

11、由于攻击者不知道账号密码，点击“找回密码”，进行尝试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEZJJDeJ1On2VlWLj7KlETXAX0SrBft8XbOYxHYWbNAJTCFTKodQ0icpJfvJvhzjKVOE5TicxRM8bUuZs7ukWUMq90dpKEHiby5rY/640?wx_fmt=png&from=appmsg)

12、输入任意用户名，提示“该用户名不存在”，利用网站反馈的多余信息，不断猜测用户名，直到正确为止

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEscMsFIianDZMReNxlDFjn3xd7YkPqXCCn40GYl2cjaiaJUe7sR6dQayx2DSuiaeRXjiaS9Ywz405yuBiczgEtDrVokCmC7STVibm1A/640?wx_fmt=png&from=appmsg)

13、根据图片验证码中的结果填写，进行验证码验证，然后点击“下一步”，进入安全验证阶段

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGYHnEgxeobibQibNgoWKUZIibZauSqR0ruA949XygULR5pJBneEXNicuv82pdDLgOEh7wGtADHia6yfhNGNNogqv8GnoqJrUa8MbsM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trHxibJ7PfoaXeLsDSnyfmzG0b5NGEhSnd9KXOGfjo51R5s4wjP1tzYGIJZ8HbNxxmnAZDvm5cFTmBul9Gg5CbAPEdKhkDAt702g/640?wx_fmt=png&from=appmsg)

14、由于验证码会发送到用户的邮箱进行安全验证，而攻击者无法获取到验证码，无法进入下一步。尝试抓包，打开桌面的的“Burp”文件夹，双击“BURP.cmd”启动Burp Suite抓包工具

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHyXIygG0pTX6hBP6gjYNmYT2yTVicwSibCZmo9biaBaayAujXFkfibOgHFPiceia2x0vxzSbzmaV9OGGKGZ5PA4krGxsUPKldFUVkeo/640?wx_fmt=png&from=appmsg)

15、切换到“Proxy”代理模块的“Options”，查看Bp的代理

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGuOxiaYpgTrXR9ZH8x6CBE9FsRlAN0ICZibbzSrTblQ66L6NFm14Yxue9KgibCgTtAZJH9WFnibu187jOKib5X92oKacuJI8WVWxNA/640?wx_fmt=png&from=appmsg)

16、切换到浏览器，选择火狐插件中的代理（配置浏览器的的代理），与Bp的代理一致

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEibbPzP3iar6wEr4TSdMd9CibEab8OxE7w8vf5w4ib0kOSk4icHxAxV5j6CDxZfHdUjyz6VJ92uhRMZrMClqMtHEkjVufKAfDiaNVjg/640?wx_fmt=png&from=appmsg)

17、随便输入验证码（不要点击获取验证码），点击“下一步”，提交输入的验证码，Bp成功抓取数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trESg0zxd5xsibJZFiaMNNFxicp43w4qujw7fwjHesWaOJDSlbKaA20OZUzSib21wu7YqZwicBq5dg9ujdGZIdMb5VzohjmbhkXJK01I/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trGUYeL5NajklFicZEbfSEuFQagQ1R0cXj7p9Ub5NN9EJvxHHBNLEXRZag1Dicw8icjVyV9mCbw8MZGmFAsk35kiccicsicg7svFaPEMg/640?wx_fmt=png&from=appmsg)

18、右键，选择“Do intercept”下的“Response to this request”，抓取响应数据包（即可以抓取数据包的响应包进行修改）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trFO5TjABJYYZ7k7jXuryUznPMx45YFB8WPAfJZ2lz4LIBbVeLbs4kQYlkxVP97jUnibJ3a3D3KATdCGK3iawMDapibQd6acOK1MtI/640?wx_fmt=png&from=appmsg)

19、点击“Forward”，转发数据包，获取响应数据包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEibv2dhweuu59ibusgn7gGibwKZiam7JRNytGF4dtdResYmNhH7HyuapmwCEibtzNgfKA1BbKTC13slSdl6hsZSn7ARk5gcfptKkJ4/640?wx_fmt=png&from=appmsg)

20、把响应数据包中的“no”改为“yes”,然后点击“Forward”，继续转发数据包

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trFUqPlumEnSU8sNKsLDwJePZ0gia3biaf7PKHeYvbVfkgT4Fw2K73TjZoPJDPwcXQKcL8NSyaUMKCI4rJOxrQyhymbuPHTJD75XI/640?wx_fmt=png&from=appmsg)

21、切换到浏览器，发现已经绕过安全验证，关闭浏览器代理，输入任意新密码即可，比如“sxf123”，点击“确定”即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trGzknCbcm7oSygYn1kklV5icAUS1gNpIiaHPZhvwLvAwI7sA3nvricuVk44lA7ibGLMcOaXCpIK8mSKym9XtARaQlrTp4kZ83ffUdQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEHkxxmgUJ9AyflITzs6xQ5zcXSnypib6FbvM1bqEPQs1HneD2pPF0dPwwMrQQmMmkBWDV9XFtVibcRaVftwtKn9HXblokicIkonU/640?wx_fmt=png&from=appmsg)

22、重置密码成功

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trE4TUNYCGO3tTWibAY2yu6YMYhDWfql1CtEnlE6lHFTibM8NO35ko7B3j2cxruFKXxm6oSzKvXgWtQGHuyoV30hK6XGibb17YXNb8/640?wx_fmt=png&from=appmsg)

23、点击“登录”，用修改的密码尝试登录，成功登录

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trHm2ZibfWQHdXAww8P9aTcSpxerzGQ9d5Hlpszyl4raO209Kec6xoIibX7Q2qYnSzWmBkYHsWY1R24bqmjIkJoL7qyGemuPj55ns/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QJTLZsy5trEKfJu1XhJLe8pZgVkP0IegwTOWXHEj2MdlpXqEMDibEhabk5wJjUBChaSHWZWQGG98IzhpiblYONKicvkHn2SrDicV5tK4GC1DZhs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QJTLZsy5trELOGm3bJpRG6390xaTczbtMZcOWrFdoPN2bWRiaWLNo4x6w8ZSjobVCKRib1uQ98R2XGcw8eY7jGDViceGZYD67YteOyMvicAQaDM/640?wx_fmt=png&from=appmsg)

## **实验总结**

通过本实验，掌握在找回密码的过程中，可以利用密码重置的常见攻击方法进行尝试，枚举用户名、抓包修改数据包、暴力破解验证码、拼接重置密码连接等方法尝试绕过安全验证，从而重置密码，登录账户。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

建哥聊安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Yxh0GAibwTaORa9r0ajicyoicMtnziaKFLwhxuibUhsBa2Wup0Frtic9OI56H3Psr3tYtxVTDQcPAUk8Oze23XAeFQoQ/0?wx_fmt=png)

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