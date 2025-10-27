---
title: 打造自己的云端nas代码
url: https://blog.upx8.com/3111
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:13.018339
---

# 打造自己的云端nas代码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 打造自己的云端nas代码

发布时间:
2022-11-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
17414

本教程使用到的源码
[https://github.com/vitaminx/gd-utils](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL3ZpdGFtaW54L2dkLXV0aWxz)
[https://github.com/iwestlin/gd-utils](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2l3ZXN0bGluL2dkLXV0aWxz)

## 1、申请google无限网盘

[https://td.fastio.me/](https://blog.upx8.com/go/aHR0cHM6Ly90ZC5mYXN0aW8ubWUv)
[https://gd.404edu.workers.dev/](https://blog.upx8.com/go/aHR0cHM6Ly9nZC40MDRlZHUud29ya2Vycy5kZXYv)
[http://leon.educationhost.cloud/](https://blog.upx8.com/go/aHR0cDovL2xlb24uZWR1Y2F0aW9uaG9zdC5jbG91ZC8)

记录下他的ID，网址最后一段

## 2、准备工作

1）一台vps，512内存，干净的机器
2）一个域名，解析到cf（先做，免得后面dns解析慢，连不上机器人）
免费域名申请，可看[https://youtu.be/VdCXgeFL37E](https://blog.upx8.com/go/aHR0cHM6Ly95b3V0dS5iZS9WZENYZ2VGTDM3RQ)
————————————————————————————————————————

## 创建sa，突破750GB限制

升级系统

```
apt update -y &&　apt upgrade -y
```

安装依赖

```
apt install wget curl screen git sudo python3-distutils -y
```

安装python

```
apt install python3 python3-pip -y
```

（由于部分朋友在仓库内找不到 pip/pip3 故提供以下安装方式curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"python3 get-pip.py)

下载并安装 AutoRclone

```
git clone https://github.com/xyou365/AutoRclone && cd AutoRclone && sudo pip3 install -r requirements.txt
```

配置AutoRclone
[https://developers.google.com/drive/api/v3/quickstart/python](https://blog.upx8.com/go/aHR0cHM6Ly9kZXZlbG9wZXJzLmdvb2dsZS5jb20vZHJpdmUvYXBpL3YzL3F1aWNrc3RhcnQvcHl0aG9u)

下载credentials.json

将刚才下载的 credentials.json 文件上传至 ~/AutoRclone 目录下

创建项目

之前没有创建过项目
直接运行：

```
python3 gen_sa_accounts.py --quick-setup 1
```

以上命令含义：

创建1个项目
开启相关的服务
创建100个 service accounts
将100个 service accounts 的授权文件下载到 accounts 文件夹下面

2、已有项目，需要创建新的

```
python3 gen_sa_accounts.py --quick-setup 2 --new-only
```

以上命令含义：

额外创建2个项目（项目N+1到项目N+2）
开启相关的服务
创建200个 service accounts（2个项目，每个项目100个）
将200个 service accounts 的授权文件下载到 accounts 文件夹下面

## 将添加到google无限盘

1.直接加入到用户里面

```
python3 add_to_team_drive.py -d 0AD7rQlWmuc5HUk9PVA
```

2.加入到google群组里面

————————————————————————————————

## 如何搬运

1、直接利用gclone搬运

```
bash <(wget -qO- https://git.io/gclone.sh)
```

记录
/root/AutoRclone/accounts/
/root/AutoRclone/accounts/02db52406f300663f5e6f7b60216616df3e6b869.json

gclone config

特别注意
service\_account\_file 填入以上记下的 .json 文件
service\_account\_file\_path 时，填入 /root/AutoRclone/accounts/

screen
测试用
[https://drive.google.com/drive/folders/12p02xr5EuXoVMvH2H-BTp\_RShBuJnvMx](https://blog.upx8.com/go/aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2RyaXZlL2ZvbGRlcnMvMTJwMDJ4cjVFdVhvVk12SDJILUJUcF9SU2hCdUpudk14)

克隆命令

```
gclone copy a:{12p02xr5EuXoVMvH2H-BTp_RShBuJnvMx} a:测试1 --drive-server-side-across-configs -v
```

## TG机器人搭建

@BotFather
@userinfobot

✅一键脚本使用方法：
只需复制以下链接到VPS命令行窗口粘贴回车即可以执行
✅gdutils项目一键部署脚本（包括“查询转存”和“TG机器人”两部分）

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/vitaminx/gd-utils/master/gdutilsinstall.sh)"
```

✅gdutils项目一键部署脚本之“转存查询部分”

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/vitaminx/gd-utils/master/gdutilscsinstall.sh)"
```

✅gdutils项目一键部署脚本之“TG机器人部分”

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/vitaminx/gd-utils/master/gdutilsbotinstall.sh)"
```

复制sa

```
cd /root/AutoRclone/accounts/

cp -r ./* /root/gd-utils/sa
```

## 挂载emby

```
mkdir -p /home/gdrive

/usr/bin/gclone mount a: /home/gdrive \
 --umask 0000 \
 --default-permissions \
 --allow-non-empty \
 --allow-other \
 --buffer-size 32M \
 --dir-cache-time 12h \
 --vfs-read-chunk-size 64M \
 --vfs-read-chunk-size-limit 1G &
```

查看挂载

```
df -h
```

如果挂载出错

```
apt install fuse -y
```

自动挂载

```
cat > /etc/systemd/system/gclone.service <<EOF
[Unit]
Description=gclone
AssertPathIsDirectory=LocalFolder
After=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/gclone mount a: /home/gdrive \
 --umask 0000 \
 --default-permissions \
 --allow-non-empty \
 --allow-other \
 --buffer-size 32M \
 --dir-cache-time 12h \
 --vfs-read-chunk-size 64M \
 --vfs-read-chunk-size-limit 1G
ExecStop=/bin/fusermount -u LocalFolder
Restart=on-abort
User=root

[Install]
WantedBy=default.target
EOF
```

6、设置启动

```
systemctl start gclone
```

7、开启启动

```
systemctl enable gclone
```

## 安装emby

```
wget https://github.com/MediaBrowser/Emby.Releases/releases/download/4.4.3.0/emby-server-deb_4.4.3.0_amd64.deb

dpkg -i emby-server-deb_4.4.3.0_amd64.deb
```

一键虚拟内存

```
wget https://www.moerats.com/usr/shell/swap.sh && bash swap.sh
```

xxx.xxx.xxx.xxx:8096

## 如果打不开，可能是防火墙没关

```
iptables -F
```

如果你的是contos的系统，有可能是文件权限不够或防火墙没关
服务器防火墙检查

```
firewall-cmd --state
```

关闭防火墙

```
systemctl stop firewalld.service
```

禁止firewall开机启动

```
systemctl disable firewalld.service
```

如果还是无法方位，再查看emby服务器的状态

```
systemctl status emby-server.service
```

没有启动是有个红色的 failed
这个时候去/var/lib/,给emby文件夹权限，777
再启动emby

```
systemctl start emby-server
```

完结，撒花

测试影视搬家
[https://drive.google.com/drive/folders/1uoH-CAENT26YCV0u4rs6SvJF6craQNHM](https://blog.upx8.com/go/aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2RyaXZlL2ZvbGRlcnMvMXVvSC1DQUVOVDI2WUNWMHU0cnM2U3ZKRjZjcmFRTkhN)

[取消回复](https://blog.upx8.com/3111#respond-post-3111)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")