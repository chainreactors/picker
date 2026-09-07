---
title: 营业执照（统一信用代码）的真伪识别程序设想（三）
url: https://mp.weixin.qq.com/s/uWRCd5GU3pqeLfUNTCOEgQ
source: Doonsec's feed
date: 2026-09-06
fetch_date: 2026-09-07T06:48:10.708750
---

# 营业执照（统一信用代码）的真伪识别程序设想（三）

# 营业执照（统一信用代码）的真伪识别程序设想（三）

老皮的碎碎念念

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

对营业执照进行本地库校验：

将本地营业执照主体库导出为 REG\_MARPRIPINFO.csv （字段名根据总局标准定义）

根据REG\_MARPRIPINFO.csv校验ocr\_result.csv，具体如下，将ocr\_result.csv的数据逐个依次校验：首先统一社会信用代码是否包含在UNISCID中，如是，继续校验entname对名称，dom对住所，lerep对法定代表人，是否一致，输出不一致的，（如果统一社会信用代码是15位那么在reg\_no中搜索，兼容老个体执照）

```
# -*- coding: utf-8 -*-"""交叉校验: ocr_result.csv vs REG_MARPRIPINFO.csv
逐条读取 ocr_result.csv 的统一社会信用代码, 在 REG_MARPRIPINFO.csv 中查找:  1. 优先匹配 UNISCID 字段  2. 未命中且为 15 位纯数字时, 回退匹配 REGNO 字段(老版执照注册号)命中后逐项比对: ENTNAME↔名称, DOM↔住所, LEREP↔法定代表人输出: 不一致明细 CSV + 控制台摘要"""import csvimport osimport sys

def norm(s):    """归一化: 去首尾空白、去尾部 \t、合并连续空白"""    if not s:        return ""    return " ".join(s.replace("\t", "").strip().split())

def main():    base = r"C:\Users\Administrator\AppData\Roaming\TRAE SOLO CN\ModularData\ai-agent\work-mode-projects\6a956215a09016f81bdfcb06"    reg_csv = os.path.join(base, "REG_MARPRIPINFO.csv")    ocr_csv = os.path.join(base, "ocr_result.csv")    out_dir = base
    # 1) 加载 REG_MARPRIPINFO.csv, 构建 UNISCID 索引 + REGNO 索引    uscc_map = {}   # UNISCID(大写) -> (ENTNAME, DOM, LEREP)    regno_map = {}  # REGNO       -> (ENTNAME, DOM, LEREP)
    with open(reg_csv, "r", encoding="utf-8-sig", newline="") as f:        rd = csv.reader((ln.replace("\x00", "") for ln in f))        header = next(rd)        idx = {name: i for i, name in enumerate(header)}        i_ent = idx["ENTNAME"]        i_dom = idx["DOM"]        i_lerep = idx["LEREP"]        i_regno = idx["REGNO"]        i_uniscid = idx["UNISCID"]
        for row in rd:            if len(row) <= max(i_ent, i_dom, i_lerep, i_regno, i_uniscid):                continue            rec = (                norm(row[i_ent]),                norm(row[i_dom]),                norm(row[i_lerep]),            )            uscc = norm(row[i_uniscid]).upper()            if uscc:                uscc_map[uscc] = rec            regno = norm(row[i_regno])            if regno:                regno_map[regno] = rec
    print("REG_MARPRIPINFO.csv 加载完成: UNISCID 索引 %d 条, REGNO 索引 %d 条" % (len(uscc_map), len(regno_map)))
    # 2) 逐条校验 ocr_result.csv    results = []  # (图片, 信用代码, 匹配方式, 名称_ocr, 名称_reg, 名称_一致?, 住所_ocr, 住所_reg, 住所_一致?, 法定代表人_ocr, 法定代表人_reg, 法定代表人_一致?)    matched = 0    not_found = 0    mismatch_cnt = 0
    with open(ocr_csv, "r", encoding="utf-8-sig", newline="") as f:        rd = csv.DictReader(f)        for row in rd:            img = row.get("图片文件", "")            code_raw = row.get("统一社会信用代码", "").strip()            code_up = code_raw.upper()            ocr_name = norm(row.get("名称", ""))            ocr_addr = norm(row.get("住所", ""))            ocr_lerep = norm(row.get("法定代表人", ""))
            # 查找: 先 UNISCID, 再 REGNO            rec = None            match_by = ""            if code_up in uscc_map:                rec = uscc_map[code_up]                match_by = "UNISCID"            elif code_raw in regno_map:                rec = regno_map[code_raw]                match_by = "REGNO"
            if rec is None:                not_found += 1                results.append((img, code_raw, "未找到", ocr_name, "", "", ocr_addr, "", "", ocr_lerep, "", ""))                continue
            matched += 1            reg_name, reg_dom, reg_lerep = rec
            name_ok = (ocr_name == reg_name) if ocr_name and reg_name else None            dom_ok = (ocr_addr == reg_dom) if ocr_addr and reg_dom else None            lerep_ok = (ocr_lerep == reg_lerep) if ocr_lerep and reg_lerep else None
            has_mismatch = False            for ok in (name_ok, dom_ok, lerep_ok):                if ok is False:                    has_mismatch = True                    break            if has_mismatch:                mismatch_cnt += 1
            def status_str(ok):                if ok is True:                    return "一致"                if ok is False:                    return "不一致"                return "OCR为空"
            results.append((                img, code_raw, match_by,                ocr_name, reg_name, status_str(name_ok),                ocr_addr, reg_dom, status_str(dom_ok),                ocr_lerep, reg_lerep, status_str(lerep_ok),            ))
    # 3) 输出不一致明细    report = os.path.join(out_dir, "ocr_cross_check_report.csv")    with open(report, "w", encoding="utf-8-sig", newline="") as f:        w = csv.writer(f)        w.writerow([            "图片文件", "信用代码", "匹配方式",            "名称(OCR)", "名称(库)", "名称比对",            "住所(OCR)", "住所(库)", "住所比对",            "法定代表人(OCR)", "法定代表人(库)", "法定代表人比对",        ])        # 只输出未找到 + 不一致的记录        for r in results:            if r[2] == "未找到" or "不一致" in r[5] or "不一致" in r[8] or "不一致" in r[11]:                w.writerow(r)
    # 4) 全量明细(含一致的)    full_report = os.path.join(out_dir, "ocr_cross_check_full.csv")    with open(full_report, "w", encoding="utf-8-sig", newline="") as f:        w = csv.writer(f)        w.writerow([            "图片文件", "信用代码", "匹配方式",            "名称(OCR)", "名称(库)", "名称比对",            "住所(OCR)", "住所(库)", "住所比对",            "法定代表人(OCR)", "法定代表人(库)", "法定代表人比对",        ])        w.writerows(results)
    # 5) 控制台摘要    sys.stdout.reconfigure(encoding="utf-8", errors="replace")    print()    print("=== 交叉校验报告 ===")    print("ocr_result.csv 总条数 : %d" % len(results))    print("成功匹配库中记录     : %d" % matched)    print("未找到              : %d" % not_found)    print("存在不一致          : %d" % mismatch_cnt)    print()    print("--- 逐条明细 ---")    for img, code, mby, n_ocr, n_reg, n_st, d_ocr, d_reg, d_st, l_ocr, l_reg, l_st in results:        flag = "✗" if (mby == "未找到" or "不一致" in n_st or "不一致" in d_st or "不一致" in l_st) else "✓"        print("  %s %s" % (flag, img))        if mby == "未找到":            print("      信用代码 %s 未在库中找到" % code)            continue        print("      匹配方式: %s  信用代码: %s" % (mby, code))        print("      名称    : [%s] vs [%s]  → %s" % (n_ocr, n_reg, n_st))        print("      住所    : [%s] vs [%s]  → %s" % (d_ocr, d_reg, d_st))        print("      法定代表: [%s] vs [%s]  → %s" % (l_ocr, l_reg, l_st))    print()    print("不一致明细: %s" % report)    print("全量明细  : %s" % full_report)

if __name__ == "__main__":    main()
```

