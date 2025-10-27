---
title: 源码分析 kubernetes ingress nginx controller 控制器的实现原理
url: https://buaq.net/go-143687.html
source: unSafe.sh - 不安全
date: 2023-01-02
fetch_date: 2025-10-04T02:51:56.024734
---

# 源码分析 kubernetes ingress nginx controller 控制器的实现原理

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

![](https://8aqnet.cdn.bcebos.com/092e3d4a02fff97b9df4eb89ccb0da36.jpg)

源码分析 kubernetes ingress nginx controller 控制器的实现原理

源码分析 kubernetes ingress nginx controller 控制器的实现原理本文基于 kubernetes/ingress-nginx v1.
*2023-1-1 19:11:26
Author: [xiaorui.cc(查看原文)](/jump-143687.htm)
阅读量:33
收藏*

---

## 源码分析 kubernetes ingress nginx controller 控制器的实现原理

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202301/202301010021497.png)

本文基于 kubernetes/ingress-nginx `v1.5.1` 源码分析, ingress-nginx 里的 controller 控制器是 golang 开发的. 而 ingress-nginx 容器内使用了官方的 nginx, 没有直接使用 openresty, 原生 nginx 编译时打入了 lua / luajit 模块, 但引用的三方的库包是属于 openresty 社区里的. 在这看 ingress-nginx 详细的 lua 库包引用信息.

<https://github.com/kubernetes/ingress-nginx/blob/21aa7f55a3/images/nginx/rootfs/build.sh>

#### ingress-nginx 为什么没有直接使用 openresty?

在 github issue 列表中没有找到答案. 按理来说社区方面 openresty 要比 nginx 更加开放, 但毕竟没有 nginx 的背景和后台金主.

像社区的 kong 和 apache apisix 是基于 openresty 开发的, 另外他们也在社区中开源了自己的 ingress-controller.

#### ingress-nginx 项目地址:

<https://github.com/kubernetes/ingress-nginx>

#### ingress-nginx 核心函数调用关系流程:

实现过程略显复杂, 故图中忽略细节.

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202301/202301010007853.png)

### 实例化 nginx ingress controller 控制器

```
// NewNGINXController creates a new NGINX Ingress controller.
func NewNGINXController(config *Configuration, mc metric.Collector) *NGINXController {
    // 读取 resulv.conf 文件，获取 dns server 地址集合
    h, err := dns.GetSystemNameServers()

    n := &NGINXController{
        stopCh:   make(chan struct{}),

        // informer 注册 eventHandler 会往这个 chan 发送事件.
        updateCh: channels.NewRingChannel(1024),
        Proxy: &tcpproxy.TCPProxy{},
        command: NewNginxCommand(),
    }

    // 实例化 store 对象, 可以把 store 想成一个有各种数据的缓存的存储, 内部也有 informer.
    n.store = store.New(
        ...
        n.updateCh, // 把上面实例化的 updateCh 传进去了
        ...
    )

    // 实例化 queue, 并且在 queue里注册了回调方法, syncIngress 是 nginx ingress controller 最核心的同步方法.
    n.syncQueue = task.NewTaskQueue(n.syncIngress)

    // 用在 inotify 文件监听的回调方法
    onTemplateChange := func() {
        // 从 `/etc/nginx/template/nginx.tmpl` 读取预设的模板, 然后进行解析生成 template 对象.
        template, err := ngx_template.NewTemplate(nginx.TemplatePath)
        if err != nil {
            klog.ErrorS(err, "Error loading new template")
            return
        }

        n.t = template

        // 向 queue 传递事件, 平滑热加载 nginx 配置
        n.syncQueue.EnqueueTask(task.GetDummyObject("template-change"))
    }

    // 从 `/etc/nginx/template/nginx.tmpl` 读取预设的模板, 然后进行解析生成 template 对象.
    ngxTpl, err := ngx_template.NewTemplate(nginx.TemplatePath)
    if err != nil {
        klog.Fatalf("Invalid NGINX configuration template: %v", err)
    }

    n.t = ngxTpl

    // 使用 inotify 机制异步监听 nginx.tmpl 模板文件, 当模板文件发生变更时, 则回调 onTemplateChange 方法, 重新读取模板并构建模板对象, 然后同步配置
    file.NewFileWatcher(nginx.TemplatePath, onTemplateChange)

    // 获取 geoip 目录下的相关文件, v4.4.2 里当前就只有三个文件, 分别是 geoip.dat, geoIPASNum.dat, geoLiteCity.dat 数据文件.
    filesToWatch := []string{}
    err = filepath.Walk("/etc/nginx/geoip/", func(path string, info os.FileInfo, err error) error {
        filesToWatch = append(filesToWatch, path)
        return nil
    })

    for _, f := range filesToWatch {
        // 异步监听 geoip dat 数据文件, 当发生增删改时, 重新平滑热加载 nginx 配置.
        _, err = file.NewFileWatcher(f, func() {
            n.syncQueue.EnqueueTask(task.GetDummyObject("file-change"))
        })
    }

    return n
}
```

### 服务启动入口

`Start()` 启动 nginx controller 控制器, 其原理如下:

