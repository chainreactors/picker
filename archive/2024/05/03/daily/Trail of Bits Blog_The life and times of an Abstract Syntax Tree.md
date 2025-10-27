---
title: The life and times of an Abstract Syntax Tree
url: https://blog.trailofbits.com/2024/05/02/the-life-and-times-of-an-abstract-syntax-tree/
source: Trail of Bits Blog
date: 2024-05-03
fetch_date: 2025-10-06T17:14:57.462618
---

# The life and times of an Abstract Syntax Tree

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# The life and times of an Abstract Syntax Tree

Francesco Bertolaccini

May 02, 2024

[compilers](/categories/compilers/), [research-practice](/categories/research-practice/)

You’ve reached computer programming nirvana. Your journey has led you down many paths, including [believing that God wrote the universe in LISP](https://xkcd.com/224/), but now the truth is clear in your mind: every problem can be solved by writing one more compiler.

It’s true. Even our soon-to-be artificially intelligent overlords [are nothing but compilers](https://twitter.com/theseamouse/status/1771323607622312279), just as the legends foretold. That smart contract you’ve been writing for your revolutionary DeFi platform? It’s going through a compiler at some point.

Now that we’ve established that *every* program should contain at least one compiler if it doesn’t already, let’s talk about how one should go about writing one. As it turns out, this is a pretty vast topic, and it’s unlikely I’d be able to fit a thorough disquisition on the subject in the margin of this blog post. Instead, I’m going to concentrate on the topic of Abstract Syntax Trees (ASTs).

In the past, I’ve worked on a [decompiler that turns LLVM bitcode into Clang ASTs](https://github.com/lifting-bits/rellic), and that has made me into someone with opinions about them. These are opinions on the things they don’t teach you in school, like: what should the API for an AST look like? And how should it be laid out in memory? When designing a component from scratch, we must consider those aspects that go beyond its mere functionality—I guess you could call these aspects “pragmatics.” Let’s go over a few of them so that if you ever find yourself working with ASTs in the future, you may skip the more head-scratching bits and go straight to solving more cogent problems!

### What are ASTs?

On their own, ASTs are not a very interesting part of a compiler. They are mostly there to translate the dreadful stream of characters we receive as input into a more palatable format for further compiler shenanigans. Yet the way ASTs are designed can make a difference when working on a compiler. Let’s investigate how.

### Managing the unmanageable

If you’re working in a managed language like C# or Java, one with a garbage collector and a very OOP type system, your AST nodes are most likely going to look something like this:

```
class Expr {}
class IntConstant : Expr {
    int value;
}
class BinExpr : Expr {
    public Expr lhs;
    public Expr rhs;
}
```

This is fine—it serves the purpose well, and the model is clear: since all of the memory is managed by the runtime, ownership of the nodes is not really that important. At the end of the day, those nodes are not going anywhere until everyone is done with them and the GC determines that they are no longer reachable.

(As an aside, I’ll be making these kinds of examples throughout the post; they are not meant to be compilable, only to provide the general idea of what I’m talking about.)

I typically don’t use C# or Java when working on compilers, though. I’m a C++ troglodyte, meaning I like keeping my footguns cocked and loaded at all times: since there is no garbage collector around to clean up after the mess I leave behind, I need to think deeply about who owns each and every one of those nodes.

Let’s try and mimic what was happening in the managed case.

### The naive approach

```
struct Expr {
    virtual ~Expr();
};
struct IntConstant : Expr {
    int value;
};
struct BinExpr : Expr {
    std::shared_ptr lhs;
    std::shared_ptr rhs;
};
```

Shared pointers in C++ use reference counting (which one could argue is a form of automatic garbage collection), which means that the end result is similar to what we had in Java and C#: each node is guaranteed to stay valid *at least* until the last object holding a reference to it is alive.

That *at least* in the previous sentence is key: if this was an Abstract Syntax Graph instead of an Abstract Syntax Tree, we’d quickly find ourselves in a situation where nodes would get stuck in a limbo of life detached from material reality, a series of nodes pointing at each other in a circle, forever waiting for someone else to die before they can finally find their eternal rest as well.

Again, this is a purely academic possibility since a tree is by definition acyclic, but it’s still something to keep in mind.

I don’t know Rust that well, but it is my understanding that a layout roughly equivalent to the one above would be written like this:

```
enum Expr {
    IntConstant(i32),
    BinExpr(Arc<Expr>, Arc<Expr>)
}
```

When using this representation, your compiler will typically hold a reference to a root node that causes the whole pyramid of nodes to keep standing. Once that reference is gone, the rest of the nodes follow suit.

Unfortunately, each pointer introduces additional computation and memory consumption due to its usage of an atomic reference counter. Technically, one could avoid the “atomic” part in the Rust example by using Rc instead of Arc, but there’s no equivalent of that in C++ and my example would not work as well. In my experience, it’s quite easy to do away with the ceremony of making each node hold a reference count altogether, and instead decide on a more disciplined approach to ownership.

### The “reverse pyramid” approach

```
struct Expr {
    virtual ~Expr();
};
struct IntConstant : Expr {
    int value;
};
struct BinExpr : Expr {
    std::unique_ptr lhs;
    std::unique_ptr rhs;
};
```

Using unique pointers frees us from the responsibility of keeping track of when to free memory without adding the overhead of reference counting. While it’s not possible for multiple nodes to have an owning reference to the same node, it’s still possible to express cyclic data structures by dereferencing the unique pointer and storing a reference instead. This is (very) roughly equivalent to using `std::weak_ptr` with shared pointers.

Just like in the naive approach, destroying the root node of the AST will cause all of the other nodes to be destroyed with it. The difference is that in this case we are guaranteed that this will happen, because every child node is owned by their parent and no other owning reference is possible.

I believe this representation is roughly equivalent to this Rust snippet:

```
enum Expr {
    IntConstant(i32),
    BinExpr(Box<Expr>, Box<Expr>)
}
```

#### Excursus: improving the API

We are getting pretty close to what I’d call the ideal representation, but one thing I like to do is to make my data structures as immutable as possible.

`BinExpr` would probably look like this if I were to implement it in an actual codebase:

```
class BinExpr : Expr {
    std::unique_ptr lhs, rhs;
public:
    BinExpr(std::unique_ptr lhs, std::unique_ptr rhs)
        : lhs(std::move(lhs))
        , rhs(std::move(rhs)) {}
    const Expr& get_lhs() const { return *lhs; }
    const Expr& get_rhs() const { return *rhs; }
};
```

This to me signals a few things:

* Nodes are immutable.
* Nodes can’t be null.
* Nodes can’t be moved; their owner is fixed.

### Removing the safeguards

The next step is to see how we can improve things by removing some of the safeguards that we’ve used so far, without completely shooting ourselves in the foot. I will not provide snippets on how to implement these approaches in Rust because last time I asked how to do that in my company’s Slack channel, the responses I received were something like “don’t” and “why would you do that?” and “someone please call security.” It should not have been a surprise, as an AST is basically a linked list with extra steps, and Rust hates linked lists.

Up until now, the general idea has been that nodes own other nodes. This makes it quite easy to handle the AST safely because the nodes are self-contained.

What if we de...