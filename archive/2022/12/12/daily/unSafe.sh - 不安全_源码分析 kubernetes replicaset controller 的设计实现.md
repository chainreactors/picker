---
title: 源码分析 kubernetes replicaset controller 的设计实现
url: https://buaq.net/go-139517.html
source: unSafe.sh - 不安全
date: 2022-12-12
fetch_date: 2025-10-04T01:14:29.853262
---

# 源码分析 kubernetes replicaset controller 的设计实现

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

源码分析 kubernetes replicaset controller 的设计实现

replicaset controller 作用replicaset controller 是 kube-controller-manager 组件中负责 repl
*2022-12-11 13:15:17
Author: [xiaorui.cc(查看原文)](/jump-139517.htm)
阅读量:16
收藏*

---

## replicaset controller 作用

`replicaset controller` 是 `kube-controller-manager` 组件中负责 replicaset 资源对象的控制器, 内部通过 informer 监听 pod 和 replicaSet 两个资源.

`replicaset controller` 主要作用是根据 replicaSet 对象所期望的 pod 数量与现存 pod 数量做比较，然后根据比较结果来选择扩容创建还是缩容删除 pod, 最终使得 replicaset 对象里预期 pod 数量和当前激活的 pod 数量相等.

## replicaset controller 源码分析

`基于 kubernetes v1.27.0 进行源码分析.`

