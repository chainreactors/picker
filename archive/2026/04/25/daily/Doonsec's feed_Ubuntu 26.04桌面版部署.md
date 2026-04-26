---
title: Ubuntu 26.04桌面版部署
url: https://mp.weixin.qq.com/s/Zsfy2Oki1RCy9OolOqdF4g
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T05:02:06.655350
---

# Ubuntu 26.04桌面版部署

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9j14GSZeRZbia6yNpnbCrJ7QKQLwn3JbT5ffFVQk08N4pwibnJmCNlLnOG0YD9PhK3eNRFZfCAOkugHK9GYFbG8PxRJE3ibjsUMlJWmblchFf4/0?wx_fmt=jpeg)

# Ubuntu 26.04桌面版部署

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

自打CentOS停服之后（[CentOS 7停服之后该怎么安装软件呢？](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458856221&idx=1&sn=0a0891564d8a56fc8357f179146726e3&scene=21#wechat_redirect)），我几乎是用遍了Ubuntu自18.04之后所有的LTS版本。当然，在之前的文章中（[Hyper-V别开！VMware 25H2安装避坑指南，附Hermes新动向](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458866306&idx=1&sn=946a02606e9e71b56adc165ca4e32134&scene=21#wechat_redirect)），我们也对Ubuntu 26.04做了预告。

对于这次26.04 LTS的发布，我也可谓是衣带渐宽终不悔、为伊消得人憔悴。按理说，Ubuntu 26.04 LTS正式版应该是在4月23日发布的，也就是说这篇推送应该在4月24日与大家见面。但是，我在23日晚11点多刷新Ubuntu官网和各大镜像网站，依旧只有Beta版本，真是千呼万唤始出来、犹抱琵琶半遮面。

直到24日一早，我打开Ubuntu官网，终于看到了那只目光如炬的果敢浣熊，26.04 LTS上线了！

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZa208pG6LGan9BhOpa7q8B3hExGfhzTz6kWyUZiaTQa6g8hstzExvzKE6GYpPECAjyicwQp2YVhdPcanU0GAYnkzkiciawia3UOGBkg/640?wx_fmt=png)

按照官方介绍，Desktop版本的几个重大更新包括：桌面环境从GNOME 46升级到了GNOME 50，内核升级到了Linux 7.0，支持TPM全磁盘加密，支持云身份登录。当然，一些不太直观的改进还有新的默认应用、提升可访问性的辅助功能体验等。不过，对于桌面用户而言，最重要的应该就是GNOME 50和新版应用了。

当然，好马配好鞍，新版本对硬件资源要求更高了，起步要求双核2.0 GHz、6 GB运行内存，基本上锁定10年内的电脑了。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZwGcQel9UbiaiaNgek0YsHnQhPsTtdzYIhoSuYkic95ibmY24MtxXgmmDCNsHRG1j5ZribFLBCU3nFEVsMjibCOU7ZVRSNroropc5Nw/640?wx_fmt=png)

基础信息了解完了，那就开整吧，搞一台尝尝鲜。配置按照当前笔记本电脑的标配，给上16核CPU、32 GB运行内存，磁盘跟不上，先分个100 GB看看分区情况。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZoN5lObVUiaY5m1d4NAibAMv5pGkBF833oubeInkhWdey6vONYic3v2cqXeQjmgZysskOOiblUc147mpl2bOrX3fIUsSMJiaNzr3ibU/640?wx_fmt=png)

开机，经典的GRUB引导页面。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZbSwhYXkTGckHT1ZSNWlwxQzkUYTA7dEXm1SIUG9WTdSLz9iaxd8fFawjbMAbXypia1RaECeXibUxsA7ic40ua8HbkZzQVqy8nrZoY/640?wx_fmt=png)

进入到Ubuntu安装程序，看到下面密密麻麻的小点，步骤真不少啊，我们今天来数一下。

第1步，选择经典的【中文（简体）】。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZb5Rqab6a3FXqSPfuCzEDO1Iwia8YnL0gQrs83tLOG0jiaiattYzufcdZBmaBYPmcPsnxtKpC1OALQvg3BP1GWIL7fNRhe3koJVK4/640?wx_fmt=png)

第2步，可访问性，不用管。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYyC30B4JiaVrMdtUFsCC0as4O51ibQ0N9EfKepPLBjwQVmsr1cRLE2n2qxVMG4jeLxic0UKKHhZazatL1jbQyY7RK0AVkH6e4Npk/640?wx_fmt=png)

第3步，键盘布局，默认使用跟中文配套的【汉语】。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaibZ4GdicCD01ZzdvoXrbhX0QgeU264Q9dExhbUicbVwwxZ8faeynciatGCibB8ibKiadKkib8SoMRqa99bbnPsYibDxgibZODAfCZEQcY0/640?wx_fmt=png)

