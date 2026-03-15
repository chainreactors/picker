---
title: 火爆全网的小龙虾！OpenClaw保姆级安装教程，一步到位
url: https://mp.weixin.qq.com/s/jZ95HD_zAht50uBaYJpoLA
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:32:48.238821
---

# 火爆全网的小龙虾！OpenClaw保姆级安装教程，一步到位

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ykvGPw5iakHicSzSpaibMut5BBkibN9UGEkhf8ia6O8Ls15hKcTKGZ9dricTmbchjCgcZd7qzS1vV9ic9KojwPlGueibfasNn9DcW7JIiby6aVYL7Pz8/0?wx_fmt=jpeg)

# 火爆全网的小龙虾！OpenClaw保姆级安装教程，一步到位

原创

小白爱学习Sec
小白爱学习Sec

小白爱学习Sec

![]()

在小说阅读器中沉浸阅读

0x1引言

1、现在关于 OpenClaw 小龙虾的安全提醒越来越多，这东西确实有利有弊。千万别在主力机上直接装，要么找台不存重要文件的闲置电脑，要么就在虚拟机里跑。

2、另外装之前最好先了解清楚它的原理和风险，别盲目跟风。新东西刚出来，风险还没完全摸清，一定要在隔离环境里安装和试用，别拿日常工作、存资料的机器去冒险。

3、目前小龙虾有3种部署方式，本地部署、云端部署、大模型厂家部署。云端和模型这些都需要成本和门槛，本地部署门槛相对较低一些，新手强推。

4、各位师傅安装的时候建议先下载需要的组件【文末附下载链接】，部署的安装包都是从国外网站下载，自己装的时候下载都等麻了，能科学上网的也可以直接官网下载。

5、本文主要参考了一些网上的安装方式，仅供参考，不足之处还请斧正！

0x2安装教程

2.1下载安装包，安装【cherry studio】（这里主要以Windows来进行展示）

下载地址：https://www.cherry-ai.com/download

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH9hKiaRCFhxBUQuBqPt2NS8PaG5sXEiaEmHwndoDJ1GPibaRXCGmibqibH07TrcqyMpBjb1DQvloIcfrOia1Q7QGKbuqIpjSp3UrMNsM/640?wx_fmt=png&from=appmsg)

![]()![]()![]()

Windows的exe软件的好处就是，傻瓜试下一步直接搞定

2.2、运行安装

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH8qgGGxqsBkVAZtWfARibvSDiazvxic011iaToUhiac5jIjnJhA8YyXxDIOjKLlNQqzUlF7lC41V3nXofZxtO2HuPRETia40bibua2Fbc/640?wx_fmt=png&from=appmsg)

如果你电脑有多个用户，你想其他用户也能用，那就选所有，如果只是自己用，那就选仅为我安装

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH9QqibQiaPSC3CTxhRQiaLH6Ju1k9UspQJmjtTSCibcgYcjccPuqWFL9f2rXug7zbzpc5Dnpib3vSPOcfejMfhJfZibHLVYiad5a9YZmI/640?wx_fmt=png&from=appmsg)

2.3、选择安装地址

建议不要装在C盘，我这里是虚拟机，就这一个盘了，我就不顾那么多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakHibl0xTWua4Cpu4nE8HlZL8kft96U90BZ59VClRoDP8gp18dejmicspf0Q6fWuROC0eBCPQiaKiaxYhyvKERgnWf1fvicIiaI56FHdz4/640?wx_fmt=png&from=appmsg)

2.4、安装【cherry studio】完成

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakHibEPjS9uzHSJrCKmnTbeL4xZvWaCleiaaK2hdk5XU45HarzTcr8nSxAMGWsWNID4oiaCmp6HXboTpo0QkIlpIkUr8U5crHZ0dibeE/640?wx_fmt=png&from=appmsg)

0x3配置模型openrouter

3.1、配置模型openrouter

OpenRouter是什么？

