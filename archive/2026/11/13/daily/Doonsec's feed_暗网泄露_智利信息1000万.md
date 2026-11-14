---
title: 暗网泄露:智利信息1000万
url: https://mp.weixin.qq.com/s/lrH8yxC-Afe-8AvJnE2hCA
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:19:26.719580
---

# 暗网泄露:智利信息1000万

# 暗网泄露:智利信息1000万

原创

暗网分析师
暗网分析师

开源情报技术研究院

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

Elasticsearch 的原始文档（\_index: "people"、\_type: "\_doc"，带 \_score: null 和 sort），也就是对某个 ES 集群做分页查询的返回结果。有人把泄露的数据集索引进自己的 Elasticsearch，再从那里往外抽。

字段映射：

字段 内容

rut 智利 RUN/RUT 身份证号，左补零至 10 位，带校验位

nombre 全名（名 + 两个姓）

fnacim 出生日期，以整数 YYYYMMDD 存储

sexo 1 = 男，0 = 女

timestamp 入库时间戳，微秒精度

出生日期存成数字而不是 ISO 日期、RUT 用零填充，这是智利旧系统被未经规范化地导进 ES 的指纹。

来源

关键线索在 timestamp：整批数据落在 2020 年 3 月 23 日 18:19:51 到 18:40:01 之间。时间戳在每页内单调递增，是典型的 \_bulk 批量顺序写入，说明整个索引是由一个脚本一次性灌进去的。两页分别是 sort 3,780,885-3,780,896 和 6,377-6,379，相隔 20 分钟持续写入，索引里至少已有 378 万个文档。

这个日期与 Control Ciudadano 对一份 1050 万条记录文件的分析完全吻合——那份文件 2025 年 12 月在论坛流出，字段一模一样（rut、nombre、fnacim、timestamp，全部集中在 2020 年 3 月的同一小时内）。该分析的结论是：

民事登记局（Registro Civil）否认了，理由是文件把字段标成 rut，而该机构用的是 run。

数据不是对某个机构的单次窃取，而是攻击医疗系统的数据聚合中间件（bonos／病假单校验类接口）得来的"弗兰肯斯坦"：注入数百万个 RUN，再收割返回的姓名、出生日期、是否属于 Fonasa 或 Isapre。

这解释了它记录在案的完整性缺陷：250 万条记录出生日期为 0，2300 条是默认值 19170101，398 人的"姓名"直接写着 Fonasa、139 人写着 Isapre，以及紧贴 RUT 后面那个没有键名的值（0/1/null），对应"能否购买医疗券"。

不过你给的这个子集很干净：重音符号正确，日期与 RUT 号段相符，没有上述那些毛病。

更早的背景：2019 年就流出过选举服务局（Servel）经无认证 Elasticsearch 暴露的整份数据，1430 万条，含 RUT 和出生日期。字段和量级都对得上，说明这份文件是那批材料被重新索引后的副本，或由它衍生。

校验：RUT 是真的

我用模 11 校验了全部 15 个校验位，15 个全部通过。不是合成数据也不是占位样本：都是带正确校验位的真实 RUN，姓名和日期与之一致。

RUT 姓名 出生日期 当时年龄（2020-03） 性别

12.355.020-K Campos Cuevas Jorge Antonio 1973-03-13 47 男

9.276.649-7 Espinoza Muñoz Victor 1962-01-22 58 男

4.221.667-4 Quiroz Muñoz Jose Ramon 1942-10-18 77 男

7.727.033-7 Campillay Alarcon Orlando 1961-01-22 59 男

10.543.140-6 Olivares Alvarez Patricio Antonio 1972-08-29 47 男

10.681.510-0 Bahamonde Araya Marcelo Victor Hugo 1972-05-20 47 男

10.456.972-2 Garces Perez Adrian Hugo 1966-04-09 53 男

11.948.339-5 Maldonado Gutierrez Ernesto Javier 1972-07-07 47 男

12.278.590-4 Diaz Delgado Maximo Cesar Hernan 1972-07-30 47 男

10.951.364-4 Montecinos Bello Marcelo Andres 1972-06-08 47 男

11.683.447-2 Marquez Salgado Eduardo 1970-10-12 49 男

11.655.877-7 Saavedra Medina Luis Alberto 1970-10-16 49 男

5.166.911-8 Mendez Iturra Elsa Zunilda 1943-11-22 76 女

16.626.162-7 Bernal Martinez Rocio Del Pilar 1987-04-05 32 女

4.250.156-5 Díaz Bruna Mirta Del Carmen 1941-07-16 78 女

样本的人口学特征

年龄跨度：2020 年时 32 至 78 岁（今天 39 至 85 岁）。全部成年，符合选民册特征。

异常集中：15 人里有 7 人出生于 1970-1972 年，其中 5 人恰好在 1972 年。三年占 47%，远高于正常的每年约 4%。样本太小不足定论，但说明这份导出没有打乱顺序。

