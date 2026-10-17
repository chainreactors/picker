---
title: 200 台机器要封 IP， 别再一台台敲
url: https://mp.weixin.qq.com/s/u8D-n8gNVLDxJnOvOha5aA
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:35:03.712512
---

# 200 台机器要封 IP， 别再一台台敲

# 200 台机器要封 IP， 别再一台台敲

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 安全加固 · 运维实战

// 运维加固 · 批量封禁

# 200 台机器要封 IP， 别再一台台敲

封 IP 慢不是手速问题，是把该做哈希表的活，干成了挨个比对

ipsetAnsible批量下发服务器端封禁

🔑 一句话精华

封 IP 慢不是手速问题，是把该做哈希表的活，干成了挨个比对。

![万级黑名单经哈希集合由一条规则生效](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibJo67rRkzmicOzJcIv1NlVXR9A1G2s6wC8TWaDdiapJ7tkibvvypxWV0IIx0iceXp9iaQyJSHG1g1CkSYxjSDp4h5lAdZib5ianBOwmA/640?wx_fmt=png&from=appmsg)

凌晨三点，安全组丢过来一张截图：一台公网服务器被同一个 C 段两万多个 IP 轮番扫描。

一台机器好办。你打开终端，`ipset restore` 一灌，五分钟收工。

那如果是两百台呢？你挨个 SSH 上去敲一遍？等你敲到第 37 台，攻击者已经换了一批 IP。今天这篇就把这条线讲完：为什么 ipset 比堆 iptables 快，单机怎么配，以及怎么用剧本把这些动作按分组一次下发到几百台机器——特别是那些没有防火墙、只能靠服务器自己顶的场景。

## 01ipset 快在哪：一条规则，吃掉两万个 IP

先说清楚为什么不能硬堆。iptables 的规则是线性匹配的，你写一万条 DROP，内核就得按顺序往下比对，包命中最后一条之前要匹配上万次；而且 `-A` 是往链尾追加，每加一条都是 O(n)，脚本批量刷的时候比人还慢。

ipset 是内核里的哈希表。把 IP 塞进一个集合，iptables 只写一条规则引用这个集合，匹配走哈希查找，复杂度接近 O(1)——集合里放十个 IP 还是十万个 IP，查表耗时基本一样。

⏺ Shell · 创建并引用集合

ipset create blacklist hash:net timeout 86400

iptables -I INPUT -m set --match-set blacklist src -j DROP

两万条规则变成一条，转发性能几乎不受影响。

这里有个容量坑先提醒：ipset 默认 `maxelem` 是 65536，超过就直接报 `set is full`，新 IP 加不进去。真要上百万级，建集合时就把容量显式写出来，`hashsize`取略大于 `maxelem` 的 2 的幂能降低哈希碰撞。

⏺ Shell · 百万级容量

ipset create blacklist hash:net maxelem 1200000 hashsize 16384 timeout 86400

## 02单机三件套：批量灌、吃网段、自动解封

第一件是批量灌。别用 `for` 循环一条条 add，那是给 shell 开上万个进程，慢还容易中断。正确姿势是写文件一次 restore：

⏺ Shell · 文件批量导入

ipset create blacklist hash:net timeout 86400

ipset restore -f /etc/ipset.d/blacklist.ipset

文件里一行一条，`add blacklist 1.2.3.0/24`。十万条也就几秒。

第二件是吃网段。用 `hash:net`，一个 `/24` 一条就够，不用把整段拆成 256 个单 IP——这直接把条目数压下来。有人实测过，2000 多个攻击 IP 按前缀聚合并段后，243 条规则压到了 76 条。

第三件是timeout。黑名单最烦的是「封了忘了解」，`timeout` 到点自动过期，不用你写定时任务捞人。临时封一个：

⏺ Shell · 临时封禁一小时

ipset add blacklist 9.9.9.9 timeout 3600

顺手说一句，这几条命令你先收藏，下面讲批量下发时还要用。

## 03从一台到两百台：剧本 + 分组，一次下发

单机搞定了，真正的麻烦才开始——同一个黑名单，怎么让两百台机器都生效，而且不同角色的机器策略不一样？

答案是**剧本（playbook）+ 分组（inventory）**。分组是这件事的核心：按角色分，不按 IP 分。

![控制节点按分组向对外发布机和内网机器下发黑名单](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9Qm9NTcIvzic9Jy84FyTzRxAxKE3WvtK8HAeYOg98BtPribl7Izib0xGcfJXPW0GeRuPqhErP5lmNyfND2MhtqTne4QeWW1yvcPc/640?wx_fmt=png&from=appmsg)

一份典型的分组长这样：

⏺ inventory · 按角色分组

# 对外发布机，全量黑名单

[pub\_web]

web01.example.com

web02.example.com

# 内网机，只封爆破源

[internal]

db01.example.com

然后剧本只做一件事——把黑名单文件推到每台机器，再 restore：

⏺ YAML · 按分组批量下发

- hosts: pub\_web

become: yes

tasks:

- name: 下发黑名单并加载

ansible.builtin.copy:

src: files/blacklist.ipset

dest: /etc/ipset.d/blacklist.ipset

- name: 灌入集合

ansible.builtin.command:

cmd: ipset restore -f /etc/ipset.d/blacklist.ipset

注意两个细节。

第一，用文件 restore，不要用 loop 逐条 add。Ansible 的循环是一条一条发命令过去，两百台机器乘以两万条，跑到明天早上。文件推过去、本机 restore，才是几秒钟的事。

第二，先试跑再落地。剧本加 `--check --diff`，会告诉你「哪些机器会变、变成什么样」，确认没误伤再真跑。这是剧本比手工敲最大的价值：变化可预览、可回溯。

