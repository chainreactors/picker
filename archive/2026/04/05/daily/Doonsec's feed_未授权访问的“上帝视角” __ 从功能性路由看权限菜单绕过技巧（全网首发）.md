---
title: 未授权访问的“上帝视角” || 从功能性路由看权限菜单绕过技巧（全网首发）
url: https://mp.weixin.qq.com/s/mcWvFIB28e4BJbgLP2NJDg
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:38:37.985526
---

# 未授权访问的“上帝视角” || 从功能性路由看权限菜单绕过技巧（全网首发）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9chXicZO71s5VCJU2j9Wld8qCtjLml12bqiamWmsWxGrqErbhKFozqL0YGyyHaia94U2NibjFhmFlTiaFGdTBwN7vlXic94CDouoSMNA3M1RZ60Io/0?wx_fmt=jpeg)

# 未授权访问的“上帝视角” || 从功能性路由看权限菜单绕过技巧（全网首发）

进击的HACK

![]()

在小说阅读器中沉浸阅读

编者荐语：

好文推荐

以下文章来源于Daylight庆尘
，作者庆尘

![](http://wx.qlogo.cn/mmhead/OM4v0FU2h0s97hBneksdKoudzI5qAtzW7vQkBZYfJUTGnoBob4kroP77siaBiapntIBYJ6PKDaXbQ/0)

**Daylight庆尘**
.

专注于代码审计与企业SRC漏洞挖掘思路与案例分享，想了解SRC漏洞挖掘培训的可以联系我，本人亲带

很久没发技术文了，今天继续给大家讲一下未授权的场景渗透技巧，以下手法基本可覆盖95%以上的测试场景，希望对师傅们挖洞有所帮助

![](https://mmbiz.qpic.cn/mmbiz_png/mYa0sCia1qwCvHOMJjG9CpYS2Dxg4BTswGyYqHicBiblUPjYtNVRRV8FfvmjHGrv2QDbXSTonQI2cxWbClolxgR1Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/zG8IRvK3Jv7v7KkHWz3icB3KyTibM5FHc8agmPbXe6JmlEBp8DaAicJnXP6uGW3ib9GC27vCvuiadzB0wiaticmUqWAUQ/640)

注：下文均为个人自总结内容，其中的很多命名，思路之类的名词，都是讲课教学方便自己起的，切勿较真，内容纯为个人见解，欢迎各位师傅交流

![](https://mmbiz.qpic.cn/mmbiz_png/1DVZP48AYchdT255kFMRWTzyhjz4G7gCkibZoIZzGyRL8tC8TmnwMNRXvnQzXIQfpXicBhryMc8v4iczz9jcOKVTA/640)

![](https://mmbiz.qpic.cn/mmbiz_png/O8ibmtKwBdw2y81ibxiaccicUBbaVmPQtu2EYiaUDwicb704E6QHad6o5oJhLeibDSMewvakJR9UNJ43ibibLCyYeAkWZVA/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icK836swLHcwv06xdgiciaePbs85RyQiceibNhgtGvGoRv2pOXX0wqtvNjPia8qANBibTzu2OjhFHprrgBPnzCicbP5HSBcwvhjlNicmabwqFTNa92NA/640?from=appmsg)

引言

        在我给学员们讲课时，未授权的路由测试流程中一个非常重要的点就是权限菜单，为了方便学员们理解，我将路由分为页面性路由和功能性路由

       师傅们所熟知的最简单一类未授权，通过Findsomething拼接页面路由，直接进后台页面，这里的页面路径，我就将他归为页面性路由的一种，师傅们可以简单理解为隐藏起来的页面，这个页面性路由后面我们可以单独出一篇文章来讲解，但今天我们的重点是——功能性路由

那怎么理解功能性路由，其实说句大白话，就是隐藏起来的功能

        比如某个平台有管理员，有普通用户，有商家，有供应商，首先每个角色进入平台后，平台显示的功能肯定是不一样的，比如这个平台，普通用户进入时，页面如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s5uk1AQXmeel5zrqh3RAJp250pGqc0nXibQwFicDhxdARktialSNNX8ReudsLQuH9VNqZDo4Wydx8J7ic2p0f6SISXWaEQVxsDibibNU/640?wx_fmt=png&from=appmsg)

而管理员用户进入时，页面如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s63wXwWX5UcCHMEGmMmBveyC81icVQUh5zL2OGQZehAuBHbIdz5H24gsiccVkOP9dPiafbjARqZenLgf1XpkZJ9b412pZYYZds8cQ/640?wx_fmt=png&from=appmsg)

可以看到很明显管理员的左侧多了几个功能点

那么同一个站点，同一个页面，同一个登录口，前端是依据什么来判断该如何渲染页面呢，自然就是后端响应中的参数，而这里后端响应中的参数，就是我们今天讲的，权限菜单，权限菜单简单来说就是根据登录用户的身份，动态展示其有权访问的功能模块导航的机制

       首先在讲之前，我将权限菜单分为5种，这五种在我的测试生涯中，能够覆盖到99%的场景，，我将这五种场景分别命名为全开放，半开放，0开放，特殊类型半开放，以及特殊类型0开放

*1*

全开放

全开放指在响应包的权限菜单中，权限菜单将所有菜单都回显了出来

    假设某个站总共只有四个路由页面，分别是首页，信控优化，信控大屏，账号管理，普通用户登录后，网站加载的第一个数据包用于获取用户信息，响应如下

加载之后普通用户发现页面左侧只有一个首页，其他啥都没有

```
200xxxx{  "id":1,"name":"庆尘","menus":[{    {       title: "首页",       "url":"/index",       "isshow":"1"    },    {       title: "信控优化",       "url":"/controlOptimization"       "isshow":"0"    },    {      "title":"信控大屏",      "url":"/signalScreen"      "isshow":"0"    },     {      "title":"账号管理""url":"/accountAccess""isshow":"0"    }  ],  "sex":1  xxxx}
```

        这种怎么让前端把所有功能点都渲染出来呢，直接修改isshow为1就可以了，这种对于我们挖未授权来讲是最方便的，也是最简单的一种权限菜单

     当然参数不一定是isshow，比如下图的display之类的，实际碰到时师傅们自己举一反三就行

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s7cluuiaTP8GQmmOL1gzaJSZLIXEznJ5HcEn6n0iceZA0zZjENuT5xiaibbicUQh6ylPk6pF22nqHcXVw6ia11XEL4ryM410UHXKJ2ia4/640?wx_fmt=png&from=appmsg)

*2*

半开放

半开放也比较容易理解，就是返回的权限菜单中，只将你有权限的菜单返回了出来，比如还是刚才那个场景，但这次普通用户进入网站的之后，返回的权限菜单如下

```
200xxxx{  "id":1,"name":"庆尘","menus":[{    {        title: "首页",       "url":"/index"    }  ],  "sex":1  xxxx}
```

可以看到页面中只返回了我有权限进入的首页菜单——/index

这时候应该怎么处理呢，其实就是去找出完整的权限菜单来替换响应包，从而实现网站内全功能点的渲染，那应该怎么去找其他的权限菜单呢？对于这种半开放最好的办法就是用已有的菜单关键字到js中检索，也就是在js搜索/index或"首页"，这些菜单在代码中大概率会扎堆，从而让你找到所有的菜单，再替换响应就可以了

当然并不是每个场景都跟我这个案例一模一样，还是那句话，师傅们自己要学会举一反三，这里来看一个半开放的案例

进入平台后，平台返回权限菜单的响应包如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6Kic5mibtagDcicQQ4y8icHBZK82LiczZrqQ4H3CXPEcn5BZiaWwIP4XJptaTOHsNGqbSBxpqhGMT6ezGnDMFVNSmLelIqKUuIVHVT4/640?wx_fmt=png&from=appmsg)

