---
title: 源码分析 kubernetes kubelet pod 管理的设计实现
url: https://buaq.net/go-140487.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:13.897474
---

# 源码分析 kubernetes kubelet pod 管理的设计实现

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

源码分析 kubernetes kubelet pod 管理的设计实现

源码分析启动入口实例化 kubelet 服务实例, 并启动 syncLoop 调度核心.代码位置: pkg/kubelet/kubelet.gofunc Run
*2022-12-18 17:59:7
Author: [xiaorui.cc(查看原文)](/jump-140487.htm)
阅读量:27
收藏*

---

## 源码分析

### 启动入口

实例化 kubelet 服务实例, 并启动 syncLoop 调度核心.

代码位置: `pkg/kubelet/kubelet.go`

```
func RunKubelet(kubeServer *options.KubeletServer, kubeDeps *kubelet.Dependencies, runOnce bool) error {
    // 创建且实例化 kubelet 服务
    k, err := createAndInitKubelet(kubeServer,
        kubeDeps,
        hostname,
        hostnameOverridden,
        nodeName,
        nodeIPs)
    if err != nil {
        return fmt.Errorf("failed to create kubelet: %w", err)
    }
    podCfg := kubeDeps.PodConfig

    // 启动 kubelet
    startKubelet(k, podCfg, &kubeServer.KubeletConfiguration, kubeDeps, kubeServer.EnableServer)
}

// 启动 kubelet
func startKubelet(k kubelet.Bootstrap, podCfg *config.PodConfig, ...) {
    go k.Run(podCfg.Updates())
}

func (kl *Kubelet) Run(updates <-chan kubetypes.PodUpdate) {
    ctx := context.Background()

    ...

    kl.pleg.Start()

    // kubelet 的核心调度代码
    kl.syncLoop(ctx, updates, kl)
}
```

updates 这个管道很重要，在初始化 `kubelet` 对象时, 内部通过 `makePodSourceConfig` 方法可以监听 apiserver 的配置更新, 把更新的事件扔到这个 updates 管道里. 另外它还监听了文件及http的接口.

调用关系: `createAndInitKubelet -> NewMainKubelet -> makePodSourceConfig`

```
func makePodSourceConfig(kubeCfg *kubeletconfiginternal.KubeletConfiguration, kubeDeps *Dependencies, nodeName types.NodeName, nodeHasSynced func() bool) (*config.PodConfig, error) {
    // source of all configuration
    cfg := config.NewPodConfig(config.PodConfigNotificationIncremental, kubeDeps.Recorder, kubeDeps.PodStartupLatencyTracker)

    // define file config source
    if kubeCfg.StaticPodPath != "" {
        klog.InfoS("Adding static pod path", "path", kubeCfg.StaticPodPath)
        config.NewSourceFile(kubeCfg.StaticPodPath, nodeName, kubeCfg.FileCheckFrequency.Duration, cfg.Channel(ctx, kubetypes.FileSource))
    }

    // define url config source
    if kubeCfg.StaticPodURL != "" {
        klog.InfoS("Adding pod URL with HTTP header", "URL", kubeCfg.StaticPodURL, "header", manifestURLHeader)
        config.NewSourceURL(kubeCfg.StaticPodURL, manifestURLHeader, nodeName, kubeCfg.HTTPCheckFrequency.Duration, cfg.Channel(ctx, kubetypes.HTTPSource))
    }

    if kubeDeps.KubeClient != nil {
        klog.InfoS("Adding apiserver pod source")
        config.NewSourceApiserver(kubeDeps.KubeClient, nodeName, nodeHasSynced, cfg.Channel(ctx, kubetypes.ApiserverSource))
    }
    return cfg, nil
}
```

### 调度核心 (syncLoop)

syncLoop 是 kubelet 的调度核心, 内部定义了两个定时器, 一个用来同步的 syncTicker 定时器, 一个是 用来清理异常 pods 的 housekeepingTicker 定时器.

循环调度 syncLoopIteration 方法.

```
func (kl *Kubelet) syncLoop(ctx context.Context, updates <-chan kubetypes.PodUpdate, handler SyncHandler) {
    klog.InfoS("Starting kubelet main sync loop")

    syncTicker := time.NewTicker(time.Second)
    defer syncTicker.Stop()

    housekeepingTicker := time.NewTicker(housekeepingPeriod)
    defer housekeepingTicker.Stop()

    plegCh := kl.pleg.Watch()

    ...
    for {
        kl.syncLoopMonitor.Store(kl.clock.Now())
        if !kl.syncLoopIteration(ctx, updates, handler, syncTicker.C, housekeepingTicker.C, plegCh) {
            break
        }
        kl.syncLoopMonitor.Store(kl.clock.Now())
    }
}
```

kubelet 的 pods 同步逻辑都在 `syncLoopIteration` 这里. `syncLoopIteration` 同时监听下面的 chan, 根据事件做不同的处理.

* configCh: 监听 file, http, apiserver 的事件更新
* syncCh: 定时器管道, 每隔一秒去同步最新保存的 pod 状态
* houseKeepingCh: housekeeping 事件的管道，做 pod 清理工作
* plegCh: 该信息源由 kubelet 对象中的 pleg 子模块提供，该模块主要用于周期性地向 container runtime 查询当前所有容器的状态.
* livenessManager.Updates: 健康检查发现某个 pod 不可用, kubelet 将根据 Pod 的 restartPolicy 自动执行正确的操作

