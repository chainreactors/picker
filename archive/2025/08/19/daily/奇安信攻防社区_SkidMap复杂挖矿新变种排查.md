---
title: SkidMap复杂挖矿新变种排查
url: https://forum.butian.net/share/4497
source: 奇安信攻防社区
date: 2025-08-19
fetch_date: 2025-10-07T00:12:37.090560
---

# SkidMap复杂挖矿新变种排查

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### SkidMap复杂挖矿新变种排查

* [安全管理](https://forum.butian.net/topic/54)

本次应急响应遇到入行以来排查过的最复杂挖矿——SkidMap。直接击穿我脆弱的知识体系，前后搞了很久才定性并清理，多亏网上前人公开的分析文章才让我能一步步溯源。故将排查内容整理出来，成为下一个前人供同行继续前进。

现象定性：
=====
top 一切正常，但是 CPU 爆满：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1182b7fe411da92e2449560fccedcf36a83c9851.png)
netstat -tunp 看见一个可疑外联，但是似乎并没有建立连接，无法定位其 PID 进程，那就没法定位执行文件了：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-461dc58f273570670758b969c4d1dff409ededb0.png)
上微步上看是恶意外联，确认中了病毒。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-46756391c96e6ae0e204ae9f4162c70ffbebae8e.png)
用 tcpdump 查看一下外联域名，涉及多个域名：c443.softgoldinformation.com、c80.softgoldinformation.com、log.softgoldinformation.com
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-78422686eaff04379072f7078e16631073aebaca.png)
根据威胁情报，明确是一个叫做 SkidMap 家族的挖矿病毒。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-1b6c29767cc7a4e2758676444a2b7a8d3bfe808c.png)
开始排查：
=====
到这里我还没意识到问题的严重性，依旧以为是普通的挖矿病毒，按照常规方式进行排查
\*\*根据外连信息进行排查\*\*
第一个想法，按照以往的思维通过 lsof -i:port 定位连接中的进程，但是每一次运行 netstat -tunp 时显示的端口都不一样，根据以往的经验，可能是连接并没有建立，就是所以恶意程序是由计划任务或母体程序持续拉起的，每次尝试连接后，如果失败就退出，然后换一个进程。如果成功就建立连接，然后由于互斥体的存在就只能有一个进程。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f0dedae81ff02cd7268f49a48a1112e276f4dcdb.png)
由于怀疑进程是持续重启的，通信端口转瞬即逝，所以写个批处理命令在 tcpdump 捕获到端口的同时通过 lsof -i: 或 ss 来截获并输出，但是都无所获：
```js
sudo tcpdump -i any udp port 53 -n -l | \
awk '/softgoldinformation\.com/ {
split($3, a, ".");
ip = a[1]"."a[2]"."a[3]"."a[4];
port = a[5];
addr = ip ":" port;
if (addr != "8.8.8.8:53") {
sub(/:$/, "", addr);
print port;
system("lsof -iUDP:" port);
}
}'
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
sudo tcpdump -i any udp port 53 -n -l | \
awk '/softgoldinformation\.com/ {
split($3, a, ".");
ip = a[1]"."a[2]"."a[3]"."a[4];
port = a[5];
addr = ip ":" port;
if (addr != "8.8.8.8:53") {
sub(/:$/, "", addr);
print "Port: " port;
system("ss -lunp | grep \":" port "\"");
}
}'
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-5d9d4e510db6034d35df8136ca5d41c690c5a93f.png)
\*\*尝试其它排查线索：\*\*
常规排查计划任务，一无所获：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-bde2065290c2866bc690a55aaffac973d926d064.png)
排查系统服务，也没看出个所以然：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-e37484f257576d871e770a4dbc659e9d72b38910.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-a75693f15534656f6e123b233401f12f8f8b13a0.png)
查看 Linux “预加载库”配置文件，看是否存在内核 HOOK：包括 LD\\_PRELOAD 环境变量、root 用户设置、是否被加入了全局配置、/etc/ld.so.preload 文件，结果都没有发现。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-fe350242cbb97c14fb071e001915baae4d6d6c1c.png)
保险起见下个 rkhunter 排查一下，也没发现什么 rookit
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-334305f1f5d1a248e38d9411b281b4b5a321a8e6.png)
最后用 unhide 看下有没有什么隐藏进程，发现还是没有：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f4592bde4f783e0921123fecf879d1f5790bab8b.png)
至此陷入一个困境，怎么定位到发出这个 \\*.softgoldinformation.com 连接的进程。
\*\*资料收集\*\*
========
卡住之后就开始全网搜集资料了，把微步上的域名网页资料都点了个遍，后来发现根本不够用，网页上的博客要不就讲得太简略了，要不就排查方式对不上：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-f3cbfe59a3e483e7f1a03c5ca44153f036855c46.png)
最后搜罗全网，发现微信公众号的文章比较多且质量高，列出相关文章如下：
Linux | 揭秘SkidMap Rootkit复杂挖矿活动（二）
<https://mp.weixin.qq.com/s/wlpZ1zfKjtA2YUspTse60w>
Linux | 揭秘SkidMap Rootkit复杂挖矿活动（一）
[https://mp.weixin.qq.com/s/BwIKcuVJ3VpEa0sPXhbV\\\\_A](https://mp.weixin.qq.com/s/BwIKcuVJ3VpEa0sPXhbV%5C\_A)
记一次挖矿病毒的溯源
<https://mp.weixin.qq.com/s/kbGSMhHm32LntUlsxpS1bw>
SkidMap病毒利用Redis未授权访问漏洞攻击，数千台云主机沦为矿机
[https://mp.weixin.qq.com/s/r6ix1nubOdtA7pyUwJ\\\\_4Sw](https://mp.weixin.qq.com/s/r6ix1nubOdtA7pyUwJ%5C\_4Sw)
Linux | SkidMap 内核态 Rootkit 取证分析
<https://mp.weixin.qq.com/s/NOSlERGuBrACP3q0S3VwfQ>
Linux Rootkit对抗无从下手？LinuxAR给出答案
[https://mp.weixin.qq.com/s/nGpe5\\\\_E1pw4C6rdT9dKfSQ](https://mp.weixin.qq.com/s/nGpe5%5C\_E1pw4C6rdT9dKfSQ)
服务器真的没有异常吗？挖矿病毒Skidmap伪造CPU使用率
<https://mp.weixin.qq.com/s/LR6TFxPfNrQC9faAH5hEBg>
根据博客手法定性
--------
在[安全狗威胁情报中心的博客](https://unsafe.sh/go-139148.html)中发现排查入口点是挂载点，但是执行 findmnt 时并没有文章提到的现象。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-2288edbcc90c319b29e0b28a8a69311a591903d4.png)
在 TahirSec 的博客[Linux | 揭秘SkidMap Rootkit复杂挖矿活动（一）](https://mp.weixin.qq.com/s/BwIKcuVJ3VpEa0sPXhbV\_A) 中发现 netstat 行为一致，是本次事件相似度最高的文章了，但是它用到了深信服的 LinuxAR 工具，我并没有。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-4ebf69c56d1eb44138a5e36df11662b0cd9108e1.png)
然后就懵了，也不知道是不是这篇博客上的样本逻辑，最后通读全文，测了一下 ssh，才最终确认是这篇博客写的，但是一个变种，很多行为对不上了
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-42a7af9c9e2adf81d006b433831b5b24d3629d7b.png)
继续测试一下，确认 rootkit 被加载了，reviews 文件无法展示，但是用绝对路径能访问到，尝试了 busybox 也不行，当然这也是因为病毒 rootkit 做了排查工具的对抗。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-2ac334816149151c489aa3df238e7925af4e1985.png)
如何卸载驱动？
=======
后面操作基本按照 [Linux | 揭秘SkidMap Rootkit复杂挖矿活动（二）](https://mp.weixin.qq.com/s/wlpZ1zfKjtA2YUspTse60w) 来排查了，先是替换了系统命令 rm 为 cp，希望拦截所有删除文件的操作来得到样本进行分析，但也只拿到部分文件如 mcpuinfotest.ko 和 kmeminfotest.ko 这两个驱动文件。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-ae299d7b95ae47d3b84eb716f0a09a505e58019c.png)
释放它的母体 reviews 和 mldconfigs 死活拿不到，怀疑是没有调用系统的 rm 命令，后来也从释放得 systemdtest-udeved.xxxxx 程序也证实了调用的是 remove() 底层函数 !
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-7daeff5385422d163e2588cc8438f0d5c5f778d9.png)
systemdtest-udeved.xxxx 的执行逻辑
后来想了想既然它是开机自动释放——执行——删除的，既然拦不住它的删除操作，是否可以在它删除之前 copy 一份到别的地方呢？只要能拿到母体 reviews mldconfigs 就能拿到后面大部分文件了，于是写入如下的系统服务，后来干脆加上 rm -f 删除它使 cpu 先降低下来从而没那么卡。
```js
/usr/local/bin/clean\_targets.sh
#!/bin/bash
while true; do
cp -f /usr/bin/reviews ~/rev
cp -f /usr/bin/mldconfigs ~/mld
rm -f /usr/bin/reviews
rm -f /usr/bin/mldconfigs
done
/etc/systemd/system/clean-targets.service
[Unit]
Description=Clean Targets Script
After=network.target
[Service]
ExecStart=/usr/local/bin/clean\_targets.sh
Restart=always
User=root
Group=root
StandardOutput=null
StandardError=null
[Install]
WantedBy=multi-user.target
```
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-6e274b0939e3cf70f19a13bb09bcfc8eb6093a96.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-7fd4763d8c3f5dc1b6a8d1a4a6aaa066971671d2.png)
reviews 和 mldconfigs 分析
=======================
reviews|mldconfigs 有着同样的 hash，该变种比前面提到的文章还多替换了一个 sshd 文件，并且替换文件后时间戳对齐原始 ssh 的时间戳。这三个被替换文件的执行时机分别是：ssh——登录远程服务器时手动执行(非开机自启动)、scp——远程拷贝文件时手动执行(非开机自启动)、sshd——开启 ssh 服务时执行（开机启动）
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-c8a54c08634e55a7cef88308362c5aeb2197c2a1.png)
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/07/attach-66cdc9f8999ee1a81134e2eaebf2fbeb1dce4b14.png)
其中 ssh 逻辑变化了一点，从原来的明文 /usr/include/olog.h 变成了 bash64 加密方式，scp 同理，其它像 sshd 的并没有细看。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/0...