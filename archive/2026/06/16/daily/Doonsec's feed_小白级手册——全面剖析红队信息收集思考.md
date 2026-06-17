---
title: 小白级手册——全面剖析红队信息收集思考
url: https://mp.weixin.qq.com/s/nOwirydlGkHpUcbwGlJOgw
source: Doonsec's feed
date: 2026-06-16
fetch_date: 2026-06-17T07:01:09.727720
---

# 小白级手册——全面剖析红队信息收集思考

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/T0ibbhsCmribTprAAR2Ty1picmowDqgSkmlomK45f60JNy75DPe0PUtVKAI1iaMHDoD8ibcMVKsJztrqAX9QRN2PvIkTldGus9MeCvOZRYpTJ0go/0?wx_fmt=jpeg)

# 小白级手册——全面剖析红队信息收集思考

网络安全民工

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

红队信息收集思考

一、 简介

      红队实战中分散工具与碎片化收集思路效率低下，本文整理一套标准化资产挖掘完整链路，两万字覆盖企业股权备案、子域名测绘、IP 网段、CT 日志、JS 提取、Host 碰撞、Google Hacking、云存储桶枚举、深网泄露全流程。配套 Tscan、Subfinder、BucketHunter 等工具实操命令，聚焦影子资产、边缘隐蔽资产挖掘，剔除冗余淘汰手段，给出可直接落地的侦察流程，适配渗透测试、攻防演练、企业攻击面梳理学习。

| 本文仅用于技术学习与合规交流，严禁非法滥用。因违规使用产生的一切后果，由使用者自行承担，与作者无关。 |
| --- |

二、 正文详情

（一）主域名&企业信息收集

1.1 企业信息查询

如果客户要求去收集子公司或母公司，需要跟客户约定好持股比例，去平台上通过股权穿透图先把子公司名称、域名收集一下。这个目前没有很好用的工具，通过人工更靠谱一下，如果组织比较多使用Tscan、ENscan，是目前比较推荐的，接口可用企查查、天眼查、爱企查等（商用）。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribTTCE41vMoPDGH6qjJU6WthMM9ZOibYnmTINLuoED8WIicfLHN0ThJGZsEhLib0ic5ibeMdpvDwDw9sAD6nthGXoq3H8JNFicHfDzr6Y/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1.2 Tscan

配置站点的cookie和key，输入公司名即可进行基本信息收集，这个还是比较方便的# https://github.com/TideSec/TscanPlus/releases。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribQ2Hn9JJhoGlBOEJP8gzjTvNhMz3FrxUFq7vrRVh0OxwSRxtv9HCo4xsakDWurqSeAJSQ1htqwSERa0eQu5wUibgnyjf1IlH1J0/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribSxBhDiah3JKI4gLMbEu03rORftg3ENicUdiaD6CjC6y9G0aRk6h26zr48flVafhtbe9XWo4VpibzHahdZNZS42ebrQmzsQLJEJFZk/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1.3 EnScan\_GO

下载后需要配置API、cookie后使用，这里给一下我常用的命令，如果报错可以微调命令，每个人的环境和配置文件都不一样不用完全照搬，这里我们目标是一些基础信息不用太过关注。

* ./enscan-v2.0.5-darwin-arm64 -n 北京XX网络技术有限公司 -field icp,weibo,wechat,app,job,wx\_app,copyright,supplier -type tyc,chinaz -timeout 30 --hold --supplier --branch# 下载链接：https://github.com/wgpsec/ENScan\_GO

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribQKe5mFlVLsxGYFvJIImib8m4DPvic2bianRRia6xTg5iaODS6HcrLsBM7yfF0j7S8icIBIF4kUpV1Vg2uISQh0Rhx5kamicVMalxskQo/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribQL8P3Z0wtPKO9U81aUNFm29ia33PrficmloNI6lRlgRw9HyGI31TMgT5MzycuOPPzesSTsFqiaTupZ2WThTicosKj0j1LQuYYA66M/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1.2.ICP备案查主域名

企业信息查询”已经查询到了公司名和一部分备案号信息，这时候我们就访问时效性最高的工信部ICP，直接查询`公司名`可获取当前公司备案的主域名，需要点击`详情`。`时效性高是因为ICP备案会定期变更一部分，工信部作为数据来源是第一手信息。#官方地址：https://beian.miit.gov.cn/#

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribThzXesdhzd34pgHr0IOkP7M9oPpTvPzoOickleaNPVcQKVgJI9MCqDMYxkWUERhVyXial9doYvYl6jWgnvPD1iajeBdU6EsdNxWE/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1.3.WHOIS 历史与反查

| 通过域名的历史注册信息（注册人邮箱、电话、姓名），反查该人名下的所有其他域名，找到企业被淘汰的"影子域名"，`这种域名运气好还能测绘到资产，再不济在后面的host碰撞会用到。 |
| --- |

