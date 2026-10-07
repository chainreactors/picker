---
title: 从 union 读到路径，到写进一句话：SQL 注入 getshell 这条链，到底卡在哪
url: https://mp.weixin.qq.com/s/BFB-NuP8ld7cvwuN9Ry75g
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:25.249218
---

# 从 union 读到路径，到写进一句话：SQL 注入 getshell 这条链，到底卡在哪

# 从 union 读到路径，到写进一句话：SQL 注入 getshell 这条链，到底卡在哪

原创

Sink
Sink

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

实战笔记 · PENTEST

从 union 读到路径，到写进一句话：SQL 注入 getshell 这条链，到底卡在哪

船山信安 · 2026 · 靶场原理向复盘 · 阅读约 12 分钟

你点开一个商品详情页，URL 后面跟着 id=1。你把它改成 id=1'，页面报错了。就这一个单引号，足够让一条查询变成你手里的笔。

这篇不教你怎么打谁。它讲的是：一条注入从"能读"到"能写文件"再到"服务器上多了一个壳"，中间每一脚踩的是什么、卡在哪、以及——站在防守这边，每一脚怎么断。所有命令都来自公开靶场与原理教材，点到为止。

1洞为什么存在：不是程序员手抖，是把用户输入当成了 SQL 的语法

绝大多数注入的根，就一句话：**程序把用户传进来的字符串，直接拼进了 SQL 语句**。数据库分不清哪部分是"命令"、哪部分是"数据"，它照单全收。

SELECT \* FROM products WHERE id = '$id'

当 $id 是 1' OR '1'='1，这条语句的逻辑就被改写了——它不再找 id 为 1 的商品，而是把整张表都吐出来。行业里常见的 id、cat、page 这类 GET 参数，是重灾区。这不是某个单位的问题，是十年没变的老毛病。

2union 那一脚：从报错到回显，先把"嘴"撬开

拿到一个疑似注入点，第一件事不是想怎么写文件，是搞清楚"它回不回显、字段有几列"。

先探字段数。用 ORDER BY N 一点点加，直到页面从正常变成异常，那个临界点就是列数。接着用 UNION SELECT 1,2,3... 把数字顶上去，看哪个位置的数字出现在页面正文里——那个位置，就是你能"吐数据"的回显位。

id=1 ORDER BY 4    # 正常

    id=1 ORDER BY 5    # 报错 → 4 列

    id=0 UNION SELECT 1,2,3,4    # 看哪个数字回显

卡点来了：很多站点页面正常，但回显位一个都没有。这时候别急，换报错注入。MySQL 有个经典公式，靠 floor(rand(0)\*2) 故意制造主键重复，把你想看的数据塞进报错信息里吐出来：

UNION SELECT 1 FROM(SELECT COUNT(\*),

      CONCAT(FLOOR(RAND(0)\*2),(SELECT VERSION()))x

    FROM information\_schema.tables GROUP BY x)a

要是连报错都被吞了，就剩盲注：用 SLEEP(5) 看响应慢不慢，用 SUBSTRING() 一个字符一个字符往外抠。慢，但稳。这一步到这，你还只是"能读"。

3真正要命的一步：从读数据，到往磁盘写文件

读，只是偷看；写，才是把脚迈进去。MySQL 有两个函数让注入突破"只读"：load\_file() 读服务器上的文件，INTO OUTFILE 把查询结果写成文件。

读配置文件，往往是写马的前奏——先拿到网站物理路径、数据库账号，才知道往哪落、用什么权限落：

UNION SELECT 1, LOAD\_FILE('/etc/passwd')

    UNION SELECT 1, '<?php eval($\_POST[cmd]);?>'

      INTO OUTFILE '/var/www/html/s.php'

这里有个真实的坑，老教材里反复提：用 INTO OUTFILE 写马时，MySQL 会把你语句里的换行原样写进文件。大马里换行一多，PHP 直接解析报错。所以实战里几乎都写"一句话"，而不是整匹大马——一行搞定，少出错。

