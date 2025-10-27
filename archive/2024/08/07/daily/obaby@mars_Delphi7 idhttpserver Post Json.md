---
title: Delphi7 idhttpserver Post Json
url: https://h4ck.org.cn/2024/08/17770
source: obaby@mars
date: 2024-08-07
fetch_date: 2025-10-06T18:02:51.399097
---

# Delphi7 idhttpserver Post Json

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[后台开发『BackEnd』](https://h4ck.org.cn/cats/cxsj/backend)

# Delphi7 idhttpserver Post Json

2024年8月6日
[31 条评论](https://h4ck.org.cn/2024/08/17770#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1076.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/08/WechatIMG1076.jpg)

万万没想到，多年以后还会重新写 delphi 7 的代码。当然，代码不是全部都是自己写的，在原有的 demo 的基础上增加了一些功能。

其中，有一个需求就是需要能够远程接收 http post 的请求，请求方式是 post，数据格式是 json。然而，多年不写代码，在网上随便一搜，搜到的代码感觉都是同一个地方抄来抄去实现的，在处理 poststream 的时候都会出问题。

直到翻到了下面的代码，https://www.cnblogs.com/yangxuming/p/12462459.html

```
1 procedure TForm1.IdHTTPServer1CommandGet(AContext: TIdContext; ARequestInfo: TIdHTTPRequestInfo; AResponseInfo: TIdHTTPResponseInfo);
 2 var
 3   tmp: UTF8String; //也可以是 array of AnsiChar; 不能用RawByteString或 widestring
 4   tmpstr: string;
 5   size: Integer;
 6   JSONObject: TJSONObject; // JSON类
 7   i: Integer;
 8   jo: ISuperObject;
 9 begin
10   size := ARequestInfo.PostStream.size;
11   SetLength(tmp, size);
12   ARequestInfo.PostStream.Position := 0;
13   ARequestInfo.PostStream.ReadBuffer(tmp[1], size); //tmp为array of AnsiChar时为tmp[0]
14   tmpstr := UTF8ToString(tmp);
15
16   jo := SO(tmpstr);
17   Memo1.Lines.Add(jo['test'].AsString);
18 20   kbmMemTable1.Append;
21   kbmMemTable1.FieldByName('test').AsString := jo['test'].AsString;
22   kbmMemTable1.Post;
23
24 //  Memo1.Lines.Add(ExtractFilePath(Application.ExeName) + 'testPrint.fr3');
25
26   frxReport1.LoadFromFile(ExtractFilePath(Application.ExeName) + 'testPrint.fr3');
27   frxReport1.PrintOptions.ShowDialog := false;
28   frxReport1.ShowProgress := False;
29   frxReport1.PrepareReport;
30   frxReport1.Print;
31
32 //  JSONObject := TJSONObject.ParseJSONValue(Trim(tmpstr)) as TJSONObject;
33 //  for i := 0 to JSONObject.Count - 1 do
34 //    Memo1.Lines.Add(JSONObject.Pairs[i].JsonString.ToString + '=' +
35 //      JSONObject.Pairs[i].JsonValue.ToString);
36 end;
```

这里的处理逻辑是争取的，poststream 貌似不能直接将 stream 转换为 stringstream 或者 memorystream，在后续的转换过程中会出错，当然，也可能是由于 stream 的Position位置异常导致的。

另外 一个问题就是处理 json，网上的代码多数都是一笔带过，但是这个一笔带过就很烦人，找个可用的 json 库也比较麻烦，TJSONObject这个东西，看很多代码说都是内置的，但是实际在使用的时候，会提示找不到这个类。

所以，可以借助第三方的 json 库，例如https://github.com/frostney/superobject

通过这个东西来解析 json 就简单多了：

```
var
  obj: ISuperObject;
begin
  obj := SO('{"foo": true}');
  obj := TSuperObject.ParseString('{"foo": true}');
  obj := TSuperObject.ParseStream(stream);
  obj := TSuperObject.ParseFile(FileName);
end;
```

```
val := obj.AsObject.S['foo']; // get a string
 val := obj.AsObject.I['foo']; // get an Int64
 val := obj.AsObject.B['foo']; // get a Boolean
 val := obj.AsObject.D['foo']; // get a Double
 val := obj.AsObject.O['foo']; // get an Object (default)
 val := obj.AsObject.M['foo']; // get a Method
 val := obj.AsObject.N['foo']; // get a null object
```

现在 ai 生成的代码质量的确也是个问题，这些小众（当前）语言生成的效果就更差了。

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Delphi7 idhttpserver Post Json》](https://h4ck.org.cn/2024/08/17770)
\* 本文链接：<https://h4ck.org.cn/2024/08/17770>
\* 短链接：<https://oba.by/?p=17770>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Delphi](https://h4ck.org.cn/tags/delphi)[json](https://h4ck.org.cn/tags/json)

[Previous Post](https://h4ck.org.cn/2024/08/17775)
[Next Post](https://h4ck.org.cn/2024/08/17763)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2025年1月1日

#### [哪吒监控 1.5.1 自定义头像](https://h4ck.org.cn/2025/01/18912)

2012年12月11日

#### [再谈WindowsBlinds 7.4的试用期](https://h4ck.org.cn/2012/12/4825)

2010年12月16日

#### [文件夹智能同步工具1.0 （美化版）](https://h4ck.org.cn/2010/12/2254)

### 31 comments

1. ![](https://gg.lang.bi/avatar/d838166f05390e17979f10c8e0fcc3b1d719369e6450e9eb30f218d8579263ee?s=64&d=identicon&r=r) **[dujun](https://dujun.io/)**说道：

   [2024年8月6日 17:14](https://h4ck.org.cn/2024/08/17770#comment-117924)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 7](https://badgen.net/badge/亲密度/Level 7/pink?icon=codebeat)

   ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   太久远了，找不到人维护了，能不动就不动。

   [回复](#comment-117924)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年8月6日 17:23](https://h4ck.org.cn/2024/08/17770#comment-117926)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      给的编译的 32 位的 dll，java 加载不了，不知道神马情况。就 delphi 的代码能加载，并且功能目前看起来还算正常。

      [回复](#comment-117926)
2. ![](https://gg.lang.bi/avatar/58a79d6c1371a10b17245e3121ec03aaebb1c4d40ee32b0e3fd717fc45d953d4?s=64&d=identicon&r=r)

   [2024年8月6日 19:20](https://h4ck.org.cn/2024/08/17770#comment-117928)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 3](https://badgen.net/badge/亲密度/Level 3/green?icon=codebeat)

   ![Microsoft Edge 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 127") Microsoft Edge 127 ![Windows 10](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 10") Windows 10 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   delphi ，好多年没听过这个名字了

   [回复](#comment-117928)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年8月6日 19:21](https://h4ck.org.cn/2024/08/17770#comment-117929)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      可不，上古时期了得追溯到

      [回复](#comment-117929)
3. ![](https://gg.lang.bi/avatar/65cd1f408c1cc0949b34d3cd2acad0cb5a2b8c362ebf31ca9ee0dc9edcc63e81?s=64&d=identicon&r=r)

   [2024年8月7日 00:03](https://h4ck.org.cn/2024/08/17770#comment-117931)

   ![](https://badgen.net/badge/友链/集美们/blue?icon=chrome) ![Level 6](https://badgen.net/badge/亲密度/Level 6/red?icon=codebeat)

 ...