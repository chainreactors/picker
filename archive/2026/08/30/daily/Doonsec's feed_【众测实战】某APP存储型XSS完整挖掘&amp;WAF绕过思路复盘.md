---
title: 【众测实战】某APP存储型XSS完整挖掘&amp;WAF绕过思路复盘
url: https://mp.weixin.qq.com/s/9Gdh_bEoV_YkhYUdSqOKHA
source: Doonsec's feed
date: 2026-08-30
fetch_date: 2026-08-31T07:51:42.324528
---

# 【众测实战】某APP存储型XSS完整挖掘&amp;WAF绕过思路复盘

# 【众测实战】某APP存储型XSS完整挖掘&WAF绕过思路复盘

Level718
Level718

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

文章作者：Level718

文章来源：https://xz.aliyun.com/news/92642

01

0x1 【众测实战】某APP存储型XSS完整挖掘&WAF绕过思路复盘

大家好，今天给大家复盘一次近期众测挖到的**某APP存储型XSS漏洞**，从前端限制突破、WAF规则绕过、事件FUZZ、字符截断踩坑到最终成功拿洞拿赏金，完整还原每一步测试逻辑，新手也能看懂核心绕过思路。

本文章敏感信息全部脱敏打码处理，请勿使用文章技术进行违法犯罪活动。

## 一、突破前端限制

本次测试目标为某APP**个人账户昵称修改功能**，属于典型的用户可控输入点，是存储型XSS的高危测试位置。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUAeQ5YaQOsrGVRUMoHBp6lPVUAdSRpVI1gDuiaIF8I0fX9gXovKwDRVibU7yVdGQ5gfl8D5j7lgTwyIZBzmoQWnPWtFgX2JVgCA/640?wx_fmt=png&from=appmsg)

首次测试发现，前端页面对昵称输入做了字符输入限制，无法直接发送payload。

**突破思路：抓包修改绕过前端校验**

所有前端校验都是客户端校验，完全可控可绕过。前端的限制仅作用于页面输入，抓包拦截修改接口请求数据包，即可绕过所有前端JS校验，直接向服务端提交恶意载荷。

初步测试 payload：

```
<s>Test</s>
```

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXGSSHxrSpiba0oJYFFWUQeZdOKb3LeNUg7fMibZAicV9WeZrpEX44eicXR1WQaqmeXrY80XwtlyKpHOZibUZo9E3icokI5KhDgzTdoE/640?wx_fmt=png&from=appmsg)

提交后页面正常解析标签、字体生效，证明服务端未过滤HTML标签、前端渲染无转义，存在XSS漏洞基础条件。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVa0EqtTsXZMsKCvya5xq3J6dia7iaIt2NWaKKdcltCuFKcQiaD8icwVtp3V6pxibwF6sxPkl7VeVGM6DQyXAqSBibh0KHHwOlgQSnibc/640?wx_fmt=png&from=appmsg)

## 二、时间戳校验

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QU3zQibz5NeLEMoSSUqtEy82ZeSuPvf8II0OMtoRY4ibu1Vvzm879xOe0FaCpjQM0DicmLEHRiczSjHF0mH7Iapbia8wAlfE27ialiaNA/640?wx_fmt=png&from=appmsg)

重放数据包发现响应**修改已经超时**，这里猜测服务端可能做了一些时间范围限制。

## 三、WAF拦截高危事件

在确认标签可解析后，使用常规hover触发payload测试：

```
<svg onmouseover=1>
```

提交后直接拒绝连接，初步判定：**服务端WAF未拦截HTML标签，但是严格拦截常见高危JS事件**。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWibn1hZO6NbPJsMh41OxwmQ6rg1552I3QZpoGkYYSNESczibs3dwH0vicic9ekta0ic8groQQQX3MGPHpUfO3QjpbZribVzSQ66foP8/640?wx_fmt=png&from=appmsg)

为验证猜想，单独提交纯标签

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXX0z1a5dswZIo7rHPnzfG2zicr3oYcRR7JleOxCX8RnYrzJy5Me42HQvkldGdBjYtH5LqtxDSzESUE17qzGbFYToF8rKwoXxDk/640?wx_fmt=png&from=appmsg)

，数据包正常回显、无拦截，这里修改超时提示不影响后续WAF响应状态的判断。

