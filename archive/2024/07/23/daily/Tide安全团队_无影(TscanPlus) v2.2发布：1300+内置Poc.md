---
title: 无影(TscanPlus) v2.2发布：1300+内置Poc
url: https://mp.weixin.qq.com/s?__biz=Mzg2NTA4OTI5NA==&mid=2247516589&idx=1&sn=107da3b45e88255f240504d033ebde7f&chksm=ce5da3ccf92a2adab0511bd798570d967cd4b0b7d7528f2f17163f5ed77e4dd7a02ac17c39d7&scene=58&subscene=0#rd
source: Tide安全团队
date: 2024-07-23
fetch_date: 2025-10-06T17:43:51.839270
---

# 无影(TscanPlus) v2.2发布：1300+内置Poc

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOna51M5QOOGC5aQmiazfOKKRNA5lsbkQEb8HQy8HD0poaCQfOmHZUEZg/0?wx_fmt=jpeg)

# 无影(TscanPlus) v2.2发布：1300+内置Poc

原创

重剑无锋

Tide安全团队

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png)

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png)

**【无影(TscanPlus) v2.2新增key认证功能，转发本文章到朋友圈，获赞30个以上，截图发到"Tide安全团队"公众号后台，可获取一个key，解锁所有POC功能。】**

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEO6fvSbC8libRWFfcnV30QomKHblp3zwz7mnibkGLibU4Vaia1vaa1Zb3HwQ/640?wx_fmt=png&from=appmsg)

无影(TscanPlus)，一款综合性网络安全检测和运维工具，旨在快速资产发现、识别、检测，构建基础资产信息库，协助甲方安全团队或者安全运维人员有效侦察和检索资产，发现存在的薄弱点和攻击面。

**【主要功能】** 端口探测、服务识别、URL指纹识别、POC验证、弱口令猜解、目录扫描、域名探测、网络空探等。

**【辅助功能】** 编码解码、加密解密、CS上线、反弹shell、杀软查询、提权辅助、常用命令、字典生成等。

**TscanPlus 功能介绍可参考文章：《TscanPlus——一款红队自动化工具》**https://mp.weixin.qq.com/s/G\_ErhJZqvS9h-XHKeAcy3A

**【特色功能】**

1、内置5.2W余条指纹数据，对1万个web系统进行指纹识别仅需8-10分钟，在效率和指纹覆盖面方面应该是目前较高的了。

2、在指纹探测结果中，对130多个红队常见CMS和框架、Poc可关联CMS进行了自动标注。内置大量高质量Poc，并可外接Nuclei、Afrog、Xray等Poc工具，可实现指纹和Poc的联动，根据指纹识别的结果自动关联Poc，并可直接查看poc数据包相关信息。

3、在创建IP端口扫描、Url扫描时，可关联Poc检测、密码破解、目录扫描等功能，发现匹配的服务或产品时会自动触发密码破解或poc检测。

4、内置34种常见服务的弱口令破解，可方便管理员对内网弱口令进行排查，为提高检测效率，优选并精简每个服务的用户名和密码字典。覆盖的服务包括：SSH,RDP,SMB,MYSQL,SQLServer,Oracle,MongoDB,Redis,PostgreSQL,MemCached,Elasticsearch,FTP,Telnet,WinRM,VNC,SVN,Tomcat,WebLogic,Jboss,Zookeeper,Socks5,SNMP,WMI,LDAP,LDAPS,SMTP,POP3,IMAP,SMTP\_SSL,IMAP\_SSL,POP3\_SSL,RouterOS,WebBasicAuth,Webdav,CobaltStrike等。

5、实现了编码解码、哈希计算、加密解密、国密算法、数据格式化、其他转换等共36种类型，其中编码解码类8种、哈希计算13种、加密解密9种、国密算法3种、数据格式化9种、其他2种。

6、目录枚举默认使用HEAD方式，可对并发、超时、过滤、字典等进行自定义，内置了DirSearch的字典，可导入自己的字典文件，也可用内置字典fuzz工具进行生成。

7、内置各类反弹shell命令85条、Win内网(凭证获取、权限维持、横向移动)命令26类、Linux内网命令18类、下载命令31条、MSF生成命令21条、CS免杀上线命令等，可根据shell类型、操作系统类型、监听类型自动生成代码。

8、灵活的代理设置，可一键设置全局代理，也可以各模块单独开启代理功能，支持HTTP(S)/SOCKS5两种代理，支持身份认证。

9、快速的子域名探测，域名可联动其他子功能，可配置key后对接多个网络空间探测平台，一键查询去重。

10、内置资产分拣、JsFinder、Host碰撞、Jwt秘钥破解、IP查询、Windows提权辅助、杀软查询、shiro解密等各类工具。

### 更新日志

无影(TscanPlus) v2.2正式版发布，感谢各位师傅提出的宝贵修改建议和诸多bug！

主要更新：

1、新增4项新功能：Host碰撞、40xBypass检测、Jwt破解和加解密、IP归属地查询。

