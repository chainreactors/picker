---
title: 【PC样本分析】从吾爱破解弹广告到浏览器插件网页挟持行为分析
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651138610&idx=1&sn=482d29d14f534dbb2ddd540fcaedc694&chksm=bd50ba668a273370865e9d54b0681b9f1c65dcc3c9ec78187a4dc1559c4e9b40601f26f48e5f&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2022-11-05
fetch_date: 2025-10-03T21:45:40.369352
---

# 【PC样本分析】从吾爱破解弹广告到浏览器插件网页挟持行为分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDper1icHiaRrmCicbM4S7rYC6OPNjicYD0iaQVGMtthE26wJbKjF93icaceLDLQ/0?wx_fmt=jpeg)

# 【PC样本分析】从吾爱破解弹广告到浏览器插件网页挟持行为分析

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：漁滒**

# 一、分析背景与危害

起因为站务区出现的几篇帖子

1.咱这论坛（木马插件劫持）
2.为啥每次登录都有广告弹出来（木马插件劫持）
3.进入吾爱好多广告，怎么设置进去吾爱没有广告。
4.pc端上52论坛子论坛跳广告，是中毒了吗

这几篇文章中均为插件劫持类型，并且分析代码发现其中结构高度相似。起被挟持后访问部分网站会出现奇奇怪怪的广告

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpel7Wn8DyDWtxLFo7yMI15Fq16OcMzpU2nNQ5YzPaoAIznFVDMKPyIzw/640?wx_fmt=jpeg)
会出现但不限于左上角和右上角的长方形广告，以及左下和右下随机出现的正方形广告

同时使用百度搜索的话，链接会被添加返利参数如【tn=xxxxxxxxx】,虽然这个明面上没有上面广告这么恶心，但是也被强制添加了推广返利参数，那也是相当的流氓。

综上所述，这类插件主要的危害有两个：

1.会导致部分网页出现诈骗、赌博等广告，即广告弹窗劫持。又因为是部分网页才会显示广告，导致用户误以为是网页的广告，使得插件隐蔽性更高。
2.在搜索百度搜索等搜索时，会被添加额外的返利参数。即使是正常的搜索行为，也会被不断给开发者进行返利推广。同时也是特定的搜索引擎才会出现，也导致大部分网友认为是官方添加上去的，也具有极高隐蔽性。

备注：
本样本是被人恶意篡改，并不是原本插件就是这样
本样本是被人恶意篡改，并不是原本插件就是这样
本样本是被人恶意篡改，并不是原本插件就是这样

# 二、行为分析

首先在未安装插件前，访问52破解官方首页。这时是没有出现上述广告的，然后打开Fiddler，安装插件，安装完成后就发现会发出大量的请求

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeQicRRVfuU8h33807JFq8hCF9EzqoRQI5cpziafEwlIw85QQF0JCzN5hQ/640?wx_fmt=jpeg)
此时尝试访问52破解官方首页

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeWPH9H9A0dKiciaD9Mpk46B3dZbpeVsFXiboib8ziad9a0u95LpKXqGMe7mg/640?wx_fmt=jpeg)

很明显是插件的挟持行为，导致了页面出现预料之外的广告。从上往下开始看看

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpe9uwsgRmyGCOcjN1VnDqwDWtIBUL7QcFIYibaP605U8iaov49rAZD66hw/640?wx_fmt=jpeg)
第一个是一个【channeldelaytime】的api，里面请求参数有一个加密的字符串，但是响应里面并没有什么有用的东西，所以先抛弃不看，接着下一个。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpe0glFwiczp35yIYqpVMmblflTWnDTS0CcgPwpOUicYxhSBeP8hwmOCujw/640?wx_fmt=jpeg)
接着是一个【getonlinecode】的api，从名称上可以猜测，很有可能是加载在线的恶意js，并且这是一个302的响应码，跳转到路径【/old/0.1.1.9/code.json】的一个文件，里面是一个加密了的文件，那么只能动态调试分析了。

打开插件文件目录，浏览器的核心文件是【manifest.json】

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeclRWcBZRSJaiaYTu3uVsLmWW4Nla8ocmaGvYPFNMEwABgMfFrXIzsGg/640?wx_fmt=jpeg)
发现前面加了一个一些奇怪的js，全部打开这些js，然后在搜索文件中搜索【getonlinecode】

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpexU8suwwc79zxmB7MYD7euxZazibTCBJk3nwXBIX9BfGoFia56iaoD0mcg/640?wx_fmt=jpeg)
只匹配到一次，出现在【backg.img】，说明这个是一个比较关键的js，然后在单个文件中继续搜索

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeYKbF0ia7bsIgNsX8kK8z6mywORb7kwZZU4Dm7RVosCCWnjE6iaMzzIGA/640?wx_fmt=jpeg)
可以看到请求结果经过【openDoor】方法得到真实的js文件，然后直接eval运行。接着打开插件的背景页，删除搜索缓存，设置一个xhr断点后刷新

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeMeJbkh6jUEg8ckn7S4MoIOz4ldTCgP5eDVdCRO1mlbia7I8Z1YyHVEg/640?wx_fmt=jpeg)
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeumCa2QS1wIIaXYnem6Ry76tuJDobO0LicOvUs2caDQWD5wH6u11Surw/640?wx_fmt=jpeg)
成功断下，然后在异步回调的地方下一个断点

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeaSJO9TTVRyK7RwKia49sLVrmq6VoMKyKz7l59dyDicTMiariacbLS7VjOQ/640?wx_fmt=jpeg)
data.data就是响应的加密内容，this.key就是【softwarecenter】，继续跟进【openDoor】方法

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeloBCm7BcvWyVhWRVNGFZ9k5KkibA3IVAvz4urNzh8CkT7apvxxmalCg/640?wx_fmt=jpeg)
发现是一个aes加密，但是奇怪的是，密钥才14位，并不是16位，拿解密个锤子？

