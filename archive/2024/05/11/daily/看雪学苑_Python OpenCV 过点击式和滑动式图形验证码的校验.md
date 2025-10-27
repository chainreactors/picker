---
title: Python OpenCV 过点击式和滑动式图形验证码的校验
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458554259&idx=1&sn=7408f6d495f8c926eee7ebf7a3f3637f&chksm=b18dbf1986fa360fbc396ee82f19ebd4cbaada1acdb64c22350741dc2d01c5a4ae7ead924916&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-05-11
fetch_date: 2025-10-06T17:17:21.572600
---

# Python OpenCV 过点击式和滑动式图形验证码的校验

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F58BEbw642jdrS1Geofo5QhkNnAsoToprWcxY6ib2WdiaJeB8WRZoIBP8YGMA1HNRGB7cCZnH3fR2w/0?wx_fmt=jpeg)

# Python OpenCV 过点击式和滑动式图形验证码的校验

暮至夜寒

看雪学苑

```
一

背景
```

最近在给一个app抓包的时候发现App在特定时间会弹出验证码，验证之后会给一个token，需要携带token才能发起能正常请求。

文章源码地址：https://github.com/ThinkerWen/CaptchaPass

**验证码如下：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5Q0GaMP2yjcsVohURJEsWjgoNbgJWx0J5KtgEI09EFl9A4abicCV2Cgicw/640?wx_fmt=png&from=appmsg)

**弹出验证码的Response如下：**

```
{
    "data": {
        "errorCode": 0,
        "errorMsg": "",
        "bg": "https://example.com/ENZg076503962.jpg",
        "front": "https://example.com/ENZg076503963.png",
        "token": "eyJhbGci...",
        "width": 765,
        "height": 396
    }
}
```

**完成验证码的Request如下：**

```
{
    "m": "[{\"x\":395,\"y\":256},{\"x\":89,\"y\":273},{\"x\":670,\"y\":140}]",
    "token": "eyJhbGci..."
}
```

由此观察到只要将验证码的点击坐标post到完成验证码的接口，就可以获取到token，即现在的目标就是提取坐标。

```
二

方案
```

观察了下这个验证码不是很难，因为它没有图案扭曲，所以还是比较好过的，同时我也想起了以前过滑动验证码的一个方案（同时给出）。

要过验证码，就是将目标图案在背景图片上找到，并且将其像素点找到就可以。

于是我使用Python的OpenCV进行图片的识别。

### 1.提取图片

首先观察发现目标图片都是黑色图案，且背景为透明地址，当我直接使用**cv2.imread(front\_image)**来加载图片时，会显示一片漆黑：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QaIBlOJfgVRluqEQV8Kc08t4fOtHoR77j8qon6HApp1LjxNVne27arQ/640?wx_fmt=png&from=appmsg)

即使后来我使用了保留透明通道的加载**cv2.imread(front\_path, cv2.IMREAD\_UNCHANGED)**，依旧是一片漆黑。

于是我想可以将透明通道剥离，然后将目标图案透明色设置为白色，那么目标图案就自然显现了，成品如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QtBibXTqibJo7NI1icHeP3j70AAVj0JibCAJnquB6s01QNzZraUsTvpKprQ/640?wx_fmt=png&from=appmsg)

###

### 2.即然提取出了目标图片，那么就开始下一步，将目标图的位置找出来。

我先要将目标图片的三个图案分割出来，对每一个图案分别找出他的像素位置。

本来想通过颜色精准分割，但有些图案并不是整体粘连的，经过观察发现目标图片的三个图案排列位置都是固定的，所以直接记录出他的坐标进行像素分割：

**rectangle\_list**每一个元素是[x1,y1,x2,y2]

```
rectangle_list = [[9, 9, 75, 75], [109, 9, 175, 75], [209, 9, 275, 75]]
for idx, rectangle in enumerate(rectangle_list, start=1):
    cropped_image = white_front[rectangle[1]:rectangle[3], rectangle[0]:rectangle[2]]
```

