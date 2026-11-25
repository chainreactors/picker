---
title: 26数证杯初赛-服务器wp
url: https://mp.weixin.qq.com/s/Semp9Y_DJG9Q051vAb3veA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:38:55.740633
---

# 26数证杯初赛-服务器wp

# 26数证杯初赛-服务器wp

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

服务器题难度也不高，第一题感觉是在放水，都可以静态分析搞定。所有都只给提示，不给出答案了

"比对附件《线索视频.mp4》的画面、文字和配音，确定服务器内与其对应的完整导出视频。该视频文件名是什么？提交格式：仅填写视频文件名，包含小写扩展名，不含目录，如 sample.mp4。",

/engine/output/stock  下面的直接看一下，文字一致，基本确定，注意下，网站下面也有个一样的，但是题目问的是导出视频

 "第1题目标成片生成任务的本地工作台登录账号是什么？提交格式：仅填写工作台登录账号，保留原始大小写，如 admin\_test",

跟着上一题 找到/engine/stock\_worker/workbench.db 看runs表和users表

 "已知案发服务器IPv4地址为172.23.194.128，查明目标成片在本地工作台生成的完整HTTP分享链接，包含协议、地址、端口和完整分享标识。提交格式：填写完整HTTP URL，不加尾部斜杠或查询参数，如 http://192.168.10.20:8080/s/a1b2c3d4e5f6。",

 workbench.db数据库  shares表  material\_edit只有一个共享 share\_id 为859e2b811ee7

