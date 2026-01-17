---
title: __NS_hxfalcon  vmp长文分析
url: https://mp.weixin.qq.com/s/o5eDkU0Y5zOB3i3sYY_Ygg
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:26:16.651292
---

# __NS_hxfalcon  vmp长文分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhvjtDxBBCU377vNKBuCibJWQ5q8mUSzskUBrpeZdUKyZ9X14EialRSaJw/0?wx_fmt=jpeg)

# \_\_NS\_hxfalcon vmp长文分析

原创

可乐还是百事好
可乐还是百事好

爬虫逆向小林哥

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhWjhK7scwnaZib3tWyzlPcgE12bdeib7PdoRXVRcpRIyG4zFUaHicESI5Q/640?wx_fmt=jpeg&from=appmsg)

## 介绍

```
aHR0cHM6Ly9tLm0uY2hlbnpob25ndGVjaC5jb20vZi9YNUI4TXZJckpiM00xdDA=
```

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVh216ceI1Jeq9rwpLdnvPq3r55eia42rFyiaATXlerlJZN976kqwxgIkXw/640?wx_fmt=png&from=appmsg)

## 过程

### webpack

大体跟之前sig3一样，简单看下就带过了,Ae===Jose,然后重写了call方法

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhCZQkXty4GxhgCjTsVjJw9UDJ9CpEiaHHJNhric6ZicP1ysiaDQLqMtTGSA/640?wx_fmt=png&from=appmsg)

断到下面，然后就可以进入加载器定义地方，整体复制下来

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhr52INlTxVicHzEkrQrqscsZTMuz2aRWKwKvVTl9xePhopzOibic6HkR3A/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhxXZy6dvduEaOnvgXC189nOTSibTlDpuLJ2Scrwib5zRGSRK4SiciaB4AHQ/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhic2ZgPzu3UjEQlYxhUextj9iaibqJpxZ27gvJ9a1MKWesajgicGxO5Ie0w/640?wx_fmt=png&from=appmsg)

模块也只有15个简单补一下就可以了,很容易出结果，完整代码在文底

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhQ7pKkktrnOG6NhNAQmXq64XVBnricglQg7oXWT8kUWTarylzUO3nadA/640?wx_fmt=png&from=appmsg)

代码太多，Jose以及模块自己复制把

```
window = global;
navigator = {
    userAgent: "hhh",
    sendBeacon: function () {

    }
};
document = {
    cookie: 'did=web_370514bcc9a749efaa81800776c5257e; didv=1761011259000; kwpsecproductname=kuaishou-growth-offSite-h5-ssr; ktrace-context=1|MS44Nzg0NzI0NTc4Nzk2ODY5Ljk0NDU4ODk1LjE3NjEwMTIwNDA3MDIuNTA3NzU1NzM=|MS44Nzg0NzI0NTc4Nzk2ODY5LjU2NjY3NTE5LjE3NjEwMTIwNDA3MDIuNTA3NzU1NzQ=|0|webservice-user-growth-node|webservice|true|src-Js; kwfv1=PnGU+9+Y8008S+nH0U+0mjPf8fP08f+98f+nLlwnrIP9+Sw/ZFGfzY+eGlGf+f+e4SGfbYP0QfGnLFwBLU80mYGAz0+/r7804SPfrM+eWh+9GU+e4S+/D9w/q9wemfPBGl+/WU+9bfw/GI80mj+ASSPfLM+nzSG/G7+0m0Pnc78Br9GA+YPerlGAZ7PnLh+/LI8nGh+AYf+ebYP9bD8nLFGI==; kwssectoken=mqJ1iMEKH5gjUmwkO0jf/4DcKZN0fWlypmCz3VP8oHz8owGHxlIxg/YqSt1HBaLfbZrXsEVaoUf7TePI+WZrag==; kwscode=75d440673de879734b8700f363119968b4fabb4eb0369b1607e206d8e8c1ac9d',
}
location = {
    "ancestorOrigins": {},
    "href": "https://ktag6nr93.m.chenzhongtech.com/fw/tag/text?cc=share_copylink&kpf=ANDROID_PHONE&fid=1966405051&shareMethod=token&kpn=KUAISHOU&subBiz=TEXT_TAG&rich=false&shareId=18635675162938&shareToken=X-JMlHsLScP21Ru&tagName=jk%E5%88%B6%E6%9C%8D&shareType=7&shareMode=app&appType=21&shareObjectId=jk%E5%88%B6%E6%9C%8D&timestamp=1761011213925",
    "origin": "https://ktag6nr93.m.chenzhongtech.com",
    "protocol": "https:",
    "host": "ktag6nr93.m.chenzhongtech.com",
    "hostname": "ktag6nr93.m.chenzhongtech.com",
    "port": "",
    "pathname": "/fw/tag/text",
    "search": "?cc=share_copylink&kpf=ANDROID_PHONE&fid=1966405051&shareMethod=token&kpn=KUAISHOU&subBiz=TEXT_TAG&rich=false&shareId=18635675162938&shareToken=X-JMlHsLScP21Ru&tagName=jk%E5%88%B6%E6%9C%8D&shareType=7&shareMode=app&appType=21&shareObjectId=jk%E5%88%B6%E6%9C%8D&timestamp=1761011213925",
    "hash": ""
}

function sign(e) {
    Jose.call("$encode", [e, {
        suc: function (fs, Ks) {
            console.info("signResult: ", fs, " signInput: ", Ks)
            get_sign = fs;
        },
        err: function (fs) {
            console.info("sig4 encode error: ", fs)
        },
    }])
}

function main(payload) {
    sign(payload)
    return get_sign
}

a = {
    "url": "/rest/wd/ugH5App/tag/text/feed/recent",
    "query": {
        "caver": "2"
    },
    "form": {},
    "requestBody": {
        "tagName": "jk制服",
        "pcursor": "1",
        "count": 18
    },
    "projectInfo": {
        "did": "web_370514bcc9a749efaa81800776c5257e",
        "appKey": "nuojwbmH5T"
    }
}

main(a)
```

