---
title: fic2026初赛服务器部分wp
url: https://mp.weixin.qq.com/s/Udz5bglhba2xiGRRA2-DBQ
source: Doonsec's feed
date: 2026-04-28
fetch_date: 2026-04-29T05:07:47.698391
---

# fic2026初赛服务器部分wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SVAhggk0wbwCojFK8UQtFXsrIxeDrkQn7V78muOk86yOeG3mwYed8zqEuPECa1sxRsDvgSCDicth2PyKtYwQfQXFiaJ744viaAXnA4Mk3VSdvk/0?wx_fmt=jpeg)

# fic2026初赛服务器部分wp

原创

老皮皮
老皮皮

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Fic打完了，照例是一塌糊涂，这次全程基本都交给AI，比以往成绩要好（笑），但是因为模型选的不好，中途不停的死掉，挂掉。很糟心，现在用手搓复个盘看看。

火眼服务器仿真会报识别不了，直接选linux就行了，如果还不行，把第二个文件调到上面

启动后会进入一个图形界面，也能打开终端，其实不对劲，当你在终端里用systemctl和ls的时候会发觉有些不对（出题人实在太坏了），其实这个图形界面是在容器里，直接是进了容器里面，所以找不到网站文件的，比赛时候进终端开了ssh，看似一切正常，实则相当离谱。

想直接进到宿主机里其实也很简单，不用逃逸什么的，直接按ctrl+alt+f2就好，没有ssh 直接安装就好

sudoapt install openssh-server

sudosystemctl start ssh

sudosystemctl enable ssh

然后就能用ai来爬了

### 1. 服务器操作系统版本

lsb\_release -a

答案：Debian GNU/Linux 13 (trixie)

### 2. 根分区UUID

vi /etc/fstab

答案：3231e52f-5e15-44c4-b224-e29cb4201c0e

### 3. 最新Docker镜像创建时间

sudo docker ps -a

Sudo docker inspect u22

答案:2026-04-16T07:15:50 （u22:latest镜像）

### 4. 根分区快照路径

sudo btrfs subvolume list /

答案：root/history

### 5. 网站后台入口文件名

/var/www/html/maccms10/下的文件一个个试

答案：user.php （从 admin.php 改名而来，位于 /var/www/html/maccms10/user.php ）

### 6. 网站ICP备案号

直接访问服务器地址，网站页面上有

答案：icp1919810

### 7. 网站主域名

查看网站首页源代码

答案：www.2026fic.forensix

### 8. 分类3的视频拼音名

用第11题的地址，用户名连接数据库，在mac - mac\_type 中即可看到

答案：fenlei3

### 9. 网站设置页面前端模板源文件

AI复盘，注意，这个不是thinkphp预定义的模板

- 后台模板在 application/admin/view/ 目录

- 网站设置页面通常是 system/config.html

- 需要确认是后台模板还是前台模板

答案：/var/www/html/maccms10/application/admin/view/system/config.html

### 10. 伪静态规则配置文件的SM3值

AI复盘，find /var/www/html/maccms10/ -name "maccms.conf" -o -name "\*pseudo\*" -o -name "\*rewrite\*"

答案5a6c86366041509a0a9a31b72a341372182e00f4c9df6a6ae34cc5e779639c54 （文件路径： /var/www/html/maccms10/说明文档/伪静态规则/maccms.conf ）

### 11. 网站数据库IP地址

在网站数据库配置文件里/var/www/html/maccms10/application/database.php mytidb

答案：10.0.3.100 （LXC容器 mytidb，通过 /etc/hosts 解析）

### 12. 数据库容器技术

AI复盘这个容器没听说过，命令lxc-ls

答案：LXC（Linux Container） — mytidb 容器使用 LXC 技术，rootfs 位于 ZFS 数据集 /db/tidb

### 13. 备份数据库版本（4000端口）

AI复盘

ps aux | grep tidb-server

root 2218  2.3  7.0 2255100 283500 ?      Sl   Apr27  31:57 /root/.tiup/components/tidb/v7.5.0/tidb-server -P 4000 --store=tikv --host=0.0.0.0 --status=10080 --path=10.0.3.100:2379 --log-file=/root/.tiup/data/aamac/tidb-0/tidb.log --config=/root/.tiup/data/aamac/tidb-0/tidb.toml

答案：TiDB v7.5.0 （完整版本号：8.0.11-TiDB-v7.5.0）

### 14. 新注册用户最多的日期

SELECT

DATE(FROM\_UNIXTIME(user\_reg\_time)) AS 注册日期,

COUNT(\*) AS 注册人数

FROM mac\_user

WHERE user\_reg\_time IS NOT NULL

GROUP BY 注册日期

ORDER BY 注册人数 DESC

LIMIT 1;

答案：2026-04-15 （36386个新注册用户）

### 15. 用户"马慧美"的最后登录IP

mac\_user里看

答案：51.43.21.163 （在数据库中以拼音形式存储： Ma Hui Mei ，user\_id=4236，user\_last\_login\_ip 对应的 IP 为 51.43.21.163）

### 16. 未使用的文件系统

mount查看

答案：NTFS

### 17. 已安装的数据库服务

AI复盘

# 方法1：查看安装的包

dpkg -l | grep -i "mysql\|mariadb\|postgres\|sqlite\|mongo"

# 方法2：查看运行的服务

systemctl list-units --type=service | grep -i "mysql\|postgres\|mongo"

# 方法3：查看端口

netstat -tlnp | grep -E "3306|5432|27017|6379"

# 方法4：查看可执行文件

which mysql psql mongod redis-server

答案：

- MariaDB Client （1:11.8.6，仅客户端）

- PostgreSQL 17 （服务端+客户端）

- TiDB v7.5.0 （运行在 LXC 容器 mytidb 中，端口3306和4000）

- ZFS （用于存储 TiDB 数据，池名 db）

附记:用的trae.cn(鸣谢谢老师),赛后用三个AI,glm5.1,qwen3.6,deepseek,发现每个AI都有3-4题不能做出来或者有明显的错误,听群友说gpt5.4可以完美打通关。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EsNNx0KLiawZLgs5PZVjW3EsyTjiafk5PickpBNicuMRqgDjnPdYNwfQ0duxXZJs9FNYeD4jX506YtCD09pBEoK9ibQ/0?wx_fmt=png)

老皮的碎碎念念

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EsNNx0KLiawZLgs5PZVjW3EsyTjiafk5PickpBNicuMRqgDjnPdYNwfQ0duxXZJs9FNYeD4jX506YtCD09pBEoK9ibQ/0?wx_fmt=png)

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