```
func (kl *Kubelet) syncLoopIteration(ctx context.Context, configCh <-chan kubetypes.PodUpdate, handler SyncHandler,
    syncCh <-chan time.Time, housekeepingCh <-chan time.Time, plegCh <-chan *pleg.PodLifecycleEvent) bool {

    select {
    case u, open := <-configCh: // 来自 apiserver 的 pod 事件
        if !open {
            return false
        }

        switch u.Op {
        case kubetypes.ADD: // 添加
            handler.HandlePodAdditions(u.Pods)
        case kubetypes.UPDATE: // 更新
            handler.HandlePodUpdates(u.Pods)
        case kubetypes.RECONCILE: // 协调
            handler.HandlePodReconcile(u.Pods)
        case kubetypes.DELETE: // 删除
            handler.HandlePodUpdates(u.Pods)
        default:
            klog.ErrorS(nil, "Invalid operation type received", "operation", u.Op)
        }

        kl.sourcesReady.AddSource(u.Source)

    case e := <-plegCh: // 由 pleg 子模块上报的事件, pleg 会扫描当前所有容器, 当状态发生变更时发出事件
        if isSyncPodWorthy(e) {
            if pod, ok := kl.podManager.GetPodByUID(e.ID); ok {
                handler.HandlePodSyncs([]*v1.Pod{pod})
            }
        }

        if e.Type == pleg.ContainerDied {
            if containerID, ok := e.Data.(string); ok {
                kl.cleanUpContainersInPod(e.ID, containerID)
            }
        }
    case <-syncCh: // 由定时器触发更新
        podsToSync := kl.getPodsToSync()
        handler.HandlePodSyncs(podsToSync)
    case update := <-kl.livenessManager.Updates(): // 当 liveness 状态发生变更时
        if update.Result == proberesults.Failure {
            handleProbeSync(kl, update, handler, "liveness", "unhealthy")
        }
    case update := <-kl.readinessManager.Updates(): // 当 readiness 状态变更时
        kl.statusManager.SetContainerReadiness(update.PodUID, update.ContainerID, ready)

        handleProbeSync(kl, update, handler, "readiness", status)
    case update := <-kl.startupManager.Updates(): // 当 startup 状态变更时
        kl.statusManager.SetContainerStartup(update.PodUID, update.ContainerID, started)
        handleProbeSync(kl, update, handler, "startup", status)

    case <-housekeepingCh: // 定时器触发
        handler.HandlePodCleanups(ctx)
    }
    return true
}
```

### 增加 pod 流程 (HandlePodAdditions)

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202212/202212181730298.png)

`HandlePodAdditions` 是创建 Pod 的核心代码. 首先对传入的 pods 进行排序, 保证先提交创建请求的 pod 被先创建, 最后调用 dispatchWork 来创建 pod.

另外静态 pod 是走 `handleMirrorPod` 流程.

```
func (kl *Kubelet) HandlePodAdditions(pods []*v1.Pod) {
    start := kl.clock.Now()

    // 按照创建事件的先后对传入的 pods 进行排序, 保证是 fifo 的模型.
    sort.Sort(sliceutils.PodsByCreationTime(pods))
    for _, pod := range pods {
        existingPods := kl.podManager.GetPods()

        // 把 pod 添加到 podManager 里
        kl.podManager.AddPod(pod)

        // 判断是否是静态 pod
        if kubetypes.IsMirrorPod(pod) {
            kl.handleMirrorPod(pod, start)
            continue
        }

        // 在 dispatchWork 里去做 pod 操作, 这里操作为创建 pod
        kl.dispatchWork(pod, kubetypes.SyncPodCreate, mirrorPod, start)
    }
}
```

另外, 主调度核心里对 pod 进行增删改操作, 其实最后都会跳到 dispatchWork 方法上.

该方法里主要定义了类型 `kubetypes.SyncPodType`, 然后调用 `podWrokers.UpdatePod` 异步操作 pod.

代码位置: `pkg/kubelet/pod_workers.go`

```
func (kl *Kubelet) dispatchWork(pod *v1.Pod, syncType kubetypes.SyncPodType, mirrorPod *v1.Pod, start time.Time) {
    // Run the sync in an async worker.
    kl.podWorkers.UpdatePod(UpdatePodOptions{
        Pod:        pod,
        MirrorPod:  mirrorPod,
        UpdateType: syncType,
        StartTime:  start,
    })
}
```

由于 kubelet 创建 pod 容器路径太深, 索性忽略下面的路径，直接跳到 syncPod 方法中.

`podWorkers.UpdatePod -> podWorkers.managePodLoop -> podWorkers.syncPodFn -> kubelet.syncPod`

#### 为 pod 做准备工作及创建 pod ( syncPod )

kubelet.syncPod 主要用来实现 pod 资源的创建, 内部会做好 pod 的准备工作, 流程如下:

1. 更新 pod 状态到 statusManager
2. 检查网络插件是否就绪
3. 把 pod 注册到 secretManage...