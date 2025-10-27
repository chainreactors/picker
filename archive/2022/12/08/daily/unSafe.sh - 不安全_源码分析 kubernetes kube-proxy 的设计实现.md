---
title: 源码分析 kubernetes kube-proxy 的设计实现
url: https://buaq.net/go-139045.html
source: unSafe.sh - 不安全
date: 2022-12-08
fetch_date: 2025-10-04T00:52:02.811337
---

# 源码分析 kubernetes kube-proxy 的设计实现

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

源码分析 kubernetes kube-proxy 的设计实现

kubernetes kube-proxy 的版本是 v1.27.0cmd 入口kube-proxy 启动的过程就不细说了，简单说就是解析传递配置，构建 Prox
*2022-12-7 22:6:54
Author: [xiaorui.cc(查看原文)](/jump-139045.htm)
阅读量:28
收藏*

---

`kubernetes kube-proxy 的版本是 v1.27.0`

### cmd 入口

`kube-proxy` 启动的过程就不细说了，简单说就是解析传递配置，构建 `ProxyServer` 服务，最后启动 `ProxyServer`.

```
cmd/kube-proxy/proxy.go: main
    cmd/kube-proxy/app/server.go: NewProxyCommand
        cmd/kube-proxy/app/server.go: ProxyServer.Run()
```

### ProxyServer

在创建 `NewProxyServer()` 时，根据 `proxyMode` 实例化不同的 proxier 对象. 在 kube-proxy 里 proxier 有iptables 和 ipvs 两种实现, 以前在 userspace 实现的代理已经在老版本中剔除了.

代码位置: `cmd/kube-proxy/app/server.go`

```
// NewProxyServer returns a new ProxyServer.
func NewProxyServer(o *Options) (*ProxyServer, error) {
    return newProxyServer(o.config, o.master)
}

func newProxyServer(
    config *proxyconfigapi.KubeProxyConfiguration,
    master string) (*ProxyServer, error) {

    // 实例化 iptables 的 proxy
    if proxyMode == proxyconfigapi.ProxyModeIPTables {
        if dualStack {
        } else {
            proxier, err = iptables.NewProxier(
                iptInterface,
                utilsysctl.New(),
                execer,
                config.IPTables.SyncPeriod.Duration,
                config.IPTables.MinSyncPeriod.Duration,
                ...
            )
        }

    // 实例化 ipvs 的 proxy
    } else if proxyMode == proxyconfigapi.ProxyModeIPVS {
        // 实例化 kernel, ipset，ipvs 管理工具
        kernelHandler := ipvs.NewLinuxKernelHandler()
        ipsetInterface = utilipset.New(execer)
        ipvsInterface = utilipvs.New()

        if dualStack {
        } else {
            if err != nil {
                return nil, fmt.Errorf("unable to create proxier: %v", err)
            }

            proxier, err = ipvs.NewProxier(
                iptInterface,
                ipvsInterface,
                ipsetInterface,
                utilsysctl.New(),
                ...
            )
        }
        ...
    }

    return &ProxyServer{
        Client:                 client,
        EventClient:            eventClient,
        IptInterface:           iptInterface,
        IpvsInterface:          ipvsInterface,
        IpsetInterface:         ipsetInterface,
        ...
    }, nil
}
```

`ProxyServer` 在调用 Run() 启动时会实例化 informer 监听器，然后一直监听 apiserver 反馈的 service, endpoints, node 变动事件.

```
func (s *ProxyServer) Run() error {
    informerFactory := informers.NewSharedInformerFactoryWithOptions(s.Client, s.ConfigSyncPeriod,
        informers.WithTweakListOptions(func(options *metav1.ListOptions) {
            options.LabelSelector = labelSelector.String()
        }))

    // 监听 service resource 资源
    serviceConfig := config.NewServiceConfig(informerFactory.Core().V1().Services(), s.ConfigSyncPeriod)
    serviceConfig.RegisterEventHandler(s.Proxier)
    go serviceConfig.Run(wait.NeverStop)

    // 监听 endpoints resource 资源
    endpointSliceConfig := config.NewEndpointSliceConfig(informerFactory.Discovery().V1().EndpointSlices(), s.ConfigSyncPeriod)
    endpointSliceConfig.RegisterEventHandler(s.Proxier)
    go endpointSliceConfig.Run(wait.NeverStop)

    informerFactory.Start(wait.NeverStop)

    // 监听 node 资源更新
    currentNodeInformerFactory := informers.NewSharedInformerFactoryWithOptions(s.Client, s.ConfigSyncPeriod,
        informers.WithTweakListOptions(func(options *metav1.ListOptions) {
            options.FieldSelector = fields.OneTermEqualSelector("metadata.name", s.NodeRef.Name).String()
        }))
    nodeConfig := config.NewNodeConfig(currentNodeInformerFactory.Core().V1().Nodes(), s.ConfigSyncPeriod)
    nodeConfig.RegisterEventHandler(s.Proxier)
    go nodeConfig.Run(wait.NeverStop)

    currentNodeInformerFactory.Start(wait.NeverStop)

    s.birthCry()

    go s.Proxier.SyncLoop()

    return <-errCh
}
```

