---
title: 暗网数据泄露情报精选周报（2026.11.07-2026.11.13）
url: https://mp.weixin.qq.com/s/5lsMVlYtHft0loJHkSWTcQ
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:17:32.257709
---

# 暗网数据泄露情报精选周报（2026.11.07-2026.11.13）

# 暗网数据泄露情报精选周报（2026.11.07-2026.11.13）

原创

第59号
第59号

第59号

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**本周情报概述**

本周在暗网论坛共监测到 163 条新建主题；按数据泄露属性、类别与地域合规要求筛选，并对相同组织、站点和重复转载去重后，纳入统计 113 起数据泄露事件。事件覆盖政府与公共服务、教育培训、医疗健康、银行与支付、保险、电商零售、招聘、SaaS 与云数据库、加密货币、制造业与能源、国防军工、酒店旅游及物流运输等行业。从地域看，涉及美国、法国、俄罗斯、印度、韩国、厄瓜多尔、墨西哥、巴西、阿根廷、智利、多米尼加、洪都拉斯、玻利维亚、秘鲁、越南、土耳其、新加坡、卡塔尔、几内亚、比利时、乌克兰、意大利、加拿大、英国、印度尼西亚、孟加拉国、肯尼亚、克罗地亚等 20 余个国家和地区。本周体量较大的案例包括：帖子宣称包含 1.97 亿条记录、覆盖 970 余家企业与平台的数据合集；LimeLeads 4,000 万条；QNB 2,500 万客户及 2.8 万员工；阿根廷 RENAPER 约 1,900 万人；法国 Mutuelle des Motards 1,311 万条；Gemini.com 1,211 万条；智利公民 1,000 万条；CAPES 约 400 万邮箱、400 万电话及 100 万银行信息；Digikala 300 万条；Transfast 120 万条；美国 Tax ID 100 万条；美国公民 80 万 SSN；以及 Spencer’s 自称 461,876,732 条结构化记录。整体看，本周高影响情报集中在 WordPress 用户表与后台账户、业务系统订单/支付/收货数据、政务与教育身份档案，以及多来源数据合集；多条帖子以隐藏下载或私信询价方式引流，规模与字段完整性仍需结合后续样本继续验证。

**每日纳入统计事件数**

| **日期** | **事件数** |
| --- | --- |
| 2026-11-07 | 17 |
| 2026-11-08 | 16 |
| 2026-11-09 | 12 |
| 2026-11-10 | 13 |
| 2026-11-11 | 16 |
| 2026-11-12 | 17 |
| 2026-11-13 | 22 |

**美国零售商 Spencer’s 全量数据库泄露**

**泄露数据介绍：**2026 年 11 月 7 日，用户 scarlettgroup 发布美国零售商 Spencer’s（spencers.com）数据泄露帖。帖子称已入侵目标并公开完整数据库，列出的主要数据包括用户 1,558,731 条、忠诚度会员 1,550,695 条、忠诚度账户 32,260,574 条及扩展记录 12,897,184 条；个人记录 1,552,030 条，其中含出生日期 1,531,534 条、用户名 1,550,255 条、密码哈希 1,558,731 条，以及邮箱、手机、地址和邮编等联系信息。帖子还列明设备、PIN、交易头、交易明细、支付、优惠券与营销记录的数量，并自称合计 **461,876,732 条结构化记录**。公开样例为 PersonalDetails 表，包含姓名、出生日期、性别、语音姓名键和更新时间等字段。若样本属实，将显著放大撞库、精准钓鱼和支付欺诈风险。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.131304.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO3k1heu6YibxdRiaYj1FB4FJaIqkBCQWMe6Rh7d91z1V1A5GQHLSjl83gGV6y42eicjX4KO8VNwMu1Rk9yNqfQyPTds2jX85ibPmWg/640?wx_fmt=png&from=appmsg)

**多米尼加 ITLA 2.3 万名学生数据泄露**

