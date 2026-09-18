---
title: PDF 解析为什么难：一份面向 RAG 的问题清单与解决路线 - bamb00
url: https://www.cnblogs.com/goodhacker/p/23008551
source: 博客园 - bamb00
date: 2026-09-17
fetch_date: 2026-09-18T06:51:45.434664
---

# PDF 解析为什么难：一份面向 RAG 的问题清单与解决路线 - bamb00

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [周边](https://cnblogs.vip/store)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19316348)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://www.cnblogs.com/my "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://www.cnblogs.com/my)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/goodhacker/)

# [人怜直节生来瘦，自许高材老更刚。](https://www.cnblogs.com/goodhacker)

##

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/goodhacker/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/bamb00)
* 订阅
* [管理](https://i.cnblogs.com/)

# [PDF 解析为什么难：一份面向 RAG 的问题清单与解决路线](https://www.cnblogs.com/goodhacker/p/23008551 "发布于 2026-09-17 10:57")

> **核心观点**：很多教程把 PDF 进 RAG 简化成 `PDF -> 纯文本 -> 切块 -> 向量库`。这只在单栏电子 PDF 上成立。
> 真实语料中，同一个 `.pdf` 背后可能是扫描件、乱码字体、双栏论文、跨页表格或公式教材。
> **跳过结构恢复的代价**：阅读顺序错乱、表格列错位、公式消失、无法回溯原页。

本文按「问题 → 原则 → 可运行实现」展开，带你理清 PDF 解析的完整链路。

---

## 🎯 一、先定目标：重建结构，而非抽取文本

一份 PDF 要进入 RAG，必须先具备以下能力。对应的目标形态是：
`page -> block（标题/正文/表格/图片） -> line -> span（文字/公式/资源）`

| 能力维度 | 解决的问题 |
| --- | --- |
| **文件识别与规范化** | 扩展名不可信、图片输入 |
| **文本层判断** | 文本 PDF、扫描 PDF、乱码 PDF |
| **版面识别** | 标题、正文、表格、图片、公式分别在哪里 |
| **内容识别** | OCR 文字、公式 LaTeX、表格 HTML |
| **阅读顺序恢复** | 双栏、侧栏、脚注、竖排文字 |
| **结构恢复** | span、line、block、段落、列表与标题层级 |
| **证据保留** | 页码、bbox、图片资源、解析版本 |

---

## 🔗 二、处理链：九个问题，一条固定顺序

一份 PDF 进入 RAG 前，要依次解决这九个问题。

### 1. 核心流程图

```
输入 -> 文本/OCR 判断 -> 版面识别 -> 专项识别 -> 阅读顺序 -> 段落/表格结构 -> Content List -> RAG chunk
```

### 2. 关键问题与处理阶段

| # | 问题 | 处理阶段 | 解决后得到 |
| --- | --- | --- | --- |
| 1 | 文件类型不可信、需要裁剪页码 | 第四节：统一输入 | 可控的页面输入 |
| 2 | 没有文本层，或文本层已是乱码 | 第三节：文本/OCR 判断 | 选择原生字符或 OCR |
| 3 | 标题、正文、表格、页眉混在一起 | 第五节：版面识别 | 按类型划分的内容区域 |
| 4 | 普通文字、公式、表格无法用同一种识别方法 | 第七、八、九节：专项识别 | 带置信度的文字、HTML 表格、LaTeX 公式 |
| 5 | 双栏、竖排、侧栏、脚注不能只按坐标排序 | 第十节：阅读顺序 | 可读的段落顺序 |
| 6 | 字符要恢复成行、段落、列表和标题层级 | 第十节：结构恢复 | 段落与标题路径 |
| 7 | 表格行列、表头、合并单元格、跨页关系 | 第八节：表格 | 保留列关系的 HTML |
| 8 | 图片、公式截图、表格要与原页对应 | 第九、十一节：资源与中间结构 | 可定位的资源与证据 |
| 9 | 切块必须保留标题路径、页码、bbox 和来源 | 第十二节：RAG 入库 | 可引用的知识块 |

> **💡 注意**：表格从第一步就被当作独立内容类型。它不该先变成普通文本再“猜列”，而要直接走表格专用流程。

---

## 🔍 三、判断文本 PDF、扫描 PDF 和乱码 PDF

### 现象与原因

* **现象**：提取结果为空；部分页面有文字；整篇结果充满 `(cid:123)`。
* **原因**：扫描页只有像素；隐藏文本层为空；字体 ToUnicode 映射损坏；混合体（电子页+扫描页）。

### 一种可行的判断实现

`utils/pdf_classify.py::classify` 随机抽取最多 10 页，依次检查有效字符数、乱码比例和图像覆盖率：

```
if (get_avg_cleaned_chars_per_page(pdf, pages_to_check) < 50 or detect_invalid_chars(sample_pdf_bytes)):
    return 'ocr'
if get_high_image_coverage_ratio(sample_pdf_bytes, pages_to_check) >= 0.8:
    return 'ocr'
return 'txt'
```

* **有效字符数**：去掉空白再统计，避免“排版空格多”被误判。
* **乱码检测**：统计 `(cid:数字)` 的字符占比。

  ```
  cid_pattern = re.compile(r'$cid:\d+$')
  cid_chars_ratio = cid_count / (cid_count + text_len - cid_len)
  return cid_chars_ratio > 0.05
  ```

> **参数背后的取舍**：异常时默认走 OCR，是刻意的“召回优先”。OCR 慢，但把整页当成空文档，RAG 将永远检索不到它。生产系统应当记录抽样指标，并支持**逐页分类**。

---

## ⚙️ 四、统一输入，并在推理前裁剪页码

### 1. 图片为什么先转成 PDF？

后续所有算法都依赖 PDF 的页数、页面尺寸、页对象和渲染接口。
`cli/common.py::read_fn` 按**文件字节**判断类型，图片统一转成 PDF：

```
def read_fn(path):
    path = Path(path)
    file_bytes = path.read_bytes()
    file_suffix = guess_suffix_by_bytes(file_bytes, path)
    if file_suffix in image_suffixes:
        return images_bytes_to_pdf_bytes(file_bytes)
    if file_suffix in pdf_suffixes:
        return file_bytes
    raise Exception(f"Unknown file suffix: {file_suffix}")
```

### 2. 页码为什么在推理前裁剪？

`start_page_id` 和 `end_page_id` 从 0 开始，裁剪发生在渲染和模型调用之前：

```
def _prepare_pdf_bytes(pdf_bytes_list, start_page_id, end_page_id):
    return [
        convert_pdf_bytes_to_bytes_by_pypdfium2(
            pdf_bytes, start_page_id, end_page_id
        ) for pdf_bytes in pdf_bytes_list
    ]
```

**收益**：

1. 不处理无关页面（省算力）。
2. 不覆盖源文件（可回溯）。
3. 子任务的页索引保持连续（页码不错位）。

---

## 🧩 五、先做版面识别，再做内容识别

**整页 OCR 是常见错误**：它会把正文、页眉、页脚、表格线、图片中的文字、公式和旁注全部混进一个文本流。

**正确的顺序**：
`整页图像 -> 版面区域 -> 按类型调用模型 -> 合并回页面坐标`

* **版面检测**：找区域。
* **OCR**：负责普通文字。
* **公式检测**：定位公式框，输出 LaTeX。
* **表格**：先做方向校正与有线/无线分类，再选对应的结构模型。

实现上，Pipeline 首先跑版面模型：

```
images_layout_res = self.model.layout_model.batch_predict(
    pil_images, YOLO_LAYOUT_BASE_BATCH_SIZE
)
```

`images_layout_res` 只是每页的**区域候选**，不是最终文本。

---

## 🚀 六、批处理到底在控制什么

这一段有三个名字最容易被误解：一个环境变量、一条任务记录、一个倍率。

### 1. `MINERU_MIN_BATCH_INFERENCE_SIZE`：页面任务的分批上限

* **含义**：Pipeline 外层一次交给 `batch_image_analyze()` 处理的“页面任务数上限”。
* **默认值**：384。
* **逻辑**：
  + 设为 `384`：1000 页输入 -> 分成 `384 + 384 + 232` 三批。
  + 设为 `100`：1000 页输入 -> 分成 10 批。
* **作用**：控制**页面如何分批进入 Pipeline**。调大减少调度开销但抬高内存；调小省内存但吞吐下降。

### 2. `(pdf_idx, page_idx, image, ocr_enable, lang)`：一条页面任务

这是任务的记账结构，不是 PDF 内容：

| 字段 | 含义 |
| --- | --- |
| `pdf_idx` | 该页属于输入列表中的第几个 PDF |
| `page_idx` | 该页在这个 PDF 内的页号，从 0 开始 |
| `image` | 页面渲染出的 PIL 图像 |
| `ocr_enable` | 该页是否启用 OCR |
| `lang` | OCR 语言，如 `ch`、`en` |

### 3. `batch_ratio`：显存自适应倍率

它是倍率，用来放大某些子模型的基础 batch，不是质量分数：

```
if gpu_memory >= 16: batch_ratio = 16
elif gpu_memory >= 12: batch_ratio = 8
elif gpu_memory >= 8: batch_ratio = 4
elif gpu_memory >= 6: batch_ratio = 2
else: batch_ratio = 1
```

例如公式识别的基础 batch 是 16，实际使用值可能是 `batch_ratio * 16`。

---

## 🛡️ 七、OCR 如何避免截断和误识别

### 1. 扩边：避免把字符裁掉

布局框往往贴着文字边缘，直接裁剪会截断首尾字符。稳妥的做法是裁剪时向外扩边：

```
new_image, useful_list = crop_img(
    res, np_img, crop_paste_x=50, crop_paste_y=50
)
adjusted_mfdetrec_res = get_adjusted_mfdetrec_res(
    single_page_mfdetrec_res, useful_list
)
```

* `50`：上下左右预留的安全边界像素。
* `useful_list`：记录裁剪区域在原页中的坐标。

### 2. 分组识别与低置信度处理

* **分组识别**：OCR 识别应按语言分组，中英文混排时尤其重要。
* **低置信度**：宁可标注，不要入库。

  ```
  if ocr_score > OcrConfidence.min_confidence:
      span['content'] = ocr_text
      span['score'] = float(f"{ocr_score:.3f}")
  else:
      span['content'] = ''
      span['score'] = 0.0
  ```

  **原则**：低质量区域标记为待复核，而不是当作正常文本 embedding。

---

## 📊 八、表格：为什么必须独立解析

把表格压成一句话，列关系就没了：

> **错误示例**：`产品 2023 2024 增长率 A 10 12 20%`
> **问题**：“10 是 2023 年的，还是 2024 年的？”——这句话已经无法回答。

**正确流程**：
`表格框 -> 方向旋转 -> 有线/无线分类 -> 单元格 OCR -> 网格匹配 -> HTML`

* **兜底策略**：先用无线表格模型处理全部表格，再把“被判为有线”或“无线模型自身置信度偏低”的结果交给有线表格模型兜底。
* **HTML 转义**：单元格文本写入 HTML 之前必须转义 `html.escape(ocr_res[0])`，否则 `<`、`>` 会破坏结构。
* **跨页表格**：判定原则是**宁可少合并，也不能把两个相邻表格拼错**。即使最终没有合并，RAG 侧也要把表头复制到后页数据块的 chunk 里。

---

## 🧮 九、公式、图片和方向文字

公式需要两个动作：**检测在哪里**，再**识别写了什么**。

```
images_mfd_res = self.model.mfd_model.batch_predict(
    np_images, MFD_BASE_BATCH_SIZE
)
images_formula_list = self.model.mfr_model.batch_predict(
    images_mfd_res, np_images,
    batch_size=self.batch_ratio * MFR_BASE_BATCH_SIZE,
)
```

* `MFD`：公式检测，只输出框。
* `MFR`：公式识别，输出 LaTeX。

普通 OCR 处理不了上下标、矩阵和希腊字母，所以公式必须独立走一条链路。

---

## 📖 十、恢复字符顺序、段落和标题结构

### 1. 概念定义

* **span**：文字、公式、图片、表格等最小内容单元。
* **line**：视觉上属于同一行的一组 span。
* **block**：标题、正文、表格主体等区域。
* **page**：包含页面尺寸和多个 block 的页面对象。

### 2. 排序逻辑

span 依靠“覆盖率 + 类型兼容性”放进 block：

```
if calculate_overlap_area_in_bbox1_area_ratio(span_bbox, block_bbox) > temp_radio \
   and span_block_type_compatible(span['type'], block_type):
    block_spans.append(span)
```

* **横排 vs 竖排**：

  ```
  if vertical_ratio > 0.8:
      # 竖排：按 x2 从右到左成列、再按 y 从上到下
      block_lines = merge_spans_to_vertical_line(block['spans'])
      line...