1. 启动 `store.Run()`, 内部会启动 informer 监听并维护各资源的本地缓存 ;
2. 进行 leader election 选举, 只有主实例才可以执行状态同步的逻辑 ;
3. 启动 nginx 进程, 指定配置为 `/etc/nginx/nginx.conf` ;
4. 启动 syncQueue 里 run 方法, 该方法内部会从队列中读取任务, 并调用 syncIngress 来同步 nginx 配置 ;
5. 前面 nginx 启动使用时, 只是使用了默认的 nginx.conf, 里面几乎没什么东西, 这里通过主动通知 syncqueue, 然后 syncqueue worker 调度 syncIngress 来同步配置并完成热加载 ;
6. 启动一个协程每隔 5秒进行临时配置文件清理 ;
7. 从 informer 导入的 updateCh 获取任务, 并写到 syncQueue 队列里.

```
func (n *NGINXController) Start() {
    klog.InfoS("Starting NGINX Ingress controller")

    // 启动 store, 内部会启动 informer 监听并维护各资源的本地缓存.
    n.store.Run(n.stopCh)

    // 进行选举, 只有主实例才可以执行状态同步的更新的逻辑.
    setupLeaderElection(&leaderElectionConfig{
        Client:     n.cfg.Client,
        ElectionID: electionID,
        OnStartedLeading: func(stopCh chan struct{}) {
            if n.syncStatus != nil {
                // 开启状态的同步更新
                go n.syncStatus.Run(stopCh)
            }
        },
    })

    // 配置进程组, 使用 cmd 创建的程序都所属相同的 pgid 组id, 这样杀掉进程时可以按照进程组杀, 避免有遗漏的进程.
    cmd := n.command.ExecCommand()
    cmd.SysProcAttr = &syscall.SysProcAttr{
        Setpgid: true,
        Pgid:    0,
    }

    // 加载 ssl proxy
    if n.cfg.EnableSSLPassthrough {
        n.setupSSLProxy()
    }

    // 启动 nginx 进程, 指定配置为 `/etc/nginx/nginx.conf`.
    n.start(cmd)

    // 启动 syncQueue 里 run 方法, 该方法内部会从队列中读取任务, 并调用 syncIngress 来同步 nginx 配置.
    go n.syncQueue.Run(time.Second, n.stopCh)

    // 前面 nginx 启动使用时, 只是使用了默认的 nginx.conf, 里面几乎没什么东西, 这里通过主动传任务到 syncqueue, 然后 syncqueue 利用 syncIngress 来同步配置并完成热加载
    n.syncQueue.EnqueueTask(task.GetDummyObject("initial-sync"))

    go func() {
        for {
            time.Sleep(5 * time.Minute)

            // 启动一个异步 gc 协程, 清理 nginx 临时文件, 临时文件的名字前缀有 `nginx-cfg` 字符串, 当满足临时文件特征, 且更改超过5分钟则删除该临时文件
            cleanTempNginxCfg()
        }
    }()

    for {
        select {
        case err := <-n.ngxErrCh:
            ...
        case event := <-n.updateCh.Out():
            // 从 informer 拿到更改事件
            if evt, ok := event.(store.Event); ok {
                // 如果事件的类型是配置相关的, 则通知给 syncqueue, 让 syncqueue 的内部去同步配置.
                if evt.Type == store.ConfigurationEvent {
                    n.syncQueue.EnqueueTask(task.GetDummyObject("configmap-change"))
                    continue
                }

                // 同上, 只是任务可跳过.
                n.syncQueue.EnqueueSkippableTask(evt.Obj)
            }
        case <-n.stopCh:
            return
        }
    }
}
```

### 监听 informer 事件

`store` 实例化了 nginx ingress controller 所需资源的 informer 和 lister, 并注册 eventHandler 方法.

源码位置: <https://github.com/kubernetes/ingress-nginx/blob/main/internal/ingress/controller/store/store.go>

```
func New(
    namespace string,
    ...
    updateCh *channels.RingChannel) Storer {

    store := &k8sStore{
        informers:             &Informer{},     // 各资源 informers 的集合
        listers:               &Lister{},       // informers listers 集合
        updateCh:              updateCh,        // 通知给 syncqueue 的通道
        backendConfig:         ngx_config.NewDefault(), // 获取 nginx 模板中需要的默认变量, 比如缓冲大小呀, keepalive 配置, http2 相关配置等, 另外默认 WorkerProcesses 为当前的cpu核心数.
    }

    // 实例化 nginx ingress controller 所需资源的 informer 和 lister.
    store.informers.Ingress = infFactory.Networking().V1().Ingresses().Informer()
    store.listers.Ingress.Store = store.informers.Ingress.GetStore()
    store.informers.EndpointSlice = infFactory.Discovery().V1().EndpointSlices().Informer()
    store.listers.EndpointSlice.Store = store.informers.EndpointSlice.GetStore()
    store.informers.Secret = infFactorySecrets.Core().V1().Secrets().Informer()
    store.listers.Secret.Store = store.informers.Secret.GetStore()
    store.informers.ConfigMap = infFactoryConfigmaps.Core().V1().ConfigMaps().Informer()
    store.listers.ConfigMap.Store = store.informers.ConfigMap.GetStore()
    store.informers.Service = infFactory.Core().V1().Services().Informer()
    store.listers.Service.Store = store.informers.Service.GetStore()

    ...
    // 巴拉巴拉, 实现了各类 informer 的 eventHandler 方法.
    ...

    // 监听 ingress 资源并注册方法
    store.informers.Ingress.AddEventHandler(ingEventHandler)

    // 监听 ...