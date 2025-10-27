---
title: Voice recognition
url: http://www.imperialviolet.org/2023/07/29/voice-recognition.html
source: ImperialViolet
date: 2023-07-30
fetch_date: 2025-10-04T11:53:24.372055
---

# Voice recognition

# [ImperialViolet](https://www.imperialviolet.org)

### [Voice recognition](/2023/07/29/voice-recognition.html) (29 Jul 2023)

**Update**: [Evan](https://neugierig.org/software/blog/) let me know that [Whisper](https://github.com/ggerganov/whisper.cpp) solved the voice recognition problem. He has a wrapper that records from a microphone and prints the transcription [here](https://github.com/evmar/whisper). Whisper is very impressive and the only caveat is that it sometimes inserts whole fabricated sentences at the end. The words always sort of make sense in context, but there were no sounds that could possibly have caused it. It's always at the very end in my experience, and it's no problem to remove it so, with that noted, you should ignore everything below because Whisper is a better answer.

Last week’s blog post was rather long, and had a greater than normal
number of typos. (Thanks to people who pointed them out. I think I’ve
fixed all the ones that were reported.)

This was because I saw in reviews that iOS 17’s voice recognition was
supposed to be much improved, and I figured that I’d give it a try. I’ve
always found iOS’s recognition to be superior to Google Docs and I have
an old iPad Pro that’s good for betas.

iOS’s performance remains good and, yes, I think it’s better than iOS
16. But it’s still hardly at the level of “magic”, especially when using
technical terms. Here’s a paragraph taken directly from the raw output
of last week’s post (I’ve highlighted errors with italics):

> It is integrated into the W3C credential management specification and
> so it is called via *navigator . credentials . create* and
> *navigator .credentials. get*. This document is about
> understanding the deeper structures that underpin *web orphan*
> rather than being a *guy* as to its details. So we will leave a
> great many details to the numerous guides to *Web Oran* that
> already exist on the web and instead focus on how structures from
> *UF* were carried over into *Web orphan* and updated.

While it’s nice that many of the words are there, with that density
of errors doing all the corrections means that it’s not clearly better
than typing things out. However, the world is all aflutter about LLMs
these days. Can they help?

I wrote a script to chunk paragraphs of text so that the chunks were
at least 500 bytes, and then to send them to `gpt-3.5-turbo`
with the following instructions prefixed, and a temperature of 0.6:

> The following is the output of a poor speech recognition system.
> Please correct its errors and reply with the corrected version without
> any preamble. Some of the uncommon words that the system can’t recognise
> are U2F, CTAP, FIDO, CTAP2, JSON, FIDO2, WebAuthn, bearer token, hash,
> phishing, RP ID, passkey, caBLE, and password manager.

Here’s the cleaned up version of that paragraph.

> It is integrated into the W3C credential management specification and
> so it is called via navigator.credentials.create and
> navigator.credentials.get. This document is about understanding the
> deeper structures that underpin *web authentication* rather than
> being a guide as to its details. So we will leave a great many details
> to the numerous guides to WebAuthn that already exist on the web and
> instead focus on how structures from U2F were carried over into WebAuthn
> and updated.

There’s one case where it wrote “web authentication” rather than
“WebAuthn”, but it fixed all the other problems!

So that’s what I tried: I dictated long chunks to iOS, then ran a
script to clean it up with GPT, then edited it manually in Obsidian.
From Obsidian, pandoc converted to HTML and EPUB formats.

That prompt is the result of some experimentation. Initially, I asked
GPT to fix “errors and grammar” but, when reading the results, some
sentences were incorrect and I found that it had “fixed” them into
nonsense. Therefore I dropped “and grammar”. You can ask it to output in
Markdown format, and I probably should have done that, but I was too far
into manual editing by the time that I thought of it.

An oddity was that I wrote the instructions with the word “recognise”
(English spelling) but then thought that it might work better with the
more common American spelling (“recognize”). But that seemed to make it
worse!

An obvious thing to try was to use GPT 4. However, I misread the [costs of OpenAI’s API](https://openai.com/pricing) and thought
that their charges were per-token, not per 1000 tokens. So with
estimates that were off by three orders of magnitude, GPT 4 seemed a bit
too expensive for a random experiment and I used GPT 3.5 for
everything.

I didn’t write this post the same way, but this experimental worked
well enough that I might try it again in the future for longer public
writing.