**泄露数据介绍：**2026 年 11 月 7 日，用户 RoyalLeaked 发布多米尼加 Instituto Tecnológico de las Américas（ITLA）学生数据库，标题称规模为 23K+。帖子称数据覆盖在读与非在读学生，包含注册 ID、国家身份证号、姓名、专业/学位、学校邮箱、课程计划、累计与季度 GPA、学籍和账户状态、身份证件照片、体检证明、官方成绩单和 2×2 照片，并提供 1,000 行样例链接；完整数据库需私信获取或询价。该批数据同时包含**身份证明与教育记录**，具备身份冒用、学籍欺诈和二次勒索风险。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.131599.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO02uCicFefUaTanyKibiaRcOtzQgWKXfSLHeCLjbQmOCTC4Pkibjo3NJ4J2ckjWNtpZWVyq6hILyNLcdxib2nKrabam2lDOlicPhVejs/640?wx_fmt=png&from=appmsg)

**多平台 1.97 亿条数据集合在暗网展示**

**泄露数据介绍：**2026 年 11 月 8 日，用户 Marx 发布标题为“Database (Noon,Viber,Google,Facebook,CANBNK,Whatsapp,SIVVI,noonGrocery...) +197M”的帖子。帖子称公开内容仅为其收藏中的小部分样本，点名 Noon、Viber、Google、Facebook、CANBNK、WhatsApp、SIVVI、noon Grocery 等平台，并声称掌握覆盖 **970 余家企业、跨行业和跨地区的数据集合**；下载内容置于登录可见区域。公开页面未逐项披露数据来源、字段和去重口径，因此应将该帖视为多来源数据合集展示，而非单一平台独立泄露。若规模属实，将增加跨站撞库、身份关联和定向诈骗风险。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.131956.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO26YXfb3AoHudpoDypqH6JJ2exKic62SichvDJsBrTTWWbg5aPqTTME3IsqOJXVt5x73unOd7K8nDeApz3m1slC5GibDJJ3y0heC0/640?wx_fmt=png&from=appmsg)

**比利时国防军事委员会通讯录泄露**

**泄露数据介绍：**2026 年 11 月 8 日，用户 th3sevenflow 发布标题为“BELGIAN DEFENCE — MILITARY COMMITTEE DIRECTORY”的帖子。公开页面仅显示标题及登录可见的隐藏内容，未展示数据条数、字段、样例或下载信息；因此本报告仅能确认其声称涉及比利时国防军事委员会通讯录，无法核验具体内容。若真实性得到确认，该类人员、职务和联系信息可能被用于**定向社工、钓鱼及供应链渗透**。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.132189.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO364Dj9uuqvO0qgZmw2ASF63e2Ro9UCWehibcavX7iagx62cq8Tgcia0J1pmEBRa4usTs4jDtTaUtjY8Zic0P8aiczIYjd1ZDX01ggU/640?wx_fmt=png&from=appmsg)

**克罗地亚 starter.estudent.hr 用户数据库泄露**

**泄露数据介绍：**2026 年 11 月 9 日，用户 Richard2002 发布克罗地亚教育站点 starter.estudent.hr 数据库。公开样例为 **WordPress 用户表**，字段包括 ID、登录名、密码哈希、昵称、邮箱、站点地址、注册时间、激活密钥、账户状态和显示名；样例中出现管理员、IT Admin、PR 等账户。帖子未在公开区域给出总记录数，下载链接为登录可见状态。风险集中在账户接管、密码复用和后台权限滥用。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.132441.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO204JmN6qmGHJ8jHrSL4CBxjbqCnGzZ7K6TtpbjE06TEDAP3FzVDKHHWVo2P8467ZNVIoTmViaCicY1My6phaZuZwZicD7Otxq1gE/640?wx_fmt=png&from=appmsg)

**acuteposting.com WordPress 用户数据库泄露**

