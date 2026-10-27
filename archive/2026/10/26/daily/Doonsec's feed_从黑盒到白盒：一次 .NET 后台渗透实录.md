---
title: 从黑盒到白盒：一次 .NET 后台渗透实录
url: https://mp.weixin.qq.com/s/BznAnmylt410IApnbiYjcQ
source: Doonsec's feed
date: 2026-10-26
fetch_date: 2026-10-27T06:59:50.477482
---

# 从黑盒到白盒：一次 .NET 后台渗透实录

# 从黑盒到白盒：一次 .NET 后台渗透实录

youki
youki

C4安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、登录框常规测试

原文：https://forum.butian.net/share/5116，作者：轩公子

目标是一个常见的后台登录页面。先用插件扫了一遍接口，不出所料，全部返回 403。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNnMMvO06a8E0brylb1icLTgq9B58AaueVayqZQDR6ZrneUmTtrG3cVUOWDrlD2nfGHMIOs0WTGiatO5XkYGuia0hzBeWnJxZ2xick/640?wx_fmt=png&from=appmsg)

抓登录包看数据格式，发现是 JSON 提交。本来想试试 Fastjson 反序列化，但响应头暴露了服务器信息：**IIS 7.5 + ASP.NET 8**，Java 那一套漏洞直接排除。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNVVTpbmR8chGDVOGMvobfoShvx31icEaJ195HnDBJibLicD9sODlicfo4XZNVnRwVaWgn2N11JhMcbzuFVs1RhYLQ4oDL5ROIJibbI/640?wx_fmt=png&from=appmsg)

转向爆破弱口令，却发现验证码无法绕过——删除验证码字段返回"不能为空"。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPFibSgGxub9401QkpVoN9hotMwpia70PZQvcyHAbDX8MfCbfWalJe92QfIYObbjvJicaFRzX9Yp1At4Dic1icN24ayBB7mhrNrI6jk/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNJKeA73d8u83ZGJBlrrkicWtgnpWuDV4wSkrJEWfjq6wztpU1A1q9PhlRojSo33M65PQgia6P65yQu7XKtv6ZrUT59HC8TEFKfs/640?wx_fmt=png&from=appmsg)

有人可能会说用 OCR 识别，但这里的验证码是 Base64 内嵌的，现有爆破工具都不支持，需要写中转脚本配合，较麻烦，先放一放。

于是我又想到了，修改返回包，看看能否中个奖，绕过登录。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPRujUfwf187op2Fa3JeKKicRg9eBO5Q8dOyeZic5VZZbQ9b40rpMa0jib8ic3GjMTsU1utRNFo3rUnL9wA45HfuJibFPhtG9DibXZnc/640?wx_fmt=png&from=appmsg)

返回了，jwt 认证格式，我寻思，jwt 不都是 java 里面的，net 竟然也会有

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CP4rhszBWqsZkrGaAlkPCic1QqEic2PsGZAuLh0LY3jD6Rk76rOXM9lBibDZXcLbCzjoUohG6yzQKql2BLibEDPIdoVkMMTibZjl1oo/640?wx_fmt=png&from=appmsg)

于是f12，全局搜索关键字，翻找半天，并未发现相关的参数，点燃的希望又破灭了

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPic4MBiaCYwTicGuYpIBZfMRzylDqB2WAV8WBUMiafvFu3hFPBqrEqJsJjYiaSBsppmzgcgrTW0C1nvibMEowMfvD8SKaaeUsHUzDtk/640?wx_fmt=png&from=appmsg)

常规思路走完一遍，还是没有突破，剩下最后一招：扫目录。

二、Swagger 未授权访问

目录扫描命中了 Swagger 接口文档。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CN5laGQMDwqicHwjMBURUhOR0E1Jboy3uwObJ68s6g9LWAN1wSXNq21vwY6uuEIKOIQh2PIJ0fbY2kXgccxxamoOsxJWUnBl67U/640?wx_fmt=png&from=appmsg)

文档里列出了大量后台接口，但绝大多数都需要鉴权，只有两三个字典类接口能匿名访问，且不含敏感信息。

不过有一个有价值的收获：响应中暴露了后端框架信息——Vol.Core（一个开源的 .NET 后台框架）。

三、源码审计：定位加密逻辑

既然知道了框架，直接下载源码审计。

翻到 SQL 初始化文件，里面存了默认管理员密码，但是 Base64 解不开，说明是加密存储，需要找密钥。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNvW6tGxbHny0iaMfl2MBoTrYLzlQYTWRXgLapLG5YyAC3bX7gX1th51XJnuslwky7aLF4DTdMKdYqz3jJgTnfXXTyLl8BWrdwk/640?wx_fmt=png&from=appmsg)

