---
title: 黑客利用 Ninja Forms WordPress 插件关键漏洞
url: https://hackernews.cc/archives/64053
source: HackerNews
date: 2026-04-08
fetch_date: 2026-04-09T04:30:41.324143
---

# 黑客利用 Ninja Forms WordPress 插件关键漏洞

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-wordpress-581849_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-wordpress-581849_1280.jpg)

# 黑客利用 Ninja Forms WordPress 插件关键漏洞

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-04-08](https://hackernews.cc/archives/64053 "10:38")
分类: [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
[暂无评论](https://hackernews.cc/archives/64053#respond)

* 浏览次数 169
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

**Ninja Forms文件上传高级插件存在关键漏洞，允许未经认证上传任意文件，可导致远程代码执行。**

该漏洞编号CVE-2026-0740，目前正遭攻击利用。据WordPress安全公司Defiant称，**其Wordfence防火墙过去24小时已拦截超过3600次攻击。**

Ninja Forms是一款拥有超60万次下载的流行WordPress表单构建器，让用户无需编码即可使用拖放界面创建表单。其文件上传扩展同属该套件，服务9万客户。

CVE-2026-0740漏洞严重性评分9.8（满分10分），影响Ninja Forms文件上传3.3.26及之前版本。

据Wordfence研究人员称，该缺陷源于对目标文件名文件类型/扩展名缺乏验证，**允许未经认证的攻击者上传任意文件（包括PHP脚本），还可操纵文件名实现路径遍历。**

Wordfence解释：”该函数在易受攻击版本的移动操作前，未对目标文件名进行任何文件类型或扩展名检查。这意味着不仅可上传安全文件，还可上传.php扩展名文件。由于未使用文件名清理，恶意参数还便于路径遍历，允许将文件甚至移动到网站根目录。”

“这使未经认证的攻击者能够上传任意恶意PHP代码，然后访问文件以在服务器上触发远程代码执行。”

利用的潜在后果严重，包括部署Web shell和完全接管网站。

**发现与修复**

该漏洞由安全研究员Sélim Lanouar（whattheslime）发现，于1月8日提交至Wordfence漏洞赏金计划。

验证后，Wordfence同日向供应商披露完整细节，并通过防火墙规则向客户推送临时缓解措施。

经补丁审查及2月10日的部分修复后，供应商于3月19日发布3.3.27版本的完整修复。

鉴于Wordfence每日检测到数千次利用尝试，强烈建议Ninja Forms文件上传用户优先升级至最新版本。

---

**消息来源：[bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-flaw-in-ninja-forms-wordpress-plugin/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[WordPress](https://hackernews.cc/archives/tag/wordpress)[漏洞](https://hackernews.cc/archives/tag/%E6%BC%8F%E6%B4%9E)[黑客](https://hackernews.cc/archives/tag/%E9%BB%91%E5%AE%A2)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-美国](https://hackernews.cc/wp-content/uploads/2025/10/flag-2141861_960_720-210x140.jpg)](https://hackernews.cc/archives/64067 "洛杉矶市律师系统遭入侵，敏感警局文件泄露")

##### [洛杉矶市律师系统遭入侵，敏感警局文件泄露](https://hackernews.cc/archives/64067 "洛杉矶市律师系统遭入侵，敏感警局文件泄露")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用 代码](https://hackernews.cc/wp-content/uploads/2026/01/可用-代码-210x140.jpg)](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

##### [Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光](https://hackernews.cc/archives/64066 "Apache ActiveMQ Classic 潜伏 13 年的 RCE 漏洞曝光")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-犯罪](https://hackernews.cc/wp-content/uploads/2025/08/criminal-8444883_640-1-210x140.jpg)](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

##### [OpenSSL 修复数据泄露等七处漏洞](https://hackernews.cc/archives/64065 "OpenSSL 修复数据泄露等七处漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

[![可用-AI安全](https://hackernews.cc/wp-content/uploads/2026/02/techmanic-digital-art-8420361_1920-210x140.jpg)](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

##### [Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞](https://hackernews.cc/archives/64062 "Anthropic 推出 Claude Mythos 模型，发现数千零日漏洞")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-04-09

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team