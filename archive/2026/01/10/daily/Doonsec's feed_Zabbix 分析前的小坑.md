---
title: Zabbix 分析前的小坑
url: https://mp.weixin.qq.com/s/0qfKrRz8BzR2Pe91-6CeWw
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:40:20.300901
---

# Zabbix 分析前的小坑

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tiaKRx8m4Wn7EO0B8sibtQNC2zQibrUlNvK5vjrzpXruvTEPt0HC4riaxOCcDA3GToGH7ibm0F44pNs8j509AXibjhcg/0?wx_fmt=jpeg)

# Zabbix 分析前的小坑

原创

Heihu577

Heihu Share

![]()

在小说阅读器中沉浸阅读

# Zabbix 分析前的小坑

最近在分析 zabbix 漏洞时发现官方提供的 docker 比较麻烦, 一些额外的配置比较多, 索然让 AI 给整理了一个 docker compose.

```
version: '3'
services:
  zabbix-mysql:
    image: mysql:5.7  # 4.4版本用5.7更稳定
    restart: always
    container_name: zabbix-mysql-4.4
    environment:
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=zabbix
      - MYSQL_ROOT_PASSWORD=123qwe
    command:
      - mysqld
      - --character-set-server=utf8  # 4.4用utf8而不是utf8mb4
      - --collation-server=utf8_bin
      - --default-authentication-plugin=mysql_native_password
    volumes:
      - /data2/zabbix/db:/var/lib/mysql  # 保持你的路径
      - /etc/localtime:/etc/localtime
    ports:
      - 3306:3306  # 改回标准端口
    networks:
      - zbx_net

  zabbix-server-mysql:
    image: zabbix/zabbix-server-mysql:centos-4.4.0  # 4.4版本
    restart: always
    container_name: zabbix-server-4.4
    volumes:
      - /data2/zabbix/alertscripts:/usr/lib/zabbix/alertscripts  # 保持你的路径
      - /etc/localtime:/etc/localtime
    ports:
      - 10051:10051
    environment:
      - DB_SERVER_HOST=zabbix-mysql
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=zabbix
      - MYSQL_ROOT_PASSWORD=123qwe
    depends_on:
      - zabbix-mysql
    networks:
      - zbx_net

  zabbix-web-nginx-mysql:
    image: zabbix/zabbix-web-nginx-mysql:centos-4.4.0  # 4.4版本
    restart: always
    container_name: zabbix-web-4.4
    environment:
      - DB_SERVER_HOST=zabbix-mysql
      - MYSQL_DATABASE=zabbix
      - MYSQL_USER=zabbix
      - MYSQL_PASSWORD=zabbix
      - PHP_TZ=Asia/Shanghai  # 4.4用PHP_TZ而不是ZBX_SERVER_HOST
    ports:
      - 8080:80  # 4.4内部是80端口，不是8080
    volumes:
      - /etc/localtime:/etc/localtime
      - /data2/zabbix/fonts/DejaVuSans.ttf:/usr/share/zabbix/fonts/graphfont.ttf  # 4.4字体路径不同
      - ./source:/usr/share/zabbix
    networks:
      - zbx_net
    depends_on:
      - zabbix-server-mysql
      - zabbix-mysql

networks:
  zbx_net:
    driver: bridge
```

要注意的是 `zabbix-web-nginx-mysql` 中的 volumes, 这里的`- ./source:/usr/share/zabbix`用于映射源码到宿主机中.

* 如果宿主机不存在`./source`目录那么这行可以先注释掉再启动, 启动完 docker 后使用`docker cp`将源码文件夹复制到`./source`.
* 之后再打开注释再启动 docker compose 即可将docker中的源代码与宿主机进行挂载.

利用 VsCode 的 `Remote SSH` 插件连接上 SSH（宿主机）, 随后定位到宿主机的`./source`目录后再使用 var\_dump 之类的打断点会轻松些, 方便进行调试.

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tiaKRx8m4Wn7XfKiaGtjxIgZSCrf2YKfiazxbsm5FLibgEtLxIDzR5qKlwtSlsTAyXhULneesPRQ8H1cibO0SLDpEwQ/0?wx_fmt=png)

Heihu Share

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tiaKRx8m4Wn7XfKiaGtjxIgZSCrf2YKfiazxbsm5FLibgEtLxIDzR5qKlwtSlsTAyXhULneesPRQ8H1cibO0SLDpEwQ/0?wx_fmt=png)

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