另一个更硬的卡点：现代 MySQL 默认 secure\_file\_priv 不是空，而是 NULL 或某个固定目录。一旦是 NULL，INTO OUTFILE 直接被拦，任凭你权限多大都没用。当年不少管理员图省事把这参数放开、还用 root 连库，才把这条路铺平；现在这扇门，运维默认就焊死了。

灵光一闪往往在这：outfile 走不通，就去看 general\_log 能不能开、日志路径能不能写；或者换数据库——PostgreSQL 的 COPY 和 INSERT ... VALUES('<?php eval...') 同样能把一句话落进磁盘。这，就是从"能读"跨到"能写"的那道坎。

4对抗升级：WAF 拦了，就换皮再来

能写马，不代表能落地。前面大概率还站着一道 WAF。它的规则大多盯着明文 UNION SELECT、SLEEP()。绕它，本质是把同一条语义，穿上不同的衣服：

内联注释插空：/!50000UNION/ /!50000SELECT/

换行与制表符：%0a、%09 塞进关键字缝隙

大小写与 URL 双重编码：UnIoN、%2553

Base64 变形：把整段 payload 编码后由解码函数还原

这一来一回，是攻防双方在"语义等价"上的拉锯。WAF 越严，变形越花；变形越花，规则越要上语义分析。没有终点的猫鼠游戏。

5防守视角：这条链，每一脚都能断

讲完攻击链，回到我们该站的一边。上面每一脚，防守都有对应的断点。别等出了事再补课。

|  |  |
| --- | --- |
| 攻击那一步 | 防守怎么断 |
| 拼接 SQL，用户输入当语法 | 参数化查询 / 预编译，让输入永远是数据 |
| UNION / 报错 / 盲注读数据 | 白名单校验类型长度、最小权限账号、关错误回显 |
| INTO OUTFILE / LOAD\_FILE 写读文件 | secure\_file\_priv=NULL、禁用 general\_log、降权 |
| WAF 变形绕过 | 语义级检测 + 代码审计根治，而非只加正则 |

参数化是根上的修法。给一段正确的 Java，对比拼接写法：

// 错误：拼接

    String sql = "SELECT \* FROM u WHERE id='"+id+"'";

    // 正确：预编译

    PreparedStatement ps = conn.prepareStatement(

      "SELECT \* FROM u WHERE id=?");

    ps.setString(1, id);

检测侧，别只靠 WAF 被动挡。自己用 sqlmap 扫一遍自己的站，比等别人扫你强：

sqlmap -u "https://example.com/p?id=1" --batch

    sqlmap -u "https://example.com/p?id=1" --os-shell # 自查写文件风险

代码审计上，可以用 CodeQL 这类工具写规则，把"用户输入流入 SQL 执行"的路径一次性捞出来——把洞在合并之前就掐死，比上线后救火便宜得多。

注入不是某个函数的 bug，是把用户输入当成了 SQL 的语法。

你修的是"参数化"这一个习惯，不是某一行过滤。链子再长，断在任何一节都够用；可只要拼接还在，后面九道门都形同虚设。

参考来源

· 《习科SQL注入自学指南》· ima 知识库「网络安全知识库」（union / into outfile / load\_file / 报错注入 / 换行坑）

· 《靶场SQL注入篇(中)：以 sql1\_POST 实战，讲 POST 注入、getshell 与 sqlmap》· ima「信息安全备份」

· 《渗透测试从业者的实战课：SQL注入到Getshell》· ima「信息安全备份」

· 《SQL注入:堆叠注入写shell详解》· 小话安全

· 《绕 WAF 实战：6 种 SQL 注入变形技巧》· CISSP

· 《实战复盘：严苛 WAF 防护下的 SQL 注入绕过思路与实现》· 洞悉安全团队

本文为授权靶场与公开原理教材的合规复盘，所有命令与技巧均用于防御视角学习，点到为止。任何未授权的渗透行为均属违法。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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