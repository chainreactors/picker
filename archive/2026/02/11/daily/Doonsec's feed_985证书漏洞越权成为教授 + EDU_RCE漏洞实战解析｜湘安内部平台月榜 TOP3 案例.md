---
title: 985证书漏洞越权成为教授 + EDU/RCE漏洞实战解析｜湘安内部平台月榜 TOP3 案例
url: https://mp.weixin.qq.com/s/9AAoIbOoMxVTjx9Vvu760w
source: Doonsec's feed
date: 2026-02-11
fetch_date: 2026-02-12T04:18:32.957181
---

# 985证书漏洞越权成为教授 + EDU/RCE漏洞实战解析｜湘安内部平台月榜 TOP3 案例

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tlibgKYKL9EtbqnxemmsbvrVS06b2sQVVE3Su6PmRwsXJ3yicqoDibngIiaiaVZKFRMTHW2AgiaY34NhGEvoT97YTBicEjqpOlkom7nb1ibOMXWNo2M/0?wx_fmt=jpeg)

# 985证书漏洞越权成为教授 + EDU/RCE漏洞实战解析｜湘安内部平台月榜 TOP3 案例

原创

湘南第一深情
湘南第一深情

湘安无事

![]()

在小说阅读器中沉浸阅读

**声明：****由于传播、利用本公众号湘安无事所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。如有侵权烦请告知，我们会立即删除并致歉。谢谢！**

## **前言**

上个月湘安无事团队内部漏洞平台给一月前三的学员和成员发了kfc奖励。

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtSQk0O3NPDY2lzlfPaqiaUgrVAODs2jicVry1gBib4frICdpk4ibq3ZDtNXH2unXknVMVBJopia6gJmSlqSGZMrSgMXcCmfcUXsIZo/640?wx_fmt=png&from=appmsg)

这里挑选了一些优秀的报告进行分享，来自0X77学员的rce报告

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtPMVaN2zR2CgPFTgvk3yHvXxD7ickF68OFtgVCWGJPkdUibn4EmM7yRIic1MibbKvyKIBbrRsptrDVYhI5bOkshvg9ECpnzpOojpU/640?wx_fmt=png&from=appmsg)

还有来自根本睡不醒成员的证书站逻辑漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuCHCN5p2tKxWXS1tpvibibBoCICE9ecajRNOVKDXCvlW0BKNricTYy8CYEgNgyib1iaaSTNmBPFg0qcVGHBpnboS7CY2cCHq7UpzibE/640?wx_fmt=png&from=appmsg)

## **edu漏洞rce报告**

选择之后存在登录，随便输入尝试

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Euavib8pAerBnD4Nlg662lkUZm8opd4moQjcITZmK5MQ0m6Kqy9YkqC58HUrVFou19V3IUOPsca1tFhsUfY2fDkauqqupPjwIn8/640?wx_fmt=png&from=appmsg)

发现存在shiro明显的特征

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EtruOrn4lyd74YVu91OnxyynwWJUlvNhA1Rlic30KplnIhETQAak6aemsfVA9FUb6ywjyg2PswfuPPg8j90Q7iaNcribcicOqbJCUA/640?wx_fmt=png&from=appmsg)

猜测是Spring Boot + Shiro + Tomcat的框架开发的网站，可能存在spring未授权

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Etruy1I3VbF6iakqmicmOAKGzSN6flbibLzZ9Du6B1Q3cXQTZ0szfqDhKO2dphXOBHiaVOj4l5GX1u9icpb1x6l2DLuN33Lp1icL99ics/640?wx_fmt=png&from=appmsg)

直接扫描，发现存在/env泄露，应该是深情哥上课说的spring1.x版本的未授权

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvYGqw1DCa9RkgnHz6b5y3I5Xhcw0ca9YLib5WZ5QtVT7VPwsnH9KIgWmrBDy9iaCIhIzD9UILPictXB5DWpWibD5gbju7SNJrcP9A/640?wx_fmt=png&from=appmsg)

