---
title: 【游戏逆向】腾讯系微信小游戏JceStruct协议分析
url: https://mp.weixin.qq.com/s/3L7an3scB-dgtKEiI-MsIg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:54:17.377947
---

# 【游戏逆向】腾讯系微信小游戏JceStruct协议分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vRTpz13XcLibbTaAMW1TXkeUUz41sg4j6MawU4MCLr7Liaq0DuwDXkesoebB2FrwhKNh5WvSzmDjvYwFxLOZV2JuGWCcZamvZAmRS6SjNBictY/0?wx_fmt=jpeg)

# 【游戏逆向】腾讯系微信小游戏JceStruct协议分析

原创

挖个洞先
挖个洞先

挖个洞先

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**“** 我们都会做出选择，那些选择会让我们走上某条道路。有时候那些选择看起来很微小，但它们足以让你走上某条道路。你想着离开，但最后你还是会回来。——《风骚律师》S5E09 **”**

01

—

操作步骤

1、控制台Fetch/XHR看到只有配置文件json和ini，没有看到业务请求

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLibB30YJYLSyb53HL4K78iaMHB8DFUGYLVolcuRkFgwBMsSmTMWrppibpXjUydFuQ2V7WovPHicYeKMzibvCS5iaO8EEP5gFtaXF6m6U/640?wx_fmt=png&from=appmsg)

2、小游戏没走http大概率走的是websocket

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLickKNibHy85nfqFSaPlcddW8n2nLPXY6oWdyer74TVnM4icibmHuvTJNorzzmagFiciaMJo96EYhP7UVxS3WRUteFo01LdjvRaSdGiaE/640?wx_fmt=png&from=appmsg)

3、断点进入卡住请求，强制ws触发重连，跟进game.js，

发现n.JCEProtocol关键字

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcLicxrx5nyG3GpjLiaK4MEqiaS0HISgicc6vEghcTY6L7SIf6kYOibCDZPErvn86llSHrgOZ6QoUNhicGcnbfnmibQpO48JSXker17EZGs/640?wx_fmt=png&from=appmsg)

4、JceStruct协议分析文章

```
https://bbs.kanxue.com/thread-276418.htm
```

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL8R4gRj2hKgpuKmMNDpicqHthmUhwliaFyvzic39DGxw8nS2zPLgSriaugHwlibXyTjfPj926FpH34qM5zElT8sY49I396tovxESpM4/640?wx_fmt=png&from=appmsg)

5、n.JCEProtocol对象里定义了封包函数X0b，收包函数J0b

```
// 封包函数X0b: function(t) {    // 创建JCE输出流    var o = new e.Taf.nr;    // 将业务明文msgBody序列化写入到o    if (t.md.msgBody.writeTo(o),     // 密钥d存在且ag不在ihd列表中进入加密逻辑    d && 0 > h.ihd.indexOf(t.md.Pe.ag)) {    	// 提取流中数据并调用ohd加密函数        var n = r.default.ohd(new Uint8Array(o.bc.bc, 0, o.bc.len), d);        // 将加密后的数据重新写回流中        o.bc.vec(n.buffer),        // 1，代表加密        t.iFlag |= 1    // 0，代表不加密    } else t.iFlag = 0;    // 省略    new Uint8Array(o.bc.bc, 0, t)}
```

```
// 收包函数J0b: function(t, i) {    // 省略    if (t = new t.va,    // 判断是否存在密钥d，且i.iFlag=1加密的情况，进入解密逻辑    d && 1 == (1 & i.iFlag)) {        var o = new Uint8Array(i.md.yc.byteLength);        // 调用nQb解密函数，结果存入数组o        r.default.nQb(new Uint8Array(i.md.yc.bc, 0, i.md.yc.byteLength), d, o),        o = new e.Taf.Jn(o.buffer) // 将解密后的明文转为输入流    }    // 未加密直接读取流    else o = new e.Taf.Jn(i.md.yc.bc);    try {    	// 将流反序列化赋值给实例对象t        t.readFrom(o)    } catch(t) {    	// 抛出报错，这里可以作为关键字定位        return t instanceof Error ? e.console.warn("decode body fail,msgID:" + i.md.Pe.ag, t.message) : e.console.warn("decode body fail,msgID:" + i.md.Pe.ag, JSON.stringify(t)),        l.fdk.Mhc("DecodeJceFail"),        i    }    // 触发字典c中注册的命令号对应的回调函数，传入i和t    return c[i.md.Pe.ag] && c[i.md.Pe.ag](i, t),    // 将明文对象挂载到外层信封的msgBody上，在这里断点查看响应    i.md.msgBody = t,    i}
```

6、X0b在序列化之前断点，修改难度设定，开始挑战

```
var o = new e.Taf.nr;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcL8KWMMTK6MMiaibrRVgibJn1YdVuVrWFpWW70X9yicqdAuC5h0iaSjobOI2AZoRflanVzh9rPibiaeM21pU22YS2tMm5R7go6iceRtz1aM/640?wx_fmt=png&from=appmsg)

7、跟调用堆栈

```
e && e.XDd(this.aiLevel),
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vRTpz13XcLibfGlnsVgaM4xlO3HribaL4a3J41l40tPyONDnj2HKzicKcbUpZc8mnwTdKFocnKJrSzStRy0mD1ibmJY4zmMPy6xUKVktkib9UoZ0/640?wx_fmt=png&from=appmsg)

8、修改this.aiLevel=1000，人机难度由入门变成了特级大师

![](https://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9AibTQPJB3MwGibume9ibvGQEdljEgzhHcx0qlK4hWUjTDHbwSPvRiay0OBt7Y4J5lRrf8CAHhsllOUS1v6TP1Cfb7EeeuF6c4AWk/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9JgmqXFZSPcaqyGsr3TeRvHibxR9e3VA1HtNvjNr1CpRegjl6R3sLIEK0UiajJ3Nd3dLog4ibNZK8ksqdPudmfMEQgPJKHsTR1eE/0?wx_fmt=png)

挖个洞先

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRTpz13XcL9JgmqXFZSPcaqyGsr3TeRvHibxR9e3VA1HtNvjNr1CpRegjl6R3sLIEK0UiajJ3Nd3dLog4ibNZK8ksqdPudmfMEQgPJKHsTR1eE/0?wx_fmt=png)

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