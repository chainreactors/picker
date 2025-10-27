---
title: 第二届RASP挑战赛开启
url: https://mp.weixin.qq.com/s?__biz=MzIxMjEwNTc4NA==&mid=2652993127&idx=1&sn=5d801918840ad8e0e58892308ac1d567&chksm=8c9ef930bbe97026d32e6354d7919e91c181e4940d3ea72306cd61274fb55921253d4a393bc7&scene=58&subscene=0#rd
source: 阿里安全响应中心
date: 2023-02-16
fetch_date: 2025-10-04T06:46:44.149459
---

# 第二届RASP挑战赛开启

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tCS9QJPdcGfqHyv2EdMOIDickyVJ9QdapXOrY2sIYnoLuzOd1IB1E7ATgo7Dtw2ia63mztrndEewAXdGys123Yog/0?wx_fmt=jpeg)

# 第二届RASP挑战赛开启

阿里安全响应中心

RASP（Runtime Application Self-Protection）技术，通过在应用运行时检测攻击并进行应用保护，为应用提供安全防御。开发无需修改应用代码，只需在实例中安装应用防护探针，即可为应用提供强大的安全防护能力，并抵御绝大部分未知漏洞所使用的攻击手法。当应用出现可疑行为时，RASP会根据当前上下文环境识别并阻断攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGfqHyv2EdMOIDickyVJ9Qdap1apOvziaibX1Fg4lXWPqoyAewFFLOSwUNnmgNfQDtFISP3ZxQGpLn8Xg/640?wx_fmt=png)

在大型攻防演练中，RASP已广泛应用于系统的安全防御。

为了促进安全对抗技术的发展，阿里云安全于2022年2月开启了第一期RASP靶场绕过挑战赛，相关赛事得到了众多专家的支持。2月16日第二期RASP靶场挑战赛来啦，欢迎大家参与！

**活动时间：**2023年2月16日12:00 ～2月23日12:00

**活动奖励：**报告基础奖励为2000元/个有效报告，根据绕过程度会有浮动，具体见规则

**提交方式：**请在ASRC官网报名(文末点击“阅读原文”直达)并提交相关的报告，报名无需审核

**活动规则详情：**

#### **1. SQL注入**

##### **1.1 数据库版本**

Mysql  8.0.31、Oracle 11g、Psql 12-alpine

mybatis框架，三种数据库的语句均如下，

```
    <select id="selectByName" parameterType="java.lang.String" resultType="com.challenge.vulns.entity.Person">
        SELECT stuid, stuname, sex, age, birth
        FROM boy
        WHERE stuname = '${name}'
    </select>
```

##### **1.2 得分规则**

写入文件到 /usr/local/check 目录下（文件类型不限）  -获得80%奖金

读取到数据库flag表中的文件内容 -获得100%奖金

成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生成文件  -获得120%奖金

#### **2.XXE**

任意目录遍历  50%

读取到服务器上的/flag文件内容 100%

#### **3.命令执行**

包括log4j、ognl表达式注入、spel表达式注入、el表达式注入

读取到服务器上的/flag文件内容  60%

成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生成文件  100%

#### **4.反序列化**

包括ois、fastjson两个环境

读取到服务器上的/flag文件内容 60%

成功系统命令touch /usr/local/check/XXX在/usr/local/check 目录下生产文件 100%

#### **5. dependency信息**

```
<dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <exclusions><!-- 去掉默认配置 -->
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-logging</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency> <!-- 引入log4j2依赖 -->
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-log4j2</artifactId>
        </dependency>
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.3.0</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/com.alibaba/fastjson -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.24</version>
        </dependency>

        <dependency>
            <groupId>ognl</groupId>
            <artifactId>ognl</artifactId>
            <version>3.0.8</version>
        </dependency>

        <dependency>
            <groupId>commons-beanutils</groupId>
            <artifactId>commons-beanutils</artifactId>
            <version>1.9.2</version>
        </dependency>

        <!-- https://mvnrepository.com/artifact/commons-collections/commons-collections -->
        <dependency>
            <groupId>commons-collections</groupId>
            <artifactId>commons-collections</artifactId>
            <version>3.2.1</version>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.11</version>
        </dependency>
        <dependency>
            <groupId>com.oracle.database.jdbc</groupId>
            <artifactId>ojdbc8</artifactId>
            <version>19.3.0.0</version>
        </dependency>
        <dependency>
            <groupId>org.postgresql</groupId>
            <artifactId>postgresql</artifactId>
            <version>42.2.23</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
```

#### **6. 注意事项**

* 报告需至少包含利用成功的Poc、token 信息、成功证明截图三部分信息
* 可将文档内容放到语雀中（http://www.yuque.com），提交到ASRC，语雀文档分享时，请选择【需要密码访问】，也可直接在ASRC的漏洞页面编写详情内容提交。
* 禁止伪造提交，我们会核实相关内容、活动规则较为复杂，请仔细查阅
* 禁止恶意攻击靶场，相关恶意攻击行为会导致奖金被取消、IP被封禁，并可能引起云的业务拉黑关联云账号，请不要进行绕过测试之外的恶意攻击行为
* 靶场地址见ASRC活动详情页面

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

阿里安全响应中心

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tCS9QJPdcGc4qyoL5yEDEwCA3qymRyXXXWS4kTrduhg01ASfv6cwXQU0e1Td0XuJ63HMLCUrYDhaBchiawDpRxg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过