**泄露数据介绍：**2026 年 11 月 9 日，用户 Richard2002 发布 acuteposting.com 数据库。公开样例同样为 WordPress 用户表，包含用户 ID、登录名、密码哈希、昵称、邮箱、站点地址、激活密钥、状态和显示名，下载链接置于登录可见区域。帖子未公开总条数，但样例覆盖多个普通用户及站点账户。若密码哈希可被破解，可能引发账户接管、内容发布权限滥用和跨站撞库。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.132677.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO2ibUNmbIy3kicU9Ideb4qsDoicIGxYkuOXfkHJl5X2AfLBk73IInLF8cP2vfVM2nUAW4FVScNmXDzJAD01ia3Dh0dwn9Nv93CF44w/640?wx_fmt=png&from=appmsg)

**韩国 webcruit 招聘平台求职者数据库泄露**

**泄露数据介绍：**2026 年 11 月 10 日，用户 Richard2002 发布韩国招聘站点 ksryu.webcruit.co.kr（标题亦写作 ksryu@webcruit.co.kr）数据库。公开样例包含 userid、姓名、性别、生日、居民号码、邮编、地址、邮箱、电话/手机、短信与邮件接收标记、职位类别、工作类型、入职日期、期望薪资、职业经历、主页、银行名称、账户名和账户号、状态及备注等字段。下载内容隐藏，总记录数未在公开区域说明。数据同时覆盖**求职者身份、联系方式和金融账户**，敏感度较高。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.132958.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO0CgHVaaM0jUibRhsNhLWI9Npg8WyVFObmtibpJoTETQwiaUPfxJX6Z0pz9ujBIz9Q09zpOS3pkKUGKZshuPGKLfTmkBuEx3kLDr4/640?wx_fmt=png&from=appmsg)

**韩国 koreastamp.net 会员与订单数据库泄露**

**泄露数据介绍：**2026 年 11 月 10 日，用户 Richard2002 发布韩国 koreastamp.net 会员与订单数据库。公开样例显示至少两张表：会员表包含用户编号、账号、密码、姓名、等级、邮箱、居民号码、代理/营业执照字段、积分和登录次数；订单表包含订单号、下单日期、状态、金额、账户、订购人、收件人、电话、邮箱、地址、支付方式、配送方式、运单号等。帖子未披露总条数，下载链接需登录。会员凭证与订单、收货信息可组合用于**账户接管、身份冒用和精准诈骗**。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.133224.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO2DIkTRAauCLAAk1hG8BAVoIYR7cd4vQGZycmtgxzxUIGp5jkLiaBibhlRFJBtv2h2kdzDzfgsDiacK6r8xGEv5vdpM0Gk8K6c1HY/640?wx_fmt=png&from=appmsg)

**Transfast 跨境汇款 120 万条记录泄露**

**泄露数据介绍：**2026 年 11 月 11 日，用户 Marx 发布 Transfast 数据泄露帖，标题称记录规模为 120 万。帖子介绍 Transfast 为被万事达卡收购的全球跨境汇款网络，当前主要提供 B2B 支付与部分地区的消费者汇款服务；公开字段包括 SequentialId、用户名、创建时间、源地址、目的地址、国家、运营商、移动国家码/网络码、携号转网状态、消息 ID、消息内容、汇率和短信投递错误码。下载链接隐藏，帖子未公开展示实际样例记录。字段指向**短信/交易日志类数据**，一旦属实可能暴露跨境资金与通信关系。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.133519.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO0JuI4zDyTrK9Pqia9xHpE5PLF8u3RaniahBSFIMATJibtvKX3iciaD1w4RQjMd4z3NHhxH3xtWPvibFEaKr8lw5jTxshxT7ibMXpJMf0/640?wx_fmt=png&from=appmsg)

**美国税务识别号数据库 100 万条记录泄露**

**泄露数据介绍：**2026 年 11 月 11 日，用户 joss1232 发布标题为“USA Tax ID Database 1 Million”的帖子，声称包含 **100 万条美国税务识别号相关数据**。公开字段包括索引、类型、ID、评分、来源 ID、姓名、性别、出生日期、tax\_id、多个关联 ID、地址、城市、州、邮编、县、电话、第二电话、邮箱、设备 ID、Cookie ID 和 IP 地址。下载信息被隐藏，公开区域未提供可核验样例。若数据真实，可能被用于税务身份冒用、开户欺诈、信用申请和精准钓鱼。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.133797.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO3aTFQmIuQMF0cYic0peR8SfLXOHTbPDgczPzibKeeBLbBQSwyXK1Wzy0bsFkcWic0dnlGNhNIqPztc3da2dYhWfn20XL4VeRy1WQ/640?wx_fmt=png&from=appmsg)