分割后我们将目标图和背景图都转化为灰度，防止颜色碍事：

```
gray_bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
gray_front = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
```

然后直接进行最佳匹配：

```
res = cv2.matchTemplate(gray_front, gray_bg, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
cv2.putText(bg, str(idx), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (7, 249, 151), 2)
show(bg)
```

最后发现匹配结果欠佳，总是不能完整的将3个目标图案都准确找到，所以还需要再优化。

### 3.优化匹配方案

继续观察，发现背景图片中的目标图案总是白色的，所以我们放弃使用默认的灰度，转而将背景图片上所有的白色部分保留，其余全部转为黑色，这样不就完全没有杂色了。

为了尽可能保留完整的图案，经过多次RGB颜色的尝试，发现250-255区间可以保留大部分目标图案的白色：

```
gray_bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
_, strong_contrast_bg = cv2.threshold(gray_bg, 250, 255, cv2.THRESH_BINARY)
```

同时为了和背景图片上的黑色色块一致，我再将黑色的目标图案反转为白色。

由于要获取的是点击坐标，所以我们将x1,y1(即左上角坐标)进行+20的偏移，来移动到图案本身上面。

```
gray_bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
_, strong_contrast_bg = cv2.threshold(gray_bg, 250, 255, cv2.THRESH_BINARY)

res = cv2.matchTemplate(
    strong_contrast_bg,
    cv2.bitwise_not(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)),
    cv2.TM_CCOEFF_NORMED
)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

x, y = max_loc
x, y = x + 20, y + 20
```

经过验证，现在的识别就能正常过点击验证码了。

贴出代码：

```
import logging

import cv2
import numpy as np

def ProcessCaptcha(bg_path: str, front_path: str):
    result = []

    """
    加载图像
    背景为jpg格式的普通图像 像素为 765x396
    目标为png格式的包含透明通道图像 像素为 300x84
    """
    bg = cv2.imread(bg_path)
    front = cv2.imread(front_path, cv2.IMREAD_UNCHANGED)

    """
    由于目标图为透明黑色图片，直接加载会导致图像全黑，
    为了避免全黑情况，创建与图像尺寸相同的白色背景图像，再提取图像的透明度通道，将透明部分的像素值设置为白色
    这样加载完后的图像就变成了白底黑色目标的图像
    """
    white_front = np.ones_like(front) * 255
    alpha_channel = front[:, :, 3]
    white_front[:, :, 0:3] = cv2.bitwise_and(
        white_front[:, :, 0:3],
        white_front[:, :, 0:3],
        mask=cv2.bitwise_not(alpha_channel)
    )

    """
    为了按序点击，需要提取目标区域的矩形方块
    由于目标图像较为规律有序，于是计算出3个目标图像像素坐标，直接按像素截取
    """
    rectangle_list = [[9, 9, 75, 75], [109, 9, 175, 75], [209, 9, 275, 75]]
    for rectangle in rectangle_list:
        cropped_image = white_front[rectangle[1]:rectangle[3], rectangle[0]:rectangle[2]]

        """
        将背景图片转换为黑白两色的图片，只保留RGB(250-255)的图像
        如此能保留绝大部分目标图像轮廓
        将目标图像转换为黑色背景白色轮廓
        如此便与背景的颜色逻辑一致
        """
        gray_bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
        _, strong_contrast_bg = cv2.threshold(gray_bg, 250, 255, cv2.THRESH_BINARY)
        strong_contrast_front = cv2.bitwise_not(cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY))

        res = cv2.matchTemplate(
            strong_contrast_bg,
            strong_contrast_front,
            cv2.TM_CCOEFF_NORMED
        )
        """
        使用 TM_CCOEFF_NORMED 算法匹配到最佳
        由于此时的 X,Y 坐标为左上角坐标，需要加20进行偏移处理，获取到点击坐标
        """
        x, y = cv2.minMaxLoc(res)[3]
        result.append((x + 20, y + 20))

    logging.info(f"Done process: "+str(result).replace('\n', ' '))
    return result
```

