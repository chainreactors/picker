---
title: Fast and accurate syntax searching for C and C++
url: https://blog.trailofbits.com/2022/12/22/syntax-searching-c-c-clang-ast/
source: Trail of Bits Blog
date: 2022-12-23
fetch_date: 2025-10-04T02:20:13.553930
---

# Fast and accurate syntax searching for C and C++

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Fast and accurate syntax searching for C and C++

Mate Kukri

December 22, 2022

[compilers](/categories/compilers/), [internship-projects](/categories/internship-projects/)

The naive approach to searching for patterns in source code is to use [regular expressions](https://en.wikipedia.org/wiki/Regular_expression); a better way is to parse the code with a custom parser, but both of these approaches have limitations. During my internship, I prototyped an internal tool called Syntex that does searching on [Clang ASTs](https://clang.llvm.org/docs/IntroductionToTheClangAST.html) to avoid these limitations. In this post, I’ll discuss Syntex’s unique approach to syntactic pattern matching.

## Searching, but with context

Syntex addresses two overarching problems with traditional pattern-searching tools.

First, existing tools are prone to producing false negatives. These tools usually contain their own parsers that they use depending on the language of the codebase they are searching in. For C and C++ codebases, these tools usually parse source code without performing macro expansion, searching through non-macro-expanded code instead of the macro-expanded code that a real compiler like Clang would produce. This means these tools cannot ensure accurate results. A client of such a tool won’t be able to confidently say, “here are all the occurrences of this pattern” or “this pattern never occurs.” In theory, these tools could match uses of macros in non-macro-expanded code, but in practice, they would be able to match only top-level uses of macros, meaning that false negatives are likely.

Another problem with these tools is that their internal parsers do not use the same representation of the code as a real compiler would, and they do not have an understanding of the semantics of the source code. That is, these tools produce plaintext output highlighting their results, so they cannot provide semantic information about the code in which their results appear. Without such information, it is difficult to further analyze the output, especially using other analysis tools. It is not strictly speaking impossible to access the source code internally parsed by these tools, but it would not be particularly useful in a multi-stage analysis pipeline requiring access to semantic information available only to a compiler. All this severely limits these tools’ usefulness as a foundation on which to use other analysis tools to more deeply analyze the given code.

For instance, let’s say we are trying to find code in which the length of a string in the argument list of a call to some risky function is implicitly truncated. We might have our tool search for the pattern `$func($... $str->len $...)`. The tool will likely find a superset of code snippets that we actually care about. We ought to be able to semantically filter these search results to check that len is the structure field of interest and that its use induces an implicit downcast. However, whatever tool we choose to use would not be able to do this filtering because it would understand only the structure of the code, not the semantics. And because of its lack of semantic understanding, it’s more difficult to introduce other analysis tools to help further analyze the results.

Syntex solves both of these problems by operating on actual Clang ASTs. Because Syntex uses the same ASTs that the compiler uses, it eliminates the inaccuracies of typical pattern-searching tools and provides semantic information for further analysis. Syntex produces results with references to AST nodes, allowing developers to conduct follow-up semantic analysis. For instance, a client enumerating the downcast pattern above will be able to make decisions based on the type and nature of the submatches corresponding to both `func` and `str`.

## Syntex matches syntax patterns against indexed code

Parsing C and C++ code is a notoriously difficult task, in that it requires implementing unbounded lookaheads and [executing Turing-complete templates](https://blog.reverberate.org/2013/08/parsing-c-is-literally-undecidable.html) just to obtain a parse tree. Syntex solves the problem of parsing source code by relying on Clang, but how does it parse Syntex queries themselves?

Aside from queries containing $-prefixed meta variables, Syntex queries are syntactically valid C and C++ code. Ideally, we would parse Syntex queries with Clang, then [unify](https://en.wikipedia.org/wiki/Unification_%28computer_science%29) the parsed queries and parsed source code to identify matches. Unfortunately, life is not so easy: Syntex queries lack the necessary syntactic/semantic context that would allow them to be parsed. For example, the pattern `foo(0)` yields [different parse trees](https://godbolt.org/z/Pa7ET3Tne) depending on the type of `foo`.

Syntex doesn’t directly resolve the edge cases of C and C++ syntax; instead, it considers all possible ambiguous interpretations while parsing queries. However, instead of defining the ambiguous language patterns itself, Syntex derives its pattern grammar from the Clang compiler’s AST. Using this approach, we can guarantee that patterns will be accepted for every construct appearing in the indexed source code.

## Synthesizing the grammar

[![](/img/wpdump/52af3229b32cf193fc539d12735f6567.png)](/img/wpdump/52af3229b32cf193fc539d12735f6567.png)

Parse tree of a simple declaration

At code building and indexing time, Syntex creates a context-free grammar by recursively walking through the Clang AST and recording the relationships between AST nodes. Nodes with children correspond to non-terminals; each appearance of such a node adds a production rule of the form `parent -> child_0 ... child_n`. Nodes with no children become terminal symbols in the generated grammar. For instance, the grammar (production rules and terminals) corresponding to the AST in figure 1 is as follows:

```
DECL_REF_EXPR           -> IDENTIFIER
INTEGER_LITERAL         -> NUMERIC_CONSTANT
IMPLICIT_CAST_EXPR      -> DECL_REF_EXPR
BINARY_OPERATOR         -> IMPLICIT_CAST_EXPR PLUS IMPLICIT_CAST_EXPR
PARENT_EXPR             -> L_PARENTHESIS BINARY_OPERATOR R_PARENTHESIS
BINARY_OPERATOR         -> PAREN_EXPR SLASH INTEGER_LITERAL
VAR                     -> KEYWORD_INT IDENTIFIER EQUAL BINARY_OPERATOR
DECL_STMT               -> VAR SEMI

IDENTIFIER, NUMERIC_CONSTANT, PLUS, L_PARENTHESIS, R_PARENTHESIS, SLASH,
KEYWORD_INT, EQUAL, SEMI
```

If we interpret `DECL_STMT` as the “start symbol” of this grammar, then the grammar is deterministic, and a parser that accepts strings could be generated with the commonly used [LR algorithm](https://en.wikipedia.org/wiki/LR_parser). However, when parsing search queries, Syntex doesn’t actually know the start symbol that the query should reduce to. For example, if the query consists of an `IDENTIFIER` token, then Syntex can parse that token as an `IDENTIFIER`, a `DECL_REF_EXPR` containing an identifier, or an `IMPLICIT_CAST_EXPR` containing a `DECL_REF_EXPR` containing an identifier. This means that, in practice, Syntex assumes that every symbol could be a start symbol and retroactively deduces which rules are start rules based on whether they cover the entire input query.

## Parsing Syntex queries

Conceptually, the first step in parsing a query is to perform tokenization (or lexical analysis). Syntex performs tokenization using a hand-coded state machine. One difference between Syntax’s tokenizer and those used in typical compilers is that Syntex’s tokenizer returns all possible interpretations of the input characters instead of just the greediest interpretation. For example, Syntex would tokenize the string `”<<“` as both `<<` and two `<` symbols following each other. That way, the tokenizer doesn’t have to be aware of which interpretation is necessary in which context.

Syntex parses...