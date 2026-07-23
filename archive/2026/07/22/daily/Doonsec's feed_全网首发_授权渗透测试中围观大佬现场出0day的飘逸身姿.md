---
title: 全网首发|授权渗透测试中围观大佬现场出0day的飘逸身姿
url: https://mp.weixin.qq.com/s/DVAMYRjIBuVf_4MJc_oYYw
source: Doonsec's feed
date: 2026-07-22
fetch_date: 2026-07-23T05:08:34.054966
---

# 全网首发|授权渗透测试中围观大佬现场出0day的飘逸身姿

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ianpxKPnLHoLKFXs1o5GduWviawDLV5NbX8dh2cj7EzgYCqDKXIJZa1aR2fbEbwbd0ibefzeeKad4Lgb1FS6h7AjRtIO1ypFdOcBiaGwoFISNy8/0?wx_fmt=jpeg)

# 全网首发|授权渗透测试中围观大佬现场出0day的飘逸身姿

zkaq-flysheep
zkaq-flysheep

掌控安全EDU

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

扫码领资料

获网安教程

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/BwqHlJ29vcrpvQG1VKMy1AQ1oVvUSeZYhLRYCeiaa3KSFkibg5xRjLlkwfIe7loMVfGuINInDQTVa4BibicW0iaTsKw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=1)

# 本文由掌控安全学院 - **flysheep 投稿**

**来****Track安全社区投稿~**

**千元稿费！还有保底奖励~（ https://bbs.zkaq.cn  **）****

在一次授权渗透测试中，有幸和一位大佬合作，目标打不进去后，通过供应链迂回攻击，拿到源码后，大佬现场审计出0day，印象非常深刻，于是把整个过程复现一下，希望给其他红队大佬做个参考借鉴。

## 缘起-常规信息搜集

在某年某月的某一天，领导突然给我们下达了渗透任务—进入某集团内网。承诺完成后带我们吃大餐，于是我们欢欢喜喜不情不愿地接受了。但是目标在网上暴露的攻击面较小，而且很多都藏在统一身份认证服务之后：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJ0SkYSiaBB3SibgCypsEY0ZaHln8ZrZzq34f9qoib5ibicrHyPC54325bYFbtSq77DkJQvakp2xZSNyTHj9YACnTpbRYV6sksAxADU/640?wx_fmt=png&from=appmsg)

既然绕不过就仔细分析下吧，发现如果输入的账号不对会回显“用户不存在”。输入的账号对，但是密码不对，会回显“密码错误”。这不就是用户名枚举漏洞吗。而且登录页面没有验证码，尝试利用burpsuite暴力破解用户名密码，万一运气好搞出来了呢也说不定啊，然而很悲催跑不出来
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIiasmjOBLFiaEKvnOsKAD8dDEtpdC15cv0Yolm6T9TFbfGWqGdZCRDlblyvaDery3riaOtpO4fibgVCKaLsiauDPpdibVjohtbv8MhA/640?wx_fmt=png&from=appmsg)

利用goby常用企业端口扫描和漏洞扫描，发现IP资产14个，开放端口7个，中间件11个，但是没有扫描出可供利用的漏洞。
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLjW43L8lGWGYy4evPGpbKcfrVe9QmgibuHYU0WD0Kut815Ab0jRdH5BG4X0vgjYCV0kydXU2t7s9E5OoQrSWElLMAX51f82PVg/640?wx_fmt=png&from=appmsg)

此外，我们还尝试了目录扫描、指纹识别等常规套路。

## 迂回-站在前人的肩膀

经过两天尝试始终没有进展，出师不利呀，这个时候请教团队的一位渗透测试前辈。他给我们提供的思路就是尝试迂回攻击。我们于是通过爱企查，分析目标的子公司。不查不知道，一查吓一跳，确实有很多子公司，这一下攻击面扩大了很多
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI0odcyXISJPhU3ibH23fuCK77kYeLRHpNH7tOmFyenHNM7QaMfW5h1LhUsPom2sngcnlLlXRKuCWKMTq8OtKJyPqacuqHQIzoQ/640?wx_fmt=png&from=appmsg)

于是接下来我们分别尝试看看这些子公司有没有薄弱点能够进入，我们最终锁定了子公司A的新闻发布站点后台：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJIGDR7ib2BfIGHG9ac1IibazP8LhJx9icFibA72MY3iaNfYiaBPtxIibvHxUma5ylksLJu0QwDPBNIENCBxbxCQjg2ICKAvzEGH3n6NM/640?wx_fmt=png&from=appmsg)

之所以想要“搞它”，是因为我们通过网络空间测绘平台fofa搜索，发现这个子公司站点存在很多的旁站：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIibvkLDdvkVQDPf37dpkF9Fblk1vIT1ic23wqkskW2xx0VsEAWibDzvzPGSRky3gADyYqQbVU6I449meIvdx12G8Oia42X7y60Z14/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLicFr0R5NPb5XXicXPwU29RticQ5xJtJO1Rj6eGO8udJevfaQd12laYJ8A9iblVxbEgXLVheMav6C5gHbFPhtu0TMwskxcqHj1sC8/640?wx_fmt=png&from=appmsg)

其中，部分站点存在列目录漏洞：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKqoETuWNicyWSe7BsxESDPRIh6upy8R8BsvXXp4oZazmCrOzjyAtP02ZxMzITUvKUTf2SBZFHYq0He7D6HiaLRAX3bSMRrpEBO8/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLyTaro3tarvsEfu5t4xSn8s47uQfibAso8jIRe6U17WHIJTYpiceuCOxI5ichw6icGtjaTwzwV43wnhmhGm67ib4X5dO139SGSmRzU/640?wx_fmt=png&from=appmsg)

经测试发现这些站点访问相应功能文件时均会报错：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoL6mpuhuX98pt9GRAv8Dn6A6eXafXmrIlDDriawcWY6XsfYcxLlkT1gtm0fy9D9p55iaBgkm1h6wlr17KlyWzWSDMjnx7WBxDzJY/640?wx_fmt=png&from=appmsg)

猜测已被废弃，其中/AdminControlPanel/upfile.php可正常访问：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJBiatiaa6go6ibfIrtLKjbNMcpMSXf4fj8MlPo1TibdvbY6tRsJUgr6FNEeUHb9oFBuOYm9eV2rTErBL0r6KUx0LAMicMbVQmJIt60/640?wx_fmt=png&from=appmsg)

但上传后无结果回显，我们把目前掌握的绕过文件上传校验的方法都试了一遍，各种无效，严重怀疑后台的页面也许压根就没有正常运行。尝试了很久本来打算放弃了，上了个厕所回来后突然来了灵感，峰回路转了。通过对站点下文件检查，发现一处异常文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJz3pSzUZibeEkVX1ly2jbf7Jibm7K1LYsDmxU0AxrUpiafQOjxDeXibAuvFhekqyIZ3Ek5BcT7YutRxL0HvCOrMd3A1Z44LpL3NJQ/640?wx_fmt=png&from=appmsg)

代码逻辑翻译后即为：

TQ5r29v() -> return “assert”
参数1 -> $\_POST[‘z’]
Hu3eT对象销毁后调用 TQ5r29v()(参数1)，即assert($\_POST[‘z’])
明显为恶意文件，这时发现目录下存在多个类似文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLfXq1QlaNiblmQWG6LUJ2VVvd39F4E4xYicjWLft4pDzcyrtyyNnbWcm35RF14WSYP19ERdibu3aoh3u2U1sCh3IMmCfV2j86K7Y/640?wx_fmt=png&from=appmsg)

其中部分为正常文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoLqegibU7whXwPoGE0zOcxrQibDib5qeZXvvYNG7icytdgBlbaeu6fhbmRgfWCwGmWcdbNmicXCXzQbItN90C38cf2uQcC9eRrSdTdc/640?wx_fmt=png&from=appmsg)

猜测为long long ago的攻击者隐藏恶意文件构造相似文件名，部分文件返回 404 file not found !!：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKImXSAdwx2ea1zY7Np5CabqmNwqIIXFYibg39dOc9llP3euE4wS8XlD9iaWrRNJ9OmSbXUb26HOWKWYSe3ia7rOF8FTFThqMFEG8/640?wx_fmt=png&from=appmsg)

牛顿站在前人的肩膀发现了三大定律，我们站在前人的肩膀要拿到shell了么？但是一切也没有这么顺利的，直接传入z参数无回显。猜测代码逻辑没变，构造字典fuzz，发现传入参数为U时成功执行代码：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJLjFPplwibicaibSLMfibnvicBHIiaQeZSOYbA5Dc3vzGn9ic9tCRiaTqEcH9Zt8gh2xpPbWxPP5WF5O1I3yVEsDHiaeaqkfSLU9iczBXvg/640?wx_fmt=png&from=appmsg)
激动人心的时刻到来啦，掏出我的哥斯拉连接之，最终获取主机管理员权限，哈哈哈！！！
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoK8eyszqOpHA0RFz3Zjmmn4wTwqO2fAsAFiaCSZicx4egyxrxRIgeGz7uzd88aA5hSib2n0yicZiahXianLQY7FYc9YWQ2YbiawRP8FsE/640?wx_fmt=png&from=appmsg)
接下来就是翻找目录，看看有没有什么有用的东西。发现该主机搭载多台应用：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIOYPKyjdpg00NJgrFJ3fouPUO9TkjkpJrpichv2s6qYCNuRjy7lKic5JaPTNAseUUw41ic7UlkALEstxdibyGcdeic2JAMCRWKicz30/640?wx_fmt=png&from=appmsg)
查找发现子公司官网对应目录：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoImL291QuA1jIb6tuHiaUcQ5j8sFlSh0wfyVsohAJw7AsguX1s04Bm7Zt2PodsfhLzKIQCGCSuSUnWxxeibPSTEFC2JibLIaARVK8/640?wx_fmt=png&from=appmsg)

