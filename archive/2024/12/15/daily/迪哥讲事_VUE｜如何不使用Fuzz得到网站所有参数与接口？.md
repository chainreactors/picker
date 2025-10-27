---
title: VUE｜如何不使用Fuzz得到网站所有参数与接口？
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496602&idx=1&sn=b23208b7113632dbea687ab88a6e3ef9&chksm=e8a5f9f9dfd270eff0f807aa5450f12ad14a02ffe1a7a0107ac5a8da3d9872c511ed1e16434f&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-12-15
fetch_date: 2025-10-06T19:38:41.395415
---

# VUE｜如何不使用Fuzz得到网站所有参数与接口？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj7G4qiaib9HQr2EZXThLjvTtRq1sbM6INvHOp1cRw47q0WKic8jfvON4e5jrT889ptmTsKBx1I7ohAQA/0?wx_fmt=jpeg)

# VUE｜如何不使用Fuzz得到网站所有参数与接口？

迪哥讲事

以下文章来源于一位不愿透露姓名的热心网友
，作者不愿透露姓名的热心网友

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7EomoAliaxuCKn0blUwibX3ANtxXaSz0vFiaynokNXbMybQ/0)

**一位不愿透露姓名的热心网友**
.

不定时更新一些渗透、逆向及个人心得随笔。

访问某`VUE`站点，发现直接重定向要求从飞书登陆，立马抓包丢掉请求了。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBB6ehKpiaQgWTHEsURIg7Yh1042v3BH3Aia1kbict13mSE3YiaaTK6SZqGtw/640?wx_fmt=png&from=appmsg)

imagecopy

使用`JS`替换在本地调试修改尝试绕过

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBB6YQtSQA2wG7Jsic7zFGHE4E2zRyt0SM7LmeUCIVH7kpcxr0WO8Xztqg/640?wx_fmt=png&from=appmsg)

直接全局搜索跳转到`url`找到原因， 把这个注释掉并保存，重新刷新进入。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBWujN3twJWMdDyyFcG7644SZdfHia5x1qcYEaMnMUlwqUeoScZevf2GQ/640?wx_fmt=png&from=appmsg)

image

接着又发现无限重定向到主页，然后打开`console`发现最后一个提示是`401`，仅接着又重现`location`到到根目录了。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBpoRU5ataTZQibCOBBhrYmkbdyRdrwuYM1pfOkh5d7QnkR3F2jScMh0Q/640?wx_fmt=png&from=appmsg)

image copy 3

在控制台看见最后的请求是`api/user/info`，搜一下是什么发起的

```
e.headers.common.Authorization = "Bearer " + Object(o["b"])(),
        e), e=>{
            console.log(e),
            Promise.reject(e)
        }
        ),
        c.interceptors.response.use(e=>(e.request.responseType,
        e.data), e=>(401 === e.response.status && (Object(o["c"])("code"),
setTimeout(()=>{
  location.reload()
        }
        , 4e3)),
  console.log("err" + e),
        Promise.reject(e))),

```

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBHMopJd1l7FiavBZGJy6v4Pz8T8b9nvRedDqYZapMDbH6kcut9QYicg6g/640?wx_fmt=png&from=appmsg)

image-1

原来是有一个判断`401`的定时任务执行 `location.reload()`

直接注释掉

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBIhibfawEc5xDMwc32rbbfNMHwOmicrsoRAAkS1icUSC4s0lt1CmjAiclEA/640?wx_fmt=png&from=appmsg)

image-3

ok不执行`reload()`了，但是也不继续走了，没有画面了😭

---

既然`401`会`reload()` 那么`200` 会发生什么？我这里直接点击`at XMLHttoRequest.m` 的报错来到请求发出处对`status code` 进行修改，当然也可以直接选择使用`burp`替换。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBLhOukKh3csOmRAxFNRX8zwSmt4Q85BGMBGaiaAicuBkULgvYrX9X5P6g/640?wx_fmt=png&from=appmsg)

image-2

我选择直接把`status`写得`200`

