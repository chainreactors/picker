---
title: AlmaLinux9.8(EL9)系统下一键脚本安装GrayLog7.2.0最新版本
url: https://mp.weixin.qq.com/s/XfgZr9AEhgLNkRhJMFUNfw
source: Doonsec's feed
date: 2026-10-13
fetch_date: 2026-10-14T06:50:33.826563
---

# AlmaLinux9.8(EL9)系统下一键脚本安装GrayLog7.2.0最新版本

# AlmaLinux9.8(EL9)系统下一键脚本安装GrayLog7.2.0最新版本

原创

yuanfan2012
yuanfan2012

Linux运维实践派

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 1、开源日志平台GrayLog发布了最新版本7.2.0

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWgEG8fxU7nwlk34yulNDKr4bCEdib7Uz0t43ialCBR9ZS3hYx4wwaKVVMJZLyOoecVL7xHXQF4z9N8hxUuNibDfUyNy7iaMRywyLo8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWh0JvJSWw8B2oDEeDhff86JKr8q2I0JjXJicdCj5melIkWy7icA8Ugtew8QppAsh7X3mRWlqNH9xQxBmPClpRGicPneC5j9TyNQK4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWgfIicUCTmlfUBpNMREnicQRD5wQWZLfOqGoepZPPC4IpICReiakuib2pmNLUuK2JMN2DRvNibibUCOR4l5M5enuqKfRic2AD6Q2t2lK8/640?wx_fmt=png&from=appmsg)

## 2、EL9系统下的GrayLog7.2.0一键安装脚本内容如下

```
#!/bin/bash
#关闭SELINUX
sed -i 's/enforcing/disabled/g' /etc/selinux/config
setenforce 0
#解压安装包
mkdir -p /opt/GrayLog_install
tar -zxvf ./GrayLog7.2.0_MongoDB8.2.5_DataNode7.2.0_EL9_RPM.tar.gz -C /opt/GrayLog_install
cat > /etc/yum.repos.d/mongodb-org.repo << \EOF
[mongodb-org-8.2]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/8.2/x86_64/
gpgcheck=0
enabled=1
EOF
cd /opt/GrayLog_install
#安装mongodb-server服务
rpm -ivh cyrus-sasl*.rpm
rpm -ivh mongodb*.rpm

#启动mongodb-server服务
systemctl daemon-reload
systemctl enable mongod.service
systemctl start mongod.service
systemctl --type=service --state=active | grep mongod
firewall-cmd --add-port=27017/tcp --permanent --zone=public
firewall-cmd --reload

#安装graylog-datanode（其内置OpenSearch）
rpm -ivh /opt/GrayLog_install/graylog-datanode-7.2.0-11.x86_64.rpm
#Ensure that the Linux setting vm.max_map_count is set to at least 262144
echo'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.d/99-graylog-datanode.conf
sysctl --system
cat /proc/sys/vm/max_map_count
#根据官方文档openssl rand -hex 32命令随机生成password_secret
#可以自行使用sudo openssl rand -hex 32命令随机生成password_secret并在/etc/graylog/datanode/datanode.conf文件中进行替换
sed -i "s/password_secret =/password_secret = 923d7af5ae3049978a19d328bea02935c2400688222e3b0f0217b6d159af5e47/g" /etc/graylog/datanode/datanode.conf

#修改graylog-datanode中opensearch日志数据存储目录到/data目录下，方便后期扩容
mkdir -p /data/graylog-datanode/opensearch/data
mkdir -p /data/graylog-datanode/opensearch/logs
chown -R graylog-datanode:graylog-datanode /data/graylog-datanode
sed -i "s|opensearch_data_location = /var/lib/graylog-datanode/opensearch/data|opensearch_data_location = /data/graylog-datanode/opensearch/data/|g" /etc/graylog/datanode/datanode.conf
sed -i "s|opensearch_logs_location = /var/log/graylog-datanode/opensearch|opensearch_logs_location = /data/graylog-datanode/opensearch/logs/|g" /etc/graylog/datanode/datanode.conf
systemctl daemon-reload
systemctl enable graylog-datanode.service
systemctl start graylog-datanode.service
#安装graylog-server服务
rpm -ivh  /opt/GrayLog_install/graylog-server-7.2.0-11.x86_64.rpm
cp /etc/graylog/server/server.conf /etc/graylog/server/server.conf_default
#修改graylog-server相关配置文件
sed -i "s/password_secret =/password_secret = 923d7af5ae3049978a19d328bea02935c2400688222e3b0f0217b6d159af5e47/g" /etc/graylog/server/server.conf
sed -i "s/root_password_sha2 =/root_password_sha2 = fdf5e0ba25719d981ae4bd3edd465d71fb91e1d113bdf62a0b0a9963711163ef/g" /etc/graylog/server/server.conf
sed -i "s@#root_timezone = UTC@root_timezone = Asia/Shanghai@g" /etc/graylog/server/server.conf
sed -i "s@#http_bind_address = 127.0.0.1:9000@http_bind_address = 0.0.0.0:9000@g" /etc/graylog/server/server.conf
sed -i "s/allow_highlighting = false/allow_highlighting = true/g" /etc/graylog/server/server.conf
#修改graylog-server启动时JVM内存大小
sed -i "s/-Xms1g -Xmx1g/-Xms2g -Xmx2g/g" /etc/sysconfig/graylog-server

firewall-cmd --add-port=9000/tcp --permanent --zone=public
firewall-cmd --reload
#启动graylog-server服务
systemctl daemon-reload
systemctl restart graylog-server
systemctl enable graylog-server
#请根据最后graylog-server日志文件中的登录账号与密码 浏览器登录Graylog Web界面进行初始化
#tail -f /var/log/graylog-server/server.log | grep "0.0.0.0:9000"
```

