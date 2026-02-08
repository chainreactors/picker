---
title: 破阵阁・网安淬锋巅峰赛 应急响应WP
url: https://mp.weixin.qq.com/s/mDD4zIuId5yySSvPxhFQoA
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:19.797490
---

# 破阵阁・网安淬锋巅峰赛 应急响应WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/A79OztZnWVnFmHpqCUfIIiafyk4hT7O7kkNxs07r2eOna1qnyw3iaJx6CBcHMrofpteRNINZ7rUQc1YxWW63uPHSsmWxpXibLjuicoILySxTn6g/0?wx_fmt=jpeg)

# 破阵阁・网安淬锋巅峰赛 应急响应WP

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

# 应急拯救计划：隐匿潜袭

攻击者手法全面升级，在Tomcat服务器中留下了更深层的后门。请彻底排查所有入侵痕迹，只有完美清除所有后门，才能获取最终的flag！

```
账号 root
密码 idgfxuxvr2tqekhz
```

## Tomcat后门程序

先通过netstat命令来查看一下java进程

```
netstat -anptu
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn8cnXtMpX4kKqDY1ic9wDKka7icnwHeEZH4iaDfYm21lmuaxzMdR9BryBWAibs3Rjz7cxJPsnuwicy5MKM3nr83lkr8gggnYVnr9qE/640?wx_fmt=png&from=appmsg)

tomcat放到了/var/crash目录下。这个程序刚刚异常退出了（Exit 1），crash是崩溃转储目录，很奇怪。

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkPE4WYrib8PIq4E34cxlMGnXzkyycnY4btwg5sxP8HkkFEGeHmC79rj1xF7Ls08VEW3nibQibC33j8A9ibe36qDbuk7xzANshicqCE/640?wx_fmt=png&from=appmsg)![fig:](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmzH32DSIMrcEOeiax9zk0CxIlL8rGqqfMp7VhmTZHbC9Xo793Sukw5wqu1CGJjXicMXjgEibKElKyToTyR7CSQPJBEu11RgIIZYk/640?wx_fmt=png&from=appmsg)

看到tomcat的文件头是elf可执行文件，确定这就是后门程序

```
rm -rf tomcat
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVkCdcRPM6UH6jmcaPVMoiauXqBhibP53Tzr63VPqupO2l0M89OJRYicTNMibnzicjWNPPaeHnbgd2NDJOTbDVX8zgSVQ3nM2ovjKC70/640?wx_fmt=png&from=appmsg)

profile文件是当我们登陆shell时自动运行的文件。

profile文件中也有后门静默运行的命令痕迹，清除掉

```
vim /etc/profile
```

## 后门持久化文件检查

![fig:](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmu5ic9tfVibZwL4b1QeGt1xI4fzhEmexcCMoxict2b3dUEr5Qndx8u7bq2Zp4kNicFYHx6yfJ0R2jKpvFEL9GxB7BVc6FU190PHMs/640?wx_fmt=png&from=appmsg)

清除持久化

```
crontab -r
```

## 内存马清除

![fig:](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmuA6zAlSHnROsbsGmIylSmY9qNKvRNuibTMDNCJSYkGQxjVDljGMguMffGg6zic4K30ibLKlezj3GW2kTYEOPiakGISDX7cxUKH3M/640?wx_fmt=png&from=appmsg)

a命名的可疑目录

```
find /opt/apache-tomcat-8.5.100/webapps
```

![fig:](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVkpRSvco9jsLMmj8AHDDN0X1IygH4qGcrdQZZXsYoXbsp9s0qaiaDibiamw0MJ8Qian18STiaJ00gToeVedTnODsZ4jIV54ibZDvEzzI/640?wx_fmt=png&from=appmsg)

login.jsp没有内容？怀疑是内存马落脚点，源码被清空但编译类仍在。

找到编译后的落脚点：

```
/opt/apache-tomcat-8.5.100/work/Catalina/localhost/a/org/apache/jsp/login_jsp.java
# 编译残留在work目录
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVn5NdhiaWribbFJZdiamHCgHCWe2hnd6wSAS25FYGWxHlbLGteEArQH8hy2uUdwicS3iatLgtmoOBM9F1gIyHG9XP5QqqrkSWfmy1Xk/640?wx_fmt=png&from=appmsg)

定位后门位置

典型的 **JSP/Servlet “类加载器后门（字节码马）”**：攻击者发一个参数，服务端把它当成 Java 类加载进 JVM，然后把 request/response 传进去执行。

```
rm -rf /opt/apache-tomcat-8.5.100/work/Catalina/localhost/a/
rm -rf /opt/apache-tomcat-8.5.100/webapps/a
rm -rf /opt/apache-tomcat-8.5.100/webapps/examples/login.jsp
# examples/login.jsp 同样也是后门落脚点
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVlU4x5nicHDBLcYt95GxCQL48zWnLrmWfYfNKYDgCCdMS0ZKcBj0MXCBf8RGVcl6BuORkUKGL5p0LF6iaKqBlR2K2mhocQ5Oa9ew/640?wx_fmt=png&from=appmsg)

```
vim /opt/apache-tomcat-8.5.100/webapps/manager/META-INF/context.xml
```

^.\*$ 等于允许任意来源IP访问manager，这是后门化配置，正常应只允许本地访问，manager 文件被篡改

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmCGic8JYhuSmQHq5tEjwAruLC0Wb4gibSWUnIGu96jApmQb73jASB5NJicYVC00gtpWYzGKia7fZuzQNRyblCibjibMiaib9zBDpAcvJ8/640?wx_fmt=png&from=appmsg)

## 后门用户清除

![fig:](https://mmbiz.qpic.cn/mmbiz_png/A79OztZnWVmSJQH5iah3icNwlGPe9AxJzhGxRBfaictxosC4XdSVTp2NRUmGxvvq30s3DcMFmZoCFACE0hFIb9tmuwhAGLjvdVpYwZfW1XfbX4/640?wx_fmt=png&from=appmsg)

发现dev的所属组和root所属组一致，相当于dev的权限等同于root，怀疑是后门用户，删除掉

```
sed -i '/^dev:/d' /etc/passwd
sed -i '/^dev:/d' /etc/shadow
sed -i '/^dev:/d' /etc/group
sed -i '/^dev:/d' /etc/gshadow
```

![fig:](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVmJK9ibic1J7kxg7xn60IOxHuFrvXB3TNskqics5u4y9QZBEu03Nic9enErqOEYjvd0iarMmDPh6T60wtyUCVStgxJBVaw7KOAKsfdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/A79OztZnWVnmPMsf0GvPf6DJicIHg3UY9M3Oje8v5vJcqXIFibNKGWcF4dboelvvx16Wx3pbgWlKKya7qtocgBiboK1Ma1AGiau5VXkP5P8Een8/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

云晞科技Sec

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNOexrWpDgDYXpYTLbLrl7RhtCuwTAdmvLKiaF0kN9rgKnvsq0GYhnCY3w34I63n5U9ocibeG87eFCqg/0?wx_fmt=png)

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