```
a = {
data: i,
status: 200,
statusText: h.statusText,
headers: r,
config: t,
request: h
};
```

---

`console`依然是`401`的报错，但是多了一条别的报错，说明代码继续往下走了。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBsYmChvPIrboZBgOAnARQr4YjxiaHJU2Fdib2JQUrJHeWcIYlGiawmaN3Q/640?wx_fmt=png&from=appmsg)

image-4

提示`TypeError: Cannot read properties of undefined (reading 'staff_id')`说明无法读取`t.profile`对象的`staff_id`属性。

断点查看一下`t`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBqJSu6xl7TBuTLziaiaan4WcoTdDibFIOc8XibnHbpdr7DuQxwmbH7Gv7og/640?wx_fmt=png&from=appmsg)

image-5

应该是在请求认证接口返回的一些数据结构，但是我并没修改返回的`response`，只是对`status code` 做了修改，其他的数据哪里来的呢？

向上回溯发现一些地方也是做了处理。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBmbdq7kQqLgAAElWicpDDicsANYiafbKdh5yo6PTSZtibtlVXqV2jJDgfSQ/640?wx_fmt=png&from=appmsg)

当然这些都不重要，即使有了数据也不一定是正确的，后端如果做了鉴权，伪造的数据是肯定无法通过的。我们的目的是欺骗前端。

先简单的统统杀掉`staff_id`, 就是那里报错删那里，最后什么`name/avatar`之类的报错都删除了，只留下了`e.profile`

终于出画面了，也出新错误了😭

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBSFzglarbibDicGUliaEdeb40vxk08x3ANsHW4mWrT0vicFVd1qnUanaibqg/640?wx_fmt=png&from=appmsg)

image-7

又是提示`Cannot read properties of undefined (reading 'xxxx')`

看`e.data`的规律应该是从某个接口的`responses`中读取公司和部门列表做展示，这里依然是直接做删除处理✖️

结果如何请看VCR🎬

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBz1tZpFdNBgBabCdKuuxjwwf5Qur1J8FoNadYyWjn03rjaiaxvaPDqBQ/640?wx_fmt=png&from=appmsg)

image-9

好了不报错了，收工。忙活了半天发现做了个空页面展示。![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBtLgwnlhjrmy2Niba6qibaTlg7gy15cTpPlu29XgCJu5sLuYLmQb4ZzEg/640?wx_fmt=png&from=appmsg)

---

即便是没有公司部门数据也不至于什么功能都没有展示啊？？？肯定在哪里还有逻辑判断
下个断点往回追一追看（其实上面某处已经出现过了）。

最后发现在`create`方法下有`admin`相关的字眼

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBfqwDPNXPZPqJlhGahXUBcnw1StQrV8PyKwqE5ARKNfOQCrEOuxYhHQ/640?wx_fmt=png&from=appmsg)

image-11

```
  methods: {
    loadRoute(e) {
    var t = !0;
    e.forEach(e=>{
      ("recruit" === e || this.$store.state.user.staffAuth.includes("admin") || this.$store.state.user.staffAuth.includes(e)) && (t = !1)
    }
    ),
    t && (window.location.href = "/#/home")
}
}

```

在这里有一个路由守卫判断权限，遍历判断权限是否为`e`是否为`recruit`或s`taffAuth`包含`admin`，如果条件成立则设置  `t = !1`

结果修改完发现依然是空白展示，压根没走到`t = !1`这个地方判断。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBSUtIxFHdk9uj3PgZN4KsDRAvsCoqSGjaqVLCHG3Lyb4LwHexiaYuuicw/640?wx_fmt=png&from=appmsg)

如何仔细阅读代码其实根本不用走到这一步就能展示路由了，写到到这的原因完全是因为补控制台的报错🤣

---

> > 应该是在请求认证接口返回的一些数据结构，但是我并没修改返回的`response`，只是对`status code` 做了修改，其他的数据那里来的呢？向上回溯发现一些地方也是做了处理。![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBmbdq7kQqLgAAElWicpDDicsANYiafbKdh5yo6PTSZtibtlVXqV2jJDgfSQ/640?wx_fmt=png&from=appmsg)