80% 男性（12/15）。智利约为 49/51。样本这么小可能是偶然，但前 12 行全是男性、女性直到第二批才出现，值得留意。

样本：

```
{"_id":"0012355020-K","_index":"people","_score":null,"_source":{"fnacim":19730313,"nombre":"Campos Cuevas Jorge Antonio","rut":"0012355020-K","sexo":1,"timestamp":"2020-03-23T18:40:01.828885"},"_type":"_doc","sort":[3780885]} {"_id":"0009276649-7","_index":"people","_score":null,"_source":{"fnacim":19620122,"nombre":"Espinoza Muñoz Victor","rut":"0009276649-7","sexo":1,"timestamp":"2020-03-23T18:40:01.828895"},"_type":"_doc","sort":[3780886]} {"_id":"0004221667-4","_index":"people","_score":null,"_source":{"fnacim":19421018,"nombre":"Quiroz Muñoz Jose Ramon","rut":"0004221667-4","sexo":1,"timestamp":"2020-03-23T18:40:01.828908"},"_type":"_doc","sort":[3780887]} {"_id":"0007727033-7","_index":"people","_score":null,"_source":{"fnacim":19610122,"nombre":"Campillay Alarcon Orlando","rut":"0007727033-7","sexo":1,"timestamp":"2020-03-23T18:40:01.828918"},"_type":"_doc","sort":[3780888]} {"_id":"0010543140-6","_index":"people","_score":null,"_source":{"fnacim":19720829,"nombre":"Olivares Alvarez Patricio Antonio","rut":"0010543140-6","sexo":1,"timestamp":"2020-03-23T18:40:01.828929"},"_type":"_doc","sort":[3780889]} {"_id":"0010681510-0","_index":"people","_score":null,"_source":{"fnacim":19720520,"nombre":"Bahamonde Araya Marcelo Victor Hugo","rut":"0010681510-0","sexo":1,"timestamp":"2020-03-23T18:40:01.828939"},"_type":"_doc","sort":[3780890]} {"_id":"0010456972-2","_index":"people","_score":null,"_source":{"fnacim":19660409,"nombre":"Garces Perez Adrian Hugo","rut":"0010456972-2","sexo":1,"timestamp":"2020-03-23T18:40:01.828949"},"_type":"_doc","sort":[3780891]} {"_id":"0011948339-5","_index":"people","_score":null,"_source":{"fnacim":19720707,"nombre":"Maldonado Gutierrez Ernesto Javier","rut":"0011948339-5","sexo":1,"timestamp":"2020-03-23T18:40:01.828959"},"_type":"_doc","sort":[3780892]} {"_id":"0012278590-4","_index":"people","_score":null,"_source":{"fnacim":19720730,"nombre":"Diaz Delgado Maximo Cesar Hernan","rut":"0012278590-4","sexo":1,"timestamp":"2020-03-23T18:40:01.828969"},"_type":"_doc","sort":[3780893]} {"_id":"0010951364-4","_index":"people","_score":null,"_source":{"fnacim":19720608,"nombre":"Montecinos Bello Marcelo Andres","rut":"0010951364-4","sexo":1,"timestamp":"2020-03-23T18:40:01.828979"},"_type":"_doc","sort":[3780894]} {"_id":"0011683447-2","_index":"people","_score":null,"_source":{"fnacim":19701012,"nombre":"Marquez Salgado Eduardo","rut":"0011683447-2","sexo":1,"timestamp":"2020-03-23T18:40:01.828989"},"_type":"_doc","sort":[3780895]} {"_id":"0011655877-7","_index":"people","_score":null,"_source":{"fnacim":19701016,"nombre":"Saavedra Medina Luis Alberto","rut":"0011655877-7","sexo":1,"timestamp":"2020-03-23T18:40:01.828999"},"_type":"_doc","sort":[3780896]} {"_id":"0005166911-8","_index":"people","_score":null,"_source":{"fnacim":19431122,"nombre":"Mendez Iturra Elsa Zunilda","rut":"0005166911-8","sexo":0,"timestamp":"2020-03-23T18:19:51.245145"},"_type":"_doc","sort":[6377]} {"_id":"0016626162-7","_index":"people","_score":null,"_source":{"fnacim":19870405,"nombre":"Bernal Martinez Rocio Del Pilar","rut":"0016626162-7","sexo":0,"timestamp":"2020-03-23T18:19:51.245154"},"_type":"_doc","sort":[6378]} {"_id":"0004250156-5","_index":"people","_score":null,"_source":{"fnacim":19410716,"nombre":"Díaz Bruna Mirta Del Carmen","rut":"0004250156-5","sexo":0,"timestamp":"2020-03-23T18:19:51.245164"},"_type":"_doc","sort":[6379]}
```

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TEBBMzxzv79ibbJL0UiaZhowrpEOC2OQyZWpf8dPPNOxNib56qImcCo3DA2ickq5aBL0UuF0K1okVYrlS11lSwylibg/0?wx_fmt=png)

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