它整合了几十种不同的大模型（比如 GPT、Claude、Step 这些），你不用分别去各个大厂申请接口，只要在 OpenRouter 注册一个账号、拿到 API 密钥，就能统一调用这些模型，省了挨个对接的麻烦

3.2、点击【设置】这个图标

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH9vYBIWTWM2ZpOHcmQ3aV33nIAic2hm8FUzoeClDYJFInlAgTB3gicBJygK2zQFWgTXyuDD7P4M4KzoQWRwdiacVEiblHBLh6gL24w/640?wx_fmt=png&from=appmsg)

3.3、点击创建密钥会调用电脑浏览器

打开openrouter，去注册账号，获取一个密钥，页面会自动打开 openrouter 页面（网站是国外的访问较慢），注册并登录账号。然后点击【Create】创建一个 apikey。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/hR7N0Kkr3z61JCImdNiavPkv70VY96icxZOmV1YADdys1vfnpLUL7MzdKTUoPPDnGorQuKkqgtNcMHM9UUcrgDmpZeJ1B9rbQ2AkS1xpGZibBs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

3.4、在【cherry studio】，输入创建的【apikey】然后点击添加。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH8xlbzrPgflZrQmoAoP7bnPSicia59bI2clbxNakBV6a6JEFoE1meENyIcwNl6oCjialzTaTT7GmDtFcypErym75STJtSINKrk238/640?wx_fmt=png&from=appmsg)

3.5、这里将这个免费模型名称粘贴进去：stepfun/step-3.5-flash:free

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakHibibZhUKUWld3IlK5udxwMhUrtgtBdplcfjZ0YFXV395YicrENKlwSRqicYArdBNC4IxJktoDEvRIQIbpaHVDgXGe3tFMBST0RbpA/640?wx_fmt=png&from=appmsg)

3.6、接着来到首页，选择阶跃模型。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH9Hj4EsCWzwLTB0ia5icdwcvaFXjombcxS5QoIibdneJmibLpq3QlHhxT7cvHymK9GTy6WD07eoUOBUPUo2BSqJb0BAzqtO0iauOpWw/640?wx_fmt=png&from=appmsg)

3.7、简单做一下测试一下，回显了，说明配置没问题

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH94AyzRBGDvRMHRictibibJ9kPtDQibOcibv29fSbJnyAn5eYLCBUPjfaVCakuA482fK8Pcv9KobUyqdumXbhPAaI4rRicpP8Ang8I88/640?wx_fmt=png&from=appmsg)

0x4 OpenClaw的配置

4.1、在首页的【+】号，选择openclaw。

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH8jfdMehHSlEEybPelIsjU0RY9icKsajLOia6qiaAl4Fk94sTUHOrLPib3oI4VdpXf3QspLY6vfqZ3BsKyHHa274hwZlPrV2845C5U/640?wx_fmt=png&from=appmsg)

4.2、 安装必要组件

        ①下载安装【Node.js】组件，

        ②安装【Git】工具，

        ③最后点击【安装OpenClaw】。

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakHib9O3jUcNxaE95h6pia89BJmia770vHVib0PQglE2uMnA38Eia6EpVia3G17VicHUTrL99RVmvvgNfjyagewBZdVOFdx0icp66gB1unvk/640?wx_fmt=png&from=appmsg)

4.3、又是比较经典的傻瓜安装

下一步、下一步即可

![](https://mmbiz.qpic.cn/mmbiz_png/ykvGPw5iakH9273baRdnHjrff3HcibBnJKj5F1j9SIW6m3iajHCL7q3RGmjyQj7hF2s66JyVicSCqnlEDkvd9VGW1pStthFITBbibiajsZ28Hsx9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakHicqM3dEOdBmv3vcZl4MdHnPVXaEBGCcZbLoGQ5El25d9GPHKDzoj9bR8TmgwL1GrXicrO9pbIzdHTeSCeAE7qlciaZIBfl6KBkUU/640?wx_fmt=png&from=appmsg)

4.4组件安装完成后，安装openclaw

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH9gnv4ibHwkoYNM4EibYUEibpbfPpvqSvhq3kia3abP2KOI3qianhgJopd1DsYHk1w7KWpbBicApKbQvdjkfBvQvcc8X5Q0D5licAB6UM/640?wx_fmt=png&from=appmsg)![]()

