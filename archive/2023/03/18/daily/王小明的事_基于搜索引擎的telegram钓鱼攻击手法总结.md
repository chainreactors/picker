---
title: 基于搜索引擎的telegram钓鱼攻击手法总结
url: https://mp.weixin.qq.com/s?__biz=MzU1NDYxMTE5OA==&mid=2247484927&idx=1&sn=564fd831cd7856768b7b3100db5b8f88&chksm=fbe1bd6ecc963478096221010bf977a8becbe84b0d1f886e5ef32f819a073f4b3efa92b73cfa&scene=58&subscene=0#rd
source: 王小明的事
date: 2023-03-18
fetch_date: 2025-10-04T09:58:40.181960
---

# 基于搜索引擎的telegram钓鱼攻击手法总结

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzwWGLiblQo7nlYrcNEL39s0ibwicqemDDfpkwlvlKNeB7yhWjdEiab5Gotw/0?wx_fmt=jpeg)

# 基于搜索引擎的telegram钓鱼攻击手法总结

原创

流水账小明

王小明的事

目前该攻击类型的主要受害者是tg中文用户，固然tg中的坏人含量相当高，但是对于像金融、贸易、区块链等这些带有跨境业务性质的甲方安全来说，个人认为这是一个不容忽视的风险点。今天能替换你员工剪贴板，明天就能给你域控下发个 lock.exe 天下大乱。

换了个方向写流水账，欢迎拍砖。

## TL;DR

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzakjHlRH2XWqYEtwYkHXib4icckaoAlU61CoVaJJ1mmo35YxfmiaC7Gsgg/640?wx_fmt=png)

搜索引擎tg钓鱼手法简要思维导图

## 搜索引擎分类

### Google

目前Google是该攻击类型的主流平台，因为telegram的使用需要XFW以外的网络，也就意味着具备该网络条件的用户一般也具备浏览谷歌的条件。截至目前为止的相当长一段时间内，直接在Google搜索 “telegram” 相关的关键字，返回的搜索结果中的前1-4条一般都会带有 “AD” 或 “赞助商” 这种标识，这些广告结果当中绝大多数都是有所图谋的恶意攻击者故意投放的 “有毒” 广告。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzhQymt0dbcs9yqoiciajU5buJ0dwnVtyYfFL9GjQ4vaC9fQtP1YkOajJw/640?wx_fmt=png)

### Bing

Bing搜索引擎也具有付费广告服务，但是使用bing搜索引擎直接搜索 “telegram”、“纸飞机” 等关键字的话，得到的页面是被过滤和筛选后的，猜测是因为政策原因导致搜索结果均是新闻网页。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzV1goVXNXdjjEj2bibgsj73KGcPQEFUpMKWiapcmOtl5Qbgb0jaUXv4Pw/640?wx_fmt=png)

但是该屏蔽政策似乎没有兼顾所有的关键字，使用关键字 **“电报”、“电报中文版”** 等关键字仍然可以得到真实的搜索结果，其中包含广告结果以及使用SEO等手段将排名做的很靠前的假冒官网。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTztsnic4CEGnpd8xwBEPHjKMhoeKdwWFqF5FickiaEIAcvZ9XtukaibhevSA/640?wx_fmt=png)

## 广告投放筛选条件

详细分类的话，广告投放大致分为地理位置、语言、意向群体、关键字这几类。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzr5vrBLfRRLZZlSq4HRdsMDO6VpJjr3dvAxyQVfAfpicTY8WfQvOQBhw/640?wx_fmt=png)

但是站在自动化搜寻并封禁的角度，我们的方向可以有：语言、IP归属、地理位置、关键字、时段、搜索次数、客户端UA等，尽量满足这些条件去主动迎合恶意攻击者的投放群体画像，以此来达到最佳的封禁效果。

下面仅举例几个对搜索结果影响较大的关键要素，不一一赘述。

### 语言

简体中文搜索结果

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzwZYicO1N54EuibIceEOyrBrsBVgVoFMXu5Ijwx64PmngWcfM8sbX37Bw/640?wx_fmt=png)

繁体中文

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzWphWS5vrCbTuASTS94iahJxOibNdibIhWc6d8vG1hcmafQfHaNHWV4VZA/640?wx_fmt=png)

英文搜索结果

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTz6yicNKicA6RyhF6MMLo0IuIJ9ZIaaQ1TxqqiaOzficia9V0ldF3ibH8XlZzg/640?wx_fmt=png)

### 关键字

以telegram中文版为关键字

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzTowQ21xKYMVfmHhPNib13PcVqh8dp41RwRR5cSgEbKkZk11ylf2HWUg/640?wx_fmt=png)

