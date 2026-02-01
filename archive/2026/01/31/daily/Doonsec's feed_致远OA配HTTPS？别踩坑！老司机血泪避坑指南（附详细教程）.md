---
title: 致远OA配HTTPS？别踩坑！老司机血泪避坑指南（附详细教程）
url: https://mp.weixin.qq.com/s/ngNvDo_qxCGmOqUS7J1ozQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:23:17.555011
---

# 致远OA配HTTPS？别踩坑！老司机血泪避坑指南（附详细教程）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TEnldia9cPN8G51Fk3ia9zxDnatpdxSdu5d9a9qkIc4f6qeh0OSLiaS7avs7YJgliaF3DVGpBlELGMQCnTnGZsH72A/0?wx_fmt=jpeg)

# 致远OA配HTTPS？别踩坑！老司机血泪避坑指南（附详细教程）

原创

谢谢您哦
谢谢您哦

OA大助手

![]()

在小说阅读器中沉浸阅读

马到功成

马上有钱

平安吉祥

马年鸿运

![](https://mmbiz.qpic.cn/mmbiz_png/Mqliame43BvlcEyz2qicttuhNwJuEkDDhX5wztz2vRdicnE6RSMXo168iacb3WYczcTBYQGW7Fd3bJuXhIdK2ZzaZQ/640?wx_fmt=png)

马上来财

马上快乐

马上健康

马上躺赢

![](https://mmecoa.qpic.cn/mmecoa_png/wQsJPqtAJ8Bmsks36ichneCESzicULrVssJqCRrEWyJvV9eCyWEHQawiaEiaIl3PzetsniaQrog4hZmV2z1ooeqCo2w/640?wx_fmt=png)

**点击蓝字 关注我们**

“配个HTTPS，踩坑踩到怀疑人生！”——作为致远OA从7.1用到9.1的“资深受害者”，今天必须把这份避坑秘籍分享给各位同行！从证书申请到配置落地，手把手教你避开那些官方文档没写的坑，省下时间多摸鱼不香吗？

**导语**

**一、**

**HTTPS配置：本该10分钟的事，为啥成了“技术马拉松”？**

但问题来了：致远OA配HTTPS真不是“申请证书就能用”，官方文档模糊，社区教程老旧（尤其9.1版本），稍不注意就卡在证书校验、端口配置或反向代理上…

* **证书申请容易，部署踩坑多：**致远OA不同版本（如7.1/8.0/9.1）对证书格式、私钥要求可能不同，稍不匹配就会报错“证书无效”。
* **反向代理配置复杂：**如果通过Nginx/Apache反向代理HTTPS，需额外调整代理规则，否则可能出现“页面能打开但功能报错”。
* **云端强制捆绑收费：**部分企业迁移到集团“所谓的高安全云平台”后，不仅基础资源费翻3倍，还要额外收取“安全服务费”“证书托管费”……

**二、**

**致远OA实现加密访问的逻辑图**

我们通过 Nginx 做反向代理，在 Nginx 里完成 SSL 证书的部署与 HTTPS 配置，只需在 Nginx 侧统一管理 HTTPS，协同 OA 以及它依赖的所有中间件（包括东方通、金蝶、宝兰德等信创中间件）都不需要做任何改动——它们依旧保持默认的HTTP模式运行，HTTPS 的全部管理工作全部由 Nginx 承担。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPN8G51Fk3ia9zxDnatpdxSdu5RGicd5hL8uDbDu6dujhh368IDRGEsT9GKpsjic0CLdDYL5ScVGzD4TFA/640?wx_fmt=png)

**三、**

**准备事项**

这里埋了一个不小的坑：需要使用Sticky模块！

**3.1**

**提前部署Nginx**

Nginx的Sticky模块是一种基于Cookie的负载均衡解决方案，能够确保来自同一客户端的请求始终路由到同一台后端服务器，从而实现会话保持，大致原理：

1. 客户端首次发起访问请求，nginx接收后，发现请求头没有cookie，则以轮询方式将请求分发给后端服务器。
2. 后端服务器处理完请求，将响应数据返回给nginx。
3. 此时nginx生成带route的cookie，返回给客户端。route的值与后端服务器对应，可能是明文，也可能是md5、sha1等Hash值。
4. 客户端接收请求，并保存带route的cookie。
5. 当客户端下一次发送请求时，会带上route，nginx根据接收到的cookie中的route值，转发给对应的后端服务器。

```
# 创建目录
mkdir /usr/local/nginx/module
cd /usr/local/nginx/module
#下载sticky
wget https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/get/master.tar.gz
tar xf master.tar.gz
#解压
tar -zxvf master.tar.gz

#进入nginx安装目录
cd /usr/local/nginx-1.9.9

./configure --prefix=/usr/local/nginx-1.9.9 \
--sbin-path=/usr/local/nginx/sbin/nginx \
--conf-path=/usr/local/nginx/conf/nginx.conf \
--pid-path=/usr/local/nginx/run/nginx.pid \
--error-log-path=/usr/local/nginx/logs/error.log \
--http-log-path=/usr/local/nginx/logs/access.log \
--with-pcre \
--user=nginx \
--group=nginx \
--with-stream \
--with-threads \
--with-file-aio \
--with-http_v2_module \
--with-http_ssl_module \
--with-http_realip_module \
--with-http_gzip_static_module \
--with-http_stub_status_module \
--add-module=/usr/local/nginx/module/nginx-sticky-module            #在此载入sticky模块
make
# 更新检测
make upgrade
# 查看模块是否被载入
cd /usr/local/nginx-1.9.9
./sbin/nginx -V

#查看是否添加成功
./sbin/nginx -V
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPN8G51Fk3ia9zxDnatpdxSdu54Sds6ibqhLvv7ibXvI4Dk2JK61dZuVOk5sUJo223dqtKQ5RpZom5nBjQ/640?wx_fmt=png)

**3.2**

**提前准备SSL证书**

SSL证书的申请渠道丰富多样（比如阿里云、腾讯云、DigiCert等），但价格差异悬殊（从免费到每年上千元不等），大家可以根据预算灵活选择。作者本次是在阿里云购买的通配符域名证书（如\*.xxx.com），它的核心优势在于支持无限匹配同一主域下的所有二级域名——举个实际场景：假设企业OA系统的域名是oa.xxx.com，只要这些域名都属于xxx.com这一主域，同一张通配符证书就能全部覆盖，完全不用为每个二级域名单独申请证书，既省去了重复申请的麻烦，也大幅降低了证书管理成本和后续维护的复杂度。

**3.3**

**Nginx配置HTTPS**

在获取到与Nginx兼容的SSL证书后，建议将证书文件（通常包括.pem格式的证书文件和.key格式的私钥文件）统一存放在Nginx配置目录下的conf/ssl/子目录中（例如：/etc/nginx/conf/ssl/，具体路径可根据实际安装情况调整，文件名请以您下载的证书文件为准）。

参照以下示例修改Nginx的主配置文件nginx.conf，即可完成HTTPS服务的配置与管理。

```
bashworker_processes auto;
worker_rlimit_nofile 20960;
error_log  logs/error.log  error;
events {
    worker_connections  4096;
    multi_accept on;
    accept_mutex on;
    accept_mutex_delay 500ms;
 }
http {
        server_tokens off;
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        access_log off;
        include       mime.types;
        default_type  application/octet-stream;
        keepalive_timeout  300;
        client_max_body_size 10240M;
        gzip on;
        gzip_min_length 1k;
        gzip_buffers 416k;
        gzip_comp_level 3;
        gzip_types text/xml text/plain text/css text/javascript application/x-javascript application/javascript application/xml;
        gzip_disable "MSIE [1-6]\.";
        upstream seeyon_v5_cluster{
      # 默认安装的Nginx无sticky模块无法启动，必须参考手册基于Linux或信创进行Nginx+sticky编译才能启动
            sticky;
            server 192.168.0.1:80 max_fails=300 fail_timeout=30s;
            server 192.168.0.2:80 max_fails=300 fail_timeout=30s;
        }
        server {
            listen 443 ssl;
            ssl_certificate ssl/www.seeyon.com.pem;
            ssl_certificate_key ssl/www.seeyon.com.key;
      # TLS协议按需调整
            ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
            charset utf-8;
            location / {
                proxy_pass http://seeyon_v5_cluster;
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header REMOTE-HOST $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_redirect http:// $scheme://;
                #proxy_redirect  off;
                proxy_connect_timeout 300;
                proxy_read_timeout 300;
                proxy_send_timeout 300;
            }
            error_page   500502503504  /50x.html;
            location = /50x.html {
                root   html;
            }
        }
}
```

**3.4**

**致远OA测HTTPS配置调整**

新版本9.0+以上不需要再做额外的操作了，但是7.x和8.x需要在系统配置中勾选https

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPN8G51Fk3ia9zxDnatpdxSdu56aBMhqChlBe4EgL1oT4NSH9QOYVicwX5rlySicepZ1OuQqdPjyQdzJMg/640?wx_fmt=png)

**3.5**

**重新启动Nginx服务**

以nginx安装在/home/nginx下为例，nginx的启动脚本为/home/nginx/sbin/nginx。重启后查看是否正常，启动示例如下：

```
# 切换命令行到nginx启动脚本目录
cd /home/nginx/sbin
# 启动
./nginx
# 重启
./nginx –s reload
# 指定配置文件重启，一般用于nginx异常停止后的启动
./nginx –c /home/nginx/conf/nginx.conf
```

**3.6**

**Nginx调整http转https**

找到nginx.conf文件进行编辑，在http段落中增加server段，并新增http协议的端口，做rewrite跳转：

```
    ......
    server {
        listen 80;
        server_name  localhost;
        charset utf-8;
        location / {
            rewrite ^(.*)$ https://$host$1 permanent;
        }
    }
    ......
```

到此配置是完成了，另外官方还有些性能调优的参数设置可以结合实际业务情况来做参考设置。

参数优化需依据nginx的运行情况，及服务器负载情况进行调整。常见的优化参数有以下内容：

* worker\_processes：nginx的进程数，一般为cpu的倍数，可以为1倍。
* worker\_rlimit\_nofile：nginx的进程打开文件数，可以与ulimit --u的值一致。
* worker\_connections：每个进程允许的最多连接数。
* keepalive\_timeout：客户端超时时间，单位秒。
* client\_max\_body\_size：客户端连接的最大请求实体，影响协同系统的上传附件大小，建议设置大于或等于运行附件上传的最大值。
* access\_log：请求日志，建议无需调试时关闭（off）。

![](https://mmbiz.qpic.cn/mmbiz_png/icL8rOBsZ6Jx8PoV02eATodKZFOPEgsf0lM7x8PfKvVczPwlDX0GD5Wepqm2jbNHlML3EicMmibJuA926zEiaaeQVA/640?wx_fmt=png/format,webp)

![](https://mmbiz.qpic.cn/mmbiz_png/icL8rOBsZ6Jx8PoV02eATodKZFOPEgsf0lM7x8PfKvVczPwlDX0GD5Wepqm2jbNHlML3EicMmibJuA926zEiaaeQVA/640?wx_fmt=png/format,webp)

![](https://mmbiz.qpic.cn/mmbiz_png/DlUwG7Amt1cfomBrsGj6GDP19gLgW5Xskk3mO8Ykzz8gAeb3HwKnxQX7t5uk8DNXzeWMu9KtQRUSicjygbiaXYoQ/640?wx_fmt=png)

**END**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/MVPvEL7Qg0F674fqUuZwzH0o4stN0C1ZFBSGwBXv5cU7X6ibk8vXfrNNRyaKAPSVibIkatVJy0hSKLEt8RRGB3Aw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MVPvEL7Qg0HCBZWsNxp5WDcYlGYo1WSHv0h5drcNIfrDoZt78zvW0mdpARYNOSib5saic904VQicRElRibSKnL6MLw/640?wx_fmt=png)

点**阅读原文**了解更多

![](https://mmbiz.qpic.cn/mmbiz_png/SZ0IAkWSmon9o4dg5nmBaic8cFjI4s72WPYR18k4kjuxHEz7DWofH17nneMibia3qtZh7135GueNCgOXl5V0aZ9Pg/640?wx_fmt=png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPNib3PtzEdOVlJ9mZGSCYRtib5gFFYDmzzPIGibFIqib2ZQIQptzpiaAH17gBe74aeBX600YwXvWgp9ns5Q/0?wx_fmt=png)

OA大助手

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TEnldia9cPNib3PtzEdOVlJ9mZGSCYRtib5gFFYDmzzPIGibFIqib2ZQIQptzpiaAH17gBe74aeBX600YwXvWgp9ns5Q/0?wx_fmt=png)

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