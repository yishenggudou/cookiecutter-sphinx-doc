使用plantuml来画UML
====================

UML在各种项目中用来描述项目,系统,流程,便于理解.我们既然是技术类写作,UML少不了.

什么是PlantUML PlantUML是一个快速创建UML图形的组件，PlantUML支持的图形有： sequence diagram, use case diagram, class diagram, activity diagram, component diagram, state diagram, object diagram, wireframe graphical interface PlantUML通过简单和直观的语言来定义图形，语法参见PlantUML Language Reference Guide，它支持很多工具，可以生成PNG、SVG、LaTeX和二进制图片

更多内容参见plantuml官网 `plantuml`_.

下面说下怎么和sphinx一起结合使用. 主要两种方式

sphinx提供了支持`plantuml`_ 的插件 `sphinx-contrib-plantuml`_ `sphinx-contrib-plantuml`_ 提供了一个`uml`指令

`uml`指令可以有四个配置项

=====      ======================================
配置项      可选值
=====      ======================================
height
width
scale
align      `left`,`center`,`right`
alt
caption
=====      ======================================




1. 在rst中使用文件
2. 在rst中使用代码

使用文件
-----------------------------

.. code-block:: python

    .. uml:: /_static/test.puml

.. uml:: /_static/test.puml
    :align: center


使用代码
-------------------------------
用法

.. code-block:: python

    .. uml::
       :caption: Caption with **bold** and *italic*
       :width: 100mm

       Foo <|-- Bar

结果

.. uml::
   :caption: Caption with **bold** and *italic*
   :width: 100mm

   Foo <|-- Bar


.. note::
   使用代码方式主题将不会生效,主要sphinx插件 `sphinx-contrib-plantuml`_ 不支持.


.. _plantuml: http://plantuml.com/
.. _planttext: https://www.planttext.com/
.. _sphinx-contrib-plantuml: https://github.com/sphinx-contrib/plantuml/