---
title: MySQL导入远程数据库
url: https://www.yanglong.pro/%e8%bf%9c%e7%a8%8b%e5%af%bc%e5%85%a5%e6%95%b0%e6%8d%ae%e5%ba%93/
source: 杨龙
date: 2026-03-06
fetch_date: 2026-03-07T03:55:35.665573
---

# MySQL导入远程数据库

[跳至正文](#content)

# [杨龙](https://www.yanglong.pro/)

菜单

* [首页](https://www.yanglong.pro/)
* [links](https://www.yanglong.pro/link/)

# MySQL导入远程数据库

[发表评论](https://www.yanglong.pro/%E8%BF%9C%E7%A8%8B%E5%AF%BC%E5%85%A5%E6%95%B0%E6%8D%AE%E5%BA%93/#respond)

```
mysqldump -h 123.3.3.3 --compress --single-transaction --quick -u OOOK -pPP01 OOOK | mysql -h 127.0.0.3 -u OOOK -pPP01 OOOK
127.0.0.3 适用于连接 OOOK@%
--quick 用于省内存
--compress 用于压缩传输
--single-transaction 防止锁库
```

本条目发布于[2026年3月6日](https://www.yanglong.pro/%E8%BF%9C%E7%A8%8B%E5%AF%BC%E5%85%A5%E6%95%B0%E6%8D%AE%E5%BA%93/ "下午2:29")。属于[MySQL](https://www.yanglong.pro/category/mysql/)分类。作者是[杨龙](https://www.yanglong.pro/author/admin/ "查看所有由杨龙发布的文章")。

### 文章导航

[← 为什么basename丢失中文？](https://www.yanglong.pro/%E4%B8%BA%E4%BB%80%E4%B9%88basename%E4%B8%A2%E5%A4%B1%E4%B8%AD%E6%96%87%EF%BC%9F/)

### 发表回复 [取消回复](/%E8%BF%9C%E7%A8%8B%E5%AF%BC%E5%85%A5%E6%95%B0%E6%8D%AE%E5%BA%93/#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

Math Captcha
 − 6 = 3

Powered by [MathCaptcha](https://wordpress.org/plugins/wp-advanced-math-captcha)

搜索

搜索

[502](https://www.yanglong.pro/tag/502/)
[certbot](https://www.yanglong.pro/tag/certbot/)
[composer](https://www.yanglong.pro/tag/composer/)
[docker](https://www.yanglong.pro/tag/docker/)
[ElasticSearch](https://www.yanglong.pro/tag/elasticsearch/)
[Flask-RESTful](https://www.yanglong.pro/tag/flask-restful/)
[flex](https://www.yanglong.pro/tag/flex/)
[gizp](https://www.yanglong.pro/tag/gizp/)
[goaccess](https://www.yanglong.pro/tag/goaccess/)
[GuzzleHttp](https://www.yanglong.pro/tag/guzzlehttp/)
[InnoDB存储引擎](https://www.yanglong.pro/tag/innodb%E5%AD%98%E5%82%A8%E5%BC%95%E6%93%8E/)
[javascript](https://www.yanglong.pro/tag/javascript/)
[jdk](https://www.yanglong.pro/tag/jdk/)
[laravel](https://www.yanglong.pro/tag/laravel/)
[lru](https://www.yanglong.pro/tag/lru/)
[LVM](https://www.yanglong.pro/tag/lvm/)
[make](https://www.yanglong.pro/tag/make/)
[mongodb](https://www.yanglong.pro/tag/mongodb/)
[MySQL](https://www.yanglong.pro/tag/mysql/)
[mysql 函数大全](https://www.yanglong.pro/tag/mysql-%E5%87%BD%E6%95%B0%E5%A4%A7%E5%85%A8/)
[nginx](https://www.yanglong.pro/tag/nginx/)
[nginx gzip](https://www.yanglong.pro/tag/nginx-gzip/)
[openssl](https://www.yanglong.pro/tag/openssl/)
[php-fpm](https://www.yanglong.pro/tag/php-fpm/)
[pt-online-schema-change](https://www.yanglong.pro/tag/pt-online-schema-change/)
[python](https://www.yanglong.pro/tag/python/)
[RabbitMQ](https://www.yanglong.pro/tag/rabbitmq/)
[redis](https://www.yanglong.pro/tag/redis/)
[RESTful](https://www.yanglong.pro/tag/restful/)
[rockylinux](https://www.yanglong.pro/tag/rockylinux/)
[SELinux](https://www.yanglong.pro/tag/selinux/)
[shell](https://www.yanglong.pro/tag/shell/)
[slave](https://www.yanglong.pro/tag/slave/)
[solr](https://www.yanglong.pro/tag/solr/)
[SQL\_SLAVE\_SKIP\_COUNTER](https://www.yanglong.pro/tag/sql_slave_skip_counter/)
[Supervisor](https://www.yanglong.pro/tag/supervisor/)
[swoole](https://www.yanglong.pro/tag/swoole/)
[web.py](https://www.yanglong.pro/tag/web-py/)
[WebService](https://www.yanglong.pro/tag/webservice/)
[X-Forwarded-For](https://www.yanglong.pro/tag/x-forwarded-for/)
[xfs](https://www.yanglong.pro/tag/xfs/)
[xml](https://www.yanglong.pro/tag/xml/)
[Zend Studio](https://www.yanglong.pro/tag/zend-studio/)
[弹性布局](https://www.yanglong.pro/tag/%E5%BC%B9%E6%80%A7%E5%B8%83%E5%B1%80/)
[慢查询](https://www.yanglong.pro/tag/%E6%85%A2%E6%9F%A5%E8%AF%A2/)

### 其他操作

* [登录](https://www.yanglong.pro/wp-login.php)
* [条目 feed](https://www.yanglong.pro/feed/)
* [评论 feed](https://www.yanglong.pro/comments/feed/)
* [WordPress.org](https://cn.wordpress.org/)

### 交流讨论群

[![PHP开发技术交流](//pub.idqqimg.com/wpa/images/group.png "PHP开发技术交流")](https://qm.qq.com/cgi-bin/qm/qr?k=83kWH9ed7-t8BXB5zh3uDC2TfJdNtSJj&jump_from=webapi)

[![Flag Counter](data:image/bmp;base64...)](https://info.flagcounter.com/Egb7)
[![本站支持IPv6访问](https://static.ipw.cn/icon/ipv6-s3.svg)](https://ipw.cn/ipv6webcheck/?site=www.yanglong.pro "本站支持IPv6访问")

[粤ICP备2026014361号](https://beian.miit.gov.cn)

[粤公网安备44030002010655号](https://beian.mps.gov.cn/#/query/webSearch?code=44030002010655)

[自豪地采用WordPress](https://cn.wordpress.org/ "优雅的个人发布平台")