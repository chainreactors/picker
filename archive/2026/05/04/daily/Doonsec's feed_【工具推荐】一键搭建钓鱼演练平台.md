---
title: 【工具推荐】一键搭建钓鱼演练平台
url: https://mp.weixin.qq.com/s/RtvVgZos6_cVYt7dj-_WXQ
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:58:45.302297
---

# 【工具推荐】一键搭建钓鱼演练平台

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2I159AwKj57WSTFhzDzLNtgkFywytV4A5RaaoQY4Pmja00cFpJNgzttibUCjWg8UqhialleiaY04hoUNFj3jnGl6kcBO3BkObHHnlWuEVL5fmE/0?wx_fmt=jpeg)

# 【工具推荐】一键搭建钓鱼演练平台

点击关注👉
点击关注👉

马哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

字数 290，阅读大约需 2 分钟

## 前言

在去年末，公司要进行内部钓鱼演练，提高员工的警惕度。

在 github 上，找到了一个可以快速启动，无需搭建的羡慕。

项目地址：https://github.com/safe1024/apollofish

![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl8Tic0ts81IZrfJrAmbQ80LJlOTf5AI294mb03GSRMFAR5GibJohia6ncnIxhicolKbk54THDMmxLLMLcL2Iy9CvCtzRW4PfWPYFU/640?from=appmsg#imgIndex=0 "null")

5bf11df2ad65e654feb334933fc58067.png

## 配置

config.yaml
![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkqAxfO8xojVc5XI2nm2WVnl89micqxPK6G73FKSJRR3gsCjd0QJn9UxeqFgibTpedHjLQIqQsyyYoQ53uHBXyFJ9KxykhWE00GM/640?from=appmsg#imgIndex=1 "null")

4a201c55a3262a1519de926fb3686c0d.png

配置信息，可配置路径、端口、账号密码

```
panel:
    path: 9964b510acb907ee07a8a0093f7b83d9
    port: 3333
    username: vyrvy57k
    password: 8g3mqvz7
clickpush:
    wxwork: ""
    dingding: ""
    feishu: ""
```

访问 URL path，输入账号密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnDgEeWa7sp0ibXnND7l558OctAF46bmuHYPibqm6kT22sib0XMjrPQqCpUryicguddBmyFCia1h5DallPCZM54VUh7For0Rjgtvpk0/640?from=appmsg#imgIndex=2 "null")

97315cb12ba11472e138d1002fa8a0ac.png

生成提示词，复制到大模型中获取 HTML
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVm29j4cibibtfGyNg26XibWGKicWFRGxwlHtQIQibnrHemViaSXWmYYvFzhHZQhqq1xJS5Sf2g8nPy5p2icIhDiaIQaugUr339gcXxdgN4/640?from=appmsg#imgIndex=3 "null")

0d6bed5d9d01b24bc19ced2e4fdf2875.png

交给大模型
![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlBBGcS2mYmhpr4wDwYqO3sXlYXGMqBCHoviafIqLm0LReuZkph3YfE9PtMy6LCH6F18wUsaKibqhWZAKIP4DRSPuBwcX2GLnKgo/640?from=appmsg#imgIndex=4 "null")

9996096db526c13f714a9a1a429b898a.png

结果
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkzD12hGVsEfSibWv5XzevIsdzu1EmUJ8YwkEV8Y1JR6zzssbjRkPlPCyKOnIrsreRDwqcsKtibCmYF8nL2WXoea5GyJ5Aj0teSk/640?from=appmsg#imgIndex=5 "null")

1785d1a18f3eb8c4fec734b3fb644b1c.png

下一步
![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmszVYzjKjXs9fkYnZfwyIibicck0wVtLicfXSqQMT046WZneWnibK9sQbJ3WxicY6OOLBdiaBgV8cPjzFztZ8LicTACclCTE8zoRVguQ/640?from=appmsg#imgIndex=6 "null")

31abb916e7037c302fe4422db21c0ee6.png

继续下一步
![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVncicHR2kHjDgDUv6NVu01NwOiblJ1B9eQl4MicjxRvvHxR9bGr19Y2dp0DNrogeIO7tIJKibd1vW87VWzOVzIqvaqibN7n811arQ1s/640?from=appmsg#imgIndex=7 "null")

c983ea79164b8f61212775cb0cbf3096.png

添加成功
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn4DgAjz5xLAt6CFiajngKLPx3K9QlialgX4Yia7LQGm8DA7O1Hhlr0j9PlnHmR1ZwkoPGPFnuOVaQzbHZRq50UEibnpd3p5WJN4VQ/640?from=appmsg#imgIndex=8 "null")

abea6146ed9d8286960a990254dc9530.png

访问
![](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkMp1ZmibJ1zFB8icBqYeYAaKpB9xsHhzC6Hoj8t4zVZU9IErTLHAO2KgU2wldDFpiagM1RIUDQApsCmicibyofVO3YIiaKibwAj0xPJE/640?from=appmsg#imgIndex=9 "null")

db3812d60cfb1950cffc68f6ac10a5fc.png

## 分析

弹框原理
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmbNiaE8KVLBiaqdGccib7mLhpdv5chohOVt9p6o2JjFcJb2W7uib55ksCDGlDsdYw2dUia20t5aMe094ZXKWB4IMsmM8u6EnCrM6gU/640?from=appmsg#imgIndex=10 "null")

88beff3ac1987b6b3e0fbd1db6adb19c.png

如果点击 login 无反应

点击登录按钮无反应的核心原因是**表单输入框缺少`name`属性**，导致登录逻辑中收集的参数数据不合法，被校验逻辑拦截，最终未执行实际的登录请求。

参考：

```
<input type="email" id="email" name="email" class="form-input" placeholder="请输入您的邮箱" required>
<input type="password" id="password" name="password" class="form-input" placeholder="请输入您的密码" required>
```

在 input 标签内添加 name。

## 邮箱钓鱼

将企业邮箱/163 邮箱/QQ 邮箱等的相关信息配置在其中即可
![](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkoVhLqf7EZmO20eyWbfibxThSodicFLicBDRfjb2FclibbWegXMPibdQv7cTKGTTyHo5lwZbN9gP0K7FwSIMYGxL8OY8ibaXRMfM670/640?from=appmsg#imgIndex=11 "null")

a4c7c43d1d8f2da5df5a0a9d08d7f677.png

文章内容转自进击的HACK，侵删

**更多福利**

2026年AI+网络安全专家班是今年最新更新的系统培训课程，欢迎大家咨询参加！

本培训旨在为对安全感兴趣的师傅们提供系统的安全学习路线，在短时间内习得AI+网络安全领域的关键技能，将网络安全核心技能一网打尽，实现AI环境下网络安全高端人才的培养。

![](https://mmbiz.qpic.cn/mmbiz_jpg/UkV8WB2qYAnPKNEglFy69HR9vFlRSicsR5SibFMswbkKtibCwUOtKHgXbjyoxia12j6JhpktMywVmDpQUqkoQKvdmg/640?wx_fmt=jpeg&from=appmsg)

完整版课程内容

请扫码备注：**【安全课程】**免费领取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2I159AwKj568J1dg5nlyfZghicYudMgPmng1QhQLJQwARGFiavOK45Bn7ko5bMn0rnG2w00icA4lp5iaeKOrXWNpFheOhM28fQv9DiabmbdOQnGg/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

马哥网络安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/UkV8WB2qYAnOoZBIicAo3zEb7I6rU7bM6SZGvLjU26JzsajoMuu3oLacM4XPJ9O91942IelPRTHSQFso09IxvVg/0?wx_fmt=png)

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