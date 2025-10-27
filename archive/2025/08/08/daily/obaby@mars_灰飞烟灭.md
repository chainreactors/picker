---
title: 灰飞烟灭
url: https://h4ck.org.cn/2025/08/21152
source: obaby@mars
date: 2025-08-08
fetch_date: 2025-10-07T00:16:03.436240
---

# 灰飞烟灭

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[个人日记『Diary』](https://h4ck.org.cn/cats/dddd/grrj)

# 灰飞烟灭

2025年8月8日
[43 条评论](https://h4ck.org.cn/2025/08/21152#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1653.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1653.jpg)

上周的某一天，早上吃饭的时候，宝子掉了一地的渣渣。我去拿吸尘器给吸了一下，立到支架上就去看电视了。然而，过了一分钟左右突然传来“嘭”的一声，吸尘器直接摔倒了地上，尘盒也掉了下来。

想装回去的时候却发现怎么也扣不住了，仔细一看才发现那个卡扣断掉了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16601754272188_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16601754272188_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/16591754272187_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16591754272187_.pic_.jpg)

在京东上提交了一条售后服务申请，很快就接到了追觅的客服电话，告知京东无法提供线上维修，会直接把申请结束，他们安排顺丰上门取件。本来预约的时间是下午，但是下午也是在没时间，只能改到中午。

就在自己准备回家的时候，连续收到多条 nas 报警。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16641754272804_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16641754272804_.pic_.jpg)

刚才是看到这几条消息，觉得应该没什么太大问题，然而，事实证明情况远比自己想象的要严重的多。到家之后，打开门就听到滴滴滴的间歇性报警音。先把 nas 从机柜里拆出来，重新上电开机，插上网线。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16581754272186_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16581754272186_.pic_.jpg)

可以看到 hdd2 的硬盘指示灯已经变成了黄色，进入系统之后。显示的也是存储已经损毁。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/9101DEE542986DEDC4FB260875A66E71.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/9101DEE542986DEDC4FB260875A66E71.jpg)

之前也曾经想过可能会出现硬盘损坏的情况，于是按照群晖的建议组的 shr-1 （*Synology* Hybrid RAID (SHR)）带一块磁盘冗余的阵列模式，想着这样即使坏了一块硬盘也可以重建存储。

此时，我觉得坏的只是第二块硬盘而已。就在这时顺丰也来取快递了，把东西寄走，给 nas 关机，从二手东上买新的硬盘。这次没有选择所谓的 nas 盘，直接买了块普通的台式机硬盘。至于 nas 盘是不是智商税，其实我也不清楚。

第二天，磁盘终于送到了。晚上回家之后自然是先尝试解决这个问题，将新硬盘换上去。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16561754272184_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16561754272184_.pic_.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/16551754272183_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16551754272183_.pic_.jpg)

然而事情远不像自己想象的那么顺利，装上去之后，并没有更换硬盘的选项。并且 nas 系统是 7.1.1，卡在了这个奇怪的版本，监测更新提示没有更新。然而，另外一台 nas 是 7.2.2.

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-02-230125.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-02-230125.png) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-01-195135-scaled.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-01-195135.png)

套件中心也只有寥寥无几的几个 app。最后只找到一个停用的选项，然而停用的时候，说看指示灯提示操作，这尼玛，怎么看？什么时候拔硬盘，带电拔还是停电拔？怎么个换法，没有任何的提示，去看官方的文档也都是一堆废话，有用的信息一点都没有。最后停用了，插上新硬盘，却只是提示新硬盘未初始化，没有重建磁盘阵列的选项，只有个新建，这尼玛和官方文档给的也不一样啊？这是什么骚操作？

一通操作下来，是在是没有任何的办法，系统没有更新，也找不到重建磁盘阵列的选项。

既然到这这一步，也就不在想着能重建磁盘阵列了。删除存储空间，直接重建。至于各种数据：上万首音乐，数千部电影，存的数年的照片，基本都不可能复原了。不过好在照片之类的，在另外一台 nas 上备份了。

只是前面的这些东西，就这么没了。之前看一部删一部的计划，最终没能实现，现在也不用删除了，自动删除了，一切都灰飞烟灭了。

之前建存储的时候，为了能够使用更多空间，四块硬盘（单盘 4T）组的 shr 阵列，实际可用空间大约 11T 左右，当然，最后电影多的时候还是快能塞满了，这也是为什么之前要看一部删一部了。但是，这稳定性的确让人觉得尴尬，这磁盘阵列，组不组有什么区别？不过回想之前的邮件提示，隐约看到两块硬盘一块出问题的提示。最后还是决定去看看之前的报警信息。

此时再去翻看发的邮件才发现，最开始的时候是11:25硬盘 2 异常断电了。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16651754272805_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16651754272805_.pic_.jpg)

这明显应该不是 nas 本身的问题，是硬盘出问题了。

