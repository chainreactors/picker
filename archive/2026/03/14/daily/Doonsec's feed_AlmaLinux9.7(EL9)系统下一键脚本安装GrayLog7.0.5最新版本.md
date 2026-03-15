---
title: AlmaLinux9.7(EL9)系统下一键脚本安装GrayLog7.0.5最新版本
url: https://mp.weixin.qq.com/s/vMnCIcr4BFxj1hpPKfxf9w
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:24:42.241387
---

# AlmaLinux9.7(EL9)系统下一键脚本安装GrayLog7.0.5最新版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7W03ib572XWjsbQceq5oGnP8qk4Qk68hu9sNEyxtEptNlMIu58ZUBiao7EFtN53V8c3DppdoIYx08o85r1JuCKW3sxjDaZ8DxKMqbmYRXxF7c/0?wx_fmt=jpeg)

# AlmaLinux9.7(EL9)系统下一键脚本安装GrayLog7.0.5最新版本

原创

yuanfan2012
yuanfan2012

Linux运维实践派

![]()

在小说阅读器中沉浸阅读

## 1、开源日志平台GrayLog发布了最新版本7.0.5

由于官方推荐使用Graylog-Datanode作为Graylog的日志数据节点，其已经内置了OpenSearch2.9.13

且众多网友还是比较倾向于CentOS系的系统

例如RockyLinux9.7及AlmaLinux9.7，因此重新制作了最新的GrayLog7.0.5的EL9系统下的一键安装脚本

其中的主要组件版本信息

* GrayLog7.0.5
* GrayLog-Datanode7.0.5
* MongoDB8.2.5

## 2、EL9系统下的GrayLog7.0.5一键安装脚本内容如下

```
#!/bin/bash
#关闭SELINUX
sed -i 's/enforcing/disabled/g' /etc/selinux/config
setenforce 0
#解压安装包
mkdir -p /opt/GrayLog_install
tar -zxvf ./GrayLog7.0.5_MongoDB8.2.5_DataNode7.0.5_EL9_RPM.tar.gz -C /opt/GrayLog_install
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
rpm -ivh /opt/GrayLog_install/graylog-datanode-7.0.5-2.x86_64.rpm
#Ensure that the Linux setting vm.max_map_count is set to at least 262144
echo 'vm.max_map_count=262144' | sudo tee -a /etc/sysctl.d/99-graylog-datanode.conf
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
rpm -ivh  /opt/GrayLog_install/graylog-server-7.0.5-2.x86_64.rpm
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

以上脚本是针对RHEL9.X/CentOS9.X等EL9系列系统的一键安装脚本

## 3、使用一键脚本进行安装

将如下脚本与压缩包上传到AlmaLinux9.X或RockyLinux9.X系统的同一个目录下`GrayLog7.0.5_MongoDB8.2.5_DataNode7.0.5_EL9_RPM.tar.gz``GrayLog7.0.5_Datanode7.0.5_MongoDB8.2.5_EL9_install.sh`aaa

然后sh GrayLog7.0.5\_Datanode7.0.5\_MongoDB8.2.5\_EL9\_install.sh 执行一键安装脚本即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWgjgPiaeibSgFrtcaNJG78XIfRfCKXhvGMTZ7Jky3yQ9D7BNMIptRX8sZTkJiazT848ygYwp2cBk1J9ntjYdbibyRnkbvAHln9Z2kI/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

下面是安装过程的截图

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWg5W6ibAvg1kicY53icDacP8HtRabacHkJjNmjO0Blia7DRYTjU2rX1sfZGxu9gqQt7zjmicEk8clgQ5IHl9I5RI9JsjQ4OmOSQdq6o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWgJOcs0HekLVspA654jOmMeSkOUtMIaNlPK0uGoiaLaMAWepEvoibvzE2uAg7WNnO4xqjVr4pyhS3LM0kOpwWvibolqTibX7ZOqKZo/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

## 4、初始化

tail -f /var/log/graylog-server/server.log

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWjnA9BricUjKR0HpwicvfoHMqhVqK2bKyDlFK4q8Ly7ZJzsn95WyZyNC6cYO4qLEEfeEAMaicfZDK1h9r45cMhcLrkczt6ala8cww/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

## 5、Web登录Graylog7.0.5

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWjuKwBx9W1UYHuX5mtYpmxMXYibUTArtgpdPhTDQk6409nptgGxcK2f99BmqgUVNNSDH4HoNz3aAQGSjlpbeSJF6AsrxmNIiaibnQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWgMREWAv9uXPFH39TCkR74xpb8H8LT3Wp7mm1ibu07A1T5cxn50PibrdZeJiaibJRRbiaVzKJzrSD5xKQRYHib9SzetcUE5r57s92c6c/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWiacibJzqBKibcPyU8bAWhlVJUapZia6ibQNxmOsa5J4VejS53XiaVoFDJ2CFiavt8baMB7jQvRibdAFTlrIGMp6XnN0UpMNdpBPwMqlxg/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWj0wfDIgc2zGtXfCyyAFmHJU836E8zcQbL7umUgHEfLYmIFx5sZeCQwQDREPa1YL7JYh6GhTdwgygD96rKc7fNLIO2L9nuicbUI/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWjl47kqic1ajwrOzLaITkp0WpNT4ibq4kNeQ4nKHOlktIRyyYSKu4KR0OXnbx0QvoatqzCbcJ9DGzjSUd50hHQyI5Wdp3Wj7pH1k/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

安装完成后Graylog的登录账号密码为admin/Graylog@2025

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWjythpCmsBF7IQwYIct830pUFyTfNI3fwc9hFFCiaCF6WZu5WcOL8kSaAJP8Oe03OOI5XTFPsnhBovdD6NgWqic3TGue89P4xia1Q/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

![](https://mmbiz.qpic.cn/mmbiz_png/7W03ib572XWiaNaLG3WQIM99FDgEy79YcjeWJDYcRWs8u6fAo3fFYt672zbo8ibtJBlswjGMRur72oIjRfraU7IleAfEsGE6EWO0AzsS1jCERU/640?wx_fmt=png&from=appmsg)

**(图片点击放大查看)**

## 6.脚本获取方式

GrayLog7.0.5 EL9一键安装脚本与压缩包下载链接请在添加本文作者微信【yuanfan2012】入群获取

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n8kWxMqYcWWS0vr9oejHFQdX6f1Bibk8ZkRv5UaViaZjHKTfIbmv2N4ibFebWqCQoHBAo3VY8cgRtHAKYMy7dt8VQ/0?wx_fmt=png)

Linux运维实践派

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