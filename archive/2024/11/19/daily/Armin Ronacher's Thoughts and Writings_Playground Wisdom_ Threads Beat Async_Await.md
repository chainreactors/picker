---
title: Playground Wisdom: Threads Beat Async/Await
url: http://lucumr.pocoo.org/2024/11/18/threads-beat-async-await
source: Armin Ronacher's Thoughts and Writings
date: 2024-11-19
fetch_date: 2025-10-06T19:15:56.343538
---

# Playground Wisdom: Threads Beat Async/Await

[Armin Ronacher](/about/)'s Thoughts and Writings

* [blog](/)* [archive](/archive/)* [projects](/projects/)* [travel](/travel/)* [talks](/talks/)* [about](/about/)

# Playground Wisdom: Threads Beat Async/Await

written on November 18, 2024

It’s been a few years since I wrote about my challenges with
`async`/`await`-based systems and how they just seem to not [support back
pressure well](/2020/1/1/async-pressure/). A few years later, I do not
think that this problem has subsided much, but my thinking and
understanding have perhaps evolved a bit. I’m now convinced that
`async`/`await` is, in fact, a bad abstraction for most languages, and we
should be aiming for something better instead and that I believe to be
thread.

In this post, I’m also going to rehash many arguments from very clever
people that came before me. Nothing here is new, I just hope to bring it
to a new group of readers. In particular, you should really consider
these who highly influential pieces:

* Bob Nystrom’s [What Color is Your Function](https://journal.stuffwithstuff.com/2015/02/01/what-color-is-your-function/)
  post, which makes a very strong case that having two types of functions,
  which are only compatible in one direction, causes problems.
* Ron Pressler’s [Please stop polluting our imperative languages with pure
  concepts](https://www.youtube.com/watch?v=449j7oKQVkc) which I think
  is probably the single most important talk on that topic.
* Nathaniel J. Smith’s [Notes on structured concurrency, or: Go statement
  considered harmful](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/)
  which does a really good job laying out the motivation for structured
  concurrency.

## Your Child Loves Actor Frameworks

As programmers, we are so used to how things work that we make some
implicit assumptions that really cloud our ability to think freely. Let
me present you with a piece of code that demonstrates this:

```
def move_mouse():
    while mouse.x < 200:
        mouse.x += 5
        sleep(10)

def move_cat():
    while cat.x < 200:
        cat.x += 10
        sleep(10)

move_mouse()
move_cat()
```

Read that code and then answer this question: do the mouse and cat move at
the same time, or one after another? I guarantee you that 10 out of 10
programmers will correctly state that they move one after another. It
makes sense because we know Python and the concept of threads, scheduling
and whatnot. But if you speak to a group of children familiar with
[Scratch](https://en.wikipedia.org/wiki/Scratch_%28programming_language%29),
they are likely to conclude that mouse and cat move simultaneously.

The reason is that if you are exposed to programming via Scratch you are
exposed to a primitive form of actor programming. The cat and the mouse
are both actors. In fact, the UI makes this pretty damn clear, just that
the actors are called “sprites”. You attach logic to a sprite on the
screen and all these pieces of logic run *at the same time*.
Mind-blowing. You can even send messages from sprite to sprite.

The reason I want you to think about this for a moment is that I think
this is rather profound. Scratch is a very, very simple system and it’s
intended to teaching programming to young kids. Yet the model it promotes
is an actor system! If you were to foray into programming via a
traditional book on Python, C# or some other language, it’s quite likely
that you will only learn about threads at the very end. Not just that, it
will likely make it sound really complex and scary. Worse, you will
probably only learn about actor patterns in some advanced book that will
bombard you with all the complexities of large scale applications.

There is something else though you should keep in mind: Scratch will not
talk about threads, it will not talk about monads, it will not talk about
`async`/`await`, it will not talk about schedulers. As far as you are
concerned as a programmer, it’s an imperative (though colorful and visual)
language with some basic “syntax” support for message passing.
Concurrency comes natural. A child can program it. It’s not something to
be afraid of.

## Imperative Programming Is Not Inferior

The second thing I want you to take away is that imperative languages are
not inferior to functional ones.

While probably most of us are using imperative programming languages to
solve problems, I think we all have been exposed to the notion that it’s
inferior and not particularly pure. There is this world of functional
programming, with monads and other things. This world have these nice things
involving composition, logic and maths and fancy looking theorems. If you
program in that, you’re almost transcending to a higher plane and looking
down to the folks who are stitching together if statements, for loops,
make side effects everywhere, and are doing highly inappropriate things
with IO.

Okay, maybe it’s not quite as bad, but I don’t think I’m completely wrong
with those vibes. And look, I get it. I feel happy chaining together
lambdas in Rust and JavaScript. But we should also be aware that these
constructs are, in many languages, bolted on. Go, for instance, gets away
without most of this, and that does not make it an inferior language!

So what you should keep in mind here is that there are different
paradigms, and mentally you should try to stop thinking for a moment that
functional programming has all its stuff figured out, and imperative
programming does not.

Instead, I want to talk about how functional languages and imperative
languages are dealing with “waiting”.

The first thing I want to back to is the example from above. Both of the
functions (for the cat and the mouse) can be seen as separate threads of
execution. When the code calls `sleep(10)` there’s clearly an
expectation by the programmer that the computer will temporarily pause the
execution and continue later. I don’t want to bore you with monads, so as
my “functional” programming language, I will use JavaScript and promises.
I think that’s an abstraction that most readers will be sufficiently
familiar with:

```
function moveMouseBlocking() {
  while (mouse.x < 200) {
    mouse.x += 5;
    sleep(10);  // a blocking sleep
  }
}

function moveMouseAsync() {
  return new Promise((resolve) => {
    function iterate() {
      if (mouse.x < 200) {
        mouse.x += 5;
        sleep(10).then(iterate);  // non blocking sleep
      } else {
        resolve();
      }
    }
    iterate();
  });
}
```

You can immediately see a challenge here: it’s very hard to translate the
blocking example into a non blocking example because all the sudden we
need to find a way to express our loop (or really any control flow). We
need to manually decompose it into a form of recursive function calling
and we need the help of a scheduler and executor here to do the waiting.

This style obviously eventually became annoying enough to deal with that
`async`/`await` was introduced to mostly restore the sanity of the old
code. So it now can look more like this:

```
async function moveMouseAsync() {
  while (mouse.x < 200) {
    mouse.x += 5;
    await sleep(10);
  }
}
```

Behind the scenes though, nothing has really changed, and in particular,
when you call that function, you just get an object that encompasses the
“composition of the computation”. That object is a promise which will
eventually hold the resulting value. In fact, in some languages like C#, the
compiler will really just transpile this into chained function calls.
With the promise in hand, you can await the result, or register a callback
with `then` which gets invoked if this thing ever runs to completion.

For a programmer, I think `async`/`await` is clearly understood as some
sort of neat abstraction — an abstraction over promises and callbacks.
However strictly speaking, it’s just worse than where we started out,
because in terms of expressiveness, we have lost an important affordance:
we cannot freely suspend.

In the or...