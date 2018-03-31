# 使用项目

本次的安装所有在`python3.5` 环境下安装,

什么? `python2.x` 怎么办? 

都什么年代, 你想要被2的中文折腾可以自己研究一下

## 安装`cookiecutter`

```bash
pip install cookiecutter
```

未防止一些全局版本问题尽量使用 `virtualenv`

## 生成样板工程

切换到测试演示目录,并且切换到`virtualenv`

```bash
cd tmp
mkdir test_doc
. /data/vpythons/python3/bin/activate 
```

用`cookiecutter`命令生成项目模板
命令过程中可能需要输入一些基本的数据信息

```
(python3) ➜  test_doc cookiecutter https://github.com/yishenggudou/cookiecutter-sphinx-doc.git
You've downloaded /Users/timgerk/.cookiecutters/cookiecutter-sphinx-doc before. Is it okay to delete and re-download it? [yes]: yes
project [example project name]: 
project_slug [epo]: 
book_title [实例项目文档]: 
author [author name]: 
version [0.0.1]: 
release [0.0.1]: 
description [some long description]: 
src [docs]: 
```

安装环境需要的依赖

```bash
pip install -r requirements.txt
```

测试html部分

```bash
cd docs
make html
open _build/html/index.html
```

测试生成pdf

```bash
cd docs
./topdf.sh
```