可以看到响应在获取用户信息的同时，返回了一个menuIds，这个menu其实是很经典的权限菜单关键字，也就是说这个menuIds的值，大概率决定了前端如何渲染，数据包加载之后页面如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s7kTpg2iaVPK0R3AxeGXF7pibQODz7ibcFicl5PTB6U66Fn72dW58EWkQQCYicN6bCicDNp2sxIicib6XOib6VmRib3A6Jhj90pC6GUsLHPY/640?wx_fmt=png&from=appmsg)

但可以看到menuIds的值只有几个数字，没有任何的路径，菜单名，这种怎么改呢？其实也是一样的

这里的数字就代表了对应的菜单，发现menuId中缺少了很多数字，所以也是半开放，我们直接补上缺少的数字就可以了，这里是纯数字比较简单，所以我们直接改为1-20就行，没变化可以继续扩大一下数值，这里先试试20，如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s7C4KMzxGqMD1QicmgwV0gqmh18hPSxEgBwic8DObOPLSNdMXPRLs8By6PstpE2fa7L2VcHayTRQd99Wl5G37Fn4YaLVFOHVjWKs/640?wx_fmt=png&from=appmsg)

保存之后回到首页刷新

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s7jSbYpozqBh7FNicY8sz25dGa4MOQdhM9M46lP4PGQFCOaqorCp6hia8r7NqOPTKozNAbIL93F7Fic4ftr7WFn5mmv12VPHeYiadc/640?wx_fmt=png&from=appmsg)

