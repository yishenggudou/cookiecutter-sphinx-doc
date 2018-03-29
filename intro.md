# 测试文档2121

### 简介

1. [markdown语法](http://commonmark.org/help/)
2. [rst](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#colored-boxes-note-seealso-todo-and-warnings)
3. [rst][http://sphinx-doc-zh.readthedocs.io/en/latest/rest.html]

### code

```

code

```

```ipython
In [1]: import os

In [2]:
```

### sas

`hello`


### math

a = `$ y=\sum_{i=1}^n g(x_i) $`

a+b

```math
  (a + b)^2 = a^2 + 2ab + b^2

```


### rst



```eval_rst
.. todo::

    some todo things

```


```eval_rst
.. note::

    some todo things

```



```eval_rst
.. warning:: note the space between the directive and the text
```

```eval_rst
.. seealso:: This is a simple **seealso** note.

```


## table

| 1 | 1 | 1 |
| --- | --- | --- |
|  1|  1|  1|

## 脚注

```eval_rst
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
```


## 引证

```eval_rst

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

```

## 注释

```eval_rst
..
   This whole indented block
   is a comment.

   Still in the comment.
```

## image

![](https://pic3.zhimg.com/v2-c657cb9afc6db03a7ae7529dae58ced9_is.jpg)