---
title: Using AI to find software vulnerabilities in XNU
url: https://www.inulledmyself.com/2023/05/using-ai-to-find-software.html
source: INulledMyself
date: 2023-05-10
fetch_date: 2025-10-04T11:39:18.255608
---

# Using AI to find software vulnerabilities in XNU

# [INulledMyself](https://www.inulledmyself.com/)

## Tuesday, May 9, 2023

### Using AI to find software vulnerabilities in XNU

***Note**: This work took place in May-Aug of 2022. It just took me this long to finally finish writing this (Too busy playing with my SRD 😅)*

Last year I found several vulnerabilities in XNU source code using AI. My actual stated goal was to better understand NLUs, but I ended up with a very nice double win! I had started working at an AI startup ([Moveworks.com](https://www.moveworks.com/) - it's pretty awesome! [I'm obviously not biased 😉]) and wanted to have a better understanding of how this all worked. And there is no better way to learn anything than doing the work yourself to not only understand the how, but more importantly the why.

While understanding how NLUs worked was my main goal, I also wanted to gain insight and provide data for the following questions:

* Can I understand NLPs & NLUs well enough to not look like a *complete* idiot at work?
* How good is AI at finding bugs?
* How does it compare to joern, codeql, ripgrep, and grep?
* How likely am I to find bugs in well audited open source code such as XNU

***Note***: I didn't intend to have so much code here, but I think it makes it easier to follow along at home; I don't really explain any code so feel free to ask questions 😀!

### Understanding NLPs & NLUs

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrroy-uSEeouD-6hBjuDmrgx7qFb1Xu-SgF_yKmQMP4FuccPodLWhRF6R5gf7VlSNZZ1MSVPJmKA4OKl65xC0-k5kkXtnOZ2fgLls4mH2WUzfPadIW05O5wGCI3obfthjpyMj2Ln3-hErrgtlW9sOJ3PwZ5xVvifP9f1luUEpQ6bQfsXK_r9L2Me5_/s1600/hmmm-yeah-i-know-some-of-these-words.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrroy-uSEeouD-6hBjuDmrgx7qFb1Xu-SgF_yKmQMP4FuccPodLWhRF6R5gf7VlSNZZ1MSVPJmKA4OKl65xC0-k5kkXtnOZ2fgLls4mH2WUzfPadIW05O5wGCI3obfthjpyMj2Ln3-hErrgtlW9sOJ3PwZ5xVvifP9f1luUEpQ6bQfsXK_r9L2Me5_/s300/hmmm-yeah-i-know-some-of-these-words.jpg)

In my *totally* unbiased opinion, Moveworks has a [great explanation](https://www.moveworks.com/insights/practical-guide-to-nlp-and-nlu) for how NLU and NLP work together to allow computers to understand human natural language. While there is a lot more complexity and much deeper understanding to be had than in one blog post, I do not possess such a deep understanding. So here's a big ole grain of salt before we dive in!

My aim was to make sure I could explain this to my dad: If I can make him understand how it works then I likely actually understand it myself!  In my mind, NLP is effectively an incredibly large set of rules used to distill an utterance (A string of text) into mostly useful instructions and actions that the NLU will be able to more accurately understand and then act upon.

The better you can transform and distill typos/adjectives/filler from the actual need the better your AI will be, as it can pull out the actual need you or your end user have. (Figure 3 from the aforementioned blog post has a great explanation of how this works at a high level)

Of course, in my use case there is less to structure than *actual* natural language, as the C/C++ programming language is somewhat restrictive compared to how we communicate human to human.

### Stage 1: Fight! (with OpenAI)

As with most things, I wanted to start with what had the least roadblocks. I already knew about OpenAI, so I signed up for an account and went to experiment with their API. Thankfully, the API was pretty straightforward and the following is what I used to start finding bugs:

```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Is there a vulnerability in this code? If so write the line of vulnerable code out in your response and tell me why it's vulnerable\n\nCODESNIPPETHERE",
  temperature=0.7,
  max_tokens=1500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)
```

My prompt was "Is there a vulnerability in this code? If so write the line of vulnerable code out in your response and tell me why it's vulnerable", followed by a code snippet. But what was the best code snippet to use? Originally I was going to try and parse out files so there would be additional context, but the max\_tokens parameter was limited to 4000, so this wasn't an option. Instead, I used sed to split files into functions, and fed each function as part of the prompt to see what the AI would say. Here's an example:

```
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="Is there a vulnerability in this code? If so write the line of vulnerable code out in your response and tell me why it's vulnerable\n\nint\nspec_kqfilter(vnode_t vp, struct knote *kn, struct kevent_qos_s *kev)\n{\n\tdev_t dev;\n\tassert(vnode_ischr(vp));\n\tdev = vnode_specrdev(vp);\n\n#if NETWORKING\n\t/*\n\t * Try a bpf device, as defined in bsd/net/bpf.c\n\t * If it doesn't error out the attach, then it\n\t * claimed it. Otherwise, fall through and try\n\t * other attaches.\n\t */\n\tint32_t tmp_flags = kn->kn_flags;\n\tint64_t tmp_sdata = kn->kn_sdata;\n\tint res;\n\tres = bpfkqfilter(dev, kn);\n\tif ((kn->kn_flags & EV_ERROR) == 0) {\n\t\treturn res;\n\t}\n\tkn->kn_flags = tmp_flags;\n\tkn->kn_sdata = tmp_sdata;\n#endif\n\tif (major(dev) > nchrdev) {\n\t\tknote_set_error(kn, ENXIO);\n\t\treturn 0;\n\t}\n\tkn->kn_vnode_kqok = !!(cdevsw_flags[major(dev)] & CDEVSW_SELECT_KQUEUE);\n\tkn->kn_vnode_use_ofst = !!(cdevsw_flags[major(dev)] & CDEVSW_USE_OFFSET);\n\tif (cdevsw_flags[major(dev)] & CDEVSW_IS_PTS) {\n\t\tkn->kn_filtid = EVFILTID_PTSD;\n\t\treturn ptsd_kqfilter(dev, kn);\n\t} else if (cdevsw_flags[major(dev)] & CDEVSW_IS_PTC) {\n\t\tkn->kn_filtid = EVFILTID_PTMX;\n\t\treturn ptmx_kqfilter(dev, kn);\n\t} else if (cdevsw[major(dev)].d_type == D_TTY && kn->kn_vnode_kqok) {\n\t\t/*\n\t\t * TTYs from drivers that use struct ttys use their own filter\n\t\t * routines.  The PTC driver doesn't use the tty for character\n\t\t * counts, so it must go through the select fallback.\n\t\t */\n\t\tkn->kn_filtid = EVFILTID_TTY;\n\t\treturn knote_fops(kn)->f_attach(kn, kev);\n\t}\n\t/* Try to attach to other char special devices */\n\treturn filt_specattach(kn, kev);\n}",
  temperature=0.7,
  max_tokens=1500,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)
```

During my first run through, I mostly got responses that looked like this:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCPoJoRspMA7IIBNJGLSj7z2JZWTXFhBdrJLQ4NaB-atAKCWtq2DV-mdFJmu59LBAtLBb1yXDOuWA0SHcRLIMrsGYkwHGW8iu_Ir8ngH-rCyIHXucuKVJ5ipWL7JlRdLS_9tXajB6Yjr3sWxFM2vWq4BqB4P7K23r05omwa6zuIx_LbM0c8Y1OCpWX/s16000/DavinciIsMissing.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCPoJoRspMA7IIBNJGLSj7z2JZWTXFhBdrJLQ4NaB-atAKCWtq2DV-mdFJmu59LBAtLBb1yXDOuWA0SHcRLIMrsGYkwHGW8iu_Ir8ngH-rCyIHXucuKVJ5ipWL7JlRdLS_9tXajB6Yjr3sWxFM2vWq4BqB4P7K23r05omwa6zuIx_LbM0c8Y1OCpWX/s340/DavinciIsMissing.png)

However, I got a single hit that was, well, I'll let Davinci explain it to you:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjICh5ncbd6sjOxNdGrGdqvwLsBYqnmwpkprT0QOt8djI5nf4POjkNesFXhTqh5raRjpf5QzzsEWvrq-SGxmEm1wMXIYC3CXoX44N17ljGnWCy7Vg_03TaN9aFVVbFKPS2JNAJ8tZ5O6PfyGChKVTkjCVl6HlvYfvkXcXbgcLyBcZm2pmofIKd_Oh7F/w640-h87/partiallywrongexample.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjICh5ncbd6sjOxNdGrGdqvwLsBYqnmwpkprT0QOt8djI5nf4POjkNesFXhTqh5raRjpf5QzzsEWvrq-SGxmEm1wMXIYC3CXoX44N17ljGnWCy7Vg_03TaN9aFVVbFKPS2JNAJ8tZ5O6PfyGChKVTkjCVl6HlvYfvkXcXbgcLyBcZm2pmofIKd_Oh7F/s867/partiallywrongexample.png)

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjfojjo7z1quPY1LcXdoMg-AN_blV_kO4geOMmJHsNyLftfhumWZWJRetnTN0CtjzUt943EWqrktKxtutkpDqq2H8Y2f9mCMX9BAbVujld6s948ZILfKw6G4e1NTb-YHLlZ6eY8nmc60WpVuLIEp2FAxbLmlS_J0p_wZnTSuKIY7hwDTs1WmDg_HPM2/s320/mind-blow-galaxy.gif...