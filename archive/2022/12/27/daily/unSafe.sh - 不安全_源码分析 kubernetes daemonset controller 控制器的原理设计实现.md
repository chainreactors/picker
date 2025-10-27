---
title: 源码分析 kubernetes daemonset controller 控制器的原理设计实现
url: https://buaq.net/go-141480.html
source: unSafe.sh - 不安全
date: 2022-12-27
fetch_date: 2025-10-04T02:31:57.288863
---

# 源码分析 kubernetes daemonset controller 控制器的原理设计实现

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

源码分析 kubernetes daemonset controller 控制器的原理设计实现

基于 k8s v1.27.0 进行源码分析其原理.入口创建 daemonset controller 控制器对象, 并且在内部使用 informer 注册监听 da
*2022-12-26 23:12:4
Author: [xiaorui.cc(查看原文)](/jump-141480.htm)
阅读量:22
收藏*

---

基于 k8s `v1.27.0` 进行源码分析其原理.

### 入口

创建 daemonset controller 控制器对象, 并且在内部使用 informer 注册监听 daemonset, pod, node 资源的变更事件. 注册 eventHandler 没什么可说的，跟其他控制逻辑类型，就是把对象往 queue 里推.

```
func NewDaemonSetsController(
    ...
) (*DaemonSetsController, error) {
    dsc := &DaemonSetsController{
        ...
    }

    // daemonset informer
    daemonSetInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc:    dsc.addDaemonset,
        UpdateFunc: dsc.updateDaemonset,
        DeleteFunc: dsc.deleteDaemonset,
    })

    // pod informer
    podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc:    dsc.addPod,
        UpdateFunc: dsc.updatePod,
        DeleteFunc: dsc.deletePod,
    })

    // node informer
    nodeInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc:    dsc.addNode,
        UpdateFunc: dsc.updateNode,
    })

    return dsc, nil
}
```

`Run()` 启动时要确保各个 informer 同步完毕，`cache.WaitForNamedCacheSync` 的实现很简单，就是周期性的判断所有的 `informer` 是否 synced 同步完成, 一直轮询知道成功同步完毕. 启动多个 `runWorker` 协程, 接着启动一个 gc 回收协程.

`informer` 会把事件生成 key, 怼到队列里, runwokrer 会监听 queue, 然后调用 syncHandler 去完成 daemonset 的同步状态. syncHandler 的具体实现函数是 `syncDaemonSet` 方法.

```
func (dsc *DaemonSetsController) Run(ctx context.Context, workers int) {
    // 启动时要确保各个 informer 同步完毕， WaitForNamedCacheSync 的实现很简单，就是周期性的判断所有的 informer 是否 synced 同步完成, 一直轮询到成功.
    if !cache.WaitForNamedCacheSync("daemon sets", ctx.Done(), dsc.podStoreSynced, dsc.nodeStoreSynced, dsc.historyStoreSynced, dsc.dsStoreSynced) {
        return
    }

    // 启动多个 runWorker
    for i := 0; i < workers; i++ {
        go wait.UntilWithContext(ctx, dsc.runWorker, time.Second)
    }

    // 启动 gc 回收
    go wait.Until(dsc.failedPodsBackoff.GC, BackoffGCInterval, ctx.Done())

    <-ctx.Done()
}

func (dsc *DaemonSetsController) runWorker(ctx context.Context) {
    // 一直循环调用, controller 只有运行，没有退出，当然也不需要退出.
    for dsc.processNextWorkItem(ctx) {
    }
}

func (dsc *DaemonSetsController) processNextWorkItem(ctx context.Context) bool {
    // 从队列里获取 daemonset key, queue 内部有条件变量，拿不到资源会陷入等待.
    dsKey, quit := dsc.queue.Get()
    if quit {
        return false
    }
    defer dsc.queue.Done(dsKey)

    // 执行同步函数, syncHanlder 是 ds 里关键业务处理入口
    err := dsc.syncHandler(ctx, dsKey.(string))
    if err == nil {
        dsc.queue.Forget(dsKey)
        return true
    }

    dsc.queue.AddRateLimited(dsKey)
    return true
}
```

### 同步管理 daemonset 配置

关键函数的调用关系如下:

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202212/202212262247518.png)

#### syncDaemonSet

下面是 `syncDaemonSet` 的流程:

1. 从 key 获取 namespace 和 name.
2. 从 ds infomrer lister 里获取 ds 对象.
3. 获取所有的 node 集合.
4. 判断是否满足 expectations 条件, 当不满足预期时, 只更新状态即可, 满足则继续运行.
5. 同步 daemonset 配置.
6. 更新 daemonset status 状态.

