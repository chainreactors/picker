---
title: b2801_[bagku] [MISC]_webshell流量分析 writeup
url: https://mp.weixin.qq.com/s/lI0cOVr6x6Bv8hbwAtJU8g
source: Doonsec's feed
date: 2026-05-03
fetch_date: 2026-05-04T05:26:39.741580
---

# b2801_[bagku] [MISC]_webshell流量分析 writeup

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/WTULWRVyhM3wrzwC0XmRkf7CsnLxg7soYNx1iaaNzicunjibmZzH93Tx76ReiaicSLibzxS43t7BIYfvNQ7au6x69Mtw/0?wx_fmt=jpeg)

# b2801\_[bagku] [MISC]\_webshell流量分析 writeup

原创

长弓三皮
长弓三皮

长弓三皮

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/WTULWRVyhM355SQ3VwNKn1t4icEDiatRdCHBOz48XCyqG12bFkJiaXVQ9NSK8d4sQxdDWAAeBnE3vxI7Kv8L16ulQ/640?wx_fmt=gif&from=appmsg)

***随波逐流工作室—-探索前沿科技，分享最新软件。点击标题下蓝字“******长弓三皮******”关注，我们将为您提供有深度、有价值、有意思的阅读。***

*朋友们，现在只对常读和星标的公众号才展示大图推送，建议大家把长弓三皮“设为星标”，否则可能就看不到了啦！*

作者：随波逐流

![](https://mmbiz.qpic.cn/mmbiz_png/WTULWRVyhM3WyznugvYy71CFweUXJfda3ibXhwJxiaWbHNxxaJP1mKV6eWq1CO9BhQ7ibAMCnhVtrFUEQW4dkUMuA/640?wx_fmt=png&from=appmsg)

**bagku MISC**

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXXsn1Db1FpkKxkl0ZFaO8ITuCbHAvfqGtGQKl85QzdT5frmBwM4cCpo6CpA3eA1T5nqoQ0ebcbRNDiaz3qnK0iczTYqWibJ9kUco8/640?wx_fmt=png&from=appmsg)

**随波逐流**

![](https://mmbiz.qpic.cn/mmbiz_gif/WTULWRVyhM0zic6S2ibB39fUwj77vFF6t89hX4SFM95tD8rTVMcuGs97WSOgYJxUj3CEjvic95S3lWTTAGjaXAUJA/640?wx_fmt=gif&from=appmsg)

**WriteUp**

这道题主要是用于测试新版的[随波逐流]CTF编码工具  PACP流量分析工具

题目下载 ：https://pan.quark.cn/s/93a63d273888

不管它是什么，先拖入 [随波逐流]CTF编码工具

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXWSLrzic9gJaD7htibZBIlpDVyZW8T4vtcNDkFSX8xaAibqVzRXrsQIjlMaZlBt4yoj2dHibSDOTibxBA0IavnaVORr5wdZB39jAKics/640?wx_fmt=png&from=appmsg)

 [随波逐流]CTF网络工具--文件--PACP流量分析

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXXN0C9eofib6bwVFgicvtYfYt3zHgFIx5FSJqcGyyThW9JwBfqU2BLIYYlvrVWJYXHRMWiaLh8ygrqVOvtR7seg45XrgjZMnfafHk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXUsUZFiapiaicwbKTibcq4SvNLWHHeKGbKeuvQCB5gHmrKOyBicpxW17EY7AzQACwESe8Y1crmP9HYYzI6jicd5h9z2fVLZdnl5ENJ50/640?wx_fmt=png&from=appmsg)

题目说了是黑客，黑客总要上传些东西，先看GET吧

[随波逐流]流量查看器--协议筛选--GET

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXWXmuPHsJXOzeThVqlftO35jNpfEJsFZEfz3Hb81d1JfB9malW83X7TPGicyaFXlnMdjMjPMlqt1ByEOOsWAfBfJuic4IsnXlaOY/640?wx_fmt=png&from=appmsg)

一片红啊，红色代表包含关键词，呵呵

一个个看，然后看到一个奇怪的东西

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXXvx3lEn6G7iabrk7avTjvFU58ic9AFQ6icE6EQrWhzhYldoQTqDIWjLltLGpOPQE6pwticvsGqwCWX0raoLnn2CMPXTT2MTSnGZ6Q/640?wx_fmt=png&from=appmsg)

GET /uploads/1768728211\_696ca6939300d\_san.php

