---
title: Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿
url: https://www.4hou.com/posts/zlZy
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-01-10
fetch_date: 2025-10-04T03:23:57.943348
---

# Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿

Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# Automated Libra通过CAPTCHA绕过自动创建GitHub账号，进行加密货币挖矿

ang010ela
[技术](https://www.4hou.com/category/technology)
2023-01-09 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)116937

收藏

导语：​Automated Libra黑客组织通过CAPTCHA绕过技术自动账号创建，进行加密货币挖矿。

Automated Libra黑客组织通过CAPTCHA绕过技术自动账号创建，进行加密货币挖矿。

近期，南非黑客组织'Automated Libra'通过CAPTCHA绕过技术实现自动账号创建，在云平台创建账户，利用免费的资源进行加密货币挖矿来获利。

Automated Libra是位于南非的黑客组织，也是freejacking攻击活动PurpleUrchin背后的黑客组织。Freejacking 是使用免费云资源来执行加密货币挖矿活动的过程。Unit 42 研究人员分析了Automated Libra的250GB数据，发现了黑客的基础设施、历史和使用的技术。黑客使用简单的图像分析技术绕过CAPTCHA图像，实现云平台自动化账号创建，每分钟可以成功创建3-5个GitHub账户。Unit 42研究人员成功发现了黑客在PurpleUrchin攻击活动中使用的40个加密货币钱包和7种不同的加密货币。

**利用GitHub工作流进行加密货币挖矿**

Automated Libra在针对GitHub的攻击活动中融合了Play and Run以及freejacking技术。此外，攻击者还利用了GitHub CAPTCHA检查的弱点。

攻击者以平均每分钟3-5个的速度自动创建GitHub账号。创建GitHub账号后，就开始了freejacking攻击活动。

攻击者在不同的VPS（virtual private server）提供商和云服务提供商平台上创建了超过13万个账户，但是并没有付费。这些创建的账户使用的都是虚假的个人信息以及信用卡信息。这使得攻击者可以在完成加密货币挖矿活动后并未完成付费。

**自动化账号创建**

创建GitHub账户的第一步是输入邮件地址、密码和用户名，如图1所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158484425789.png "1673158143110507.png")

容器运行虚拟网络计算（VNC）服务器：使用如下命令启动Iron浏览器：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158485138586.png "1673158182695519.png")

图 2. VNC服务器展示Iron浏览器

然后使用xdotool工具，该工具是完成GitHub表单的主要脚本。表单完成后，GitHub会提示CAPTCHA：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158486115366.png "1673158208326670.png")

图 3. GitHub CAPTCHA

攻击者使用了一个非常简单的机制来解决CAPTCHA问题。从攻击者创建的GitHub账户统计数据来看，攻击者实现CAPTCHA绕过的方法非常有效。

**利用CAPTCHA的弱点**

为绕过CAPTCHA需要识别图片背景中的星系，攻击者使用了ImageMagick工具套件中的2个工具：convert 和 identify。

首先，使用convert工具将图像转化为RGB格式。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158488161238.png "1673158235104723.png")

图 4将图像转化为RBG

转化完成后，使用identify命令来提取red 通道的skewness 特征：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158489185126.png "1673158264343071.png")

图 5. 提取red 通道的skewness 特征的命令

最终的结果如图6所示，以从大到小的顺序排序。值最小的图像就是背景图片，比如：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158490274593.png "1673158278486341.png")

图 6. 每个图片的red通道输出

图4中的image 2就是识别出的星系背景图片。CAPTCHA解决后，GitHub需要一个启动码，如图7所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158490167501.png "1673158298689417.png")

图 7. GitHub 请求启动码

攻击者使用Gmail账号来自动获取启动码。这一过程使用了IMAP协议和PHP脚本来读取收到的IMAP消息。

启动码输入后，自动化过程就可以生成个人访问token。GitHub注册过程的最终结果是一个用户名和GitHub部署的个人访问token。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158497207692.png "1673158385435894.png")

图 8. 调用运行的容器

随后，容器执行以下操作：

设置SSH 密钥；

使用GitHub API创建GitHub库；

配置创建的库的权限。

此外，攻击者还使用基于MD5哈希值的随机名来对库进行命名。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158498113378.png "1673158408303262.png")

图 9. 对库进行随机命名的命令

GitHub库创建完成后，攻击者调用一个bash脚本来用目标工作流来更新库。工作流是用PHP脚本生成的， PHP模板编码的工作流示例如图10所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158505708123.png "1673158435156101.png")

图 10. PHP模板

研究人员发现其中的一个工作流中有64个任务。生成的工作流配置为github.event.client\_payload.app事件下的repository\_dispatch运行。工作流机制允许攻击者执行外部应用。在本例，攻击者运行外部bash脚本和容器，如图11所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158506135867.png "1673158459777383.png")

图 11. 执行外部应用的工作流机制

工作流运行的bash脚本是从外部域名访问的。攻击者运行的容器是用来安装和初始化加密货币挖矿功能的，如图12所示：

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158483106900.png "1673158483106900.png")

图 12. 加密货币挖矿容器

生成的工作流运行64个任务，每个任务都从5个可用的唯一配置中随机选择一个。

经过确认的攻击者创建的GitHub账户数如下图所示。

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230108/1673158510113185.png "1673158510113185.png")

图 13. PurpleUrchin攻击者创建的GitHub账户数

此外，攻击者还在Heroku、Togglebox、GitHub等不同云平台服务商创建了超过13万用户账户。

本文翻译自：https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?YDN5Yknn)

#### 你可能感兴趣的

* [![]()

  新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
* [![]()

  ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
* [![]()

  Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
* [![]()

  NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
* [![]()

  前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)
* [![]()

  攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

![](https://img.4hou.com/wp-content/uploads/2017/11/1b9b2c77b008ed64b865.gif)

# [ang010ela](https://www.4hou.com/member/e7OO)

这个家伙很懒,什么也没说!

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/e7OO)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)

  安天
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)

  企业资讯
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)

  胡金鱼
* [前瞻对抗｜这大概是首次，AI挖出了Linux内核可利用0day](https://www.4hou.com/posts/6MAV)

  企业资讯
* [攻防速写｜一条微信消息，实现客户端持久化攻击](https://www.4hou.com/posts/5MzK)

  企业资讯

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)