### 如何监听和处理事件 ?

kube-proxy 开启了对 services 和 endpoints 的事件监听，但篇幅原因这里就只聊 Services 的事件监听.

初始化阶段时会实例化 ServiceConfig 对象， 并向 serviceConfig 注册 proxier 对象. `ServiceConfig` 实现了对 informer 的监听，并向 informer 注册封装的回调接口. 当有 service 的增删改事件时, 调用 proxier 的 `OnServiceAdd, OnServiceUpdate, OnServiceDelete` 方法.

```
type ServiceConfig struct {
    listerSynced  cache.InformerSynced
    eventHandlers []ServiceHandler
}

// NewServiceConfig creates a new ServiceConfig.
func NewServiceConfig(serviceInformer coreinformers.ServiceInformer, resyncPeriod time.Duration) *ServiceConfig {
    result := &ServiceConfig{
        listerSynced: serviceInformer.Informer().HasSynced,
    }

    serviceInformer.Informer().AddEventHandlerWithResyncPeriod(
        cache.ResourceEventHandlerFuncs{
            AddFunc:    result.handleAddService,
            UpdateFunc: result.handleUpdateService,
            DeleteFunc: result.handleDeleteService,
        },
        resyncPeriod,
    )

    return result
}

// 注册事件处理，其实就是 proxier, 它实现了 ServiceHandler 接口.
func (c *ServiceConfig) RegisterEventHandler(handler ServiceHandler) {
    c.eventHandlers = append(c.eventHandlers, handler)
}

func (c *ServiceConfig) Run(stopCh <-chan struct{}) {
    // 第一次启动时, 同步下数据到缓存
    if !cache.WaitForNamedCacheSync("service config", stopCh, c.listerSynced) {
        return
    }

    // proxier 的 OnServiceSynced 实现是调用 `proxier.syncProxyRules()`
    for i := range c.eventHandlers {
        c.eventHandlers[i].OnServiceSynced()
    }
}

// 处理 service 新增事件
func (c *ServiceConfig) handleAddService(obj interface{}) {
    service, ok := obj.(*v1.Service)
    for i := range c.eventHandlers {
        c.eventHandlers[i].OnServiceAdd(service)
    }
}

// 处理 service 更新事件
func (c *ServiceConfig) handleUpdateService(oldObj, newObj interface{}) {
    oldService, ok := oldObj.(*v1.Service)
    for i := range c.eventHandlers {
        c.eventHandlers[i].OnServiceUpdate(oldService, service)
    }
}

// 处理 service 删除事件
func (c *ServiceConfig) handleDeleteService(obj interface{}) {
    service, ok := obj.(*v1.Service)
    for i := range c.eventHandlers {
        c.eventHandlers[i].OnServiceDelete(service)
    }
}
```

从 ipvs 的 proxier 里, 分析下 `OnServiceAdd`, `OnServiceUpdate`, `OnServiceDelete` 这几个方法的实现. 其实就是对 proxier 的 `serviceChanges` 做存储变动对象操作. 需要注意的是，真正处理变动的在 `proxier.syncProxyRules()` 方法里.

```
// OnServiceAdd is called whenever creation of new service object is observed.
func (proxier *Proxier) OnServiceAdd(service *v1.Service) {
    proxier.OnServiceUpdate(nil, service)
}

// OnServiceUpdate is called whenever modification of an existing service object is observed.
func (proxier *Proxier) OnServiceUpdate(oldService, service *v1.Service) {
    if proxier.serviceChanges.Update(oldService, service) && proxier.isInitialized() {
        proxier.Sync()
    }
}

// OnServiceDelete is called whenever deletion of an existing service object is observed.
func (proxier *Proxier) OnServiceDelete(service *v1.Service) {
    proxier.OnServiceUpdate(service, nil)
}
```

### 真正干活 Proxier 的实现

在阅读了 kube-proxy 源码后可以发现，Proxier 才是真正干活的类，kube-proxy 里对于 ipvs，iptables, ipset 等工具的操作都在 proxier 里.

在 kube-proxy 中 proxier 有 iptables 和 ipvs 两种实现, 现在已经少有用 iptables 的了，所以就只分析 ipvs proxier 实现.

在实例化 `Proxier` 对象时会注册一个定时任务，它会周期性调用 `syncProxyRules` 方法.

```
func NewProxier(
    syncPeriod time.Duration,
    minSyncPeriod time.Duration,
    masqueradeAll bool,
    ...
) (*Proxier, error) {
    ...
    proxier := &Proxier{
        svcPortMap:            make(proxy.ServicePortMap),
        endpointsMap:          make(proxy.EndpointsMap),
        ...
    }

    ...
    proxier.syncRunner = async.NewBoundedFrequencyRunner("sync-runner", proxier.syncProxyRules, minSyncPeriod, syncPeri...