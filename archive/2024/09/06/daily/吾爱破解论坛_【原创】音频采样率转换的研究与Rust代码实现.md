---
title: 【原创】音频采样率转换的研究与Rust代码实现
url: https://mp.weixin.qq.com/s?__biz=MjM5Mjc3MDM2Mw==&mid=2651141350&idx=1&sn=1a63fc243a6b682b5b891eb6d46ac034&chksm=bd50a4b28a272da42279038ea345f744531bd339e50c108ca16efe968047f815ce6420ae3ff6&scene=58&subscene=0#rd
source: 吾爱破解论坛
date: 2024-09-06
fetch_date: 2025-10-06T18:27:07.773531
---

# 【原创】音频采样率转换的研究与Rust代码实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LFPriaSjBUZJOuFUlhgZKickQicqJduECFiba9dNT9iaxM9iaMxHve048cqbqd0FaCRia3HBhxw7o5ib44gQLXJXGvOBHQ/0?wx_fmt=jpeg)

# 【原创】音频采样率转换的研究与Rust代码实现

原创

吾爱pojie

吾爱破解论坛

**作者****论****坛账号：DEATHTOUCH**

# 采样率转换

## 前言

两年前，我简单研究了 Direct Sound 和 WASAPI 的使用方法，发现了 WASAPI 的 `IAudioClient` 接口的 `GetMixFormat` 可以获取系统内部混音器结构。但是在调用 `Initialize` 时如果设置的 wav 格式不符合系统内部混音器结构会导致调用失败。然而，在其 flags 参数添加 `AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM` 就可以解决这个问题。后来发现还有一个 `AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY` 说是可以获得更好的采样率转换质量。

因此我开始好奇采样率转换是如何进行的，并在当时进行了一些研究，阅读了一些代码，又照猫画虎对着文献写了些代码，能够跑起来但设计上存在问题，且质量非常一般。由于了解到存在知识盲区，因此就暂时搁置，直到最近我又重新研究了这个话题。

## 简介

采样率转换（Sample Rate Conversion）通常也称作重采样（Resample），是对已有的数字信号采样进行处理的一种手段，在音频、图像处理等领域比较常见。本文将要讨论的内容，主要是在音频处理领域的常见采样率转换方法。

相信对于很多人来说，采样率转换似乎并不常见，但实际上你的手机、电脑每天都在运行相关的代码。在音频领域，只要手机或电脑在播放声音，那么系统极有可能会进行采样率转换的操作；在图像领域，对图片或视频的缩放就会对像素进行处理。

从音频角度来说，声卡驱动通常会提供多种不同的输出设置，如 44100Hz 16bit、48000Hz 24bit 等。但是系统通常只允许用户选择一种选项，可能是声卡不支持多采样率，也可能是系统不支持。因此当播放的音频文件采样率与系统设置的采样率不同时就涉及到采样率转换了。

在音乐行业，常见的 CD 音频标准是 44100Hz 16bit；而在影视行业，通常采用 48000Hz 的压缩格式（如 AAC）。比如使用音乐软件听歌，大部分情况下都是 44100Hz 的音频；而视频网站的视频内置的音频几乎都是 48000Hz 的。这种情况下，用户可以手动切换声卡设置，或者使用更专业的播放器，采用独占音频（一般是 WASAPI 或者是 ASIO）的方式使得声卡按照音频文件的采样率播放，从而达到无损的效果。而对于大部分普通板载声卡的驱动，可能只提供了一种采样率标准且甚至无法切换，因此必须使用采样率转换。

由于大部分声卡提供的输出采样率标准通常是 44100Hz 和 48000Hz，本文主要也着重于这二者之间的转换，但也会研究 96000Hz 的下采样问题（Hi-Res 通常要求至少 96k/24bit）。注意使用的算法其实是通用的，但是针对不同的采样率需要调整特定的参数才能达到最好的效果。

