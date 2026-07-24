---
title: 好靶场杯第一届综合赛道（流量分析-古法赛道）详细版Wireup
url: https://mp.weixin.qq.com/s/D4YSX_1-ZpcbT5WmYfcXkg
source: Doonsec's feed
date: 2026-07-23
fetch_date: 2026-07-24T05:02:21.710533
---

# 好靶场杯第一届综合赛道（流量分析-古法赛道）详细版Wireup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qK3m3mOz5ic8CXiakueDwpSAgE4UmR4KXs3HO0KibiakE21F9lp3PeH3Lsll5kQlic07HWBaEdCKKezPFw1IVaVjQvKscaoShOrBh4n7G1h0ZHbw/0?wx_fmt=jpeg)

# 好靶场杯第一届综合赛道（流量分析-古法赛道）详细版Wireup

泷羽Sec-静安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

编者荐语：

虽然报名了，但是我太懒了，连签到题都没做

以下文章来源于鱼影安全
，作者落寞的鱼

![](https://wx.qlogo.cn/mmhead/Q3auHgzwzM5oDN9nnkG1ziaib2XoYrq2oQKCtJRc5cIqdzZ12Qne3ssA/0)

**鱼影安全**
.

阿里云博客专家 CSDN博客专家 网络安全领域优质创作者 中高职全国职业技能大赛国赛金牌培训讲师 青年工匠 多次培训出省赛第一名、国赛二等奖，市赛无数等战绩。第七届全国残疾人职业技能大赛 网络安全 赛项 浙江集训教练等。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/iabIwdjuHp2WoekX6fnZ3APEKJwyvmf76EZ0Z309yU3fUicsMz4d7aZ7G41VxQPvKcqmzdqnYwcgWW0V6c8LZBiaQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

点击上方蓝字·关注我们

#

#

**前言：**

***今天这篇是好靶场杯-流量分析部分，钓鱼邮件该师傅1血！***

***本次文章由：yuiiijuk师傅提供文档，修改了一上午！***

---

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic96thek4qia0RGAXwosHV2BXiaiaiaRlRFQ6KtICZPAgDbzBGkGvD0oTocLx6XZSia2VTXcSSjJPrOhDiar9iayXicHrhSG05iaMPAicA4Vk/640?wx_fmt=png&from=appmsg)

完成度：流量分析完成7/8

最后那个钓鱼流量，因为有56问，题量大，难度比较高涉及多个过滤手法和分析思路，在比赛结束后，才后续完成。不进行公开分享全方位细节分析

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icicsoNibRYjlLicBljKnSausbs6icWTEzr70EUTJ1bxvpTuic2pmNavBFdDRm9BtY1DkE4z5gib2hYQewtOrj6IpsNfxbcOTRicBGEoe4/640?wx_fmt=png&from=appmsg)

比赛结束的11分钟后完成该题。

接下来我将细节的讲解剩下7道流量题做题思路和做题流程

问题有些比赛的时候不够详细，我是在结束后的靶场进行细节补充。

---

所需工具：

Wireshark/lovelyspark/CTF-NetA（付费）/CyberChef

任意一款解冰蝎，哥斯拉流量的工具（免费）

PS:在我写完wp的时候，lovelyspark完成了更新，usb以及各种bug修复好了，可以完成该古法赛道所有流量题解密。

本次wp的过滤命令，默认已经搜索学习，不展开详细讲解，可以从wireshark官方wiki或者CSDN、本公众号以往文章等一系列平台进行学习。

技术有限，有些题会标注是否可以用不付费软件去做，USB那种网上有python脚本也可以实现非付费去做，付费软件也是一个个脚本去完成功能实现，只不过更加方便快速。

---

Webshell3：

(此题wp有非付费软件的做法)

1.提交攻击者IP地址

点统计-> IPv4->ALL addresses（找流量最大、主动连接最多的一方）

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icicb39E11VicEiaiaEPMJVf8EAVkM7zEz32icvGGs3lvrjTCeWrYN3netHjZpUicBns6y81icotzIC8WusA9cBAb4SpAGSibHJFibCXgm5I/640?wx_fmt=png&from=appmsg)

