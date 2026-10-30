---
title: Custom Voices With Qwen3-TTS
url: https://lucumr.pocoo.org/2026/10/29/qwen3-custom-voices/
source: Armin Ronacher's Thoughts and Writings
date: 2026-10-29
fetch_date: 2026-10-30T07:54:13.324308
---

# Custom Voices With Qwen3-TTS

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Custom Voices With Qwen3-TTS

written on October 29, 2026

With my kids I’m currently building a little [dungeron
crawler](https://github.com/mitsuhiko/dungeon-crawler) and we’re trying to
[learn a bit about game
development](https://mitsuhiko.github.io/dungeon-crawler/learn/) along the way.
However given that we live in the modern times of increasing capabilities we
wanted to get a narrator and voice over.

But we also wanted it to not sound like everyone’s standard AI voices so I
looked into what options there are on the table. After some investigation I
narrowed down to using [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) which
uses voice embeddings for custom voices.

With a bit of creativity you can also do more with those custom voices than
appears initially. In case this is of interest to you, this post just covers
what we learned and with some examples. You can probably point your agent to
it and it can do something with it.

## What Qwen Offers

Qwen3 is not the only TTS model in town, and it wans’t even my first choice. We
initially used [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M). However
Qwen3 supports voice cloning and we wanted to have it feel a bit more unique.

In practice it’s a bit tricker though. Qwen3 ships three kinds of models:

* `1.7B-Base` (and 0.6B): clones a voice from a few seconds of reference audio
* `1.7B-CustomVoice`: comes with nine built-in speakers and instructions
* `1.7B-VoiceDesign`: invents a voice from a text description

The base model clones either in context or from the speaker embedding alone but
there is no documented way to clone a voice and direct it with instructions.
That means unlike the custom voice and voice design models you cannot say “speak
sad” or “whisper” with a cloned base model.

At present the official options for a custom voice are fine-tuning Base on a
single speaker or to make a clip with VoiceDesign and clone it with Base. That
is not all that bad, but it means instructions are gone.

## Playing With It

For this blog post I took 28 seconds of me from my talk at [PyAI
Conf](https://www.youtube.com/watch?v=8RHYyRUxVrA), cut between two pauses so
that it starts and ends on a full sentence, and transcribed it with Whisper.
The transcript is really only needed for baking but to compare against an
already existing voice it’s useful to have it say the same thing as the original
recording.

Note that a conference talk recording is not ideal but it works anyways. Which
is also a good reminder that you really don’t need a particularly clean
recording (or a very long one) to get a halfway convincing version of a person.
Particularly when then presented to you on a low quality phone call, it won’t be
very hard to trick your grandmother.

The first thing you can do is to blend that recording with another voice. For
instance you can use VoiceDesign to make up a voice from a description. For this blog
post the designed voice was created like this, with Qwen’s own Python package
[`qwen-tts`](https://pypi.org/project/qwen-tts/) (`pip install qwen-tts`, I used
0.1.1), which the rest of the code in this post uses too:

```
import torch
from qwen_tts import Qwen3TTSModel

kw = dict(device_map="mps", dtype=torch.bfloat16, attn_implementation="sdpa")
design = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign", **kw)
wavs, sr = design.generate_voice_design(
    text=open("voices/transcript.txt").read(), language="English",
    instruct="A man in his forties with a warm, natural, medium-low voice, speaking "
             "clearly and calmly at an easy conversational pace, like someone reading "
             "aloud to a friend.",
)
```

You can see how the two different voices behave, particularly when blended together:

Loading the voice samples…

The interactive voice samples require JavaScript.

## Voice Embeddings

What Base takes from a recording when cloning from the embedding alone is a
speaker embedding which is basically 2048 numbers out of a speaker encoder that
was trained. The same voice gets similar numbers and different voices get
different ones. Which btw, is also a convenient way to do speaker detection
from recordings if you want to! It’s not perfect, but it’s quite helpful for a
single audio track recording to tell two speakers apart if you do some basic
slicing and dicing (more on that below).

Because it is just a vector, you can do arithmetic on it. For instance a
weighted average of two embeddings is a spaker that is somewhere between two
voices:

```
base = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-Base", **kw)

def fingerprint(path):
    prompt = base.create_voice_clone_prompt(ref_audio=path, x_vector_only_mode=True)
    return prompt[0].ref_spk_embedding

def blend(a, b, t):
    a, b = a.float(), b.float()
    mixed = (1 - t) * a + t * b
    return (mixed / mixed.norm() * ((1 - t) * a.norm() + t * b.norm())).to(torch.bfloat16)

armin, designed = fingerprint("voices/armin.flac"), fingerprint("voices/designed.flac")
```

Here is the same sentence in eleven blends:

Loading the voice samples…

Note that it stops sounding like me quite quickly, but it retains some of my
features. And it for sure ends up with creating a unique voice regardless.
I found some better successes when ensuing that the two voices have similar
spectograms (eg: similar “recording setups”). In this recording you can hear
that one voice picked up by the lapel mic was a bit hollow compared to the
designed voice.

If you like a a voice that comes out, you can bake it back into a new recording
that you can then use as reference:

```
import soundfile as sf

mixed = blend(armin, designed, 0.5)
audio, rate = say(open("voices/transcript.txt").read(), mixed)  # say() is shown further down
sf.write("voices/final.flac", audio, rate)
final = fingerprint("voices/final.flac")
```

The baked voice does not come back exactly as the blend but it makes handling it
easier if you want to. It’s just one voice reference file.

So on the question of using those embeddings for speaker recognition: how good
does that work? I took an episode of [State of Agentic
Coding](https://www.youtube.com/watch?v=qCpY4K9jtOg), the podcast Ben and I
record, cut it into 2-second windows one second apart and compared each with an
embedding of me form the conference.

Somewhat surprising, but maybe not too surprising using my conference recording
clip as the reference this does not work at all with Qwen3. If instead I take
the 20 seconds where I introduce myself at the start of the episode as the
reference, it gets 98% of the rest right.

On the other hand using a model that was trained for speaker verification
instead does manage to pick me up from the conference recording clip. For
instance [ECAPA](https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb),
finds me from the conference clip in 97% of the windows.

Here are 20 minutes of that podcast, classified by speaker with the different
approaches:

Loading the voice samples…

## Instructed Cloned Voices

But the embeddings a very useful for the voice cloning! But how to give them
instructions? Base and CustomVoice manipulate the speaker the same way: one
vector inserted into the talker’s input sequence. In CustomVoice that vector is
a row of the embedding table. In Base it is the x-vector from the speaker
encoder, which only Base has. The generation code takes either
(`voice_clone_prompt` is a regular argument of `generate`), and the transformer
weights of the two models are nearly identical. So take the embedding with
Base, then hand it to CustomVoice instead of one of its speakers:

```
cv = Qwen3TTSModel.from_pretrained("Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice", **kw)

def say(text, xvec, instruct=None, language="English"):
    ids = cv._tokenize_texts([cv._build_assistant_text(text)])
    tol...