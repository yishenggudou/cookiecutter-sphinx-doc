# cookiecutter-sphinx-doc

一个项目模板基于[cookiecutter](https://github.com/audreyr/cookiecutter)

## 用法

```bash
pip install cookiecutter
cookiecutter https://github.com/yishenggudou/cookiecutter-sphinx-doc.git
```


## example

```bash
(python3) ➜  /tmp cookiecutter https://github.com/yishenggudou/cookiecutter-sphinx-doc.git
You've downloaded /Users/timgerk/.cookiecutters/cookiecutter-sphinx-doc before. Is it okay to delete and re-download it? [yes]: yes
project []: simple doc project
project_slug []: sdp
book_title []: 项实例项目
author []: 作者
version [0.0.1]: 
release [0.0.1]: 
description []: 长的简介
src []: docs
```

然后进入`docs` 看到

```bash
(python3) ➜  docs tree
.
├── Makefile
├── conf.py
├── index.rst
├── intro.md
├── make.bat
├── plantuml.jar
├── releasenotes.py
├── test.rst
└── topdf.sh

0 directories, 9 files
```

#### 生成html

```bash
make html
```

#### 生成pdf

```bash
pip install -r requirements.txt
./topdf.sh
```

文件实例 [pdf实例文件](data/odc.pdf)


## 特点

1. 支持markdown
2. 支持planuml
3. pdf中文支持

## 依赖

1. [mactex](https://tug.org/mactex/mactex-download.html)
2. [planuml](http://plantuml.com/)
3. [httpdomain](https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/)
4. [其他插件](https://github.com/sphinx-contrib)

## 注意

测试仅验证了`python3` 建议`2`的用户 `virtualenv` 到 `3`

## 关注微信公众号

![](data/qrcode_for_gh_eb014d2c0920_344.jpg)