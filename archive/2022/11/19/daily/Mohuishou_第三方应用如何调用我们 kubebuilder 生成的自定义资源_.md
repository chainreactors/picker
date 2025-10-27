---
title: 第三方应用如何调用我们 kubebuilder 生成的自定义资源?
url: https://lailin.xyz/post/operator-kubebuilder-clientset.html
source: Mohuishou
date: 2022-11-19
fetch_date: 2025-10-03T23:10:50.134103
---

# 第三方应用如何调用我们 kubebuilder 生成的自定义资源?

[**mohuishou**](/)

* Go 系列

  [Go 进阶训练营](/categories/Go%E8%BF%9B%E9%98%B6%E8%AE%AD%E7%BB%83%E8%90%A5/)  [Go 数据结构与算法](/post/list.html)  [Go 设计模式](/post/go-design-pattern.html)
* [kubernetes 系列](/post/operator-01-overview.html)
* [归档](/archives/)
* [关于](/about/)
* 更多

  [友链](/links/)  [rss](/atom.xml)  [标签](/tags/)

第三方应用如何调用我们 kubebuilder 生成的自定义资源?

2022年11月16日 中午

12k 字  97 分钟

[kubernetes 系列(14)](#collapse-8650aedc39c7321537da33309e414b5a)

[k8s job 为何迟迟不能结束？](/post/kubernetes-job-running-not-end.html) [Kubernetes 简明教程](/post/k8s-tutorials.html)

[operator(12)](#collapse-4b583376b2767b923c3e1da60d10de59)

[1. Operator概述: 如何对 Kubernetes 进行扩展](/post/operator-01-overview.html) [2. Kind: 如何快速搭建本地 K8s 开发环境？](/post/operator-02-use-kind-create-k8s-local-cluster.html) [3. KubeBuilder 简明教程](/post/operator-03-kubebuilder-tutorial.html) [4. kustomize 简明教程](/post/operator-04-kustomize-tutorial.html) [5. kubebuilder 实战: CRUD](/post/operator-05-kubebuilder-crud.html) [6. kubebuilder 实战: status & event](/post/operator-06-kubebuilder-status-and-event.html) [7. kubebuilder 进阶: 测试](/post/operator-07-kubebuilder-test.html) [8. kubebuilder 进阶: webhook](/post/operator-08-kubebuilder-webhook.html) [9. kubebuilder 进阶: 源码分析](/post/operator-09-kubebuilder-code.html) [10. 总结](/post/operator-11-summary.html) [第三方应用如何调用我们 kubebuilder 生成的自定义资源?](/post/operator-kubebuilder-clientset.html) [如何实现支持多集群的 Kubernetes Operator?](/post/multi-cluster-operator.html)

# 第三方应用如何调用我们 kubebuilder 生成的自定义资源?

注：本文已发布超过一年，请注意您所使用工具的相关版本是否适用

注：本文所有示例代码都可以在 [blog-code](https://github.com/mohuishou/blog-code) 仓库中找到

## kubebuilder 能否生成类似 client-go 的 sdk?

在去年写的[系列文章](https://lailin.xyz/post/operator-11-summary.html)中，我们完整的实现了 operator 开发过程中涉及到的绝大部分要素，但是在实际的生产应用中我们定义的 CR([CustomResource](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/api-extension/custom-resources/)) 就像 k8s 自带的 deployment、pod 等资源一样，会存在其他服务直接调用 api-server 接口进行创建更新的需求，而不仅仅只是通过 kubectl 编辑yaml

那么 k8s 自带的对象我们可以通过 client-go 进行调用，我们自己设计的 CR 能否直接生成类似的 SDK 呢？

这个问题在 kubebuilder 社区从 v1 - v2 版本都有用户在提，但是 kubebuilder 官方似乎不太赞同生成 sdk 的这种做法

* <https://github.com/kubernetes-sigs/kubebuilder/issues/403>
* <https://github.com/kubernetes-sigs/kubebuilder/issues/1152>

目前找到以下几种方案

| 方案 | 优点 | 缺点 |
| --- | --- | --- |
| 通过 [client-gen](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-api-machinery/generating-clientset.md) 生成对应的 sdk | 调用方使用起来会更加的方便，毕竟是静态代码，不容易出错 | 对于 operator 的开发者来说比较麻烦，因为要通过这个工具生成对应的代码还需要做很多其他的事情，甚至需要调整 kubebuiler 生成的代码结构 客制化较强，通用性较弱，每个 CR 都需要单独生成 |
| [controller-runtime/pkg/client](https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/client?utm_source=godoc#example-Client-Update) | 调用也比较方便 通用性强，只需要将 kubebuilder 生成好的 CR 定义暴露出去即可 | 相对于通过 client-gen 来说静态代码检查的能力相对较弱 |
| [client-go/dynamic](https://pkg.go.dev/k8s.io/client-go%40v0.25.4/dynamic) | 通用性极强，甚至可以不用 Operator 开发中提供对应的 CR 定义代码 | 调用方来说极其不方便，需要自定义很多东西，并且需要反复进行序列化操作 |

接下来我们就自定义一个简单的 CR，这个 CR 没有任何的逻辑，只是为了用来验证客户端调用，关于 kubebuilder 生成 CR 如果不是特别清楚，可以阅读之前的这篇文章: [kubebuilder 简明教程](https://lailin.xyz/post/operator-03-kubebuilder-tutorial.html)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` apiVersion: job.lailin.xyz/v1 kind: Test metadata:   labels:     app.kuberentes.io/managed-by: kustomize     app.kubernetes.io/created-by: operator-kubebuilder-clientset     app.kubernetes.io/instance: test-sample     app.kubernetes.io/name: test     app.kubernetes.io/part-of: operator-kubebuilder-clientset   name: test-sample   namespace: default spec:   foo: test ``` |

如上所示这个 CR 只有一个 foo 字段，也就是 kubebuilder 初始化的一个字段，除此之外什么也没有

接下来我都以 get 数据为例来分别说明这三种方式的基本使用方法，下面的示例代码可以在 [operator-kubebuilder-clientset](https://github.com/mohuishou/blog-code/tree/main/02-k8s-operator/operator-kubebuilder-clientset/client-example) 项目中找到

## 通过 client-go 调用

如下所示可以看到，代码整体来说相对比较复杂，`dynamic`​ 包生成的 client 是一个通用的 client，所以他只能获取到 k8s 的一些通用的 metadata 数据，如果想要获取到 CR 的结构化数据就只能通过 json 来进行转换

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 ``` | ``` func main() { 	cfg, err := clientcmd.BuildConfigFromFlags("", os.Getenv("HOME")+"/.kube/config") 	fatalf(err, "get kube config fail")  	// 获取 client 	gvr := schema.GroupVersionResource{ 		Group:    jobv1.GroupVersion.Group, 		Version:  jobv1.GroupVersion.Version, 		Resource: "tests", 	} 	client := dynamic.NewForConfigOrDie(cfg).Resource(gvr)  	ctx := context.Background() 	res, err := client.Namespace("default").Get(ctx, "test-sample", v1.GetOptions{}) 	fatalf(err, "get resource fail")  	b, err := res.MarshalJSON() 	fatalf(err, "get json byte fail")  	test := jobv1.Test{} 	err = json.Unmarshal(b, &test) 	fatalf(err, "get json byte fail")  	log.Printf("foo: %s", test.Spec.Foo) } ``` |

执行代码可以获取到正确的结果

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ❯ go run client-example/client-go/main.go 2022/11/15 23:16:23 foo: test ``` |

简单看一下源码，可以看到实际上 `Resource`​ 方法就是返回了 `NamespaceableResourceInterface`​ 接口，这个接口支持了 Namespace 以及非 Namespace 级别的资源的 `CURD`​ 等访问方法

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` type ResourceInterface interface { 	Create(ctx context.Context, obj *unstructured.Unstructured, options metav1.CreateOptions, subresources ...string) (*unstructured.Unstructured, error) 	Update(ctx context.Context, obj *unstructured.Unstructured, options metav1.UpdateOptions, subresources ...string) (*unstructured.Unstructured, error) 	UpdateStatus(ctx context.Context, obj *unstructured.Unstructured, options metav1.UpdateOptions) (*unstructured.Unstructured, error) 	Delete(ctx context.Context, name string, options metav1.DeleteOptions, subresources ...string) error 	DeleteCollection(ctx context.Context, options metav1.DeleteOptions, listOptions metav1.ListOptions) error 	Get(ctx context.Context, name string, options metav1.GetOptions, subresources ...string) (*unstructured.Unstructured, error) 	List(ctx context.Context, opts metav1.ListOptions) (*unstructured.UnstructuredList, error) 	Watch(ctx context.Context, opts metav1.ListOptions) (watch.Interface, error) 	Patch(ctx context.Context, name string, pt types.PatchType, data []byte, options metav1.PatchOptions, subresources ...string) (*unstructured.Unstructured, error) 	Apply(ctx context.Context, name string, obj *unstructured.Unstructured, options metav1.ApplyOptions, subresources ...string) (*unstructured.Unstructured, error) 	ApplyStatus(ctx context.Context, name string, obj *unstructured.Unstructured, options metav1.ApplyOptions) (*unstructured.Unstructured, error) }  // dynamic.NewForConfigOrDie(cfg).Resource(gvr) 返回的接口 type NamespaceableResourceInterface interface { 	Namespace(string) ResourceInterface 	ResourceInterface } ``` |

上面的这些方法返回的都是 `*unstructured.Unstructured`​ 类型的数据，这个类型本质上就是把 object 通过 map 保存了下来，然后提供了 `GetNamespace`​ 等便捷的方法给用户使用

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` type Unstructured struct { 	// Object is a JSON compatible map with string, float, int, bool, []interface{}, or 	// map[string]interface{} 	// children. 	Object map[string]interface{} } ``` |

## 通过 controller-runtime 调用

如下所示，可以发现 controller-runtime 的代码明显要比上一种方式要简洁一些，不需要手动去 json 编码解码了，基础的 scheme 数据也可以直接使用生成好的数据

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 ``` | ``` func main() { 	cfg, err := config.GetConfigWithContext("kind-kind") 	fatalf(err, "get config fail")  	scheme := runtime.NewScheme() 	utilruntime.Must(clientgoscheme.AddToScheme(scheme)) 	utilruntime.Must(v2.AddToScheme(scheme))  	c, err := client.New(cfg, client.Options{Scheme: scheme}) 	fatalf(err, "new client fail")  	test := v1.Test{} 	err = c.Get(context.Background(), types.NamespacedName{ 		Namespace: "default", 		Name:      "test-sample", 	}, &test) 	fatalf(err, "get resource fail")  	log.Printf("foo: %s", test.Spec.Foo) } ``` |

执行测试一下

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ❯ go run client-example/controller-runtime/main.go 2022/11/15 23:34:45 foo: test ``` |

同样简单看下接口，controller-runtime 的 client 是多个接口组合而来...