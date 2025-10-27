---
title: 源码分析 kubernetes coredns 插件服务发现及解析的实现原理
url: https://buaq.net/go-143815.html
source: unSafe.sh - 不安全
date: 2023-01-03
fetch_date: 2025-10-04T02:54:28.693776
---

# 源码分析 kubernetes coredns 插件服务发现及解析的实现原理

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

![](https://8aqnet.cdn.bcebos.com/7f1e900fa291fce705d54a3c37109b93.jpg)

源码分析 kubernetes coredns 插件服务发现及解析的实现原理

Kubernetes Coredns controller 控制器是用来监听 kube-apiserver 获取 service 等资源配置, 资源发生变更时修改内存里
*2023-1-2 23:3:33
Author: [xiaorui.cc(查看原文)](/jump-143815.htm)
阅读量:26
收藏*

---

Kubernetes Coredns controller 控制器是用来监听 kube-apiserver 获取 service 等资源配置, 资源发生变更时修改内存里的缓存. 当 coredns server 收到 dns query 请求时, 根据请求的域名在本地缓存 indexer 中找到对象, 组装记录后并返回, 完成域名解析.

k8s coredns controller 是已 coredns plugin 插件形式存在的, 插件的设计也是 coredns 一个优势所在.

**coredns 项目地址:**

从 kubernetes v1.11 起，coreDNS 已经取代 kube-dns 成为默认的 DNS 方案.

<https://github.com/coredns>

**coredns controller 调用关系**

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202301/202301022021998.png)

### coredns plugin 的实现原理

#### 加载插件

这里用 log 插件举例说明, 在 `init()` 内注册 log 的 setup 装载方法, 然后使用 AddPlugin 注册一个 plugin.Plugin 方法. 其目的就是要实现中间件那种调用链.

代码位置: `plugin/log/setup.go`

```
// 注册 log 插件, 把 log 的 setup 装载方法注册进去.
func init() { plugin.Register("log", setup) }

func setup(c *caddy.Controller) error {
    // Logger 实现了 plugin.Handler 接口了, 注册一个 plugin.Plugin 方法.
    dnsserver.GetConfig(c).AddPlugin(func(next plugin.Handler) plugin.Handler {
        return Logger{Next: next, Rules: rules, repl: replacer.New()}
    })

    return nil
}
```

#### 实例化 coredns server

coredns 在创建 Server 时, 倒序遍历已注册的 plugin 来构建 pluginChain 调用链.

```
func NewServer(addr string, group []*Config) (*Server, error) {
    s := &Server{
        Addr:         addr,
        zones:        make(map[string][]*Config),
        graceTimeout: 5 * time.Second,
        readTimeout:  3 * time.Second,
        writeTimeout: 5 * time.Second,
        ...
    }

    ...

    for _, site := range group {
        var stack plugin.Handler
        // 倒序插入
        for i := len(site.Plugin) - 1; i >= 0; i-- {
            // 两个邻居的 plugin 关联起来.
            stack = site.Plugin[i](stack)
            site.registerHandler(stack)

            ...
        }

        // 赋值 plugin 调用链
        site.pluginChain = stack
    }

    ...

    return s, nil
}
```

启动 udp/tcp 的监听, 读取 dns 请求报文, 处理 dns 请求.

* `ServePacket` 会启动启动 dns server, 并启动 udp server ;
* `ActivateAndServe` 会根据配置来启动 tcp 和 udp 服务 ;
* `serveUDP` 读取 dns 请求报文, 然后开一个协程去调用 `serveUDPPacket` ;
* `serveUDPPacket` 内部会实例化 writer 写对象, 然后调用 `serveDNS` 处理请求.

```
func (s *Server) ServePacket(p net.PacketConn) error {
    s.m.Lock()
    s.server[udp] = &dns.Server{PacketConn: p, Net: "udp", Handler: dns.HandlerFunc(func(w dns.ResponseWriter, r *dns.Msg) {
        // 调用 ServeDns 方法
        s.ServeDNS(ctx, w, r)
    }), TsigSecret: s.tsigSecret}
    s.m.Unlock()

    // 启动监听
    return s.server[udp].ActivateAndServe()
}

// 根据 srv.net 决定是开启 udp 还是 tcp server.
func (srv *Server) ActivateAndServe() error {
    // 启动 udp 服务, 当 srv.net 为 udp 时启动 udp server.
    if srv.PacketConn != nil {
        return srv.serveUDP(srv.PacketConn)
    }

    // 启动 tcp 服务, srv.net 为 tcp 时才启动 tcp server.
    if srv.Listener != nil {
        return srv.serveTCP(srv.Listener)
    }
    return &Error{err: "bad listeners"}
}

// serveUDP starts a UDP listener for the server.
func (srv *Server) serveUDP(l net.PacketConn) error {
    for srv.isStarted() {
        ...

        // 读取 dns 请求报文
        if isUDP {
            m, sUDP, err = reader.ReadUDP(lUDP, rtimeout)
        } else {
            m, sPC, err = readerPC.ReadPacketConn(l, rtimeout)
        }

        // 异常处理 dns 请求, 每个请求都会启动一个协会处理.
        go srv.serveUDPPacket(&wg, m, l, sUDP, sPC)
    }

    return nil
}

// 处理 dns 请求
func (srv *Server) serveUDPPacket(wg *sync.WaitGroup, m []byte, u net.PacketConn, udpSession *SessionUDP, pcSession net.Addr) {
    // 构建 response writer
    w := &response{tsigProvider: srv.tsigProvider(), udp: u, udpSession: udpSession, pcSession: pcSession}
    if srv.DecorateWriter != nil {
        w.writer = srv.DecorateWriter(w)
    } else {
        w.writer = w
    }

    // 调用 ServeDNS 处理请求
    srv.serveDNS(m, w)
}
```