以纸飞机中文版为关键字

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzxic1L0jrlibhPq0kQ5TwLfRQ6jaUGCwqajicaB7krsE75gjeGNumicCticA/640?wx_fmt=png)

以电报中文版为关键字

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTz1dm2DEvayicsQ9ibulPxzTB3pSTz1Jj6CibfwWFr3McLJnBEGp7GfX1zA/640?wx_fmt=png)

### 客户端

直接展示移动端的搜索结果，根据部分搜索结果的网站标题可以看出，其目标群体为安卓用户，这些搜索结果使用PC桌面端的user-agent是无法触达的。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzOU1CuOBcH2grz7b0hZkF9ucMb7UCqrloicLY3S9QhcJ8SIBmIHQzthw/640?wx_fmt=png)

### 位置

Google的广告投放按照位置来区分可以简单的分为顶部和底部两种，顶部的广告展示位于真正的搜索结果之上比较引人注目，转化率可能会相对较好，但是容易被人忽略的底部广告位也存在telegram钓鱼攻击广告投放的情况。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzNM5Cyyia8u5GOPBGTpmsYGoNu1vZliaqeSflPBZ3G0VqQhVMiaLNMzYQA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzhVIkxnvd9TbgSBiaWtTicGfz9OwOEjvNpjBvy4fLO47gXDsfdiaHsJ5PQ/640?wx_fmt=png)

## 中转页面

中转页面即为搜索引擎给出的搜索结果，攻击者一般会围绕 ”白利用“ 的思想采用各种手段保证中转页面的合法性，下面介绍的是结合日常安全运营工作当中发现的主流中转手法。

### YouTube频道页面

YouTube是最传统、在搜索结果中最常见的中转方式，从最初出现到现在可能达到数年之久。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzL16Eu4H6zLj9cF1EtFBOg7jZSaGY9w872xRjx4JqjMZWchCpuVJazg/640?wx_fmt=png)

目前为止基本只有一种形式，即创建一个名称为 “telegram中文版” 相关的YouTube频道，频道的背景、介绍话术、头像、各种图标ico等均设置为telegram相关，给搜索者一种telegram官方制作的推广页面的感觉。

然后频道详情页面下方的超链接被设置为恶意的链接，以此引导用户浏览假冒的telegram官网等页面，直至用户下载安装假冒的telegram客户端。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzm4OgNE1iaYLkQ2OvI3FDIib9AWIibp6IvNRZIcZWzsh4X6mjy2Y781QXw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzjj4x81RPVYOVIJAyIzRpuBPwEwb3LJj4riaKicK2faZCW8zvgYYGpiazA/640?wx_fmt=png)

#### 频道链接指向问题

在以往的应急过程中，大多数情况下频道页面下面的6个超链接对应的跳转链接是一致的。

需要注意的是，虽然不是很常见，但是有时会遇到六个超链接对应的跳转链接不一致的情况，所以手动排查和自动化搜集时应该注意这个问题避免遗漏。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzkHk0YUvxaWGCwBDfnQvPMVCwmF3Oj1rB6zA4PYUmm8c7aOvwiaPuHjg/640?wx_fmt=png)

#### YouTube搜索频道

YouTube支持根据关键字搜索频道，不过搜索结果当中作品和频道是混在一起的。根据这个思路可以直接通过搜索关键字的形式找到这些假冒的频道页，再提取详情介绍里面的超链接，批量封禁。

并且根据实际观察到的情况来看，大多数实际触达到用户的频道基本都是提前建立的，提前时间在几天到一两个月不等。个人猜测攻击者准备资源、通过审核可能也需要一定的时间，所以这种方式封禁域名有一定的预判作用，时效性的效果可能会好一些。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzvPvict1rEYFqicy5f5piaRpOBwssmMUBCqYic0b6mOpksAdbAflVsdWRhA/640?wx_fmt=png)

### Google文档

Google文档即为谷歌官方提供的在线文档服务，使用Google文档作为中转页面的手法出现时间相对较短，不过也是目前出镜率相对较高的一种中转方式。

搜索相关关键字时，可以看到推广域名是 docs.google.com。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTz6uY49jkuRcAVbQ6RbVJnJgDVN7S7yzF4j8gNKqSGUZeGf3sQEQS0zA/640?wx_fmt=png)

链接对应的实际就是攻击者设计好的谷歌在线文档，文档假冒telegram推广相关主题，下载文本的超链接同样被设置为恶意地址，诱导用户继续访问假冒telegram官网或直接返回恶意telegram客户端的下载地址。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzex0Ugk1NG3Tr0FIK7vSs7G4WiaWrxBCMN45pN9G3pL22rp2lcBAb3Zw/640?wx_fmt=png)