接着翻配置文件，找到了 Key。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPNUE1RRQl1ic44DdDsOPjE5e5rmURP5wLOGrwP5E9oDiawhpjXJql8oic7N0WmiaytEQCsribzO11KJkn6tulQibSicbMicwsYKpAy60w/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPPia1IbVSciazPuuTSZydjicINZxTj0ziazC4S9XdJgbc1qvib9jaic1hjibGajhqpkPaAmvTYb3yLNETxVQrm5xBbbVG4lKY9NTicP18/640?wx_fmt=png&from=appmsg)

但直接拿这个 Key 还是解不出来，说明加密逻辑不是简单的 **AES/DES**。全局搜索**decrypt**定位解密函数。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CP4ibvvZ5gK7Sd5mHVk5AH8a8bOdsF6O0ETeylV5Sv4LTw5HmicnwNplhMCA7A3qTb8jvF4ZYyOfuwl1feTdmJx0lbakia01noul0/640?wx_fmt=png&from=appmsg)

发现一个有意思的地方：函数命名是 Des，但内部实际调用的是 AES。密钥取配置值的前 16 位。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPos7IKkj6e5QXTFE0a2xiajuZ5ibpepykB85hAzgqugUH2a067RaGnsSficEEKVrD8aNLwPyK0dXKowq0KA68QwsSyiamILW7jXOA/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CMuCyB7OxEFX6foDuhbKrGe4NsGSXoSuMlicjQDgVwNHzXyicGO9jsOAQYEDicJLqHEtpGuS1rgeqBOoBfol0yZibSvwDsCAK0MfTg/640?wx_fmt=png&from=appmsg)

解密成功，拿到默认 admin 密码，登录——失败。说明默认密码已被修改。

四、JWT 伪造：第一次尝试

思考片刻：配置文件里同时存在 JWT 密钥，如果默认密钥没改，直接伪造 Token 就能进后台。

伪造 Token 需要知道参数结构，前端没有，但这是后端，继续全局搜索 jwt，定位到核心生成逻辑。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COcfoKTun59n7Uia2ibnEjARzkSl4lDAFY3skpl8uBV806hkQycNF1V1N0A3hspDYjzaOMcVp9HoanjrgaotbeEr2XBDBeSaGfHw/640?wx_fmt=png&from=appmsg)

需要六个字段：

```
jti	用户ID
iat	当前时间戳
nbf	当前时间戳
exp	过期时间戳
iss	配置中的 Issuer
aud	配置中的 Audience
```

构造 Payload：

```
{
  "jti": "1",
  "iat": "1788013440",
  "nbf": "1788013440",
  "exp": "1788020640",
  "iss": "vol.core.owner",
  "aud": "vol.core"
}
```

用 配置文件里的密钥签名后请求——401。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPpoufU1ZLlFWVXve901A7elZwGIHX0wu5x30btpInrSaUL60atq03MtibhM0sk9RmFHTcJpQg67hummsPIKNaBJ6g1wceQcDQc/640?wx_fmt=png&from=appmsg)

说明 JWT 密钥也被改了。继续硬刚的话，只能审未授权漏洞或前台 RCE

但审了半个多小时，确认 Swagger 里的接口和代码里的接口一一对应，不存在未授权接口。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPCQibgDzcgpqsbKP97mBdx4fNGKvxV3vpre3SLmHyGicWbrBiaerGqhHrv7aumXcUIxDTibRTPcJlwJ9a9CaLJbkyesNTJ01JvtZY/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CP8icQ832nr4CChXBpibP0pxZhHAf2mibg3YIUqdNeQ3MCCbZZ0WzhRD3cH3ibT5gJZWQrJU2Pqk7WGTZV7ibBR0tDQeLVpM5yBNribQ/640?wx_fmt=png&from=appmsg)

正当准备放弃时，重新仔细看了一遍接口文档，发现一个被忽略的接口：**string/{key}**。
而这个接口，findsomething 插件并未提取出来，所以在一开始接口 fuzz 的时候，并未注意。

起初不知道这个接口是干什么的，丢给 AI 生成了一批常见 key 值挨个试，还真发现了问题。