让我们回到上面👆这一部分重新开始。

首先这里异步获取了`h["a"].state.user.staffAuth`用户权限的属性，并存储在`e`中，接着访问了 `/permission/generateRoute/` 路由生成接口将用户权限传入。

最后执行`addRoutes(e)` ，所以这里应该是关键点，判断权限并添加路由。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBGIYAanSdZVorzibMibX8WKBibPMxorg10JNNYAj6WoicxjaDj6Wic560nYA/640?wx_fmt=png&from=appmsg)

image-14

断点得到了一个存储了路由信息的数组，并且有个`"hidden":true`属性，这应该就是控制展示的参数。这里选择继续深入，看看是哪里判断hidden是false还是true的。

这里需要了解VUE相关知识，`.dispatch` 用作于分发 `action` ， 一直跟进到原生的`vuex.min.js` 中拦截，看看这个 `/permission/generateRoute/`绑定的是什么action

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBdJZceuJIkXpia7rttdvJbdO6FbKdKbeKY522vF3tybYE06jzQWZia2hA/640?wx_fmt=png&from=appmsg)

image-15

最后得到这么一个`action : s` 的东西, `s`命名为`generateRoutes`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBicMpeMOqqxscj0SnkaqwtK2eVG3vGt7SOS2L7lsXDIAicDLcrFyuNLWA/640?wx_fmt=png&from=appmsg)

断点发现`r`路由信息是由`i(n["a"], t);` 返回的

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBB6ZhcKsPWRAAkcvhKIyrSsbQT9E4ib2BicyB1g8x90vCObb7EBXTz5v2A/640?wx_fmt=png&from=appmsg)

image-16

跟进`i`  发现组建设置`hidden`的判断点`("recruit" === t || a.includes(t)) && (e.hidden = !1), a.includes("admin") && "other" !== t && (e.hidden = !1)`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBcNxicavMtqHjWicOcZvJHEdmVc1jicIRkOGxyqiackpTCCtWwYFibumsGpA/640?wx_fmt=png&from=appmsg)

直接注释掉设置为 `e.hidden =!1`

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISYqybTKUIfAhLPyLqj0ciaBBRHkILkWnPYOtnfCib8iatBZXuLx8a7AOxcSJ6KU8QrFLX9xzwFY0PzyA/640?wx_fmt=png&from=appmsg)

image-18

#### 收工，点点点半天功能发现所有接口都没有未授权，白干一天。

> 错了，是好几天，还写了好几天😭

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5EMr3X76qdKBrhIIkBlVVyuiaiasseFZ9LqtibyKFk7gXvgTU2C2yEwKLaaqfX0DL3eoH6gTcNLJvDQ/640?wx_fmt=png&from=appmsg)

## 往期回顾

[一款bp神器](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495880&idx=1&sn=65d42fbff5e198509e55072674ac5283&chksm=e8a5faabdfd273bd55df8f7db3d644d3102d7382020234741e37ca29e963eace13dd17fcabdd&scene=21#wechat_redirect)

[ssrf绕过新思路](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495841&idx=1&sn=bbf477afa30391b8072d23469645d026&chksm=e8a5fac2dfd273d42344f18c7c6f0f7a158cca94041c4c4db330c3adf2d1f77f062dcaf6c5e0&scene=21#wechat_redirect)

[一个辅助测试ssrf的工具](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496380&idx=1&sn=78c0c4c67821f5ecbe4f3947b567eeec&chksm=e8a5f8dfdfd271c935aeb4444ea7e928c55cb4c823c51f1067f267699d71a1aad086cf203b99&scene=21#wechat_redirect)

[dom-xss精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247488819&idx=1&sn=5141f88f3e70b9c97e63a4b68689bf6e&chksm=e8a61f50dfd1964692f93412f122087ac160b743b4532ee0c1e42a83039de62825ebbd066a1e&scene=21#wechat_redirect)

[年度精选文章](http://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0M...