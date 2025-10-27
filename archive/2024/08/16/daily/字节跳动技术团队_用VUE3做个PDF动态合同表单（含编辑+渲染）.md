---
title: 用VUE3做个PDF动态合同表单（含编辑+渲染）
url: https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247508846&idx=2&sn=6a25b185bba641a10403e670e84ccecf&chksm=e9d3688cdea4e19aaed93f74521b555a0475a3a1bb262b34fe93a6bfdaa1386a9cbd60922dfd&scene=58&subscene=0#rd
source: 字节跳动技术团队
date: 2024-08-16
fetch_date: 2025-10-06T18:04:51.139155
---

# 用VUE3做个PDF动态合同表单（含编辑+渲染）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5EcwYhllQOh9Ce0uqBHdTNurI1eUicmfwLSAHDX1UlFWaXZAHSRhDicc8hWWhxkqFxI8XW9TSb8icFYFVgdGpfSoA/0?wx_fmt=jpeg)

# 用VUE3做个PDF动态合同表单（含编辑+渲染）

字节跳动技术团队

以下文章来源于稀土掘金技术社区
，作者啊逼不懂code

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7YyxZtr9dqXDATzlgGsENjAzWK2dBWH5OsiajWImcJACg/0)

**稀土掘金技术社区**
.

掘金，一个帮助开发者成长的技术社区

# 最终产物

嗯直接看仓库好点，我写文章不行，当个乐子看就行。pdf-signature: VUE版本的PDF合同电子签（含生成端+渲染端）。可实现预定义表单，前端填写业务数据后发送后端进行生成PDF。(gitee.com)希望能帮助到你，如果觉得可以，请留个印记。

## 渲染端