2、为使"无影"Poc检测能形成良性生态，增加Key认证功能(可解锁所有Poc)。

3、支持自定义被动指纹和主动指纹添加，并增加指纹策略，可根据不同需求和电脑配置选择不同指纹库。

4、各功能模块支持断点重扫功能，当扫描中断、点Stop停止或程序闪退、卡死等情况，可恢复之前的扫描。

5、增加配置文件自动备份、hunter自定义API、红队内置命令可编辑等。

6、修复目录扫描闪退、Telnet蜜罐误报、端口策略、主动指纹误报、WMI/RDP密码破解误报、标题乱码显示等诸多Bug。

在此也感谢各位师傅（来自Github、知识星球、工具交流群等）提出的宝贵修改建议和诸多bug！所有提过bug或建议的小伙伴会被拉入工具交流群，并享受新版本新功能第一时间尝鲜及永久VIP服务！

### 1、软件使用

Github下载：https://github.com/TideSec/Tscanplus

软件基于Wails开发，可支持Windows/Mac/Linux等系统，下载即可使用。

### 2、新功能介绍

#### 2.1 新增Key认证功能

为了"无影(TscanPlus)"的Poc检测更全面、精准，能形成良性生态，新增key认证功能，经过key认证后，可使用所有内置POC，未认证用户只能使用420个POC，其他功能均可正常使用。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOLXThjBmlr0LVxaExaej7POw2zIKia0es5KsOgDLOnPoibF0MIK0l18Bw/640?wx_fmt=png&from=appmsg)

通过key认证后，可使用所有内置的1300个poc。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEONINYxwcibkran0Sm5Kk3bwcictoiaGEWAO6ObEAV1tZiafdiaUrNYo4oKwg/640?wx_fmt=png&from=appmsg)

**获取Key的四条途径:**

1、在Poc平台提交3个Poc后可获得3个Key，之后每多提交一个Poc可多获得一个Key。

2、在交流群或Github Issue中提交一个有效Bug，Bug修复后可获得一个Key。

3、加入星球可直接获得3个Key，之后每提交一个Poc可多获得一个Key。

**4、转发本文章到朋友圈，获赞30个以上，截图发到"Tide安全团队"公众号，可获得一个key，解锁所有poc功能。**

**详细Key提交、获取和使用说明可看这里：http://poc.tidesec.com/index/explain.html**

#### 2.2 新增Host碰撞功能

Host碰撞通过修改Host字段来发送数据包，该功能可对 IP和域名碰撞匹配，访问到绑定host才能访问的系统。因为现在越来越多的业 务是通过nginx等负载进行反向代理访问，可能有些内网域名和外网域名使用相同的 负载均衡进行反代，这样就可能通过修改host字段实现访问内网系统。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOSicXKYKu2ByrJxr2o4fx8gDicq0110B0HvsOyGAYyFicHuoeNktbZEj5w/640?wx_fmt=png&from=appmsg)

2.3 新增40xBypass检测功能

做渗透测试时常会碰到40x的资产，而有一些40x的页面是可以绕过的，比如不同的HTTP方法、Referer绕过、代理IP、HTTP Header修改、替换大小写等。40xBypass检测功能集成了8种常见bypass方式，并可在config/4xxBypass目录下修改字典文件。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOap5zCYiaG2XadAHnhwMia1VfwzsVT9pejSSyGbgehicqibOLjycXsaic0aw/640?wx_fmt=png&from=appmsg)

2.4 新增Jwt破解和加解密功能

可对jwt进行加解码和秘钥破解，支持HS256、HS384、HS512、RS256、RS384、RS512、ES256、EDDSA等多种算法。内置秘钥字典10W+，两秒可完成，

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOXlIWyoia5OpaVGhaBUehyC11yOWftB774mTHtibPm0ibnPdciajzEXHwRg/640?wx_fmt=png&from=appmsg)

2.5 新增IP归属地查询

针对ip地址、子域名等资产可自动提取，并查询物理地址。并在ip扫描、url探测、子域名枚举时，增加ip查询功能。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOJRQYQZR0TEUgicKepzzy7ibjCNtg4tVSAIsT4cya36OquSDUC0bdOInw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOBMLdJD5HRnDiahlSCeaX1XANicmLw6VzlWQjK3A7ts4OuAXjOJ1jiaU6w/640?wx_fmt=png&from=appmsg)

3、其他已有功能

#### 1、Welcome

软件运行后，需审慎阅读、充分理解**《免责声明&使用许可》**内容，并在Welcome页面勾选**“我同意所有条款”**，之后方可使用本软件。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOKEjTugqdAvLflvkh5DTWdU6wwwUZBm38DXu69C44RSicK0adIDB593Q/640?wx_fmt=png&from=appmsg)

2、项目管理

项目管理功能是把各分散功能进行流程整合，用户可根据自己的使用场景设计项目功能，完美融合了"资产测绘"、"子域名枚举"、"IP端口扫描"、"密码破解"、"POC检测"、"URL扫描"、"目录探测"、"UrlFinder"等功能。项目执行结果会存储到相应项目数据库中，方便后续查询和使用。