写一个python服务，网页访问展示校验输出的错误数据，点击图片文件名称可以显示照片，便于人工核对未校验通过的执照

### 页面功能

* **汇总卡片**

  ：总记录数 / 有异常 / 正常
* **筛选按钮**

  ：全部 / 仅异常 / 仅正常
* **数据表格**

  ：每行展示图片文件名、信用代码、USCC 校验结果（GB 32100-2015）、名称/住所/法定代表人（含交叉比对详情）、匹配方式、备注
* **图片预览**

  ：点击图片文件名，弹出原图浮窗，按 Esc 或点击空白处关闭
* 异常记录自动排在最前面

### 判定逻辑

以下情况标记为异常：

* USCC 校验：校验码不符 / 长度异常 / 非法字符
* 交叉校验：未找到 / 字段不一致

```
# -*- coding: utf-8 -*-"""OCR 执照识别结果校验可视化服务
启动后访问 http://127.0.0.1:5000展示 ocr_result.csv + USCC 校验 + 交叉校验的合并结果点击图片文件名可弹出原图预览"""import csvimport osimport sys
from flask import Flask, abort, send_file, render_template_string
BASE = os.path.dirname(os.path.abspath(__file__))IMG_DIR = r"D:\Personal\Desktop\新建文件夹 (2)"
app = Flask(__name__)

def norm(s):    return (s or "").replace("\t", "").strip()

def load_ocr_result():    path = os.path.join(BASE, "ocr_result.csv")    data = {}    if not os.path.exists(path):        return data    with open(path, "r", encoding="utf-8-sig", newline="") as f:        for row in csv.DictReader(f):            img = norm(row.get("图片文件", ""))            if img:                data[img] = {                    "code": norm(row.get("统一社会信用代码", "")),                    "name": norm(row.get("名称", "")),                    "address": norm(row.get("住所", "")),                    "legal_rep": norm(row.get("法定代表人", "")),                    "note": norm(row.get("备注", "")),                }    return data

def load_uscc_check():    path = os.path.join(BASE, "ocr_uscc_check_report.csv")    data = {}    if not os.path.exists(path):        return data    with open(path, "r", encoding="utf-8-sig", newline="") as f:        for row in csv.DictReader(f):            img = norm(row.get("图片文件", ""))            if img:                data[img] = {                    "uscc_status": norm(row.get("校验结果", "")),                    "uscc_reason": norm(row.get("说明", "")),     ...