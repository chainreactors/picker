---
title: Hugo Sidenotes Shortcode
url: https://0xda.de/blog/2024/07/hugo-sidenotes-shortcode/
source: Blogs  dade
date: 2024-07-15
fetch_date: 2025-10-06T17:40:27.172690
---

# Hugo Sidenotes Shortcode

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/hugo-sidenotes-shortcode/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Hugo Sidenotes Shortcode](https://0xda.de/blog/2024/07/hugo-sidenotes-shortcode/)

I’ve recently really enjoyed a number of small features that make blogs feel more… interesting. One of those features is sidenotes. They are like footnotes, except, well, on the side. As someone who writes with a lot of parentheticals, a sidenote seems like a great way to remove my comment out of the flow of the sentence and I can make it separate, but still easy to read.

I am certainly not the first to add sidenotes to my blog. [Maggie Appleton](https://maggieappleton.com/)’s site is fantastic in a lot of ways, and sidenotes are indeed one of them.

While discussing this with a friend, he sent me this post about “[microfeatures](https://danilafe.com/blog/blog_microfeatures/)” in blogs and websites. The author of this post also has a post about [implementing Sidenotes in Hugo](https://danilafe.com/blog/sidenotes/), and most importantly, without relying on Javascript. Several of my other posts about my website have highlighted my distaste for requiring javascript to browse my site, so it should come as no surprise that I don’t want to require it here.

Daniel’s blog post about the implementation of sidenotes in Hugo gave me almost everything I needed to get started, but frustratingly there were a few details left out. There was also no example usage, and it required *three* parameters when writing the shortcode. This seemed like too much for my preference, so I wanted to simplify it. I’m not going to dive too far into the rationale of each styling decision here or anything, I think Daniel’s blog does a good job at this. I just wanted to capture and share my variation.

## The Shortcode

Here is Daniel’s shortcode from his blog post.

```
<span class="sidenote">
<label class="sidenote-label" for="{{ .Get 1 }}">{{ .Get 2 }}</label>
<input class="sidenote-checkbox" type="checkbox" id="{{ .Get 1 }}"></input>
<span class="sidenote-content sidenote-{{ .Get 0 }}">
{{ .Inner }}
</span>
</span>
```

As I mentioned, I really didn’t like that this shortcode required three parameters to initialize. The parameters, in order, are:

1. Position of the sidenote (right or left)
2. ID of the sidenote (some unique html identifier)
3. Label text that will show up in your paragraph and link to your sidenote

Then you need to supply the actual sidenote content inside the shortcode block. Now, unfortunately, the bare minimum that will be required here is the label text and the sidenote content. But I think we can optimize the shortcode to make usage simpler.

First, let’s remove the need to create unique identifiers. We can do this by using the `.Ordinal` value inside the shortcode, which will give you a number based on how many times you’ve used the shortcode in the document.

**Note:** One problem with this is that if you ever go back and add a sidenote further up your document, all ids of all later sidenotes will increase by one. But I don’t want to optimize for people deep-linking to sidenotes, so that’s okay.

Now our variation would look like this:

```
<span class="sidenote">
    <label class="sidenote-label" for="sidenote-{{ $.Ordinal }}">{{ .Get 1 }}</label>
    <input class="sidenote-checkbox" type="checkbox" id="sidenote-{{ $.Ordinal }}"></input>
    <span class="sidenote-content sidenote-{{ .Get 0 }}">
    {{ .Inner }}
    </span>
</span>
```

We’ve reduced our parameters to 2, the position of the sidenote and the label text of the sidenote. Note that the positional parameter numbers have changed to reflect the new calling convention. But I think we can still do better. What if we default all of our sidenotes to the right side, unless we explicitly provide a position? We can do that using some conditional logic in the shortcode.

```
<span class="sidenote">
    <label class="sidenote-label" for="sidenote-{{ $.Ordinal }}">{{ .Get 0 }}</label>
    <input class="sidenote-checkbox" type="checkbox" id="sidenote-{{ $.Ordinal }}"></input>
    <span class="sidenote-content sidenote-{{ if ( .Get 1 ) }}{{ .Get 1 }}{{ else }}right{{end}}">
    {{ .Inner }}
    </span>
</span>
```

Now we can
call our shortcode
[ ]

I had to learn how to [escape hugo short codes](https://liatas.com/posts/escaping-hugo-shortcodes/) to display this. Otherwise it would just render the shortcode inside the code block lol.
like so:

```
{{< sidenote "This is an example sidenote" >}}
Sidenotes are pretty cool, this is how they work. Maybe I could make them look a little better, though.
{{< /sidenote >}}
```

Which produces:

This is an example sidenote
[ ]

Sidenotes are pretty cool, this is how they work. Maybe I could make them look a little better, though.

We can also call our shortcode with an explicit position, such as left, to move the sidenote to the left of the page instead of the right.

```
{{< sidenote "This is an example sidenote" left >}}
Sidenotes are pretty cool, this is how they work. Maybe I could make them look a little better, though.
{{< /sidenote >}}
```

Which produces:

This is an example sidenote
[ ]

Sidenotes are pretty cool, this is how they work. Maybe I could make them look a little better, though.

Now we’ve optimized our shortcode for writing, at least as much as Hugo will allow us to, so let’s move on to the style.

## The SCSS

Most of this SCSS is just copied from Daniel’s blog, though there were a few things notably absent from his post that I have included here, such as specifying how the label and content should actually look, as well as defining variables that I didn’t previously have defined, and figuring out a caveat about the main content’s `position` attribute.

```
/*
Make sure that your main content container has position: relative;
Otherwise your sidenotes may show up in weird places, or even off the side of the screen.
In my case, I added position: relative; to my `.post` selector.
*/
:root {
    --neon-pink: #ff6ec7;
}
$sidenote-width: 240px;  // how wide the sidenote can be
$sidenote-offset: 10px; // how much you want to offset the sidenote from the body
$container-width: 800px; // how wide your main content is
.sidenote {
    &:hover {
		background-color: var(--neon-pink);

        .sidenote-label { text-decoration: none; }
        .sidenote-content { border: dashed 3px var(--neon-pink);}
    }
	.sidenote-label {
		text-decoration: underline dashed var(--neon-pink);
	}
}

.sidenote-checkbox {
	display: none;
}

.sidenote-content {
    display: block;
    position: absolute;
    width: $sidenote-width;
    box-sizing: border-box;
    margin-top: -1.5em;
	border: solid 1px var(--border-color);
	padding: 0.5rem;
    font-size: .75rem;

    &.sidenote-right {
        right: 0;
        margin-right: -($sidenote-width + $sidenote-offset);
    }

	&.sidenote-left {
        left: 0;
        margin-left: -($sidenote-width + $sidenote-offset);
    }

	@media screen and
	  (max-width: $container-width + 2 * ($sidenote-width + 2 * $sidenote-offset)) {
      position: static;
      margin-top: 10px;
      margin-bottom: 10px;
      width: 100%;
      display: none;

	  .sidenote-checkbox:checked ~ & {
	    display: block;
	  }

      &.sidenote-right {
        margin-right: 0px;
      }
	  &.sidenote-left {
        margin-left: 0px;
      }
    }
}
```

## Conclusion

Most of the credit for this work goes to [Daniel](https://danilafe.com/). I simply tried to make it a l...