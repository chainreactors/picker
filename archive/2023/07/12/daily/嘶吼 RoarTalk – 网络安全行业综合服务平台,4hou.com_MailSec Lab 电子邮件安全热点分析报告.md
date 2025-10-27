---
title: MailSec Lab 电子邮件安全热点分析报告
url: https://www.4hou.com/posts/BXQQ
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-07-12
fetch_date: 2025-10-04T11:51:24.439540
---

# MailSec Lab 电子邮件安全热点分析报告

MailSec Lab 电子邮件安全热点分析报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# MailSec Lab 电子邮件安全热点分析报告

网际思安
[技术](https://www.4hou.com/category/technology)
2023-07-11 13:44:17

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)138408

收藏

导语：本周（2023年7月3日~7日），网际思安麦赛安全实验室(MailSec Lab)观察到大量新增的“薪资调整”类钓鱼邮件攻击，并做了详细的风险特征、攻击溯源等技术研究与分析，请各企事业单位及时做好相关的防护。

概要：***“薪资调整”类钓鱼邮件激增***

本周（2023年7月3日~7日），网际思安麦赛安全实验室(MailSec Lab)观察到大量新增的“薪资调整”类钓鱼邮件攻击，并做了详细的风险特征、攻击溯源等技术研究与分析，请各企事业单位及时做好相关的防护。

**热点描述：**

关于此批“薪资调整”类钓鱼邮件的典型样本邮件，如下图所示：

*图1. 关于薪资调整通知的钓鱼邮件*

![1.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986915743141.jpg "1688986667967545.jpg")

该邮件通过伪造“薪资调整”通知，诱导员工点击邮件正文中URL超链接，从而访问精心构造的钓鱼网站。当员工输入其邮箱帐号和密码后，攻击者将获得该私人账户信息，并可利用该信息成功登陆员工的私人邮件账户。

*图2. 点击超链接后访问的钓鱼网站*

![2.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986916202679.jpg "1688986702141124.jpg")

*图3. 记录帐号信息，并模拟系统繁忙*

![3.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986916137121.jpg "1688986720888311.jpg")

**专家分析：**

MailSec Lab的技术专家从源IP、URL链接、邮件头、邮件内容等方面，对此邮件的风险特征进行了详尽的技术分析。

l  **邮件头分析：X-Mailer字段**

此类风险邮件的头部包含的“X-Mailer”字段值为“Supmailer 38.1.2”。

*图4. 邮件头部X-Mailer字段展示*

![4.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986917185272.jpg "1688986735153062.jpg")

X-Mailer字段表明了攻击者通过Supmailer软件的38.1.2版本来发送钓鱼邮件。Supmailer是由一家德国公司研发的，用于批量创建和发送广告邮件的软件。该软件的官方网站是“https://int.supermailer.de/”。该文件头字段表明邮件发送者通过使用Supmailer软件群发钓鱼邮件，而非正常使用Outlook, Foxmail等邮件客户端发送邮件。

*图5. Supmailer官方网站*

![5.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986918176487.jpg "1688986746419876.jpg")

*图6. Supmailer广告邮件群发软件界面截图*

![6.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986919901470.jpg "1688986760196816.jpg")

l  **邮件头分析：源IP字段**

通过对邮件头字段的分析可知，在该钓鱼邮件到达公司之前，分别先后经过了221.235.220.134和218.70.153.165两跳IP地址。

*图7. 邮件头部源IP字段展示*

![7.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986919146954.jpg "1688986773869659.jpg")

查询覆盖全球的91个RBL数据源，检测结果如下。两个外部IP地址被列入了多达10多个的RBL黑名单。

|  |  |  |
| --- | --- | --- |
| **序列号** | **URL/IP** | **被列为黑名单的RBL名称** |
| 1 | 218.70.153.165 | Anonmails DNSBL |
| 2 | BARRACUDA |
| 3 | Sender Score Reputation Network |
| 4 | SORBS SPAM |
| 5 | Spamhaus ZEN |
| 6 | UCEPROTECTL2 |
| 7 | TRUNCATE |
| 8 | UCEPROTECTL3 |
| 9 | 221.235.220.134 | RATS NoPtr |
| 10 | Spamhaus ZEN |
| 11 | UCEPROTECTL2 |
| 12 | UCEPROTECTL3 |

l  **URL****超链接分析**

对URL链接的Whois信息进行查询。该网站于1个多月前建立（2023年5月22日），并且服务器位于香港，因此不用进行公安注册。此类新建设且未进行公安部注册的网站大概率被用于发起黑客攻击。

*图8 邮件中URL链接的Whois信息*

![8.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986920180940.jpg "1688986838571843.jpg")

对该IP进行域名反查，可得知该IP地址下共服务了42个域名，其中有近20个域名被威胁情报识别为恶意域名。由此可见，该IP下的服务器被攻击者用于批量建设钓鱼网站。

*图9. 同一个IP下有近20个恶意域名*

![9.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986921150935.jpg "1688986855141141.jpg")

并且该URL超链接的域名被知名威胁情报也列为恶意域名：

*图10. 该域名被威胁情报列为恶意域名*

*![10.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986921132871.jpg "1688986908505069.jpg")*

邮件正文中URL链接格式如下：<https://mail-al.cn/#contact@xxxxxx.com>

该URL包含了“域名”与“收件人邮件地址”两部分信息。“域名”被用于访问钓鱼网站，而“收件人邮件地址”用于告知攻击者是谁访问了钓鱼网站。因此，针对不同收件人所发送的邮件，其中的URL链接都不相同。