曾经的安卓系统就因为其内置的采样率转换而为人诟病，彼时的骁龙芯片更是让听歌体验变得极度糟糕。但是对于听歌来说，在音源已经达到 CD 标准的时候，好的播放和收听设备的影响显然是明显大于音源的。而且对于所谓的 Hi-Res，"母带级" 等音质，实际上更高的采样率对于听歌的来说毫无意义（也就是在音乐发行环节，参考此文：https://people.xiph.org/~xiphmont/demo/neil-young.html），但对于音乐的制作环节还是有价值的。

## 前置知识

首先要明确的是，本文所需的知识主要来自数字信号处理（Digital Signal Processing）领域，建议掌握一定的基础，以便于了解本文内容。推荐书籍有奥本海姆的《信号与系统》和《离散时间信号处理》，当然其他的书籍也是可以的。这些书籍的内容不必全都了解（我自己就没看太多），根据需要即可。下面列出重点内容：

1. 傅里叶变换、时域和频域的关系
2. 采样定理及相关内容
3. 滤波器，特别是 FIR 滤波器

其中 1 点应该算是广为人知的了。2 和 3 点则是对于后面部分的重点，也是本文最重要的部分。

当然还需要一定代码能力，本文不涉及 MATLAB 相关内容，而是使用 Rust 语言。当然不会很复杂的，因为我自己也是属于 Rust 初学者，所以有很多地方都不了解，写这个也是练练手。而且总体代码量不大，也可以轻松的用 C/C++ 等其他语言实现。此外，还需要一定的 Python 基础，因为分析时需要使用。

## 采样率转换的方法

如果你看过上面说的基本书籍，通常会给出采样率转换相关的内容。一般来说，对于采样率从高到低的过程，称为减采样（或者下采样，downsampling）；反之则称为增采样（或者上采样，upsampling）。而具体的实施需要低通滤波器的配合，这样的过程则称为抽取（decimation）和内插（interpolation）。

上述过程都是针对整数倍数转换的，也就是说只能从 44100Hz 到 22050Hz，或者反过来。而要实现非整数倍的转换，则可以级联内插器和抽取器。比如从 44100Hz 到 48000Hz，可以先找出最大公因数 300，从而得出需要内插系数 L=160，抽取系数 M=147。

为了克服巨大的系数，就出现了多采样率信号处理的方法。比如对于前面的 L=160，可以分解成 L1=40 和 L2=4；而 M=147 可以分解为 M1=49 和 M2=3。当然具体的分解方法有详细的论证和严格的数学证明，这里只是举个例子。这样的好处是可以减少计算量，因为对于带限信号，44100Hz 采样率下的最大有效频率是 22050Hz，在 L=160 的情况下，滤波器为了能抑制镜像频率需要较高的阶数，需要很大的计算量。而先以 L1=40 进行内插可以允许一定的镜像频率，因为在下一级 L2=4 时内插时可以使用相对较高阶数的滤波器来去除这个镜像频率。这样下来总体需要的计算量是远远小于不分解的情况。同理在抽取的时候，第一级抽取可以允许一定的混叠，因为第二级可以进行过滤。

当然以上都是书中提到的方法，在实际的使用中并不一定是最合适的。比如按照上面的描述，我们在实现 44100Hz 和 48000Hz 采样率互相转换的时候，需要复杂的多级系统，实现起来也是相当的麻烦。

比如我们有时候只是为了实现简单，快速的转换，完全可以使用基本的线性插值加 IIR 滤波器。而对于较高要求的情况，则可以使用精度更插值算法，如 sinc 函数插值。文献 https://ccrma.stanford.edu/~jos/resample/resample.html 给出了一种基于 sinc 函数的带限插值的算法，网站 https://src.infinitewave.ca/ 提供了各种常见软件的各项技术指标。

正如文献所说，插值算法有拉格朗日插值、三次样条插值、贝塞尔样条插值等，但是这些算法对于图像的优秀效果并不适用于音频。对于音频来说可听性是最重要的，因此文献提出了一种公共领域的算法，用来实现带限信号的插值。该算法主要使用 sinc 函数插值，并针对软件和硬件设备进行了优化，有较高的性能且实现简单，使用灵活。本文也针对这种算法进行了研究，并分析了具体的细节。

