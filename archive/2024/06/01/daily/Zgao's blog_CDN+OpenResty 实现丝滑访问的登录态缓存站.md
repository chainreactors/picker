---
title: CDN+OpenResty 实现丝滑访问的登录态缓存站
url: https://zgao.top/cdnopenresty-%e5%ae%9e%e7%8e%b0%e4%b8%9d%e6%bb%91%e8%ae%bf%e9%97%ae%e7%9a%84%e7%99%bb%e5%bd%95%e6%80%81%e7%bc%93%e5%ad%98%e7%ab%99/
source: Zgao's blog
date: 2024-06-01
fetch_date: 2025-10-06T16:55:17.525949
---

# CDN+OpenResty 实现丝滑访问的登录态缓存站

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# CDN+OpenResty 实现丝滑访问的登录态缓存站

* [首页](https://zgao.top)
* [CDN+OpenResty 实现丝滑访问的登录态缓存站](https://zgao.top:443/cdnopenresty-%E5%AE%9E%E7%8E%B0%E4%B8%9D%E6%BB%91%E8%AE%BF%E9%97%AE%E7%9A%84%E7%99%BB%E5%BD%95%E6%80%81%E7%BC%93%E5%AD%98%E7%AB%99/)

[5月 31, 2024](https://zgao.top/2024/05/)

### CDN+OpenResty 实现丝滑访问的登录态缓存站

作者 [Zgao](https://zgao.top/author/zgao/)
在[[安全运维](https://zgao.top/category/%E5%AE%89%E5%85%A8%E8%BF%90%E7%BB%B4/)](https://zgao.top/cdnopenresty-%E5%AE%9E%E7%8E%B0%E4%B8%9D%E6%BB%91%E8%AE%BF%E9%97%AE%E7%9A%84%E7%99%BB%E5%BD%95%E6%80%81%E7%BC%93%E5%AD%98%E7%AB%99/)

去年在博客上分享过用Nginx反向代理实现的zsxq登录态网站，但是实际体验并不友好。

1. 第一次访问加载js时间非常长
2. 服务端接口故意返回报错，导致页面空白
3. 多人访问导致Nginx反向代理替换大文件字符串效率低下
4. Nginx部署在境外，国内访问速度很慢

而上面出现的问题，实际上都可以通过CDN缓存加速的方式解决。

文章目录

[ ]

* [腾讯云CDN配置](#%E8%85%BE%E8%AE%AF%E4%BA%91CDN%E9%85%8D%E7%BD%AE "腾讯云CDN配置")
  + [备案过的域名](#%E5%A4%87%E6%A1%88%E8%BF%87%E7%9A%84%E5%9F%9F%E5%90%8D "备案过的域名")
  + [CDN控制台配置](#CDN%E6%8E%A7%E5%88%B6%E5%8F%B0%E9%85%8D%E7%BD%AE "CDN控制台配置")
  + [配置CDN https（可选）](#%E9%85%8D%E7%BD%AECDN_https%EF%BC%88%E5%8F%AF%E9%80%89%EF%BC%89 "配置CDN https（可选）")
* [开启OpenResty自带的缓存功能](#%E5%BC%80%E5%90%AFOpenResty%E8%87%AA%E5%B8%A6%E7%9A%84%E7%BC%93%E5%AD%98%E5%8A%9F%E8%83%BD "开启OpenResty自带的缓存功能")
  + [为什么不会缓存接口数据？](#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%B8%8D%E4%BC%9A%E7%BC%93%E5%AD%98%E6%8E%A5%E5%8F%A3%E6%95%B0%E6%8D%AE%EF%BC%9F "为什么不会缓存接口数据？")
* [接口报错数据也被缓存？](#%E6%8E%A5%E5%8F%A3%E6%8A%A5%E9%94%99%E6%95%B0%E6%8D%AE%E4%B9%9F%E8%A2%AB%E7%BC%93%E5%AD%98%EF%BC%9F "接口报错数据也被缓存？")
* [如何解决Nginx 401 认证被CDN缓存绕过？](#%E5%A6%82%E4%BD%95%E8%A7%A3%E5%86%B3Nginx_401_%E8%AE%A4%E8%AF%81%E8%A2%ABCDN%E7%BC%93%E5%AD%98%E7%BB%95%E8%BF%87%EF%BC%9F "如何解决Nginx 401 认证被CDN缓存绕过？")

## 腾讯云CDN配置

CDN如果要对境内加速的话，是要求加速的域名备案的。

### 备案过的域名

我自己的域名备案过期了，找朋友借一个备案过的域名作为子域名。

### CDN控制台配置

在控制台添加一个要加上的域名。

![](https://zgao.top/wp-content/uploads/2024/05/image-14-900x1024.png)

配置都选默认配置即可，然后就是为要加速的域名添加CNAME记录。

![](https://zgao.top/wp-content/uploads/2024/05/image-15-1024x390.png)

配置完成后，通过CDN加速的域名访问Nginx，速度已经有了明显的提升，所有的静态资源js、css都被CDN缓存了。

### 配置CDN https（可选）

在腾讯云控制台申请一个域名免费的ssl证书。

![](https://zgao.top/wp-content/uploads/2024/05/image-17-1024x791.png)

这样即使源站是http请求也无所谓，在CDN这一层配置https即可。

![](https://zgao.top/wp-content/uploads/2024/05/image-18-977x1024.png)

顺便开启302强制跳转。

## 开启*OpenResty*自带的缓存功能

OpenResty® 是一个基于 Nginx 与 Lua 的高性能 Web 平台，其内部集成了大量精良的 Lua 库、第三方模块以及大多数的依赖项。用于方便地搭建能够处理超高并发、扩展性极高的动态 Web 应用、Web 服务和动态网关。*OpenResty* 可以理解为Nginx的升级版。

先在http中配置全局的proxy\_cache\_path。如果想要在log中显示当前请求是否命中Nginx的缓存需要修改日志格式如下。

```
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path=off;

    log_format main      '$remote_addr - $remote_user [$time_local] "$request" '
                         '$status $body_bytes_sent "$http_referer" '
                         '"$http_user_agent" "$upstream_cache_status" '
                         '$request_time $upstream_response_time $pipe';
```

然后在Location中指定proxy\_cache的名字。

```
        location /api/ {
                proxy_pass https://api.xxxx.com/;

                proxy_cache my_cache;
                proxy_cache_valid 200 302 24h;
                proxy_cache_valid 404 1m;
        }
```

然后重启Nginx即可。但是会发现Nginx确实也缓存了js、css等静态资源。但是却不会缓存接口的数据？

![](https://zgao.top/wp-content/uploads/2024/05/image-16-1024x531.png)

查看日志中请求是否有命中缓存。

### 为什么不会缓存接口数据？

CDN和Nginx同样不会对接口数据缓存，通过对header的逐一调试，发现当服务端当存在Cache-Control、Expires 、Set-Cookie等header时，中间件就不会进行缓存。

进一步修改配置文件如下：

```
        location /api/ {
                proxy_pass https://api.xxxx.com/;

                proxy_cache my_cache;
                proxy_cache_valid 200 302 24h;
                proxy_cache_valid 404 1m;

                proxy_hide_header Set-Cookie;
                proxy_hide_header Expires;
                proxy_hide_header X-Expire-In;
                proxy_ignore_headers Cache-Control Expires Set-Cookie ;
        }
```

* **`proxy_hide_header`**：用于隐藏指定的响应头，使其不传递给客户端。
* **`proxy_ignore_headers`**：用于忽略指定的响应头，使其对 Nginx 的缓存逻辑无效，但仍然可以传递给客户端。

因为Nginx前面还有CDN所以需要proxy\_hide\_header和proxy\_ignore\_headers配合使用。

## 接口报错数据也被缓存？

由于zsxq时不时返回一个1059的接口报错返回，导致错误的数据被*OpenResty*和CDN缓存，这是非常致命的问题。如何让*OpenResty*判断服务端返回的数据是否存在错误状态码？有的话就不缓存错误数据。

这个问题我思考了好多天，尝试过很多种方式。比如通过先判断body中是否包含特定的状态码，再决定是否在header中添加Cache-Control使其不缓存错误数据。但是Nginx在返回数据时是先返回header，再返回body内容。这就导致Nginx获取到body内容后，header已经返回给客户端了，就无法成功修改header。

我甚至动了手动改造Nginx源码的念头，最终还是忍住了。

下面是我曲线救国的配置实现，思路非常巧妙。

```
            header_filter_by_lua_block {
                if ngx.var.upstream_cache_status == "HIT" then
                    ngx.log(ngx.ERR, "Cache hit, removing Cache-Control header for request: ", ngx.var.request_uri)
                    ngx.header["Cache-Control"] = nil
                end
            }

            body_filter_by_lua_block {
                local chunk = ngx.arg[1]
                local eof = ngx.arg[2]

                if ngx.ctx.response_body == nil then
                    ngx.ctx.response_body = chunk
                else
                    ngx.ctx.response_body = ngx.ctx.response_body .. chunk
                end

                if eof then
                    local body = ngx.ctx.response_body
                    local body_length = #body

                if body_length < 512 then
                        local json = require "cjson"
                        local data = json.decode(body)

                if data and data.code == 1059 then
                    local upstream_scheme = "https"
                    local upstream_host = "api.xxxx.com"
                    local new_url = ngx.var.request_uri:gsub("^/api", "")
                    local upstream_url = upstream_scheme .. "://" .. upstream_host .. new_url

                        local cache_key = ngx.md5(upstream_url)
                        local cache_dir = "/var/cache/nginx/"
                        local subdir1 = string.sub(cache_key, -1)
                        local subdir2 = string.sub(cache_key, -3, -2)
                        local cache_file_path = cache_dir .. subdir1 .. "/" .. subdir2 .. "/" .. cache_key

                            local res = os.remove(cache_file_path)
                            if res then
                                ngx.log(ngx.ERR, "Cache for ", ngx.var.request_uri, " has been purged due to error code 1059")
                            else
                                ngx.log(ngx.ERR, "Failed to purge cache for ",cache_file_path, " ", upstream_url)
                            end
                        end
                    end
                end
            }
```

先判断body中是否存在错误状态码，如果有的话就删除对应的缓存文件。这样下一次请求同意的url，由于缓存文件不存在，同样不会命中缓存。但是第二次接口返回正常数据时，就不会触发删除规则，就能正常被CDN给缓存，极为巧妙。

## 如何解决Nginx 401 认证被CDN缓存绕过？

```
        location / {
                        auth_basic "zsxq";
                        auth_basic_user_file /etc/nginx/htpasswd.txt;

                        if ($uri = '/'){
                                return 301 https://zsxq.xxxxx.top/dweb2/index/group/xxxxxxx;
                        }
        }
```

上面的配置虽然对 / 配置了密码认证，同时对url进行了跳转。但是经过CDN缓存后401认证就失效了。这是因为接口数据都被静态缓存了就不会弹窗认证了。

需要重新配置要认证的页面不经过CDN缓存。对于页面的URL需要单独配置认证。

```
        location ~ ^/dweb2/index/group/\d+$ {
                auth_basic "zsxq";
                auth_basic_user_file /etc/nginx/htpasswd.txt;

                proxy_pass https://wx.xxxx.com;

                add_header Cache-Control no-store;
        }
```

通过add\_header Cache-Control no-store;就能成功配置当前路由不被CDN缓存，正常弹窗认证。

Post Views: 589

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 发表评论 [取消回复](/cdnopenresty-%E5%AE%9E%E7%8E%B0%E4%B8%9D%E...