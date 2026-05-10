---
title: 扩展Burp Suite：用Montoya API给你的工具加个\"解密\"标签（第四部分）
url: https://mp.weixin.qq.com/s/Q3rg0izsupgfLHCsKgqdBg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:33:06.533871
---

# 扩展Burp Suite：用Montoya API给你的工具加个\"解密\"标签（第四部分）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibcQ9xhiaJMyWV9p6jWk7wUy3j8c0tGZVtxSqlVkia73TYOoOibLID9PKn2CW67huVTndkQRGibFaLuecrWCzhjFfASZArXlubxm9j0/0?wx_fmt=jpeg)

# 扩展Burp Suite：用Montoya API给你的工具加个"解密"标签（第四部分）

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 本文教你用Burp Suite Montoya API创建自定义选项卡，一键解密HTTP请求和响应。通过一个AES加密的移动应用场景，手把手实现HttpRequestEditor/HttpResponseEditor插件，让安全测试不用每次手动加解密。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibd3ibvZMQJckx4SfhP45f0yKd4U9W2a9fmcocTTyILwvD2BpRbaOnHUdYey6kv5gFTmAebO7CkqJ3SicHmKNsUlOiavrmyibedZDVw/640?wx_fmt=png&from=appmsg)

Hi，各位。

今天聊怎么给Burp Suite界面加自定义组件，方便处理各种加密场景。重点放在创建新选项卡，用来处理HTTP请求和响应。

老规矩，先讲一个具体场景。假设你在测一个移动应用，它对HTTP请求体和响应体都做了AES加密。客户端发请求前用AES加密体，收到响应后用同样方式解密——后端也是这么干的。移动端常见这情况，但Web端也有，浏览器用JavaScript库做加解密。

我给你写个简单的Flask Python应用，演示这个过程（加解密代码直接抄的StackOverflow，需要的包：flask和pycryptodome）：

import flask
from flask import request
import base64
from Crypto import Random
from Crypto.Cipher import AES

app = flask.Flask(\_\_name\_\_)

bs = AES.block\_size
key = bytes.fromhex("eeb27c55483270a92682dab01b85fdea")
iv = bytes.fromhex("ecbc1312cfdc2a0e1027b1eaf577dce8")

def encrypt(raw):
    raw = \_pad(raw)
    cipher = AES.new(key, AES.MODE\_CBC, iv)
    return base64.b64encode(cipher.encrypt(raw.encode()))

def decrypt(enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE\_CBC, iv)
    return \_unpad(cipher.decrypt(enc)).decode('utf-8')

def \_pad(s):
    return s + (bs - len(s) % bs) \* chr(bs - len(s) % bs)

def \_unpad(s):
    return s[:-ord(s[len(s)-1:])]

@app.route('/', methods=['POST'])
def handle\_request():
    encrypted\_body = request.get\_data()
    decrypted\_body = decrypt(encrypted\_body)
    response = "Your request was: \"" + decrypted\_body + "\""
    encrypted\_response = encrypt(response)
    return encrypted\_response

app.run(host="127.0.0.1", port=5000, debug=True)

这个应用接收加密的请求体（AES/CBC，固定Key和IV，Base64编码），返回同样加密的响应。所以请求和响应都是密文，没Burp插件根本没法测。

懒得写个移动应用demo，直接在Burp Repeater里伪造一个HTTP请求。用CyberChef加密请求体，再解密响应。等插件写好，这些脏活就交给插件了。

先用固定Key和IV加密一个测试句子：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdjrO2BwmVd41YnY5dh1NhYmAYbbL48lZdYGshwxjYVzkrvlgjH1JnY284QmdTfiaMlWrL8eibZr7XaDnianVe7ce4ay6KjE4ibQBk/640?wx_fmt=png&from=appmsg)

然后通过Burp Repeater发给后端：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfetHr3febFt0LPqDuCjEOpO4ecpxblu73PvicScgNpnJEWw2uibyAO1E799LfyMXXdcicicficGL8UgHCKMCUNGX09zO0DeACZZ2aE/640?wx_fmt=png&from=appmsg)