右键-追踪流

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXVBjSQcYmibSibjrLUOQdWV80TRD25wD7bGK2aBHLojAFyOHheHhuNXnh5x8RrbTPrtwVkCNrSicQxbUtRbLwDfyLVHV96aPBb4S4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXUJLgT3gSCXd2cJMPIDEX6pGSZfwus4U6ajxrMEAx129ef5GhhRBsnlUib9HdFpsufvClrvuglu9lDoAXAuCxWAXp8wEEvogjWk/640?wx_fmt=png&from=appmsg)

呵呵

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXUWE2mQAJNPorj9oENzdsP8A2gFXPZHA61gg9P6XkNYNmdYaujxRFYGZ1u3XsRGaezJhPGgdgCDjfusWrpAMDww3w7TbqUqFw4/640?wx_fmt=png&from=appmsg)

方向：192.168.11.39:59980 → 192.168.11.93:80

$data = @$\_POST['shell']

问题1：黑客的 IP 地址是什么？

答案：192.168.11.39

问题2：黑客通过漏洞上传连接服务器的文件名字是什么？

答案：1768728211\_696ca6939300d\_san.php

问题4：黑客利用什么漏洞来进行攻击？A.SQL注入 B.文件上传 C.XXE D.反序列化漏洞

答案：文件上传

问题5：黑客连接 Webshell 的连接密码是什么？[明文]

答案：shell

知道密码是 shell，那就直接搜索shell

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXV3a0liaKVvNL2icH2adI7LoukFogWDNC8ia2LdqcFqicWicMicslHSTf1TwreG81g9D3hMdyjTKMia3nDZ5X4mQpicfTrich93EfSZ0ibkQ/640?wx_fmt=png&from=appmsg)

一个个看，第二个

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXVeAP4vhNdLUwYsEqnPT9HHPgGjKyQAkjODujWb62Oy3PB0hHgQ04nQCrH4wKqiaFibNCGGN21p1BvyQGYojhiaBc0dEozQ1BH8BM/640?wx_fmt=png&from=appmsg)

看shell=后面的数据

[随波逐流]CTF编码工具--编码转换--URL解密

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXUibmAyWcFKibLaX58ote59QZicyGiarYazEsehia1H7rasKS45Om7nL29ia7JCOMiaIZAQtLH5LdCUSEJRVQVcyJj6JkVlEVP63Yq0DE/640?wx_fmt=png&from=appmsg)

数据是用“|”分段，可以分段RSA解码

```
import base64from Crypto.PublicKey import RSAdef rsa_public_key_decrypt(cipher_b64, public_key_pem):    # 1. 导入公钥，取出 n, e    pub_key = RSA.importKey(public_key_pem)    n = pub_key.n    e = pub_key.e    # 2. Base64 解码密文    cipher_bytes = base64.b64decode(cipher_b64)    # 3. 转成大整数    cipher_int = int.from_bytes(cipher_bytes, byteorder='big')    # 4. RSA 公钥解密运算（核心：m = c^e mod n）    plain_int = pow(cipher_int, e, n)    # 5. 转回字节    plain_bytes = plain_int.to_bytes((n.bit_length() + 7) // 8, byteorder='big')    # 6. 去掉 PKCS1 填充（ToolsFx 逻辑）    if plain_bytes.startswith(b'\x00\x02'):        plain_bytes = plain_bytes.split(b'\x00')[-1]    return plain_bytesif __name__ == "__main__":    # 你的密文    cipher_b64 = "YTmeiI0qFHL9R5GScdFkn6YYss3SQq4+6G40D+9Tg1CmQhoEUcE8HEm3rINqbMR/NICLwQIIWErcATO0dW/9Kb8VB7h7ZbGAAoKdCXyb9tlJ4ipN7sHBZSeXGtOG/6CoaiAWwde6b5MIHgI8jPA+44Ougl2bxeNnYECEV5mVecI="    # 你的公钥（已清理掉多余的点）    public_key_pem = """-----BEGIN PUBLIC KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCd4MxZ+bp49Fy3KF/kfTUbOgaJVQTKVbvAEtA+mdowqmPZUKaE2R6EKgBoFSPdifyTtVDj3WjEezSYFiYOZlYwEYT6RhzwnmczKI/QKDq1+BUZqKF0FdyoQVJIo/3M5t+uBVswwlQ5l+eBo9fCdXqrI5xJxib6Z/MRrAYtbLkykwIDAQAB-----END PUBLIC KEY-----"""    try:        result = rsa_public_key_decrypt(cipher_b64, public_key_pem)        print("✅ 解密成功！")        print("明文：", result.decode('utf-8', errors='ignore'))    except Exception as e:        print("❌ 解密失败：", e)
```

```
✅ 解密成功！明文：   @ini_set("display_errors", "0");@set_time_limit(0);$opdir=@ini_get("open_bas
```