### vmp

简单理一下这个webpack运行的思路

首先加载进去 4，看看4执行了啥![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhwicQ94FzHm7Uh6Dhxbsx7ib7tHpvUFArPPg7VVq8IWbfUV62bTwNe9PQ/640?wx_fmt=png&from=appmsg)

就是给模块5的eval传入了很长的字符串 new p  然后调用p的eval

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhXbc9Rd1uak21ByP4jAn8R0ZpoGgZMiatCU1xk1k0UDCUACpvnKEOfKw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhic3xpfs6RncjcDicmYqHa2eDHupwIWnBj1DTMnNyLialL7UmwMIOehISw/640?wx_fmt=png&from=appmsg)很明显就算vmp了.

注意两个地方，在在甲子执行n(4)时候初始化了this.realm ===》 n(6)

一些函数与操作符![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhjr7cwvhjeEMhWZBRDic9mOaeaVia2G2701sreey5F8ITpZjGC5Agt5iaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhNB9youAPACajlYmYM909b2y66Ou19on30IYzicu15U5vcxKey8vgtaQ/640?wx_fmt=png&from=appmsg)

具体的指令集在n(9)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhgWXyklSVdZxg8lLGhkerPHfKncVicQIDzGsj9XO3LI8snr00iaUxazVQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhhghUKa38icgNb0gfhtnV6F653tBlwn7iaIY8eZFCsM4vXNGJ3x2s354g/640?wx_fmt=png&from=appmsg)

整个解释器具体的运行逻辑看下面分析

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhDbia2pG7NmcC3rlvJJicE0I66S3Ih7O0IHzOoNBZbZQEVrhAqW3Gwx1w/640?wx_fmt=png&from=appmsg)

```
s = n(3).Fiber
```

进入n(3)查看

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhIVwBVDScztE2zYiaOtmdjgWzuibFINP2MAQMnnvZ74NRttnw7aTo1Vtg/640?wx_fmt=png&from=appmsg)

```
t.Fiber = i
i = a
```

因此run就是这里的a.run, 最后到下面c.run，通过ip的自增调用上面找到OP的exec

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhXbols0WHF2Vz88Jhmmkibfib107SAX9pRu8SzNJeS358ooVTicsSnsNVw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhGGU6DjF1IJu10ErZ8kgzYg0IRTqVSkoiclxwzsjUkytXCmTe0vZS6kQ/640?wx_fmt=png&from=appmsg)

这里的this.evalStack就是临时寄存器了![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhLkemk2LX3tvIX0Lm4SZ7Y9n7ByrQuFye1AOiacvIJ1W8Bk0gyBzKjkQ/640?wx_fmt=png&from=appmsg)下面指令集也是再不断操作第二个参数也就是this.evalStack

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhgu60lbb9ibdoPu0ko2u62IoUwBicY8xyc6Lr9TibPMB20PT6ibwNnJWOOQ/640?wx_fmt=png&from=appmsg)

### 日志点

先在循环处看看寄存器的内容

```
console.log('ip=', this.ip, '\n', JSON.stringify(this.evalStack.array.filter(item => item != null && item !== '')));false
```

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhh58Y71vGMbB660WS0dEpicl4X8iaMXlzibEQiaiaVTMD6EKnFiaCE26fhCVg/640?wx_fmt=png&from=appmsg)

#### collectDeviceInfo 风控

```
e[this.ip++].exec  ---> callm(e,this.args[0],t.pop(),t.pop(),this.args[1])}
```

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhVYBQUVpdzLMtwMAeOvibNVtu5uAZBQAX4DWwALMstg3Oibt6xEE9YORg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhVzstCqSLN1Mbv63CmSDXIVBNEczXgpay5ZhyhSM63MCRxvolFtIQ6g/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhhK53HSIAxGeLJZkGfno12NY8ykkbeWDuVZ9lL8Tov2A8UdtMYHakyw/640?wx_fmt=png&from=appmsg)

最后掉用了collectDeviceInfo函数

![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhxbyrh1b6PMdgA14ibtD1l8qwibTJuIpbTDGPtAaY4klagJdUHCzS5s9A/640?wx_fmt=png&from=appmsg)

这里的this每调用一次count就会+1，第一次是100

```
[{"count":100,"infoCache":[68,0,27,0,0,0]},"now","jmpOnw_ms"]

[{"count":101,"infoCache":[68,0,27,0,0,0]},true,"jmpOnw_ms"]
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhZko7M4vgZWRVkzkOkibictiaic3meweoA0iakWvmPichpdMopwkXGlpsQ0gw/640?wx_fmt=jpeg&from=appmsg)

ip===84的时候又有一次调用函数当然可以在call上日志的， ip= 93 ip = 102都在一样得位置![](https://mmbiz.qpic.cn/mmbiz_png/5aP6U4veSuxxO3gS2dXBLbhtQSmz5kVhNhicOWmpmb0LxQgicRNop7G7Lj7c8nDq7UfJDP5qSic3jLI1uG5NGZSYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5a...