## 四、事件大小写绕过

针对事件做大小写变形测试，例如 OnMouseOver、ONMOUSEOVER 等，结果全部被WAF拦截。该站点WAF对常见高危事件开启了大小写忽略匹配规则，普通大小写混淆的绕过方式完全失效，必须FUZZ**WAF黑名单缺失的冷门事件**。

## 五、黑名单FUZZ

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXPfJSjWUFf7u9ricynJvzMX3bSicrObcLics2kiagpQdGlUFkN6R6qrULJk4RtjV0yCQQOV71q98TqNr5afzA2RPPDMqUj4QGwork/640?wx_fmt=png&from=appmsg)

针对DOM交互事件进行批量FUZZ测试，最终筛选出**WAF完全放行、可正常触发JS**冷门事件，也是本次漏洞利用的核心关键

> OnMouseEnter、onmouseenter、OnMouseLeave、onmouseleave、OnChange、onchange、OnToggle、ontoggle

这类事件属于HTML5小众交互事件，WAF规则库未收录，无拦截策略，是本次绕过的核心突破口。

## 六、进阶绕过

确定可用事件后，选择兼容性最强、触发最稳定的 **ontoggle 事件**（details标签专属折叠展开事件）搭配大小写混淆标签：

```
<dETAILS>
```

初步测试 payload：

```
<dETAILS OnToggle=alert(document.cookie)>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUymfoBkcqThPO6oY1iajKQFePsnB06h6ib66eh295ic3dGfr3TdSFMoTWsicVOCv1fibaHeU0KVFVeUQ4vuf3bP8PQ68IYGp14vGIs/640?wx_fmt=png&from=appmsg)

```
 <dETAILS OnToggle=alert(document.cookie)>
```

被WAF拦截

**利用逗号表达式写法：从根源抹除攻击特征**

绕过 payload：

```
<dETAILS OnToggle=a=alert,a(document.cookie)>
```

该写法利用 **JS逗号运算符特性**，将「函数定义」和「函数调用」拆分执行，彻底规避WAF特征检测，语法逻辑如下：

第一步：a=alert // 将原生alert函数地址赋值给自定义变量a，**无任何高危特征**

第二步：a(document.cookie) // 调用自定义变量a执行弹窗拿Cookie操作

**关键核心**：整个请求报文里，不存在 **alert(** 这个高危特征串，WAF只能看到普通变量a的调用，无法通过文本匹配识别恶意行为，直接放行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWfZa81K3CqfPLo1LuRO8zia6AWyap8S0R7Wb1vlWB1spIiaCf58mL5h4LmPWyfjBicUqTS5wZnGc59YzAicaZK2TKWTvkkd6mmh4I/640?wx_fmt=png&from=appmsg)

## 七、服务端32位字符硬截断

来到昵称这，发现确实解析出了折叠标签，但是没弹窗

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUgZBfj6QuhwqG5MFEIYgYxgK7j9ZVia3ZbVQ3zfVzNsGj57lTmXCavswiaiaQvmaKklmy1x9tJu0tYPkic1wxuSQ0FsDt6oonzWdg/640?wx_fmt=png&from=appmsg)

站点存在**固定32字符硬截断机制**：超出32位的内容会被直接截断丢弃，不会报错、无提示。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWIkNVMwJEN0FsBRJcZnficRdhSz08h7LfCxVA8AQq6icVCV13US1eZ0E0hSucZP7HwyAXmXiaBP5OefnNIUx5Jro3h6RjnMBF0nU/640?wx_fmt=png&from=appmsg)

测试 payload：

```
<dETAILS OnToggle=a=alert,a(document.cookie)>
```

被服务端强制截断为：

```
<dETAILS OnToggle=a=alert,a(docu
```

JS语法残缺、表达式不完整，完全无法执行，这也是上一步无弹窗的核心原因。

索性放弃弹cookie，直接弹窗1即可

```
<dETAILS OnToggle=a=alert,a(1)>
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWv7yHpIqjiaI42poXx8q8avfEenP95PSibYtxo1MkFIa8PianFLWN6ACYU4lgnherHED7oXESIYuSX2Gv964d1Vb0xLP6Nv28ahs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QX4jiaVpGhN8ceWvHdLN4Vrfs9ZySOk8icEE8y3iaibUdqF2IPC04UvF1hKzq5tBqMOIb874Aliaj3qDEHvia1I1s8saYGkj2qaicqr9E/640?wx_fmt=png&from=appmsg)

