---
title: 【技术原创】ADAudit Plus利用分析——数据加密分析
url: https://www.4hou.com/posts/MKQB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-08-19
fetch_date: 2025-10-04T11:59:25.820605
---

# 【技术原创】ADAudit Plus利用分析——数据加密分析

【技术原创】ADAudit Plus利用分析——数据加密分析 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】ADAudit Plus利用分析——数据加密分析

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-08-18 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)118634

收藏

导语：本文分析了ADAudit Plus数据加密的算法，区分域用户，编写实现代码，后续根据算法可以用来对用户口令进行暴破。

**0x00 前言**

在上篇文章[《ADAudit Plus漏洞调试环境搭建》](https://www.4hou.com/posts/L18W "https://www.4hou.com/posts/L18W")介绍了漏洞调试环境的搭建细节，经测试发现数据库的部分数据做了加密，本文将要介绍数据加密的相关算法。

**0x01 简介**

本文将要介绍以下内容：

数据加密的位置

算法分析

算法实现

**0x02 数据加密的位置**

测试环境同《ADAudit Plus漏洞调试环境搭建》保持一致

数据库连接的完整命令："C:\Program Files\ManageEngine\ADAudit Plus\pgsql\bin\psql" "host=127.0.0.1 port=33307 dbname=adap user=postgres password=Stonebraker"

查询加密口令的命令示例：SELECT \* FROM public.aaapassword ORDER BY password\_id ASC;

返回结果示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414253492031.png "1682413595157629.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414259137867.png "1682413625168896.png")

点击Add technicians可以添加用户，这里可以选择添加自定义用户或者域用户

添加自定义用户需要输入口令，如下图

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414260895625.png "1682413668797870.png")添加域用户不需要输入域用户的口令，如下图

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414261393894.png "1682413702935318.png")

**0x03 算法分析**

**1.加密算法细节**

经分析，加密算法细节位于C:\Program Files\ManageEngine\ADAudit Plus\lib\AdvAuthentication.jar中的com.adventnet.authentication.util->AuthUtil.class

添加用户的实现代码：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414262134072.png "1682413853108687.png")![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414264488159.png "1682413863841274.png")![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414265915349.png "1682413873949783.png")![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414266189745.png "1682413882667760.png")![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414267131850.png "1682413892297673.png")![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414268208627.png "1682413902113515.png")![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414269296928.png "1682413912784743.png")得到加密生成Password的代码：

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414270185609.png "1682413955115369.png")生成salt的代码：

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414270108618.png "1682413979128425.png")经动态调试，发现workload默认为12，生成的salt格式示例：$2a$12$DVT1iwOoi3YwkHO6L6QSoe，如下图

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414271168004.png "1682414010835536.png")具体加密算法getEncryptedPassword()的实现细节：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414273154658.png "1682414066421460.png")![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414273182553.png "1682414091204949.png")

在此处下断点，经动态调试得出以下结论：

如果是域用户，会使用默认口令admin作为明文，随机生成salt，算法使用bcrypt，通过固定算法计算得出密文，密文前29字节对应加密使用的salt

如果不是域用户，会使用用户口令作为明文去计算，例如默认用户admin，会使用实际的口令作为明文去加密得到密文

也就是说，在查询表public.aaapassword时，我们只需要取出password项前29字节作为加密使用的salt，不需要关注表public.aaapassword中的salt项

**2.区分是否为域用户**

查询命令示例：SELECT \* FROM public.aaalogin ORDER BY login\_id ASC;

返回结果示例：

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414274156096.png "1682414128157636.png")

其中，domainname为ADAuditPlus Authentication代表自定义添加的用户

这里使用inner join查询自动筛选出非域用户和对应的hash，命令示例：SELECT aaalogin.login\_id,aaalogin.name,aaalogin.domainname,aaapassword.password FROM public.aaalogin as aaalogin INNER JOIN public.aaapassword AS aaapassword on aaalogin.login\_id=aaapassword.password\_id WHERE aaalogin.domainname = 'ADAuditPlus Authentication';

返回结果示例：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414275962762.png "1682414162120695.png")

**0x04 算法实现**

测试参数如下：

已知明文为123456

查询数据库得到的password项为$2a$12$1hKeH4aM2LY4BvYpKT9Z5.p9cD453FjBAPYjp0ek94n936WRRAYme

从中可知salt为password项的前29字节，即$2a$12$1hKeH4aM2LY4BvYpKT9Z5.

计算密文的测试代码如下：

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414276838799.png "1682414229696325.png")![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230425/1682414277305842.png "1682414241131924.png")

计算结果为$2a$12$1hKeH4aM2LY4BvYpKT9Z5.p9cD453FjBAPYjp0ek94n936WRRAYme，同数据库得到的password项一致

综上，根据以上算法可以用来对用户口令进行暴破

**0x05 小结**

本文分析了ADAudit Plus数据加密的算法，区分域用户，编写实现代码，后续根据算法可以用来对用户口令进行暴破。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?6wbFx6tn)

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

![](https://img.4hou.com/wp-content/uploads/2017/06/83af13989dee96c0471f.jpg)

# [3gstudent](https://www.4hou.com/member/bmZO)

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

[查看更多](https://www.4hou.com/member/bmZO)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/60694238...