---
title: 代码审计中的GO应用内存分配 DOS问题
url: https://blue-bird1.github.io/posts/codeql-go-dos/
source: Posts on 青鸟的博客
date: 2025-12-30
fetch_date: 2025-12-31T03:24:36.824450
---

# 代码审计中的GO应用内存分配 DOS问题

[青鸟的博客](https://blue-bird1.github.io/)

[Posts](https://blue-bird1.github.io/posts/)[About](https://blue-bird1.github.io/about/)[Friend](https://blue-bird1.github.io/friends/)

* [Posts](https://blue-bird1.github.io/posts/)
* [About](https://blue-bird1.github.io/about/)
* [Friend](https://blue-bird1.github.io/friends/)

Dec 30, 2025

# 代码审计中的GO应用内存分配 DOS问题

[go](https://blue-bird1.github.io/tags/go)[codeql](https://blue-bird1.github.io/tags/codeql)

[安全](https://blue-bird1.github.io/categories/%E5%AE%89%E5%85%A8)

976 Words

2025-12-30 00:59 +0000

---

## 前言

马上要到2026年了，我之前向codeql的github规则仓库提交的某个pr在审核人员表示投入到新的项目后，到现在依然没有回来。

想到今年还没有写博客，在关闭pr之时顺便水一篇。

### 关于codeql

2023年，作为ai爆发的几年，个人认为大概是投入到ai那边去了。

现在很流行用LLM找漏洞，实际上codeql现在也很尴尬，如果要编写追踪漏洞的复杂查询代码，学习和编写成本都很高，也容易没适配漏掉。

同样都是通过漏洞模式去找问题，LLM有很大的优势。

这种趋势下安全人员更多的是发现问题模式，而非去找具体的漏洞。

所以并不想说具体的codeql代码（当然肯定不是太久了我忘光了 细节可见https://github.com/github/codeql/pull/12663）

### 关于这种DOS漏洞

当时我编写这种查询，是受到当时查看的一些漏洞报告的影响。

它们或是通过前端展示代码或者后端处理代码的不当处理，通过特定内容能造成性能上的极端不利导致崩溃。

我编写的就是最简单的情况，外部参数直接影响到了内存分配函数。

例子代码

|  |  |
| --- | --- |
| ```  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` func serve_bad() { 	http.HandleFunc("/user", func(w http.ResponseWriter, r *http.Request) {  		c, _ := strconv.Atoi(r.Form.Get("count")) 		_ = make([]int, c)  		d, _ := strconv.Atoi(r.Form.Get("count2")) 		if(d <= 0){ 			d = 20 		} 		_ = make([]int, d)  		e, _ := strconv.Atoi(r.Form.Get("count3")) 		if(e > 0){ 			// some extra operation 		} 		_ = make([]int, e)  	}) 	http.ListenAndServe(":80", nil) } ``` |

当然现实并没有那么简单，但是这种问题是很难避免的，我当时查询top200 go库就能查到快10个。

我当时就在gog中提交了一个，作者也没有发安全公告。

只是对于大部分web应用而言，dos本身并不是很关键，大不了重启，所以除了能水十个cve外没有任何意义。

对于物联网，汽车等硬件难以重启的软件影响会更明显。

### 漏洞原理与计算性DOS

原理上很明显只是 不可控的参数流入了内存分配函数`make`，分配不出来会直接炸掉程序，大部分错误处理程序都无法防止oom杀掉程序。

很显然，不只是make，任何直接影响到内存分配的函数都存在这种问题。 例如对于某些特别大的数据库，如果没有对pagenum 单页查询数量限制，强制把所有数据查询出来不仅是数据全出来，大概会崩溃。

但实际上这很难预防，普通漏洞是不可信数据作为数据流向危险函数，这是很容易看出来防御地方的，毕竟危险函数就那么多。

但是任何数据都可能作为函数参数使用，而应用性能受参数影响。而要预防这个只能处处防御性编程，这几乎不可能。

但是除了对战这种dos意义不大，毕竟损人不利己。

[Older
从零开始自定义安卓系统(9) 初始化脚本](https://blue-bird1.github.io/posts/aosp-9/)

© 2025
·
· Made with [Hugo](https://gohugo.io/)
· Theme [Hermit-V2](https://github.com/1bl4z3r/hermit-V2)
·