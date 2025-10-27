---
title: 自己动手写一个k8s controller
url: https://jiajunhuang.com/articles/2025_02_16-k8s_controller.md.html
source: Jiajun的技术笔记
date: 2025-02-17
fetch_date: 2025-10-06T20:33:27.248564
---

# 自己动手写一个k8s controller

[Jiajun的技术笔记](/)

搜索

* [EN](https://blog.jiajunhuang.com)
* [归档](/archive)
* [分享](/sharing)
* [随想](/notes)
* [友链](/friends)
* 工具

  [面试题库](https://tiku.jiajunhuang.com)
  [幻灯片](https://jiajunhuang.com/page/index.md)
* [关于](/aboutme)

目录

* [自己动手写一个k8s controller](#%25E8%2587%25AA%25E5%25B7%25B1%25E5%258A%25A8%25E6%2589%258B%25E5%2586%2599%25E4%25B8%2580%25E4%25B8%25AAk8s%2bcontroller)
* [定义 CRD](#%25E5%25AE%259A%25E4%25B9%2589%2bCRD)
* [组织 controller](#%25E7%25BB%2584%25E7%25BB%2587%2bcontroller)
* [编写 controller](#%25E7%25BC%2596%25E5%2586%2599%2bcontroller)

# 自己动手写一个k8s controller

如果要处理一个云原生业务，尤其是跨云业务，k8s controller 是无可避免的，这篇博客就记录我自己折腾学习 k8s controller，从
最开始简单的照着 `sample-controller` 来，到扩展成一个支持多任务、多步骤的 controller。

## 定义 CRD

自定义的 controller 一般主要是为了处理 CRD，CRD 简单来说，就是一堆yaml，用来扩展自定义资源，比如 k8s 官方提供了 `Deployment`，
那么如果我想自己搞一个 `webapps` 对象呢？

所以有这么一个 CRD:

```
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: webapps.jiajunhuang.com
spec:
  group: jiajunhuang.com
  names:
    kind: WebApp
    singular: webapp
    plural: webapps
    shortNames:
    - webapp
  scope: Namespaced
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        required: ["spec"]
        properties:
          spec:
            type: object
            required: ["version", "replicas"]
            properties:
              version:
                type: string
                description: The version of the webapp
                minLength: 1
              replicas:
                type: integer
                minimum: 0
                description: The number of replicas of the webapp
              image:
                type: string
                description: The container image to use
                minLength: 1
          status:
            type: object
            properties:
              availableReplicas:
                type: integer
                description: The number of available replicas
              conditions:
                type: array
                items:
                  type: object
                  properties:
                    lastTransitionTime:
                      type: string
                      format: date-time
                    phase:
                      type: string
                    reason:
                      type: string
                    message:
                      type: string
    subresources:
      status: {}
    additionalPrinterColumns:
    - name: Replicas
      type: integer
      description: The number of replicas
      jsonPath: .spec.replicas
    - name: Version
      type: string
      description: The version of the webapp
      jsonPath: .spec.version
    - name: Age
      type: date
      jsonPath: .metadata.creationTimestamp
```

## 组织 controller

有了CRD以后，根据CRD还需要组织一下代码，大概目录如下：

```
$ tree .
pkg
$ tree .
.
├── crd
│   └── crd_webapps_jiajunhuang_com.yaml
├── go.mod
├── go.sum
├── hack
│   ├── boilerplate.go.txt
│   ├── tools.go
│   └── update-codegen.sh
├── pkg
│   ├── apis
│   │   ├── go.mod
│   │   ├── go.sum
│   │   └── jiajunhuang.com
│   │       └── v1
│   │           ├── doc.go
│   │           ├── register.go
│   │           ├── types.go
```

* `doc.go` 内容为：

  ```
  // +k8s:deepcopy-gen=package
  // +groupName=jiajunhuang.com

  // Package v1 is the v1 version of the API.
  package v1
  ```
* `register.go` 内容为：

  ```
  package v1

  import (
  	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
  	"k8s.io/apimachinery/pkg/runtime"
  	"k8s.io/apimachinery/pkg/runtime/schema"
  )

  var SchemeGroupVersion = schema.GroupVersion{Group: "jiajunhuang.com", Version: "v1"}

  func Kind(kind string) schema.GroupKind {
  	return SchemeGroupVersion.WithKind(kind).GroupKind()
  }

  func Resource(resource string) schema.GroupResource {
  	return SchemeGroupVersion.WithResource(resource).GroupResource()
  }

  var (
  	SchemeBuilder = runtime.NewSchemeBuilder(addKnownTypes)
  	AddToScheme   = SchemeBuilder.AddToScheme
  )

  func addKnownTypes(scheme *runtime.Scheme) error {
  	scheme.AddKnownTypes(SchemeGroupVersion,
  		&WebApp{},
  		&WebAppList{},
  	)
  	metav1.AddToGroupVersion(scheme, SchemeGroupVersion)
  	return nil
  }
  ```
* `types.go` 的内容为：

  ```
  package v1

  import (
  	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
  )

  // +genclient
  // +k8s:deepcopy-gen:interfaces=k8s.io/apimachinery/pkg/runtime.Object

  // WebApp 是一个自定义资源示例
  type WebApp struct {
  	metav1.TypeMeta   `json:",inline"`
  	metav1.ObjectMeta `json:"metadata,omitempty"`

  	Spec   WebAppSpec   `json:"spec"`
  	Status WebAppStatus `json:"status,omitempty"`
  }

  // WebAppSpec 定义了 WebApp 的期望状态
  type WebAppSpec struct {
  	// 在这里添加你的规格字段
  	Image    string `json:"image"`
  	Version  string `json:"version"`
  	Replicas int32  `json:"replicas"`
  }

  // WebAppStatus 定义了 WebApp 的实际状态
  type WebAppStatus struct {
  	// 在这里添加你的状态字段
  	AvailableReplicas int32 `json:"availableReplicas"`
  }

  // +k8s:deepcopy-gen:interfaces=k8s.io/apimachinery/pkg/runtime.Object

  // WebAppList 包含 WebApp 的列表
  type WebAppList struct {
  	metav1.TypeMeta `json:",inline"`
  	metav1.ListMeta `json:"metadata,omitempty"`

  	Items []WebApp `json:"items"`
  }
  ```

然后执行 `./hack/update-codegen.sh`

```
$ ./hack/update-codegen.sh
Generating deepcopy code for 1 targets
Generating client code for 1 targets
Generating lister code for 1 targets
Generating informer code for 1 targets
```

这里我踩了一个坑，一开始不知道为什么总是报错：

```
./hack/update-codegen.sh
Generating deepcopy code for 1 targets
F0216 11:17:21.869640 1489301 main.go:107] Error: failed making a parser: error(s) in "github.com/jiajunhuang/test/pkg/apis/jiajunhuang.com/v1":
-: module github.com/jiajunhuang/test@latest found (v0.0.0-00010101000000-000000000000, replaced by ./), but does not contain package github.com/jiajunhuang/test/pkg/apis/jiajunhuang.com/v1
```

后来把 `pkg/apis` 独立拆分成一个新的模块，才不报错了，花了很久排查，但是最终原因我也没搞懂。

## 编写 controller

此处大概就是参考 `sample-controller` 来写，代码详见：<https://github.com/jiajunhuang/test-k8s-controller/commit/1924a052d69cb974917e2294c3b05f3191895e1f#diff-243ebed2765f75e6a54f57167212fefb08c3b2a85967ad2acbc0eb78919019c1>

接下来就是一顿折腾，改造成了最终版本，支持多任务、多步骤，以下是运行时的日志：

```
I0216 15:08:31.963311 1716546 task1.go:20] "执行 PreCreate" webapp="webapp-sample" step="step1"
I0216 15:08:31.963325 1716546 task1.go:25] "执行 Create" webapp="webapp-sample" step="step1"
I0216 15:08:31.963330 1716546 task1.go:30] "执行 PostCreate" webapp="webapp-sample" step="step1"
I0216 15:08:31.964083 1716546 task2.go:20] "执行 PreCreate" webapp="webapp-sample" step="step2"
I0216 15:08:31.964092 1716546 task2.go:25] "执行 Create" webapp="webapp-sample" step="step2"
I0216 15:08:31.964097 1716546 task2.go:30] "执行 PostCreate" webapp="webapp-sample" step="step2"
I0216 15:08:31.964868 1716546 task3.go:20] "执行 PreCreate" webapp="webapp-sample" step="step3"
I0216 15:08:31.964875 1716546 task3.go:25] "执行 Create" webapp="webapp-sample" step="step3"
I0216 15:08:31.964879 1716546 task3.go:30] "执行 PostCreate" webapp="webapp-sample" step="step3"
I0216 15:08:31.965583 1716546 task1.go:20] "执行 PreCreate" webapp="webapp-sample" step="step1"
I0216 15:08:31.965590 1716546 task1.go:25] "执行 Create" webapp="webapp-sample" step="step1"
I0216 15:08:31.965594 1716546 task1.go:30] "执行 PostCreate" webapp="webapp-sample" step="step1"
I0216 15:08:31.966385 1716546 task2.go:20] "执行 PreCreate" webapp="webapp-sample" step="step2"
I0216 15:08:31.966394 1716546 task2.go:25] "执行 Create" webapp="webapp-sample" step="step2"
I0216 15:08:31.966400 1716546 task2.go:30] "执行 PostCreate" webapp="webapp-sample" step="step2"
I0216 15:08:31.967157 1716546 task3.go:20] "执行 PreCreate" webapp="webapp-sample" step="step3"
I0216 15:08:31.967165 1716546 task3.go:25] "执行 Create" webapp="webapp-sample" step="step3"
I0216 15:08:31.967169 1716546 task3.go:30] "执行 PostCreate" webapp="webapp-sample" step="step3"
I0216 15:08:34.701611 1716546 task3.go:35] "执行 PreDelete" webapp="webapp-sample...