再用CyberChef解密响应：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdGhdovuWvrcxicicdAPO7xafY0REmuZRD3Rciag6vRMD4cTkHafaqFSDV2Y38HDP2zVx4NqMBp7JicUSoYGvyg2yqa1iaWMTN8Ok1k/640?wx_fmt=png&from=appmsg)

好，后端代码没毛病。

现在想想怎么解决问题。目标是方便地分析应用，不用每次输完payload手动加密请求、解密响应看攻击结果。

一个思路是实现HttpHandler插件（参考本系列第二部分），透明地解密进入Burp的请求，再自动重新加密发送出去。这样Burp里看到的流量就像没加密一样，好处是Scanner也能无缝工作。但我通常只在Scanner和Intruder用这种插件，Proxy和Repeater不用。为啥？我想保留原始流量记录，而不是经过插件处理后的，方便后续回看。

下面说两种替代方案：用HttpRequestEditor/HttpResponseEditor插件（我常用的），和ContextMenuItem插件（灵活性差点，但适合请求格式变化大的场景）。这两种都要从UserInterface对象注册，UserInterface从MontoyaApi拿到。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd5ReSCd8nnHqjJWK5ibGibX640aQW3FvtC4sZem2sw2tJhAkfRNiaGpbLicr8icguueDJONfMmaX8nCZAGuU6KFaIHCG8qLZRhzubU/640?wx_fmt=png&from=appmsg)

这篇文章重点讲HttpRequestEditor/HttpResponseEditor。ContextMenuItem留到下一篇。

这类插件可以在Burp显示请求/响应的区域加一个选项卡。点一下，插件就解密请求并展示解密版本（响应同理）。要是在支持修改的工具里（比如Repeater或Intercept），你还能修改解密后的内容，插件自动重新加密再发出去。这样既保留了原始流量，又像没有加密层一样工作。实际效果长这样：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibfNSNQL76J7jSEWuZsYxmXlGNgoJiaxwjdT4wGCBGibfovGUzCGWVIbiaVwgZ6B1ECYMNia3qS7tkHGxHNUn4Rlg7hibhdS0ql05Fyg/640?wx_fmt=png&from=appmsg)

从第一部分的Hello World框架开始：

package org.fd.montoyatutorial;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.logging.Logging;

public class HttpRequestResponseEditorExample implements BurpExtension {

    MontoyaApi api;
    Logging logging;

    @Override
    public void initialize(MontoyaApi api) {
        this.api = api;
        this.logging = api.logging();
        api.extension().setName("Montoya API tutorial - HttpRequestResponseEditorExample");
        this.logging.logToOutput("\*\*\* Montoya API tutorial - HttpRequestResponseEditorExample loaded \*\*\*");
        // TODO - 注册监听器
    }
}

扩展需要注册两个监听器，一个处理请求，一个处理响应。看文档：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibd9ap1DYjVYCDhNq4ICCWd364OUd8NywpWxuqGnozfJEgBOiaWLcfI2fHuRhjjClGfXOeyCS73Qobx6j8S6YibwXyu36RICmB9I4/640?wx_fmt=png&from=appmsg)

每个监听器需要实现特定接口的对象：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfAgiadskZlvTIyvBYDZsux1tH5uLIs4c7p0It8s48rtS5CDib2RgcdkUj7ckY0tavVYrY3oIibpO3DqNx7TYALUztthS9drz5Vd4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibdGrSJYv5gzmzdab4fJvRqLib97loPibSN2oCrwJfl7p54Ue6V3IWmCIRTB6UOsqeMLYic7BTzcFRTv0Vz13FWMCpVw2UOL163xib4/640?wx_fmt=png&from=appmsg)

两个接口都很简单，每个只需要一个方法。我打算用一个Java类同时实现两个接口，当然你也可以分开写。

package org.fd.montoyatutorial;

import burp.api.montoya.MontoyaApi;
import burp.api.montoya.ui.editor.extension.\*;

public class CustomHttpRequestResponseEditor implements HttpRequestEditorProvider, HttpResponseEditorProvider {

    MontoyaApi api;

    public CustomHttpRequestResponseEditor(MontoyaApi api) {
        this.api = api;
    }