查看数据库配置文件：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoIFny6OQCU1fHcBaACjZ5vuwGYCIjIiaGmFTU9qXk2qfJ9J4ticwibdicLvZhxW6njgOQI3dhFribKMvWp0TpEVvptSx9IAOPn8UBQ0/640?wx_fmt=png&from=appmsg)
连接可获取数据库管理员权限，查找到管理员用户信息：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJTz9R7dpbISM6yianUqNcQR11IsRmFfmG8t2g68X0ibwSbJTBFeVUJnM02YzoUZxfGNdx9pxWVkZd1bBcCgjEYeNluYRgUPYnGI/640?wx_fmt=png&from=appmsg)

## 波折-加密逻辑破解姿势

但是上述密码是被未知算法加密的，直接放到各种解密工具下都是乱码。关键时刻，前辈再次出手了，只见他大手一挥，就下载了网站源文件。然后利用神器dnspy反编译查看代码，通过关键字查找迅速定位到登录操作：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJgTk4W7Qx5jyZVgf9tI3GgK7uC8vQPiaSpve8Zia0wKlKuPjP2BTw81oL6xZxZmqeLXaZicicpwOo1vwEvOBfSDOURmg3fse0ZZS4/640?wx_fmt=png&from=appmsg)
进入GetModel函数体中发现里面有加密函数Encrypt，然后跟进Encrypt函数中看看函数的详细逻辑，主要是DES加密，带盐的，总结其算法就是md5(md5($pass).$salt);VB;DZ知道了算法我们就可以随便解开密码了：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoLaiaFnzu4MLXiczuzc9gETBOJUwtdczJGFtkCV9VToial5hhUWicSVL35yc2g6wZ1RXeeYL3iauATEbxuWP1ia0eNuZN5apAaNz79iaE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIeFakHfQfibib6JNwldbaVBrM4XsGib6icfj10FcFGCibM4J0icPaLCBGAlzMGkLls030ouNL10DxLcAfI92PQWwwNibjbVFiaJdb2U3o/640?wx_fmt=png&from=appmsg)
手动添加测试函数：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoKibyoLId4z8Ay38nQaGD3n0VvLMX8rmSoAsM6QRsicODE2eKt2m3bbnoVDicyTPib4tsGM29NDH3MqicW8a9vWQ4kLibujbdKHNB6Po/640?wx_fmt=png&from=appmsg)
修改为Console类型并设置入口点为Test.Main：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoJGA3ZAdR31AC0pdOUbJg9tQVoiaia17XnVbJgZlgCpMUgunnzGfw7lWZibVLT4piaF4xbkwFbgNDicQBdouCxbjHnV0NmgxHCj8Fuk/640?wx_fmt=png&from=appmsg)
保存后可解密出管理员明文密码：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoIjCJ37o5pWMMfgtI6qKfsMvfhHZLIt7o2GmUjSeJ0R08UFXeFGEiaLpVbjUVSmic0GR14KAVY0iatpfJich3GZa1LrLbbUCpoia7do/640?wx_fmt=png&from=appmsg)
登录网站后台可以证明确实是管理员权限，解密是成功的：
![](https://mmbiz.qpic.cn/mmbiz_png/ianpxKPnLHoKxJ8wdoUiayQqxvaCQGJOuiaicydVibRKBqRzFfwP56SCYMJ6oJ2xzWKph2QWpnAK8hcxvzSCYS8QnlVTnicNEia5n5kvMfG39fnjzs/640?wx_fmt=png&from=appmsg)

## 终章-不忘初心

万万没想到的是，我们在网站目录翻找的过程中，居然也发现了母公司官网对应目录：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoI7gerUOFk6EjulaaPholbQiaUiaQQsKkbfSxuMMhfPSzugGbtZ9HSLOhwv3vLz0GDxv4O6jiaurV6GWOibK1OM21MHOMUL4Cxjic44/640?wx_fmt=png&from=appmsg)
于是我们如法炮制，查看母公司网站数据库配置文件：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoJEbfxXkiaoTvIQmdwKEFAEsmRlz2ywgcg7Mf1vpzfP6BuT7SichLiaEoKicYe43TJVAeiaHwvEFUJmnLA1q5IpnRFt9Mls97pHRUb8/640?wx_fmt=png&from=appmsg)
可获取数据库管理员权限：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ianpxKPnLHoL7sWZfPjpiclygKZ3gicbwibCwIZ2ZUyMnYK2mATrhibv1RqqC8BE...