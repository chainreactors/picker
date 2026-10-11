---
title: 传统BOT防护不够用？意图分析才是未来
url: https://blog.nsfocus.net/%e4%bc%a0%e7%bb%9fbot%e9%98%b2%e6%8a%a4%e4%b8%8d%e5%a4%9f%e7%94%a8%ef%bc%9f%e6%84%8f%e5%9b%be%e5%88%86%e6%9e%90%e6%89%8d%e6%98%af%e6%9c%aa%e6%9d%a5/
source: 绿盟科技技术博客
date: 2026-10-10
fetch_date: 2026-10-11T08:02:39.929587
---

# 传统BOT防护不够用？意图分析才是未来

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)
* [登录](https://blog.nsfocus.net/wp-login.php)

* [首页](https://blog.nsfocus.net)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* 传统BOT防护不够用？意图分析才是未来

# 传统BOT防护不够用？意图分析才是未来

[0](https://blog.nsfocus.net/%E4%BC%A0%E7%BB%9Fbot%E9%98%B2%E6%8A%A4%E4%B8%8D%E5%A4%9F%E7%94%A8%EF%BC%9F%E6%84%8F%E5%9B%BE%E5%88%86%E6%9E%90%E6%89%8D%E6%98%AF%E6%9C%AA%E6%9D%A5/#comments)

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=40&d=identicon&r=g) [NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/ "written 2026-10-1016:13") 发布于 24 小时前

![](https://blog.nsfocus.net/wp-content/uploads/2026/10/封面of-2ed.jpg)

阅读： 46

### 一、超一半流量不是真人

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/70407d0dcf1c400eb243424125b7387b~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261010161119FF2D4ABCFA62C48FA281&x-expires=2147483647&x-signature=xk6ZOwzCIKRxQwAdrhm1IbQmEIQ%3D)

全球互联网流量监测和分析平台Cloudflare Radar统计：2026年，BOT占全球HTML内容HTTP请求达57.5%；过去一年内，AI Agent日请求量同比增长超1700%。

您的WEB业务“访客”里，超过一半不是真人。自动化流量威胁越发严重，有扫描器四处刺探漏洞，爬虫批量抓取商品价格和文章内容，抢票脚本在开售瞬间把票一抢而空。AI工具普及之后，这类自动访问还在飞速增长。

根据DataDome统计，全网能把10类机器人流量全部拦住的网站，只占2.4%。仅靠“封IP地址、写固定规则”的老办法，已经越来越力不从心。并非BOT防护规则写得不够多，而是对抗方式从根上落后了。

### 二、老办法为什么不灵了？

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/77514704aab346fe88203c186d788c62~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261010161119FF2D4ABCFA62C48FA281&x-expires=2147483647&x-signature=6w6qbBjVOgUBHvq8WE9KbQUpR1E%3D)

* **第一，分不清“谁是谁”。**传统BOT防护难以精准认出访客身份，尤其是NAT“一址多人”场景。公司、学校、手机网络的大量用户往往共用少数几个出口IP。封掉这个IP，几百个正常用户跟着受影响；不封，恶意BOT又藏在里面，误伤与漏防很难两全。

* **第二，伪装太容易。**单一线索通常不足以给BOT“定罪”，需要多条证据互相印证；而线索组合的复杂程度，早已超出人工应付的范围。

* **第三，看不透“在干什么”。**传统BOT防护缺少业务视角，无法判断BOT摸的是公开信息还是核心资产。规则配松了拦不住，配紧了又容易误伤正常用户。

* **第四，需要改造业务，运维烦琐。**传统BOT防护通过JS挑战，由网页下发挑战代码让浏览器执行，能答出才放行。这种方式需在页面注入JS并改造客户端，接入与验证周期长，交付较重；与前端页面深度耦合，业务改版需同步回归，维护成本高；并且依赖浏览器 JS 环境，对 APP、小程序、纯 API 调用兼容性差；JS 可被逆向与模拟，对抗随混淆强度持续升级，容易失效。

### 三、意图分析：不看“你是谁”，先看“你想干什么”

![](https://p11-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/0b5e15d985004c20b633b924cd6e37d8~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261010161119FF2D4ABCFA62C48FA281&x-expires=2147483647&x-signature=tdRNN5QVVEPDsQnF6b%2BuD2D3jJU%3D)

**绿盟Web应用防护系统（WAF）**融合BOT意图分析引擎，通过身份情报和行为指纹精准识别恶意自动化攻击。这种方式不打扰任何访客，只在旁边默默观察真实流量，从访问者身份、所用工具特征、访问业务方式三个方面画出“行为画像”，靠统计分析判断它到底想干什么。

基于意图分析的BOT防护有四个明显优势：

* **1）接入轻。**以旁路方式接入，不用改动一行网页代码，不影响现有业务，接入即可开始分析，业务方几乎毫无感知。

* **2）不耦合。**防护不依赖网页结构，网站改版、前端升级、接口调整，通常都不会让防护策略失效，安全团队不用跟着业务版本反复测试。

* **3）管得全。**Web网页、手机App、小程序、接口调用全覆盖，一套策略管住所有入口——而App、小程序和接口这些“没有浏览器”的地方，恰恰是BOT最活跃的区域。

* **4）越用越聪明。**行为画像在长期运营中持续积累，BOT为完成任务很难完全隐藏这些规律；运营越久，画像越清晰。

### **四、从“被动封堵”到“主动管理”**

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/88ed4ee3facd4dbcb6ca5244e7f0fe2f~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261010161119FF2D4ABCFA62C48FA281&x-expires=2147483647&x-signature=aRooQSimHOfakE6q%2B%2B1f%2BaQJ4So%3D)

意图分析带来的不只是多几条规则，更是整套防护方式的升级。

* **系统自己出情报。**绿盟WAF以Session、UserID、Token、IP为粒度，按请求量、资源构成、状态码、URL广度、访问节奏等5大维度、12项指标聚合统计，像信用评分一样给每个访客打分。内置7种意图标签：恶意扫描、数据爬取、API滥用、暴力破解、AI BOT、搜索引擎、恶意抢占。各项得分累计达到阈值才判定可疑，标签开箱即用，也支持调参与自定义。

* 身份识别同样自动完成，从IP、Session、UserID到Token四层逐级细化，给出0到100的可信度评分，人工确认后才生效。BOT换IP、换代理，也甩不掉行为上的痕迹。

* **运营形成闭环。**高频BOT几分钟内就能发现，低频潜伏的则靠小时级、天级的分析兜底；判定类型后，身份、工具特征、业务对象一键沉淀为可复用的情报。处置手段有7种：放行、限流、验证码、JS挑战、重定向、伪装、阻断。善意的搜索引擎直接放行，可疑行为先观察留证，确认是威胁再阻断，分级应对而不是“一刀切”。

* **业务对象自动归类。**几十万个具体网址会被自动归并成几百个模板，比如/user/123/abc归并为/user/｛数字｝/abc，通过手动标注登录、抢购、查询等业务场景。配合460多条内置工具特征——覆盖主流扫描器、爬虫框架、无头浏览器和搜索引擎，按恶意、可疑、善意三级分类——多重证据交叉验证，有助于降低误报和漏报。

### 五、三个常见疑问

**会不会误杀正常用户？**

绿盟WAF有打分制、观察期、白名单三道防线。以“恶意扫描”为例，可设定70分阈值，单条可疑行为不处罚，多条证据累计达标才触发；触发后也不立即拦截，先进观察期留证，人工研判后再处理。白名单优先级最高，定时监控这类正常自动化行为一旦误报，一键放行即可。

**JS挑战是不是就不用了？**

绿盟WAF以意图分析为主线，旁路接入、全端覆盖、行为画像持续积累，能够独立支撑对各类自动化流量的识别与防护。

**接入会不会很麻烦？**

绿盟WAF采用代理模式部署，BOT流量不介入业务串联处理流程。不改客户端、不动现网链路。设备发现的身份标识不会自动生效，必须用户确认后才能启用，最终决定权始终在用户手里。

### 六、下半场，比拼的是“懂流量”

![](https://p3-sign.toutiaoimg.com/tos-cn-i-6w9my0ksvp/8497c9e562954244a21bbec998ef071e~tplv-tt-shrink:640:0.image?lk3s=06827d14&traceid=20261010161119FF2D4ABCFA62C48FA281&x-expires=2147483647&x-signature=%2BxU9bCXGmuf6moLhYdBDlIp2FUA%3D)

BOT治理已从“规则对抗”进入“智能识别”阶段。上半场比拼规则数量与IP库规模，下半场比拼谁更懂流量、谁的情报更厚。对手已经用上自动化和AI，防守方也该让系统替自己读懂每一次访问。

正在选型或计划升级的企业，不妨先问自己三个问题：当前最头疼的BOT场景是什么？现有手段的误报、漏报到了什么程度？哪些核心业务最怕被爬取、被抢占？

让每一次机器访问，都被看见、被理解、被恰当对待——这是绿盟WAF的目标，也是每个线上业务在机器流量时代的必修课。

最后修改日期: 2026-10-10

### 作者

![](https://secure.gravatar.com/avatar/99bcec439a2a5078218073d2459e8069eb89b5ce5cbf840afef1c3ed7395d75c?s=96&d=identicon&r=g)

[NSFOCUS](https://blog.nsfocus.net/author/zhengfangying/)

## 最新发布

* [议程速递 | 绿盟科技集结群贤，邀您共赴驭智之约](https://blog.nsfocus.net/%E8%AE%AE%E7%A8%8B%E9%80%9F%E9%80%92-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%9B%86%E7%BB%93%E7%BE%A4%E8%B4%A4%EF%BC%8C%E9%82%80%E6%82%A8%E5%85%B1%E8%B5%B4%E9%A9%AD%E6%99%BA%E4%B9%8B%E7%BA%A6/)
* [传统BOT防护不够用？意图分析才是未来](https://blog.nsfocus.net/%E4%BC%A0%E7%BB%9Fbot%E9%98%B2%E6%8A%A4%E4%B8%8D%E5%A4%9F%E7%94%A8%EF%BC%9F%E6%84%8F%E5%9B%BE%E5%88%86%E6%9E%90%E6%89%8D%E6%98%AF%E6%9C%AA%E6%9D%A5/)
* [高频业务：一种IP网段判断重叠的算法（其四）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E5%9B%9B%EF%BC%89-2/)
* [高频业务：一种IP网段判断重叠的算法（其二）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%BA%8C%EF%BC%89-2/)
* [高频业务：一种IP网段判断重叠的算法（其三）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E4%B8%89%EF%BC%89-2/)

## 文章导航

[上一篇文章 高频业务：一种IP网段判断重叠的算法（其四）](https://blog.nsfocus.net/%E9%AB%98%E9%A2%91%E4%B8%9A%E5%8A%A1%EF%BC%9A%E4%B8%80%E7%A7%8Dip%E7%BD%91%E6%AE%B5%E5%88%A4%E6%96%AD%E9%87%8D%E5%8F%A0%E7%9A%84%E7%AE%97%E6%B3%95%EF%BC%88%E5%85%B6%E5%9B%9B%EF%BC%89-2/)

[下一篇文章 议程速递 | 绿盟科技集结群贤，邀您共赴驭智之约](https://blog.nsfocus.net/%E8%AE%AE%E7%A8%8B%E9%80%9F%E9%80%92-%E7%BB%BF%E7%9B%9F%E7%A7%91%E6%8A%80%E9%9B%86%E7%BB%93%E7%BE%A4%E8%B4%A4%EF%BC%8C%E9%82%80%E6%82%A8%E5%85%B1%E8%B5%B4%E9%A9%AD%E6%99%BA%E4%B9%8B%E7%BA%A6/)

著作权 © 2026 **[绿盟科技技术博客](https://blog.nsfocus.net/)**. 保留一切权利。 本站采用的布景主题为 [Mynote](https://terryl.in/).