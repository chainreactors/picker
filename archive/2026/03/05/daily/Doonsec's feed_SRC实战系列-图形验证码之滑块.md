---
title: SRC实战系列-图形验证码之滑块
url: https://mp.weixin.qq.com/s/Ymqyy4_Scb6bI1DSIu1yZg
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:03:01.876406
---

# SRC实战系列-图形验证码之滑块

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhiadt1yEIF5IbfC0TAB5kK6Ks3IXq4fJ8dkrIXr5kzSdaIoPQ9ibaJq5jE4AuEl8SicVBLibwY03XtnYF9SDHkLVfSIBpgZeXOTEpY/0?wx_fmt=jpeg)

# SRC实战系列-图形验证码之滑块

原创

鲨鱼辣椒
鲨鱼辣椒

B1ackTide安全团队

![]()

在小说阅读器中沉浸阅读

一、原理及其分类

原理：滑块验证码的工作流程可以分为前端交互、后端验证

1. **前端交互**：用户拖动滑块完成拼图。这个过程中，前端会记录下用户的**滑动轨迹、速度、加速度、点击的停顿**等一系列行为数据，并连同最终的滑块位置一起发送给服务器。
2. **后端验证**：服务器收到数据后，会进行双重校验：

**图像验证**：检查滑块最终停留的位置是否与预存的目标位置一致或误差极小。

**行为验证**：利用机器学习模型分析收到的行为数据，判断其是否符合人类的操作习惯（例如，机器可能画出完美的直线，而人的轨迹总会有细微抖动）。

分类：逻辑上讲，可以大致分为两类

**基于图像识别**：核心是验证用户是否将滑块拖动到了**正确的图像坐标**上。

**基于行为分析**：更侧重于验证用户的**拖动行为特征**（如轨迹、速度）是否自然。

**二、绕过思路**

滑块验证码的验证逻辑是基于图像和行为轨迹的，所以绕过思路也可以分为两个方向：行为拟真和底层绕过。

**行为拟真：**

1. 模拟滑动

**原理**：机器直接移动鼠标通常是从A点直线到B点，匀速且僵硬。而真人操作往往有起点停顿、中途抖动、速度由慢到快再到慢等特征。

**绕过方式**：可以通过自动化脚本，算法生成类似人类的贝塞尔曲线或随机抖动轨迹，从而欺骗后端的行为检测模型。

**底层绕过：**

1. 参数重放（未加密）

**原理：**一些简单验证码只验证起点和终点坐标或者滑动的距离，不严格验证中间轨迹的真实性。

**绕过方式：**抓包成功的滑动轨迹数据包，记录相关的参数，在需要破解时修改相关参数或者直接原封不动地重放这段数据包。

**2.****前端JS逆向**

**原理：** 在金融、医疗等数据保密要求极高的系统中，几乎所有的请求参数和数据都是经过加密的。但是可以通过分析滑块验证码的前端 JS 代码，逆向出参数加密逻辑，复现加密过程，生成合法的验证参数。

**绕过方式：**首先抓包分析请求的参数，然后在前端找到处理这些参数的JS文件，分析加密算法（偏移量、拼接规则、AES密钥等）。再通过脚本复现加密逻辑，根据滑动轨迹生成明文参数后再生成密文，提交最终的密文完成绕过。

**3.****接口绕过**

**原理：** 通过抓包分析目标接口与验证码验证接口的关联关系，找到后端校验的漏洞，直接绕开滑块验证环节，或伪造简单的验证参数通过校验

**绕过方式：**1、直接尝试尝试访问目标接口。2、未对token进行校验，可以将 token 设置为固定值或空值。3、验证的参数是固定的。

**那么有同学就要问了，主播主播，你写的这些有什么用啊？emm…其实用处不大。所以补充一点之——安服如何水洞**

**1****、究极逆天之信息泄露**

**话不多说上图**