![](https://xiaorui-cc.oss-cn-hangzhou.aliyuncs.com/images/202212/202212111048962.png)

* [实例化副本控制器](#实例化副本控制器)
* [启动副本控制器](https://xiaorui.cc/archives/%E5%90%AF%E5%8A%A8%E5%89%AF%E6%9C%AC%E6%8E%A7%E5%88%B6%E5%99%A8)
* [控制器内的 informer 监听](https://xiaorui.cc/archives/%E6%8E%A7%E5%88%B6%E5%99%A8%E5%86%85%E7%9A%84-informer-%E7%9B%91%E5%90%AC)
* [核心同步管理副本集](https://xiaorui.cc/archives/%E6%A0%B8%E5%BF%83%E5%90%8C%E6%AD%A5%E7%AE%A1%E7%90%86%E5%89%AF%E6%9C%AC%E9%9B%86)

### 实例化副本控制器

kube-controller-manager 会注册各种的 controller 控制器，其中包括 replicaSet 副本控制器.

startReplicaSetController 为 replicaSet controller 的启动入口，通过 NewReplicaSetController() 方法实例化控制器.

源码位置: `cmd/kube-controller-manager/app/apps.go`

```
func startReplicaSetController(ctx context.Context, controllerContext ControllerContext) (controller.Interface, bool, error) {
    go replicaset.NewReplicaSetController(
        controllerContext.InformerFactory.Apps().V1().ReplicaSets(),
        controllerContext.InformerFactory.Core().V1().Pods(),
    ).Run(ctx, int(controllerContext.ComponentConfig.ReplicaSetController.ConcurrentRSSyncs))
    return nil, true, nil
}
```

### 启动副本控制器

NewBaseController 是 replicaSet controller 的具体实现, 初始化时其内部会启动监听 replicaset 和 pod 资源的 informer, 并且注册了增删改对应的回调方法.

```
func NewReplicaSetController(rsInformer appsinformers.ReplicaSetInformer, podInformer coreinformers.PodInformer, kubeClient clientset.Interface, burstReplicas int) *ReplicaSetController {
    return NewBaseController(rsInformer, podInformer, kubeClient, burstReplicas,
        ...
    )
}

func NewBaseController(rsInformer appsinformers.ReplicaSetInformer, podInformer coreinformers.PodInformer, kubeClient clientset.Interface, burstReplicas int,
    gvk schema.GroupVersionKind, metricOwnerName, queueName string, podControl controller.PodControlInterface, eventBroadcaster record.EventBroadcaster) *ReplicaSetController {

    rsc := &ReplicaSetController{}

    rsInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc:    rsc.addRS,
        UpdateFunc: rsc.updateRS,
        DeleteFunc: rsc.deleteRS,
    })

    podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc: rsc.addPod,
        UpdateFunc: rsc.updatePod,
        DeleteFunc: rsc.deletePod,
    })

    rsc.syncHandler = rsc.syncReplicaSet

    return rsc
}
```

`Run()` 启动 rs 控制器, 并发启动 workers 数量的协程, 通过 `wait.UntilWithContext` 定时拉起 worker 处理函数.

`workers` 这个参数很重要，影响了 rs 控制器的处理性能, 调高此数值自然可以提供 rsc 的效率, 初始化配置里 `ConcurrentRSSyncs` 默认为 5.

```
func (rsc *ReplicaSetController) Run(ctx context.Context, workers int) {
    // 等待 informer 完成同步缓存
    if !cache.WaitForNamedCacheSync(rsc.Kind, ctx.Done(), rsc.podListerSynced, rsc.rsListerSynced) {
        return
    }

    for i := 0; i < workers; i++ {
        go wait.UntilWithContext(ctx, rsc.worker, time.Second)
    }

    <-ctx.Done()
}
```

worker 处理函数相对简单，就是从 queue 里获取 key, 然后调用 syncHandler 处理, 如果失败则调用 queue 进行重入队.

```
func (rsc *ReplicaSetController) worker(ctx context.Context) {
    for rsc.processNextWorkItem(ctx) {
    }
}

func (rsc *ReplicaSetController) processNextWorkItem(ctx context.Context) bool {
    // 从队列获取数据
    key, quit := rsc.queue.Get()
    if quit {
        return false
    }
    defer rsc.queue.Done(key)

    // syncHandler 核心处理函数
    err := rsc.syncHandler(ctx, key.(string))
    if err == nil {
        rsc.queue.Forget(key)
        return true
    }

    // 如果增删 pod 有异常, 则重新推到队列中, 等待下次重试.
    rsc.queue.AddRateLimited(key)

    return true
}
```

### 控制器内的 informer 监听

rsc 通过 informer 机制来监听处理 rs 和 pod 资源变动.

#### replicaSet informer

在 replicaSet informer 上注册增删改的 eventHandler, 这些逻辑都相对简单, 直接入队列就行了, 等待后面的 worker 协程去驱动 `syncReplicaSet` 来处理.

* 当 add rs 时, syncReplicaSet 识别有新 rs 被创建, 则创建 rs 对应的 pods.
* 当 delete rs 时, syncReplicaSet 在 expectations 找不到, 则进行清理.
* 当 update rs 时, syncReplicaSet 会进行副本数的协调同步.

```
func (rsc *ReplicaSetController) addRS(obj interface{}) {
    // 直接入队列
    rs := obj.(*apps.ReplicaSet)
    rsc.enqueueRS(rs)
}

func (rsc *ReplicaSetController) updateRS(old, cur interface{}) {
    oldRS := old.(*apps.ReplicaSet)
    curRS := cur.(*apps.ReplicaSet)
    ...

    // 如果新老配置的 replicas 副本数发生变更, 则打印出来.
    if *(oldRS.Spec.Replicas) != *(curRS.Spec.Replicas) {
        klog.V(4).Infof("%v %v updated. Desired pod count change: %d->%d", rsc.Kind, curRS.Name, *(oldRS.Spec.Replicas), *(curRS.Spec.Replicas))
    }
    // 入队
    rsc.enqueueRS(curRS)
}

func (rsc *ReplicaSetController) deleteRS(obj interface{}) {
    rs, ok := obj.(*apps.ReplicaSet)
    key, err := controller.KeyFunc(rs)

    // 在 expectations 里删除.
    rsc.expectations.DeleteExpectations(key)

    // 入队
    rsc.queue.Add(key)
}
```

enqueueRs 是入队列的逻辑, 从 rs 对象获取 namespace/name 格式的 key, 后扔到 rsc 队列即可.

```
func (rsc *ReplicaSetController) enqueueRS(rs *apps.ReplicaSet) {
    key, err := controller.KeyFunc(rs)
    if err != nil {
        utilruntime.HandleError(fmt.Errorf("couldn't get key for object %#v: %v", rs, err))
        return
    }

    rsc.queue.Add(key)
}
```

#### pod informer

`addPod` 和 `deletePod` 主逻辑是先操作下 expectations, 遇到 add 时加一, 遇到 del 时减一, 然后把 rs 入队列里, 当 `syncReplicaSet` 处理时发现当前跟预期的副本数不一致, 进行同步协调.

updatePod 的事件代码相对麻烦点, 内有各种的条件判断, 请直接看下面代码中的注释.

```
func (rsc *ReplicaSetController) addPod(obj interface{}) {
    pod := obj.(*v1.Pod)

    // 如果 pod 字段不为空，则删除.
    if pod.DeletionTimestamp != nil {
        rsc.deletePod(pod)
        return
    }

    if controllerRef := metav1.GetControllerOf(pod); controllerRef != nil {
        rs := rsc.resolveControllerRef(pod.Namespace, controllerRef)
        rsKey, err := controller.KeyFunc(rs)

        // 在 expectations 里把 add 字段加一.
        rsc.expectations.CreationObserved(rsKey)

        // 把 rskey 推到队列里
        rsc.queue.Add(rsKey)
        return
    }

    // 走到这里说明是孤儿 pod, 获取 pod 所属的 rs 集合
    rss := rsc.getPodReplicaSets(pod)
    if len(rss) == 0 {
        return // 没找到对应 rs 则忽略.
    }
    for _, rs := range rss {
        // 把 rs 扔到队列里, 让后面的同步流程去清理
        rsc.enqueueRS(rs)
    }
}

func (rsc *ReplicaSetController) deletePod(obj interface{}) {
    pod, ok := obj.(*v1.Pod)

    controllerRef := metav1.GetControllerOf(pod)
    rs := rsc.resolveControllerRef(pod.Namespace, controllerRef)

    // 在 expectations 里找到 rskey 对应的 exp, 在 del 字段 -1
    rsKey, err := controller.KeyFunc(rs)
    rsc.expectations.DeletionObserved(rsKey, controller.PodKey(pod))

    // 把 rskey 插入到队列里
    rsc.queue.Add(rsKey)
}

func (rsc *ReplicaSetController) updatePod(old, cur interface{}) {
    curPod := cur.(*v1.Pod)
    oldPod := old.(*v1.Pod)
    if curPod.ResourceVersion == oldPod.ResourceVersion {
        return
    }

    // 如果 pod label 改变或者处于删除状态，则直接删除
    labelChanged := !reflect.DeepEqual(curPod.Labels, oldPod.Labels)
    if curPod.DeletionTimestamp != nil {
        rsc.deletePod(curPod)
        if labelChanged {
            rsc.deletePod(oldPod)
        }
        return
    }

    // 如果 pod 的 OwnerReference 发生改变，将 oldRS 入队
    curControllerRef := metav1.GetContr...