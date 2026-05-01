---
title: Markdown 双哈希逃逸 (Bleach 清洗后 markdown2 SafeMode 的 Alt 属性 XSS 完整链路)
url: https://mp.weixin.qq.com/s/GcEmnucQDb5tOc8UO0O7Ig
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:34:48.646918
---

# Markdown 双哈希逃逸 (Bleach 清洗后 markdown2 SafeMode 的 Alt 属性 XSS 完整链路)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SPfHPOgCrHqnDL0XU9LpLUGmpFnKV5JjzaPcd9neI2Eym5ticMLicR6VMKQFYlvDWFEYV7ESTnFzVS9n3iaDI4IgdwChpMfaEmCI9YvnfndCPs/0?wx_fmt=jpeg)

# Markdown 双哈希逃逸 (Bleach 清洗后 markdown2 SafeMode 的 Alt 属性 XSS 完整链路)

原创

YMsora
YMsora

YMs0ra的安全漫路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

就按照闲谈学习去完成这个吧

无容置疑的点只有两个，就是需要让markdown语法和js进行联系

以及让bot的无头浏览器执行我们的js

我们看代码片段

```
safe_md = bleach.clean(        md,        tags=[],        attributes={},        protocols=[],        strip=True,        strip_comments=True,    )
```

直接进行追溯

这个函数传的参数很多都是默认的

```
def clean(    text,    tags=ALLOWED_TAGS,#[]    attributes=ALLOWED_ATTRIBUTES,#{}    protocols=ALLOWED_PROTOCOLS,#[]    strip=False,    strip_comments=True,    css_sanitizer=None,):
    cleaner = Cleaner(        tags=tags,        attributes=attributes,        protocols=protocols,        strip=strip,        strip_comments=strip_comments,        css_sanitizer=css_sanitizer,    )    return cleaner.clean(text)
```

继续跟

```
def clean(self, text):        if not isinstance(text, str):            message = (                f"argument cannot be of {text.__class__.__name__!r} type, "                + "must be of text type"            )            raise TypeError(message)
        if not text:            return ""
        dom = self.parser.parseFragment(text)#text是的        filtered = BleachSanitizerFilter(            source=self.walker(dom),            allowed_tags=self.tags,            attributes=self.attributes,            strip_disallowed_tags=self.strip,            strip_html_comments=self.strip_comments,            css_sanitizer=self.css_sanitizer,            allowed_protocols=self.protocols,        )
        # Apply any filters after the BleachSanitizerFilter        for filter_class in self.filters:            filtered = filter_class(source=filtered)
        return self.serializer.render(filtered)
```

其中parseFragment(text)是讲其解析为良好的树形结构，暂时不看

看看BleachSanitizerFilter

```
def sanitize_token(self, token):        """Sanitize a token either by HTML-encoding or dropping.
        Unlike sanitizer.Filter, allowed_attributes can be a dict of {'tag':        ['attribute', 'pairs'], 'tag': callable}.
        Here callable is a function with two arguments of attribute name and        value. It should return true of false.
        Also gives the option to strip tags instead of encoding.
        :arg dict token: token to sanitize
        :returns: token or list of tokens
        """        token_type = token["type"]        if token_type in ["StartTag", "EndTag", "EmptyTag"]:            if token["name"] in self.allowed_tags:                return self.allow_token(token)
            elif self.strip_disallowed_tags:                return None
            else:                return self.disallowed_token(token)
        elif token_type == "Comment":            if not self.strip_html_comments:                # call lxml.sax.saxutils to escape &, <, and > in addition to " and '                token["data"] = html5lib_shim.escape(                    token["data"], entities={'"': "&quot;", "'": "&#x27;"}                )                return token            else:                return None
        elif token_type == "Characters":            return self.sanitize_characters(token)
        else:            return token
```

其实就是将html标签转为不支持的格式

然后直接转markdown，看看当markdown的safe标签的时候的过滤

 html = Markup(markdown2.markdown(safe\_md, safe\_mode="escape"))

