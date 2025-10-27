---
title: 近期团队系列网站遭恶意流量攻击的声明
url: https://blog.aabyss.cn/post-176.html
source: 渊龙Sec安全团队博客
date: 2023-07-27
fetch_date: 2025-10-04T11:50:55.900299
---

# 近期团队系列网站遭恶意流量攻击的声明

# [渊龙Sec安全团队博客](https://blog.aabyss.cn/)

欢迎您访问渊龙Sec团队博客

* [首页](https://blog.aabyss.cn/)
* [安全资讯](https://blog.aabyss.cn/sort/zx)
* [网络安全](https://blog.aabyss.cn/sort/safe)
  + [渗透测试](https://blog.aabyss.cn/sort/5)
  + [漏洞复现](https://blog.aabyss.cn/sort/6)
  + [内网渗透](https://blog.aabyss.cn/sort/7)
  + [逆向破解](https://blog.aabyss.cn/sort/8)
  + [代码审计](https://blog.aabyss.cn/sort/9)
  + [社会工程学](https://blog.aabyss.cn/sort/14)
  + [极客硬件](https://blog.aabyss.cn/sort/16)
  + [CTF](https://blog.aabyss.cn/sort/17)
* [资源分享](https://blog.aabyss.cn/sort/fx)
  + [神兵利器](https://blog.aabyss.cn/sort/10)
  + [编程开发](https://blog.aabyss.cn/sort/program)
  + [网站源码](https://blog.aabyss.cn/sort/12)
  + [学习资料](https://blog.aabyss.cn/sort/13)
  + [故障排查](https://blog.aabyss.cn/sort/15)
* [黑科技](https://blog.aabyss.cn/sort/hkj)
* [登录](https://blog.aabyss.cn/admin)

* [推荐:团队官方靶场](http://ctf.aabyss.cn)
* [团队Github](https://github.com/Aabyss-Team/)
* [团队官网](https://www.aabyss.cn)
* [团队在线导航](https://dh.aabyss.cn)
* [AabyssZG](https://blog.zgsec.cn)
* [关注团队](https://dh.aabyss.cn)
  + [哔哩哔哩](https://space.bilibili.com/122627170)
  + [公开QQ群](https://jq.qq.com/?_wv=1027&k=xn0WTok1)
  + [Github项目](https://github.com/Aabyss-Team/)
  + [RSS订阅](http://blog.aabyss.cn/rss.php)

* [主页](https://blog.aabyss.cn/)
* [团队事务](https://blog.aabyss.cn/sort/18)
* 近期团队系列网站遭恶意流量攻击的声明

# 近期团队系列网站遭恶意流量攻击的声明

日期：2023-7-26
 [渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn")
 [团队事务](https://blog.aabyss.cn/sort/18)
 浏览：2949次
 评论：1条

**0# 前言**
近期（2023年7月24-25日），我们团队系列网站和曾哥个人博客受到僵尸网络的恶意流量攻击，我们及时组织技术力量抗击恶意流量，积极将该恶性事件的影响降到最低，及时保障正常用户的访问需求

**1# 事件经过**
在7月24日上午11时左右，攻击者通过北美地区众多的云服务器和代理节点，对我们团队的系列网站进行CC攻击，并且不断更换使用代理池，企图规避流量清洗和黑名单的限制，峰值达到3.18Gbps
![](https://s2.loli.net/2023/07/26/9ZRNQPXixpv2He7.png)攻击位于下午4时许结束，共攻击5个小时之久，对团队系列网站造成高达4.05TB的流量消耗
团队成员于上午12时接到阿里云的流量反馈，及时上线排查发现流量异常，我们马上进行应急操作：

* 对相关访客进行JavaScript鉴权（CC攻击无法识别js）
* 设置策略，在20秒内访问5次以上的IP自动拉入黑名单
* 限制海外地区流入国内CDN的带宽
* 打开负载均衡，做服务器的主备切换

这几种措施，大大缓解了相关流量，本身预计峰值将会达到10Gbps的恶意攻击流量后面被锁死到3.18Gbps，但同样对团队造成损失
**说明****：我们团队对源站IP（服务器真实IP）隐藏做的很好，攻击者没找到真实IP，就对团队部署的CDN进行流量攻击，这个带宽指的是是CDN承受的带宽**
![](https://s2.loli.net/2023/07/26/4QGSD6seTiURIvl.png)
本次攻击，大量消耗海外CDN流量，阿里云这边支出共1848元流量费进行防御，加上腾讯云这边的高防包，共支出两千余元

同时，我们对服务器状态进行监测，团队共4台服务器，在本轮攻击下均无宕机/死机的情况，并捕获到了部分来自国内的恶意地址：
![](https://s2.loli.net/2023/07/26/2kXDeisK9G51rzT.png)
之前并不是没有遭到过流量攻击，团队已经发展了2年左右，这两年，陆陆续续有大大小小的攻击事件的产生，但第一次碰到持续时间那么久，规模和流量这么大的事件
本次事件，团队也收获了宝贵的经验，并对此类事件的处理有了更加深刻的理解和认识

**3# 后续处理**
2023年7月25日，阿里云方面和我取得联系，我们也和他们讨论这种情况的应对方案，并对相应流量进行溯源取证
![](https://s2.loli.net/2023/07/26/zlSODTENHmJV8v6.jpg)
我们正采取各种措施及协同阿里云进行防御和溯源取证，必要时我们将采取法律措施保护我们的权益

**注：由于防御策略变更，团队网站和我的博客访问速度将受影响，等具体方案调整****（约2-3天）****后会访问速度会恢复正常，对于访客受到的影响我们在此表示抱歉**

本博客所有文章如无特别注明均为原创。作者：[渊龙Sec团队](https://blog.aabyss.cn/author/1 "为国之安全而奋斗，为信息安全而发声！ admin@aabyss.cn") ，复制或转载请以超链接形式注明转自 [渊龙Sec安全团队博客](/) 。
原文地址《近期团队系列网站遭恶意流量攻击的声明》

分享到：更多

标签: [实时资讯](https://blog.aabyss.cn/tag/%E5%AE%9E%E6%97%B6%E8%B5%84%E8%AE%AF)

### 相关推荐

* [2021补天白帽大会，我们共同前行](https://blog.aabyss.cn/post-138.html)
* [渊龙Sec安全团队公众号已开通](https://blog.aabyss.cn/post-132.html)
* [团队2021年会议总结](https://blog.aabyss.cn/post-111.html)
* [渊龙Sec安全团队博客](https://blog.aabyss.cn/post-51.html)
* [沉痛悼念江泽民同志](https://blog.aabyss.cn/post-167.html)
* [4月4日举国哀悼](https://blog.aabyss.cn/post-64.html)

### 取消回复发表评论

![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/1.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/5.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/6.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/7.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/9.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/10.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/11.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/13.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/14.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/16.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/19.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/21.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/24.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/25.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/26.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/27.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/28.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/29.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/30.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/31.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/33.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/39.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/40.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/43.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/44.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/45.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/47.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/48.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/49.png)![](https://blog.aabyss.cn/content/templates/emlog_dux/images/face/50.png)

### 网友评论**（1）**

![](http://q.qlogo.cn/headimg_dl?bs=qq&dst_uin=3571386204&src_uin=qq.feixue.me&fid=blog&spec=100)

怎样进行流量攻击的？

KKJ  2年前 (2023-11-23) [回复](#comment-17)

### AD

### 分类

* [安全资讯](http://blog.aabyss.cn/sort/zx "4 篇文章")
* [网络安全](http://blog.aabyss.cn/sort/safe "12 篇文章")
* [资源分享](http://blog.aabyss.cn/sort/fx "4 篇文章")
* [黑科技](http://blog.aabyss.cn/sort/hkj "9 篇文章")

Powered by [emlog](http://www.emlog.net "骄傲的采用emlog系统")
© 大前端优化版 By [渊龙Sec安全团队](http://www.aabyss.cn "渊龙Sec团队官网") [浙ICP备20003630号-2](https://beian.miit.gov.cn/)