可以看到左侧多了几个功能点，成功渲染出所有功能性路由，接下来测未授权就方便多了

*3*

0开放

第三种是0开放，这种是最头疼也是最难的一种，但平时也会遇到不少，所谓0开放，自然就是给你一个空权限菜单，示例响应包如下

```
200xxxx{  "id":1,  "name":"庆尘",  "menus":[],  "sex":1  xxxx}
```

进入站点之后直接就是空白页或者首页

目标依旧是找到所有的权限菜单并填充替换响应包，那很多师傅看到这种，就完全没办法了，但根据我们这么久的未授权测试以来，还是总结出了不少可行的办法

1、Js搜关键字，因为虽然我们没有明面没有任何信息，但js中是一定有权限菜单存在的，所以可以尝试用关键字搜索，看能否找到，常见的关键字比如menu,router

    还有比如Findsomething发现了路径/scrm/usermanage，这时候可以尝试去搜/usermanage,这种就适用于菜单中携带路由路径的，比如全开放的那个示例数据包

2、js搜接口名，带着接口特征去搜，案例如下

某个站进入之后，页面纯空白，如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s4QdzZFKNe8zYXfvVcs4xgPYqc5kIXucQxnfca31l2vqdUutlEaGibNnKYjaBib3B6dlzjEHSMBy1EfAQ98zB9s97cGXAdQmJudc/640?wx_fmt=png&from=appmsg)

获取权限菜单的数据包响应如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s6mX2CwwQaiaIuYmhic6I5ic8KohkQ0y7bicjnOE5KibwicPv02mC7fhhn6YCBZkPGDmQ4so4W22jZqibpEgLicOHwuQkibkwxZcTOuCWUc/640?wx_fmt=png&from=appmsg)

可以看到响应只有一个list，想找权限菜单怎么找都找不到，这时候观察接口路径——/system/getPermissionConfigure，联想接口含义为获取权限配置，猜测这里的权限配置就是权限菜单的意思，自然就将PermissionConfigure带入js检索，结果如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9chXicZO71s4bOg04EM3MREkqLXNhCXVbyU55ibq4Ga3QWlu1Ria5x5AhEJEqTIDyttMkICry6sgjvTQUqsAMx9jZvMc2MeQ9Au2HQTSicKyDib0/640?wx_fmt=png&from=appmsg)

成功检索到相关代码

```
xxxcheckPermissionConfigure)(home_page)&&/===window.location.pathname)xxx
```

看不懂代码也没关系，直接英译汉

含义为检查权限配置（home\_page）,说白话就是检查home\_page这个权限配置，既然要检查home\_page这个权限配置，那home\_page是不是就是其中一个权限配置，按我们的猜想那自然就是权限菜单

