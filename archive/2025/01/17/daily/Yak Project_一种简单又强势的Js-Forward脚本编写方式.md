---
title: 一种简单又强势的Js-Forward脚本编写方式
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527481&idx=1&sn=9bee930fcf19964ae14c0d949c517570&chksm=c2d1109df5a6998b7ef18c9aa6230c5759ef54ac86481b4372e0b3e08e5217cc312d81f83fe4&scene=58&subscene=0#rd
source: Yak Project
date: 2025-01-17
fetch_date: 2025-10-06T20:11:38.667704
---

# 一种简单又强势的Js-Forward脚本编写方式

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPK6WhnloduZNPWJ9SBbgbu5MhTxbl0mZbviasHukyFiaPrbYVUpto5WUg/0?wx_fmt=jpeg)

# 一种简单又强势的Js-Forward脚本编写方式

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

听牛牛说

先这样，在这样，最后再这样

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZdUYXaiccQFYhEArmU3f9ef0KattgbSlER0ibQRtxzicS0icGlQQiaOqD6u7GoNVTzgicicYMQrEia405iaiaoA/640?wx_fmt=png&from=appmsg)

一个**Js-Forward脚本**就写出来了

你学废了吗？

![](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZeeTiaUCTkrXfbtIPCxmicjgPYpcUvoicyagIcrXqeTmFuvZDibXQXGkP4FW6zdqSgNicdTkMZibmczHQLw/640?wx_fmt=webp&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPzFPQPwxykd4mqicMPibdNte0K13wA8P0Bb3OErUmZ6npT6Tp4JMbhNMQ/640?wx_fmt=png&from=appmsg)

JS-Forward是一款可以配合抓包软件的脚本，脚本的功能是可以将js里面的参数通过Http请求将参数发送出来，在外部(例如Yakit的MITM中)进行修改，最后将修改后的返回值再替换回原参数。在一些特定场景是可以方便做功能测试。比较常见是在JS加密解密场景下使用。

一个简单的时序图如下：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPJIrGLWxqPCxCRjKQq5UuCPqxoHcVWDKbElgnibBmiammBMoWu07DVv8g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryP3H4nAm6lme41Wcic2ZDJMjk7N7oKampNuJMkMoJ6UicpK50sBxn6PEicA/640?wx_fmt=png&from=appmsg)

**原版Js-Forward地址：**

https://github.com/G-Security-Team/JS-Forward/

原版Js-Forward的脚本比较简短，实际上原理也非常简单，我们拿最重要的两个服务器处理函数进行解析：

```
class ForwardRequestHandler(BaseHTTPRequestHandler):    def do_POST(self):        content_length = int(self.headers.get('content-length'， 0))
        self.send_response(200)        self.send_header('Access-Control-Allow-Origin'，'*')        self.end_headers()        data = self.rfile.read(content_length)        if str(self.path) == "/REQUEST":            r = requests.request('REQUEST'， 'http://127.0.0.1:{}/'.format(ECHO_PORT)，                                 proxies={'http': 'http://127.0.0.1:{}'.format(BURP_PORT)}，                                 data=data)            new_data = r.text            self.wfile.write(new_data.encode('utf8'))        else:            try:                r = requests.request('RESPONSE'， 'http://127.0.0.1:{}/'.format(ECHO_PORT)，                                     proxies={'http': 'http://127.0.0.1:{}'.format(BURP_PORT)}，                                     data=data)                new_data = r.text                self.wfile.write(new_data.encode('utf8'))            except:                self.wfile.write(data)
```

以上是其中一个转发HTTP服务器的处理函数，在接收到POST请求时将请求转发到另外一个Echo服务器（对应时序图中的第一步），并且途中设置代理为BurpSuite端口的代理，以此来让外部对请求参数进行修改。在收到响应时，直接将原始的响应写回给客户端即可（对应时序图的第四步）。

```
class RequestHandler(BaseHTTPRequestHandler):    def do_REQUEST(self):        content_length = int(self.headers.get('content-length', 0))        self.send_response(200)        self.end_headers()        self.wfile.write(self.rfile.read(content_length))
    do_RESPONSE = do_REQUEST
```

这个是另外一个Echo服务器的处理函数，直接将收到的请求体原封不动地写入响应体即可。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryP21rgUkJNW19WDPkPXKU5nmwpFvqw4ibTAvDyBgibF6nDmxGwr2IHnKicw/640?wx_fmt=png&from=appmsg)

Js-Forward的核心函数就是以上两个函数，在了解了Js-Forward原理之后，有一个常见的疑问是为什么会有一个”多余“的Echo服务器。

实际上这个答案很简单，即我们不能直接将请求发给MITM代理，因为代理会将请求发到真实的服务器，并将响应返回给客户端，如果我们不将请求发给Echo服务器而是发给其他服务器或者目标服务器，显然我们无法将响应体作为修改后的请求参数来使用。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPdyk4XO0a60Ls0tpLEQjFXUdvDKiaTZ4JqQ0KmsayaC29cXQEGWvBylA/640?wx_fmt=png&from=appmsg)

使用yaklang自带的httpserver库，我们可以很轻易地启动一个http server。一个简单的echo server例子如下：

```
httpserver.Serve("127.0.0.1", 18888, httpserver.handler(func(w, req) {    w.WriteHeader(200)    rawRequest = http.dump(req)~ // 获取完整的请求数据包    body = poc.GetHTTPPacketBody(rawRequest) // 获取请求体    if len(body) > 0{        w.Write(body)    }}))
```