**意大利 sardegnaoggi.it 用户数据库泄露**

**泄露数据介绍：**2026 年 11 月 12 日，用户 Linda2000 发布意大利撒丁岛新闻站点 sardegnaoggi.it 数据库。公开样例为 WordPress 用户表，字段包括 ID、登录名、密码哈希、昵称、邮箱、站点地址、注册时间、激活密钥、账户状态和显示名，样例可见编辑或管理相关账户及 2024 年注册记录。帖子未披露总条数，下载链接登录可见。风险包括**新闻后台账户接管、内容篡改、密码复用和定向钓鱼**。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.134039.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO08ddmtZ6mm4ktsss2vwaXHTs9oQfibD0UbF3jMlslxUhVmsQTFZvhJMoYOfFXTxwoh8a37xspOXB4CWpicUlr8D6j0HI9LLeO8A/640?wx_fmt=png&from=appmsg)

**俄罗斯 lib26.ru 1.6 万用户数据库泄露**

**泄露数据介绍：**2026 年 11 月 12 日，用户 bobus123 发布俄罗斯站点 lib26.ru 数据库，标题称约 1.6 万用户。帖子称数据于 2025 年通过 SQL 注入获取，目标站点目前疑似停止运营；公开样例主要来自 zakaz.csv，包含订单标识、疑似哈希值、地区或详细地址、日期、姓名、邮编、电话、支付或配送备注及邮箱等字段，<blank> 表示空值。下载链接隐藏。数据覆盖实名、地址、电话和订单信息，可用于身份关联、精准诈骗及历史订单分析。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.134302.png](https://mmbiz.qpic.cn/mmbiz_png/hzXgvqPiczO3UxkCoZ0spoQdy5kibXlSscnXSrs30ELibebgUdpnhwL4W12mx0aGWhS3BmWux3NFz3rhRJo2YzIpJYpfZr7wMLgVyQ0JxCRVia8/640?wx_fmt=png&from=appmsg)

**几内亚央行 SYRIF 系统 3.9GB 数据泄露**

**泄露数据介绍：**2026 年 11 月 13 日，用户 byte224 发布几内亚共和国中央银行（BCRG）SYRIF 系统数据泄露帖。帖子称已攻陷该系统并取得全部数据库，数据量约 **3.9GB**，包含 800 万条会计分录、48 家金融机构的资产负债表、182 个用户账户，以及包括毕马威审计材料在内的内部机密文件；帖内附有两张系统或数据截图。该事件若属实，涉及**央行支付清算与监管数据**，可能暴露金融机构业务关系、账户与审计信息，并带来高等级金融欺诈和系统性风险。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.134562.png](https://mmbiz.qpic.cn/sz_mmbiz_png/hzXgvqPiczO3XXfN9Nyco9BicCa10PfIW2cSVSVicBVyBhmpfW6oZUn9atByZvp9FCyIBpBkDJibSdoADZzAlKia7fC2gGVNGsUKYjAXM5E5k04o/640?wx_fmt=png&from=appmsg)

**Gemini.com 1211 万条数据库泄露**

**泄露数据介绍：**2026 年 11 月 13 日，用户 Darkiros687 发布标题为“12.11M Gemini.com database”的帖子，标题声称数据规模为 **1211 万条**。公开页面仅显示登录可见的隐藏内容，未展示数据字段、样例、来源说明或下载地址；因此只能确认帖子对目标与规模的单方面宣称。若数据真实，可能与账号凭证、身份或交易数据相关，需重点关注撞库、账户接管和资产安全风险。

![暗网数据泄露情报精选周报_2026.11.07-2026.11.134788.png](https://mmbi...