## 如何判断转换的好坏

对于采样率转换来说，通常有很多的指标，通常是检测噪音的引入程度。细分一下包括对无关频率的影响、混叠和镜像频率的产生等。前面提供的网站给出了详细的技术指标，本文主要测试 1kHz 固定音调的正弦音频，以及频率在 (0,FS/2)Hz(0,FS/2)Hz 的以二次函数变化的正弦音频（其中 FsFs 表示采样率）。前者通常称为 beep，后者则称为 sweep。

为了能够准确地反映转换的质量，需要使用特定的工具来显示音频文件的频谱（Spectrum）以及 Spectrogram（可译为语谱图，也通常叫做时频图或者频谱图）。反正名字挺乱的不同的人可能说的不一样，建议以英文为主。其中 Spectrum 通常是对于某一时间段（比如 1024 个样本）或者全部样本的傅里叶变换的结果，对于 beep 音频来说很合适；而 Spectrogram 则是关于时间、频率和功率的图，功率用颜色表示，通过短时傅里叶变换实现，非常适合 sweep 音频。

除此之外，对于 sinc 插值方法，还需要使用冲激函数测试其滤波器的性能。冲激函数 δ(t)δ(t) 在数学上的表述是当 t=0t=0 时，δ(t)=∞δ(t)=∞；当 t≠0t≠0 时，δ(t)=0δ(t)=0；且 ∫∞t=−∞δ(t)dt=1∫t=−∞∞δ(t)dt=1 。不过实际上，我们只需要让 x[0]=1x[0]=1 ，让其他值都为 0 就行了，在需要的时候进行一定的缩放。

### 生成测试文件

由于需要生成一个固定频率的正弦波和频率逐渐变化的正弦波，所以仅使用简单的 sin 函数显然无法满足要求。我们需要一个振荡器（Oscillator）来生成波形，这并不难实现。考虑正弦函数的特性，我们知道其相位在 (0,2π)(0,2π) 之间，幅度在 (0,1)(0,1) 之间，频率则取决于周期 TT。其生成公式为 x[n]=Asin(ωn+φ)x[n]=Asin(ωn+φ)，其中 AA 表示振幅，ω=2π/Tω=2π/T，φφ 表示初始相位，nn 是表示样本的整数。

由于数字音频的特点，实际的相位、频率和采样率相关。已知采样率 FSFS，要求频率 FAFA，显然周期 T=FA/FST=FA/FS，带入可得 ω=2πFS/FAω=2πFS/FA 。考虑到 sin 函数的周期性，我们可以在相位超过 2π2π 时减去 2π2π，一般我们使用 ττ 来表示 2π2π 。

因此代码可以这样来写：

```
 复制代码 隐藏代码
use std::f64::consts::TAU; // 等于 2 * PI

struct Osc {
    phase: f64, // 相位
    omega: f64, // 角频率
    freq: f64,  // 目标频率
    sample_rate: f64, // 采样率
}

impl Osc {
    fn init(sample_rate: f64) -> Self {
        Self {
            phase: 0.0,
            omega: 0.0,
            freq: 0.0,
            sample_rate,
        }
    }

    fn set_freq(&mut self, freq: f64) {
        self.freq = freq;
        self.omega = TAU * freq / self.sample_rate;
    }

    fn next(&mut self) -> f64 {
        let sample = self.phase.sin(); // 计算样本
        self.phase += self.omega;
        while self.phase >= TAU { // 用 while 是为了防止设定过高的频率
            self.phase -= TAU;
        }
        sample
    }
}
```

生成采样之后，还需要写入文件才行，这里我们使用了 Rust 库 hound，这个库提供了完整的 wav 文件的读写操作，支持整数和 32 位浮点数。为了减少量化带来的损失，同时方便操作，我们使用 32 位浮点数来保存文件。

下面是生成 beep 和 sweep 文件的代码：