#### coredns serveDNS 主处理逻辑

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202301/202301022231339.png)

遍历执行 pluginChain 插件链的所有 Plugin 插件, 依次执行 plugin.ServeDNS 方法.

代码位置: `core/dnsserver/server.go`

```
func (s *Server) ServeDNS(ctx context.Context, w dns.ResponseWriter, r *dns.Msg) {
    ...

    // 判断 edns 判断, edns 是个很厉害的功能, 没有 edns 之前, gslb 拿到的只是 dns server 地址, 拿不到用户地址. 而使用 edns 开放协议后, gslb 可以拿到用户的地址. 这样的流量调度才更加准确.
    if m, err := edns.Version(r); err != nil { // Wrong EDNS version, return at once.
        w.WriteMsg(m)
        return
    }

    w = request.NewScrubWriter(r, w)

    for {
        // 遍历每个 zone
        if z, ok := s.zones[q[off:]]; ok {
            for _, h := range z {
                ...
                if passAllFilterFuncs(ctx, h.FilterFuncs, &request.Request{Req: r, W: w}) {
                    if r.Question[0].Qtype != dns.TypeDS {
                        // 执行 plugin 插件调用链, 调用每个插件的 ServeDNS 方法.
                        rcode, _ := h.pluginChain.ServeDNS(ctx, w, r)
                        if !plugin.ClientWrite(rcode) {
                        }
                        return
                    }
                    dshandler = h
                }
            }
        }

        off, end = dns.NextLabel(q, off)
        if end {
            break
        }
        ...
    }

    ...

    errorAndMetricsFunc(s.Addr, w, r, dns.RcodeRefused)
}
```

### 加载 kubernetes 插件

```
const pluginName = "kubernetes"

// 把插件注册到 caddy 的 plugins 注册表里, 格式为 map[serverType][plugin.name]Plugin
func init() { plugin.Register(pluginName, setup) }

// 解析配置, 生成 kubeclient, 实例化 newdnsController 控制器等
func setup(c *caddy.Controller) error {
    // 解析 k8s 配置
    k, err := kubernetesParse(c)
    if err != nil {
        return plugin.Error(pluginName, err)
    }

    // 实例化 kubeclient 并 实例化 dns controller 控制器
    onStart, onShut, err := k.InitKubeCache(context.Background())
    if err != nil {
        return plugin.Error(pluginName, err)
    }
    ...

    // 把插件注册到 plugin 链表里, 执行效果就是 middleware 中间件模型
    dnsserver.GetConfig(c).AddPlugin(func(next plugin.Handler) plugin.Handler {
        k.Next = next
        return k
    })

    // 获取本地非回环的 ip 地址集合
    c.OnStartup(func() error {
        k.localIPs = boundIPs(c)
        return nil
    })

    return nil
}
```

后面补一篇专门说下 coredns server 的实现原理, 其关键几个插件的实现, 另外如何自定义开发插件.

### dnsController 控制器逻辑

源码位置: `plugin/kubernetes/controller.go`

#### 实例化控制器

实例化 dnsControl 对象, 同时实例化各个资源的 informer 对象, 在实例化 informer 时传入自定义的 eventHandler 回调方法 和 indexer 索引方法.

* 为什么需要监听 service 资源 ? 用户在 pod 内直接使用 service\_name 获取到 cluster ip.
* 为什么需要监听 pod 资源 ? 用户可以直接通过 podname 进行解析.
* 为什么需要监听 endpoints 资源 ? 如果 service 有配置 clusterNone, 也就是 headless 类型, 则需要使用到 endpoints 的地址.
* 为什么需要监听 namespace 资源 ? 需要判断请求域名的 namespace 段是否可用.

```
// newdnsController creates a controller for CoreDNS.
func newdnsController(ctx context.Context, kubeClient kubernetes.Interface, opts dnsControlOpts) *dnsControl {
    // 自定义 dns controller 控制器对象
    dns := dnsControl{
        client:            kubeClient,
        selector:          opts.selector,
        namespaceSelector: opts.namespaceSelector,
        zones:             opts.zones,
    }

    // 实例化 service 资源的 informer 对象, 自定义 list 和 watch 的筛选方法.
    dns.svcLister, dns.svcController = object.NewIndexerInformer(
        &cache.ListWatch{
            ListFunc:  serviceListFunc(ctx, dns.client, api.NamespaceAll, dns.selector),
            WatchFunc: serviceWatchFunc(ctx, dns.client, api.NamespaceAll, dns.selector),
        },
        // 指定 service 资源类型
        &api.Service{},
        // 向 informer 注册 eventHandler 回调方法
        cache.ResourceEventHandlerFuncs{AddFunc:...