看到192.168.99.28 <-> 192.168.99.59 流量最大

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icibofpPTas9oslrndUdCtgkkOTWW4djJMnwjOoYrff0xfyUc3mjvHIvM3X6BGKkSicgdicxrPfibcjdREgLTZbuDn8vtxBolIArpSM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icicX4lEa8hxWJhowCnibJsTd7HNqqrJJR9iaXJTJvGJtMlXS0OjwQ0WCOAWRyrL2A7BHxALqJjiajKyibPECjXN2u3uCKRwoW0juuU8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9MG89ATr9WE6cibEZ0bIg0YYapC3eEibsoVdaxs2NOcAkHm0P1TaBWgziaFafcDViccdTG1Hiae8awh03UpRb3KLvt77Rc0PQt5uibY/640?wx_fmt=png&from=appmsg)

2.提交受害服务器 IP 地址

参考上一题

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9l8nH9PWS0thne1whKEAPMubBEtsesuIn29M6DaP9Upjw6iccOGS0Dmciajb5iaeG87Ux6208ZxuOuIBW3iaGRpOhOryqpwicZ6ypE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icibR9z1G3wynPzxrjzWOibrUdMnoPE5XBZW3NSYQwyRh11MOvWNdB0jMh5rCjU1k2ibkvh8t1RCvqgEVcQGfqibo1wDpX5KybsKmlI/640?wx_fmt=png&from=appmsg)

3.攻击者使用什么工具进行了内网资产探测？

使用命令：icmp || arp || tcp.flags.syn == 1 进行过滤

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icibRJgsibGotUkUCnRy9Q1YEGIgUjQAiaf82zFdTtiaibjlWTc23xJRa2zzDelAibm0yyCJwKNicmibic2Ff4HAzn5pIsyYAPzgEkJW1rUg/640?wx_fmt=png&from=appmsg)

看到.28对整个192.168.99.0/24 做ARP/ICMP 探活。

随后批量探测80,135,139,445,3306,5985,3389等端口。

这种“先探活、再扫端口、再识别服务”的行为特征是 fscan。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic9vKdyT4ZM1YKib9LTSmibcicR498qFxdnYwriaWvHBQE2C5YplOpibBIMckxvLyuDoyCpQgE0wSJRTvOAUS2X6b4qy1pMBUibehzSWA/640?wx_fmt=png&from=appmsg)

4.攻击者内网扫描了哪些存活主机 IP？（从小到大，逗号分隔）

过滤 ICMP 回包

icmp.type == 0 && ip.dst == 192.168.99.28

可见回包主机：.58,.59,.60,.61,.62,.128

.254 也有 ARP 应答，是网关/DHCP 相关存活主机

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9Wj5tnmUEmHDRplN1fda6B1UfWicanRP5Z1kYa4p0sovDDBVlrTxmYqxptrG34TII4w4WUkyU0qonFt1T2Y2oc2P6SsaOFSRlo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic893LQCkE2IiaoNezibII1tu74ghBROpbwW0Q38UVziaXDPiaRiboqEt8a2U98dCaSiauJWJFxoNWTglVpTDRuRaeWqObdbT1bHeTicJM/640?wx_fmt=png&from=appmsg)

5.受害服务器开放了哪些端口？（从小到大，逗号分隔）

使用过滤规则：

```
ip.src == 192.168.99.59 && ip.dst == 192.168.99.28 && tcp.flags.syn == 1 && tcp.flags.ack == 1
```

过滤受害机返回 SYN-ACK，

看到 .59 对扫描返回开放端口：80,135,139,445,3306,5985

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icibefMP38mjPCymWszyOkaQeZWu7qvgaXSE10zia9uia2hNgfz5ocLPyp0SzO0AicrQibiaW9MbiafMSaPa3nM0fZ6iahjZItts3ibpd3Zw/640?wx_fmt=png&from=appmsg)

后续再过滤 RDP

tcp.port == 3389 && ip.addr == 192.168.99.59

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5iciben9scokxYqtbHlt8ZGQErpHcwW6JYuq5FqHKO9hSR90vkicibfB7OTuUE0sic8lGfYvyjuExOj5VhFXKtxm5jAeInLg76Btwkqk/640?wx_fmt=png&from=appmsg)

看到攻击者成功连3389

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icic1icLEb2EG7ZskKYx5u1fAicicwkMLBqhBmiclUQphTAqBLeVz0PHibD1AGvCuL9uYBUAQ2Z1pE8cia8ZylR1EX5OvX8ic3TKicX0GItc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icibGCMHJjxBpEskE3iaqCGzWAbhbDibudQvwJJl4TSVCLCMg9YnI3NUNcb6Uwz2oiaheGQlZKeCE5CTZicv0M1jlJ1TmmXya1kPra5I/640?wx_fmt=png&from=appmsg)

6.受害服务器 Web 中间件及版本是什么？