```
string/Path → 返回系统环境变量
string/username → 返回系统用户名
string/os → 返回 Windows
```

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNRXLnmHqmNKOjNOwE6mtCDKrxrb6PmEErueicnaBGvZdvy8GWmR9g1B7qTX0FTiaoJT0UHMiciaGQbbbGYRSOayeCKG8QVz1eNtGo/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNycWDKmvKG6XaVF5A8WbFgNs7r34FZvCW0WxiaRH1voEBVqRfSicib4GlhibgyC9Ynicvmtgvl8GVYq3aicxcoltEuqEibRp1l73WmEQ/640?wx_fmt=png&from=appmsg)

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CNLNIS3cGibH60J4CQ05fj7RiclTfDdKpxtySHYPeic6DXj9Ss07COC5ZiceHJZiaWFvsbmbtwF7ClYZ26a0Uv7mpOG9icL3qfmWoOZ0/640?wx_fmt=png&from=appmsg)

第一反应是命令注入或文件读取，但试了 **id、cmd:whoami** 都没反应

卡了一个小时无法深入利用。

回头看接口定义：

```
"/string/{key}": {
  "get": {
    "tags": ["ApiConfig"],
    "parameters": [
      {
        "name": "key",
        "in": "path",
        "required": true,
        "schema": { "type": "string" }
      }
    ],
    "responses": {
      "200": { "description": "Success" }
    }
  }
}
```

推测逻辑是：根据 key 从 API 配置文件中返回对应的字符串值。

关键来了——我手上有源码啊。匹配了三层参数后确认，这个接口就是从配置中按 key 取值。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CODRgv17PfEJcVSf8FQDF3ZsQt9yC7j7pgjoHzILtJe5FzB6m0ldvQqOD62v8Qx1nwwOuGIIfQbXKrjLs4yyhQ5CpibENUJAhFc/640?wx_fmt=png&from=appmsg)

一一对应

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNV7VyMQAakyOwzAcGCYIh2Gaq1vN79A2TVty2jbibEnuWOIaNiabvKSVBurrzuJpAxic0Gb5OPozfgGNqRoLz3ibYsiauXIylhqA40/640?wx_fmt=png&from=appmsg)

既然前面 JWT 默认密钥伪造失败，那就用这个接口把真实密钥读出来。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COmKqHicl5xibAJKS2icnyd34JKvv3aUxO4rx643Z8xkgdibEicfkJcbiblpy4ORAldicu3n5HBf4Br5qqyXsez0QOBGuicpwaU4KWLQ5c/640?wx_fmt=png&from=appmsg)

成功拿到真实密钥。

六、二次伪造：拿下后台权限

用读到的真实密钥重新签发 JWT，调用用户列表接口测试。

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COLDuSqVmqEZYlzO8mJXzUnIYEzAaicZSGIYQryU4Kyet6libCA5m7VauIDprNbyoVKLC6LCLUFqNhibOa38scGhypGicJIJN3O2tU/640?wx_fmt=png&from=appmsg)

接口直接返回了 1000+ 条用户数据，且包含密码字段。

用前面审计到的 AES 密钥解密，发现存在弱口令（如 123456），只是用户名是中文姓名。

![image.png](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COb2fYcDlCu4DUicK2X7RiaRwIAZ8h0H7Q9lLDLnLafrexibe5CsMRX4wsQ2BxhibK7Ww7J8BvvGLusfyWAhJWZ8B1Ogyuc5yocBAI/640?wx_fmt=png&from=appmsg)

再多说一嘴，在前期审计的时候，发现了上传接口，需 token，但由于是配置原因， aspx 不解析

![image.png](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPRVhJu5tnvLnDia0UIKXUicJBKXPptKgPYwSLYUPQaKEU5EY59ABVblFBUdvYXvVocj5uG58g4WPcMPGTkMV698HMcsBMwNkmhA/640?wx_fmt=png&from=appmsg)

最后在登录页面，抓包修改返回包 并添加有效 token，即可登录后台。

七、总结

主要坑点在于 NET 系统 权限做的比较好，但好在接口文档泄露了后台框架，且为开源项目，可自行审计，发现配置关键字，一举拿下后台。

---

内部社区已有770+师傅加入

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9COOXsEf7oiaRxI0zH6PeHYb9BEwdXNz4TCsawW7gycYHe0bXRMf8J1B6bKmZl9LElQrZL20J0q0t8wSicqTwoWjRILUsuiaGPWbaU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1#imgIndex=3)

价格已涨价至**79.9**，后续人数增加还会上涨价格！先到先得！

![图片](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CM32bZTCSvrvydC0Ocnshic72UrzKZjkCRDdZT5OPOTec0twm1SLFDzQCXJpsz3hQXAqud93sIykjhZZUIIl7If2LbL207Yx61E/640?wx_fmt=png&from=appmsg&...