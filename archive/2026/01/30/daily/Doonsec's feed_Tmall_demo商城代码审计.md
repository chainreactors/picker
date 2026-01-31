---
title: Tmall_demo商城代码审计
url: https://mp.weixin.qq.com/s/6bMHsjV5ubCPfc8UNXZ18g
source: Doonsec's feed
date: 2026-01-30
fetch_date: 2026-01-31T04:01:35.831319
---

# Tmall_demo商城代码审计

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7nIrJAgaibicOhLOZahllxlxckCPZpuyroubOqUdkkDpnfJWziaYS6DWviaeREFvfthDSkPTjoCObSrTwmOhxV4oUw/0?wx_fmt=jpeg)

# Tmall\_demo商城代码审计

原创

时针
时针

船山信安

![]()

在小说阅读器中沉浸阅读

# 与作者沟通过可发布他的作品并标注原创，原文连接：https://xz.aliyun.com/news/19037

# 环境搭建

项目地址：https://gitee.com/project\_team/Tmall\_demo

修改src/main/resources/application.properties中的对应数据库配置信息，创建对应数据库，导入sql文件。

jdk版本1.8

前台地址：http://127.0.0.1:8080/tmall

后台地址：http://127.0.0.1:8080/tmall/admin

后台管理员账户密码：admin/123456

如果登录后台出现500，系统错误的提示，可以将src/main/resources/mybatis/mapper/ProductMapper.xml中的最后一条select语句改成如下即可

```
 <select id="selectTotalByGroupCategory" resultType="map">        SELECT category.category_name name, COUNT(0) value        FROM product        LEFT JOIN category ON category.category_id = product.product_category_id        GROUP BY category.category_id, category.category_name        ORDER BY category.category_id    </select>
```

# 代码审计

## 鉴权绕过

在pom.xml中没有发现jwt或者shiro之类的鉴权关键字，看一下目录结构是否有filter或者Interceptor

可以看到存在filter，里面只有一个鉴权文件

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrowicWnuRBicHOCiaA0cpJy609Nz4t04nuicusKMWTCRtODibcxacUaTGCC4g/640?wx_fmt=png&from=appmsg)

里面只有一段，可以看到这里，只有url中包含`/admin/login`或`/admin/account`即可直接放行，绕过鉴权。

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrouQeoCADznY0GIaO03AjT9wCSpibnD9nfLV4fosFL6LDRyxQmokpRn8A/640?wx_fmt=png&from=appmsg)

在后台找个需要登录才能查看的功能点

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroOdibn0zzRI7icRS24WMQ0yAXicdFq9lVibxnSX8POQQ84AnmlPE2L1qKzQ/640?wx_fmt=png&from=appmsg)

抓包看一下

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyro6bSCPYJKBNY9xicgiafLYkHEzOEB2QyZaJs9defVOMarZCgQv1cg4tGw/640?wx_fmt=png&from=appmsg)

接着我们退出登录，可以看到直接访问是无法查看人员信息的

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroQ8uMIUhbiaPhfcqjWGE6P80Vk5HzFdWdia2f0zeqx8jorkHibMRDLUfTw/640?wx_fmt=png&from=appmsg)

在前面加上/admin/login或/admin/account结合目录穿越即可绕过鉴权

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroHAB8CvYqaGcy1NUVSoJ2FZoL2emyIKcwC1TqUhMMTeVG4HrXjZ8AiaA/640?wx_fmt=png&from=appmsg)

## 前台文件上传

在前台个人资料处的头像上传功能存在文件上传。

在前端校验文件后缀，可以看到使用了uploadImage函数，

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrocibHJDhLiaCHP4uxA2B7c4kHI227MBCBiaNqRHZVtT4N737P2SjbibvEwg/640?wx_fmt=png&from=appmsg)

在js中搜一下这个函数，可以看到只校验了MIME类型和大小

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroXFXoVEibFb5xnAMs5ib6MicaZiaIsN5svU6ZP95l7BBqZT4MibXIsYYdaWg/640?wx_fmt=png&from=appmsg)

哥斯拉生成个jsp马，后缀改成png，抓包之后再改成jsp即可。

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroicarxugMN0t6UeeE5J3icKfmtBPgfcXib4zBBLNASCBAFN41ZQINUm3nQ/640?wx_fmt=png&from=appmsg)

抓包可以看到对应的路由为`/user/uploadUserHeadImage`，去源码里全局搜索一下，发现没有对文件进行检测过滤，只是对文件名进行了uuid编码，并且也给了文件路径，也会返回文件名。

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroXgyUM7AR6UxGNMPvy0PEAwPbuRy59CuzDgRD3fsp7DuCFIFqteSuAQ/640?wx_fmt=png&from=appmsg)

在pom.xml文件中也可以看到有jsp解析依赖，传马也能解析。

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrofnqfVvJdPDnrW0jw3X0MNYTYPxiaT3Ze8Ymaw8eBgyvB1iajfI7RsHkg/640?wx_fmt=png&from=appmsg)

