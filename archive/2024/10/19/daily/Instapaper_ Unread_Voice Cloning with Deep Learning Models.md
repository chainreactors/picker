---
title: Voice Cloning with Deep Learning Models
url: https://blog.compass-security.com/2024/10/voice-cloning-with-deep-learning-models/
source: Instapaper: Unread
date: 2024-10-19
fetch_date: 2025-10-06T18:56:25.101834
---

# Voice Cloning with Deep Learning Models

## [Compass Security Blog](https://blog.compass-security.com "Compass Security Blog — Offensive Defense")

### Offensive Defense

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

* [Home](https://blog.compass-security.com/)
* [Archive](https://blog.compass-security.com/archive/)
* [Contact](https://blog.compass-security.com/contact/)
* [Newsletter](https://blog.compass-security.com/mailing-list-tigerinfo/)

# [Voice  Cloning with Deep Learning Models](https://blog.compass-security.com/2024/10/voice-cloning-with-deep-learning-models/ "Voice  Cloning with Deep Learning Models")

[October 18, 2024](https://blog.compass-security.com/2024/10/voice-cloning-with-deep-learning-models/ "Voice  Cloning with Deep Learning Models")
 /
[Nicolo Fornari](https://blog.compass-security.com/author/nfornari/ "Posts by Nicolo Fornari")
 /
[2 Comments](https://blog.compass-security.com/2024/10/voice-cloning-with-deep-learning-models/#comments)

[![](https://blog.compass-security.com/wp-content/uploads/2024/06/tortoise.jpg)](https://blog.compass-security.com/wp-content/uploads/2024/06/tortoise.jpg)

Given the explosion of development and interest in deep learning models in the past year, we decided to research on the topic to increase our know-how and find applications where these technologies can be leveraged in offensive security engagements.

One of the golden rules of machine learning is to apply it to stable data distributions. Amongst the different data modalities, such as text, audio and images, audio applied for voice cloning is one of the most concerning.

Human voice has a stable distribution, at least for the majority of a person’s adulthood. Once cloned, unlike credentials, it cannot be changed. Voice cloning is therefore a perfect candidate to apply machine learning for phishing or social engineering purposes.

Despite voice cloning not being a new topic we nevertheless wanted to cover the gap between hearing existing deep fakes and creating them on our own, determining which level of effort is required and which results can be obtained.

## Methodology

Voice cloning essentially requires three steps: gathering audio recordings of the target, processing them and finally providing the data in input to a deep learning model.

Gathering data is quite straightforward: it consists of finding audio clips from interviews and podcasts, with the only challenge of finding good audio quality with no background noise, music or reverb.

The audio clips then need to be pre-processed to be fit for the model.

The model can be an open source one which can be executed locally, provided that the minimum hardware requirements are met, or an online service.

We did use existing models as black-box as we believe it is a far assumptions that, except for Nation state adversaries, criminals will also use off-the-shelf products.

## Choosing the Model

Under the assumption that voice cloning providers should require some form of voice verification, to ensure that users are cloning their own voice, and not somebody’s else, we chose to run an open-source model locally, namely [tortoise-tts](https://github.com/neonbjb/tortoise-tts), where no restrictions are applied. Given the stunning text to speech capabilities of tortoise-tts with pre-packaged voices, we deemed it as a solid model to experiment with custom voices.

Trivia: tortoise-tts is named after a tortoise for being slow. The fact that it implements a [transformer](https://en.wikipedia.org/wiki/Transformer_%28deep_learning_architecture%29) architecture provided inspiration for the cover art.

## Data Processing

Data processing has some dependencies on the chosen model, while other steps are generally applicable.

In order to perform text to speech with a custom voice, tortoise-tts requires the following:

* Gather audio clips of your speaker(s). Good sources are YouTube interviews (you can use youtube-dl to fetch the audio), audiobooks or podcasts. Guidelines for good clips are in the next section.
* Cut your clips into ~10 second segments. You want at least 3 clips. More is better, but I only experimented with up to 5 in my testing.
* Save the clips as a WAV file with floating point format and a 22,050 sample rate.
* Create a subdirectory in voices/
* Put your clips in that subdirectory.
* Run tortoise utilities with `--voice=<your_subdirectory_name>`

The first step consists of cutting clips into ~10 second segments. It should be obvious that a clip cannot be cut in a for loop every 10 seconds, instead it should be cut when there is silence. In addition, this operation must be scriptable (i.e. no manual work in an editing tool like Audacity).

There exists a tool that handles the job: [sox](https://sourceforge.net/projects/sox/). It is sufficient to experiment with the different thresholds until the clip is correctly cut corresponding to the moments of silence.

One of the three thresholds we experimented with:

```
sox input.wav output.wav silence -l 1 0.1 1% -1 2.0 1% : newfile : restart
```

At this stage, the audio is split without truncation during speaking. However, there is another issue: people do not pause every 10 seconds, as a matter of fact the chunks have different lengths:

```
Created chunk001.wav with duration 3.310476
Created chunk002.wav with duration 0.627438
Created chunk003.wav with duration 5.030567
Created chunk004.wav with duration 2.359819
Created chunk005.wav with duration 4.707120
Created chunk006.wav with duration 2.240544
Created chunk007.wav with duration 1.187574
Created chunk008.wav with duration 1.568345
Created chunk009.wav with duration 3.405034
Created chunk010.wav with duration 2.573333
Created chunk011.wav with duration 4.042993
Created chunk012.wav with duration 1.219184
Created chunk013.wav with duration 2.434875
```

This can be solved with FFMPEG and some scripting around it to merge small chunks into bigger chunks that are around 10 seconds long.

Are we now ready to feed the data to the model? Not quite.

Good audio sources are interviews, and of course an interviewer is present, polluting the input data, and must be removed from the audio.

This problem is less trivial and must be automated. Luckily there exists a technique called “[speaker diarisation](https://en.wikipedia.org/wiki/Speaker_diarisation)” which, given an audio, identifies the number of speakers and marks in seconds the start-end segments for each speaker.

We identified an open-source project which worked particularly well for this purpose: [pyannote](https://github.com/pyannote/pyannote-audio). With some scripting around pyannote’s output we could automatically identify the segments during which the target is speaking, crop them and merge them into a clean audio with the target only.

If the reader were to reproduce our steps we have two recommendations: first a GPU is required as pyannote is yet another deep learning model. Secondly, a quite hidden [github issue](https://github.com/pyannote/pyannote-audio/issues/1403) solved a huge blocker: the GPU was no longer being used with long audios in input, and the solution was to load audios not from the disk but directly from memory.

## Voice Cloning with models

The pre-processed data can now be fed to tortoise-tts with the `--voice` switch. Despite having used good samples in terms of audio quality and length, the results were poor.

Only one attempt yielded an acceptable result, namely this audio track for Edward Snowden.

Using the model as a black box we could not determine if and how the results could be improved.

Therefore, we went back to online providers trying out one and, with great surprise, realized that the identity validation was required only for the high tier offering, while only a self-validation checkbox was required for the low tier one which nevertheless performed v...