1. 查询历史whois

* 企业的whois信息会因为各种原因进行变更，有时候会变更关键的（注册人邮箱、电话、姓名），通常搜索这些信息可以获取到企业注册过但是没备案的域名。这里推荐用微步，因为它隐藏了不重要的变更。#https://ipwhois.cnnic.net/ #https://webwhois.cnnic.cn/WelcomeServlet

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTzuXibMiaG6qCUGJDmKloHJBUic2J6WLoYQylSEvwiaI5hy6vmLjMtFdMyFGyakibBImAfNjibGIUDplicfr8pcD58rPw3gjraWd47iaI/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

2. 反查关联域名

* 上一步获取到了whois中的（注册人邮箱、电话、姓名）信息后，我们可以通过这些信息反查注册过的域名，这些域名有的还没过期但是不在企业备案中，可能企业自己也忘记了。#https://x.threatbook.com/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTQ5ibGSAPLfI9co8XaFagtG5h85aibSNrzFnMoLf90WUYZejwXbJoSmJsh0qhJjWoyLib1ibUhtFg7IYVaV8B9btMAbibXEScGSIWk/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

（二）子域名&ip收集

主域名&企业信息收集”完成后，我们已经拿到了企业基本信息，接下来我们就基于这些信息，使用各种渠道扩展这些信息。

2.1.测绘平台被动收集

注：被动收集要工具和测绘平台结合使用，1是不能完全相信工具输出，2是接口调用接口可能因为程序原因缺失结果，而大部分资产都在这一步产出所以要尽可能覆盖全。

2.1.1.工具调用接口

1.Tscan☆多平台付费

这里把Tscan放到第一位的原因是它能够快速收集我们想要的信息，当然我们要更详细收集时还是要用到下面的资产测绘平台语法，不是要打攻防的不要太详细非常耗时。

1. 配置好各个平台的API

这里尽量配置全一些，虽然资产多不了多少，但是多出来的可能就是关键的入口点`,这里要通过ICP备案、主域名、证书绑定域名，查询资产信息

1. 收集域名、IP信息（ICP备案）

输入我们在“一、主域名&企业信息收集”获取到的主ICP备案号，字段选择“备案”，`一定要是主备案号，子备案号会漏下，记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选，可以看到通过ICP备案号收集到了很多信息

| Plain Text下载链接：https://github.com/TideSec/TscanPlus/releases |
| --- |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribQRz2mO2oicc6sPgho2lFwQxUWR3XXA5sTu7uQt5mdKVgeQ1X3fYarfiarziavkfzuuicllOhlcXHRDLM24fenSHdXFmrfDPeK9YK8/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribTNeQs4xoq51mRrZeaMmobbE260Jm5SRCKgonxd5AZicOl7wrv4ADFfXOnPWeC1edEYNSCIibNZl3b8eIUQZzpxrfF8bPFna3LMw/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1. 收集子域名、IP（主域名）

