---
title: 如何实现支持多集群的 Kubernetes Operator?
url: https://lailin.xyz/post/multi-cluster-operator.html
source: Mohuishou
date: 2022-11-23
fetch_date: 2025-10-03T23:26:37.318494
---

# 如何实现支持多集群的 Kubernetes Operator?

[**mohuishou**](/)

* Go 系列

  [Go 进阶训练营](/categories/Go%E8%BF%9B%E9%98%B6%E8%AE%AD%E7%BB%83%E8%90%A5/)  [Go 数据结构与算法](/post/list.html)  [Go 设计模式](/post/go-design-pattern.html)
* [kubernetes 系列](/post/operator-01-overview.html)
* [归档](/archives/)
* [关于](/about/)
* 更多

  [友链](/links/)  [rss](/atom.xml)  [标签](/tags/)

如何实现支持多集群的 Kubernetes Operator?

2022年11月22日 中午

6.9k 字  58 分钟

[kubernetes 系列(14)](#collapse-8650aedc39c7321537da33309e414b5a)

[k8s job 为何迟迟不能结束？](/post/kubernetes-job-running-not-end.html) [Kubernetes 简明教程](/post/k8s-tutorials.html)

[operator(12)](#collapse-4b583376b2767b923c3e1da60d10de59)

[1. Operator概述: 如何对 Kubernetes 进行扩展](/post/operator-01-overview.html) [2. Kind: 如何快速搭建本地 K8s 开发环境？](/post/operator-02-use-kind-create-k8s-local-cluster.html) [3. KubeBuilder 简明教程](/post/operator-03-kubebuilder-tutorial.html) [4. kustomize 简明教程](/post/operator-04-kustomize-tutorial.html) [5. kubebuilder 实战: CRUD](/post/operator-05-kubebuilder-crud.html) [6. kubebuilder 实战: status & event](/post/operator-06-kubebuilder-status-and-event.html) [7. kubebuilder 进阶: 测试](/post/operator-07-kubebuilder-test.html) [8. kubebuilder 进阶: webhook](/post/operator-08-kubebuilder-webhook.html) [9. kubebuilder 进阶: 源码分析](/post/operator-09-kubebuilder-code.html) [10. 总结](/post/operator-11-summary.html) [第三方应用如何调用我们 kubebuilder 生成的自定义资源?](/post/operator-kubebuilder-clientset.html) [如何实现支持多集群的 Kubernetes Operator?](/post/multi-cluster-operator.html)

# 如何实现支持多集群的 Kubernetes Operator?

注：本文已发布超过一年，请注意您所使用工具的相关版本是否适用

注：本文所有示例代码都可以在 [blog-code](https://github.com/mohuishou/blog-code) 仓库中找到

在之前的文章当中我们讨论的都是在单个 kubernetes 集群内，我们该如何设计并实现一个 operator，但是随着我们应用的规模的上升或者是因为公司内部的各种其他原因（例如权限等）我们不得不采用多个 kubernetes 集群才能满足我们的需求，这时候，我们的 operator 该如何适应多集群这个场景呢？

当然目前在多集群的场景下也有了很多解决方案，例如 [ClusterNet](https://clusternet.io/)、[Karmada](https://karmada.io/zh/) 等等，但是可能由于权限或者并不想要那么重的解决方案等原因，我们有的时候还是会有 operator 直接监听多个集群的资源的需求。

* <https://github.com/admiraltyio/multicluster-controller> 这个项目使用 [controller-runtime](https://github.com/kubernetes-sigs/controller-runtime) 实现了多集群的 controller 但是已经 3 年没更新过了
* 在 controller-runtime 的库下 2019 年就有人提出了类似的需求 [Support for controllers spanning across clusters](https://github.com/kubernetes-sigs/controller-runtime/issues/745)

  2020 年有人在 controller-runtime 提出了 [POC](https://github.com/kubernetes-sigs/controller-runtime/pull/950)，将 cluster 从 manager 中提取了出来，利用 controller-runtime 监听多集群的资源变得简单了起来

## 多集群 Operator 实践

tips: 后续示例项目代码放到了 [multi-cluster-operator](https://github.com/mohuishou/blog-code/tree/main/02-k8s-operator/multi-cluster-operator) 中

### 需求

首先我们先设定一下需求和环境

* 我们现在有集群 main 和 集群 sub ，其中 main 为主集群, sub 为子集群
* 我们在 main 集群有一个 CRD，这个 CRD 的功能就是创建一个 job
* 现在多集群的环境下，我们主集群监听到 CRD 的创建之后会自动在主集群以及子集群创建一个 job

### 创建实验环境

之前的文章 [Kind: 如何快速搭建本地 K8s 开发环境](https://lailin.xyz/post/operator-02-use-kind-create-k8s-local-cluster.html) 已经比较详细的介绍了如何使用 kind 搭建集群，这里我就直接使用命令创建了

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # 创建主集群 kind create cluster --name main  # 创建子集群 kind create cluster --name sub ``` |

### 代码实现

主要逻辑见下方，其实就是在 `TestReconciler`​ 中加入了子集群的 client

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 ``` | ``` // TestReconciler reconciles a Test object type TestReconciler struct { 	// 主集群 client 	client.Client  	// 所有集群的客户端列表 	Clients map[string]client.Client  	Scheme *runtime.Scheme }  // NewTestReconciler ... func NewTestReconciler(mgr ctrl.Manager, clusters map[string]cluster.Cluster) (*TestReconciler, error) { 	r := TestReconciler{ 		Client: mgr.GetClient(), 		Scheme: mgr.GetScheme(), 		Clients: map[string]client.Client{ 			"main": mgr.GetClient(), 		}, 	} 	for name, cluster := range clusters { 		r.Clients[name] = cluster.GetClient() 	}  	err := r.SetupWithManager(mgr) 	return &r, err }  func (r *TestReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) { 	var test jobv1.Test 	var res ctrl.Result  	err := r.Get(ctx, req.NamespacedName, &test) 	if err != nil { 		return res, client.IgnoreNotFound(err) 	}  	job := test.Job()  	for _, c := range r.Clients { 		err := c.Create(ctx, job.DeepCopy()) 		if err != nil { 			return res, err 		} 	}  	return ctrl.Result{}, nil }  // SetupWithManager sets up the controller with the Manager. func (r *TestReconciler) SetupWithManager(mgr ctrl.Manager) error { 	builder := ctrl.NewControllerManagedBy(mgr). 		For(&jobv1.Test{}) 	return builder.Complete(r) } ``` |

需要注意的是我们在 `main.go`​ 初始化的时候，需要使用 `mgr.Add()`​ 把子集群加入到 manager 中，这个在后面监听资源变化的时候会用到

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` // NewSubClusters 初始化子集群 // 在 ~/.kube/config 文件中需要有这两个 context 集群 func NewSubClusters(mgr ctrl.Manager, clientContexts ...string) map[string]cluster.Cluster { 	clusters := map[string]cluster.Cluster{}  	for _, v := range clientContexts { 		conf, err := config.GetConfigWithContext(v) 		checkErr(err, "get client config fail", "context", v)  		c, err := cluster.New(conf) 		checkErr(err, "new cluster fail", "context", v)  		err = mgr.Add(c) 		checkErr(err, "add cluster in manager", "context", v)  		clusters[v] = c 	} 	return clusters } ``` |

## 如何同时监听多个集群的资源变化?

上面我们演示了如何像在多个集群创建资源，这个其实很简单，其实不需要 controller-runtime 也能实现，就像上面的这个例子，往往创建并不能解决问题，我们还需要跟进所创建资源的状态。

假设现在有这么一个需求：只要有一个 job 完成，**那么我们就认为这个 CRD 的状态应该是 finished**，该如何实现？

### 官方示例

在 [Move cluster-specific code out of the manager](https://github.com/kubernetes-sigs/controller-runtime/blob/master/designs/move-cluster-specific-code-out-of-manager.md) 的设计文档中有下面的一个简单示例，但是我觉得这个例子不是很好，因为实在是太简单粗暴了一些

* 首先在监听资源变化的时候直接监听了两个集群的 Secret 资源
* 然后在 `Reconcile`​ 方法内，由于并部只带这个资源是来自哪个集群，只能先试一下第一个集群，然后再试第二个集群

**所以我们可以在 ​**​\*\*`Reconcile`**​**​ 时候分辨是来自那个集群的事件么？\*\*

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 ``` | ``` type secretMirrorReconciler struct { 	referenceClusterClient, mirrorClusterClient client.Client }  func (r *secretMirrorReconciler) Reconcile(r reconcile.Request)(reconcile.Result, error){ 	s := &corev1.Secret{} 	if err := r.referenceClusterClient.Get(context.TODO(), r.NamespacedName, s); err != nil { 		if kerrors.IsNotFound{ return reconcile.Result{}, nil } 		return reconcile.Result, err 	}  	if err := r.mirrorClusterClient.Get(context.TODO(), r.NamespacedName, &corev1.Secret); err != nil { 		if !kerrors.IsNotFound(err) { 			return reconcile.Result{}, err 		}  		mirrorSecret := &corev1.Secret{ 			ObjectMeta: metav1.ObjectMeta{Namespace: s.Namespace, Name: s.Name}, 			Data: s.Data, 		} 		return reconcile.Result{}, r.mirrorClusterClient.Create(context.TODO(), mirrorSecret) 	}  	return nil }  func NewSecretMirrorReconciler(mgr manager.Manager, mirrorCluster cluster.Cluster) error { 	return ctrl.NewControllerManagedBy(mgr). 		// Watch Secrets in the reference cluster 		For(&corev1.Secret{}). 		// Watch Secrets in the mirror cluster 		Watches( 			source.NewKindWithCache(&corev1.Secret{}, mirrorCluster.GetCache()), 			&handler.EnqueueRequestForObject{}, 		). 		Complete(&secretMirrorReconciler{ 			referenceClusterClient: mgr.GetClient(), 			mirrorClusterClient:    mirrorCluster.GetClient(), 		}) 	} }  // ... 省略 main 函数 ``` |

### 代码实现

实现的难点在于我们如何区分事件的源集群，在 `Reconcile`​ 的参数 `ctrl.Request`​ 中只有 namespace 和 name 两个字段，所以我们想要区分集群也只有从这两个字段中想办法

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Reconcile(ctx context.Context, req ctrl.Request) (res ctrl.Result, err error) ``` |

显然 namespace 相比 name 来说更适合一些，所以我们可以给 namespace 加一个规则，namespace 字段实际的值变成 `${cluster}/${namespace}`​​，所以我们需要在事件的入口加上集群的标志，然后再在 `Reconcile`​​ 中根据集群使用对应的 client 进行操作即可

首先在监听的时候，我们可以自定义一个 handler，将集群名字注入进去

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 ``` | ``` // MuiltClustersEnqueue 多集群入队器 // 将集群名称附加在 Namespace 上 func MuiltClustersEnqueue(clusterName string) handler.EventHandler ...