如果对该IP地址进行网络爬虫，可以列出该IP地址下所提供服务的所有URL。这些URL中所含的“收件人邮件地址”，即为被攻击的收件人邮件地址。

*图11. 被攻击的收件人邮件地址*

![11.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986934737472.jpg "1688986934737472.jpg")

l  **发件人分析**

通过邮件头分析可知，为了增加钓鱼邮件的可信度，攻击者从一个已被攻陷的第三方企业邮箱帐号来发送钓鱼邮件，以此躲避邮件安全设备的检测。与此同时，攻击者故意设置发件人的显示名称为“财务”来增加邮件的可信度。

尽管如此，因为邮件是从第三方企业邮箱帐号发送的，因此发件人地址是第三方企业的域名，非收件人公司的域名。如果员工仔细辨认是可以识别出问题的。

*图12. 发件人域名为第三方企业的域名*

![12.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986953151520.jpg "1688986953151520.jpg")

**总结与攻击溯源：**

经网际思安麦赛安全实验室(MailSec Lab)的分析测试，我们认为此“薪资调整”邮件为高危邮件。总结来看，其含有的风险特征包括：

ü  该文件头字段表明邮件发送者通过使用Supmailer软件群发钓鱼邮件，而非正常使用Outlook, Foxmail等邮件客户端发送邮件；

ü  该邮件的两个外部源IP地址被列入了多达10多个的RBL黑名单；

ü  邮件中所含的网站为新建设且未在公安部进行注册；

ü  该网站所在IP地址下的服务器被用于批量建设恶意网站；

ü  邮件中所含的网站被知名威胁情报也列为恶意域名；

ü  发件人地址是第三方企业的域名，非收件人公司的域名。

此邮件的完整攻击溯源图如下所示：

*图13. 攻击溯源图*

![13.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20230710/1688986980120984.jpg "1688986980120984.jpg")

**防范建议：**

钓鱼邮件是一种常见的网络诈骗手段，通过冒充合法的机构或个人，诱导受害者提供个人敏感信息、登录凭证或进行不当操作。为了保护自己免受钓鱼邮件的攻击，以下是思安麦赛安全实验室的一些建议。

1. 使用邮件安全防护设备：部署可靠且稳定的邮件安全网关、邮件安全沙箱等邮件安全防护设备；

2. 定期检查安全防护设备：确保邮件安全防护设备的策略配置正确且生效，并确保设备的防护库已升级到最新版本；

3. 使用强密码：员工的邮箱账户应使用强密码，包括字母、数字和特殊字符的组合。避免使用容易猜测的密码，同时确保定期进行更换；

4. 员工意识培训：为员工提供钓鱼邮件识别和应对的培训，教育他们如何判断和避免潜在的威胁，并定期进行钓鱼邮件演练，测试员工的安全意识；

5. 验证发件人身份：在回复或提供任何敏感信息之前，细心验证发件人的身份。确保邮件地址和发件人姓名与正式机构或公司的信息相符；

6. 鼓励员工报告可疑邮件：如果员收到可疑的钓鱼邮件，应及时将其报告给您的组织或相关机构，以帮助企业采取适当的行动保护其他员工；

7. 警惕紧急情况：钓鱼邮件常常试图制造紧急情况，以迫使受害者匆忙采取行动。要保持冷静，不要受到威胁或诱惑；

8. 防止个人和邮件信息泄露：尽量不要在公开的论坛、社交媒体或不受信任的网站上泄露个人和邮件信息。攻击者可能会利用这些信息来制作更具针对性的钓鱼邮件；

9. 定期备份数据：定期备份您的重要数据，并将备份存储在安全的地方。这样，即使您受到钓鱼邮件攻击，并造成了数据损坏的情况下，您仍然可以恢复您的数据

10. 验证财务交易：如果收到涉及财务交易的电子邮件，避免通过邮件直接响应。相反，通过银行官方网站、银行柜台、财务部同事等安全渠道来验证交易。

**麦赛安全实验室（MailSec Lab）介绍：**

北京网际思安科技有限公司麦赛邮件安全实验室（MailSec Lab）依托于网际思安过去12年积累的邮件威胁数据，汇集了一批10+工作经验的行业专家，专注于新型邮件威胁的调研，和下一代邮件安全技术的创新性研究。在过去十多年中，MailSec Lab服务于3000+家各个行业领域的典范客户，获得客户的广泛赞誉。与此同时，实验室积极与国际和国内知名信息安全厂商合作，广泛开展威胁情报互换、共同研究等合作，构建共同防御的威胁防护体系。

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Q8sVaWuu)

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

![](https://img.4hou.com/portraits/5d184b9bc3a3a51505f2857d652bdb34.png)

# [网际思安](https://www.4hou.com/member/m1Zr)

电子邮件安全专家，17+年致力于电子邮件安全威胁防护领域

#### 最新文章

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)
  2025-09-17 12:00:00
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE9)
  2025-07-28 11:41:32
* [Darka5恶意家族样本分析](https://www.4hou.com/posts/jBmR)
  2025-07-24 14:04:33
* [NimDoor加密盗窃macOS恶意软件被删除后会自动恢复](https://www.4hou.com/posts/qoEG)
  2025-07-15 12:00:00

[查看更多](https://www.4hou.com/member/m1Zr)

# 相关热文

* [新型钓鱼即服务平台VoidProxy：瞄准微软365与谷歌账户 可绕过第三方SSO防护](https://www.4hou.com/posts/om1K)

  胡金鱼
* [ArmouryLoader加载器的全面分析——典型加载器家族系列分析五](https://www.4hou.com/posts/xyE...