##

```
三

滑动验证码
```

滑动验证码与上同理，甚至现在比较常见的一种滑动验证码已经有了通用的代码，如：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5Q2BxIvL64jfbsGWyEj2w3rHTVkia04oZJhlZA2icDlZpbjkgau19pbLYg/640?wx_fmt=png&from=appmsg)

这种滑动验证码已经是无脑式**matchTemplate 、minMaxLoc**就可以，非常方便：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F58BEbw642jdrS1Geofo5QjSW7hztKFyT7tfsgibTzp8oyTebHXoodOXYsBmWAypmWxsNX4Edq83Q/640?wx_fmt=jpeg&from=appmsg)

贴出代码：

```
def process(bg_path: str, front_path: str) -> None:

    # flags0是灰度模式
    image = cv2.imread(front_path, 0)
    template = cv2.imread(bg_path, 0)
    template = cv2.resize(template, (340, 191), interpolation=cv2.INTER_CUBIC)

    # 寻找最佳匹配
    res = cv2.matchTemplate(_tran_canny(image), _tran_canny(template), cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    x, y = max_loc
    w, h = image.shape[::-1]
    cv2.rectangle(template, (x, y), (x + w, y + h), (7, 249, 151), 2)
    show(template)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QxpA0XBokR6hPGFOzAH4rOHWkcVlgiaGT1vic92wHQepsI0MBRKqPtMTg/640?wx_fmt=png&from=appmsg)

**看雪ID：暮至夜寒**

https://bbs.kanxue.com/user-home-959049.htm

\*本文为看雪论坛精华文章，由 暮至夜寒 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8F58BEbw642jdrS1Geofo5QzIfEQicMAq5iboGC7XXD9ibY4bSyjJCyXMYeEFMXhelrmYFmgduRibeJFQ/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553432&idx=2&sn=7938e74463db1fed445f716b4099e0e4&chksm=b18dbcd286fa35c464a56edf60ab75bd5f745266f81dc51f4b102d967151ac55f41d16297d2b&scene=21#wechat_redirect)

**#****往期推荐**

1、[通过修改物理内存实现跨进程内存读写](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553962&idx=1&sn=4918d3fd46149a68a89ebb3fd1088811&chksm=b18dbee086fa37f6715d624c24893ed8af8b86c831a8efa35a20c164ae7ac4518daf7d28cbb9&scene=21#wechat_redirect)

2、[CVE-2020-9802：Incorrect CSE for ArithNegate 导致的越界访问](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553736&idx=1&sn=fa9d04982a90b1c0cf6c375efce65314&chksm=b18dbd0286fa3414de804dbd2315099238c1ec027489de8a51a7a6dd663b3a239d6768593497&scene=21#wechat_redirect)

3、[通过BLECTF入门BLE](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553587&idx=1&sn=555f3300fdfb937c866049ec95101e07&chksm=b18dbc7986fa356f385dbffe62de254e6d722f876becce0a78ebe8c2b742e83a71fd87bea561&scene=21#wechat_redirect)

4、[InfinityHook 可兼容最新版windows](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553456&idx=1&sn=2df223026199d77ea1ee2672cd2792a4&chksm=b18dbcfa86fa35ece674c4810d4596eafd31fb2fee0e692de35fd9375dff614fccb9583c2704&scene=21#wechat_redirect)

5、[CVE-2023-4427：ReduceJSLoadPropertyWithEnumeratedKey 中的越界访问](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458553432&idx=1&sn=93377c71147ef00b8e58571093d5ab55&chksm=b18dbcd286fa35c424bcf128759e907304820fb4289f407f6ba5ecd0b48897ce31ddb7623caa&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4Vy...