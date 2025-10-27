---
title: 源码分析 kubernetes cronjob controller 控制器的实现原理
url: https://buaq.net/go-143123.html
source: unSafe.sh - 不安全
date: 2022-12-30
fetch_date: 2025-10-04T02:42:56.016041
---

# 源码分析 kubernetes cronjob controller 控制器的实现原理

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

源码分析 kubernetes cronjob controller 控制器的实现原理

我们可以利用 CronJob 执行基于 crontab 调度的 Job 任务. 创建的 Job 资源是立即执行, 而使用 cronjob 后, 可以周期性的延迟创建 j
*2022-12-29 23:12:33
Author: [xiaorui.cc(查看原文)](/jump-143123.htm)
阅读量:19
收藏*

---

我们可以利用 CronJob 执行基于 crontab 调度的 Job 任务. 创建的 Job 资源是立即执行, 而使用 cronjob 后, 可以周期性的延迟创建 job 任务.

**一个例子**

每隔一分钟访问一下网站.

```
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - curl xiaorui.cc
          restartPolicy: OnFailure
```

**并发性规则**

`.spec.concurrencyPolicy` 也是可选的。它声明了 CronJob 创建的任务执行时发生重叠如何处理。 spec 仅能声明下列规则中的一种：

* Allow: CronJob 允许并发任务执行.
* Forbid: 如果新任务执行时, 老 job 还未完事, 则直接忽略.
* Replace: 如果新任务执行时, 老 job 还未完事, 则清理旧 job, 创建新 job 任务.

### 实例化入口

实例化 cronjob controller 控制器, 传递进去 job 和 cronjob 的 informer 对象, 注册 eventHandler.

在 jobInformer 里注册的 eventHandler 逻辑简单, 从 job 拿到 cronjob 对象然后格式化 key, 再扔到 queue 里, cronjob 也做了同样的逻辑.

```
func NewControllerV2(jobInformer batchv1informers.JobInformer, cronJobsInformer batchv1informers.CronJobInformer, kubeClient clientset.Interface) (*ControllerV2, error) {
    jm := &ControllerV2{
        queue:       workqueue.NewNamedRateLimitingQueue(workqueue.DefaultControllerRateLimiter(), "cronjob"),
        jobControl:     realJobControl{KubeClient: kubeClient},
        cronJobControl: &realCJControl{KubeClient: kubeClient},
        jobLister:     jobInformer.Lister(),
        cronJobLister: cronJobsInformer.Lister(),
    }

    // 在 job informer 注册 eventHandler
    jobInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc:    jm.addJob,
        UpdateFunc: jm.updateJob,
        DeleteFunc: jm.deleteJob,
    })

    // 在 cronjob informer 注册 eventHandler
    cronJobsInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc: func(obj interface{}) {
            jm.enqueueController(obj)
        },
        UpdateFunc: jm.updateCronJob,
        DeleteFunc: func(obj interface{}) {
            jm.enqueueController(obj)
        },
    })

    return jm, nil
}
```

### 启动入口

启动多个 worker 协程, 每个 worker 先从 queue 获取任务, 然后执行 sync 方法, 如果同步异常则扔到队列里重试. 如果无异常, 则根据下次执行时间把任务放到延迟队列里, 等待下次调度.

```
func (jm *ControllerV2) Run(ctx context.Context, workers int) {
    // 等待 job 和 cronjob 同步到本地
    if !cache.WaitForNamedCacheSync("cronjob", ctx.Done(), jm.jobListerSynced, jm.cronJobListerSynced) {
        return
    }

    // 启动多个 worker
    for i := 0; i < workers; i++ {
        go wait.UntilWithContext(ctx, jm.worker, time.Second)
    }

    // 阻塞, 直到 ctx 被取消
    <-ctx.Done()
}

func (jm *ControllerV2) worker(ctx context.Context) {
    for jm.processNextWorkItem(ctx) {
    }
}

func (jm *ControllerV2) processNextWorkItem(ctx context.Context) bool {
    // 从队列后去 cronjob 的 key
    key, quit := jm.queue.Get()
    if quit {
        return false
    }
    defer jm.queue.Done(key)

    // 执行 cronjob 的核心同步方法
    requeueAfter, err := jm.sync(ctx, key.(string))
    switch {
    case err != nil:
        // 失败, 把任务放到队列里进行重试
        jm.queue.AddRateLimited(key)

    case requeueAfter != nil:
        // 从队列中剔除
        jm.queue.Forget(key)

        // 通过上面的 sync 计算出下次执行的时间, 然后把任务放到 queue 的延迟队列里, 延迟时间为 requeueAfter.
        jm.queue.AddAfter(key, *requeueAfter)
    }
    return true
}
```

### 核心 sync 代码

`sync()` 是 cronjob controller 里核心处理代码的入口, 而 `syncCronJob()` 实现了 cronjob 的主要逻辑.

源码逻辑流程如下:

1. 从 informer lister 获取 cronjob 对象;
2. 获取 cronjob 关联的 jobs 对象集合;
3. 同步 cronjob 的状态, 按照不同的 `ConcurrencyPolicy` 策略, 选择不同的动作, 计算下次执行的时间;
4. 清理已经完成的 jobs;
5. 更新 cronjob 的状态.