有env泄露，那不就直接访问/heapdump下载,不就行了,解密后得到shirokey。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuzU5v8ZxMLZ4Ir0I5Vgny7MumamoBUAyvfZpFiasQ6EYwIKD9BYaPIDwNVlqahVqWqScKJxamDZLicF6mByLciaGYXYa8aWb1qh4/640?wx_fmt=png&from=appmsg)

然后直接梭哈不就行了，这有什么难的

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9EvHlxAPDy27UD3PmE8gOOR6QvbiamLTp9Qqg80w5ae8Nk7hcq4mcTFOMq4DxoE9RnfRvMhVqHO51ZGE7fPS3jv9rWSVSmdDrekI/640?wx_fmt=png&from=appmsg)

直接拿下，简简单单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Evcd9Pp2IX5yibDa5Jp3aVFJEKp7TsCxVc2MaGCCnYvfw7bicogoIs1neBjnP0P4JzjevUJZ4dN2btZHk7uQU4EPZLwX1zENzghU/640?wx_fmt=png&from=appmsg)

后续让深情组教发送了kfc，再接再厉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvibJvia9gSc4oTppAj6piaKRe33mJANibicG1aHQ5Dtic0llianHNKzl2tWKSsgDE7wXQUvTyOibqibYFAKWu4LgRVJT9Y8IwsGkKmy7Zw/640?wx_fmt=png&from=appmsg)

## **985证书漏洞之越权成为教授**

首先来到一个院校系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EtzVoyghruh7otgnYicKickojA0VPTPJDsugMVibHOKxIyqeq8mSuKIiaKianSNDDDUXLWibmuWbWSHFs6gCJsH7ROoKI1XXhtCX1oibQ/640?wx_fmt=png&from=appmsg)

院系系统在进入系统菜单会先请求报文/user/profile

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9Ev11cibVfjop61KcSz013PbU0HgiafhgP8hNBKGtVbFicmQtlHqu0m8Ee6vI7FNrIhWGzzkQfEfbprUQDJc1YHGIcnl1DqjESibIIU/640?wx_fmt=png&from=appmsg)

第一拦截返回报文

并且报文中的routeUrl改为https://xaws.edu.cn/#/user

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuZ6J0mJO9VJkicbcDbJoxvbSs6S4kWiaqDibHsLVFhMPfu927mIUg5RkWicyd543J7yDAeaGZ2ibgPzGomHFuzq32beUqdEMbOVe3A/640?wx_fmt=png&from=appmsg)

第一二然后在吧"isAdmin":false 改为"isAdmin":true 进入系统

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvicS2Gv5UW3ccHm8vrYjXz5nvAkB8ia69oibn3icibVH87t73hicIjnViazia62kbTSic76TCqAjJ75ElfibOe5TzEzqYUcJWjb377niaZ1k/640?wx_fmt=png&from=appmsg)

发现直接变成教授了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvfOLicQHYh9IKGh9Vqiba7j7Q0D0wicpn3EGblskdO3onAJSFDBGic4qDsYZjjkOKOFSAxiakLibAxU9PQvy3UPfmByls1ThzQcxOuc/640?wx_fmt=png&from=appmsg)

访问导师的项目模块地址：发现泄露了大量的sfz信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EuRTxict4bPIZlZn03gichYIknkPZIkiaB4NG9MniaSOKicr6Q5SIiaG2E93EcomDnGz5ewYpae20x5HoTFGQibpiaeGGhb0ibV53sMyYx0/640?wx_fmt=png&from=appmsg)

**探测数据量共 2w教师身份数据，证书站直接拿下**

![](https://mmbiz.qpic.cn/mmbiz_png/tlibgKYKL9Es7kniaqmHJms0MKGbSFTx60PvjhWgssUF1HmkhbaRwb1gSncfgmiaNiciah2K7EocKLBXOJH5vz3kj4yoqeokiaDf49vPs6feYwbfs/640?wx_fmt=png&from=appmsg)

kfc也已经发送

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tlibgKYKL9EvhrvMjvWIa6L5S2CmT5SwZoeJcicESYjGm0oRBwia3TlSXhRXon55JkHAC7TwFAgpZQhWJpOnuC8zk0Uc11icYcSn3vgnCcjLNqc/640?wx_fmt=png&from=appmsg)

