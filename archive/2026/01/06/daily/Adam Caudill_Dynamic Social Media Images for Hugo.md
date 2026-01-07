---
title: Dynamic Social Media Images for Hugo
url: https://adamcaudill.com/2026/01/06/dynamic-social-media-images-for-hugo/?utm_source=atom_feed
source: Adam Caudill
date: 2026-01-06
fetch_date: 2026-01-07T03:29:16.264428
---

# Dynamic Social Media Images for Hugo

# [Adam Caudill](https://adamcaudill.com/)

* [Exposera](https://exposera.com/u/adamcaudill "Exposera")

*Security Leader, Researcher, Developer, Writer, & Photographer*

* [Home](https://adamcaudill.com/)
* [Blog](https://adamcaudill.com/blog/)
* [Research](https://adamcaudill.com/research/)
* [Speaking](https://adamcaudill.com/speaking/)
* [Photography](https://adamcaudill.com/photography/)
* [Writing](https://adamcaudill.com/writing/)
* [About](https://adamcaudill.com/about/)

# Dynamic Social Media Images for Hugo

Today
|
6 minute read
|
[News](https://adamcaudill.com/categories/news)

I’m a big fan of [Hugo](https://gohugo.io/) as a publishing platform, it’s the framework behind this site, and is incredibly flexible – if you are willing to invest the time and effort to make it truly yours. It’s fast, versatile, and has robust theming support. However, it’s also a static site generator, so doing anything dynamic means doing some extra work (as you have to do it at build time).

My life philosophy can be summed up to “work hard to be lazy” - in this case, that means I want a solution for social media sharing (OpenGraph) images that I will work without me needing to think about them again. This way, when a link is shared to Bluesky, Mastodon, LinkedIn, or other platforms, a reasonable image will be shown – even if I didn’t include an image for the article.

More importantly, I was a solution that’s smart about what images it uses.

The solution I use here will select the image to be used, with a series of fallback options, so that there is always an image. In the case of the code below, it uses the following options, in order:

* `images` from the frontmatter.
* `photo` from the frontmatter.
* Image resources for the page with “feature” in the name.
* Image resources for the page with “cover” or “thumbnail” in the name.
* The first image on the page.
* A generated image with the page title.

This ensures that there will always be an image, that it will make the most reasonable choice about what that image is, and, importantly, that I don’t need to lift a finger. There’s nothing to forget, no risk of there being no image.

This is an ideal solution for people like me that sometimes will add images, but often won’t This ensures that when shared on social media, it always looks good.

## Generating Images [#](#generating-images)

The final fallback option, the generated image with the page title is the most recent addition to this design, as in the past the code simply used a single static image. These images are generated using Hugo’s native [images.Text](https://gohugo.io/functions/images/text/) filter, making it quite easy to apply text to an image (it does just what it says on the box). This is a surprisingly friendly and feature.

This does require a little setup, there are two files that will need to be added to your `assets/` directory.

* Font: You will need to add the font you want to use to the `assists/fonts` directory. A broad selection of these can be found on the [Google Fonts Github repo](https://github.com/google/fonts/). Personally, I used [IM Fell English](https://fonts.google.com/specimen/IM%2BFell%2BEnglish), as I love the history behind it, though there are countless options available to suit your site and taste.
* Background Image: You will also need the background image, 1200 x 630 pixels, in the `assets/og-image` directory. This is the image that the text will be applied to.

In the code below, you will need to update the file names as appropriate.

In the code below, you’ll see the heavy lifting for the image generation:

```
{{ $fontPath := "fonts/IMFeENrm28P.ttf" }}
{{ $imagePath := "og-image/bg.jpeg" }}
{{ $filter := "" }}
{{ $r := "" }}
{{ $text := .Title }}
{{ $font := resources.Get $fontPath }}
{{ with $r = resources.Get $imagePath }}
  {{ $opts := dict
    "alignx" "left"
    "aligny" "bottom"
    "color" "#ffffff"
    "font" $font
    "linespacing" 8
    "size" 80
    "x" 10
    "y" (sub .Height 25)
  }}
  {{ $filter = images.Text $text $opts }}
{{ end }}
```

This is a thankfully straightforward implementation of this feature, loading the font and image as resources, collecting the page title as the text to apply, then defining the set of options we’ll use to apply the text. In my case, to match the site’s header, the text is white, the text is placed at the bottom left, and the offset are selected to keep the text visible without running off the image.

This image processing is quite fast, though for large sites, it can slow the generation process down. In my case, the slowdown is approximately 4 seconds.

## The Code [#](#the-code)

The theme for this site started as the publicly available [Kiera](https://github.com/funkydan2/hugo-kiera/tree/master) theme, though has been almost entirely rebuilt, and this incudes often replacing the use of Hugo’s built-in theme components, and replacing or extending them. The code for my OpenGraph image handling is no different, starting as a [11 lines](https://github.com/gohugoio/hugo/blob/release-0.118.2/tpl/tplimpl/embedded/templates/opengraph.html#L6-L17) of code built into Hugo, it grew substantially.

```
{{- if .IsPage }}
    {{ $imgs := findRE "<img.*src=(?:\"|')(.*?)(?:\"|').*?>" .Content 1 }}
    {{ if $imgs }}
        {{ $img := index ($imgs) 0 }}
        {{ $first_img := replaceRE "<img.*src=(?:\"|')(.*?)(?:\"|').*?>" "$1" $img }}
        {{ if $first_img }}
            {{ $first_img := $first_img | absURL}}
            {{ $.Scratch.Set "first_img" $first_img }}
        {{ end }}
    {{ end }}
{{ end -}}

{{ $fontPath := "fonts/IMFeENrm28P.ttf" }}
{{ $imagePath := "og-image/bg.jpeg" }}
{{ $filter := "" }}
{{ $r := "" }}
{{ $text := .Title }}
{{ $font := resources.Get $fontPath }}
{{ with $r = resources.Get $imagePath }}
  {{ $opts := dict
    "alignx" "left"
    "aligny" "bottom"
    "color" "#ffffff"
    "font" $font
    "linespacing" 8
    "size" 80
    "x" 10
    "y" (sub .Height 25)
  }}
  {{ $filter = images.Text $text $opts }}
{{ end }}

{{- with $.Params.images -}}
  {{- range first 6 . }}
    <meta property="og:image" content="{{ . | absURL }}" />
  {{ end -}}
{{- else -}}
  {{- with $.Params.photo -}}
    <meta property="og:image" content="{{ . | absURL }}" />
  {{- else -}}
    {{- $images := $.Resources.ByType "image" -}}
    {{- $featured := $images.GetMatch "*feature*" -}}
    {{- if not $featured }}
      {{ $featured = $images.GetMatch "{*cover*,*thumbnail*}" }}
    {{ end -}}
    {{- with $featured -}}
      <meta property="og:image" content="{{ $featured.Permalink }}"/>
    {{- else -}}
      {{- with $.Scratch.Get "first_img" }}
        <meta property="og:image" content="{{ . }}"/>
      {{- else -}}
        {{ with $r }}
          {{ with . | images.Filter $filter }}
            <meta property="og:image" content="{{ .Permalink }}"/>
          {{ end }}
        {{ end }}
      {{- end -}}
    {{- end -}}
  {{- end -}}
{{- end -}}
```

For my site, I’ve placed this in a dedicated file, `opengraph_image.html`, which is included as a partial in my header file. Whenever possible, I keep self-contained blocks such as this in separate files to improve readability and keep any other files from uncontrollable growth.

This provides an approach that is incredibly simple for day-to-day use, while being extremely flexible and ensuring a positive sharing experience for readers. This can be implemented in only a few minutes but will save you time and leave you with one less thing to worry about in the future.

If you are building or improving a Hugo site, I hope this was useful to you.

Adam Caudill

---

## Related Posts

* ### [Snapchat: API & Security](https://adamcaudill.com/2012/06/16/snapchat-api-and-security/ "Snapchat: API & Security")

  June 17, 2012
  |
  4 minute read
  |
  [Security Research](https://adamcaudill.com/categories/security-research)
* ### [Lessons Learned from 20 Years & Why You Should Blog](https://adamcaudill.com/2026/01/04/lessons-lea...