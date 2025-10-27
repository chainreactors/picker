---
title: spring 审计常见 tricks
url: https://www.cnpanda.net/talksafe/1277.html
source: Panda | 热爱安全的理想少年
date: 2024-10-29
fetch_date: 2025-10-06T18:50:21.836849
---

# spring 审计常见 tricks

[![Panda | 热爱安全的理想少年](https://www.cnpanda.net/logo.png)](https://www.cnpanda.net/)

搜一搜

# spring 审计常见 tricks

本文最后更新于 2024.10.28，总计 2321 字，阅读本文大概需要5 ~ 15 分钟。

本文已超过 343天没有更新。如果文章内容或图片资源失效，请留言反馈，我会及时处理，谢谢！

图 1 是利用墨菲安全的 jar 检测，快速梳理有漏洞组件的 jar 包

![1.png](https://www.cnpanda.net/usr/uploads/2024/10/1370617645.png "1.png")

图 2、图 3 是快速审计漏洞的时候，需要关注一下web.xml或者xxx Service.xml中的特殊 servlet 或 service

![2.png](https://www.cnpanda.net/usr/uploads/2024/10/4015349066.png "2.png")

![3.png](https://www.cnpanda.net/usr/uploads/2024/10/3296234983.png "3.png")

图 4 是为了在审计的时候避免找不到相关类的常规快速处理方法

![4.png](https://www.cnpanda.net/usr/uploads/2024/10/580161364.png "4.png")

图 5 是批量反编译的两种方法

![5.png](https://www.cnpanda.net/usr/uploads/2024/10/588962539.png "5.png")

图 6 是通过关键字来找路由的 list

![6.png](https://www.cnpanda.net/usr/uploads/2024/10/2665839186.png "6.png")

图 7 是在可以编译代码的情况下（通常是针对开源项目）快速找接口的插件

![7.png](https://www.cnpanda.net/usr/uploads/2024/10/199148806.png "7.png")

图 8 是向skay 师傅学的，在可以调试的情况下，在这个类下断点可以获取到一些路由 list

![8.png](https://www.cnpanda.net/usr/uploads/2024/10/1922915469.png "8.png")

图 9、图 10 是在suffixPatternMatch为 TRUE 的情况下绕过鉴权的一种 trick

![9.png](https://www.cnpanda.net/usr/uploads/2024/10/4183086228.png "9.png")

![10.png](https://www.cnpanda.net/usr/uploads/2024/10/545762737.png "10.png")

图 11 是 在 setUseTrailingSlashMatch 为 true 的情况下绕过鉴权的一种 trick

![11.png](https://www.cnpanda.net/usr/uploads/2024/10/971481287.png "11.png")

图 12 是向三梦师傅学的，当项目使用了 springsecurity 的时候的绕过场景

![12.png](https://www.cnpanda.net/usr/uploads/2024/10/1888228632.png "12.png")

图 13、图 14 是 startsWith( )和 endWith() 的鉴权绕过的一些方法

![13.png](https://www.cnpanda.net/usr/uploads/2024/10/359930633.png "13.png")

![14.png](https://www.cnpanda.net/usr/uploads/2024/10/879675296.png "14.png")

图 15、图 16 是在 forward 目的路由可控时绕过鉴权的一种代码写法

![15.png](https://www.cnpanda.net/usr/uploads/2024/10/937159999.png "15.png")

![16.png](https://www.cnpanda.net/usr/uploads/2024/10/2516046324.png "16.png")

图 17 、图 18 是先知师傅整理的 shiro 的鉴权绕过相关的 tips

![17.png](https://www.cnpanda.net/usr/uploads/2024/10/2511956961.png "17.png")

![18.png](https://www.cnpanda.net/usr/uploads/2024/10/3941198203.png "18.png")

图 19 是项目使用了 jwt 鉴权的一些思路

![19.png](https://www.cnpanda.net/usr/uploads/2024/10/599781618.png "19.png")

图 20 是 fuzz 鉴权绕过的一些方法思路

![20.png](https://www.cnpanda.net/usr/uploads/2024/10/1058706301.png "20.png")

#####

「感谢老板送来的软糖/蛋糕/布丁/牛奶/冰阔乐！」

赞赏

×

![](https://www.cnpanda.net/tx.png)panda

(๑＞ڡ＜)☆谢谢老板~

2元
5元
10元
50元
100元
任意金额

2元

使用微信扫描二维码打赏

![](https://www.cnpanda.net/usr/themes/7TEC/img/alipay-2.jpg)

![](https://www.cnpanda.net/usr/themes/7TEC/img/alipay-btn.png)

![](https://www.cnpanda.net/usr/themes/7TEC/img/wechat-btn.png)

版权属于：

Panda | 热爱安全的理想少年

本文链接：

https://www.cnpanda.net/talksafe/1277.html（转载时请注明本文出处及文章链接）

作品采用：

《[署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)](//creativecommons.org/licenses/by-nc-sa/4.0/deed.zh)》许可协议授权

* [技术杂谈](https://www.cnpanda.net/category/talksafe/)
* 2024-10-28
* [评论](https://www.cnpanda.net/talksafe/1277.html#comments)
* 2321 字
* 2182 次浏览

[Mybatis 从SQL注入到OGNL注入](https://www.cnpanda.net/sec/1227.html "Mybatis 从SQL注入到OGNL注入")
1/1
[ByteCTF Guess Cookie 出题思路详解](https://www.cnpanda.net/ctf/1301.html "ByteCTF Guess Cookie 出题思路详解")

### 暂时无法评论哦~

暂无评论

![](/tx.png)

**panda**

---

喜爱程序分析以及研究一些有趣的 Web 安全问题

#####

##### 文章分类[共 76 篇] [[归档](https://www.cnpanda.net/archives.html)]

* [安全研究 (24)](https://www.cnpanda.net/category/sec/)
* [代码审计 (17)](https://www.cnpanda.net/category/codeaudit/)
* [技术杂谈 (12)](https://www.cnpanda.net/category/talksafe/)
* [CTF (10)](https://www.cnpanda.net/category/ctf/)
* [编程算法 (1)](https://www.cnpanda.net/category/program/)
* [理论研究 (3)](https://www.cnpanda.net/category/sci/)
* [生活 (8)](https://www.cnpanda.net/category/life/)

##### 热门文章

* [个人经验泛谈之工控安全入门](https://www.cnpanda.net/sec/592.html "个人经验泛谈之工控安全入门") 111,464 人看过
* [第十届信息安全国赛 Web WriteUp（部分）](https://www.cnpanda.net/ctf/81.html "第十届信息安全国赛 Web WriteUp（部分）") 45,673 人看过
* [fastadmin最新版前台getshell漏洞分析](https://www.cnpanda.net/codeaudit/777.html "fastadmin最新版前台getshell漏洞分析") 37,101 人看过
* [【Java 代码审计入门-01】审计前的准备](https://www.cnpanda.net/codeaudit/588.html "【Java 代码审计入门-01】审计前的准备") 26,173 人看过
* [maccms v8 80w 字符的 RCE 分析](https://www.cnpanda.net/codeaudit/660.html " maccms v8 80w 字符的 RCE 分析") 23,964 人看过
* [【Java 代码审计入门-04】SSRF 漏洞原理与实际案例介绍](https://www.cnpanda.net/codeaudit/678.html "【Java 代码审计入门-04】SSRF 漏洞原理与实际案例介绍") 22,436 人看过
* [带你走进 S7COMM 与 MODBUS 工控协议](https://www.cnpanda.net/sec/578.html "带你走进 S7COMM 与 MODBUS 工控协议") 22,230 人看过
* [T-Star高校挑战赛WP](https://www.cnpanda.net/ctf/731.html "T-Star高校挑战赛WP") 21,871 人看过
* [挖洞神器之XRAY使用初体验](https://www.cnpanda.net/talksafe/657.html "挖洞神器之XRAY使用初体验 ")  20,856 人看过
* [【Java 代码审计入门-05】RCE 漏洞原理与实际案例介绍](https://www.cnpanda.net/codeaudit/759.html "【Java 代码审计入门-05】RCE 漏洞原理与实际案例介绍") 20,237 人看过

##### 标签

[ByteCTF](https://www.cnpanda.net/tag/ByteCTF/ "1 个话题")
[年度总结](https://www.cnpanda.net/tag/%E5%B9%B4%E5%BA%A6%E6%80%BB%E7%BB%93/ "2 个话题")
[logback](https://www.cnpanda.net/tag/logback/ "2 个话题")
[log4j](https://www.cnpanda.net/tag/log4j/ "2 个话题")
[log4j2](https://www.cnpanda.net/tag/log4j2/ "3 个话题")
[jn'di](https://www.cnpanda.net/tag/jn-di/ "1 个话题")
[Thymeleaf Bypass](https://www.cnpanda.net/tag/Thymeleaf-Bypass/ "1 个话题")
[Thymeleaf](https://www.cnpanda.net/tag/Thymeleaf/ "1 个话题")
[SSTI](https://www.cnpanda.net/tag/SSTI/ "1 个话题")
[java 代码审计入门](https://www.cnpanda.net/tag/java-%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1%E5%85%A5%E9%97%A8/ "1 个话题")
[JDK8u20](https://www.cnpanda.net/tag/JDK8u20/ "1 个话题")
[JEP290](https://www.cnpanda.net/tag/JEP290/ "1 个话题")
[Java序列化](https://www.cnpanda.net/tag/Java%E5%BA%8F%E5%88%97%E5%8C%96/ "1 个话题")
[java 序列化](https://www.cnpanda.net/tag/java-%E5%BA%8F%E5%88%97%E5%8C%96/ "2 个话题")
[序列化](https://www.cnpanda.net/tag/%E5%BA%8F%E5%88%97%E5%8C%96/ "3 个话题")
[gadget](https://www.cnpanda.net/tag/gadget/ "1 个话题")
[JDK7U21](https://www.cnpanda.net/tag/JDK7U21/ "1 个话题")
[JDK](https://www.cnpanda.net/tag/JDK/ "2 个话题")
[反序列化](https://www.cnpanda.net/tag/%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/ "2 个话题")
[java 反序列化](https://www.cnpanda.net/tag/java-%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96/ "4 个话题")
[微擎](https://www.cnpanda.net/tag/%E5%BE%AE%E6%93%8E/ "1 个话题")
[内卷](https://www.cnpanda.net/tag/%E5%86%85%E5%8D%B7/ "1 个话题")
[面试](https://www.cnpanda.net/tag/%E9%9D%A2%E8%AF%95/ "1 个话题")
[生活](https://www.cnpanda.net/tag/%E7%94%9F%E6%B4%BB/ "1 个话题")
[读研](https://www.cnpanda.net/tag/%E8%AF%BB%E7%A0%94/ "1 个话题")
[蚂蚁金服](https://www.cnpanda.net/tag/%E8%9A%82%E8%9A%81%E9%87%91%E6%9C%8D/ "1 个话题")
[非攻实验室](https://www.cnpanda.net/tag/%E9%9D%9E%E6%94%BB%E5%AE%9E%E9%AA%8C%E5%AE%A4/ "1 个话题")
[远程代码执行](https://www.cnpanda.net/tag/%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/ "1 个话题")
[骑士 CMS](https://www.cnpanda.net/tag/%E9%AA%91%E5%A3%AB-CMS/ "1 个话题")
[74cms](https://www.cnpanda.net/tag/74cms/ "1 个话题")

##### 订阅

* [RSS](https://www.cnpanda.net/feed/)

*[皖ICP备16023761号-1](https://beian.miit.gov.cn/)
© 2025 [Panda | 热爱安全的理想少年](https://www.cnpanda.net/).

站点已稳定运行：*