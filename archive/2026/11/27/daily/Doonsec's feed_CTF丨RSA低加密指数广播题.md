---
title: CTF丨RSA低加密指数广播题
url: https://mp.weixin.qq.com/s/artYzJHhsafnBpNv3VV0lg
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:38:34.623589
---

# CTF丨RSA低加密指数广播题

# CTF丨RSA低加密指数广播题

原创

予辉安全
予辉安全

予辉安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/2K4EpvaFFClay5IHWNuY8h7ATvaibnex5580qxT68BjT8K3c9zP3aOBTWbBRRky1z9dJ3RrS6iaxIPgepnTKEO6g/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAamAqcSDJ3CPHw9hjiaWWpKlqVPUNiaLshSw4grRroibfbib7E8AyCIC8ZNDzBsooCYlAfPtFViblUZZnmictoKK3hst0qKM7c4oibfVg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAbbMb1atCO66ib9b8qWb0yDT8ibbk3uZcO3gHSzplAhtz1LHs9uXhwx9mY3ZcicN4g7TL9zkB9BDuKxEj9X2wJn2NdEVjPjUFb0js/640?wx_fmt=png&from=appmsg)

**- 题目描述-**

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAZGVEX8sPO79qEPicz6pj1jUHSNELFq9xwuMLEFYW5ibpV7YqLxJomEaIh9XXlM1caIHtJiczf8fcZJsGljG9SwFxNiaSqoK8S4uJQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/CFR489vPHAaFs0azNnAKjgNfUP1pk9lWgRiasYSNKHBhBsQMKCjNwFtm2J4hbJQj3UL0ltlL4P8ddoJSXHYVKz5Nm5TdZZ7uhfibOsicLSFicG0/640?wx_fmt=png&from=appmsg)

下载附件分析可知每组包含密文 `c`、公钥指数 `e`、模数 `n`。其中 **e = 10 对所有组相同**，但每个 `n` 不同。

**-解题思路-**

---

这道题是典型的 **RSA 低加密指数广播攻击**。

当同一份明文 `m` 使用相同的较小公钥指数 `e`，在多个不同的模数 `n_i` 下加密时：![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAZnxycRze1ibY3zTGZkArbWwHLpacxkJ0ZPouVMvKEH88ajaZmT6GT8lmQ6RiblVMNeDgGDyDWicjST5HU49PxfZxVrOibIaVoH7QQ/640?wx_fmt=png&from=appmsg)如果满足：

1. 密文组数 **k ≥ e**（本题 k=10，e=10，刚好满足）
2. 所有模数两两互质
3. 明文未做随机填充，且![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAboEiaiaRf6mEvGWrnV3X9ibLc5DDhINm1U6bG8ZQPrVWvK7cG1g0oE6iaLb4gpOF5m0oNPq7NsHls713Ue89iaJ8y1PpUqaNCgkyCI/640?wx_fmt=png&from=appmsg)

那么就可以利用 中国剩余定理（CRT）将多组同余方程合并，直接还原出![](https://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAZbOcdKen6jDK9mlAqpbueW3269QcVMrXQBJfJE9DyRgcgurrUFrIlxm9icBRBM67Yy2ZhY6P0uG32pG0DhR2cjx7qEhFs2O4A4/640?wx_fmt=png&from=appmsg)的真实整数值，再开 e次整数根即可得到明文 `m`，全程无需私钥 `d`。

**-利用Pyhton脚本解题-**

---

```
import json, gmpy2from functools import reducedata = json.load(open("enc.txt"))cs = [x["c"] for x in data]ns = [x["n"] for x in data]e = data[0]["e"]N = reduce(lambda a,b: a*b,ns,1)M = sum(c * (N // n) * pow(N // n, -1, n) for c, n in zip(cs, ns)) % Nm = gmpy2.iroot(M,e)[0]print(int(m).to_bytes((int(m).bit_length() + 7)//8,"big"))
```

![](https://mmbiz.qpic.cn/mmbiz_png/CFR489vPHAb33Erib27I94wsGZ2IZECYkuH4u1TY3icicYUddMVZfg7eXX5iauuBYHZjrAjuVBCRibKibdvmwshvIPOWJn5cd4wSsHia6tBO6iciaqYo/640?wx_fmt=png&from=appmsg)

最后得到Flag：flag{wo0\_th3\_tr4in\_i5\_leav1ng\_g3t\_on\_it}

**End**

![](https://mmbiz.qpic.cn/mmbiz_png/2K4EpvaFFClay5IHWNuY8h7ATvaibnex5noCLyoyaxx7l2ChafzmKwtcOibIpFtuGcicwpdlpFLbHQhyqpnhTKwYg/640?wx_fmt=png&from=appmsg)

**文章都看完了，还不点个赞**

**回顾往期内容**

[CTF丨 PHPinfo信息泄露 Writeup 从环境变量中直接读取Flag](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484559&idx=1&sn=3951ea70c14c951f7a5ac62e34cf09b9&scene=21#wechat_redirect)

[CTF题目类型全解析](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484542&idx=1&sn=2d1d8745a5a3abecc9177fa7d108fd47&scene=21#wechat_redirect)

[CTF丨目录穿越 Writeup 从目录列表到Flag文件](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247484552&idx=1&sn=ca50597dbcc5000a8236f39401ebd5be&scene=21#wechat_redirect)

[SQL注入靶场显错注入（一）](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483818&idx=1&sn=41542d23e0391d2c390fd3bcadf9e179&scene=21#wechat_redirect)

[Sunny网络中间件](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483798&idx=1&sn=2c9305a9af4c7bc3d31e0228d87f0ebb&scene=21#wechat_redirect)

[JAVA代码审计：鉴权漏洞深度分析](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483756&idx=1&sn=57e00393f90e7753835dbb3fc6cf2941&scene=21#wechat_redirect)

[你不知道的表网、深网与暗网世界](https://mp.weixin.qq.com/s?__biz=MzI4MTE5NTY2OA==&mid=2247483745&idx=1&sn=f2d316ae89039789bd168250bac5cb14&scene=21#wechat_redirect)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/CFR489vPHAZUUSBMsWSmlOWp9D3ozPMI1Txp8Y9jy1cNvCjsok413nTBZP9SxUXLkicl8Hqd6S0eHHtqwEs1Fibk7LSk9oNWJqMxC9zbCULyQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过