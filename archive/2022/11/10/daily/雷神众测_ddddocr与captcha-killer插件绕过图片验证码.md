---
title: ddddocr与captcha-killer插件绕过图片验证码
url: https://mp.weixin.qq.com/s?__biz=MzI0NzEwOTM0MA==&mid=2652500509&idx=1&sn=8649f0b7e4f985dcd4e52612f561be2a&chksm=f25851aec52fd8b86aa0cf551d4ba57e0a14fbdc3798f15908e689513c2edc680c6aeaf51276&scene=58&subscene=0#rd
source: 雷神众测
date: 2022-11-10
fetch_date: 2025-10-03T22:15:23.234525
---

# ddddocr与captcha-killer插件绕过图片验证码

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8Pf1nwjqiczK0RQTbcmCeUC3czuGgwZVb6aseDx9iatmAH08nkfTxibo4A/0?wx_fmt=jpeg)

# ddddocr与captcha-killer插件绕过图片验证码

原创

s1mp1e

雷神众测

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NZmaRcSalKvfHadLeGuC6dEYQP3975XPbQkDYbjWI6sPOicm0hv8bmkTXMg5SzpDiapWeUxaWyqXdn/640?wx_fmt=svg)

**STATEMENT**

**声明**

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。

雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NZmaRcSalKvfHadLeGuC6dEYQP3975XPbQkDYbjWI6sPOicm0hv8bmkTXMg5SzpDiapWeUxaWyqXdn/640?wx_fmt=svg)

简介

1、ddddocr是由sml2h3开发的专为验证码厂商进行对自家新版本验证码难易强度进行验证的一个python库
python<=3.9直接用命令 pip install ddddocr 进行安装
项目地址：https://github.com/sml2h3/ddddocr

2、captcha-killer是一个burpsuite的插件，captcha-killer本身无法识别验证码，它专注于对各种验证码识别接口的调用
项目地址：https://github.com/c0ny1/captcha-killer
这个插件安装需要注意，如果burpsuite的版本在2020版之前，可以到上面的项目地址进行下载，但如果burpsuite版本在2020版及之后，则到上述项目地址下载后无法使用，可到如下地址下载：
https://github.com/Ta0ing/captcha-killer-java8

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NZmaRcSalKvfHadLeGuC6dEYQP3975XPbQkDYbjWI6sPOicm0hv8bmkTXMg5SzpDiapWeUxaWyqXdn/640?wx_fmt=svg)

使用方法

首先需要明确，ddddocr只是一个python库，需要编写脚本利用这个库进行验证码的识别，附上脚本：

```
# encoding=utf-8import osfrom flask import Flask, requestimport ddddocrimport base64app = Flask(__name__)
@app.route('/api/upload', methods=['POST'])def upload_pic():    data = request.form.get('image', '')    img_data = base64.b64decode(data)    with open('captcha.jpg', 'wb') as f:        f.write(img_data)
    ocr = ddddocr.DdddOcr()    with open('captcha.jpg', 'rb') as f:        img_bytes = f.read()        res = ocr.classification(img_bytes)    return res
if __name__ == "__main__":    app.run(host="127.0.0.1",port=8991,debug=True)
```

这个脚本利用flask框架开启一个web服务，到时候captcha-killer插件会将验证码图片通过这个web服务传过来，然后脚本对验证码图片进行解析，将解析结果返回。

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8Ocq7udBC9bNxibia9twIO17nx39OtPtfn4o8rgJZy2jPTIGCRNS6Cfibw/640?wx_fmt=png)

2、抓取验证码的请求包

1）访问登录接口，点击验证码刷新，用burpsuite抓包

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8eiajWtjTadugodiclK5Vsj4F9r20vVMftQjUickX5XTnBqkd1eibLXaxrw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8siavLbae8MYPY5Jend51BPF6dicZKU71yibjH9u5RVlW3RsRpSnSKn5zg/640?wx_fmt=png)

