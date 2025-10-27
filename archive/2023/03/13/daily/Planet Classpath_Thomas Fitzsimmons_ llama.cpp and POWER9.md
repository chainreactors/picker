---
title: Thomas Fitzsimmons: llama.cpp and POWER9
url: https://www.fitzsim.org/blog/?p=511
source: Planet Classpath
date: 2023-03-13
fetch_date: 2025-10-04T09:23:40.564351
---

# Thomas Fitzsimmons: llama.cpp and POWER9

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# llama.cpp and POWER9

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [March 11, 2023](https://www.fitzsim.org/blog/?p=511)
[Leave a comment on llama.cpp and POWER9](https://www.fitzsim.org/blog/?p=511#respond)

This is a follow-up to my [prior post about whisper.cpp](https://www.fitzsim.org/blog/?p=484). Georgi Gerganov has adapted his GGML framework to run the recently-circulating LLaMA weights. The PPC64 optimizations I made for whisper.cpp seem to carry over directly; after updating my Talos II’s PyTorch installation, I was able to get [llama.cpp](https://github.com/ggerganov/llama.cpp) generating text from a prompt — completely offline — using the LLaMA 7B model.

```
$ ./main -m ./models/7B/ggml-model-q4_0.bin -t 32 -n 128 -p "Hello world in Common Lisp"
main: seed = 1678578687
llama_model_load: loading model from './models/7B/ggml-model-q4_0.bin' - please wait ...
llama_model_load: n_vocab = 32000
llama_model_load: n_ctx   = 512
llama_model_load: n_embd  = 4096
llama_model_load: n_mult  = 256
llama_model_load: n_head  = 32
llama_model_load: n_layer = 32
llama_model_load: n_rot   = 128
llama_model_load: f16     = 2
llama_model_load: n_ff    = 11008
llama_model_load: n_parts = 1
llama_model_load: ggml ctx size = 4529.34 MB
llama_model_load: memory_size =   512.00 MB, n_mem = 16384
llama_model_load: loading model part 1/1 from './models/7B/ggml-model-q4_0.bin'
llama_model_load: .................................... done
llama_model_load: model size =  4017.27 MB / num tensors = 291

main: prompt: 'Hello world in Common Lisp'
main: number of tokens in prompt = 7
     1 -> ''
 10994 -> 'Hello'
  3186 -> ' world'
   297 -> ' in'
 13103 -> ' Common'
 15285 -> ' Lis'
 29886 -> 'p'

sampling parameters: temp = 0.800000, top_k = 40, top_p = 0.950000

Hello world in Common Lisp!
We are going to learn the very basics of Common Lisp, an open source lisp implementation, which is a descendant of Lisp1.
Common Lisp is the de facto standard lisp implementation of Mozilla Labs, who are using it to create modern and productive lisps for Firefox.
We are going to start by having a look at its implementation of S-Expressions, which are at the core of how Common Lisp implements its lisp features.
Then, we will explore its other features such as I/O, Common Lisp has a really nice and modern I

main: mem per token = 14828340 bytes
main:     load time =  1009.64 ms
main:   sample time =   334.95 ms
main:  predict time = 86867.07 ms / 648.26 ms per token
main:    total time = 90653.54 ms
```

The above example was just the first thing I tried; no tuning or prompt engineering — as Georgi mentioned in his README, don’t judge the model by the above output; this was just a quick test. The text is printed as soon as each token prediction is made, at a rate of about one word per second, which makes the generation interesting to watch.

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[March 11, 2023](https://www.fitzsim.org/blog/?p=511)Posted in[Uncategorized](https://www.fitzsim.org/blog/?cat=1)

## Post navigation

[Previous Post Previous post:
whisper.cpp and POWER9](https://www.fitzsim.org/blog/?p=484)

[Next Post Next post:
Printing an A4 document on US letter paper using Debian](https://www.fitzsim.org/blog/?p=518)

## Leave a comment

### [Cancel reply](/blog/?p=511#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)