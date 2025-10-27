---
title: 源码分析 kubernetes ingress nginx 动态更新的实现原理
url: https://buaq.net/go-143700.html
source: unSafe.sh - 不安全
date: 2023-01-02
fetch_date: 2025-10-04T02:51:54.871942
---

# 源码分析 kubernetes ingress nginx 动态更新的实现原理

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

![](https://8aqnet.cdn.bcebos.com/3ac7ef517e12de1f597976a07cfb43c7.jpg)

源码分析 kubernetes ingress nginx 动态更新的实现原理

源码分析 kubernetes ingress nginx 动态更新的实现原理阅读本文前, 建议先阅读下 k8s ingress nginx controller 实
*2023-1-1 19:13:12
Author: [xiaorui.cc(查看原文)](/jump-143700.htm)
阅读量:25
收藏*

---

## 源码分析 kubernetes ingress nginx 动态更新的实现原理

阅读本文前, 建议先阅读下 k8s ingress nginx controller 实现原理.

[kubernetes\_ingress\_nginx\_controller\_code](https://github.com/rfyiamcool/notes/blob/main/kubernetes_ingress_nginx_controller_code.md)

#### 动态更新的函数调用流程:

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202301/202301011133932.png)

#### 概述

通过 ingress-nginx 中 `nginx.tmpl` 的配置得知, nginx (openretry) 转发的逻辑是依赖 upstream 的 balancer\_by\_lua\_block 指令实现的.

http 和 stream (tcp/udp) 在生成配置时, 在 upstream 段里都插入了 `balancer_by_lua_block` 指令用来实现自定义负载均衡逻辑, nginx 会依赖该 balancer 来获取转发的地址, 然后对该连接进行转发.

> 该 lua 转发模块代码位置是 `rootfs/etc/nginx/lua/balancer.lua`.

### balancer\_by\_lua\_block 是怎么回事 ?

`balancer_by_lua_block` 是一个支持自定义负载均衡器的指令, 通常基于 nginx 的服务发现就是通过该指令实现的.

开发时一定要注意事项, balancer\_by\_lua\_block 只是通过自定义负载均衡算法获取 peer 后端地址, 接着通过 `balancer.set_current_peer(ip, port)` 进行赋值. 后面连接的建立，连接池维护，数据拷贝转发等流程统统不在这里，而是由 nginx 内部 upstream 转发逻辑实现.

一句话，nginx 只是调用 `balancer_by_lua_block` 获取理想的后端地址而已.

下面是使用 `balancer_by_lua_block` 实现调度地址池的例子:

```
upstream xiaorui_cc_backend {
    server 0.0.0.0;

    balancer_by_lua_block {
        local balancer = require "ngx.balancer"
        local host = {"s1.xiaorui.cc", "s2.xiaorui.cc"}
        local backend = ""
        local port = ngx.var.server_port
        local remote_ip = ngx.var.remote_addr
        local key = remote_ip..port

        # 使用地址 hash 调度算法
        local hash = ngx.crc32_long(key);
        hash = (hash % 2) + 1
        backend = host[hash]
        ngx.log(ngx.DEBUG, "ip_hash=", ngx.var.remote_addr, " hash=", hash, " up=", backend, ":", port)

        # 配置后端地址, nginx 进行转发时依赖该地址
        local ok, err = balancer.set_current_peer(backend, port)
        if not ok then
            ngx.log(ngx.ERR, "failed to set the current peer: ", err)
            return ngx.exit(500)
        end
    }
}

server {
    listen 80;
    server_name xiaorui.cc
    location / {
        proxy_pass http://xiaorui_cc_backend;
    }
}
```

lua-nginx-module 项目中关于 balancer\_by\_lua\_block 实现:

<https://github.com/openresty/lua-nginx-module#balancer_by_lua_block>

### 在 nginx 里加入 balancer\_by\_lua\_block 指令

在 `nginx.tmpl` 中加入了 `balancer_by_lua_block` 指令, 所以不管是 http 和 stream 段里的 upstream 转发, 不再走 server 配置, 而是走 `balancer_by_lua_block` 自定义流程.

```
http {
    upstream upstream_balancer {
        // 只是占位符, openretry 优先走 balancer_by_lua 逻辑块.
        server 0.0.0.1; # placeholder

        balancer_by_lua_block {
          balancer.balance()
        }

        {{ if (gt cfg.UpstreamKeepaliveConnections 0) }}
        keepalive {{cfg.UpstreamKeepaliveConnections }};
        keepalive_time {{ $cfg.UpstreamKeepaliveTime }};
    ...
        {{ end }}
    }

    ...

    server {
    ...
    }
}

stream {
    upstream upstream_balancer {
        // 同上, 只是占位符, 避免 nginx -t 检测出错.
        server 0.0.0.1:1234; # placeholder

        balancer_by_lua_block {
          tcp_udp_balancer.balance()
        }
    }

    ...

    server {
    ...
    }
}
```

### 把变更信息通知给 nginx

* 检查 http backends 是否有变更, 当有变更时, 把 backends 数据通知给 nginx 的 `http://127.0.0.1:10246/configuration/backends` 接口上.
* 检查 tcp/udp strem backends 是否有变更, 发生变更时, 把 stream backends 数据发到 nginx 的 tcp `10247` 端口上.
* 当证书发生变更时, 发数据发到 nginx 的 `http://127.0.0.1:10246/configuration/servers` 接口上.

源码位置: <https://github.com/kubernetes/ingress-nginx/blob/4508493dfe7fb06206109a0a9dcc6025cc335273/internal/ingress/controller/nginx.go>

```
func (n *NGINXController) configureDynamically(pcfg *ingress.Configuration) error {
    backendsChanged := !reflect.DeepEqual(n.runningConfig.Backends, pcfg.Backends)
    // 当 endpoints 地址发生变更时
    if backendsChanged {
        // 动态修改 http 的 backends
        err := configureBackends(pcfg.Backends)
        if err != nil {
            return err
        }
    }

    streamConfigurationChanged := !reflect.DeepEqual(n.runningConfig.TCPEndpoints, pcfg.TCPEndpoints) || !reflect.DeepEqual(n.runningConfig.UDPEndpoints, pcfg.UDPEndpoints)
    // 当 endpoints 地址发生变更时
    if streamConfigurationChanged {
        // 动态修改 tcp 和 udp 的 backends 地址列表
        err := updateStreamConfiguration(pcfg.TCPEndpoints, pcfg.UDPEndpoints)
        if err != nil {
            return err
        }
    }

    serversChanged := !reflect.DeepEqual(n.runningConfig.Servers, pcfg.Servers)
    // 当 servers 地址发生变更时
    if serversChanged {
        // 动态修改证书相关配置
        err := configureCertificates(pcfg.Servers)
        if err != nil {
            return err
        }
    }

    return nil
}
```

这里拿 `configureBackends()` 变更配置来说. 组装 openresty 专用的 backends 数据, 然后序列化成 json, post 发给 openresty 的 `/configuration/backends` 接口上.

```
func configureBackends(rawBackends []*ingress.Backend) error {
    backends := make([]*ingress.Backend, len(rawBackends))

    for i, backend := range rawBackends {
        luaBackend := &ingress.Backend{
            ...
        }

        var endpoints []ingress.Endpoint
        for _, endpoint := range backend.Endpoints {
            endpoints = append(endpoints, ingress.Endpoint{
                Address: endpoint.Address,
                Port:    endpoint.Port,
            })
        }

        luaBackend.Endpoints = endpoints
        backends[i] = luaBackend
    }

    statusCode, _, err := nginx.NewPostStatusRequest("/configuration/backends", "application/json", backends)
    if err != nil {
        return err
    }

    if statusCode != http.StatusCreated {
        return fmt.Errorf("unexpected error code: %d", statusCode)
    }

    return nil
}

func NewPostStatusRequest(path, contentType string, data interface{}) (int, []byte, error) {
    url := fmt.Sprintf("http://127.0.0.1:%v%v", StatusPort, path)
    buf, err := json.Marshal(data)
    ...

    res, err := client.Post(url, contentType, bytes.NewReader(buf))
    ...

    body, err := io.ReadAll(res.Body)
    ...
    return res.StatusCode, body, nil
}
```

### nginx 如何接收需要动态更新的配置 ？

上面代码是如何发送变更信息, 那么谁来接收动态数据的投递?

`nginx.conf` 中定义了一个解决动态配置更新的 server 配置段, 其中变量 StatusPort 为 10246, 接口的 prefix 路径为 `/configuration`, 该接口定义了 content\_by\_lua\_block 处理块.

当接口收到请求后, 调用自定义 lua 模块 `configuration.lua` 中 `configuration.call()` 入口方法.

```
    server {
        listen 127.0.0.1:{{ .StatusPort }};

        keepalive_timeout 0;
        gzip off;

        access_log off;

        location {{ healthzURI }} {
            return 200;
        }

        location /configuration {
            client_max_body_size                    {{ luaConfigurationRequestBodySizecfg }};
            client_body_buffer_size                 {{ luaConfigurationRequestBodySize $cfg }};
            proxy_buffering                         off;

            content_by_lua_block {
              configuration.call()
            }
        }
    }
```

下面分析 `configuration.call()` 的实现原理. `call()` 中硬编码写了各个接口的处理方法.

当 `ngx.var.request_uri` 为 `/configuration/backends` 时候, 调用 `handle_backends` 方法处理该路由.

`handle_backends` 内部实现过程很简单, 先解析 request body, 然后把读到的 body 字符串放到共享存储 `configuration_data` 的 backends 键里, 然后更新下操作的时间戳.

`configuration_data` 是一个 ngx.shared.Dict 共享内存的字典存储结构, 其 set/get 操作是并发安全的. nx.shared.dict 内部通过红黑树实现的 hashmap, 使用 lru 实现的数据淘汰.

configuration\_data:set 的时候没有 cjson 解析对象, 而是直接赋值json string.

```
function _M.call()
  if ngx.var.request_method ~= "POST" and ngx.var.request_method ~= "GET" then
    ngx.status = ngx.HTTP_BAD_REQUEST
    return
  end

  # 处理证书的 servers
  if ngx.var...