![](https://mmbiz.qpic.cn/mmbiz_jpg/fE13Qb8uKhgAoZD7egRSMkQN8nrC3zMzKibZXODzJUwibMlCScCFO2cibMHO8WCzpy5ubTnKjYCUUdxbicGPMvwbuXibB9txOqZ9Rpokjk4zmNJQ/640?wx_fmt=jpeg&from=appmsg)

**恭喜你——版本信息泄露，喜提低危一个，胆子大可以写中危。**

![](https://mmbiz.qpic.cn/mmbiz_png/fE13Qb8uKhg5yUpZRr17SR7xl97yz0E4IYqT1Pvn8LUkkiaZgV3oUibpqtc7SVH5pgVicRH5hC3ZHFEIwU7DzNicib7cIEELiaNY3pruRgUxibOty8/640?wx_fmt=png&from=appmsg)

**如果在js中找到类似的邮箱地址，并且是他们内部的私人邮箱**

**恭喜你——邮箱地址泄露，再一次喜提低危一个，数量够多可以写中危。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhgx4SW1OAfyAltU42e8PuapfCwe3dPn0kb9DbUMs7h4JmMf0OvBRiaXuicfVBqibBQFk3mx7EtGBSLrlRFPc71o3uxj5fJkRvztmc/640?wx_fmt=png&from=appmsg)

**如果在js中找到类似的IP地址，并且是他们内网的**

**恭喜你——内网IP地址泄露，再再一次喜提低危一个，这个不能写中危。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/fE13Qb8uKhh70SfkedcavMIr2uHPVU6TPOOaD5euN1VYzyEqvAMvAFyibCUzZT0O1WkE5DsibAF6bQibBpl3ZWliaLkutPXxX9XeArtdfYA3ULs/640?wx_fmt=png&from=appmsg)

**如果你在测试时下姬霸点的时候，惊喜的出现类似的错误**

**恭喜你——系统路径泄露，再再再一次喜提低危一个，胆子大依旧中危。**

**2****、神奇的CORS跨域资源共享**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhiavH1ichgHuYMUzoiaibqge9QWkCG0oBwSx3syh9rpHkicXtYxibO8Q35fF42hrYOBW55AdjYc8LzOfhqfCnzibGLiaa0e21RUFfqsmmE/640?wx_fmt=jpeg&from=appmsg)

**但你将你的请求包中的0rigin改成其他的url，并且神奇的发现响应中的access-control-allow-origin变成了你修改的url**

**恭喜你——CORS跨域资源共享，又喜提低危一个，这个你敢写中危包炸钢的。**

**3****、地图key泄露**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhg33yCHeuic6iaDaFuvvG8jYSWRrC1YbDtiaOOGYumbY3DTcWUD26eT8dktmE8s54iaGpmTyU4Bg7cZGduefpqDSTTY0SklTAw5UDI/640?wx_fmt=jpeg&from=appmsg)

**如果你正在无聊的抓包放包，突然你发现出现了key或者ak字样的参数，并且后面跟着一串神秘字符串，然后再验证一下。**

**验证用payload：**

**高德webapi：**

**https://restapi.amap.com/v3/direction/walking?origin=116.434307,39.90909&destination=116.434446,39.90816&key=****这里写key**

**高德jsapi：**

**https://restapi.amap.com/v3/geocode/regeo?key=****这里写key&s=rsv3&location=116.434446,39.90816&callback=jsonp\_258885\_&platform=JS**

**高德小程序定位：**

**https://restapi.amap.com/v3/geocode/regeo?key=****这里写key&location=117.19674%2C39.14784&extensions=all&s=rsx&platform=WXJS&appname=c589cf63f592ac13bcab35f8cd18f495&sdkversion=1.2.0&logversion=2.0**

**百度webapi：**

**https://api.map.baidu.com/place/v2/search?query=ATM****机&tag=银行&region=北京&output=json&ak=这里写key**

**百度webapiIOS版：**

**https://api.map.baidu.com/place/v2/search?query=ATM****机&tag=银行&region=北京&output=json&ak=这里写key=iPhone7%2C2&mcode=com.didapinche.taxi&os=12.5.6**

**腾讯webapi：**

**https://apis.map.qq.com/ws/place/v1/search?keyword=****酒店&boundary=nearby(39.908491,116.374328,1000)&key=这里写key**

**如果成功出现类似信息**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/fE13Qb8uKhhEDq3v6uQuT0DU3weuMZ1MNfZBaYAApydqS7lceoMEPtvNgjWibBRYg3uleiblGd3XIceuFcZ1AlSqToVAQ3BNjI0iaaiamZaQb0s/640?wx_fmt=jpeg&from=appmsg)

**恭喜你——XX地图key泄露，喜提中危一个。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

B1ackTide安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/6r4mCjmylTX8e36HibroUYWpIx20UNGSyWl5GOCJKl7bc2TBwvvaykKHK6jHrXLibd2xGicfNDt47FibeXbUBicmJZQ/0?wx_fmt=png)

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