分组真正的意义在策略差异：对外发布机吃全量黑名单，内网机只封爆破源，数据库机连黑名单都不挂、只放行白名单。你手工敲的时候，这个差异是靠人记的；写进分组，它就是配置。

## 04supervisor 管的是另一件事，别搞混

经常有人问：批量管理，是上剧本还是上 supervisor？

两个不是一回事，分工很清楚：

剧本（Ansible）负责「把配置送到每台机器」——一次性动作，跑完就结束；supervisor 负责「让某个进程一直活着」——常驻守护，挂了自动拉起来。

所以 supervisor 该管的是**同步脚本和 fail2ban 这类常驻进程**：比如你写了个脚本定时从情报源拉黑名单再灌 ipset，或者用 fail2ban 把爆破 IP 自动喂进集合，这些进程必须有守护，否则半夜挂了没人知道。

⏺ supervisor.conf · 守护同步脚本

[program:ipset-sync]

command=/usr/local/bin/ipset\_sync.sh

autostart=true

autorestart=true

redirect\_stderr=true

stdout\_logfile=/var/log/ipset-sync.log

配置推给谁、怎么统一分发，还是剧本的活。一句话：剧本管分发，supervisor 管存活。

## 05什么时候必须在服务器端封：没有防火墙的那些场景

前面这套东西，在「上游有防护」的环境里只是补充；但在下面这几种场景里，它是唯一能落地的手段：

![上游拦截优先，无防火墙时服务器端 ipset 兜底](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl8SSTSOBM1jNGAv9aCrNHX0VkAJmibEAW4PZLyRJ5uaxzTY04kttxZicuM9nCyUNapcAD451cYLaGwqOqibYMb2iaofxv2zoW9QdV4/640?wx_fmt=png&from=appmsg)

一是**没有硬件防火墙的托管机**，IDC 托管、机柜里就一台机器，出口没有可管的安全设备，防火墙就是它自己；二是**云安全组不够用**，安全组规则条数有上限，封几十上百个网段还能忍，两万个 IP 根本放不进去；三是**拿不到上游权限**，机器是别人给的、跨账号跨部门，改安全组要走流程，攻击不等人；四是**对外发布机在 CDN 后面**，回源流量已经到源站了，源站还得自己兜一道底；五是**临时应急**，等审批的两小时里，被封的服务已经在掉线。

这几类场景的共同点是：你在服务器上只有 root 权限，没有网络设备的权限。ipset 就是给这种处境准备的——不依赖任何上游设备，改完立刻生效。

⚠️ 但要摆正定位：服务器端封禁是**最后一道**，不是第一道。流量已经打到网卡上了，CPU 该消耗的一分不少。有上游能拦，优先在上游拦。

## 06别把自己封了：四条操作纪律

第一，先放行再封禁。封禁规则必须放在靠前位置，但放行回环和已建立连接的规则要在它前面，否则封完你自己的 SSH 会话就断了。

⏺ Shell · 先放行再封禁

iptables -I INPUT 1 -m state --state ESTABLISHED,RELATED -j ACCEPT

iptables -I INPUT 2 -i lo -j ACCEPT

iptables -I INPUT 3 -m set --match-set blacklist src -j DROP

第二，白名单先行。封 `/24` 之前，先确认这个段里没有你们的 CDN 回源、办公网出口、合作方对接 IP。封 `/16` 更要有人拍板——那是几万个正常 IP 的连带风险。

第三，先封一个，观察十分钟。单 IP 封下去，看流量掉不掉；不掉说明攻击者手里有一堆备用 IP，再考虑升级到网段。别一上来就扔 `/16`。

第四，留好回滚。封禁前把当前规则导出一份备份，脚本里写清楚封禁时间、封禁原因、封了多少条。出事的时候，能一键撤回去比什么都重要。

觉得这套流程有用，先转给你们值班群——半夜真用上的时候，翻聊天记录比翻文档快。

// 老宋说

技术本质：ipset 解决的是匹配效率，剧本解决的是规模一致性，这两件事经常被混为一谈，结果就是有人单机优化得很漂亮，两百台机器上还是靠人手敲，配置早就飘了。

行业观察：我判断接下来运维的分水岭不在会不会写命令，而在能不能把一个动作变成可复用、可预览、可回滚的配置——会敲 ipset 的人很多，能把 ipset 连同分组策略一起下发给两百台机器、还能说清每台机器为什么不一样的人不多。

对读者的建议：今天就做一件事，把你手上那份手工维护的封禁清单，从「某台机器的 iptables 里」挪到「一个受版本管理的 ipset 文件」里，这一小步做完，批量下发才有基础。

推荐阅读

这几篇相关的，建议一并看看：

1. [渗透测试从业者的 CTF 大模型CypherMind：6.4GB 离线跑通夺旗赛](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247487946&idx=3&sn=cc878409acc02ca73a7f59d67c06054f&scene=21#wechat_redirect)

2. [他把一台"滴水不漏"的服务器扫出了 17 个秘密](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486111&idx=1&sn=665315128391f20f3f2b742d33af8839&scene=21#wechat_redirect)

3. [AI 自动打 CTF 又刷屏了 但劝你：先看清楚再上车](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247488327&idx=2&sn=5e14217217b53808095ebf446d06f17f&scene=21#wechat_redirect)

4. [红队工程师的盲区： 你手里的C2，可能正在反控你](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247488307&idx=2&sn=a8fb8660ef9a51b0ab82e6b06466b72e&scene=21#wechat_redirect)

5. [红队工程师：818个安全技能库 正好配CyberStrikeAI](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247488367&idx=1&sn=e546b1d08f88970913db4d761177fa2e&scene=21#wechat_redirect)

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

预览时标签不可点

内容含AI生成图片

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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