在响应中加上home\_page，发现页面成功多出一个功能点，后续就是找出所有的PermissionConfigure,并替换权限菜单

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s7lB8l8uVEFibBvdQicibxujD4b9NGrL7cpnSToNiaDFdaibNkf86hgczFHLIqDD1m1hPb8b4oqcGicWPwfYP2YVkL79BuhvnyFXZFag/640?wx_fmt=png&from=appmsg)

效果如下

![](https://mmbiz.qpic.cn/mmbiz_png/9chXicZO71s7CPA5sklZYSZuvOwBpAsNlEWJffIWMB9ad5B2KGEkEfrPiaia1oFp1e1N3FX7vsWpA7Jw4gyW3DaySE7uuQzzVY5Iicia5sIkZicMc/640?wx_fmt=png&from=appmsg)

成功从空白页到全站所有功能完整渲染，可以开始爽测了

3、还有一些方法的适配性比较低，所以这里就不提了，师傅们可以自己想想还有什么思路

*4*

特殊的半开放

半开放，开放就开放，为什么特殊呢，其实就是因为路由守卫，来看下面的案例

小庆来到某个站点，打开之后只有一个首页/index，同时获取权限菜单的响应包如下

```
200xxxx{  "id":1,"name":"庆尘","menus":[{    {       title: "首页",       "url":"/index",    }  ],  "sex":1  xxxx}
```

通过Findsomething发现了路由/userManage，然后直接拼接域名访问xxx.com/userManage，访问之后是一片空白，但访问xxx.com/index，就回显首页，明明路径也对，为什么访问不上呢

其实这就是关联路由守卫的权限菜单，路由守卫只通过权限菜单来放行对应的功能点，比如这里权限菜单有/index，那用户可以可以访问/index页面，但返回的权限菜单没有userManage,，那用户就无法访问/userManage

这种其实也很常见，但解决起来很简单，只需要先在权限菜单加入对应的菜单之后，比如

```
200xxxx{  "id":1,  "name":"庆尘",  "menus":[{    {       title: "首页",       "url":"/index"    },     {      "title":"账号管理"      "url":"/userManage"    }  ],  "sex":1  xxxx}
```

再通过拼接路径访问/userManage，就能访问到/userManagae页面资源了

*5*

特殊的0开放

特殊的0开放就是权限菜单最简单的一种。前端渲染不通过菜单来动态渲染，而是通过单个值作为渲染一句，比如

```
200 xxxx
{  "id":1,  "name":"庆尘",  "sex":1,  "isadmin":0,  xxx}
```

还有很多参数，比如isvip，role之类的，都是一个道理，这种就不用多讲了，相信师傅们也都会

总结

结尾了再给大家总结一下

功能性路由的场景分类

第一种：全开放（所有功能菜单对当前用户开放）

第二种：半开放（部分功能菜单对当前用户开放）

第三种：0开放(没有功能菜单对当前用户开放)

第四种：特殊的半开放

第五种：特殊的0开放

以上内容纯属个人见解，欢迎有问题和不同看法的师傅们交流，期待下次继续给师傅们带来更优质的内容

力求把未授权玩到极致

                                                                                    ——庆尘

![](https://mmbiz.qpic.cn/mmbiz_png/2lsubo6ADBMiaTlqOrfVlNpPp1GvHb8VQMqyfbYhb39BTc4XB32iay9icib4txLebALWFdugf8udNrTHRiayiaibLJqYg/640)

结尾依旧打个广告混饭，本人亲带SRC漏洞挖掘课程第四期即将开课，欢迎感兴趣的师傅们咨询

[![](https://mmbiz.qpic.cn/mmbiz_jpg/9chXicZO71s7lgbmpTBbXwqyx0r3icZfRhm6ybTQM2buFichiayS6COe0N41JbaKB7GuCmPsPzeEfFe0ptRRZhuXKnTSsViaAiaQmYbZtMBxku4Vk/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=Mzg3Mzg3OTU4OQ==&m...