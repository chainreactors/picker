---
title: 【攻防实战】记一次内网穿透
url: https://mp.weixin.qq.com/s/OyQNQi0hKvDtWPFrzyv5mw
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:54.965331
---

# 【攻防实战】记一次内网穿透

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaiaEOGMJwvgYgD3zFPv0qMbeRCNDmricCBIztKf05qJz0yUYpuzUqQKLQ/0?wx_fmt=jpeg)

# 【攻防实战】记一次内网穿透

安全研究实验室

![]()

在小说阅读器中沉浸阅读

以下文章来源于十二主神
，作者十二

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5SmoGvQhdVZt3HnJhCaTsqw8CDhd2U8EH28EHwbYicjLA/0)

**十二主神**
.

十二主神安全团队，成立于2022年05月26日，是一群白帽子组织成立的非营利性的研究机构，以网络信息安全领域为焦点，致力于网络安全、应用安全与WEB安全领域的研究探索。

**前言**

点击下方 "**十二主神****"****公众号关注, 设为****星标**。有用的话请点赞、收藏备查。

# 01-前言

本次实战攻防是针对某个地市的神秘单位，在外围打点时发现了帆软报表存在任意文件覆盖漏洞，写入shell之后，翻阅配置文件，拿到帆软决策系统的配置密码，登录决策系统，决策系统中有个数据库连接配置，获取数据库权限，在数据库中发现nacos的系统信息，通过认证绕过登录nacos后台，获取更多的密码配置信息，在内网漫游获取更多的权限和大量的敏感数据。

# 02-入口打点

入口是一个帆软的任意文件覆盖漏洞

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaoianaBam38AvyvtrtGcS8PmRAOicjPn8FmdGSbzOEwUJqmO3qa3wEGqg/640?wx_fmt=png&from=appmsg)

写入冰蝎webshell，直接上马子

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqa1qynCNZOCzticxrQJUJO2t0X4iaIP5siaJJoSUQzfwYhUIwKfiaVrZibo8A/640?wx_fmt=png&from=appmsg)

翻阅帆软密码配置文件，发现加密的密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqad7S9uahseC7TLCQcNfdqchuP01icP13HUdxpJXYQicDvShWttdRFf2lw/640?wx_fmt=png&from=appmsg)

解密后登录数据决策系统，获取决策系统的数据库连接配置

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaPZv0sWuj9ib8NGjKTmrKRp6IBfpntia53icFwoFAs8eDVYfpstyfxy6Qg/640?wx_fmt=png&from=appmsg)

通过shell植入frp把内网代理出来，开始搞内网权限，通过认证绕过登录nacos平台

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaED1SFeibnkPYcohIjrACic5loQFmDWVCgzIsY2xCX2VJyfwkHicydWicQQ/640?wx_fmt=png&from=appmsg)

# 03-内网成果

  通过nacos平台获取mysql数据库密码，直接给我连

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaG5NKGe61EUUPibaiaAPzGfavW9867XucuhV246kNyHLrDtcmibEosP46g/640?wx_fmt=png&from=appmsg)

继续上分，获取mysql数据库权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaWKGbLfqibtJ9hO2ia0zFoT1szU9jnNom3ibbjIf6cdK8KfYiaiaKuibKs15g/640?wx_fmt=png&from=appmsg)

又一台并且突破到了172网段

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaSm4FWwjPfBLWXzbhcLR82sl033NxJTdYvFq36EopZRWLiaGtHerCJyQ/640?wx_fmt=png&from=appmsg)

并且发现了某个中医院的敏感数据，包含身份证等敏感信息

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqap8stbWqIavb9sjnjE8suZWyfp0ianxxw5Mwaiaiaw85zTlbuJOwAEoPJw/640?wx_fmt=png&from=appmsg)

获取2个minio权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaAaLfP3NEfYtAB2PTGOiabxcVq76yFqxjbh05WKKlcvDovia3MFGeXJdw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaiaXZ7CyaDLib0Ez1Uwychf0hQtGG9jsIbfMyuqNaqwgF3HYib0DJCQs9Q/640?wx_fmt=png&from=appmsg)

获取到Apache  activemq权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqa93JTvWcvYNibYNMfNFZXGMy29VibibHtVjWibm41CibKo0T3jlISu5eJkicw/640?wx_fmt=png&from=appmsg)

Apache  activemq   获取activemq的绝对路径

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqacw3ZlicVfN0HFp5yNCuIk9VXibg71TGBayH7zdgOdW6Cd1D2ianY9dicoA/640?wx_fmt=png&from=appmsg)

使用PUT方法将木马上传到fileserver下

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaMu62F9tAECyCpK7KjLO51eW3lwia7vgMMFOSqwHfHG27uicdqnzthCpA/640?wx_fmt=png&from=appmsg)

然后将木马移动到admin目录下

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaqavQg6ic2MPAxOua7OHNaruAmibCfOfgic8OLTH2aqFEUtBTeKUicwt8kg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqa6E68jCaq8iaicuS4E1P3QicPt1FWlSwzicrw90xT5poTPRexOdrFfkS6xw/640?wx_fmt=png&from=appmsg)