**核心优势&绕过原理**

1. **规避WAF alert() 特征拦截**：常规 payload 会出现明文 alert(，极易被WAF匹配拦截；本载荷采用 **逗号表达式赋值执行**，原文无 alert( 特征，先赋值 a=alert，再调用 a(1)，完美绕过函数特征检测。
2. **小众事件免拦截**：ontoggle 非高危自动事件，无WAF默认拦截规则。

最终提交 payload，页面正常渲染折叠标签，点击展开后成功弹窗，**存储型XSS漏洞验证成功**，成功拿下300元众测赏金。

## 九、漏洞总结&挖洞思路复盘

1. 前端限制全部可被抓包绕过，不要被前端输入拦截迷惑；
2. WAF大多拦截**显性高危特征**，小众HTML5事件、变量赋值调用语法，是高效绕过手段；
3. 遇到无报错不执行的情况，优先排查**服务端字符硬截断**，而非单纯纠结WAF拦截；
4. 逗号表达式伪协议，是规避alert、eval等高危函数特征的通用高阶XSS绕过技巧。

本次漏洞难度不高，但非常适合新手学习「从踩坑、判断环境、FUZZ筛选、适配限制到最终利用」的完整众测思路，所有绕过手法均为实战通用、可复用的技巧。

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是575（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[学了一堆理论，还是挖不到漏洞？你缺的是实战！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509438&idx=1&sn=1b5c5c14bef52f1a4fd8319fea73a0cb&scene=21#wechat_redirect)

内部小圈子知识星球详情🔎：[50 元封顶！渗透攻防 + SRC 漏洞星球限时开放！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509408&idx=1&sn=2e12452dfc2d34631af5109af28a6758&scene=21#wechat_redirect)

欢迎关注公众号：神农Sec，报名咨询添加VX：routing\_love

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu3QYzD5d62zsp6qwc38Pssk60mLq8VKthcMOmctVlHU716S5G4KYmrKVrEj5c/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

开课快五个月时间，课程目前已经累计加入了960+个学员了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVmdLBDlbl5p4Teyw5qqFOIFTIUxIxRay83I5qDXG690XI61gRj8MXTvTaibC4q2cCb1CbM4XS2FK6X4KYhPTX2ibgvA363YYwcE/640?wx_fmt=png&from=appmsg)

课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家交流氛围很好！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QV7iczVHowN13BzCTraG8jDUoe5hluiaZ90RUy7FjW398DictcrZhHrYpMgw4polRqvlGua6iakYdARPI3Jkiahhjvrvkviblm19U4F0/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪怕是课件笔记都没有的，我这里都是下课第一时间把录播+笔记打包发给大家！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWbRV4mBn8GZHrvHocPMYYcBuAM3gyIKOM0SicBWQhywMehkXInvEerRLySOPPMzEmM2GLSlOMFREx6QItqtCgCibGs2MeY6yvu0/640?wx_fmt=png&from=appmsg)

平常也都会给学员进行一些项目发布，包括后面的工作、护网内推等，经常上麦交流，大家互相学习，简历优化等。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXvjjkgJibDEUhdDjErjibiangGsN0rqb0Av59xfyxBbDrTMNdfIAhNXlx0HQKvxIVBIEGAAbYrEENzd77j65asejlD4a50Sb4U7o/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=20)

SRC漏洞挖掘课程培训已经两个星期了，期间也是创建了“回本小群”，希望学员回本越来越多，创建这个群主要是鼓励学员学习进步，以及不定时发小项目！

最后也是希望大家都可以赚钱，找到好工作🎉

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXwkSjEERiaNurU2EiaEQwPJUYVicJS6R6Y3AMFcx5U0YfI8c7UClJ7VMXLKELa2Cibd3Iuib9kw1tq8kicx3LqIhRWChfI9W8NDCppk/640?wx_fmt=png&from=appmsg)

培训时间不长，感谢🙏师傅们的喜报，很开心看到师傅们给我分享自己的成果，希望师傅们越来越强！

![图片](https:...