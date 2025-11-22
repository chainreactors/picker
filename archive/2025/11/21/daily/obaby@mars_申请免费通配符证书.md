---
title: 申请免费通配符证书
url: https://h4ck.org.cn/2025/11/22027
source: obaby@mars
date: 2025-11-21
fetch_date: 2025-11-22T03:07:01.926979
---

# 申请免费通配符证书

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

黑客程序媛 / 逆向工程师 / 人工智能学徒 / 用爱发电的独立开发者

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

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 申请免费通配符证书

2025年11月21日
[23 条评论](https://h4ck.org.cn/2025/11/22027#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/微信图片_20251121172409_390_42.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20251121172409_390_42.jpg)

之前有个项目，用了个域名带下划线，结果申请证书的时候就悲剧了，嗯，你问为什么不买个通配符的？当然是为了省钱，不想花钱。

[![](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251121-170956-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/11/Jietu20251121-170956.jpg)

刚开始还以为是阿里的问题，后来去腾讯发现也不行，换了几家都不行。最后搜索发现这么个情况：

```
由于受CAB出台的新规（证书中所包含的域名不能有下划线）影响，从2018年12月7日起，所有新签发的证书的域名中不能包含下划线，在2018年12月7日之前如有签发过下划线的域名，则需要在2019年1月14日进行强制吊销。
如有证书用户受到影响，可以通过下述方法进行解决：
1.请用户将含有下划线的域名进行调整，然后CA对该老证书进行重签发，将新的标准FQDN添加到冲签发的证书中。
2.用Wildcard对原老证书进行替换（但如果老证是EV SSL证书，则Wildcard证书不适用于本解决方案，因为Wildcard是OV类型证书，不支持EV）。
域名命名规范 (RFC标准)
互联网的核心技术规范由IETF（互联网工程任务组）通过一系列名为RFC（意见征求稿）的文档来定义。关于域名如何命名的规则，主要在 RFC 1035 中明确规定。

合法字符集：RFC 1035规定，域名中的“标签”（例如 www、example、com 都是独立的标签）只能使用以下字符：

字母 a-z （不区分大小写）

数字 0-9

连字符 -

关键限制：连字符 - 不能出现在标签的开头或结尾。

根据这个标准，下划线 _ 根本不在允许的字符集之内。所以，从技术规范上讲，server_name.com 本身就是一个无效的域名。
```

所以，虽然之前能创建这种二级或者三级域名，但是，在申请对应的证书的时候就悲剧了。

所以为了不影响业务，尝试申请免费的通配符证书，还是通过 acmes.sh 搞吧。

1.安装

```
curl https://get.acme.sh | sh -s email=my@example.com
```

2.配置环境变量：

```
export Ali_Key="LTA**************6yn"
export Ali_Secret="q435*************EBSaDba5"
```

3.申请证书：

```
acme.sh --issue --dns dns_ali -d example.com -d *.example.com --debug
```

需要注意的是，通配符证书只能通过配置信息自动校验，不能通过添加解析的方式校验，所以要配置 key 和 secret。如果是不同的解析服务商，设置不同的环境变量即可。

```
zhongling@MacBookPro .acme.sh % export Ali_Key="LTA**************6yn"
export Ali_Secret="q435*************EBSaDba5"
zhongling@MacBookPro .acme.sh % ./acme.sh --issue -d lang.bi -d '*.lang.bi' -k ec-256 --dns dns_ali --dnssleep 60
[2025年11月21日 星期五 16时53分34秒 CST] Using CA: https://acme.zerossl.com/v2/DV90
[2025年11月21日 星期五 16时53分34秒 CST] Multi domain='DNS:lang.bi,DNS:*.lang.bi'
[2025年11月21日 星期五 16时53分41秒 CST] Getting webroot for domain='lang.bi'
[2025年11月21日 星期五 16时53分41秒 CST] Getting webroot for domain='*.lang.bi'
[2025年11月21日 星期五 16时53分41秒 CST] Adding TXT value: fcTxHx2osERz8mqJFaV2c0yKvo6vUSMA4SH1FR95PMQ for domain: _acme-challenge.lang.bi
[2025年11月21日 星期五 16时53分44秒 CST] The TXT record has been successfully added.
[2025年11月21日 星期五 16时53分44秒 CST] Sleeping for 60 seconds to wait for the the TXT records to take effect
[2025年11月21日 星期五 16时54分46秒 CST] lang.bi is already verified, skipping dns-01.
[2025年11月21日 星期五 16时54分46秒 CST] Verifying: *.lang.bi
[2025年11月21日 星期五 16时54分47秒 CST] Processing. The CA is processing your order, please wait. (1/30)
[2025年11月21日 星期五 16时54分52秒 CST] Success
[2025年11月21日 星期五 16时54分52秒 CST] Removing DNS records.
[2025年11月21日 星期五 16时54分52秒 CST] Removing txt: fcTxHx2osERz8mqJFaV2c0yKvo6vUSMA4SH1FR95PMQ for domain: _acme-challenge.lang.bi
[2025年11月21日 星期五 16时54分54秒 CST] Successfully removed
[2025年11月21日 星期五 16时54分54秒 CST] Verification finished, beginning signing.
[2025年11月21日 星期五 16时54分54秒 CST] Let's finalize the order.
[2025年11月21日 星期五 16时54分54秒 CST] Le_OrderFinalize='https://acme.zerossl.com/v2/DV90/order/7SLmDTCNs_Qw7zls2HFDpA/finalize'
[2025年11月21日 星期五 16时54分56秒 CST] Order status is 'processing', let's sleep and retry.
[2025年11月21日 星期五 16时54分56秒 CST] Sleeping for 15 seconds then retrying
[2025年11月21日 星期五 16时55分12秒 CST] Polling order status: https://acme.zerossl.com/v2/DV90/order/7SLmDTCNs_Qw7zls2HFDpA
[2025年11月21日 星期五 16时55分13秒 CST] Downloading cert.
[2025年11月21日 星期五 16时55分13秒 CST] Le_LinkCert='https://acme.zerossl.com/v2/DV90/cert/bvCTHYFrpbcye-ASpKoS5g'
[2025年11月21日 星期五 16时55分15秒 CST] Cert success.
-----BEGIN CERTIFICATE-----
MIID/zCCA4WgAwIBAgIQS5gLQdZXhrEHdsgVdwPdgzAKBggqhkjOPQQDAzBLMQsw
CQYDVQQGEwJBVDEQMA4GA1UEChMHWmVyb1NTTDEqMCgGA1UEAxMhWmVyb1NTTCBF
Q0MgRG9tYWluIFNlY3VyZSBTaXRlIENBMB4XDTI1MTEyMTAwMDAwMFoXDTI2MDIx
OTIzNTk1OVowFzEVMBMGA1UEAxMMaGFpa2VodWkubmV0MFkwEwYHKoZIzj0CAQYI
KoZIzj0DAQcDQgAEehCGvspbOuBBQjuauz9ghdv9bmvPGJmlz/LttbMjBlBi31Wh
****************************************************************
qaiMNTAnBgNVHREEIDAeggxoYWlrZWh1aS5uZXSCDiouaGFpa2VodWkubmV0MAoG
CCqGSM49BAMDA2gAMGUCMHlmfYvfKEWtJ/CM7UNx6sJPwzu5fU1c5j8v2Oj4REQh
/KE0yJHo3YZkXegvxlSAPAIxAOPw+ZwRsatCaRL8yEGp4mX0umkKx+XbtTlus5NK
aBIOcZiS307CH5mXKOb1jXMPpg==
-----END CERTIFICATE-----
[2025年11月21日 星期五 16时55分15秒 CST] Your cert is in: /Users/zhongling/.acme.sh/lang.bi_ecc/lang.bi.cer
[2025年11月21日 星期五 16时55分15秒 CST] Your cert key is in: /Users/zhongling/.acme.sh/lang.bi_ecc/lang.bi.key
[2025年11月21日 星期五 16时55分15秒 CST] The intermediate CA cert is in: /Users/zhongling/.acme.sh/lang.bi_ecc/ca.cer
[2025年11月21日 星期五 16时55分15秒 CST] And the full-chain cert is in: /Users/zhongling/.acme.sh/lang.bi_ecc/fullchain.cer
zhongling@MacBookPro .acme.sh % start
/Users/zhongling/.acme.sh/
zsh: command not found: start
zsh: permission denied: /Users/zhongling/.acme.sh/
zhongling@MacBookPro .acme.sh % start /Users/zhongling/.acme.sh/
zsh: command not found: start
zhongling@MacBookPro .acme.sh % open /Users/zhongling/.acme.sh/
zhongling@MacBookPro .acme.sh % open /Users/zhongling/.acme.sh/
```

最终，省去了更换域名的麻烦。先将就用着吧。

---

[![闺蜜圈 APP](/wp-content/uploads/2025/11/guimiquan-ads2.jpg)](https://sj.qq.com/appdetail/ma.dayi.app?&from_wxz=1)

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《申请免费通配符证书》](https://h4ck.org.cn/2025/11/22027)
\* 本文链接：<https://h4ck.org.cn/2025/11/22027>
\* 短链接：<https://oba.by/?p=22027>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Next Post](https://h4ck.org.cn/2025/11/22016)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年7月16日

#### [WordPress 评论显示IP归属地插件–WP-UserAgent[增强版 12.01.01]](https://h4ck.org.cn/2023/07/12517)

2022年11月2日

#### [Jetpack 防火墙 引发的血案](https://h4ck.org.cn/2022/11/10651)

2013年4月18日

#### [CentOS Apache 2 FastCGI](https://h4ck.org.cn/2013/04/5114)

### 23 comments

1. ![](https://gg.lang.bi/avatar/ba8eb2c499ba91f5563756f0ef01b68fac4fa2cb941c05a6a8a139d66df4323a?s=64&d=identicon&r=r) **[倦意](https://jyblog.cn)**说道：

   [2025年11月21日 18:11](https://h4ck.org.cn/2025/11/22027#comment-130059)

   ![](https://badgen.net/badge/用户/已认证/CCFF33?icon=rss) ![](https://badgen.h4ck.org.cn/badge/友链/集美们/blue?icon=chrome) ![Level 4](https://badgen.h4ck.org.cn/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Microsoft Edge 142](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/edge-2.png "Microsoft Edge 142") Microsoft Edge 142 ![Windows 11](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/win-6.png "Windows 11") Windows 11 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   acme.sh 还是可以的 我现在是方案是用cdn自带的证书程序，然后nginx这边就搞个自签证书 这样我就可以不用管自动续签了

   [回复](#comment-130059)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2025年11月21日 19:49](https://h4ck.org.cn/2025/11/22027#comment-130066)

      ![公主](https://badgen.h4ck.o...