---
title: [原创]学习Kubernetes笔记——部署web站点环境（PHP+Nginx）
url: https://buaq.net/go-143567.html
source: unSafe.sh - 不安全
date: 2023-01-01
fetch_date: 2025-10-04T02:50:21.979620
---

# [原创]学习Kubernetes笔记——部署web站点环境（PHP+Nginx）

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

![]()

[原创]学习Kubernetes笔记——部署web站点环境（PHP+Nginx）

kind: Service apiVersion: v1 metadata:   name: php-fpm-nginx spec:  type: NodePort   selector:     a
*2022-12-31 14:56:54
Author: [bbs.pediy.com(查看原文)](/jump-143567.htm)
阅读量:30
收藏*

---

`kind: Service`

`apiVersion: v1`

`metadata:`

`name: php``-``fpm``-``nginx`

`spec:`

`type``: NodePort`

`selector:`

`app: php``-``fpm``-``nginx`

`ports:`

`-` `port:` `80`

`protocol: TCP`

`targetPort:` `80`

`-``-``-`

`kind: ConfigMap`

`apiVersion: v1`

`metadata:`

`name: nginx``-``config`

`data:`

`nginx.conf: |`

`user  nginx;`

`worker_processes  auto;`

`error_log` `/``var``/``log``/``nginx``/``error.log notice;`

`pid` `/``var``/``run``/``nginx.pid;`

`events {`

`worker_connections` `1024``;`

`}`

`http {`

`include` `/``etc``/``nginx``/``mime.types;`

`default_type  application``/``octet``-``stream;`

`log_format  main` `'$remote_addr - $remote_user [$time_local] "$request" '`

`'$status $body_bytes_sent "$http_referer" '`

`'"$http_user_agent" "$http_x_forwarded_for"'``;`

`access_log` `/``var``/``log``/``nginx``/``access.log  main;`

`sendfile        on;`

`keepalive_timeout` `65``;`

`server {`

`listen` `80` `default_server;`

`listen [::]:``80` `default_server;`

`root` `/``var``/``www``/``html;`

`index index.php index.html;`

`server_name _;`

`if` `(``-``f $request_filename``/``index.html) {`

`rewrite (.``*``) $``1``/``index.html` `break``;`

`}`

`if` `(``-``f $request_filename``/``index.php) {`

`rewrite (.``*``) $``1``/``index.php;`

`}`

`if` `(!``-``f $request_filename) {`

`rewrite (.``*``)` `/``index.php;`

`}`

`location` `/` `{`

`try_files $uri $uri``/` `=``404``;`

`}`

`location ~ \.php$ {`

`include fastcgi_params;`

`fastcgi_param REQUEST_METHOD $request_method;`

`fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;`

`fastcgi_pass` `127.0``.``0.1``:``9000``;`

`}`

`}`

`include` `/``etc``/``nginx``/``conf.d``/``*``.conf;`

`}`

`-``-``-`

`kind: StatefulSet`

`apiVersion: apps``/``v1`

`metadata:`

`name: php``-``fpm``-``nginx`

`spec:`

`selector:`

`matchLabels:`

`app: php``-``fpm``-``nginx`

`replicas:` `3`

`template:`

`metadata:`

`labels:`

`app: php``-``fpm``-``nginx`

`spec:`

`containers:`

`-` `name: php``-``fpm`

`image: ai3666191``/``php``-``fpm:ameng`

`imagePullPolicy: IfNotPresent`

`livenessProbe:`

`initialDelaySeconds:` `5`

`periodSeconds:` `10`

`tcpSocket:`

`port:` `9000`

`readinessProbe:`

`initialDelaySeconds:` `5`

`periodSeconds:` `10`

`tcpSocket:`

`port:` `9000`

`resources:`

`requests:`

`memory:` `"64Mi"`

`cpu:` `"250m"`

`limits:`

`memory:` `"128Mi"`

`cpu:` `"500m"`

`ports:`

`-` `containerPort:` `9000`

`volumeMounts:`

`-` `mountPath:` `/``var``/``www``/``html`

`name: nginx``-``www`

`lifecycle:`

`postStart:`

`exec``:`

`command: [``"/bin/sh"``,` `"-c"``,` `"echo startup..."``]`

`preStop:`

`exec``:`

`command:`

`-` `sh`

`-` `'-c'`

`-` `sleep` `5` `&& kill` `-``SIGQUIT` `1`

`-` `name: nginx`

`image: nginx`

`imagePullPolicy: IfNotPresent`

`livenessProbe:`

`initialDelaySeconds:` `5`

`periodSeconds:` `10`

`httpGet:`

`path:` `/`

`port:` `80`

`readinessProbe:`

`initialDelaySeconds:` `5`

`periodSeconds:` `10`

`httpGet:`

`path:` `/`

`port:` `80`

`resources:`

`requests:`

`memory:` `"64Mi"`

`cpu:` `"250m"`

`limits:`

`memory:` `"128Mi"`

`cpu:` `"500m"`

`ports:`

`-` `containerPort:` `80`

`volumeMounts:`

`-` `mountPath:` `/``var``/``www``/``html`

`name: nginx``-``www`

`-` `mountPath:` `/``etc``/``nginx``/``nginx.conf`

`subPath: nginx.conf`

`name: nginx``-``config`

`lifecycle:`

`preStop:`

`exec``:`

`command:`

`-` `sh`

`-` `'-c'`

`-` `sleep` `5` `&&` `/``usr``/``sbin``/``nginx` `-``s quit`

`volumes:`

`-` `name: nginx``-``www`

`nfs:`

`path:` `/``k8s``/``html``/`

`server: nfs`

`-` `name: nginx``-``config`

`configMap:`

`name: nginx``-``config`

文章来源: https://bbs.pediy.com/thread-275687.htm
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)