激活guest加入管理员，并且进行登录

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaJbaO2wkpmGBY5qM8icNEuQrpD50DdozKicX30wuic1w0HicRib3dX4ynF0A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaNUOfU5vxN0D1M1S7kGNgGeIpibZsDIejgHmjOJNTXIqGLYOruGqCzLg/640?wx_fmt=png&from=appmsg)

又是2个activemq弱口令

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaAuZqIaurY7reG2bxpPs6LRrDXLS20LicCh1ny4F0IWZOLq41Ea4QO8Q/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqakvzUpKOkpZW2XcFyjWd8c3qzDVbSMgwdpcS0h5jO6RumibZ43dKgJdA/640?wx_fmt=png&from=appmsg)

一个sql注入到手

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqarNT36LJwOcVf0ebrPiaB7xFJvd105G55Vn9XorZLicbCP0xTu9qHJCRQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaiblBEqicNIgWwRaKESmK7T6D3iaB13vEZlKzHyqFylIybKf7sAJpyUuvQ/640?wx_fmt=png&from=appmsg)

获取远程桌面权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaj1c7SR07vw1g3JywrpJf195Zu6W3pPoqgKFm6lC4JxQkia4BldnicoQA/640?wx_fmt=png&from=appmsg)

EBS系统弱口令

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqarEFGxiahWJl0xuvf6XcCsWPZq9ticjHmlCYmchz0oYy8p5wOFVhticsAg/640?wx_fmt=png&from=appmsg)

数据源-数据源列表功能处  泄露大量数据库账号密码

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqa8C3vm01vHAeTpcFN06YEtahIAqbPxcyEzQoibpSJrsDnbqlaGUHeicIA/640?wx_fmt=png&from=appmsg)

oracle 密码泄露 getshell

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaGcQcKsG7xicQrhjnu1jKnVutNP5ia3qySU9Ojut8b5ztOqCzzBM83sMg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaMQu0kwQHm992I6Le09pywialupZCWA1xLNYhgHia1qpqw3KgAg9Pj7icw/640?wx_fmt=png&from=appmsg)

激活guest并且加入到管理员组

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaNXllx8pRbOibXS9k6gl02uAEiaH4p9wtbkiaIeukRO5KL0soDWvVahhKw/640?wx_fmt=png&from=appmsg)

进入远程桌面

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaicKE1x9ltzVt1rFp2rY8m2EYOTBBjfJxFQoRg8jiaLMNUFOc8RT34CdQ/640?wx_fmt=png&from=appmsg)

获取HIS数据库配置

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaDmgVfczB61ibGgtIj18BE7ZKZ1t2Nibmuon6g0S5JlH3ibice3ib83znJpg/640?wx_fmt=png&from=appmsg)

Oracle数据库泄露360w+敏感数据

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqalOpq1t61IglY4D2WARVBJIdbovd05awTAPMm7TKf1zibLOuTbYJzUFw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaDZpdG7rIEFJBl75Uy5YdC8Fb4UlEjpdMGHUMAPBiaVldQfkYUjvxVhw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqapxZ7HL8L84Afhwk325jmMMY3iaRsricvsEj8BLkbpLJT2TAZqRZ3zSqQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqatYh3jkZibKA91AOTa5a7407NK6By41Mb6ibLhIs0XMYD2M95FmURKLibA/640?wx_fmt=png&from=appmsg)

redis反弹shell

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaEEmY5aespibbHGHIQNGkvbOhMma81qIOia1LylalhHmAibqB34apxRFaw/640?wx_fmt=png&from=appmsg)

2个redis未授权访问

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaMrSygM24Vb0e35Ric1aibicI7RUrZumrAKicMtoBghXkEF9vpLB965f8dw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaLxemkgWhE6IkWfun8afribMyspgQpWu14NxKgf7ggNwh7dkDWGIpNQg/640?wx_fmt=png&from=appmsg)

获取金马pacs诊断系统权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaNITA3GS1v6LiaIbiaYumA4OondDec2hmfxcxZ9AXYKeHSnW04T4qyziaw/640?wx_fmt=png&from=appmsg)

2个mssql权限，提权到system

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqawovORLsDB9oCX2vZgGVFmeVsYZhWHMu2PjiarCjAXp22WC1jd39GhlQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaVQG20bAN0Gqbhn8DpIZhOWRVm6ALCYgFpTNWIjj0e2J8rHsktVicoSA/640?wx_fmt=png&from=appmsg)

获取minio权限，minio中保存大量发票信息

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqaa8y3ALb6cSRZM5jck72zAFCXUbSm6ybYHZVXnLOpCNZDCHkiap4x1oQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqavsDCOKEIiag3awrWPT1CHOI4Z8kyaM3lxOm3eGicSKeDH0ppMclPtFgw/640?wx_fmt=png&from=appmsg)

获取反统方系统权限

![](https://mmbiz.qpic.cn/mmbiz_png/BJUTXWkQqmAU0Dr5HV0MJnRB0gqVtCqazWZeAnDicLpRfNMYcs2MZ0k43WDPNPKNDibIKR9uBlBwtoo46hgGSKXg/640?wx_fmt=png&from=appmsg)

打完收工，其实还有很多东西可以挖掘的，但是没有那么多时间，一切以挖掘敏感数据和权限为主。

            ...