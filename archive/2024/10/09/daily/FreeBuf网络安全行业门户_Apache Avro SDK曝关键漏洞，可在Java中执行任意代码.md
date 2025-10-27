---
title: Apache Avro SDK曝关键漏洞，可在Java中执行任意代码
url: https://www.freebuf.com/news/412231.html
source: FreeBuf网络安全行业门户
date: 2024-10-09
fetch_date: 2025-10-06T18:53:45.197302
---

# Apache Avro SDK曝关键漏洞，可在Java中执行任意代码

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

Apache Avro SDK曝关键漏洞，可在Java中执行任意代码

* ![]()
* 关注

* [资讯](https://www.freebuf.com/news)

Apache Avro SDK曝关键漏洞，可在Java中执行任意代码

2024-10-08 10:43:02

所属地 上海

Apache Avro Java软件开发工具包（SDK）中披露了一个关键安全漏洞，如果成功利用，可以在易受攻击的实例上执行任意代码。该漏洞编号为CVE-2024-47561，影响1.11.4之前版本的所有软件。Databricks安全团队的Kostya Kortchinsky被发现并报告了这个安全缺陷。

Apache Avro与谷歌的Protocol Buffers（protobuf）类似，是一个为大规模数据处理提供语言中立的数据序列化框架的开源项目，提供紧凑、快速且高效的数据格式。它在大数据处理、分布式系统和云计算中被广泛使用。项目维护者发布公告称，“Apache Avro 1.11.3及之前版本的Java SDK中的模式解析允许恶意行为者执行任意代码，建议用户升级到1.11.4或1.12.0版本，这些版本修复了此问题。”

Avro团队进一步指出，如果应用程序允许用户提供自己的Avro模式进行解析，则该漏洞会影响任何应用程序。

“CVE-2024-47561影响Apache Avro 1.11.3及之前版本，在通过avroAvro模式反序列化接收到的输入时。处理来自威胁行为者的此类输入会导致代码执行。根据我们的威胁情报报告，没有公开的PoC，但这个漏洞存在于通过ReflectData和SpecificData指令处理包时，也可以通过Kafka利用。

## 缓解措施

### 1. 更新 Apache Avro SDK

确保您使用的是最新版本的 Apache Avro SDK来解决此漏洞。

```
xml
<!-- 示例 Maven 依赖 -->
<dependency>
<groupId>org.apache.avro</groupId>
<artifactId>avro</artifactId>
<version>1.10.2</version> <!-- 使用最新版本 -->
</dependency>
```

### 2. 验证输入数据

在反序列化任何数据之前，请根据预定义的模式对其进行验证，或使用白名单方法确保只处理预期的数据格式。

```
java
import org.apache.avro.Schema;
import org.apache.avro.file.DataFileReader;
import org.apache.avro.generic.GenericDatumReader;
import org.apache.avro.generic.GenericRecord;
import org.apache.avro.io.DatumReader;

import java.io.File;

public class AvroDeserializer {
public static void main(String[] args) throws Exception {
File file = new File("example.avro");
Schema schema = new Schema.Parser().parse(new File("schema.avsc"));

DatumReader<GenericRecord> datumReader = new GenericDatumReader<>(schema);
DataFileReader<GenericRecord> dataFileReader = new DataFileReader<>(file, datumReader);

for (GenericRecord record : dataFileReader) {
// 验证记录是否符合模式
if (isValid(record)) {
// 处理记录
} else {
throw new SecurityException("数据格式无效");
}
}
}

private static boolean isValid(GenericRecord record) {
// 在此处实现您的验证逻辑
return true;
}
}
```

### 3. 使用安全的反序列化库

考虑使用提供额外保护层以防止 RCE 攻击的安全反序列化库。例如，Jackson 库提供了 `@JsonTypeInfo` 和 `@JsonSubTypes` 等功能来控制反序列化。

### 4. 实施输入清理

在反序列化之前对输入数据进行清理，以删除潜在的恶意内容。这有助于防止执行未经授权的代码。

### 5. 监控和记录反序列化事件

实施日志记录和监控反序列化事件，以便及时发现任何可疑活动。

### 6. 使用安全扫描器

定期使用安全扫描器和工具来识别应用程序及其依赖项中的漏洞。

使用 Jackson 进行安全反序列化的示例

```
java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator;
import com.fasterxml.jackson.databind.jsontype.PolymorphicTypeValidator;

public class SecureDeserializer {
public static void main(String[] args) throws Exception {
ObjectMapper objectMapper = new ObjectMapper();
PolymorphicTypeValidator ptv = BasicPolymorphicTypeValidator.builder()
.allowIfBaseType(Object.class)
.build();
objectMapper.activateDefaultTyping(ptv, ObjectMapper.DefaultTyping.NON_FINAL);

// 安全地反序列化数据
MyObject obj = objectMapper.readValue(jsonString, MyObject.class);
}
}
```

通过遵循这些实践，可以降低使用 Apache Avro 的 Java 应用程序中远程代码执行漏洞的风险。

# 系统安全 # 数据安全

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

缓解措施

* 1. 更新 Apache Avro SDK
* 2. 验证输入数据
* 3. 使用安全的反序列化库
* 4. 实施输入清理
* 5. 监控和记录反序列化事件
* 6. 使用安全扫描器

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