第4步，使用现有的有线连接连接到互联网。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaibrcpfUpQO2sNGhFnhLxnksUIW6DblAicw5JSNqGTiciawTGibb9R9j4vNvHNmUictFu3spt98pfiahLpiaU8XrSxVV2IvZMuGYm3ZvM/640?wx_fmt=png)

第5步，选择【安装Ubuntu】，第一次出现了Ubuntu 26.04的Logo。Ubuntu 26.04的代号是 Resolute Raccoon，直译为果敢的浣熊。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbcPsNRZqmSibxGQMLupDTCDyibyia0a0EEMoHicnVZXiazf7NHyr65Kd7ZJdLHtJDiaqbKSpqx9gzzIibOZMBxt7QE1iapPZCdAfeM3EM/640?wx_fmt=png)

第6步，使用默认的【交互式安装】。如果大家对于【由自动安装文件自动化】感兴趣，可以查看我之前的文章（[插上U盘自动装系统？一文掌握Ubuntu服务器版自动安装镜像制作](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458860448&idx=1&sn=d833cc7414ffcec71297ae6bdbbea30b&scene=21#wechat_redirect)）。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaUd6faMjib6iaAcdyurauaIVacu8KjypQOhWzgxrpxIBNn2G9Rk0ScGxYJ0kbd8S7OibpLGbkRJlhRcH4axCPLQQ08GdUpZcYf5s/640?wx_fmt=png)

第7步，安装的应用选择【默认集合】。有意思的来了：进度条上的红点仿佛学会了缩地成寸，直接从第6个跳到了第10个。这大概是Canonical的程序员在教我们什么叫欲速则不达，或者是为了安慰我们这些等得焦急的工科男？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbkTzzculXIdq3diaC2BgUfbBEEibuM9P9Yj7frZK8mAq7wMc5AfQoRrnpxyjz6eb8ttb1gIa3ELjWBF44Q6cFbBqkCqNzrXSWZU/640?wx_fmt=png)

第8步，暂时不安装推荐的专有软件。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZqicmPgicYibwEe4EuuDVLpSZlrcbt5CRlOloqIfDaibFUdSp3aXTLADkt4Xzl0h5C0b6SW0QtPpRhVtf4gNyMPbeiaDQhvxSuchc8/640?wx_fmt=png)

第9步，安装方式选择【擦除磁盘并安装Ubuntu】。这一步的红点展示没有往后移动，跟第8步一样，处于第11个点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZa1X2nrHDIyV7QEFM21E4oORUVD7pfx3AWZsPj1xAFar8PbXUuQ1dLRkEgHaw7lLmcU8H7nH0dQTriay3qhUIe7RCsiajSbjUjXQ/640?wx_fmt=png)

第10步，加密与文件系统选择【无加密】，依旧处于第11个点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYQNmFVyqiaJNPicWmvZiaepYFbnvFdb9olubaMCSMTUOvZicDJQp200PfRfz8njWEKa3JibicpFLaQaQic0y0tg9qAWqicqLbNB8vpP0Y/640?wx_fmt=png)

第11步，设置账户信息。注意这里的【登录时需要密码】，跟桌面共享相关的坑你还记得吗（[原生支持真的好用吗？Ubuntu 24.04桌面共享vs远程登录全解析](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865180&idx=1&sn=f4e3583479542879415778862a907014&scene=21#wechat_redirect)）？回头我们也再次测试一下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbYMuchFb86Nu2vSZXyZdbl8IFfzSsmgnsAiahU4ut4JlzV8umjkdlLKYnrIcMNJbS9EIASqJTlCiaUzZb9eopkAejJFdZAZfjn4/640?wx_fmt=png)

第12步，选择时区。这一步没什么问题，但是一旦文章里面有这张图，就会审核不通过或者被限流，有谁知道问题原因吗？这里又跳了一下，从上一步的第12个点跳到了第14个点。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaUlm8iaXNqjTEgZMS5MMmuNqBq2oqribWyPh3ncGYagP4fANF5MPQL5QPgHIeYtyicxjHiaUOcKKzYUN6r9u7mFNMX38WuBCicW2vk/640?wx_fmt=png)

第13步，终于到了正式安装前的确认环节，单击【安装】按钮即可。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZah2SOoib3DNUKbBDjBzqVJpGCjVNQiaV22he3hicKSk33QictSWKvOGuw5NBqUIHOR5pIwbtFNDnmiaKdMZ0emAz49mcHT15tuNJgY/640?wx_fmt=png)

第14步，等待安装完成。一共17个点，当前处于第15个点，这在Ubuntu的新版Flutter安装器中，应该是UI逻辑与后台任务解耦导致的，不知道算不算BUG。

