---
title: 【Web逆向】Yakit热加载之file.ReadFile+js.Run调用本地js加解密Vulinbox靶场CryptoJS.AES(CBC)
url: https://mp.weixin.qq.com/s/VBw6mTwWgf1Ff2cvgkizxQ
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:35:43.901642
---

# 【Web逆向】Yakit热加载之file.ReadFile+js.Run调用本地js加解密Vulinbox靶场CryptoJS.AES(CBC)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculOMzZVyG30ia2gsdEiaZwqNyf3GuOTQ8JibwTMfnW3hzbKFMQZgEgEocnA/0?wx_fmt=jpeg)

# 【Web逆向】Yakit热加载之file.ReadFile+js.Run调用本地js加解密Vulinbox靶场CryptoJS.AES(CBC)

原创

挖个洞先

挖个洞先

![]()

在小说阅读器中沉浸阅读

**“**

那美丽的天总是一望无边，

有粒种子埋在云下面。

营养来自这满地污泥，

生根发芽仍然顺从天意。——《向阳花》

**”**

01

—

环境版本

环境：

电脑，Windows 11 专业版 23H2

```
https://github.com/JiaoSuInfoSec/JiaoSuInfoSec_T00ls_Win11
```

软件：

Yakit， v1.4.5-0109

```
https://www.yaklang.com/
```

02

—

操作步骤

1、Yakit试验性功能，Vulinbox

```
https://oss-qn.yaklang.com/vulinbox/latest/vulinbox_windows_amd64.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculsk1tg4O6viaElsuKkl9hoU8o1mdtz3dfQXHwUqibiaztmamtTVrNiak4Dw/640?wx_fmt=png&from=appmsg)

2、启动靶场

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebcul7ykNtRn0MheIGa3icSHbM9KYW2uiaBYD3RiaOu24uqK6Hc5pXZoAJfxtw/640?wx_fmt=png&from=appmsg)

3、CryptoJS.AES(CBC) 前端加密登陆表单

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculBTrH1n4WeB2D2RdNR47rsosPz0mXnjwwNsH4PS6PULnsmx6PkYFwgQ/640?wx_fmt=png&from=appmsg)

4、用户名admin，密码从下面随机取值

```
backupPass = []string{"admin", "123456", "admin123", "88888888", "666666"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculGoUrpwojPLThCOJ2YlW31AJ7yZRbHEQfXc303sjjV0D38bhZsR8GNA/640?wx_fmt=png&from=appmsg)

5、请求加密

```
{"username":"admin","password":"88888888"}
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculpJReZy8lhMeCXJGpR1icdrSKktsjdycEict2CPXpR3ALRicfuib3SbJQwQ/640?wx_fmt=png&from=appmsg)

6、查看网页源代码

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculsDfVAEhfRNw1LIgN3zadz3YiaibKsnUeKHjHzCk502nNABkVQuCwErJg/640?wx_fmt=png&from=appmsg)

7、CryptoJS.AES，key为硬编码的字符串1234123412341234，iv随机生成

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculPLvROOd0ZWQtkLQnAnFBTpFUB3zInt0Ya0ftG06dmPZwLkAaTvfwuw/640?wx_fmt=png&from=appmsg)

8、编写js解密

```
function Decrypt(encryptedBase64, keyHex, ivHex) {    // 1. 将 Hex 字符串还原为 CryptoJS 的 WordArray 对象    var key = CryptoJS.enc.Hex.parse(keyHex);    var iv = CryptoJS.enc.Hex.parse(ivHex);    // 2. 使用相同的模式(CBC)和填充(Pkcs7)进行解密    var decrypted = CryptoJS.AES.decrypt(encryptedBase64, key, {        iv: iv,        mode: CryptoJS.mode.CBC,        padding: CryptoJS.pad.Pkcs7    });    // 3. 将解密后的数据转为 UTF8 字符串返回    return decrypted.toString(CryptoJS.enc.Utf8);}
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculJKm8kHn78iaJMDWDrMXQ7OMvDbCicsPrIvibBicQniaiaEzQcoNicVwmynufQ/640?wx_fmt=png&from=appmsg)

9、编写热加载实时解密请求

```
// 1. 设置 JS 文件路径// 注意：Windows路径分隔符需要转义，用双反斜杠 \\jsFilePath := "C:\\Users\\Administrator\\Desktop\\js\\1.js"// 2. 读取文件内容// file.ReadFile 返回 ([]byte, error)jsBytes, err := file.ReadFile(jsFilePath)if err != nil {    die("读取JS文件失败: " + err.Error())}// 转换成字符串备用DecryptJS := string(jsBytes)// 3. 定义流量钩子hijackSaveHTTPFlow = func(flow, modify, drop) {    // 过滤 URL    if !str.Contains(flow.Url, "/crypto/js/lib/aes/cbc/handler") {        return    }    // 反转义请求    reqBytes, err := codec.StrconvUnquote(flow.Request)    if err != nil {        return    }    // 获取 Body    bodyBytes := poc.GetHTTPPacketBody(reqBytes)    if len(bodyBytes) == 0 {        return    }    // 解析 JSON    jsonObj := json.loads(bodyBytes)    if jsonObj == nil {        return    }    // 提取参数    encData := jsonObj["data"]    keyStr := jsonObj["key"]    ivStr := jsonObj["iv"]    if encData == nil || keyStr == nil || ivStr == nil {        return    }    // ==========================================    // 4. 运行 JS (使用读取到的文件内容)    // ==========================================    // 加载读取到的代码 (DecryptJS) 和 CryptoJS 库    vm, _, err := js.Run(DecryptJS, js.libCryptoJSV4())    if err != nil {        println("JS环境加载失败，请检查 1.js 语法: " + err.Error())        return    }    // 拼接执行命令    runCmd := sprintf(`Decrypt("%v", "%v", "%v")`, encData, keyStr, ivStr)    // 执行    val, err := vm.RunString(runCmd)    if err != nil {        println("JS执行错误: " + err.Error())        return    }    plaintext := val.String()    if plaintext == "" {        return    }    // 5. 替换流量    newReqBytes := poc.ReplaceHTTPPacketBody(reqBytes, []byte(plaintext))    flow.Request = codec.StrconvQuote(newReqBytes)    flow.AddTag("本地JS解密成功")    flow.Red()     modify(flow)    println("从文件加载JS并解密成功: " + plaintext)}
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculWjfibaslaHj4oy0xVx15Nxibv2NbLsuDzEPu1bQjRSibfsiavdBBibvvraw/640?wx_fmt=png&from=appmsg)

10、直接明文发包报错

```
Failed: decrypt failed: AES key length must be 16, 24, or 32 bytes, got 0 bytes
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculA504vphVCAHNrxdWFfUDuMkBibmT68fKcY7S0W2f9wRicZMVvuIYCiamg/640?wx_fmt=png&from=appmsg)