```
func (dsc *DaemonSetsController) syncDaemonSet(ctx context.Context, key string) error {
    // 从 key 拆分 namespace 和 ds name, key 的格式为 namespace/name
    namespace, name, err := cache.SplitMetaNamespaceKey(key)
    if err != nil {
        return err
    }

    // 从 informer list 里获取 ds 对象
    ds, err := dsc.dsLister.DaemonSets(namespace).Get(name)
    if apierrors.IsNotFound(err) { // 找不到则直接跳出
        return nil
    }

    // 获取所有 node 列表
    nodeList, err := dsc.nodeLister.List(labels.Everything())
    if err != nil {
        return err
    }

    // 获取 dskey
    dsKey, err := controller.KeyFunc(ds)

    // 通过 ds 获取 current, old 的 constructHistory
    cur, old, err := dsc.constructHistory(ctx, ds)
    if err != nil {
        return fmt.Errorf("failed to construct revisions of DaemonSet: %v", err)
    }
    hash := cur.Labels[apps.DefaultDaemonSetUniqueLabelKey]

    // 是否满足 expectations 条件, 当不满足预期时, 只更新状态即可.
    if !dsc.expectations.SatisfiedExpectations(dsKey) {
        return dsc.updateDaemonSetStatus(ctx, ds, nodeList, hash, false)
    }

    // 更新 daemonset, 关键函数
    err = dsc.updateDaemonSet(ctx, ds, nodeList, hash, dsKey, old)

    // 更新 daemonset 的 status 状态
    statusErr := dsc.updateDaemonSetStatus(ctx, ds, nodeList, hash, true)
    ...
    return nil
}
```

#### updateDaemonSet

分析代码得知 `updateDaemonSet()` 的流程如下:

1. `updateDaemonSet()` 内部通过 `manage` 来同步 daemonset 的状态.
2. 当满足 expectations 且更新策略为 `RollingUpdate` 滚动更新, 则调用 `rollingUpdate` 进行滚动更新.
3. 最后调用 `cleanupHistory` 来进行清理过期的 `ControllerRevision`.

```
func (dsc *DaemonSetsController) updateDaemonSet(ctx context.Context, ds *apps.DaemonSet, nodeList []*v1.Node, hash, key string, old []*apps.ControllerRevision) error {
    // 处理 daemonset
    err := dsc.manage(ctx, ds, nodeList, hash)
    if err != nil {
        return err
    }

    if dsc.expectations.SatisfiedExpectations(key) {
        switch ds.Spec.UpdateStrategy.Type {
        case apps.OnDeleteDaemonSetStrategyType:
        case apps.RollingUpdateDaemonSetStrategyType:
            // 类型为 rollingUpdate, 则进行滚动更新
            err = dsc.rollingUpdate(ctx, ds, nodeList, hash)
        }
        if err != nil {
            return err
        }
    }

    // 清理不需要的 cleanupHistory
    err = dsc.cleanupHistory(ctx, ds, old)
    if err != nil {
        return fmt.Errorf("failed to clean up revisions of DaemonSet: %w", err)
    }

    return nil
}
```

#### manage

分析代码得知 `manage()` 的流程如下:

1. 通过 `getNodesToDaemonPods()` 获取 daemonset 和 node 关系, 返回的结构为 `map[node][]*v1.Pod`.
2. 遍历 node 集合, 通过 `podsShouldBeOnNode` 获取 node 需要创建和删除的 ds pods 集合.
3. `getUnscheduledPodsWithoutNode` 获取不能调度的 Pods 集合, 就是遍历 `nodeToDaemonPods`, 把不在 nodeList 集合里的 node 相关的 pods 追加到待删除集合里.
4. 调用 `syncNodes` 来在一些 node 上创建或者删除一些 daemonset pod.

```
func (dsc *DaemonSetsController) manage(ctx context.Context, ds *apps.DaemonSet, nodeList []*v1.Node, hash string) error {
    // 获取 node 和 ds 的对应关系
    nodeToDaemonPods, err := dsc.getNodesToDaemonPods(ctx, ds)
    if err != nil {
        return fmt.Errorf("couldn't get node to daemon pod mapping for daemon set %q: %v", ds.Name, err)
    }

    var nodesNeedingDaemonPods, podsToDelete []string
    // 遍历 node 集合
    for _, node := range nodeList {
        // 获取该 node 需要创建或者删除的 pods 集合.
        nodesNeedingDaemonPodsOnNode, podsToDeleteOnNode := dsc.podsShouldBeOnNode(
            node, nodeToDaemonPods, ds, hash)

        // 添加到待新增集合里
        nodesNeedingDaemonPods = append(nodesNeedingDaemonPods, nodesNeedingDaemonPodsOnNode...)

        // 添加到待删除集合里
        podsToDelete = append(podsToDelete, podsToDeleteOnNode...)
    }

    // 获取不能调度的 Pods 集合, 把不在 nodeList 集合里的 node 相关的 pods 追加到待删除集合里.
    podsToDelete = append(podsToDelete, getUnscheduledPodsWithoutNode(nodeList, nodeToDaemonPods)...)

    // 同步操作, 这里会执行添加和删除操作
    if err = dsc.syncNodes(ctx, ds, podsToDelete, nodesNeedingDaemonPods, hash); err != nil {
        return err
    }

    return nil
}
```

#### syncNodes

syncNodes 方法主要是为需要 daemonset 的 node 创建 pod 以及删除多余的 pod, 源码流程如下:

1. 计算本次 createDiff 和 deleteDiff 增减的个数, 每次 sync 最多执行 250 个, 多余的需要等待下次调用解决.
2. 提前先把 createDiff 和 deleteDiff 写入到 expectations 中.
3. 指数级增量批量创建 daemonset pod, 执行完毕后需要依次减少 expectations creation.
4. 直接遍历并发删除 daemonset pod, 执行完毕后需要减少 expectations deletion.

```
const (
    // BurstReplicas is a rate limiter for booting pods on a lot of pods.
    // 最多单词执行 250 个
    BurstReplicas = 250
)

func (dsc *DaemonSetsController) syncNodes(ctx context.Context, ds *apps.DaemonSet, podsToDelete, nodesNeedingDaemonPods []string,...