```
 复制代码 隐藏代码
use hound::{WavSpec, WavWriter};

fn gen_beep(sample_rate: u32) {
    let filename = format!("beep_{}k.wav", sample_rate / 1000);
    let spec = WavSpec {
        channels: 1,
        sample_rate,
        bits_per_sample: 32,
        sample_format: hound::SampleFormat::Float,
    };
    let mut writer = WavWriter::create(filename, spec).unwrap();
    let mut osc = Osc::init(sample_rate as f64);
    osc.set_freq(1000.0);
    let sample_count = sample_rate * 5;
    for _ in 0..sample_count {
        let sample = osc.next() * 0.99;
        writer.write_sample(sample as f32).unwrap();
    }
    writer.finalize().unwrap();
}

fn gen_sweep(sample_rate: u32) {
    let filename = format!("sweep_{}k.wav", sample_rate / 1000);
    let spec = WavSpec {
        channels: 1,
        sample_rate,
        bits_per_sample: 32,
        sample_format: hound::SampleFormat::Float,
    };
    let mut writer = WavWriter::create(filename, spec).unwrap();
    let mut osc = Osc::init(sample_rate as f64);
    let sample_count = sample_rate * 5;
    let nyquist_freq = sample_rate as f64 / 2.0;
    for i in 0..sample_count {
        osc.set_freq(nyquist_freq * (i as f64 / sample_count as f64).powi(2));
        let sample = osc.next() * 0.99;
        writer.write_sample(sample as f32).unwrap();
    }
    writer.finalize().unwrap();
}
```

`gen_beep` 能生成指定采样率下一段长 5 秒的 1kHz 的正弦单声道音频，听起来就像嘟~的声音，为了避免将来转换时可能出现的振幅过大的问题，最后还将振幅乘了 0.99 以减少失真的可能性，这样实际最大音量约是 -0.1dBFS，因为通常我们假定 ±1 是一般系统能处理的最大值。`gen_sweep` 则是能生成指定采样率下同样规格的文件，区别是正弦的频率是不断变化的，从 0Hz 到奈奎斯特频率，振幅也同样进行了限制。

### 检测音频并绘制图像

由于生成的音频文件仅通过播放是几乎无法听出具体的转换结果是否符合预期，因此使用专业的工具进行分析是很重要的。一般来说这个时候应该请出 MATLAB 了，不过相比这个大家伙，我觉得还是 Python 更加灵活。我们使用 `numpy`、`scipy` 和 `matplotlib.pyplot` 来进行分析和绘制。

对于前面提到的 Spectrum，我们只需要对文件进行 FFT 就可以得到了；而 Spectrogram 则是需要使用 STFT 进行分析。除此之外还专门在 Spectrum 的基础上进行了一定的修改，以展示滤波器的冲激响应。具体代码如下：

```
 复制代码 隐藏代码
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import ShortTimeFFT
from scipy.signal.windows import kaiser

def _show_spectrum(fs, data, name, impulse: None | str = None):
    passband = impulse == 'passband'
    N = len(data)
    half_N = N // 2
    fft_data = abs(np.fft.fft(data))
    fft_data = fft_data / half_N if impulse is None else fft_data / max(fft_data)
    fft_dBFS = 20 * np.log10(fft_data)
    freqs = np.fft.fftfreq(N, 1/fs)
    plt.figure(figsize=(6, 4))
    xticks = np.arange(0, fs // 2 + 1, 2000)
    xticklabels = [f'{int(tick/1000)}' for tick in xticks]
    ymin, ymax, ystep = (-3, 1, 0.5) if passband else (-200, 10, 20)
    ax = plt.gca()
    ax.set(xlabel='Frequency in kHz', ylabel='Magnitude in dBFS',
           xlim=(0, fs//2), ylim=(ymin, ymax),
           xticks=xticks, yticks=np.arange(ymin, ymax, ystep),
           xticklabels=xticklabels, facecolor='black')
    ax.plot(freqs[:half_N], fft_dB...