往期文章

[服务号存在注入之有意思的edu漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494659&idx=1&sn=e357db59d806c93f3a5a36b5c312b335&scene=21#wechat_redirect)

[湘安无事之湘潭大学冬令营总结](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494727&idx=1&sn=1d17ba9ee9bcd5fc4cfabe12d463e4da&scene=21#wechat_redirect)

[赏金src报告分享&&edu证书站漏洞分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494759&idx=1&sn=65084c580bb13fa31f82985721147e7e&scene=21#wechat_redirect)

[edu小灶案例之泄露上w敏感信息&有意思的证书站报告案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494702&idx=1&sn=5f0d05b6bea8550eda36ed2ce8ddbf7a&scene=21#wechat_redirect)

[学员投稿之edu漏洞的JS逆向解密导致任意密码重置](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494634&idx=1&sn=7cc83a90badea88d7d7d25583bd0c419&scene=21#wechat_redirect)

[最近学员小灶总结之双十二特惠](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494604&idx=1&sn=80f030c8114ee3287036586c670289c9&scene=21#wechat_redirect)

[卡顿页面导致三本edu证书现世之学员案例分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494572&idx=1&sn=14c21f1cae87dbdbf2ca5c4b10533f5d&scene=21#wechat_redirect)

[看完这场EDU通杀刷屏，连我自己都沉默了](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494535&idx=1&sn=113dd5e17065def94a5dacad361176b3&scene=21#wechat_redirect)

[edu证书站挖掘之学员分享案例](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494524&idx=1&sn=bff39f27ea27bccb884e832603acda92&scene=21#wechat_redirect)

[如何快速挖掘低微漏洞-项目挖掘总结版](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494500&idx=1&sn=2da7aa0d40075b462eb27695f2da9e83&scene=21#wechat_redirect)

[公众号接管漏洞之偷偷加](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)[小姐姐微信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494345&idx=1&sn=6d9ab80cde99e95c4d1ac710e091ffdd&scene=21#wechat_redirect)

[辅助学员审计案例-php代码审计](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=1&sn=2feaf2786717c2c577fe0b5230cbc58f&scene=21#wechat_redirect)

[学员-补天800赏金报告分享](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494284&idx=2&sn=c54ea91e0b3dc79f48f54f931df413c0&scene=21#wechat_redirect)

[从js逆向到sql注入waf绕过到net审计-edu证书漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494171&idx=1&sn=0d589d01dfbb068e53f9ad9c22676d7a&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞-再次绕过](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494082&idx=1&sn=6d1cc92a049d28b5395d417e0a5203a5&scene=21#wechat_redirect)

[空白页面引起的高危src漏洞](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494061&idx=1&sn=bfb1406138041fcba8286811aa7ac6e1&scene=21#wechat_redirect)

[难忘的优惠劵漏洞(深情哥破防版)](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247494035&idx=1&sn=422326cc617c33c78b3d518471e0862d&scene=21#wechat_redirect)

[什么？又日母校？竟然还有表扬](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)[信](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493987&idx=1&sn=f8edc2f3a113591e6e4cc57fdf821c8f&scene=21#wechat_redirect)

[sql server注入靶场搭建](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493947&idx=1&sn=885ee489f74211ba26a4a097f7ba30d6&scene=21#wechat_redirect)

[记一次学校ai沦为我的宠物之拿下e](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)[du证书](https://mp.weixin.qq.com/s?__biz=MzU3Mjk2NDU2Nw==&mid=2247493890&idx=1&sn=380e9dd566b29b713993b26f524fe0e4&scene=21#wechat_redirect)

[疯狂星期四两本证书漏洞合集](https://mp.weixin.qq.com...