![](https://mmbiz.qpic.cn/mmbiz_gif/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZB4FoiaK5JuJNVibgwHYdITpFWY09NBKFySDpcIVAXXBI6lAVLZLKYia0Q/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

## 生成端

![](https://mmbiz.qpic.cn/mmbiz_gif/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZBH8FG7IaMEuOTE0keAlX5TJctcMVItVbd0U9Vd1KsUjPQHXr8icNuEQ/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1)

# 灵感来源

因为工作需要，在写合同生成的时候字段太多了，因为没有UI所以构思不出来。

刚开始是使用纯表单（**「先用Adobe Acrobat构建PDF预定义表单」**，后端按照预定义表单去写入），结果写完太乱了，不清晰且无法直观的对应合同模版。无意中看见泛微OA的合同电子签（逼格就上来了）:

![](https://mmbiz.qpic.cn/mmbiz_png/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZOzckyv0PhFicBA0deTwU8eqH19zT63K5lIq4FKdYaobXX6o38C6XiaIw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

于是乎我就去看了泛微是怎么实现的，发现他是一页PDF是一张图片然后做过ul 然后每个页面就是一个li做定位容器，然后 固定图片大小 请求模版后得到字段参数定位渲染到页面上。

![](https://mmbiz.qpic.cn/mmbiz_png/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZBr8uBpmvu4RUFftYhm9j3OOvjmSjJr1BJyHcM6ZCxm5LYK8n2ibAb7w/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

这种方式具体是不是有用到别的处理逻辑不清楚，但是让我一个个去找定位参数还不如让我死（几十个合同模版）。然后我就想能不能读取PDF里面的预定义**「表单字段属性（定位信息啥的）」** 将其渲染到页面上。后面用Adobe Acrobat看了一下有定位信息（**「这里有坑」**）

![](https://mmbiz.qpic.cn/mmbiz_png/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZNRlw2k8wlthia7H9t20o6Z0q9QiaSriaROfoicibW687Tp69MPaCg9FpFIQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

嗯有位置信息就好办，想办法找库读取出预定义表单信息就行。一番查找最终选用`pdfjs-dist` 可以实现读取 主要使用读取方法

```
const page = await pagePDfDoc.getPage(pageNum)
const viewport = page.getViewport({ scale: currentScale.value })
const annotations = await page.getAnnotations() //getAnnotations 可以读取到预定义表单信息数组
```

![](https://mmbiz.qpic.cn/mmbiz_png/lCQLg02gtibtsOozuz4SVbjOJhLnvWzYZD6TpDaWtfJcQ5RLfcd20xqY4C8sl50qbf9nTLwoVJsrXZRSzjmY8zw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其中 rect `[135.089, 746.562, 265.169, 767.255]` 完全对应上了上面截图的定位信息，那么按着之前的思路走，先绘制pdf，然后按照定位绘制一个矩形上去。

# 绘制渲染

这里直接看代码吧，整体不难照着文档走就行

```
<template>
  <div class="_container" ref="conteainerRef">
    <canvas ref="pdfCanvas"></canvas>
  </div>
</template>
```

```
import { getDocument, GlobalWorkerOptions } from 'pdfjs-dist'

GlobalWorkerOptions.workerSrc = 'https://cdn.jsdelivr.net/npm/pdfjsdist@4.3.136/build/pdf.worker.min.mjs'

const currentPage = ref(1) // 渲染那一页
const pdfURL = ref<string>('/pdfs/example.pdf') // 自持base64 + url

const pdfDoc = ref<any>(null)
let pagePDfDoc: any
const loadPdf = async () => {
  try {
    const loadingTask = getDocument(pdfURL.value)
    const pageObject = await loadingTask.promise
    pdfDoc.value = pageObject

    if (!pdfDoc.value) {
      throw new Error('PDF文档加载错误')
    }
    pagePDfDoc = pageObject
    pageNumbs.value = await pdfDoc.value.numPages
    emits('loadPdf', pageNumbs.value)
    console.log(`PDF 加载: ${pageNumbs.value} 页`)
  } catch (error) {
    console.error('加载PDF失败:', error)
  }
}

const renderPdf = async (pageNum = 1) => {
  try {
    const page = await pagePDfDoc.getPage(pageNum)
    const canvas = pdfCanvas.value!
    const ctx = canvas.getContext('2d')
    const dpr = window.devicePixelRatio || 1
    const bsr =
      ctx.webkitBackingStorePixelRatio ||
      ctx.mozBackingStorePixelRatio ||
      ctx.msBackingStorePixelRatio ||
      ctx.oBackingStorePixelRatio ||
      ctx.backingStorePixelRatio ||
      1
    const ratio = dpr / bsr
    ratioGlobal.value = ratio
    const viewport = page.getViewport({ scale: currentScale.value * 2 })
    canvas.width = viewport.width * ratio
    canvas.height = viewport.height * ratio
    canvas.style.width = viewport.width + 'px'
    pdf_div_width.value = viewport.width + 'px'
    conteainerRef.value!.style.width = viewport.width + 'px'
    conteainerRef.value!.style.height = viewport.height + 'px'

    canvas.style.height = viewport.height + 'px'
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0)
    const renderContext = {
      canvasContext: ctx,
      viewport: viewport
    }
    await page.render(renderContext).promise
  } catch (error) {
    console.error(`渲染报错 ${pageNum}: ${error}`)
  }
}

onMounted(() => {
  loadPdf().then(() => {
    renderPdf(currentPage.value) // 默认渲染第一页
  })
})
```

# 读取字段定位渲染（关注点）

这里有很大的坑，做的时候折磨了一下午，快下班了才发现原因。因为读出来的定位信息完全没有参考，`canvas` 的坐标是左上角`0,0`开始的。读出来的y坐标很明显不对，都到底部了700多，后面才发现**「PDF的坐标起点是从左下角开始」**😂。

```
<template>
  <div class="_container" ref="conteainerRef">
    <canvas ref="pdfCanvas"></canvas>
    <div class="filed_container" v-for="field in fields" :id="`point_${field.name}`" :key="field.name"
      :style="fieldStyle(field)" @click="focusField(field)">
      <span>{{ field.name }}</span>
    </div>
    <!-- 右侧悬浮表单 -->
    <div class="form_container" ref="formContainerRef"> </div>
  </div>
</template>
```

```
const extractFields = async (pageNum: any) => {
  if (!pagePDfDoc) {
    console.error('PDF对象不存在.')
    return
  }

  fields.splice(0, fields.length) // 清空现有字段数据

  try {
    const page = await pagePDfDoc.getPage(pageNum)
    const viewport = page.getViewport({ scale: currentScale.value })
    const annotations = await page.getAnnotations()
    console.log('annotations', annotations)
    const _scale = currentScale.value * 2

    // 转换canvas坐标
    function convertToCanvasCoordinates(
      pdfX: number,
      pdfY: number,
      pageHeight: number,
      scale: number
    ) {
      const adjustedPdfY = pageHeight - pdfY // 将 PDF 坐标系转换为 canvas 坐标系
      const canvasX = pdfX * scale
      const canvasY = adjustedPdfY * scale
      return { x: canvasX, y: canvasY }
    }

    annotations.forEach((annot: any) => {
      if (annot.subtype === 'Widget' && annot.fieldName && annot.fieldType === 'Tx') {
        const { x, y } = convertToCanvasCoordinates(
          annot.rect[0],
          annot.rect[1],
          viewport.height,
          _scale
        )
        fields.push({
          name: annot.fieldName,
          type: annot.fieldType,
          x,
          y,
          width: (annot.rect[2] - annot.rect[0]) * _scale,
          height: (annot.rect[3] - annot.rect[1]) * _scale
        })

        // 在 form_container 中追加表单
        generateForm(annot)
      }
    })
  } catch (error) {
    console.error(`字段提取失败 ${pageNum}: ${error}`)
  }
}

// @ts-ignore
const generateForm = (annot: { fieldName: string;[key: string]: any }) => {
  const form = document.createElement('div')
  form.id = `field_${annot.fieldName}`
  const label = document.createElement('label')
  const input = document.createElement('input')

  /**  Input反向联动表单滚动  */
  input.addEventListener('click', (e) => {
    e.preventDefault()
    e.stopPropagation()

    const pointItem = document.getElementById(`point_${annot.fieldName}`)
    if (pointItem) {
      activeFiled.value = annot.fieldName
      pointItem?.focus()
      pointItem.scrollIntoView({ behavior: 'auto', block: 'center', inline: 'center' })
    }
  })

  input.id = `input_${annot.fieldName}`
  input.type = 'text'
  input.style.backgroundColor = 'transparent'
  input.style.border = '1px solid #e2e2e2'
  label.innerText = annot.fieldName
  label.style.color = 'red'
  form.appendChild(label)
  form.appendChild(input)
  formContainerRef.value!.appendChild(form)
}
```

这里具体代码请查看Git仓库 pdf-signature (gitee.com) 不太好抽离，代码不多。

# 生成端思路

后面又想到前端做模版 然后做个表单Schema生成器进行关联业务组件，这样后端只需要关注写入字段即可。最终思路：

1. 先渲染pdf作为背景，然后叠加一层canvas在背景上
2. 在画板canvas上绘制出表单矩形区域，然后将所有数据传递给后端进行生成PDF预定义表单

这里后端采用`pdf-lib`库进行生成，前端传递数据需要进行坐标转换回去（**「要考虑缩放+坐标颠倒」**）

```
<template>
  <div>
    <button @click="handleSendGenerate">生成</button>
  </div>
  <div class="_container" ref="containerRef" style="position: rela...