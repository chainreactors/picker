---
title: F5 BIG-IP DoS 漏洞升级为关键 RCE，已遭野外利用
url: https://hackernews.cc/archives/63983
source: HackerNews
date: 2026-03-31
fetch_date: 2026-04-01T04:46:19.305090
---

# F5 BIG-IP DoS 漏洞升级为关键 RCE，已遭野外利用

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用](https://hackernews.cc/wp-content/uploads/2026/01/ransomware-2320941_640-1.jpg)

# F5 BIG-IP DoS 漏洞升级为关键 RCE，已遭野外利用

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-03-31](https://hackernews.cc/archives/63983 "15:17")
分类: [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
[暂无评论](https://hackernews.cc/archives/63983#respond)

* 浏览次数 184
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

美国网络安全机构CISA周五警告称，威胁行为体正在野外利用一个关键级别的F5 BIG-IP漏洞。

该漏洞编号CVE-2025-53521（CVSS评分9.3），最初于2025年10月作为高严重性拒绝服务（DoS）问题公开披露，但上周被重新归类为远程代码执行（RCE）漏洞。

F5已更新原始公告以反映漏洞严重性，指出攻击者可在配置了访问策略的虚拟服务器上的BIG-IP APM系统上利用该漏洞。

F5指出：”该漏洞允许未经认证的攻击者执行远程代码。设备模式下的BIG-IP系统同样存在漏洞。这是数据平面问题，控制平面未暴露。”

CVE-2025-53521影响BIG-IP APM版本17.5.0-17.5.1、17.1.0-17.1.2、16.1.0-16.1.6及15.1.0-15.1.10，已在17.5.1.3、17.1.3、16.1.6.1和15.1.10.8版本中修复。

F5在公告中表示：**“我们已获悉该漏洞在易受攻击的BIG-IP版本中遭利用。原始CVE修复方案经验证可解决修复版本中的RCE问题。”**

周五，CISA将该CVE加入已知被利用漏洞（KEV）目录，敦促联邦机构在三日内完成修补。

同时，F5发布了针对易受攻击BIG-IP系统的恶意活动相关入侵指标（IOC），包括：存在恶意文件、文件哈希不匹配、文件大小或时间戳不匹配，以及不同版本和工程热修复（EHF）版本间的文件大小和时间戳差异。

特定日志条目和命令输出，以及包含CSS内容类型和HTTP 201响应代码的出站HTTP/S流量，也表明系统已成功遭入侵。

建议各类组织立即应用CVE-2025-53521修复补丁，并优先处理CISA KEV列表中的所有漏洞缓解措施。

---

**消息来源：[securityweek.com](https://www.securityweek.com/f5-big-ip-dos-flaw-upgraded-to-critical-rce-now-exploited-in-the-wild/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[BIG-IP](https://hackernews.cc/archives/tag/big-ip)[F5](https://hackernews.cc/archives/tag/f5)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用](https://hackernews.cc/wp-content/uploads/2024/12/hacker-8003394_1280-210x140.jpg)](https://hackernews.cc/archives/61130 "复杂国家级行为者入侵 F5 系统，窃取 BIG-IP 源代码及未公开漏洞数据")

##### [复杂国家级行为者入侵 F5 系统，窃取 BIG-IP 源代码及未公开漏...](https://hackernews.cc/archives/61130 "复杂国家级行为者入侵 F5 系统，窃取 BIG-IP 源代码及未公开漏洞数据")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2025-10-16

[![可用](https://hackernews.cc/wp-content/uploads/2022/07/微信图片_20220704165039-210x140.jpg)](https://hackernews.cc/archives/42476 "F5 修复了产品中 2 个严重的远程代码执行漏洞")

##### [F5 修复了产品中 2 个严重的远程代码执行漏洞](https://hackernews.cc/archives/42476 "F5 修复了产品中 2 个严重的远程代码执行漏洞")

[Shirley](https://hackernews.cc/archives/author/shirley "Shirley") - 2022-11-17

[![Checkbox](https://hackernews.cc/wp-content/uploads/2017/02/istock-472227510-e1652249023573-210x140.jpg)](https://hackernews.cc/archives/38589 "黑客正积极利用 BIG-IP 设备漏洞 配置错误引发危险等级 9.8 安全隐患")

##### [黑客正积极利用 BIG-IP 设备漏洞 配置错误引发危险等级 9.8 安...](https://hackernews.cc/archives/38589 "黑客正积极利用 BIG-IP 设备漏洞 配置错误引发危险等级 9.8 安全隐患")

[内容转载](https://hackernews.cc/archives/author/reprint "内容转载") - 2022-05-11

[![微信图片_20220505163508](https://hackernews.cc/wp-content/uploads/2022/05/微信图片_20220505163508-e1651739953322-210x140.png)](https://hackernews.cc/archives/38460 "设备接管风险警告！F5 发现一个关键 BIG-IP 远程执行漏洞")

##### [设备接管风险警告！F5 发现一个关键 BIG-IP 远程执行漏洞](https://hackernews.cc/archives/38460 "设备接管风险警告！F5 发现一个关键 BIG-IP 远程执行漏洞")

[内容转载](https://hackernews.cc/archives/author/reprint "内容转载") - 2022-05-05

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team