输入我们在“一、主域名&企业信息收集”获取到的主域名，字段选“域名”，`记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribTAmNNWtXP0jZqqdT7sXl8FkO8ySah6CerGwcAVhg2rjWI6B3CaWvuPeesQhiaYoIhCNjUKmYSibqZ90faT4DD8wyxTgKD9icwons/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1. 收集子域名、IP（证书）

输入我们在“一、主域名&企业信息收集”获取到的主域名，字段选择“证书”，记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选。

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribTiaZ1F7wJsLTwRosIDsTUSXRU34KMdBhxLktG3MQFkpOqstU2jMichiatLCeErPnVy2iaic53QFE2a6YvIWp9s7jWAp9o3pFQBHtkA/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

注：部分站点会使用通配符证书，另外平台在证书字段上的匹配也可能带有模糊性。所以我们查询app.com.cn会匹配上abcdefapp.com.cn这种资产，这种不是目标资产，所以查询完要人工筛选一下。

2.subfinder☆多平台付费

* 0. subfinder配置文件位置运行以下命令可以看到./subfinder -version1. 配置（bevigil、censys、chaos、digitalyama、dnsdumpster、fofa、github、hunter、intelx、leakix、netlas、quake、rsecloud、shodan、zoomeyeapi）的APIkey，使用全量收集工具进行收集2. 这里列一下我使用的命令./subfinder -dL domains.txt -rl 20 -all -json -o results.json# 下载链接：https://github.com/projectdiscovery/subfinder/releases

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribSoeB1ZkXjxrkOIh8oUiboNKcjIVMxWicjjBTOjXNibqqpvclSEibhwcEK4EZwZibM9Mo1ImDzhHUyKk1pxHS0MiayIBF9bU5jSKRVy4/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribSAzM9aibt5J2It4O6bU9Jt133AXBFBmDzwzcmsyhZn2qhQruS8e3gTtITZSE6WM3f8YgYNKL3lA1SSe6s5OsVArfsd4cwpso7I/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribRgriaPuVSyGY4emo7EX72dIXMog6JS94bic234ibJmrCHgVIY3Pfe8hMf0xK0rAhRA3CMfTjlsA4YBgyVbu61oDMH1lAoMJqxVGU/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

2.1.2.资产测绘平台

1.域名查找

# Hunter domain.suffix="app.com.cn"# Quake domain:"app.com.cn"# fofahost="talentsec.cn"domain="talentsec.cn"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribQNPw4pyvxoia1LL66TicaeQuic5CuMma71rMsHLYbOSicelpnoicpsGDhWmjmaW3WchWXSOVxEHI8EOInPvygEtvtVFnD5GJpz030I/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

2.ICP备案

# Hunter icp.number="备案号"# Quake icp:"备案号"# fofaicp="沪ICP备20019790号"

3.icon\_hash

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribRZQEaoSwbOEFfyDAeNQ2bc4Tj9TMlHKKLcmFfN2ibfSEv2dSbpnrJllywCcTnflRmgnFBJaicX0wmxkLbFfYjNvCZoca6ic9cHbw/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

首先根据在测绘平台收集的结果，把icon的下载路径或测绘平台的icon\_hash保存下来，后期收集边缘资产用就行# Hunter（使用favicon的MD5值）web.icon="MD5"# Quake（使用favicon的MD5值）favicon:"MD5"# fofa（使用mmh3算法）icon\_hash="585442251"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T0ibbhsCmribSfhFJQib7ejlec9p8KGftUNh2nzZt8svtW6GvpCofczYOREOr5oMVpsvDf6qNfNly2zhJnexic1PNV35nnLhMD9eKib35lVX7xYg/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

1. title&body查询

title# Hunter web.title="标题"# Quake title:"标题"# fofatitle="螣龙安科"||title="螣龙安科，专注于新一代攻击面管理"

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribSIr5CeMRiczsKZZvOa2favGpSmZtZh8Zq2RxzkTOdsSvEUXiaz62KvSvsJibjEtHwWyL4EbE27wD2sU6bRPVvn3pr2pNTcmen2r8/640?wx_fmt=png&from=appmsg)

添加图片注释，不超过 140 字（可选）

 body注意body查询不能用title的关键字，这样会出现重复结果的问题# Hunter web.body="内容"# Quake body:"内容"# fofabody="螣龙安科是国内新一代主动安全领域的专精特新企业，致力于为客户提供专业的标准化产品与解决方案。"||body="螣龙安科，螣龙天眼，螣龙天眼ASM，螣龙攻击面管理系统"

2.2.爆破子域名

原理：搜索引擎爬虫的抓取、证书透明度日志的同步、威胁情报库的更新，都是有时间差的。如果目标企业刚刚配好了一个新的子域名，此时所有的被动接口大概率都查不到它，但通过字典爆破，可以实时地将其解析出来。

1.Findomain

1. Findomain的config需要自行下载加载，就是使用编译好的默认配置

https://github.com/Findomain/Findomain/tree/master/config\_examples

1. 将我们在“一、主域名&企业信息收集”获取到的主域名存入domains.txt，配置Apikey，Findomain的配置文件可以运行，字典可以用Tscan的字典
2. 命令：./findomain --file domains.txt --wordlist subnames-9.5w.txt --config config.example.yml --resolved --output# 下载链接：https://github.com/Findomain/Findomain

![](https://mmbiz.qpic.cn/mmbiz_png/T0ibbhsCmribTBpu8v0SUTrwfK58x4eNFYYlfJbU9YPaXru5lpYn0Ngp8icY5TezMzQf...