**【任务配置】**

在添加目标资产并配置任务参数后，TscanPlus会在后台对相应目标执行相应操作，并显示在对应功能Tab栏中。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOAdG3l4iayS2pb2a4QWWstVG3mPe3wxqyDJlutwyrk6qcccfNa3NvCSg/640?wx_fmt=png&from=appmsg)

**【项目管理】**

在项目管理中，还可直观的展示项目概览，如项目总数、URL资产、IP资产、漏洞总数、敏感信息等，并可对所有项目进行编辑、重新执行、停止、删除等操作。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEORbWn0b4LkKeAibP33OCByxLHns2VMvDdmrYqgZ4XOIRuLjmmmtJQQwg/640?wx_fmt=png&from=appmsg)

**【结果展示】**

所有扫描结果将显示在对应功能Tab中。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOcXZ42dfQxNPjoHL0uCjHzsiboVFgxRURyicAd2zQGa2rA0Y2KKjbBVNQ/640?wx_fmt=png&from=appmsg)

3、端口扫描

对目标IP进行存活探测、端口开放探测、端口服务识别、Banner识别等，可识别100余种服务和协议。

**【任务配置】**

IP支持换行分割，支持如下格式：192.168.1.1、192.168.1.1/24、192.168.1.1-255、192.168.1.1,192.168.1.3
排除IP可在可支持输入的IP格式前加!：!192.168.1.1/26

可选择端口策略、是否启用Ping扫描、是否同步密码破解、是否同步POC检测、是否开启代理，配置任务后可开启扫描。

**【扫描结果】**

扫描结果如下，会显示服务相关协议、Banner、状态码、标题等，如Banner中匹配到可能存在漏洞的产品会使用红色标识。

选择某一行，右键菜单也可对某地址进行单独POC测试、弱口令测试、目录枚举等，也可以对数据进行单条保存或全部保存。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEO3QG95CZX2ISLxQM2ibFiaNv0aDZfytEYMskRfQcVtQ6MMW306YptxE0w/640?wx_fmt=png&from=appmsg)

**【功能联动】**

在任意功能中，都可与其他功能进行联动，比如IP扫描时可同时开启密码破解和POC检测，一旦发现匹配的端口服务会自动进行密码破解，发现匹配的指纹时会进行poc检测。勾选这两项即可，结果会显示在相关模块中。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEO06vrNLyNdYSf8u28kSNlMm6DxYRSrLxzwSEn77ibX7aGicmfm8kANib1A/640?wx_fmt=png&from=appmsg)

**【高级配置】**

在高级配置中可设置代理地址，在开启全局代理后，各功能都会代理，支持HTTP(S)/SOCKS5两种代理，支持身份认证。还可以设置全局cookie或UA等。

代理格式：

HTTP代理格式：http://10.10.10.10:8081  或 http://user:pass@10.10.10.10:8081

HTTPS代理格式：https://10.10.10.10:8081  或 https://user:pass@10.10.10.10:8081

Socks5代理格式：socks5://10.10.10.10:8081  或 socks5://user:pass@10.10.10.10:8081

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOwjKcnIhQwxqfWDRHx6tTdLs5aXX2MKo5s2pG9A7EBP9ibtbXfXIK5dw/640?wx_fmt=png&from=appmsg)

4、URL探测

TscanPlus目前整合指纹2.6W余条，经多次优化，有效提高了资产发现的协程并发效率，对1万个web系统进行指纹识别仅需8-10分钟，在效率和指纹覆盖面方面应该是目前较高的了。

**【任务配置】**

URL探测主要针对web地址进行批量检测，输入格式为Url地址每行一个，并且前缀为http/https：http://www.abc.com
http://192.168.1.1:8080
https://www.abc.com:8443

同样，可选择线程数、是否同步POC检测、是否开启代理，配置任务后可开启扫描。

**【扫描结果】**

扫描结果如下，会显示web站点标题、Banner、状态码、中间件、WAF识别等，如Banner中匹配到可能存在漏洞的产品会使用红色标识。

选择某一行，右键菜单也可对某地址进行单独POC测试、目录枚举等，也可以对数据进行单条保存或全部保存。

![](https://mmbiz.qpic.cn/mmbiz_png/rTicZ9Hibb6RXrFcGYWDxQLSwIOa9S3iaEOF6l8ibFyUuuTyv2zcvYtAqhCTibTF1xZeP0QF4MDfhTnEubvgRlBXhww/640?wx_fmt=png&from=appmsg)

5、域名枚举

在域名枚举方面TscanPlus集成了多种功能，可以使用字典枚举，也可以使用多个免费接口进行查询。还可以对枚举到的域名进行联动的端口开放测试、指纹识别及poc检测、目录枚举等。

**【任务配置】**

枚举较依赖网络，所以多域名时会逐个进行。默认10000的字典，线程50在网络状态较好时大约用时12秒。

域名每行一个，不要加http前缀，如:

tidesec.com
tidesec.com.cn

同样，可选择线程数（建议50-00）、是...