    @Override
    public ExtensionProvidedHttpRequestEditor provideHttpRequestEditor(EditorCreationContext creationContext) {
        // TODO
    }

    @Override
    public ExtensionProvidedHttpResponseEditor provideHttpResponseEditor(EditorCreationContext creationContext) {
        // TODO
    }
}

这两个方法分别返回ExtensionProvidedHttpRequestEditor和ExtensionProvidedHttpResponseEditor对象。看名字你就知道，它们负责创建和返回一个图形选项卡。好消息是Burp API提供了创建选项卡的方法，不用自己跟Java图形库死磕（谢天谢地）。我们只需要用API创建选项卡，在里面实现加解密逻辑。

回到provideHttpRequestEditor和provideHttpResponseEditor，它俩的参数都是EditorCreationContext，包含当前请求/响应的上下文信息（哪个Burp工具生成的，是否可编辑）：

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibcytw1HQ6AR05brNe26U9JtwCua0LsJQ9vCYxL0JE255MIjFTfPaaXfeclPqWdvcgzf4ibgok8xibjgjaWgw8W0sN1xibeh4beMxs/640?wx_fmt=png&from=appmsg)

下面看怎么创建ExtensionProvidedHttpRequestEditor对象（只讲请求部分，响应完全一样，代码在GitHub仓库里都有）。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6Tibe1s5noib7akyAWjTjLUVg2Kca0KTP47fiarpQgequKeHUpRA4vC95zicwtPV3ibQgdHDLbC6TokYngrxwdeC9uanDdGEF1HlJvzMM/640?wx_fmt=png&from=appmsg)

需要实现一个接口，定义以下方法：

* caption：返回自定义选项卡的名字（示例里叫"Decrypted"）。
* isEnabledFor：根据当前请求和上下文决定是否显示这个选项卡。
* uiComponent：返回实际的UI组件。不用写Swing代码，Burp有现成方法生成选项卡。
* setRequestResponse：在这里生成选项卡的内容（比如解密请求体放进去）。
* isModified：用户有没有修改过选项卡内容。
* getRequest：当用户离开自定义选项卡回到默认选项卡，或者发送请求时调用。如果用户修改了内容，在这里把编辑后的内容加密，构建新请求。
* selectedData：返回用户在选项卡中选中的数据（如果有）。Burp API生成的选项卡自带方法处理这个，我们这个插件不需要让用户选中部分请求。

先写个骨架，把简单方法实现，然后处理setRequestResponse和getRequest——这里有加解密逻辑。

先写构造函数：

public class CustomHttpRequestEditorTab implements ExtensionProvidedHttpRequestEditor {

    static String keyHex = "eeb27c55483270a92682dab01b85fdea";
    static String ivHex = "ecbc1312cfdc2a0e1027b1eaf577dce8";

    MontoyaApi api;
    Logging logging;
    EditorCreationContext creationContext;
    RawEditor requestEditorTab;
    Base64Utils base64Utils;

    public CustomHttpRequestEditorTab(MontoyaApi api, EditorCreationContext creationContext) {
        this.api = api;
        this.creationContext = creationContext;
        this.logging = api.logging();
        this.base64Utils = api.utilities().base64Utils();
        if (creationContext.editorMode() == EditorMode.READ\_ONLY) {
            requestEditorTab = api.userInterface().createRawEditor(EditorOptions.READ\_ONLY);
        } else {
            requestEditorTab = api.userInterface().createRawEditor();
        }
    }
    [...]

构造函数传入MontoyaApi和上下文，保存一些工具对象。然后创建RawEditor对象——这就是我们的图形选项卡。根据当前请求是否只读（比如History里只读，Repeater或Intercept里可读写），创建只读或可读写编辑器。RawEditor提供了很多方法，后面会用到。

![](https://mmbiz.qpic.cn/mmbiz_png/tbTbtBE6TibclekN9xlrkO5jQN4C5lCDHQL4MrWEFQjjsapjH5KT6ibmbib6B5icCAJEA5E49vcOw5jeAboib7lrOtZACXUozGYW95oZHupF7X54/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdsV...