---
title: Ubuntu 22禁用apt和snap自动升级
url: http://blog.nsfocus.net/ubuntu-22/
source: 绿盟科技技术博客
date: 2022-11-08
fetch_date: 2025-10-03T21:56:28.285610
---

# Ubuntu 22禁用apt和snap自动升级

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Ubuntu 22禁用apt和snap自动升级

### Ubuntu 22禁用apt和snap自动升级

[2022-11-07](https://blog.nsfocus.net/ubuntu-22/ "Ubuntu 22禁用apt和snap自动升级")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 2,282

## 一、背景介绍

突然SystemTap、crash、eBPF都不太正常，无意中发现”uname -r”从5.15.0-48-generic升到5.15.0-50-generic，坑我。很多研究性质的VM并不想自动升级，包括安全补丁，应该禁用自动升级。

## 二、禁用apt相关的自动升级

参看

Disable Automatic Updates on Ubuntu 22.04 Jammy Jellyfish Linux – Korbin Brown [2022-04-21]
https://linuxconfig.org/disable-automatic-updates-on-ubuntu-22-04-jammy-jellyfish-linux

$ cat /etc/apt/apt.conf.d/20auto-upgrades
APT::Periodic::Update-Package-Lists “1”;
APT::Periodic::Unattended-Upgrade “1”;

这是缺省内容，改成

APT::Periodic::Update-Package-Lists “0”;
APT::Periodic::Download-Upgradeable-Packages “0”;
APT::Periodic::AutocleanInterval “0”;
APT::Periodic::Unattended-Upgrade “0”;

上面是CLI方式，也可以GUI禁用。

Software & Updates
Updates
Automatically check for updates
Daily (Default)
Never
When there are security updates
Download and install automatically (Default)
Display immediately
When there are other updates
Display weekly (Default)
Display every two weeks
Notify me of a new Ubuntu version
For long-term support versions (Default)
Never

## 三、处理snap相关的自动升级

上面只是禁用了Ubuntu 22与apt相关的自动升级，还有与snap相关的自动升级需要处理，比如snap版Firefox、Opera会每天升级，病得不轻。无法正常禁止snap自动升级，但有一些非常规手段，参[2]、[3]。

此处不讨论为何不卸载snap，只对付一种情形，既想用snap又不想让它自动升级。无此需求者，请绕行。

1) 禁用snapd

————————————————————————–
systemctl stop snapd.service
systemctl disable snapd.service
systemctl status snapd.service

systemctl enable snapd.service
systemctl start snapd.service
systemctl status snapd.service
snap refresh
————————————————————————–

“stop+disable”不够狠，启动Firefox时会自动启动snapd，必须”stop+mask”禁用之。

————————————————————————–
systemctl stop snapd.service
systemctl mask snapd.service
systemctl status snapd.service

systemctl unmask snapd.service
systemctl start snapd.service
systemctl status snapd.service
snap refresh
————————————————————————–

“stop+mask”之后，snapd禁得死死的，但同时无法启动Firefox，不符预期。

2) /etc/hosts (未测试)

127.0.0.1 api.snapcraft.io
127.0.0.1 search.apps.ubuntu.com

iptables -A OUTPUT -d api.snapcraft.io -j DROP
iptables -A OUTPUT -d search.apps.ubuntu.com -j DROP

3) metered connection

Settings
Network
Wired
Details
Metered connection: has data limits or can incur charges
On

此时软件升级或其他较大流量的下载操作不会自动启动，但snap需要额外设置

snap set system refresh.metered=hold

正常情况下snap自动升级最多暂停90天。

4) 与refresh相关的snap配置

参[4]，snapd缺省每天4次检查更新，神经病啊，可以更改这种BT行为。

————————————————————————–
snap refresh

手动强制更新

snap refresh –time

查看更新计划

snap refresh –unhold firefox

Removed general refresh hold of “firefox”

snap refresh –unhold

Removed auto-refresh hold on all snaps
————————————————————————–
snap set system refresh.timer=fri5,14:00-14:05
snap set system refresh.hold=”$(date –iso-8601=seconds -d ‘today+100 days’)”
snap set system refresh.metered=hold
snap set system refresh.retain=2
snap set core experimental.refresh-app-awareness=true

可以unset

snap get system refresh.timer
snap get system refresh.hold
snap get system refresh.metered
snap get system refresh.retain
snap get core experimental.refresh-app-awareness

snap get -d system

查看全部配置
————————————————————————–
refresh.timer

每月最后一个周五的14:00-14:05开始更新，旧版可能是

snap set core refresh.schedule=fri5,14:00-14:05

refresh.hold

将更新推迟指定天数，官方文档[4]说最长90天，为什么我测下来有95天？

refresh.metered

NetworkManager检测到”metered connection”时暂停snap更新

refresh.retain

保持最新的2个版本

experimental.refresh-app-awareness

避免升级正在运行中的软件
————————————————————————–
import time

def delta ( day1, day2 ) :
sec1 = int( time.mktime( time.strptime( day1, “%Y-%m-%d” ) ) )
sec2 = int( time.mktime( time.strptime( day2, “%Y-%m-%d” ) ) )
return ( sec2 – sec1 ) // 60 // 60 // 24
#
# end of delta
#

print( delta( “2022-11-4”, “2023-2-7” ) )
————————————————————————–

5) 人工修改last-refresh

$ snap refresh –time
timer: fri5,14:00-14:05
last: today at 12:22 CST
hold: 2023-02-07
next: in 21 days, at 14:00 CST (but held)

$ snap refresh –time
timer: fri5,14:00-14:05
last: yesterday at 12:22 CST
hold: 2023-02-07
next: in 20 days, at 14:00 CST (but held)

next值反映了timer值，2022.11.25是本月最后一个周五。

hold值有上限，从last开始计数，不超过90天(官方说辞)。我在2022.11.4有过last-refresh，当天设置refresh.hold推迟更新100天，snap根据各种阈值计算后允
许推迟至2023.2.7。在2022.11.5再次设置refresh.hold推迟更新100天，无效，hold值停留在2023.2.7。

参[2]，Alan Pope曾经用crontab每天定时设置refresh.hold，以此推迟更新。若只是这样操作，至少现在已无法永久推迟更新，因为last值不会更新。参[3]，据说
snap配置文件中的”last-refresh”值只在snapd进行”automatic refresh”时得到更新，”manually refresh”不会更新该值，未验证该说法。

snap配置文件是”/var/lib/snapd/state.json”，里面有个

“last-refresh”:”2022-11-04T12:22:49.342452532+08:00″,

这就是last值所在，可以人工修改该值。

$ date +%Y-%m-%dT%H:%M:%S.%N%:z2022-11-05T14:10:37.971117940+08:00

$ date –iso-8601=ns2022-11-05T14:10:41,633708955+08:00

$ date –rfc-3339=ns2022-11-05 14:11:39.756739004+08:00

仔细看上述三种输出，第一种与”last-refresh”的格式完全一样，第二种秒与纳秒之间是逗号，第三种年月日与时分秒之间没有T。

6) defer\_snap\_update.sh

该脚本人工修改snap配置文件中的”last-refresh”，再设置refresh.hold。只要定期执行该脚本，即可不断推迟更新，不受90天的硬限制。

————————————————————————–
#!/bin/bash
systemctl stop snapd
jq -c “.data[\”last-refresh\”] = \”$(date +%Y-%m-%dT%H:%M:%S.%N%:z)\”” /var/lib/snapd/state.json > /tmp/state.json
mv /tmp/state.json /var/lib/snapd/state.json
chmod 600 /var/lib/snapd/state.json
systemctl start snapd
snap set system refresh.hold=”$(date –iso-8601=seconds -d ‘today+100 days’)”
snap refresh –time
————————————————————————–

$ ./defer\_snap\_update.sh
timer: fri5,14:00-14:05
last: today at 14:17 CST
hold: 2023-02-08
next: in 20 days, at 14:00 CST (but held)

7) 自编译snapd (未测试)

参[2]，Alan Pope有演示，但这个太重型了，我不喜欢。

☆ 参考资源

[1] Disable Automatic Updates on Ubuntu 22.04 Jammy Jellyfish Linux – Korbin Brown [2022-04-21]
https://linuxconfig.org/disable-automatic-updates-on-ubuntu-22-04-jammy-jellyfish-linux

[2] Disabling snap Autorefresh – Alan Pope [2021-05-29]
https://popey.com/blog/2021/05/disabling-snap-autorefresh/

[3] How to disable autorefresh in snap – [2017-06-30]
https://askubuntu.com/questions/930593/how-to-disable-autorefresh-in-snap

https://github.com/snapcore/snapd/blob/master/tests/lib/tools/snapd-state
(有个prevent\_autorefresh函数)

[4] Managing updates
https://snapcraft.io/docs/keeping-snaps-up-to-date
https://forum.snapcraft.io/t/managing-updates/7022
(后者更详细)

Getting started
https://snapcraft.io/docs/getting-started

Experimental feature: snap refresh awareness and update inhibition – Igor Ljubuncic [2020-02-27]
https://snapcraft.io/blog/experimental-feature-snap-refresh-awareness-and-update-inhibition

System options
https://forum.snapcraft.io/t/system-options/29860

Setting system options
https://forum.snapcraft.io/t/setting-system-options/87

****声明****

本安全公告仅用来描述可能存在的安全问题，绿盟科技不为此安全公告提供任何保证或承诺。由于传播、利用此安全公告所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，绿盟科技以及安全公告作者不为此承担任何责任。

绿盟科技拥有对此安全公告的修改和解释权。如欲转载或传播此安全公告，必须保证此安全公告的完整性，包括版权声明等全部内容。未经绿盟科技允许，不得任意修改或者增减此安全公告内容，不得以任何方式将其用于商业目的...