打开server.py  ThreadingHTTPServer(('0.0.0.0',8392)  端口为8392

if not self.path.startswith('/s/'):return self.reply({'error':'Not found'} 目录为s 拼接下

 "目标成片首次通过分享链接被下载的最早时间是多少？换算为北京时间，精确到秒。",

downloads表中 share\_id为 859e2b811ee7 completed 为1 的记录  2026-11-14T15:43:52.874215+00:00  加8小时

 "服务器上有一份素材Q-218的授权说明已被删除。恢复该文件，写出其中的授权编号。提交格式：仅填写授权编号，如 LIC-000-0000。",

火眼查看所有的图片，可以看到有license\_Q-219.png license\_Q-220.png，要做签名恢复，用qiko则直接可以看到这张图片

 "已知工作流草稿目录最新一次提交的内容曾被改写。请找出改写前那次提交的工单号。提交格式：仅填写工单号，如 AB-0001。",

/home/fleish/workflow\_drafts/下有个.git目录，查看它下面的 /home/fleish/workflow\_drafts/.git/logs/refs/heads/master

这一题有点糊涂，不知道是什么

看了别人的wp也没弄清楚，希望有个佬来说明白一点

 "/etc/fstab中，挂载到/opt/vsynth的卷以UUID标识。该UUID对应的LVM逻辑卷名称是什么？提交格式：仅填写逻辑卷名，如data-lv",

qiko直接能看到  ，火眼要绕个圈子，先查UUID再去日志里搜索。希望火眼能改进一下，嘿嘿

 "服务器上nginx站点，其server\_name配置的域名是什么？提交格式：仅填写域名，如 www.example.com。",

/etc/nginx/sites-available/wh-promo.conf

 "MySQL数据库wms的出库单表outbound\_order中，发货日期为2026-11-14的一批出库单，仓库编码被事后统一改成了SELF。还原改动前的数据，提交被修改的出库单数量。提交格式：仅填写整数，如 10。",

根据 /var/lib/mysql/ 下的binlog 恢复删除日志，查找UPDATE\_ROWS 事件

如果要用官方工具mysqlbinlog，还要启动一个linux环境，而且我们的目的不是还原是，查找，所以，这里推荐一个离线工具

```
pymysqlbinlog 是分析/解析binlog的开源工具, 使用GPL-3.0 license项目地址: https://github.com/ddcw/pymysqlbinlog
```

将/var/lib/mysql/binlog.000001 ~ 00003，都导出来，

```
py main.py  C:\temp\binlog\binlog.000002 --sqlDELIMITER /*!*/;ROLLBACK  /*!*/;SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by ddcw pymysqlbinlog */ /*!*/;SET TIMESTAMP=1794912006 /* QUERY TIME 2026-11-17 18:40:06 */ /*!*/;SET @@session.sql_mode=1168113696 /*!*/;SET @@session.character_set_client=255, @@session.collation_connection=255, @@session.collation_server=255 /*!*/;/*!80011 SET @@session.default_collation_for_utf8mb4=255*//*!*/;USE wms /*!*/;CREATE DATABASE wms DEFAULT CHARACTER SET utf8mb4/*!*/;COMMIT /* XID 7 added by ddcw pymysqlbinlog*/ /*!*/;
SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by ddcw pymysqlbinlog */ /*!*/;SET TIMESTAMP=1794912006 /* QUERY TIME 2026-11-17 18:40:06 */ /*!*/;SET @@session.sql_mode=1168113696 /*!*/;SET @@session.character_set_client=255, @@session.collation_connection=255, @@session.collation_server=255 /*!*/;/*!80011 SET @@session.default_collation_for_utf8mb4=255*//*!*/;USE ['wms'] /*!*/;CREATE TABLE wms.outbound_order ( id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, order_no VARCHAR(24) NOT NULL, warehouse_code VARCHAR(16) NOT NULL, qty INT NOT NULL, shipped_at DATETIME NOT NULL, KEY idx_shipped (shipped_at)) ENGINE=InnoDB/*!*/;COMMIT /* XID 8 added by ddcw pymysqlbinlog*/ /*!*/;
SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by ddcw pymysqlbinlog */ /*!*/;SET TIMESTAMP=1794912006 /* QUERY TIME 2026-11-17 18:40:06 */ /*!*/;SET @@session.sql_mode=1168113696 /*!*/;SET @@session.character_set_client=255, @@session.collation_connection=255, @@session.collation_server=255 /*!*/;/*!80011 SET @@session.default_collation_for_utf8mb4=255*//*!*/;BEGIN/*!*/;INSERT INTO `wms`.`outbound_order` values(1, 'OB20261112-0001', '3PL-HX', 5, '2026-11-12 8:0:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(2, 'OB20261112-0002', 'SELF', 12, '2026-11-12 8:17:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(3, 'OB20261112-0003', '3PL-HX', 19, '2026-11-12 8:34:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(4, 'OB20261112-0004', '3PL-SF', 26, '2026-11-12 8:51:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(5, 'OB20261112-0005', 'SELF', 33, '2026-11-12 9:8:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(6, 'OB20261112-0006', '3PL-SF', 40, '2026-11-12 9:25:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(7, 'OB20261112-0007', 'SELF', 7, '2026-11-12 9:42:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(8, 'OB20261112-0008', 'SELF', 14, '2026-11-12 9:59:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(9, 'OB20261112-0009', '3PL-HX', 21, '2026-11-12 10:16:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(10, 'OB20261112-0010', 'SELF', 28, '2026-11-12 10:33:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(11, 'OB20261112-0011', '3PL-SF', 35, '2026-11-12 10:50:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(12, 'OB20261112-0012', '3PL-HX', 42, '2026-11-12 11:7:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(13, 'OB20261112-0013', '3PL-SF', 9, '2026-11-12 11:24:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(14, 'OB20261112-0014', '3PL-HX', 16, '2026-11-12 11:41:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(15, 'OB20261112-0015', '3PL-HX', 23, '2026-11-12 11:58:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(16, 'OB20261112-0016', '3PL-SF', 30, '2026-11-12 12:15:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(17, 'OB20261112-0017', '3PL-HX', 37, '2026-11-12 12:32:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(18, 'OB20261112-0018', 'SELF', 44, '2026-11-12 12:49:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(19, 'OB20261112-0019', '3PL-HX', 11, '2026-11-12 13:6:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(20, 'OB20261112-0020', '3PL-SF', 18, '2026-11-12 13:23:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(21, 'OB20261112-0021', '3PL-HX', 25, '2026-11-12 13:40:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(22, 'OB20261112-0022', 'SELF', 32, '2026-11-12 13:57:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(23, 'OB20261112-0023', 'SELF', 39, '2026-11-12 14:14:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(24, 'OB20261112-0024', '3PL-HX', 6, '2026-11-12 14:31:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(25, 'OB20261112-0025', 'SELF', 13, '2026-11-12 14:48:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(26, 'OB20261112-0026', 'SELF', 20, '2026-11-12 15:5:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(27, 'OB20261112-0027', '3PL-HX', 27, '2026-11-12 15:22:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(28, 'OB20261112-0028', '3PL-HX', 34, '2026-11-12 15:39:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(29, 'OB20261112-0029', 'SELF', 41, '2026-11-12 15:56:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(30, 'OB20261112-0030', 'SELF', 8, '2026-11-12 16:13:0')/*!*/;COMMIT /* 9 added by ddcw pymysqlbinlog*/ /*!*/;
SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by ddcw pymysqlbinlog */ /*!*/;SET TIMESTAMP=1794912006 /* QUERY TIME 2026-11-17 18:40:06 */ /*!*/;SET @@session.sql_mode=1168113696 /*!*/;SET @@session.character_set_client=255, @@session.collation_connection=255, @@session.collation_server=255 /*!*/;/*!80011 SET @@session.default_collation_for_utf8mb4=255*//*!*/;BEGIN/*!*/;INSERT INTO `wms`.`outbound_order` values(31, 'OB20261113-0001', 'SELF', 8, '2026-11-13 8:0:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(32, 'OB20261113-0002', '3PL-HX', 15, '2026-11-13 8:15:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(33, 'OB20261113-0003', 'SELF', 22, '2026-11-13 8:30:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(34, 'OB20261113-0004', 'SELF', 29, '2026-11-13 8:45:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(35, 'OB20261113-0005', '3PL-SF', 36, '2026-11-13 9:0:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(36, 'OB20261113-0006', '3PL-HX', 43, '2026-11-13 9:15:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(37, 'OB20261113-0007', '3PL-HX', 10, '2026-11-13 9:30:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(38, 'OB20261113-0008', 'SELF', 17, '2026-11-13 9:45:0')/*!*/;INSERT INTO `wms`.`outbound_order` values(39, 'OB20261113-0009', '3PL-HX', 24, '2026-11-13 10:0:0')/*...