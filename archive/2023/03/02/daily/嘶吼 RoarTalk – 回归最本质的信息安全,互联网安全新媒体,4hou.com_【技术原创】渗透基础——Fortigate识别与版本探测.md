---
title: 【技术原创】渗透基础——Fortigate识别与版本探测
url: https://www.4hou.com/posts/EQnY
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-03-02
fetch_date: 2025-10-04T08:23:56.531148
---

# 【技术原创】渗透基础——Fortigate识别与版本探测

【技术原创】渗透基础——Fortigate识别与版本探测 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 【技术原创】渗透基础——Fortigate识别与版本探测

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-03-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)297700

收藏

导语：Fortigate的识别需要区分管理页面和VPN登陆页面，版本探测需要根据页面特征提取特征，根据特征匹配出精确的版本，本文将要介绍通过Python实现Fortigate识别与版本探测的方法，开源代码。

**0x00 前言**

Fortigate的识别需要区分管理页面和VPN登陆页面，版本探测需要根据页面特征提取特征，根据特征匹配出精确的版本，本文将要介绍通过Python实现Fortigate识别与版本探测的方法，开源代码。

**0x01 简介**

本文将要介绍以下内容：

实现思路

实现细节

开源代码

**0x02 实现思路**

**1.Fortigate的识别**

可通过跳转的URL进行区分

管理页面跳转的url：/login?redir=%2F

vpn登陆页面跳转的url：/remote/login?lang=en

**2.版本探测**

页面源码中存在32位的16进制字符串可以作为版本识别的特征，每个版本对应不同的32位字符串

**0x03 实现细节**

**1.Fortigate的识别**

这里的方法是直接访问IP，根据页面返回结果进行判断

(1)管理页面

在返回结果中就能获得32位的16进制字符串

(2)vpn登陆页面

返回的内容为跳转地址，需要解析出跳转地址重新构造URL并访问，在返回结果中获得32位的16进制字符串

返回跳转地址的内容示例：

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309668213845.png "1675309313152312.png")

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309668109242.png "1675309343125864.png")

注：

在判断版本时无法在requests模块中使用allow\_redirects=False参数来控制是否重定向，原因如下：

使用requests模块时，如果使用allow\_redirects=False参数，只有在返回状态码为301或302时，才会关闭重定向，这里Fortigate返回的状态码为200，所以allow\_redirects=False参数不起作用

**2.版本探测**

在实际测试过程中，不同版本的Fortigate，虽然都会返回32位16进制字符，但是格式不同，为了提高匹配的效率，减少工作量，这里在正则匹配时选择直接匹配32位的16进制字符，示例代码如下：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309669185772.png "1675309393153724.png")

在实际测试过程中，存在response.text的输出为乱码的情况

研究解决方法的过程如下：

输出response.headers，示例代码：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309670121812.png "1675309475157468.png")

返回结果：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309671182279.png "1675309515649509.png")

发现编码格式为x-gzip

所以这里可以对response.text额外做一次gzip解码，获得原始数据，代码如下：

![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309671187174.png "1675309548297258.png")完整的实现代码如下：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309673920724.png "1675309594133255.png")![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309673150637.png "1675309602259889.png")

注：

如果遇到通过浏览器访问SSL Vpn Client页面提示ERR\_SSL\_VERSION\_OR\_CIPHER\_MISMATCH的错误时，程序将返回如下结果：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230202/1675309674532697.png "1675309650188578.png")

解决方法：

改用Python2即可

**0x04 开源代码**

完整的实现代码已上传至github，地址如下：

https://github.com/3gstudent/Homework-of-Python/blob/master/Fortigate\_GetVersion.py

代码支持区分管理页面和VPN登陆页面，提供了VM版本的指纹库作为示例，代码能够从页面自动提取出指纹特征，同指纹库进行比对，识别出精确的版本。

**0x05 小结**

本文介绍了通过Python实现Fortigate识别与版本探测的方法，介绍实现细节，开源代码，作为一个很好的学习示例。

本文为 3gstudent 原创稿件，授权嘶吼独家发布，如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?uFBpfUwM)

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

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)