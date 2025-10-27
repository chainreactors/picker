---
title: 构建支持Swoole、Kafka 扩展，运行 PHP 环境的 Docker 镜像
url: https://buaq.net/go-162587.html
source: unSafe.sh - 不安全
date: 2023-05-10
fetch_date: 2025-10-04T11:37:20.721366
---

# 构建支持Swoole、Kafka 扩展，运行 PHP 环境的 Docker 镜像

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/dab7f12764c199f98bcbc9d175b65b10.jpg)

构建支持Swoole、Kafka 扩展，运行 PHP 环境的 Docker 镜像

构建支持Swoole、Kafka 扩展，运行PHP环境的Docker 镜像Hyperf 框架官方提供了内置 Swoole 的 Docker 构建模板，最
*2023-5-9 23:48:0
Author: [blog.upx8.com(查看原文)](/jump-162587.htm)
阅读量:33
收藏*

---

![](https://eller.tech/storage/images/Hq4ELfR1Kg8EPs23S75EZW1ORYiwWSMXOVC9wXn2.png)

构建支持Swoole、Kafka 扩展，运行PHP环境的Docker 镜像

Hyperf 框架官方提供了内置 Swoole 的 Docker 构建模板，最新已经支持到了PHP8，另外也可以通过参数指定版本去构建自己的镜像。

Dockerfile 可以在 GitHub 获取：https://github.com/hyperf/hyperf-docker

现成镜像也可以到 Docker Hub 获取：https://hub.docker.com/r/hyperf/hyperf

克隆项目

```
git clone https://github.com/hyperf/hyperf-docker.git
cd hyperf-docker
```

默认可以通过 build.sh 构建所有版本镜像

```
chmod+x build.sh && ./build.sh build
```

但大多数情况下，我们只需要其中一个镜像就足够了，例如 alpine 基础的 PHP7.4 支持 Swoole 的运行环境.

```
export PHP_VERSION=7.4 && export ALPINE_VERSION=3.14 && export SW_VERSION=4.7.1 && docker-compose build alpine-swoole
```

上面的命令通过环境变量设定 PHP 的版本号，基础系统的版本和 SWOOLE 的版本号，最终通过 docker-compose.yml 配置中预设的 alpine-swoole 配置去构建镜像，也可以在配置中查看所需参数。

配置如下：

```
  # swoole image
  alpine-swoole:
    image: "hyperf/hyperf:${PHP_VERSION}-alpine-v${ALPINE_VERSION}-swoole-${SW_VERSION}"
    build:
      context: "${PHP_VERSION}/alpine/swoole"
      args:
        ALPINE_VERSION: ${ALPINE_VERSION}
        SW_VERSION: ${SW_VERSION}
        COMPOSER_VERSION: ${COMPOSER_VERSION}
```

它会调用 ${PHP\_VERSION}/alpine/swoole 目录下的 Docker 去进行构建任务。

也就是：7.4/alpine/swoole/Dockerfile

此时如果我们需要增加 支持 Kafka 扩展，就改这个 Dockerfile 就好了。

官方有示例：

```
RUN apk add --no-cache librdkafka-dev \
&& pecl install rdkafka \
&& echo "extension=rdkafka.so" > /etc/php7/conf.d/rdkafka.ini
```

你需要将他加入到合适的地方，还需要补充安装 pecl （php7-dev php7-pear），否则 Kafka 无法安装。

这是我最终的完整配置：

```
# hyperf/hyperf:7.4
#
# @link     https://www.hyperf.io
# @document https://doc.hyperf.io
# @contact  [email protected]
# @license  https://github.com/hyperf/hyperf/blob/master/LICENSE

ARG ALPINE_VERSION

FROM hyperf/hyperf:7.4-alpine-v${ALPINE_VERSION}-base

LABEL maintainer="Hyperf Developers <[email protected]>" version="1.0" license="MIT"

ARG SW_VERSION
ARG COMPOSER_VERSION

##
# ---------- env settings ----------
##
ENV SW_VERSION=${SW_VERSION:-"v4.5.7"} \
    COMPOSER_VERSION=${COMPOSER_VERSION:-"2.0.2"} \
    #  install and remove building packages
    PHPIZE_DEPS="autoconf dpkg-dev dpkg file g++ gcc libc-dev make php7-dev php7-pear pkgconf re2c pcre-dev pcre2-dev zlib-dev libtool automake"

# update
RUN set -ex \
    && apk update \
    # for swoole extension libaio linux-headers
    && apk add --no-cache libstdc++ openssl git bash \
    && apk add --no-cache --virtual .build-deps $PHPIZE_DEPS libaio-dev openssl-dev curl-dev \
    # download
    && cd /tmp \
    && curl -SL "https://github.com/swoole/swoole-src/archive/${SW_VERSION}.tar.gz" -o swoole.tar.gz \
    && ls -alh \
    # php extension:swoole
    && cd /tmp \
    && mkdir -p swoole \
    && tar -xf swoole.tar.gz -C swoole --strip-components=1 \
    && ln -s /usr/bin/phpize7 /usr/local/bin/phpize \
    && ln -s /usr/bin/php-config7 /usr/local/bin/php-config \
    && ( \
        cd swoole \
        && phpize \
        && ./configure --enable-openssl --enable-http2 --enable-swoole-curl --enable-swoole-json \
        && make -s -j$(nproc) && make install \
    ) \
    && echo "memory_limit=1G" > /etc/php7/conf.d/00_default.ini \
    && echo "opcache.enable_cli = 'On'" >> /etc/php7/conf.d/00_opcache.ini \
    && echo "extension=swoole.so" > /etc/php7/conf.d/50_swoole.ini \
    && echo "swoole.use_shortname = 'Off'" >> /etc/php7/conf.d/50_swoole.ini \
    # rdkafka
    && apk add --no-cache php7-dev php7-pear \
    && apk add --no-cache \
    librdkafka-dev \
    && curl -O https://pear.php.net/go-pear.phar \
    && php go-pear.phar \
    && pecl install rdkafka \
    && echo "extension=rdkafka.so" > /etc/php7/conf.d/rdkafka.ini \
    # install composer
    && wget -nv -O /usr/local/bin/composer https://github.com/composer/composer/releases/download/${COMPOSER_VERSION}/composer.phar \
    && chmod u+x /usr/local/bin/composer \
    # php info
    && php -v \
    && php -m \
    && php --ri swoole \
    && composer \
    # ---------- clear works ----------
    && apk del .build-deps \
    && rm -rf /var/cache/apk/* /tmp/* /usr/share/man /usr/local/bin/php* \
    && echo -e "\033[42;37m Build Completed :).\033[0m\n"
```

文章来源: https://blog.upx8.com/3535
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)