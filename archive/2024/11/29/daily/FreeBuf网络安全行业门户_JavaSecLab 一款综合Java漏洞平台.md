---
title: JavaSecLab 一款综合Java漏洞平台
url: https://www.freebuf.com/sectool/416442.html
source: FreeBuf网络安全行业门户
date: 2024-11-29
fetch_date: 2025-10-06T19:17:20.502848
---

# JavaSecLab 一款综合Java漏洞平台

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

JavaSecLab 一款综合Java漏洞平台

* ![]()
* 关注

* [工具](https://www.freebuf.com/articles/sectool)

JavaSecLab 一款综合Java漏洞平台

2024-11-28 17:30:55

所属地 广东省

## 项目介绍

JavaSecLab是**一款综合型Java漏洞平台**，提供相关漏洞缺陷代码、修复代码、漏洞场景、审计SINK点、安全编码规范，覆盖多种漏洞场景，友好用户交互UI……
![image](https://image.3001.net/images/20241128/1732785853_674836bd53c23377d9d6b.png!small)
![image](https://image.3001.net/images/20241128/1732785869_674836cdd4035c00e8328.png!small)

## 面向人群

* 安全服务方面：帮助安全服务人员理解漏洞原理(产生、修复、审计)
* 甲方安全方面：可作为开发安全培训演示，友好的交互方式，帮助研发同学更容易理解漏洞
* 安全研究方面：各种漏洞的不同触发场景，可用于xAST等安全工具测试

## 支持漏洞模块

* 跨站脚本攻击、跨站请求伪造、CORS、JSONP、URL重定向、XFF伪造、拒绝服务、XPATH注入
* SQL注入、任意文件系列、跨服务端请求伪造、XML实体注入、RCE
* 逻辑漏洞(IDOR、验证码安全、支付安全、并发安全)、敏感信息泄漏系列、登录对抗系列
* SPEL注入、SSTI注入、反序列化、组件漏洞

## 在线环境体验

<http://whgojp.top/>
账号密码：admin/admin

## 项目灵感

曾在甲方单位工作过一段时间，有机会接触到完整的**漏洞生命周期**：很多次做完渗透测试后，通过(TAPD、Jira)发送工单通知研发同学修复漏洞，经常面临着一些问题：**1、研发不知道为什么这是个漏洞？2、研发不知道这个漏洞怎么修复？**
由此，一个想法油然而生，恰巧自己也懂些开发知识，想着可不可以通过代码的方式让研发同学快速了解漏洞的产生与修复……

> 平台提供相关漏洞的安全编码规范，甲方朋友在做SDL/DevSecOps建设的时候，可以考虑加入开发安全培训这一环节

此外，自己也做过安全服务类项目，我想大部分朋友会和我一下，只是按照 信息收集->外网打点->发现漏洞->输出报告 这个流程测试，对于漏洞怎么产生、怎么修复，似乎并不关心……

代码审计过程中，通常是先定位SINK点(即代码执行或输出的关键位置)，然后再回溯寻找对应的SOURCE点(即输入或数据来源的位置)。通过将SOURCE点和SINK点串联起来，来完成代码审计工作

> 平台针对每种漏洞提供对应缺陷代码、多种安全安全修复方式(例如：1、升级修复 2、非升级修复)，同时针对代码审计，平台也提供相关漏洞的SINK点

再后来，接触了应用安全产品，SCA、SAST、DAST、RASP等，看待安全漏洞似乎又是另一种角度，对于客户来说，采购的安全工具，无论是扫源码、容器、镜像……，都希望尽可能的扫到更多的漏洞，当然也希望少点误报，笔者也或多或少接触到可达性分析等相关技术，项目中也针对每种漏洞编写了不同的触发场景，感兴趣的朋友可以测试一下……

> 平台针对同种漏洞提供多种触发场景

……

## 技术架构

SpringBoot + Spring Security + MyBatis + Thymeleaf + Layui

## 部署方式

先clone下项目代码

```
git clone https://github.com/whgojp/JavaSecLab.git
```

![image](https://image.3001.net/images/20241128/1732786088_674837a8cd9d87380a378.png!small)

### 本地部署-IDEA

> JDK环境 1.8

1. 配置数据库(**Mysql 8.0+**)
   执行 sql/JavaSecLab.sql 文件
   修改配置文件application.yml active为dev(项目默认为docker 如果搭建的过程中出现数据库连接错误 师傅们可以注意下这里)

```
spring:
  # 环境 dev|docker
  profiles:
    active: dev
```

2. 修改application-dev.yml配置文件

```
username: root
password: QWE123qwe
url: jdbc:mysql://localhost:13306/JavaSecLab?characterEncoding=utf8&zeroDateTimeBehavior=convertToNull&useSSL=false&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=GMT%2B8&nullCatalogMeansCurrent=true&allowPublicKeyRetrieval=true&allowMultiQueries=true
```

![image](https://image.3001.net/images/20241128/1732786074_6748379ae997ffb5c5948.png!small)
初始账号密码：admin/admin(后台可修改)

### Docker部署(推荐)

> 条件：已安装docker和docker-compose
>
> docker部署过程中 sql文件没有初始化执行的话(即数据库为空) 需要手动导入下sql文件

```
mvn clean package -DskipTests
docker-compose -p javaseclab up -d
```

![image](https://image.3001.net/images/20241128/1732786048_67483780e903edcab51e3.png!small)
![image](https://image.3001.net/images/20241128/1732786060_6748378c9bd86265679e3.png!small)

更多部署方案、部署问题解答详见：[部署指南](https://github.com/whgojp/JavaSecLab/wiki/%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

## 开源协议

**When we speak of free software, we are referring to freedom, not price.**

本项目遵循 [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)协议，详细的许可证内容请参见项目中的 [LICENSE](./LICENSE)文件。

## 更新记录

项目的详细更新记录请参阅 [更新日志](https://github.com/whgojp/JavaSecLab/wiki/%E6%9B%B4%E6%96%B0%E6%97%A5%E5%BF%97)

## 一些Tips

1. 安全问题：由于是漏洞靶场，因此不建议搭建在公网上使用
2. 项目中的安全修复代码仅供参考，实际业务中漏洞修复起来可能要复杂的多……
3. **问题/建议反馈：如果遇到一些项目问题或者更好的建议，欢迎各位师傅可以提Issue或加交流群进行反馈**
4. **看到这里，师傅觉得项目有用的话，麻烦动动手点个star吧，非常感谢**

# 企业安全建设 # 开发安全 # 靶场平台 # JAVA安全

免责声明

1.一般免责声明：本文所提供的技术信息仅供参考，不构成任何专业建议。读者应根据自身情况谨慎使用且应遵守《中华人民共和国网络安全法》，作者及发布平台不对因使用本文信息而导致的任何直接或间接责任或损失负责。

2. 适用性声明：文中技术内容可能不适用于所有情况或系统，在实际应用前请充分测试和评估。若因使用不当造成的任何问题，相关方不承担责任。

3. 更新声明：技术发展迅速，文章内容可能存在滞后性。读者需自行判断信息的时效性，因依据过时内容产生的后果，作者及发布平台不承担责任。

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

文章目录

项目介绍

面向人群

支持漏洞模块

在线环境体验

项目灵感

技术架构

部署方式

* 本地部署-IDEA
* Docker部署(推荐)

开源协议

更新记录

一些Tips

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)