@ini\_set能明显知道是蚁剑（antsword）

问题3：黑客上传的 Webshell 用的什么工具连接？[小写英文]

答案：antsword

第三个

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXW0teZmwicUAKK08ZaQNrlnE6mP4QzKYQOVQCKCzg7gYZEicOcCPRJ81kdkYtZEjth7t5PCr8Uics4QFwXRbKI9iaaNqEJKFibyTQ3E/640?wx_fmt=png&from=appmsg)

上传了一个zip文件，504b开头的

复制出来 放到[随波逐流]CTF编码工具

[随波逐流]CTF编码工具--文件--16进制数据转文件

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXUsIIicbEcMdwhkSHUJVdDZfHjmEZTtkm36JfebWEHoTA26sibaIXhLfEdRaicpV2gsduQf1qdhiaqUqPXicMMQEEd4FLkiaHC3GuXD4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXXlataVNIWsq3Ect8bv3VIUgMgr4ibmuJPrO9Sic3hzuF8iaMbQPcIebUXzNwqSuYRwxsfaAk5TVICdsia4tS1xAxpJAVFFfN1BQVQ/640?wx_fmt=png&from=appmsg)

需要密码，问题7有提示   [2005????]

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXXqn3GZdv1xzWI39g1UpzuqQlvziboXtTm4KoMzv6a9LgCfQjnWywy5y1GDzOGibfMvexTBaaJTuR25PbPJ9dzntOwMsQZrlIdbg/640?wx_fmt=png&from=appmsg)

直接用ARCHPR软件掩码爆破，得到密码20050101

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXWfN5BdOiaAwatficvbSxYIibVkpGibT7c8icCicHzib1A5ykvqN75iaDMxZUf0r7ibIP4uTDtPszJZ4KenpbhYtM5Pwll9sedBbhfBeNYo/640?wx_fmt=png&from=appmsg)

问题7：黑客通过 Webshell 上传的文件内容是什么？[2005????]

答案：flag{443302daf6e587bc1d358dbf7a91e9b5}

蚁剑shell参数后面一般用&连接多个参数，通过参数就能知道发送的命令

继续查看下一条，到第5条，出现参数

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXXgZz1Gic3kpIZmotibRuicickr1zFx8d4I0pqu2ib1e488PicdicMVVlP7lBic6icuCR2XKgchxz9QYk4B0xqQ65HVibOnkQvAYqchHv6bM/640?wx_fmt=png&from=appmsg)

蚁剑参数可用base64解码（去掉前2位），有的需要先URL解码

[随波逐流]CTF编码工具--base--base64解密

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXXlUe04pnf9Q0jOUeZiaWZso5E8KJRMpwm6LXMkuDnrBbw0UtKLcQW6C0KzBVGiclzaZWEa4CWIrXLVgSUXWcLXB7s9khJB7hwBE/640?wx_fmt=png&from=appmsg)

搜索yae560609298d7=，

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXWic2zwtNShTcPTOSyw9iaLicrJu1Elibxibs2Wia2haUxXzeRmNvYQIGOSTGJ6tKYV82LTQH7Q8cEF1mSvhKeef7iakrhyqPhdemYslI/640?wx_fmt=png&from=appmsg)

逐条依次解密

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXWKMht7s04OE7g2NZTat3BiaPsfh0tb4e1viaQtwTRtzE4m5ialrXTw5Bnu7BfnK5iblPibcDOUIdWKnJvl9n9fWgD5eT7o5rNNtibOM/640?wx_fmt=png&from=appmsg)

这个先要URL解码，主要是将%3D换成=

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXW5WyUf3gLtsFuPJT5hhtIR76nKMGmsFHWSnjJlbWftKSZIepibfOl2Bm0WsUx4b5dZypffZicdVCAUfw4f0Vn8Kbep1TicAw2sCM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xKia4GpOxoXUaeg0icBG3FvWiaFvOsDSicCcCJt3ibZiaVdtCVibLIsN1yA98F9mTYubN33xqEYCqbAETUBibez0A1JlgPfpIVJLp5bP5TsR5ibicV1f8/640?wx_fmt=png&from=appmsg)

.......

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xKia4GpOxoXWugbGG1Ct1icYNOjyEFwpIEA6qeZUL4kHakDzia33bRQicEDmGoBz2twleXA97MgvibF1SicbfaiaKUMWtydUbLJyqYRbL34jBXYzGM/640?wx_fmt=png&from=appmsg)

问题6：黑客连接 Webshell 后执行的第一条系统命令是什么？

答案：whoami

问题8：黑客创建系统的用户名字叫什么？

答案：jiusan

要求：上传格式 flag{1-2-3-4-5-6-...