11:26 分邮件提示，存储已经降级了，降级原因是磁盘2 出现异常。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16671754272807_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16671754272807_.pic_.jpg)

到了 11:27 分提示存储池已经损毁，损毁的原因是 硬盘 1 和硬盘 2。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16661754272806_.pic_-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16661754272806_.pic_.jpg)

然而，硬盘 1 却没收到类似硬盘 2 的提示信息。所以这个异常来自何处，并不清楚。这一下两块硬盘出问题了，也实在是让人绝望。

这种状况不能恢复，也就只能如此了。不过再次重建存储池，还是选择了 shr1，不过这次只用了三块硬盘。剩下的一块硬盘用来做 hot spare。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-214935.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-214935.png)

最终还是把硬盘 2 换成了新的硬盘，不过比较奇怪的是，那块硬盘来回折腾几次之后竟然不提示损毁了。重新插回去会提示未初始化，这尼玛都是什么诡异的情况，做 smart 测试也没任何问题。但是，也不准备再冒险了，最起码 2 先换掉把。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215020-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215020-tuya.jpg)

此时的存储空间只剩了 7.1t，不过这也算够用了，毕竟现在这台 nas 的用处一方面用来当另外一台 nas 的备份，另外就是下载电影，该放的还是要放上面，毕竟之前电视什么的连的还是它，也不想来回折腾了。

另外一台 nas 还是该怎么用继续怎么用吧，毕竟也蛮方便的。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-214941-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-214941-tuya.jpg)

后面就是创建同步备份任务，然而，此时 7.1.1 的系统不支持新系统往旧系统全量备份，最终选择了 rsync 模式。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215003.png)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215003.png)

然而在备份的时候，去官网找 chat 插件，此时翻了下系统版本支持 416j 是有 7.2.2.的固件的，这尼玛，既然有为什么不提示更新？也有可能是国内没有。

https://www.synology.com/zh-tw/support/download/DS416j?version=7.2#system

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250804-103640-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250804-103640.jpg)

同样 chat 套件也是可以下载的：

https://www.synology.com/zh-tw/support/download/DS420+?version=7.2#packages

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250804-103814-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Jietu20250804-103814.jpg)

既然折腾一次，那就折腾彻底吧，直接下载固件，离线升级到最新版。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215726-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-215726-tuya.jpg) 到这里这次折腾算是基本完成了，至于其他的。暂时也不考虑了，能够保持系统稳定就 ok 了。

看到手机上行又一封邮件，提示神马异常登录：

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1668-scaled.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1668.jpg)

点击去发现是需要提交邮箱地址和密码，这尼玛，摆明了就是钓鱼邮件，既然如此，那就毁灭吧。直接上 cursor 写个脚本，给提交点数据。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-183906-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/Screenshot-2025-08-03-183906-tuya.jpg)

开 10000 个进程，发现直接给打死了，还不行，那就开 100 个，慢慢提交吧。

此时也该出发，去陪宝子参加比赛了，其实这种比赛自己也不知有什么用处。三点二十的，磨磨唧唧的到了三点五十才入场。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1663.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1663.jpg) [![](https://h4ck.org.cn/wp-content/uploads/2025/08/16621754272190_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16621754272190_.pic_.jpg)

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1669.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/WechatIMG1669.jpg)

弹奏的曲目《筝萧吟》，这个说实话，自己本来也没听过，在加上熟练度也没那么好。等成绩出来之后，果然不理想。

[![](https://h4ck.org.cn/wp-content/uploads/2025/08/16611754272189_.pic_.jpg)](https://h4ck.org.cn/wp-content/uploads/2025/08/16611754272189_.pic_.jpg)

9.15，整个小组的最低。这也没必要说什么，重在参与，也就这样吧。多次舞台经验而已，

只是今年的钢琴考级，总是觉得有些儿戏。对象也有这个感觉，像报的网球课一样，到现在水平都很一般。甚至连基础的比赛都打不了，而到现在已经两年了，也不知道教练在教些什么。

现在网球课已经停了，准备找新的教练，而钢琴课，似乎也该找新的老师了。网球自己还能陪练，这钢琴又该何去何从，自己单手弹奏还能勉强，双手实在是跟不上，或许，是时候拿出跳绳的毅力来，陪着宝子再开始一起练琴了。这陪练，毕竟没那么简单。

然而，自己都不坚持，又如何能要求孩子坚持？现在陪着宝子写作业，跑步，打球，钢琴在宝子考完三级之后就跟不上了，现在看来得重新开始练了。至少不能拖后腿不是吗？

下午到家之后，发现运行的脚本报错了。显示连接到 127.0.0.1 失败。

http://fun.gededoors.com/?version=ZBkn42yUCMCV5sEIfMyVbeDV9MCa

打开看了下，域名解析给改了，应该是自己打了半天，被发现了，不过，这前端套的 cf，应该是针对这个 token 做了跳转，直接到 127 了。

由于没有别的 token，现在让这个东西彻底灰飞烟灭还有...