在前台查看头像地址，再拼接jsp马即可。

```
http://localhost:8080/tmall/res/images/item/userProfilePicture/ac5f3dcf-b85f-4360-b610-59bdbcfcb455.jsp
```

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroKagN55GIPrKQNLeRAO1cdCicyDZMvZQeBIto2xlYUVRkmHIR2xM76aQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroB0WnnJyb18VNF5HeibVdJKEhwPCicBly6BeEx9Iaac14Qg8aoCZMp2Lw/640?wx_fmt=png&from=appmsg)

## 多处sql注入

翻一下pom.xml，可以看到使用了Mybatis，那么大概率会使用

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrosu5sjhECb3qxsuz5QYF5MxeT4tYdRAxFc8fdWoUA8avxj7gZqHt8KA/640?wx_fmt=png&from=appmsg)

直接全局搜`${`，可以看到好几处都是使用`orderUtil.orderBy`这个参数，随便找一个跟进去看一下

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroIMO8oG9QOvUcYOibnslJcSxDdnG92LIffegdwJMhiczDVEwJrVoibQh1Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrolibicDFWDMkdZ2bsAcXWkzlCzY0ficE2BNksPORcPQe8DavkiaosOGMnGQ/640?wx_fmt=png&from=appmsg)

搜索一下orderUtil类，这里有两个OrderUtil方法，第一个没有引用，看第二个的使用

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyromglibchr0cF9W11ZyxPzDdPX8VcjfvUylTyiaPI15VxCq26S3sxichRmw/640?wx_fmt=png&from=appmsg)

优先看一下orderBy参数是否可控，看一下使用

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroSiaD8j86dmn3z4auiaJsyus4NopJkzj1cmOj0pn1RB27sEP5LvmGRxpw/640?wx_fmt=png&from=appmsg)

这里跟进第二条看一下，可以看到参数是orderBy，通过get方法获取参数，也是可控的。（其他几条也和这种类似）

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyrobtMaqeVt41rvNs2hWzKlHbPTo15nmKWpdCC39DyT0ZfUw85axr1Ttg/640?wx_fmt=png&from=appmsg)

在查询订单这里搜索

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroW3SHEg1Qdcia73tvsW39j1737wVXC7ic1iaW9oljLX7HEJyD95getLTTw/640?wx_fmt=png&from=appmsg)

可抓到下面这个包，并且有orderBy参数

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroKY4eSc3qIkicQS10VzSyB0nuUZicJwvSKE2mwvfuo62EJdiahGZnVJkDA/640?wx_fmt=png&from=appmsg)

直接sqlmap一把梭哈

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroUsc4X45HgricArtMwm5VMfAvhDxXn0AcncoXhZwTGxWlEpBl2xdZ9icQ/640?wx_fmt=png&from=appmsg)

同样的`admin/product/{index}/{count}`、`admin/user/{index}/{count}`、`admin/reward/{index}/{count}`、`product/{index}/{count}`路由也一样存在sql注入

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroNtTS3eSoXqVCIC2GD4yKJbtjBVf5YaBdRfnG1Ric4r7icHYTicviaXVYQw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyro5Dlc09EAM5eRDfK3OujEdlCvHFwa9ATpibb0t0Wj6sGHIwyzD1bJGhg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroo13oEIn3PUgMibNhVX0Ho29h5jfDsQUI4zVlqZTOjySOWAobd7nQGJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroNUp0MrD4GrtPpoaRKCCMoUTR4eA4ia68jZft5aTibaVHan7xXJlQMVYw/640?wx_fmt=png&from=appmsg)

## 多处xss

### 所有产品处

添加商品这里见框就插

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroZqCAkstm5CyiafGZyoueOlb14ZN2HhuGEkjQIUUkPEiaFD4YxA44ul9g/640?wx_fmt=png&from=appmsg)

然后搜搜产品名称`<script>alert(1)</script>`即可弹出多个xss弹窗

### 前台下单/后台查询订单处

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroTO5JTwKsWAXfprkXdlozarOicXXL46MXpLj2QFgV7Fl3SyjUMSOtsYQ/640?wx_fmt=png&from=appmsg)

提交订单即可弹出xss弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroLjfKRk5Dk7Spc6x0vtOtl6zheZ8aAl5XLKaMDIeFTxzQDyWIZ99VeA/640?wx_fmt=png&from=appmsg)

后台在全部订单这里查看刚刚的订单详情，也会弹窗

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroXHtuWB0XvxejfMyibPGguomtpr1Bd1gTkPGV7fN5bsf1NSz54ZuI7hQ/640?wx_fmt=png&from=appmsg)

### 管理员昵称处

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroYEe52Diaohq9pO5oHMBXBB2x0kVCZdYGicuS0NczF9euibYPna2zQ0HgA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicOhLOZahllxlxckCPZpuyroLaZwKjR8HYYhEhs7w9VYQtKlib23sqN9hUU1SCclTgiaeA2IugprkwrQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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