http.response 过滤HTTP响应，追踪流

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5iciceXLLuL2RruLlxic4wlIna81CjqSCibgryxklykD3bPHnXe5bBw92C5594sOiaeh7ropXMXSBdDiaW3J5ZAGp1VYuRwg96nj3M0hQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic8dfaktHXsD20unTxVOkbZR2GGCFD5HDT1vVb9xkejBJwXaD0MbeeS4T59B2sXT8cNOMH0N8XTTbYGbmPcfCf0ISGrgcmkHNy4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic8qe4bKaZliaVialbOATvPh9KrXFCfG8QdLP3UcemYuBSZ4PLia7hA2cNOv1P2ySujN6orbaGXwUZIyn1b9ib5viafJg9UdS5kHb7GQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icicCz2NIkISrOJIS1UVxNZLzvBFI7mubvTC8xsqyKAkyBw6yX1I8Lf9ybyhGjTXwRY3VbtqaOQXibw09NicpicN3XxsicrA0G3mmepQ/640?wx_fmt=png&from=appmsg)

7.受害服务器使用的 WordPress 主题名称和版本号是什么？

http.request.uri contains "themes" 过滤主题资源

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9jjlzvSpmClXC3IJrfvWtca9B675RAUKfu1GqJB9fTiahDtu14MjDcjOAjhZ4PREMo7kDrHk8nW8QCmBnQYflhMQXw79oyLPRM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic8CtdfSB5eKQQNlVa3zmmuicQW7U5gmmB6P1RWXGAcwWgACqbtBXnZgt50qRlfq32VwCTlBQ7beBAtiaAHDKEj5TgtDtSXpibmZqs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icicMRDXAIbMR6z8rQAmDhz0Tl0MWDV5nHUibUnUStMFuyfKqFiaAxuRKOSC7OibdTwqpo2tOC4ux0Hme5mIZMVMywAIO1gAc2oa7zo/640?wx_fmt=png&from=appmsg)

8.攻击者利用了哪个 CVE 漏洞？

从第上一题知道主题是 WebStack 1.2024

搜索该主题版本和接口，可对应WebStack任意文件上传漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icicuT42fPvlr4yo1fDUKecheXhF5mpuEiaVKibVuF80Z8pm1cCblyY3x2kQfWwicznic3pJrY7XCxea5T17ibEkoR0wlH5D1PlG3djdg/640?wx_fmt=png&from=appmsg)

9.攻击者漏洞利用的完整请求路径（含参数）是什么？

http.request.method == "POST"过滤找上传 Webshell 前后的 POST

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5icibHcZHoJ6WBZWmN39ABAwmBnjmTg66jNwot5n1zLBnyuhVd8KN2oWCrNFYJlJppW9fDUsia6ezVTFD0F0xWL60AGNIYicE5HJjBQ/640?wx_fmt=png&from=appmsg)

看到攻击者请求/wp-admin/admin-ajax.php?action=img\_upload

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icic34YLgLrh8w2fTcniaI8GbDz9ChFSJ6vTcAv8iaXUklCC5tUAHnaBzuKRGWge6O0iaBMribuGf4NhafnWj1S0GTZu4QFCAOj6zGBg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic9gWPNHCxcBe8QjTDCkZKRr96qGb1olOYc8YibU5oYmgO3qzCicDUlrpHnrHegACTeY1SAn6qC2qHmMwD34kBcj3zXc7rPicxOaoY/640?wx_fmt=png&from=appmsg)

10.攻击者上传 Webshell 时使用的客户端工具是什么？

追踪该流即可找到

![](https://mmbiz.qpic.cn/mmbiz_png/qK3m3mOz5ic9PwjNoC6VuAnDHwxxFwng4RFkp51nz2vl4SFqvvFFQ4U15icjJEUnmWX5JklBTjv5rkNKTRibzGwvrENA72KohFia1HgE8BBTiawo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic8IbIDPib2GK5nWbphzBCRgdgMsdedSNOermhcwgMV41K5ticgnabvA8WpWkibeusgdibR1LicFd5Jp1jbibAIrxXd7RMfDpRjV9CCas/640?wx_fmt=png&from=appmsg)

11.攻击者上传的 Webshell 在服务器上的完整 URL 是什么？

参照上上题过滤，即可找到

http.request.method == "POST"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5ic9u3qsoyvskPOeqzvv2ibuRcAu22Nsbcm2MXibfZXPTBeZArZ2HVlYdNgwqZjjLXiaApfHnsQNzbHq5NsgjevuyicRkuRaFZkSqWcw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qK3m3mOz5icic8k9...