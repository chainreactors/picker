---
title: gotenberg html转dpf
url: https://www.yanglong.pro/gotenberg-html%e8%bd%acdpf/
source: 杨龙
date: 2026-08-28
fetch_date: 2026-08-29T08:31:45.038613
---

# gotenberg html转dpf

[跳至正文](#content)

# [杨龙](https://www.yanglong.pro/)

菜单

* [首页](https://www.yanglong.pro/)
* [links](https://www.yanglong.pro/link/)

# gotenberg html转dpf

[发表评论](https://www.yanglong.pro/gotenberg-html%E8%BD%ACdpf/#respond)

## Quick Start

```
docker run --rm -p 3000:3000 gotenberg/gotenberg:8
```

Convert a URL to PDF:

```
curl \
  --request POST http://localhost:3000/forms/chromium/convert/url \
  --form url=https://sparksuite.github.io/simple-html-invoice-template/ \
  -o invoice.pdf
```

## PHP

```
/**
 * 通过file_get_contents发送HTML到Gotenberg转换PDF
 */
private function sendToGotenberg($html)
{
    // 先将HTML写入临时文件
    $tmpFile = tempnam(sys_get_temp_dir(), 'gtb_');
    file_put_contents($tmpFile, $html);

    $postFields = [
        'files' => new \CURLFile($tmpFile, 'text/html', 'index.html'),
        'paperWidth' => '8.27',
        'paperHeight' => '11.7',
        'marginTop' => '0.4',
        'marginBottom' => '0.4',
        'marginLeft' => '0.4',
        'marginRight' => '0.4',
        'waitForExpression' => "document.querySelectorAll('img').length === 0 || Array.from(document.querySelectorAll('img')).every(img => img.complete)",
    ];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, self::GOTENBERG_URL . '/forms/chromium/convert/html');
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $postFields);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
    curl_setopt($ch, CURLOPT_TIMEOUT, 120);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, false);

    $result = curl_exec($ch);
    $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $error = curl_error($ch);
    $errno = curl_errno($ch);
    curl_close($ch);

    @unlink($tmpFile);

    if ($errno !== 0) {
        recordlog("Gotenberg请求失败 [errno={$errno}]: {$error}", 'gotenberg');
        return false;
    }

    if ($httpCode !== 200) {
        recordlog("Gotenberg返回异常 HTTP {$httpCode}: " . substr($result, 0, 500), 'gotenberg');
        return false;
    }

    if (empty($result)) {
        recordlog("Gotenberg返回空响应", 'gotenberg');
        return false;
    }

    return $result;
}
```

本条目发布于[2026年8月28日](https://www.yanglong.pro/gotenberg-html%E8%BD%ACdpf/ "15:58")。属于[Linux](https://www.yanglong.pro/category/linux/)、[PHP](https://www.yanglong.pro/category/php/)分类。作者是[杨龙](https://www.yanglong.pro/author/admin/ "查看所有由杨龙发布的文章")。

### 文章导航

[← PHPDoc 语法大全](https://www.yanglong.pro/phpdoc-%E8%AF%AD%E6%B3%95%E5%A4%A7%E5%85%A8/)

### 发表回复 [取消回复](/gotenberg-html%E8%BD%ACdpf/#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

评论 \*

显示名称 \*

邮箱 \*

网站

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
[![](https://ipv6test.wcode.net/badges/ipv6.svg?host=www.yanglong.pro)](https://ipv6test.wcode.net/?q=www.yanglong.pro)

[粤ICP备2026014361号](https://beian.miit.gov.cn)

[粤公网安备44030002010655号](https://beian.mps.gov.cn/#/query/webSearch?code=44030002010655)

[自豪地采用WordPress](https://cn.wordpress.org/ "优雅的个人发布平台")