不着急，继续往里面跟进

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeTGwJzpOFZTh2PjicoRCet7s0H0KBHe1hWKhGyzAGaWOgQ6nfMV8mZyA/640?wx_fmt=jpeg)
里面调用了【i.kdf.execute】方法，返回了n对象，这个n对象的key和iv才是真实aes使用的，这里其实是一个加盐的aes。而却从加密文本的开头【U2FsdGVkX】也可以发现是加盐的aes。

根据逍遥一仙的文章【易语言】带盐AES的加解密（非调用JS），这里有易语言模块

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeyD2D337XjibviaX9kM83r61NadwX7fia7HmVMcZDwewgt8U6vR4xBextg/640?wx_fmt=jpeg)
下面给出python版本

```
复制代码 隐藏代码

def Salted_Aes_Decrypt(data: bytes, key: bytes) -> bytes:
    if data[:8] == b'Salted__':
        salt, data = data[8:16], data[16:]
        md5_1 = MD5.new(key + salt).digest()
        md5_2 = MD5.new(md5_1 + key + salt).digest()
        aes_key = md5_1 + md5_2
        aes_iv = MD5.new(md5_2 + key + salt).digest()
        crypto = AES.new(key=aes_key, mode=AES.MODE_CBC, iv=aes_iv)
        try:
            return unpad(crypto.decrypt(data), AES.block_size)
        except:
            raise Exception('解密失败，可能是key不正确')
    else:
        raise Exception('这不是一个Salted_Aes加密的结果')
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeHdRr4Jibn4SjicOJkO14bKAX2mTmiaibbefMoALIrk2nArtXibNSOosIpow/640?wx_fmt=jpeg)
解密的结果就是一段js，然后eval执行。这就达到了在线注入js了，然后注入广告的代码，很有可能也是在这段js里面。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpe3OpINKzBg5JcicNnK6bv6Pp1CVibHOIkEibymZeHrz8u8cmZFwCYCibIkw/640?wx_fmt=jpeg)
接下来这三个请求比较可以，都是返回了aes加密后的结果，用python请求并解密一下看看

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpesQwnXvZhPyJlVa9iaOibey2FNKRj2ILAZEXqoHib9icrYTxZzLMqicNORbg/640?wx_fmt=jpeg)
这里可以看到了一些类似策略文件之类的一些敏感内容，看起来不是一个标准的序列化方法，那么就在js里面分析反序列化方法，也是下载xhr断点来查看回调函数

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeksxJnMDc9sQDcaMicnVlzOPiazrzStu6CoicNPNrWLJthoiaprriboklw8g/640?wx_fmt=jpeg)
这里可以看到调用堆栈都是vm，也和前面获取在线js然后eval运行对上了，这里可以看到是调用了createTxtJson方法来解析这些敏感信息

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJUhBrOP6wwxAI0dfmPxDpeiaboQKEpTdkJEHC3Ca057xObKAsTicI3D1p7gsNU08c9qF7bXQ5FKPlg/640?wx_fmt=jpeg)
使用python稍微复现一下

```
复制代码 隐藏代码

def createTxtJson(txt: str) -> list:
    t = list()
    for each in txt.split('\n'):
        if each:
            e = each.split('||')
            if e[0] == 'list':
                t.append({
                    'type': e[0],
                    'id': int(e[1]),
                    'targetid': int(e[2]),
                    'shieldCity': e[3],
                    'shieldChannel': [] if "null" == e[4] else e[4].split("|"),
                    'targeturl': e[5],
                    'sourcesproportion': int(e[6]),
                    'targetproportion': int(e[7]),
                    'filter': e[8],
                    'refferfilter': e[9],
                    'clearcookie': int(e[10]),
                    'clearreffer': int(e[11]),
                    'domain': [] if "" == e[12] else e[12].split("|"),
                    'interval': e[13],
                    'appointchannel': [] if "null" == e[14] else e[14].split("|"),
                    'writeSourceLog': "true" == e[15],
                    'sampling': int(e[16]),
                    'intervalscope': e[17] if e[17] else "all"
                })
            elif e[0] == 'rule':
                t.append({
                    'type': e[0],
                    'id': int(e[1]),
                    'targetid': int(e[2]),
                    'shieldCity': e[3],
                    'shieldChannel': [] if "null" == e[4] else e[4].split("|"),
                    'targeturl': e[5],
                    'sourcesproportion': int(e[6]),
                    'targetproportion': int(e[7]),
                    'filter': e[8],
                    'refferfilter': e[9],
                    'clearcookie': int(e[10]),
                    'clearreffer': int(e[11]),
                    'reg': e[12],
                    'interval': e[13],
                    'appointchannel': [] if "null" == e[14] else e[14].split("|"),
                    'writeSourceLog': "true" == e[15],
                    'sampling': int(e[16]),
                })
            elif e[0] == 'insertjs':
                t.append({
                    'type': e[0],
                    'id': int(e[1]),
                    'targetid': int(e[2]),
                    'shieldCity': e[3],
                    'shieldChannel': [] if "null" == e[4] else e[4].split("|"),
                    'targeturl': e[5],
                    'sourcesproportion': int(e[6]),
                    'targetproportion': int(e[7]),
                    'filter': e[8],
                    'refferfilter': e[9],
                    'clearcookie': int(e[10]),
                    'clearreffer': int(e[11]),
                    'reg': e[12],
                    'interval': e[13],
        ...