11、编写js加密

```
// ================== 解密函数 (用于 afterRequest) ==================function Decrypt(encryptedBase64, keyHex, ivHex) {    var key = CryptoJS.enc.Hex.parse(keyHex);    var iv = CryptoJS.enc.Hex.parse(ivHex);    var decrypted = CryptoJS.AES.decrypt(encryptedBase64, key, {        iv: iv,        mode: CryptoJS.mode.CBC,        padding: CryptoJS.pad.Pkcs7    });    return decrypted.toString(CryptoJS.enc.Utf8);}// ================== 加密函数 (用于 beforeRequest) ==================function EncryptData(jsonStr) {    // 1. 密钥 (必须与网页源代码中的逻辑一致)    var keyStr = "1234123412341234";     var key = CryptoJS.enc.Utf8.parse(keyStr);    // 2. 生成随机 IV (16字节)    var iv = CryptoJS.lib.WordArray.random(16);    // 3. 执行加密    var encrypted = CryptoJS.AES.encrypt(jsonStr, key, {        iv: iv,        mode: CryptoJS.mode.CBC,        padding: CryptoJS.pad.Pkcs7    });    // 4. 构造并返回服务器需要的 JSON 字符串    var result = {        "data": encrypted.toString(),        "key": key.toString(), // WordArray 转 Hex        "iv": iv.toString()    // WordArray 转 Hex    };    return JSON.stringify(result);}
```

![](https://mmbiz.qpic.cn/mmbiz_png/l0h9T8I4fFtbb3A7a7CtV1ObTWoebculCbPKgBUQWYzicwiae1ic7Ehq6kISnrUOtOk6JCZZK0TGz9r4cf79Rkpvg/640?wx_fmt=png&from=appmsg)

12、Web Fuzzer热加载

```
// 设置 JS 文件路径 (注意双反斜杠)jsFilePath = "C:\\Users\\Administrator\\Desktop\\js\\2.js"// ==========================================// 发送请求前：将明文 Body 加密为 密文 Body// ==========================================beforeRequest = func(https, originReq, req) {    // 1. 读取本地 JS 文件    jsBytes, err := file.ReadFile(jsFilePath)    if err != nil {        println("JS文件读取失败: " + err.Error())        return req    }    // 2. 获取 Fuzzer 生成的明文 Body    // 例如: {"username":"admin", "password":"123"}    bodyBytes := poc.GetHTTPPacketBody(req)    if len(bodyBytes) == 0 {        return req    }    // 3. 运行 JS 环境    vm, _, err := js.Run(string(jsBytes), js.libCryptoJSV4())    if err != nil {        println("JS环境启动失败: " + err.Error())        return req    }    // 4. 调用 JS 中的 EncryptData 函数    // 注意：将 bodyBytes 转为 string 传入    // 这里的 sprintf 可能会因为 body 含有特殊字符而出错，但在爆破密码场景通常没事    runCmd := sprintf(`EncryptData('%s')`, string(bodyBytes))    val, err := vm.RunString(runCmd)    if err != nil {        println("加密执行错误: " + err.Error())        return req    }    encryptedJson := val.String()    if encryptedJson == "" {        return req    }    // 5. 替换请求体 (明文 -> 密文)    newReq := poc.ReplaceHTTPPacketBody(req, []byte(encryptedJson))    return newReq}// ==========================================// 收到响应后：将密文 Body 解密为 明文 Body// ==========================================afterRequest = func(https, originReq, req, originRsp, rsp) {    // 1. 读取本地 JS 文件    jsBytes, err := file.ReadFile(jsFilePath)    if err != nil {        return rsp    }    // 2. 获取响应体    bodyBytes := poc.GetHTTPPacketBody(rsp)    if len(bodyBytes) == 0 {        return rsp    }    // 3. 解析响应 JSON (提取 data, key, iv)    jsonObj := json.loads(bodyBytes)    if jsonObj == nil {        return rsp    }    // 检查是否包含加密字段    if jsonObj["data"] == nil || jsonObj["key"] == nil || jsonObj["iv"] == nil {        return rsp    }    // 4. 运行 JS 环境    vm, _, err := js.Run(string(jsBytes), js.libCryptoJSV4())    if err !...