### Google Site

该攻击方式的思想与Google文档相似，均是利用Google提供的第三方服务作为中转恶意地址的 “白名单” 基础设施。Google Site本身为Google的一款以Wiki为基础的在线网站制作系统，为Google Apps的一部分，一般被用来搭建基础的展示网页。

搜索相关关键字时，有时可以得到域名为 ”sites.google.com“ 的搜索结果。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzWLL4Lpf0pYJibd1aAy17kdEVNAMDkjywVwpFjYgTMMBRfZJWzDDSMKQ/640?wx_fmt=png)

点击链接后，可以发现攻击者使用Google sites的服务创建了一个仿冒telegram官网的web站点，最醒目处的两个按钮就是恶意客户端的下载地址。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzKVgTjpjccUmPzX3TibQgCgU9QrUF6FOMAyVMfUszJ6REw8dcvYRm6BQ/640?wx_fmt=png)

上图展示的是为Windows PC准备的钓鱼网站，针对移动端的钓鱼攻击同样也有使用Google sites作为中转页面的案例。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzVG4AWkKCSxUMmIrxJ49C2u4QDga0tuZepDQfqYXGWubjxa7YcGbytQ/640?wx_fmt=png)

### 搜索引擎语法

接触过信息安全的人可能都对Google hacking不陌生，因为早几年网上的教程基本都是从 ”信息搜集“ 开始讲，信息搜集教学当中经常就会带有Google hacking语法教学这种环节，其中比较常见的大概是 inurl、filetype、site 这些语法，其中site、inurl 语法都有筛选指定的网站搜索结果的功能，并且比较通用的语法基本对大型的搜索引擎都是适用的。

#### Google 搜索语法

当发现搜索结果中的推广地址为 www.google.com 的时候，对应的就是攻击者利用谷歌搜索语法的结果。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzLYYPMmQzic5ibTJleLoONABkcfibpmQk9ZSOyNJeaYIehTvoiar4DUES3g/640?wx_fmt=png)

点击推广的结果后，可见链接地址对应的是针对某个特定的假冒telegram官网域名的搜索引擎语法搜索结果，攻击者利用inurl语法使telegram只展示位于该假冒域名下的url搜索结果，受害用户不管点击哪个搜索结果，最终都将在攻击者的假冒官网上下载假冒的客户端。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzUliaAZKn3INiaRoz2ayPicPVsb4gAN6sDeiaWYVqzglaibWyvCj6HjRCJVQ/640?wx_fmt=png)

#### Bing 搜索结果

搜索结果中可以看到域名为 www.bing.com

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzVrflyxm5ibPStrrkUR0Kl5tcfU18QX86ZG3pLH3dOHuGV4lx045br0w/640?wx_fmt=png)

点击后发现攻击者同样是想通过site语法来限定搜索结果为特定的假冒官网地址

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzIQmkkTnB3UTbib0MvfNqOJY7iaq0R5zYkDJTkrBf3BHz8roPOdvvqmpw/640?wx_fmt=png)

但是由于上文提到过的疑似特殊原因，使用Bing中转似乎不是一个很稳定的选择

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzKAMNIUd1EiaVpicu9w4qT9wIX9ia3WE2kPb31SM35x7dQPBibsSy07yA2w/640?wx_fmt=png)

### 直接跳转假冒官网

有时也能看到攻击者直接将自己搭建的假冒官网作为推广地址的案例

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzSPn2XWySpXB5W3reCD8EzEkzqiaN1FxLVdMibYeYuvY4bUlI1WQTOfVQ/640?wx_fmt=png)

用户在搜索页面点击搜索结果后，会直接跳转到假冒官网地址

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzIN4jzibV3RLcpPGia26LS35sGD6wv6KY7jXgqStyAy8FuNwpoE17ZMIg/640?wx_fmt=png)

假冒的telegram官网域名当中绝大多数围绕 ”telegram“ 这个关键字，但是也能见到少数没有规律的域名作为推广结果的案例。

![](https://mmbiz.qpic.cn/mmbiz_png/4iacC3bS3Zh1hKL5PoXpRDAbicibLpgicFTzgeTpwEV1APicaAbeJkBGobeFbqjJia5KYqG5APMYDcwnaicVOCmuglZyQ/640?wx_fmt=png)

### 小众搜索引擎

像 www.discovertoday.co 、hk.top10quest.com 这类的域名具备搜索引擎的功能，但是又没有听说过的网站，我暂且称之为 ”小众搜索引擎“，该类网站的特点是 ”也具备广告位的设定，并且...