```
func (jm *ControllerV2) sync(ctx context.Context, cronJobKey string) (*time.Duration, error) {
    // 从 key 中拆分 ns 和 name 字段
    ns, name, err := cache.SplitMetaNamespaceKey(cronJobKey)
    if err != nil {
        return nil, err
    }

    // 从 informer lister 获取 cronjob 对象
    cronJob, err := jm.cronJobLister.CronJobs(ns).Get(name)
    switch {
    case errors.IsNotFound(err):
        return nil, nil
    case err != nil:
        // for other transient apiserver error requeue with exponential backoff
        return nil, err
    }

    // 获取 cronjob 关联的 jobs 对象集合
    jobsToBeReconciled, err := jm.getJobsToBeReconciled(cronJob)
    if err != nil {
        return nil, err
    }

    // 获取 cronjob 对象, 下次执行的时间, 是否更新状态等
    cronJobCopy, requeueAfter, updateStatus, err := jm.syncCronJob(ctx, cronJob, jobsToBeReconciled)
    if err != nil {
        if updateStatus {
            // 更新 cronjob 的状态
            if _, err := jm.cronJobControl.UpdateStatus(ctx, cronJobCopy); err != nil {
                return nil, err
            }
        }
        return nil, err
    }

    // 清理已经完成的 jobs.
    if jm.cleanupFinishedJobs(ctx, cronJobCopy, jobsToBeReconciled) {
        updateStatus = true
    }

    // 更新 cronjob 的状态
    if updateStatus {
        if _, err := jm.cronJobControl.UpdateStatus(ctx, cronJobCopy); err != nil {
            return nil, err
        }
    }

    // 如果拿到了下次执行的 duration, 则返回该 duration
    if requeueAfter != nil {
        return requeueAfter, nil
    }
    return nil, nil
}
```

#### syncCronJob 同步定时任务

代码流程如下:

* 遍历 cronjob active 集合, 如果对应的 job 不再存在, 则从 active list 中删除 job 引用. 避免 cronjob 可能永远处于活动模式 ;
* 如果删除时间不为空, 说明该对象已被删除, 后面无需处理了 ;
* 该 cronjob 已暂停则直接退出 ;
* 获取开源 cron 库的调度解释器 ;
* 根据 crontab spec 表达式计算下次执行的时间;
* 如果配置了 ForbidConcurrent 策略, 且当前已经有 job 还在运行, 则直接跳出 ;
* 如果配置了 ReplaceConcurrent 策略, 则需要清理以前还在运行的 Job ;
* 获取 cronjob 对应的 job 模板, 然后创建 job 对象资源 ;
* 在 cronjob 对象里关联 job 对象, 记录 LastScheduleTime 时间和状态等 ;
* 获取下次执行的 duration.
* return

```
func (jm *ControllerV2) syncCronJob(
    ctx context.Context,
    cronJob *batchv1.CronJob,
    jobs []*batchv1.Job) (*batchv1.CronJob, *time.Duration, bool, error) {

    cronJob = cronJob.DeepCopy()
    now := jm.now()
    updateStatus := false
    timeZoneEnabled := utilfeature.DefaultFeatureGate.Enabled(features.CronJobTimeZone)

    // 创建一个集合映射 job.uid.
    childrenJobs := make(map[types.UID]bool)
    for _, j := range jobs {
        childrenJobs[j.ObjectMeta.UID] = true

        // job 是否在 cronJob active 里
        found := inActiveList(*cronJob, j.ObjectMeta.UID)

        // 如果 job uid 跟 cronjob uid 不相同, 且任务没完成
        if !found && !IsJobFinished(j) {
            // 获取 cronjob 对象
            cjCopy, err := jm.cronJobControl.GetCronJob(ctx, cronJob.Namespace, cronJob.Name)
            if err != nil {
                return nil, nil, updateStatus, err
            }

            // 再次判断是否相等, 如果相等则使用新拿到的 cronjob 对象
            if inActiveList(*cjCopy, j.ObjectMeta.UID) {
                cronJob = cjCopy
                continue
            }

        } else if found && IsJobFinished(j) {
            // 如果相同, 且 job 已完成
            _, status := getFinishedStatus(j)

            // 从 list 中删除该 job
            deleteFromActiveList(cronJob, j.ObjectMeta.UID)

            // 往 event 里输出该状态
            jm.recorder.Eventf(cronJob, corev1.EventTypeNormal, "SawCompletedJob", "Saw completed job: %s, status: %v", j.Name, status)
            updateStatus = true

        } else if IsJobFinished(j) {
            // 如果该 job 已完成, 则更新时间.
            if cronJob.Status.LastSuccessfulTime == nil {
                cronJob.Status.LastSuccessfulTime = j.Status.CompletionTime
                updateStatus = true
            }
        }
    }

    // 遍历 cronjob active 集合, 如果对应的 job 不再存在, 则从 active list 中删除 job 引用. 避免 cronjob 可能永远处于活动模式.
    for _, j := ra...