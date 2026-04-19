---
title: 【优化篇】shell脚本实现GrayLog配置的定期备份
url: https://mp.weixin.qq.com/s/VIOENrt_kHogNaJ8S3aIgw
source: Doonsec's feed
date: 2026-04-18
fetch_date: 2026-04-19T04:47:57.395829
---

# 【优化篇】shell脚本实现GrayLog配置的定期备份

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7W03ib572XWg9BFrWSth4n6H0e3sP2VRHCSDbMZuJZfjAG6niaxUl2lnlG4f8xAjX9G7jxjVNZKVoRVQF9kUWqTTPDttSOgXqqMhUvwxuCIqQ/0?wx_fmt=jpeg)

# 【优化篇】shell脚本实现GrayLog配置的定期备份

原创

yuanfan2012
yuanfan2012

Linux运维实践派

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/7W03ib572XWiaqSWOHyTU5FaPu2LHKSlt0VApiaR34CUkE8P3WgYj7sUZGcqR5Kp1Rn4RebG1TELjHHpBZlLSYjfmQTXJZUdkYvicyxEnmFK9go/640?wx_fmt=jpeg&from=appmsg)

## 1、优化解决的问题点

[shell脚本实现GrayLog配置的定期备份](https://mp.weixin.qq.com/s?__biz=MzU2MjU1OTE0MA==&mid=2247498093&idx=1&sn=9f43ac217eff18247c33d425b63c9cb7&scene=21#wechat_redirect)

在上面这个之前的文章所使用的脚本基础上，进行了优化，为了解决几个问题

* 1、需要备份/opt目录

PrometheusAlert 以及webhook服务、和一些常用联动的脚本均在此目录下

* 2、备份一下/etc/graylog/server/目录
* 3、由于Graylog可能在其他局点，与本地的NAS服务器之间的带宽有限，为了不占用专线的带宽，使用`sshpass+rsync`命令的方式对/opt目录备份时只需要进行增量差异同步即可，不必每次都重新传输备份一次/opt目录

## 2、优化后的具体脚本

/opt/graylog\_mongodb\_backup.sh

```
#!/bin/bash
# LOCK_FILE文件路径
LOCK_FILE=/var/log/mongodb_backup_record.log
# 钉钉机器人 Webhook URL
WEBHOOK_URL="https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXXXX"
# 获取当前日期作为变量
current_datetime=$(date +"%Y-%m-%d_%H_%M_%S")
#current_date=$(date +"%Y-%m-%d")
# 定义备份目录和文件名
backup_dir="/home/graylog_mongodb_backup"
backup_file="graylog_mongodb_backup$current_datetime"

# MongoDB 连接参数
#mongodb_host="localhost"
#mongodb_user="graylog"
#mongodb_password=""
mongodb_database="graylog"

# NAS_IP及 目标路径
nas_ip="192.168.31.100"
nas_username="nasadmin"
nas_target_dir="/volume1/FileServer/GraylogBackup/192.168.31.74"
nas_ssh_port="22"
nas_ssh_Password="XXXXXXXXX"
# 创建备份目录
mkdir -p "$backup_dir"

# 备份 MongoDB 数据库
#mongodump -h "$mongodb_host" -u "$mongodb_user" -p "$mongodb_password" -d "$mongodb_database" -o "$backup_dir"  >> ${LOCK_FILE} 2>&1
mongodump  -d "$mongodb_database" -o "$backup_dir"  >> ${LOCK_FILE} 2>&1

# 检查mongodump 命令是否执行成功
if [ $? -eq 0 ]; then
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
    echo"MongoDB backup completed successfully." >> ${LOCK_FILE} 2>&1
else
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
    echo"Error occurred while performing MongoDB backup." >> ${LOCK_FILE} 2>&1
    exit 1
fi

# 打包备份文件为 tar.gz 格式
cd$backup_dir
tar -zcvf /tmp/"$backup_file.tar.gz"  graylog >> ${LOCK_FILE} 2>&1

# 检查打包命令是否执行成功
if [ $? -eq 0 ]; then
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
    echo"Backup files compressed successfully." >> ${LOCK_FILE} 2>&1
else
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
        echo"Error occurred while compressing backup files." >> ${LOCK_FILE} 2>&1
    exit 1
fi

# 上传备份文件到 NAS
current_time=$(date +"%Y-%m-%d %H:%M:%S")
sshpass -p $nas_ssh_Password  rsync -avzP scp  -r -P "$nas_ssh_port" /opt "$nas_username@$nas_ip:$nas_target_dir" >> ${LOCK_FILE} 2>&1
sshpass -p $nas_ssh_Password  rsync -avzP scp  -r -P "$nas_ssh_port" /etc/graylog/server "$nas_username@$nas_ip:$nas_target_dir" >> ${LOCK_FILE} 2>&1

sshpass -p $nas_ssh_Password scp  -P "$nas_ssh_port" /tmp/"$backup_file.tar.gz""$nas_username@$nas_ip:$nas_target_dir" >> ${LOCK_FILE} 2>&1
# 检查上传命令是否执行成功
if [ $? -eq 0 ]; then
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
    echo"Backup files uploaded to NAS successfully." >> ${LOCK_FILE} 2>&1
    echo"备份文件上传成功，发送dingding通知"  >> ${LOCK_FILE} 2>&1
    notify_message="【通知】：Graylog服务器<font color=#FF0000> IP:($(hostname -I))</font> 的MongoDB数据库备份文件已上传至NAS <font color=#FF0000>IP:($nas_ip) </font>。\n\n【备份文件上传时间】：<font color=#FF0000> $current_time </font>\n\n【备份文件上传路径及文件名称】：<font color=#FF0000>$nas_target_dir/$backup_file.tar.gz</font>"
    echo$notify_message  >> ${LOCK_FILE} 2>&1
    curl -s -H "Content-Type: application/json" -d "{\"msgtype\":\"markdown\",\"markdown\":{\"title\":\"通知\",\"text\":\"$notify_message\"}}""$WEBHOOK_URL"  >> ${LOCK_FILE} 2>&1
# 删除临时备份文件和目录
    rm -rf "$backup_dir" >> ${LOCK_FILE} 2>&1
    rm /tmp/"$backup_file.tar.gz" >> ${LOCK_FILE} 2>&1
else
    echo `date +"%Y-%m-%d %H:%M:%S"`  >> ${LOCK_FILE} 2>&1
    echo"Error occurred while uploading backup files to NAS.">> ${LOCK_FILE} 2>&1
# 删除临时备份目录
    rm -rf "$backup_dir" >> ${LOCK_FILE} 2>&1
    exit 1
fi
```

## 说明

* 1、需要提前yum install sshpass组件
* 2、NAS要开启rsync服务
* 3、然后再配置crontab定时任务

```
 crontab -l
# 每天 2:00 进行备份
0 3 * * *    /opt/graylog_mongodb_backup.sh
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWgJdwyJsCa3x72JqXb8zuX60RRGSeo7ErLvXCEVFFzzMn1IvZf96zo0OpD4jsnibxnccCBkXAocSgCAGEpicsJwhmibcYL6K1fjx4/640?wx_fmt=png&from=appmsg)

## 4、最终的效果如截图所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/7W03ib572XWgUMaHVhvBLIAjFUgp8DDqQx6WPwHExdOahEAcic8hyhVo0VponfcfOqpVubBkG549s8lyJicANibJ75NUPBCBwica3XsxDmjU3cYY/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

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