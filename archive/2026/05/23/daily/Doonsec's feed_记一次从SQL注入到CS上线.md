---
title: 记一次从SQL注入到CS上线
url: https://mp.weixin.qq.com/s/berzNgMu5OWHwFoWJfUG5w
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:59:04.610754
---

# 记一次从SQL注入到CS上线

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3os73wAPEibO9OPqVqhbX5PyxeYe0ou4t4SqgN1yicdnJF9C0IXNROiaia1EJtqZTeArgRJUdcM5AEJOdnFiczmWFpXVbO7icZo0ibODoYdW8zCpNk/0?wx_fmt=jpeg)

# 记一次从SQL注入到CS上线

原创

破阵攻防实验室
破阵攻防实验室

破阵攻防实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**免责声明**

    由于传播、利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人承担，破阵攻防实验室及文章作者不承担任何责任。如有侵权烦请告知，我们将立即删除相关内容并致歉。请遵守《中华人民共和国个人信息保护法》、《中华人民共和国网络安全法》等相关法律法规。

正文

---

某站点存在SQL注入漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibMhx0zbPG3N47j9Olxv47KQmiab4DtMwIrVlZGG7rUabYMyvqZrl03TjzdCLFU8FlMT7c7be0bg8wXubUojAYokX4H6bJwj4Hicc/640?wx_fmt=png&from=appmsg)

利用查询语法获取所有的表、字段内容，没有可利用的数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibPdKwVuuuNB0Ubu3D79brXpMcwvX4Sk7a4ONXHmphHARlliah8FpAHHhf0EnVnPLQgKtZeicaJb7cNGKk023yGBAT09oZFFRTaJQ/640?wx_fmt=png&from=appmsg)

查看操作系统信息，Windows x64系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibMv6Zcrlj8v7pMVplzQDxy1Rcj3KYgWEtNFaCdTseFOtKueZuk635rcsUsBHNDdnXCqEEC1b9SStAkAs2XAw3ibhIHGxa6FAWgA/640?wx_fmt=png&from=appmsg)

检查是否具备FILE权限

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibPz417D5SFhBjrzDhfKGkBiavgF03VavxShmSzYz72sxBJhhufRhEosuPX5DSObHA9KJf8ohribhtmHfmFicN5VUicSibqrtak8CibRI/640?wx_fmt=png&from=appmsg)

具备FILE权限，接下来检查是否存在路径限制

查询语句返回结果为NULL => 没有路径限制

![](https://mmbiz.qpic.cn/mmbiz_png/3os73wAPEibNcnj3EmfOCuVWTehOia7WUBzmPIhf3rZ6Ulw1ndFIa0FKYjp8cWtIVMVnOvHzWqfEp5m2JSib8NtfAQU4ysVlRLbjC52GImzceI/640?wx_fmt=png&from=appmsg)

根据响应包中的X-Powered-By字段可知，这应该是一个ASP.NET，而大部分ASP.NET是运行在IIS上的，IIS的全局配置文件 applicationHost.config默认位置在C:\Windows\System32\inetsrv\config\目录下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibOMmlFAM0e8oKJ3qfAXPfNCN2Cg8tkl5W6o8HRvs7Q3CJlkXp1IKXlLqFx4F39uibKrbHCn2r1PjTe6HJVoiaMPibPLIsH3tKic7RM/640?wx_fmt=png&from=appmsg)

读取applicationHost.config文件内容

```
deviceId=1' and updatexml(1,concat(0x7e,(SELECT substring(LOAD_FILE('C:/Windows/System32/inetsrv/config/applicationHost.config'),1,30)),0x7e),1) || '1'='1
```

根据协议和端口号定位到对于的项目目录

![](https://mmbiz.qpic.cn/mmbiz_png/3os73wAPEibNjjECEe5p9q2KGMIiayCQ01tO9VWb78u2wAf79PcicfMVrbDd7qmLC8kvITjnne6ccw5W7zNY1icVKIkdrjuzqTT5WQx4NSSBpBc/640?wx_fmt=png&from=appmsg)

目前可利用信息：拥有FILE权限、已知Web服务目录位置

接下来可利用SQLMap getshell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibMZPdBwQgp5XBHUDeiaWDCKW6QsyqatRGSdlNR1XNm6cIQAOPvNCYoM2COYVeTjgTBT3J1MEicz0dxzBA8FL1v3PTLnwWkia21ZdQ/640?wx_fmt=png&from=appmsg)

在VPS中启动CS并生成反向马，然后利用SQLMap os-shell执行命令将目标主机上线到CS

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibNSmOBjsbHmjSEfnuJtsLaoumxuCyZMCI21MZic8Jo91MOhOJBN7h0Dh3uwId5OxvvQNIVm6JOrdKmnm68IHkBKNia70GicufUS0M/640?wx_fmt=png&from=appmsg)

运行反向马

![](https://mmbiz.qpic.cn/mmbiz_png/3os73wAPEibMvyrjGEokrF5gYn2NiaPUticqJOxRSQeIHvfWor9JKH4icn4ox8IQiaXBrGSuOlXJKvt9gHRQWVlUEmuTvxch3f905USZdk8J3p0k/640?wx_fmt=png&from=appmsg)

成功上线到CS

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibM08jTVaog8hcrtwricEWKSRYvowJQdtqGJgvrXHb1NWWvX0LZ9gJ5GXnHzZjvQczpQYvEHI4clENROYvrekaI3sgZmA4H2J9CQ/640?wx_fmt=png&from=appmsg)

非Administrator、System权限

![](https://mmbiz.qpic.cn/mmbiz_png/3os73wAPEibMicEkPfE6ibDyJM9aQibU1csortfHHdgz8d2boMxBROw1nFkBTuyDsgiaD913t573lR4aZqTuoKCwyYZ0Q9CsSwyyyKBOaiciaLhfh0/640?wx_fmt=png&from=appmsg)

利用MS17-075提权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibOlZqX2ApiaqN9IAWbbyLXoCvplKribeShvqImscxypMGnduHjtibHsFe4VlsJkMqfSkYeGjNUsXPHYxzzXbOH7xxDSXucuicx066U/640?wx_fmt=png&from=appmsg)

提权成功~

![](https://mmbiz.qpic.cn/mmbiz_png/3os73wAPEibNkMkz3o9uC3fSKhiaCKwSicLur01eKPlDW24VicNcDWOBQRPSjHc0w67rt1kVx9FQ3nnFSwLU3JjzkyvpcXJSSnvt1XLhajtD4Wo/640?wx_fmt=png&from=appmsg)

传统渗透，点到为止，后续操作你们也不爱看，就不展示了，撤了~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3os73wAPEibMYIBlyQMzLZVVTy1B9ZrCtbniaMRyyVzFVKrclAnDuKv8d9LbcrHvSS49YeDbdKqNNqE252zUwqT5LgoWACdQQ7z6W51QxK4SY/640?wx_fmt=png&from=appmsg)

如果想要及时了解更多内容，请关注 破阵攻防实验室 微信公众号！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKozqgsbT6t325m2vibAic6Pkoqd62VXGvK85icMpFZJo3h9Mja7UmeicHqETThOJbicKwLku1XzhngqM8A/0?wx_fmt=png)

破阵攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/fo3OZEF1OKozqgsbT6t325m2vibAic6Pkoqd62VXGvK85icMpFZJo3h9Mja7UmeicHqETThOJbicKwLku1XzhngqM8A/0?wx_fmt=png)

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