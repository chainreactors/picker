---
title: HyperFlow H3 Flash 本地部署：RTX 4090 跑 5 秒视频要 152 秒
url: https://blog.upx8.com/HyperFlow-H3-Flash-RTX-4090-5-152
source: 黑海洋 - AI工具与技术教程｜免费资源与开发实战
date: 2026-11-12
fetch_date: 2026-11-13T09:06:17.800826
---

# HyperFlow H3 Flash 本地部署：RTX 4090 跑 5 秒视频要 152 秒

[![й»‘жө·жҙӢ](https://blog.upx8.com/logo.webp)
й»‘жө·жҙӢ
WIKI](https://blog.upx8.com/)

[йҰ–йЎө](https://blog.upx8.com/)
[иө„жәҗ](https://blog.upx8.com/Free)
[е®үе…Ё](https://blog.upx8.com/os_security)
[ејҖеҸ‘](https://blog.upx8.com/code)
[иө„и®Ҝ](https://blog.upx8.com/news)
[е…ідәҺ](/about.html)

еңЁзәҝе·Ҙе…·

[жһҒ

**жһҒз®Җж–Үжң¬**
*txt.upx8.com*](https://txt.upx8.com/)
[I

**IPжҹҘиҜў**
*ip.upx8.com*](https://ip.upx8.com/)
[е“Ҳ

**е“ҲеёҢи®Ўз®—**
*blog.upx8.com*](https://blog.upx8.com/app/bs64/#hash)
[U

**USTDдәӨжҳ“жҹҘиҜў**
*18u.in*](https://18u.in)
[дёү

**дёүи§’жҙІиҫ…еҠ©з«ҷ**
*sjz.upx8.com*](https://sjz.upx8.com/)
[ејҖ

**ејҖеҸ‘иҖ…е·Ҙе…·з®ұ**
*tools.upx8.com*](https://tools.upx8.com/)
[жҷҙ

**жҷҙз©әеӣҫеәҠ**
*tp.776161.xyz*](https://tp.776161.xyz/)

[йҰ–йЎө](https://blog.upx8.com)
/
[иө„жәҗ](https://blog.upx8.com/Free)
/
HyperFlow H3 Flash жң¬ең°йғЁзҪІпјҡRTX 4090 и·‘ 5 з§’и§Ҷйў‘иҰҒ 152вҖҰ

# HyperFlow H3 Flash жң¬ең°йғЁзҪІпјҡRTX 4090 и·‘ 5 з§’и§Ҷйў‘иҰҒ 152 з§’

[иө„жәҗ](https://blog.upx8.com/Free)
11-12
В·
зәҰ 15 еҲҶй’ҹ
В·
й»‘жө·жҙӢ
В·

7,322

> **ж‘ҳиҰҒ**пјҡHyperFlow H3 Flash жҠҠзәҰ 31B зҡ„ MiniMax-H3 transformer еҺӢзј©еҲ° 13.7BпјҢ6 жӯҘйҮҮж ·гҖҒж— йңҖ CFGпјҢиҫ“еҮә 1344Г—768 и§Ҷйў‘е№¶еҗҢжӯҘз”ҹжҲҗ 32kHz з«ӢдҪ“еЈ°гҖӮжң¬ж–ҮеҹәдәҺе®ҳж–№жЁЎеһӢеҚЎгҖҒComfyUI иҠӮзӮ№ README е’Ңе®ҳж–№еҹәеҮҶж–ҮжЎЈпјҢж•ҙзҗҶйғЁзҪІжё…еҚ•гҖҒеҶ…еӯҳдёҺжҳҫеӯҳиҰҒжұӮгҖҒзңҹе®һиҖ—ж—¶е’ҢжҺҲжқғйҷҗеҲ¶гҖӮ

![HyperFlow H3 Flash е®Јдј еӣҫпјҡMiniMax H3 еҺӢеҲ° 13.7BпјҢ6 жӯҘз”ҹжҲҗгҖҒж— йңҖ CFG](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/045723b84dc38ead56597d2991c2424a.webp)

## е…Ҳз»ҷз»“и®ә

| й—®йўҳ | зӯ”жЎҲ |
| --- | --- |
| жҳҜд»Җд№Ҳ | MiniMax-H3 зҡ„еҺӢзј©е°‘жӯҘзүҲпјҢз”ұ Video Rebirth ејҖеҸ‘пјҢ**дёҚжҳҜ MiniMax е®ҳж–№дә§е“Ғ** |
| еҸӮж•°йҮҸ | `fl2va`В 13.7BгҖҒ`ref2va`В 13.9BпјҢзәҰдёәеҺҹзүҲ transformer зҡ„дёҖеҚҠдёҚеҲ° |
| еҺӢзј©ж–№жі• | з»“жһ„еүӘжһқпјҲдёўеқ—пјү+ дҪҺз§©еҲҶи§Ј + ж—ӢиҪ¬ W8A8 INT8пјҲ`convrot`пјү+ еҸҢж—¶й—ҙВ `(t, r)`В жқЎд»¶ |
| йҮҮж · | 4 / 6 / 8 жӯҘпјҢй»ҳи®Ө 6 жӯҘпјҢ`CFG = 1.0`пјҢдёҚз”ЁиҙҹйқўжҸҗзӨәиҜҚ |
| иҫ“еҮә | 24 fpsпјҢй»ҳи®Ө 1344Г—768пјҢ5.2вҖ“15 з§’пјҲ124вҖ“362 её§пјүпјҢ32kHz з«ӢдҪ“еЈ°еҗҢжӯҘйҹіиҪЁ |
| RTX 4090 иғҪи·‘еҗ— | иғҪгҖӮе®ҳж–№еҹәеҮҶпјҡ24GB жҳҫеҚЎи·‘ 5.2 з§’ж–Үз”ҹи§Ҷйў‘зәҰ 152 з§’пјҢеі°еҖјжҳҫеӯҳ 23 GiB |
| 16GB жҳҫеӯҳе‘ў | е®ҳж–№жҳҺзЎ®еҶҷгҖҢ16 GB GPUs are not measured yetгҖҚпјҢжІЎжңүйӘҢиҜҒ |

дёҖеҸҘиҜқпјҡе®ғжҠҠгҖҢиғҪдёҚиғҪеңЁж¶Ҳиҙ№зә§жҳҫеҚЎдёҠи·‘гҖҚеҸҳжҲҗдәҶгҖҢиҰҒзӯүеӨҡд№…гҖҚпјҢдҪҶиҝҳи°ҲдёҚдёҠдёҖй”®з§’еҮәзүҮгҖӮ

## и§„ж јдёҖи§Ҳ

| йЎ№зӣ® | ж•°еҖј |
| --- | --- |
| еҹәзЎҖжЁЎеһӢ | MiniMax-H3пјҲзәҰ 31B transformerпјү |
| еҺӢзј©еҗҺ | `fl2va`В 13.7B /В `ref2va`В 13.9B |
| еүӘжһқз»ҶиҠӮ | `fl2va`В дёўејғ 50 дёӘеқ—дёӯзҡ„ 3 дёӘпјҲ6/21/22пјүпјҢеҲҶи§Ј 102 дёӘзәҝжҖ§еұӮпјӣ`ref2va`В дёў 1 дёӘпјҲ9пјүпјҢеҲҶи§Ј 114 дёӘ |
| йҮҮж · | `euler`В +В `BasicGuider`пјҢ`cfg = 1.0` |
| еҲҶиҫЁзҺҮ | 32 зҡ„еҖҚж•°пјҢй»ҳи®Ө 1344Г—768пјҢж”ҜжҢҒ 768Г—1152 з«–еұҸ |
| её§ж•° | `17n + 5`пјҢ124 её§пјҲ5.2 з§’пјүеҲ° 362 её§пјҲ15 з§’пјү |
| жқғйҮҚдҪ“з§Ҝ | GGUFВ `Q3_K_M`вҖ“`Q8_0`В зәҰ 7.2вҖ“15.2 GBпјҲ`Q4_K_M`В 9.1 GBпјҢ`Q8_0`В 14.9 GBпјүпјӣINT8 convrot зәҰ 16 GB |
| еҸӮиҖғиҫ“е…ҘпјҲ`ref2va`пјү | жңҖеӨҡ 9 еј еӣҫгҖҒ3 ж®өи§Ҷйў‘гҖҒ3 ж®өйҹійў‘пјҢеҗҲи®Ў 12 дёӘеҸӮиҖғ |

## йғЁзҪІеӣӣжӯҘ

### 1. еҚҮзә§ ComfyUI

е®ҳж–№иҠӮзӮ№иҰҒжұӮВ **ComfyUI 0.43.0 еҸҠд»ҘдёҠ**пјҲеёҰеҺҹз”ҹ MiniMax-H3 ж”ҜжҢҒпјүпјҢе®ҳж–№еҹәеҮҶи·‘еңЁ 0.44.0гҖӮзӣҙжҺҘеҚҮзә§еҲ°жңҖж–°зүҲеҚіеҸҜпјҢдёҚеҝ…еҚЎжҹҗдёӘе°ҸзүҲжң¬гҖӮдёӢиҪҪпјҡhttps://comfy.org/download/

иө° INT8 и·Ҝзәҝж—¶иҝҳйңҖиҰҒВ `--enable-triton-backend`пјҢжҲ–дҪҝз”Ё CUDA 13.0+ зј–иҜ‘зҡ„ PyTorchпјҢеҗҰеҲҷдјҡйҖҖеӣһ PyTorch INT8 fallbackпјҢйҖҹеәҰж…ўзәҰ 50%гҖӮ

![ComfyUI зүҲжң¬жӣҙж–°з•ҢйқўпјҢе…ҲеҚҮзә§еҲ°еёҰ MiniMax-H3 еҺҹз”ҹж”ҜжҢҒзҡ„зүҲжң¬](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/e019258527b8e89d9e7cadb22b244569.webp)

### 2. е®үиЈ…иҠӮзӮ№

**GGUF и·ҜзәҝпјҲдёӨдёӘиҠӮзӮ№пјүпјҡ**

```
cd ComfyUI/custom_nodes
git clone https://github.com/city96/ComfyUI-GGUF
git clone https://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash
pip install -r ComfyUI-HyperFlow-Flash/requirements.txt   # еңЁ ComfyUI зҡ„ Python зҺҜеўғйҮҢжү§иЎҢ
```

**INT8 и·ҜзәҝпјҲдёҖдёӘиҠӮзӮ№пјүпјҡ**В еҸӘиЈ…В `ComfyUI-HyperFlow-Flash`пјҢдёҚйңҖиҰҒ ComfyUI-GGUFгҖӮиҠӮзӮ№еҢ…йңҖ 1.1.0 жҲ–жӣҙж–°пјҢ`HyperFlow Loader`В дјҡиҮӘеҠЁиҜҶеҲ«еёҰВ `hyperflow`В е…ғж•°жҚ®зҡ„ INT8 safetensorsгҖӮжҷ®йҖҡ loader дёҚи®ӨеҸҢж—¶й—ҙеөҢе…Ҙе’ҢеҲҶи§ЈеҗҺзҡ„зәҝжҖ§еұӮпјҢдёҚиҰҒж··з”ЁгҖӮ

![ComfyUI иҠӮзӮ№з®ЎзҗҶеҷЁдёӯзҡ„ HyperFlow Flash ж ёеҝғиҠӮзӮ№](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/2d922c1e4c60ed5461c5638d98af70e3.webp)

![city96 зҡ„ ComfyUI-GGUF жҸ’д»¶пјҢд»… GGUF жқғйҮҚи·ҜзәҝйңҖиҰҒ](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/a5058d3847dda02efb3a46359eef3baa.webp)

### 3. ж”ҫзҪ®жЁЎеһӢж–Үд»¶пјҲ3 + 1пјү

HyperFlow еҸӘеҺӢзј©дәҶдё»жү©ж•ЈзҪ‘з»ңпјҢж–Үжң¬зј–з ҒеҷЁгҖҒи§Ҷйў‘ VAEгҖҒйҹійў‘ VAE жІҝз”Ё MiniMax-H3пјҢжүҖд»ҘжҳҜ 3 дёӘе…ұз”Ёз»„д»¶ + 1 дёӘ HyperFlow дё»жқғйҮҚпјҡ

```
ComfyUI/models/
в”ңв”Җв”Җ diffusion_models/
в”Ӯ   в”ңв”Җв”Җ minimax_h3_fl2va_hyperflow_flash_14b-Q4_K_M.gguf               # fl2va GGUF
в”Ӯ   в”ңв”Җв”Җ minimax_h3_fl2va_hyperflow_flash_14b-int8_convrot.safetensors   # жҲ– INT8
в”Ӯ   в””в”Җв”Җ minimax_h3_ref2va_hyperflow_flash_14b-Q4_K_M.gguf              # ref2v з”ЁпјҢеҸҜйҖү
в”ңв”Җв”Җ text_encoders/
в”Ӯ   в””в”Җв”Җ qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors                   # зәҰ 15.7 GB
в””в”Җв”Җ vae/
    в”ңв”Җв”Җ minimax_h3_video_vae_fp16.safetensors                           # зәҰ 5.21 GB
    в””в”Җв”Җ minimax_h3_audio_vae_fp32.safetensors                           # зәҰ 605 MB
```

дёӢиҪҪжқҘжәҗпјҲе»әи®®еҸӘз”Ёе®ҳж–№пјүпјҡ

* дё»жқғйҮҚпјҡhttps://huggingface.co/VideoRebirthAI/hyperflow-h3-flash
* ж–Үжң¬зј–з ҒеҷЁдёҺдёӨдёӘ VAEпјҡhttps://huggingface.co/Comfy-Org/MiniMax-H3

![HuggingFace жЁЎеһӢд»“еә“зҡ„ж–Үд»¶еҲ—иЎЁпјҡGGUF йҮҸеҢ–жЎЈдҪҚдёҺ INT8 жқғйҮҚзӣ®еҪ•](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/85c71a2b16e96e70b2fe998ad5b21b02.webp)

### 4. йҖүе·ҘдҪңжөҒ

иЈ…еҘҪиҠӮзӮ№еҗҺпјҢеңЁ ComfyUI зҡ„В **Workflow вҶ’ Browse Templates вҶ’ ComfyUI-HyperFlow-Flash**В иғҪзӣҙжҺҘзңӢеҲ°е®ҳж–№жЁЎжқҝпјҢд№ҹеҸҜд»ҘжҠҠ JSON жӢ–иҝӣз”»еёғгҖӮ

| ж–Үд»¶ | д»»еҠЎ | жүҖйңҖ transformer |
| --- | --- | --- |
| `hyperflow_t2v.json` | ж–Үз”ҹйҹіи§Ҷйў‘ | `fl2va` |
| `hyperflow_i2v.json` | йҰ–её§еӣҫз”ҹйҹіи§Ҷйў‘ | `fl2va` |
| `hyperflow_flf2v.json` | йҰ–е°ҫеё§жҺ§еҲ¶ | `fl2va` |
| `hyperflow_ref2v.json` | еӨҡеӣҫ/и§’иүІеҸӮиҖғ | `ref2va` |

е®ҳж–№ең°еқҖпјҡhttps://github.com/Video-Rebirth/ComfyUI-HyperFlow-Flash/tree/main/example\_workflows

![е®ҳж–№е·ҘдҪңжөҒж–Үд»¶еҲ—иЎЁпјҡt2v / i2v / flf2v / ref2v еӣӣеҘ—жЁЎжқҝ](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/91c73a9222b30ba4b5c465f525bd11bc.webp)

GGUF дёҺ INT8 еҗ„жңүдёҖеҘ—пјҢж–Үд»¶еҗҚеёҰВ `_int8`В зҡ„жҳҜ INT8 зүҲгҖӮеҸҰжңүзӨҫеҢәз»ҙжҠӨзҡ„ INT8 е·ҘдҪңжөҒпјҲеҗ«зЁҖз–ҸжіЁж„ҸеҠӣзүҲжң¬пјүпјҡhttps://huggingface.co/BennyDaBall/HyperFlow-H3-Flash-INT8-ComfyUI/tree/main/workflows пјҢе…¶её§ж•°гҖҒж—¶й•ҝе’ҢеҠ йҖҹе№…еәҰд»Ҙе·ҘдҪңжөҒеҶ…иҠӮзӮ№еҸӮж•°дёәеҮҶпјҢзӣ®еҪ•йЎөжңӘжҸҗдҫӣе®ҳж–№ж•°жҚ®гҖӮ

![зӨҫеҢә INT8 е·ҘдҪңжөҒзӣ®еҪ•пјҡ5 дёӘ hyperflow_int8_*.json ж–Үд»¶](https://i0.wp.com/cdn.skyimg.net/up/2026/11/12/188440412b17659db2cc5fde7961b127.webp)

е·ҘдҪңжөҒеҜјеҮәзҡ„ MP4пјҲдҝқеӯҳеңЁВ `ComfyUI/output/hyperflow/`пјүеҶ…еөҢдәҶе·ҘдҪңжөҒе…ғж•°жҚ®пјҢжҠҠ MP4 жӢ–еӣһ ComfyUI е°ұиғҪиҝҳеҺҹж•ҙеј еӣҫгҖӮ

## е…ій”®еҸӮж•°

* `prompt`пјҡжҠҠз”»йқўгҖҒиҝҗеҠЁгҖҒй•ңеӨҙиҝҗеҠЁгҖҒеЈ°йҹіеҶҷиҝӣеҗҢдёҖжқЎжҸҗзӨәиҜҚпјҢдёҚиҰҒиҙҹйқўжҸҗзӨәиҜҚгҖӮ
* `width`В /В `height`пјҡ32 зҡ„еҖҚж•°пјҢжЁӘеұҸ 1344Г—768пјҢз«–еұҸ 768Г—1152гҖӮ
* `length`пјҡ`17n + 5`пјҢ124 её§ вүҲ 5.2 з§’пјҢ362 её§ = 15 з§’гҖӮ
* `steps`пјҡеңЁВ **HyperFlow Sigmas**В иҠӮзӮ№йҮҢйҖү 4 / 6 / 8пјҢй»ҳи®Ө 6гҖӮ
* йҮҮж ·еҷЁдҝқжҢҒВ `euler`пјҢ`BasicGuider`В зҡ„В `cfg = 1.0`гҖӮ
* `ref2va`пјҡGGUF дёҺ ComfyUI INT8 и·ҜзәҝеҸӘжҺҘеҸ—еӣҫзүҮеҸӮиҖғпјҢи§Ҷйў‘е’Ңйҹійў‘еҸӮиҖғйңҖиҰҒ Python еҢ…гҖӮжҸҗзӨәиҜҚйҮҢз”ЁВ `<Picture 1>`гҖҒ`<Picture 2>`В жҢҮд»ЈеҸӮиҖғеӣҫгҖӮ
* жҜҸеј еҸӮиҖғеӣҫйғҪдјҡз»ҷжҜҸдёҖжӯҘеўһеҠ  tokenгҖӮ`ref_image_size`В й»ҳи®ӨВ `match`пјҢж”№жҲҗВ `max`В еҗҺпјҢ2048 зҡ„еӣҫзүҮдјҡи®© 5.2 з§’зүҮж®өиҖ—ж—¶зҝ»еҖҚгҖӮ

## е®ҳж–№еҹәеҮҶпјҡеҲ°еә•иҰҒзӯүеӨҡд№…

...