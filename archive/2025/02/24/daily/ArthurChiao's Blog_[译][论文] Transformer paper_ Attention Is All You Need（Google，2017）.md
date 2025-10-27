---
title: [译][论文] Transformer paper: Attention Is All You Need（Google，2017）
url: https://arthurchiao.github.io/blog/attention-is-all-you-need-zh/
source: ArthurChiao's Blog
date: 2025-02-24
fetch_date: 2025-10-06T20:32:44.941891
---

# [译][论文] Transformer paper: Attention Is All You Need（Google，2017）

# [ArthurChiao's Blog](https://arthurchiao.github.io/)

* [Home](/index.html)
* [Articles (EN)](/articles)
* [Articles (дЄ≠жЦЗ)](/articles-zh)
* [Categories](/categories)
* [About](/about)
* [Donate](/donate)

# [иѓС][иЃЇжЦЗ] Transformer paper | Attention Is All You NeedпЉИGoogleпЉМ2017пЉЙ

Published at 2025-02-23 | Last Update 2025-02-23

### иѓСиАЕеЇП

жЬђжЦЗзњїиѓСиЗ™ 2017 еєі Google жПРеЗЇ Transformer зЪДиЃЇжЦЗпЉЪ
[Attention Is All You Need](https://arxiv.org/abs/1706.03762)гАВ

![](/assets/img/attention-is-all-you-need/transformer-arch.png)

Figure 1: Transformer жЮґжЮДпЉЪencoder/decoder еЖЕйГ®зїЖиКВгАВ

жСШељХдЄАжЃµжЭ•иЗ™ [Transformer жШѓе¶ВдљХеЈ•дљЬзЪДпЉЪ600 и°М Python дї£з†БеЃЮзО∞дЄ§дЄ™пЉИжЦЗжЬђеИЖз±ї+жЦЗжЬђзФЯжИРпЉЙTransformerпЉИ2019пЉЙ](/blog/transformers-from-scratch-zh/)
зЪДдїЛзїНпЉМиѓіжШО **Transformer жЮґжЮДзЫЄжѓФељУжЧґдЄїжµБзЪД RNN/CNN жЮґжЮДзЪДеИЫжЦ∞дєЛе§Д**пЉЪ

> еЬ® **transformer дєЛеЙНпЉМжЬАеЕИињЫзЪДжЮґжЮДжШѓ RNN**пЉИйАЪеЄЄжШѓ LSTM жИЦ GRUпЉЙпЉМдљЖеЃГдїђе≠ШеЬ®дЄАдЇЫйЧЃйҐШгАВ
>
> RNN [е±ХеЉАпЉИunrolledпЉЙ](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)еРОйХњињЩж†ЈпЉЪ
>
> ![](/assets/img/transformers-from-scratch/recurrent-connection.png)
>
> RNN жЬАе§ІзЪДйЧЃйҐШжШѓ**`зЇІиБФ`**пЉИrecurrent connectionпЉЙпЉЪ
> иЩљзДґеЃГдљњеЊЧдњ°жБѓиГљж≤њзЭА input sequence дЄАиЈѓдЉ†еѓЉпЉМ
> дљЖдєЯжДПеС≥зЭАеЬ®иЃ°зЃЧеЗЇ \(i-1\) еНХеЕГдєЛеЙНпЉМжЧ†ж≥ХиЃ°зЃЧеЗЇ \(i\) еНХеЕГзЪДиЊУеЗЇгАВ
>
> дЄО RNN ж≠§еѓєжѓФпЉМ**дЄАзїіеНЈзІѓ**пЉИ1D convolutionпЉЙе¶ВдЄЛпЉЪ
>
> ![](/assets/img/transformers-from-scratch/convolutional-connection.png)
>
> еЬ®ињЩдЄ™ж®°еЮЛдЄ≠пЉМжЙАжЬЙиЊУеЗЇеРСйЗПйГљеПѓдї•еєґи°МиЃ°зЃЧпЉМеЫ†ж≠§йАЯеЇ¶йЭЮеЄЄењЂгАВдљЖзЉЇзВєжШѓеЃГдїђ
> еЬ® long range dependencies еїЇж®°жЦєйЭҐйЭЮеЄЄеЉ±
> еЬ®дЄАдЄ™еНЈзІѓе±ВдЄ≠пЉМеП™жЬЙиЈЭз¶їжѓФ kernel size
> е∞ПзЪДеНХиѓНдєЛйЧіжЙНиГљељЉж≠§дЇ§дЇТгАВеѓєдЇОжЫійХњзЪДдЊЭиµЦпЉМе∞±йЬАи¶Бе†ЖеП†иЃЄе§ЪеНЈзІѓгАВ
> пЉИдЄЇдїАдєИпЉЯеПѓеПВиАГ [дї•еЫЊеГПиѓЖеИЂдЄЇдЊЛпЉМеЕ≥дЇОеНЈзІѓз•ЮзїПзљСзїЬпЉИCNNпЉЙзЪДзЫіиІВиІ£йЗКпЉИ2016пЉЙ](/blog/cnn-intuitive-explanation-zh/)пЉЙгАВ
>
> **Transformer иѓХеЫЊеЕЉй°ЊдЇМиАЕзЪДдЉШзВє**пЉЪ
>
> * еПѓдї•еГПеѓєељЉж≠§зЫЄйВїзЪДеНХиѓНдЄАж†ЈпЉМиљїжЭЊеЬ∞еѓєиЊУеЕ•еЇПеИЧзЪДжХідЄ™иМГеЫіеЖЕзЪДдЊЭиµЦеЕ≥з≥їињЫи°МеїЇж®°пЉИдЇЛеЃЮдЄКпЉМе¶ВжЮЬж≤°жЬЙдљНзљЃеРСйЗПпЉМдЇМиАЕе∞±ж≤°жЬЙеМЇеИЂпЉЙпЉЫ
> * еРМжЧґпЉМйБњеЕН recurrent connectionsпЉМеЫ†ж≠§жХідЄ™ж®°еЮЛеПѓдї•зФ®йЭЮеЄЄйЂШжХИзЪД feed forward жЦєеЉПиЃ°зЃЧгАВ
>
> Transformer зЪДеЕґдљЩиЃЊиЃ°дЄїи¶БеЯЇдЇОдЄАдЄ™иАГиЩСеЫ†зі† вАФвАФ **жЈ±еЇ¶** вАФвАФ
> е§Іе§ЪжХ∞йАЙжЛ©йГљжШѓиЃ≠зїГе§ІйЗП transformer block е±ВпЉМдЊЛе¶ВпЉМtransformer дЄ≠**еП™жЬЙдЄ§дЄ™йЭЮзЇњжАІзЪДеЬ∞жЦє**пЉЪ
>
> 1. self-attention дЄ≠зЪД softmaxпЉЫ
> 2. еЙНй¶Ие±ВдЄ≠зЪД ReLUгАВ
>
> ж®°еЮЛзЪДеЕґдљЩйГ®еИЖеЃМеЕ®зФ±зЇњжАІеПШжНҐзїДжИРпЉМ**еЃМзЊОеЬ∞дњЭзХЩдЇЖжҐѓеЇ¶**гАВ

**жПРеЗЇ attention жЬЇеИґ**зЪД paperпЉЪ
[з•ЮзїПжЬЇеЩ®зњїиѓСпЉЪиБФеРИе≠¶дє†еѓєйљРеТМзњїиѓСпЉИAlign & TranslateпЉЙпЉИ2014пЉЙ](/blog/attention-paper-zh/)гАВ

**зЫЄеЕ≥йШЕиѓї**пЉЪ

- [[иѓС][иЃЇжЦЗ] Transformer paper | Attention Is All You NeedпЉИGoogleпЉМ2017пЉЙ](/blog/attention-is-all-you-need-zh/)

- [[иѓС][иЃЇжЦЗ] Attention paper | з•ЮзїПжЬЇеЩ®зњїиѓСпЉЪиБФеРИе≠¶дє†еѓєйљРеТМзњїиѓСпЉИ2014пЉЙ](/blog/attention-paper-zh/)

- [[иѓС] жЦЗзФЯеЫЊпЉИtext-to-imageпЉЙзЃАеП≤пЉЪжЙ©жХ£ж®°еЮЛпЉИdiffusion modelsпЉЙзЪДеіЫиµЈдЄОеПСе±ХпЉИ2022пЉЙ](/blog/rise-of-diffusion-based-models-zh/)

- [[иѓС] Transformer жШѓе¶ВдљХеЈ•дљЬзЪДпЉЪ600 и°М Python дї£з†БеЃЮзО∞ self-attention еТМдЄ§з±ї TransformerпЉИ2019пЉЙ](/blog/transformers-from-scratch-zh/)

- [[иѓС] дїАдєИжШѓ GPTпЉЯTransformer еЈ•дљЬеОЯзРЖзЪДеК®зФїе±Хз§ЇпЉИ2024пЉЙ](/blog/visual-intro-to-transformers-zh/)

ж∞іеє≥еПКзїіжК§з≤ЊеКЫжЙАйЩРпЉМиѓСжЦЗдЄНеЕНе≠ШеЬ®йФЩиѓѓжИЦињЗжЧґдєЛе§ДпЉМе¶ВжЬЙзЦСйЧЃпЉМиѓЈжЯ•йШЕеОЯжЦЗгАВ
**дЉ†жТ≠зЯ•иѓЖпЉМе∞КйЗНеК≥еК®пЉМеєіжї°еНБеЕЂеС®е≤БпЉМиљђиљљиѓЈж≥®жШО[еЗЇе§Д](https://arthurchiao.art)**гАВ

дї•дЄЛжШѓиѓСжЦЗгАВ

---

* [иѓСиАЕеЇП](#иѓСиАЕеЇП)
* [жСШи¶Б](#жСШи¶Б)
* [1 еЉХи®А](#1-еЉХи®А)
  + [1.1 RNN жЮґжЮДзЪДеЖЕеЬ®й°ЇеЇПиЃ°зЃЧйЩРеИґпЉИжЭ•иЗ™ RNN еЕґдЄ≠зЪД `R`пЉЙ](#11-rnn-жЮґжЮДзЪДеЖЕеЬ®й°ЇеЇПиЃ°зЃЧйЩРеИґжЭ•иЗ™-rnn-еЕґдЄ≠зЪД-r)
  + [1.2 RNN+Attention жЮґжЮДпЉЪжЫіе•љзЪДж®°еЮЛжХИжЮЬ](#12-rnnattention-жЮґжЮДжЫіе•љзЪДж®°еЮЛжХИжЮЬ)
  + [1.3 TransformerпЉЪйБњеЕН `R`пЉМдЄАзІНеЃМеЕ®еЯЇдЇО attention жЬЇеИґзЪДжЦ∞жЮґжЮД](#13-transformerйБњеЕН-rдЄАзІНеЃМеЕ®еЯЇдЇО-attention-жЬЇеИґзЪДжЦ∞жЮґжЮД)
* [2 иГМжЩѓ](#2-иГМжЩѓ)
  + [2.1 CNNпЉЪеЗПе∞Сй°ЇеЇПиЃ°зЃЧпЉМдљЖеѓєињЬиЈЭз¶їдЊЭиµЦеЕ≥з≥їзЪДе≠¶дє†жИРжЬђеЊИйЂШ](#21-cnnеЗПе∞Сй°ЇеЇПиЃ°зЃЧдљЖеѓєињЬиЈЭз¶їдЊЭиµЦеЕ≥з≥їзЪДе≠¶дє†жИРжЬђеЊИйЂШ)
  + [2.2 Self-attention (intra-attention) жЬЇеИґ](#22-self-attention-intra-attention-жЬЇеИґ)
  + [2.3 TranformerпЉЪйБњеЕН RNN еТМ CNN](#23-tranformerйБњеЕН-rnn-еТМ-cnn)
* [3 Transformer ж®°еЮЛжЮґжЮД](#3-transformer-ж®°еЮЛжЮґжЮД)
  + [3.0 Encoder-decoderпЉЪsequence transduction ж®°еЮЛзЪДеЯЇжЬђзїУжЮД](#30-encoder-decodersequence-transduction-ж®°еЮЛзЪДеЯЇжЬђзїУжЮД)
  + [3.1 Encoder/decoder еЖЕйГ®зїУжЮД](#31-encoderdecoder-еЖЕйГ®зїУжЮД)
    - [3.1.1 EncoderпЉЪ`6 * {multi-head-attention + feed-forward}`](#311-encoder6--multi-head-attention--feed-forward)
    - [3.1.2 DecoderпЉЪ`6 * {masked-multi-head-attention + multi-head-attention + feed-forward}`](#312-decoder6--masked-multi-head-attention--multi-head-attention--feed-forward)
  + [3.2 Attention еЖЕйГ®зїУжЮД](#32-attention-еЖЕйГ®зїУжЮД)
    - [3.2.1 Scaled Dot-Product Attention](#321-scaled-dot-product-attention)
      * [**иЊУеЕ•**](#иЊУеЕ•)
      * [иЃ°зЃЧињЗз®Л](#иЃ°зЃЧињЗз®Л)
    - [3.2.2 Multi-Head Attention зЪДиЃ°зЃЧ](#322-multi-head-attention-зЪДиЃ°зЃЧ)
      * [зЇњжАІеПШжНҐ query/keyпЉМеєґи°М attention иЃ°зЃЧпЉМжЬАеРОеЖНжЛЉжО• value](#зЇњжАІеПШжНҐ-querykeyеєґи°М-attention-иЃ°зЃЧжЬАеРОеЖНжЛЉжО•-value)
      * [еЕђеЉПеТМеПВжХ∞зЯ©йШµ](#еЕђеЉПеТМеПВжХ∞зЯ©йШµ)
    - [3.2.3 Attention еЬ®ж®°еЮЛдЄ≠зЪДеЇФзФ®](#323-attention-еЬ®ж®°еЮЛдЄ≠зЪДеЇФзФ®)
      * [вАЬencoder-decoder attentionвАЭ layers](#encoder-decoder-attention-layers)
      * [encoder layers](#encoder-layers)
      * [docoder layers](#docoder-layers)
  + [3.3 Position-wise Feed-Forward Networks](#33-position-wise-feed-forward-networks)
  + [3.4 Embeddings and Softmax](#34-embeddings-and-softmax)
  + [3.5 Positional EncodingпЉИдљНзљЃзЉЦз†БпЉЙ](#35-positional-encodingдљНзљЃзЉЦз†Б)
    - [3.5.1 зЫЃзЪДпЉЪеРС token ж≥®еЕ•дљНзљЃдњ°жБѓ](#351-зЫЃзЪДеРС-token-ж≥®еЕ•дљНзљЃдњ°жБѓ)
    - [3.5.2 зЉЦз†БзЃЧж≥ХпЉЪж≠£еЉ¶еЗљжХ∞](#352-зЉЦз†БзЃЧж≥Хж≠£еЉ¶еЗљжХ∞)
* [4 Why Self-Attention](#4-why-self-attention)
  + [4.1 Motivation](#41-motivation)
  + [4.2 дЄОеЊ™зОѓзљСзїЬгАБеНЈзІѓзљСзїЬзЪДиЃ°зЃЧе§НжЭВеЇ¶еѓєжѓФ](#42-дЄОеЊ™зОѓзљСзїЬеНЈзІѓзљСзїЬзЪДиЃ°зЃЧе§НжЭВеЇ¶еѓєжѓФ)
  + [4.3 жЫіеЕЈеПѓиІ£йЗКжАІзЪДж®°еЮЛ](#43-жЫіеЕЈеПѓиІ£йЗКжАІзЪДж®°еЮЛ)
* [5 Training](#5-training)
  + [5.1 Training Data and Batching](#51-training-data-and-batching)
  + [5.2 Hardware and Schedule](#52-hardware-and-schedule)
  + [5.3 Optimizer](#53-optimizer)
  + [5.4 Regularization](#54-regularization)
    - [Residual Dropout](#residual-dropout)
    - [Label Smoothing](#label-smoothing)
* [6 зїУжЮЬ](#6-зїУжЮЬ)
  + [6.1 Machine Translation](#61-machine-translation)
  + [6.2 Model Variations](#62-model-variations)
  + [6.3 English Constituency Parsing](#63-english-constituency-parsing)
* [7 Conclusion](#7-conclusion)
* [иЗіи∞Ґ](#иЗіи∞Ґ)
* [еПВиАГжЦЗзМЃ](#еПВиАГжЦЗзМЃ)
* [йЩДељХпЉЪAttention зЪДеПѓиІЖеМЦ](#йЩДељХattention-зЪДеПѓиІЖеМЦ)
  + [Attention жЬЇеИґе≠¶дє†йХњиЈЭз¶їдЊЭиµЦзЪДдЊЛе≠Р](#attention-жЬЇеИґе≠¶дє†йХњиЈЭз¶їдЊЭиµЦзЪДдЊЛе≠Р)
  + [дї£иѓНиІ£жЮРпЉИanaphora resolutionпЉЙ](#дї£иѓНиІ£жЮРanaphora-resolution)
  + [еП•е≠РзїУжЮДдЄО attention head е≠¶дє†и°МдЄЇ](#еП•е≠РзїУжЮДдЄО-attention-head-е≠¶дє†и°МдЄЇ)

---

# жСШи¶Б

дЄїжµБзЪД sequence transduction model йГљжШѓеЯЇдЇОе§НжЭВзЪД**еЊ™зОѓжИЦеНЈзІѓз•ЮзїПзљСзїЬ**пЉМ
еЕґдЄ≠еМЕжЛђдЄАдЄ™ encoder еТМдЄАдЄ™ decoderгАВжХИжЮЬжЬАе•љзЪДж®°еЮЛињШдЉЪйАЪињЗ attention жЬЇеИґе∞Ж encoder еТМ decoder ињЮиµЈжЭ•гАВ

жИСдїђжПРеЗЇдЄАзІНжЦ∞зЪД**зЃАеНХзљСзїЬжЮґжЮД** TransformerпЉМеЃГ**еЉГзФ®дЇЖеЊ™зОѓеТМеНЈзІѓпЉМеЃМеЕ®еЯЇдЇО attention жЬЇеИґ**гАВ

еЬ®дЄ§дЄ™**жЬЇеЩ®зњїиѓС**дїїеК°...