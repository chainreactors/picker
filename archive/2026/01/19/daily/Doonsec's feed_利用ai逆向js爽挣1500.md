---
title: 利用ai逆向js爽挣1500
url: https://mp.weixin.qq.com/s/XXtuRKhjMCJ-gLAvLRkrUQ
source: Doonsec's feed
date: 2026-01-19
fetch_date: 2026-01-20T03:31:47.360664
---

# 利用ai逆向js爽挣1500

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqn2eklGwKBhUNiaZiaAmGbK0Yz6qzR3ORj5iaiab5l18LWzx3Jp7REooeug/0?wx_fmt=jpeg)

# 利用ai逆向js爽挣1500

原创

xx
xx

jacky安全

![]()

在小说阅读器中沉浸阅读

## 前言

从朋友的朋友那里接的项目，帮忙逆向某个站的加密请求，中途自己搞花了不少时间后面利用ai辅助之后两小时就逆出来了。

## 第一处加密

这个地方也是运气好，key和iv是固定的，全程不需要逆向，一个浏览器插件就搞定了(虽然要求的加密位置不在此处)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNq6oy7LkEZnRnCnLGoGfIInUiaRZiat9CDBOROKzm3tbQoFtaxlTJVCwNQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqKKLiaCzwAwNB1JrRrSQtsTHfuk4j4ibvtMSBWg1ibZXu31RPSRu8uib6kg/640?wx_fmt=png&from=appmsg)

## 第二处加密

### 过debugger

由于请求体和响应体都是加密的，所以想着搜接口来定位，抓住加密请求之后，正准备搜接口调试的时候，出现了debugger

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqibWYnwiaYMibguabGNhusO2QKiak1AoHE1yssPkbcibicicx9iarNLXdxMKbZQ/640?wx_fmt=png&from=appmsg)

因为自己比较懒，直接找个插件就过了debugger

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNq6mz4yRmPbHm3qFUDdddC0pZJ96GWYIKVOuDUxsI2owW44M1mO00NNA/640?wx_fmt=png&from=appmsg)

问题又来了，接口搜不到，那就只能跟堆栈了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqctNFDQKoGkVGVF1s6ia97ibiatLYmKxDFfNd7pZ0om3McqzHLWibicu907Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqnxpBbTBQ3tsfwwrAYdFyVibPNmRaBJQgDiac8tn284Qy2EvKh7DRzD0w/640?wx_fmt=png&from=appmsg)

直接从最下面开始跟 顺便最上面那里打一个断点，看能不能找到明文位置，因为大多数的都是混淆代码，直接把整个代码扣下来，顺便还原一下相关代码，然后直接丢给ai帮我分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqbE4LVBk5ice1hbnU1zaH9V82djSSHy4NDjgdc1EFoDe2Xj42bMWY4eA/640?wx_fmt=png&from=appmsg)

### 疑似加密模式

看到这里就感觉像是加密模式了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqBycelCicwVjWmldH6a9vib64Zj70rC3elGweyG7zMVtqz7xTzEgwmp0Q/640?wx_fmt=png&from=appmsg)

继续往下跟，跟着跟着不小心点错了，跳出断点了，想着在来一次后面发现怎么下断点都断不住了，直接清空浏览器缓存再来一次，后面尝试了好几次都发现断不住了，后面开了无痕就可以了

### 疑似明文位置

还原之后

```
encry_t = this[x][y](desencry,{data:raw})
data应该就是请求包中的明文了
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqwSibyFenOzNUaGnnEPQnOEETzxuEfwJBeibaxRnSTRON5GLGDOcYj7nA/640?wx_fmt=png&from=appmsg)

到了这里就有点激动了，想着应该很快就能搞定加密了

### 定位密文位置

继续跟进

```
return this[_999[333]][_999[444]](this[_999[555]](), _777[_999[666]])
还原一下就是
this[desObj][desEncry](Key(),raw[data])
```

已经很明显了，继续跟这个函数 走进 desEncry

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqTW9peDVmWN5L1gWh6icoq7n6UPPhWYCjJcD5ZsxVcXtrmYRoTfI5TyA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqibGE5w5hNeNOepmAWcia2JSJ189BSlicgKgMWLZcvDEmicuA28r7vibV5gg/640?wx_fmt=png&from=appmsg)

```
this.crypto.des = function(key, data, isDecrypt, encryptMode, iv, paddingMode) {}
```

ai解释的很好，实际情况跟ai描述的也是一致的

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqP0CJfjL6bWcfx6UGJbtw431Dvm2b3eHQMUDicuGwQ4icEdVJur9T1vtQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqIn55TYX4ECoqYOkCiaScwDX6TCZibCziaOq3NrfbEADmgQuA7BMFr4gJg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqxJH70JlUhdspoRHXSJzCUPvCFBoYljdKoALlYROgcsKRlMM9FGeBxQ/640?wx_fmt=png&from=appmsg)

### key的追踪

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqU53EBgjlC0uvE8MqtREL8Hk5sibsibib7Kt9EYXjqHf7dIkdJSMkK2RmQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqpQEYlJOGIZzgBNV9EzstZpqpX5dUDrMh8ZV7CQHibwoibb1YsgtgzolA/640?wx_fmt=png&from=appmsg)

在只需要获取到des-key即可完成 解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqKpib05muCVDjbBGTaQyr0nExmeibRxnRclKibYOMssZMh74uVAU4aQjPg/640?wx_fmt=png&from=appmsg)

最后得到key的输入

```
K =  _999( id + code , _888(id + code , key + sid) )
```

后面就是慢慢利用跟踪的过程了，最后也是写出了解密脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNq8xXyUBPcpibq5zzVBgFNUv7HXRDibwXOAjjy154Q9iaqoxT2ceen9bcRw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWdSj5X31QpRL9ddN6pzZDNqx2sNsAz9aPFBCUpkhft26L9oYYMVHnMpb24RI1YSxzqPMW2pdiamibLw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWe04I77cradewwEVpnDoUEjQfTpC2T3q8Jf2guZIoUh4bM6cfYTI2GiaNVb0eAKWBLRXFzQOn1VXiaw/0?wx_fmt=png)

jacky安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/hZR1w6JVBWe04I77cradewwEVpnDoUEjQfTpC2T3q8Jf2guZIoUh4bM6cfYTI2GiaNVb0eAKWBLRXFzQOn1VXiaw/0?wx_fmt=png)

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