```
def _sanitize_html(self, s: str) -> str:        if self.safe_mode == "replace":            return self.html_removed_text        elif self.safe_mode == "escape":            replacements = [                ('&', '&amp;'),                ('<', '&lt;'),                ('>', '&gt;'),            ]            for before, after in replacements:                s = s.replace(before, after)            return s        else:            raise MarkdownError("invalid value for 'safe_mode': %r (must be "                                "'escape' or 'replace')" % self.safe_mode)
    _inline_link_title = re.compile(r'''            (                   # \1              [ \t]+              (['"])            # quote char = \2              (?P<title>.*?)              \2            )?                  # title is optional          \)$        ''', re.X | re.S)    _tail_of_reference_link_re = re.compile(r'''          # Match tail of: [text][id]          [ ]?          # one optional space          (?:\n[ ]*)?   # one optional newline followed by spaces          \[            (?P<id>[^\[\]]*?)          \]        ''', re.X | re.S)
    _whitespace = re.compile(r'\s*')
    _strip_anglebrackets = re.compile(r'<(.*)>.*')
```

貌似核心不在这，我们回去跟text

在text最开始进markdown主函数的时候调用了convert

```
def convert(self, text: str) -> 'UnicodeWithAttrs':        """Convert the given text."""        # Main function. The order in which other subs are called here is        # essential. Link and image substitutions need to happen before        # _EscapeSpecialChars(), so that any *'s or _'s in the <a>        # and <img> tags get encoded.
        # Clear the global hashes. If we don't clear these, you get conflicts        # from other articles when generating a page which contains more than        # one article (e.g. an index page that shows the N most recent        # articles):        self.reset()
        if not isinstance(text, str):            # TODO: perhaps shouldn't presume UTF-8 for string input?            text = str(text, 'utf-8')
        if self.use_file_vars:            # Look for emacs-style file variable hints.            text = self._emacs_oneliner_vars_pat.sub(self._emacs_vars_oneliner_sub, text)            emacs_vars = self._get_emacs_vars(text)            if "markdown-extras" in emacs_vars:                splitter = re.compile("[ ,]+")                for e in splitter.split(emacs_vars["markdown-extras"]):                    if '=' in e:                        ename, earg = e.split('=', 1)                        try:                            earg = int(earg)                        except ValueError:                            pass                    else:                        ename, earg = e, None                    self.extras[ename] = earg
            self._setup_extras()
        # Standardize line endings:        text = text.replace("\r\n", "\n")        text = text.replace("\r", "\n")
        # Make sure $text ends with a couple of newlines:        text += "\n\n"
        # Convert all tabs to spaces.        text = self._detab(text)
        # Strip any lines consisting only of spaces and tabs.        # This makes subsequent regexen easier to write, because we can        # match consecutive blank lines with /\n+/ instead of something        # contorted like /[ \t]*\n+/ .        text = self._ws_only_line_re.sub("", text)
        # strip metadata from head and extract        if "metadata" in self.extras:            text = self._extract_metadata(text)
        text = self.preprocess(text)
        if self.safe_mode:            text = self._hash_html_spans(text)
        # Turn block-level HTML blocks into hash entries        text = self._hash_html_blocks(text, raw=True)
        # Strip link definitions, store in hashes.        if "footnotes" in self.extras:            # Must do footnotes first because an unlucky footnote defn            # looks like a link defn:            #   [^4]: this "looks like a link defn"            text = self._strip_footnote_definitions(text)        text = self._strip_link_definitions(text)
        text = self._run_block_gamut(text)
        if "footnotes" in self.extras:            text = self._do_footnote_marker(text)            text = self._add_footnotes(text)
        text = self.postprocess(text)
        text = self._unescape_special_chars(text)
        text = self._unhash_html_spans(text)        if self.safe_mode:            # return the removed text warning to its markdown.py compatible form            text = text.replace(self.html_removed_text, self.html_removed_text_compa...