2）将抓取到的验证码请求包发送到插件

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8ohR838vFgkc97t2qVZUuPMIQaBmo4RLXic6SVjFsQCIjAiaggqiaTUy6A/640?wx_fmt=png)

3）切换到插件，点击获取，如果能获取到验证码，说明是这个包

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8wYWyq4EMhOzAfSiaIpficN1Dw3rJAicSP3RNRfVXE44KVzS6DOphdER6Q/640?wx_fmt=png)

4）配置接口，发送请求
这里给出请求包格式：

```
POST /api/upload HTTP/1.1Host: 127.0.0.1:8991User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2Accept-Encoding: gzip, deflate, brReferer: http://127.0.0.1:8991/api/uploadContent-Type: application/x-www-form-urlencodedContent-Length: 9Origin: http://127.0.0.1:8991Connection: keep-aliveCookie: ll=108296; BAIDUID=FEA7B3A131CE38315D6659E087861E2B:FG=1; BIDUPSID=FEA7B3A131CE38313A9C5BD381345226; PSTM=1644314147; channel=127.0.0.1:8084; baikeVisitId=229b0def-020a-4bf9-9635-3bb7a01623caUpgrade-Insecure-Requests: 1Sec-Fetch-Dest: documentSec-Fetch-Mode: navigateSec-Fetch-Site: same-originSec-Fetch-User: ?1
image=<@URLENCODE><@BASE64><@IMG_RAW></@IMG_RAW></@BASE64></@URLENCODE>
```

接口URL填写第一步开启脚本时使用的IP和端口

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8CK1CmoJ6Uiboo6gFUnIy2AeQib9Picv53uLco4ibIfNTyicP5dybk7jssvg/640?wx_fmt=png)

5）点击识别即可识别出验证码

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8pyUu0ttbsI6VWRKDBJbjQUeibXK0WPtKo0oYbXzraR8J6qYvKVmibiaIw/640?wx_fmt=png)

6）当以上步骤完成时，说明已经配置好了，接下来就可以进行验证码绕过爆破了，首先在登录接口输入账号密码验证码抓取请求包，发送到intruder模块，使用pitchfork攻击类型，设置密码和验证码为变量

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8GC0Va6ibaEboQT8cCUKYhU5GzqXdPibbSpSAIiaMMyuKaajc3Xta3CsxQ/640?wx_fmt=png)

7）然后在位置一设置为密码字典，位置二选择有效载荷类型为通过扩展生成，然后选择captcha-killer这个插件扩展

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8OGkwHKvPaAldG5Fia5LeqcibKd6dWh5KRQqorX3GKl96V5yBiaDnXicQkA/640?wx_fmt=png)

8）现在就可以进行爆破了

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8t9oqfmxlET8yqiah3WWl9iaM12pF8HbqdotKE0pVhFKvLTsWnTd3dUwQ/640?wx_fmt=png)

**安恒信息**

✦

杭州亚运会网络安全服务官方合作伙伴

成都大运会网络信息安全类官方赞助商

武汉军运会、北京一带一路峰会

青岛上合峰会、上海进博会

厦门金砖峰会、G20杭州峰会

支撑单位北京奥运会等近百场国家级

重大活动网络安保支撑单位

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8TNultBrX3vegYsGlkONksCRtHHsGuKdXW3wnj2YpExEydvU7ibyVUrQ/640?wx_fmt=jpeg)

END

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8OC1KAic9SUHzEcHSNTdRGkLdvXWC2E2LibmKPib6OQO3nvAQGPcNpgibHg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JV90j9ic1LSWnonIE9oChtV8t1wwIoiayRiccibPSUroCBYgCzqtMiaP3oCZ9uE6icZGQEXL36l6Lhy3HgA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JV90j9ic1LSWnonIE9oChtV80cuqnR3025oCZIobbpKcBkU4AHF8c1pTosySvwBzKKNT2QdfRNnprQ/640?wx_fmt=gif)

**长按识别二维码关注我们**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

雷神众测

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

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