# 使用markdown来写作

rst很强大,But现在markdown更流行,如果你想在sphinx中使用markdown来写作也是可以的,
sphinx也提供了组件[recommonmark](http://recommonmark.readthedocs.io/en/latest/index.html),具体参见[sphinx-markdown](http://www.sphinx-doc.org/en/stable/markdown.html)
但是recommonmark只实现了基础版本的[markdown语法](http://commonmark.org/help/)

## 简介

参见

1. [markdown语法](http://commonmark.org/help/)
2. [rst](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#colored-boxes-note-seealso-todo-and-warnings)
3. [rst][http://sphinx-doc-zh.readthedocs.io/en/latest/rest.html]

下面演示用法,你看到的是渲染后的结果了,具体源码参见示例

## code

```
\`\`\`

code

\`\`\`

\`\`\`ipython
In [1]: import os

In [2]:
\`\`\`
```

结果

```

code

```

```ipython
In [1]: import os

In [2]:
```

## sas

`hello`


## math
```
a = \`$ y=\sum_{i=1}^n g(x_i) $\`

a+b

\`\`\`math
  (a + b)^2 = a^2 + 2ab + b^2

\`\`\`
```

结果


a = `$ y=\sum_{i=1}^n g(x_i) $`

a+b

```math
  (a + b)^2 = a^2 + 2ab + b^2

```


## rst

```
\`\`\`eval_rst
.. todo::

    some todo things

\`\`\`


\`\`\`eval_rst
.. note::

    some todo things

\`\`\`



\`\`\`eval_rst
.. warning:: note the space between the directive and the text
\`\`\`

\`\`\`eval_rst
.. seealso:: This is a simple **seealso** note.

\`\`\`
```


结果:

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

```
\`\`\`eval_rst
.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====
\`\`\`
```

结果

```eval_rst
.. table:: Truth table for "not"
   :widths: auto

   =====  =====
     A    not A
   =====  =====
   False  True
   True   False
   =====  =====
```

## 脚注
```
\`\`\`eval_rst
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
\`\`\`
```

结果
```eval_rst
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] Text of the first footnote.
.. [#f2] Text of the second footnote.
```


## 引证

```
\`\`\`eval_rst

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

\`\`\`
```

```eval_rst

Lorem ipsum [Ref]_ dolor sit amet.

.. [Ref] Book or article reference, URL or whatever.

```

## 注释

```
\`\`\`eval_rst
..
   This whole indented block
   is a comment.

   Still in the comment.
\`\`\`
```

结果:

```eval_rst
..
   This whole indented block
   is a comment.

   Still in the comment.
```

## image

```
![](https://www.baidu.com/img/bd_logo1.png)
```

![](https://www.baidu.com/img/bd_logo1.png)