安装过程中的动画还展示了Ubuntu 26.04 LTS的核心特点。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaHw1BFkHbW85oeKOHYPQM8JMglstcrO0TWlzKpyQSCkrPBCIw3FAzI2Q052yMlcTUrVzALqn3qT5GEMcjG2MeEOuTq6rKqkw4/640?wx_fmt=png)

第1个是个大帽子，后面的基本上都是和应用商店相关的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYq0uAQ8gaygkB6dMBw0ibw3icibutby5v7554Z3B3ZDD4JImMCiboHEPYLFH6wSAZtLTLEgCzn7wzibAXOYrwW8V2EXriclgAZU3Ymw/640?wx_fmt=png)

结合当前最为热门的AI，展示了开发工具选项。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaArR0WXuTaA7mrLuomrHaT1GbKyTTarf69oQzA9IXHV6b4UZVlbgyAePibDibMicrH2mmCTV82icvvBhhf5xJdbYcattILUm1yWzY/640?wx_fmt=png)

还有创意工具。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZbt4dXaLWicEiaprVL1my3E5ybyln0HmaYxvsbxLrCHicQw14VRrVf1LyL3EPr4icZsMHEJibaiaOTq0FDny1f8W0Pcgn0A0iaQJNAdnk/640?wx_fmt=png)

这里也提到了游戏玩家，不过Discord是游戏（[还在为AI API费用发愁？我找到了免费使用Gemini 3和Claude 4.5的方法](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458864179&idx=1&sn=445706bfdcedbe57898abcd7f3438b48&scene=21#wechat_redirect)）？OBS Studio也是游戏？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaATJrgGc5W9q7OBuIz4uZBwRhz1iaVVuHJia1ToKZ74kBmDa1va2iaPHHLwbYcSrTjiaXNARmLXia7Z0Ek2vyAL78yRN02TmwbEJeY/640?wx_fmt=png)

安全性这里，直接把WireGuard贴上来了（[IPv6隧道搭建指南：用WireGuard轻松玩转IPv4/IPv6混合网络](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862388&idx=1&sn=1aebc96f663641b757a4175d060b83de&scene=21#wechat_redirect)），懂得都懂。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbFCRia7sEdzgWM1libFVOWZOaicctjcYiaQ7xBqygIXSYJhXPrJiaariacgdJSS2KJ9emGzDQc6f0WnVgDUR9gDbA9D076iaViab2B0Og/640?wx_fmt=png)

文档编辑工具他说预装了跟微软Office兼容的LireOffice。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZbvBdo86I851gM9FwtAICIWN2SDibWLCXTbicUibxv6EZDeZ1DbvO0jReiamBUqvdicjQORvNEquleo7OegcGU3oxhLwZS9ZWf1PQNo/640?wx_fmt=png)

还有提升可访问性的辅助功能体验。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYoxa0fdlKibsflfHS3pzxGsXbGVibYEXuPUkhqfkgrAjURicsc20ibnC7441yg7jrdpWNXt2mWvdKmWuxB6e9sWwE2S1MB0GYEibyc/640?wx_fmt=png)

最后，展示页面定格在了帮助信息页面，不像之前那样一直滚动了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZiblUdVQ9BMBImOksRkRYt8YVZBTr6Os4CthxHy5KpkkuP70aapStaAOvF3icRNasx5azgaKxvp6ue1QjUs98yicDrbEASkGFfHo/640?wx_fmt=png)

经过短暂的等待，安装完成，单击【立即重启】进入系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZrdvGzQhdR9WsTJRDIFM1JdLJeiaCnhajvPO57gW9soe6vKxIjN9quvERhy7W3PozOEwTJuFSUsIZ2Dvv7FOPrXOMNvdxPwrKA/640?wx_fmt=png)

启动过程的转圈动画也换成了这个Logo，看起来还挺好看的。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZajVicyWp7aSI2suYWTicjRN9rBiat0ic6bEwCDjt59ic5qxjrScPh8zR88VuryRjt2ytvT0yRbke9uB09N9WeZehJaC9AQPr5ticXiaw/640?wx_fmt=png)

经典的初始化配置页面，不启用定位服务。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaibPEjmaLtBMaaqrsfxn5SdeSUjiaWLTFugA6hEPGSWZ8QQY9F77QD90KxOvkODjNx0ic1q4eCprckU6HcqGXjH77KicK2IILZpno/640?wx_fmt=png)

不与Ubuntu团队分享系统数据和错误报告。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZDAE2OtOsUQdUtrIOKvq2P2QpV4kw8u9WSSgbq6t3X8FjdFXsxwoUw3mlgsic4VRLy92wpiaMBJ66WjGjaqACLcibhicEcMYGDSY0/640?wx_...