4.4、完成后，选择我们的【stepFu/step-3.6-flash:free】模型，然后【启动】。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ykvGPw5iakH86FwicyAgPEicVpTpFwAo3ibPyPxENaBEhpDPR0wQnOHmKg2vW9URO2kK9deB80XA0edOicKXWSB0f4buAxBUmPtGicwBIUneLCiaTA/640?wx_fmt=png&from=appmsg)

4.5、看到这里整个本地部署基本上就完成了。

![图片](https://mmbiz.qpic.cn/mmbiz_png/hR7N0Kkr3z7suD8LYDNKEUF4Mj8IicxWhlCKp4LiaJVFteInfrRIVNYBOjRy6HFVTmLmwWBxo0XeoaYlzX9hvSoQLSHOOoF1QibzJXTjKPXW4o/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=19)

4.6、最后的最后

小龙虾运行需要比较高的权限，不然基本就撂挑子了，师傅们在使用的同时还需注意安全风险。

0x5资源链接

百度网盘链接：https://pan.baidu.com/s/1JTt5szQinb-jTn-H3IirnA?pwd=5ie3

迅雷网盘链接：https://pan.xunlei.com/s/VOnblWifGhf36i2KbbeXbUg\_A1?pwd=3nkm#

夸克网盘链接：https://pan.quark.cn/s/bcb666d0fdfd  提取码：3BtZ

---

![](https://mmbiz.qpic.cn/mmbiz_png/RITPxDQz30icticGDszvMCTbvDxbl8zxyibFCCszl7UKqW1MsxUqMyDeWiaDTrea8mLtKZGw44uMibHkpxSoLg9t8ow/640?wx_fmt=png)

**看完点赞，养成习惯；随手转发，好运相伴！**

![](https://mmbiz.qpic.cn/mmbiz_png/RITPxDQz30icticGDszvMCTbvDxbl8zxyib2DBL0ricNOiaULtxdjiagavVW374KV3vFItTq55oeh1cYOs8sDubHI9Aw/640?wx_fmt=png)

往期推荐

[【工具推荐】自动小程序反编译并匹配敏感信息](https://mp.weixin.qq.com/s?__biz=MzkxOTIzNDgwMQ==&mid=2247484657&idx=1&sn=31d71a7288d564d80630372f8393ac69&scene=21#wechat_redirect)

[2026最新BurpSuite安装下载|多平台支持|新功能体验](https://mp.weixin.qq.com/s?__biz=MzkxOTIzNDgwMQ==&mid=2247484804&idx=1&sn=fb8dff192475e6d0ddd9403cd57058a8&scene=21#wechat_redirect)

[AI 自动逆向 JS 加密分析工具！直接搞定前端逆向难题](https://mp.weixin.qq.com/s?__biz=MzkxOTIzNDgwMQ==&mid=2247484797&idx=1&sn=b3bc5f96579427f15bebf6ae281749a2&scene=21#wechat_redirect)

[XSS常用FUZZ字典](https://mp.weixin.qq.com/s?__biz=MzkxOTIzNDgwMQ==&mid=2247484756&idx=1&sn=c1647cab3f6ccc2c2328f6a430aa49bf&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/x095A8xUTuVrDEyCViaUoBggqXNtSv9EN1d6bsVCicKvIibwosiaAvbVrggyFq6hvVjBglmc0tgWlJorruHVLaTUBw/0?wx_fmt=png)

小白爱学习Sec

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/x095A8xUTuVrDEyCViaUoBggqXNtSv9EN1d6bsVCicKvIibwosiaAvbVrggyFq6hvVjBglmc0tgWlJorruHVLaTUBw/0?wx_fmt=png)

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
在看
，轻点两下取消在看
分享
留言
收藏
听过