需要注意的是通常我们会使用协程来启动http server，因为httpserver.Server函数本身是阻塞的.

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryP5EfgF4d9xnh3cHjIh6iaZticawmM5LicdicxP7ichgL6ia80nT61DibC0nYiaw/640?wx_fmt=png&from=appmsg)

参考原版的Js-Forward脚本，我们可以很轻松地编写出来对应Yaklang版本的Js-Forward脚本。现在脚本可以在插件商店中搜索"Js-Forward"来下载使用。这里贴出全部代码：

```
varname = cli.String("varname", cli.setVerboseName("参数名"), cli.setRequired(true), cli.setHelp("要转发的参数名"))vartyp = cli.StringSlice("vartyp", cli.setVerboseName("变量类型"), cli.setRequired(true), cli.setSelectOption("字符串", "string"), cli.setSelectOption("Json", "json"))yakit_port = cli.Int("yakit_port", cli.setVerboseName("Yakit MITM端口"), cli.setDefault(8083))cli.check()
vartyp = vartyp[0]
port = os.GetRandomAvailableTCPPort()echo_port = os.GetRandomAvailableTCPPort()jsCode = f`var xhr = new XMLHttpRequest();xhr.open('POST', 'http://127.0.0.1:${port}', false);xhr.send(${varname});${varname}=xhr.responseText;`if vartyp == "json" {    jsCode = f`var xhr = new XMLHttpRequest();xhr.open('POST', 'http://127.0.0.1:${port}', false);xhr.send(JSON.stringify(${varname}));${varname}=JSON.parse(xhr.responseText);`}yakit.Info("将上述代码复制到找到的加密函数开头,变量定义之后(需要注意的是变量是否为常量,如果是常量则要改成变量)")yakit.Code(jsCode)getbody = func(req) {    r = req.Body    body, _ = io.ReadAll(r)    return body}
go httpserver.Serve("127.0.0.1", echo_port, httpserver.handler(func(w, req) {    w.WriteHeader(200)    body = getbody(req)    if len(body) > 0{        w.Write(body)    }}))go httpserver.Serve("127.0.0.1", port, httpserver.handler(func(w, req) {    opts = []    body = getbody(req)    opts.Append(poc.replaceBody(body, false), poc.proxy(f"http://127.0.0.1:${yakit_port}"))    rsp, _, err = poc.Post(f`http://127.0.0.1:${echo_port}`, opts...)    if err != nil {        yakit.Error(err.Error())        return    }    origin = req.Header["Origin"]    if len(origin) > 0 {        w.Header().Set("Access-Control-Allow-Origin", origin[0])    }    w.WriteHeader(200)    w.Write(rsp.GetBody())}))
ch = make(chan any)<-ch
```

代码中有几处关键的地方值得注意：

1. 使用cli库我们可以很轻松地获取用户的输入
2. 需要判断变量类型来对变量进行额外处理（JSON.Parse/JSON.stringify）
3. http服务器要额外处理CORS的问题,将origin原封不动写回去即可，否则响应会被浏览器的CORS策略拦截。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPaa2V0aJibW3QfqNnuXPtQZOUIOt9TG2yrVfKoHWI2zcJY6m4aqsmyXQ/640?wx_fmt=png&from=appmsg)

这里以**encrypt-labs**(**https://github.com/SwagXz/encrypt-labs**)中的第一个题目为例：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPlg9PvWUCAHDHdicstvBia6WE50djpicYvk30xRKsgRR1PYVTnEcUcNJEA/640?wx_fmt=png&from=appmsg)

1. 分析html与js代码，发现其会调用sendDataAes这个函数，在easy.js中找到该函数，并且发现我们输入的数据会赋值够jsonData:

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPtxqibe4IHibJPh5BGBN3cyQ59mAqrjOBd2wZar0MtCaaeFoL02IGtL5Q/640?wx_fmt=png&from=appmsg)

这里需要注意的是jsonData是常亮，后续修改前需要将const改为var/let，让该变量可以被修改。

2. 打开Js-Forward插件，填写对应的参数并运行：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPmI2icqibS3icVfmOxZQB2dwQ8F5iady6tK8x6Z2Jnw2s8u8NAjNia1TQb9g/640?wx_fmt=png&from=appmsg)

3. 将输出的代码块复制，并放到变量定义的后面：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPJTiabSO0fVUYgx5U63ibv3XZVoiaAicpExxpXusqbzkO4ibx55HbvqbGb0Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPtibH0yibkzqJibbMRs7JicL0oJS2icaU8kKbZicPG33Xq8PVUR0dPhzjx3Xw/640?wx_fmt=png&from=appmsg)

4. 保存修改的代码，并启动Yakit MITM服务器，需要注意端口为8083，或者在第二步中修改Js-Forward的Yakit MITM端口号：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPsQPrOoOvvuLmaOHVyoyuqG9C5SNwtQtwEicFUCWuSRII15ZOX1MMs1g/640?wx_fmt=png&from=appmsg)

5. 在靶场中随意填写用户名和密码，并点击数据发送接口为：AES固定KEY，此时MITM应该会接收到请求：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPicticYbHw54XvRPDzULZOTaOoUsALcicGicTicDeia5YpNdTsnJUcC2a8wYQ/640?wx_fmt=png&from=appmsg)

6. 修改请求中的明文参数，用户名为admin,密码为123456并点击提交数据：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPeVLFJCPSibgDYPSEe8I1tIvFXcLes56C5vx8icTcp4sDicWKibLyibOF6Ig/640?wx_fmt=png&from=appmsg)

7. 靶场提示登录成功，即证明Js-Forward正常工作，成功跳过了加密的步骤：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZeLlicKmK7XRAZA5r3pchryPvkO3g6Q1aiaxswibLKSQiaQtbQ8rqux7VbeafT7i...