安装完成后，根据server.log日志中的初始化密码进行初始化配置

具体步骤参考之前的文章[AlmaLinux9.7(EL9)系统下一键脚本安装GrayLog7.0.5最新版本](https://mp.weixin.qq.com/s?__biz=MzU2MjU1OTE0MA==&mid=2247500138&idx=1&sn=79148ae00576c66e084ec383f93bb725&scene=21#wechat_redirect)

Graylog的登录账号密码为admin/Graylog@2025

## 3、GrayLog7.2.0 EL9一键安装脚本与压缩包下载链接

请添加本文作者微信【yuanfan2012】入群获取

## 4、以下是安装过程部分截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWhq0Ac7X9KZDciabGen7YicEFlO7Uj2G1YIlA9Xdib2g5v4mxhtChcZNPRJEBiaURO9R0U6yQgY5VeytWAgBzAN1RFONKdTibmJevmY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWgQMLkygpt1T7xvcjibTJjwZOxKAic6fYWt2cT9Gy5m854sT3o3jzneW1UJs8hw5XVnb8PHljfd71j0Vldz9dR8ibqWibva3ZV4WP8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWjemcvOYiaV3uPRwHqIcb35U42mic4fMQS68OB5IBYf6wKuQTAL2MhK70l0ibzQN4EhHh6KjFIEOH1vz5BibOhCWvibjKDjZ0YXdzkw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWjF4O0Y1N0EnBKWh7kfGJVCeAuVjDzvr893p2fROGrOtIRicox26QicMkg2pbyG0Ouylcy6p2bo0bibQEnNjBjVY7WPMkQolodicsM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWiaau4oT5xO3SGWGcDiaOupVpbh1KqwIqu5gTwlhlBicWPfwuniaOst3QBO54CoRCZhicE7jAjbFsIOsP6NQlJPqiciaQ8BUamHQdlNjw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWgFeuInWMbC1aOhyg1iaCSeJ6ngVbVYCicKIPTic6ktfvJENLv4Dbx6yeUC9TOu5snzgQDIibDH3jKu5ibOGGub5Rps3e6Lgvo5pKSk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWiaR03T0snw24xtoZmllG7st02iaFzq0EhIlFJ8akHWKcxxnNmvGyRKIa38iciaYqBm5qTZjs2br7DrvIIOONVDmK6e98td7o9KwsI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWhfOp6bUeKXTvWbs2hOALU4Gpbmphgn7Dpoicd68zmV2KmgOhVf1x7ia72AWPgYGYpZiaOb5UoRwkb8Wia7yd43zGeGKbylsmYIgXk/640?wx_fmt=png&from=appmsg)

## 5、Graylog7.2 Collectors新功能测试截图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWjdspTVibCKWZ4pgSJc4oiaBZTpPS5XH9wXxZZd1y2ziab8g4xEHI68VgToRDGGiaNIJqbJSX90ChP2fvNgKX7icTRGBjiatsOIoLQ0k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWjfdlKuqSwsianqqiaE9oulbWdIe33jjYh3iaibdyz06Bo6JRNs7r9YYGGQKGibV3PEPiaFH7BnKUuhqTL98Ro4BTXB4VRmciagxA1ToM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWgw8YbFW6BUod8NmCswFWRVGubSd8KCz3zIKwEEBp4FiaLIM4ROX5Tcdaibtqeh6wVXTx1pg4HY5Ch2YdLY1dU5W5DBxjhaYicicxA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWiaOs5MC8wdDwPXWKXkRhkNsHZ01mJniaJicdwRMJIibJz96tQJK5yALOEjwh4D9cnEeCY70jrCsWH20eic78L8zZYDvICaticqicRnH4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWhlm1H8WnpibeBtSjHPXial6epvkiapf69QvaPibLBiaJ2skMHNNvBqsjNkHyO1aPSk3KibfFAGDgQ95mZc4OYW51kcboG8WpL1ZFcs8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWj8xhwIibzB6xI0RQocFQvXVKic4XOibBfyLdjys8RfvDiclFuA95rtkPCwusZZzMAcW6iczs8FYer24fM5mvSiabTKnb7w1VEibJvlg8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWhvlgibXiboNYeOoyCKdTdicp0dYwjiaKoDRKS9LnyE1jaZ2EuHmRJcP5tWaiaSMFibE5cPIrd1LKo5ibULRPuMstQDBQQJHoNW7V4nEE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWg8NGTcY8eb8O6IiaefqqvIicmpCm2Bvefymcwga7ibZcZ4qKO2mXnrd0OINko3bNLImgJ9BDVfmTV5qYAJ4xgxR7SfOe4KmtcCAE/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n8kWxMqYcWWS0vr9oejHFQdX6f1Bibk8ZkRv5UaViaZjHKTfIbmv2N4ibFebWqCQoHBAo3VY8cgRtHAKYMy7dt8VQ/0?wx_fmt=png)

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