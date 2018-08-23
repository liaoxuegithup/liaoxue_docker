pycharm常用设置
lz提示一下，pycharm中的设置是可以导入和导出的，file>export settings可以保存当前pycharm中的设置为jar文件，重装时可以直接import settings>jar文件，就不用重复配置了。

file -> Setting ->Editor

1. 设置Python自动引入包，要先在 >general > autoimport -> python :show popup

     快捷键：Alt + Enter: 自动添加包
2. “代码自动完成”时间延时设置

  > Code Completion   -> Auto code completion in (ms):0  -> Autopopup in (ms):500

3. Pycharm中默认是不能用Ctrl+滚轮改变字体大小的，可以在〉Mouse中设置

4. 显示“行号”与“空白字符”

  > Appearance  -> 勾选“Show line numbers”、“Show whitespaces”、“Show method separators”

5. 设置编辑器“颜色与字体”主题

  > Colors & Fonts -> Scheme name -> 选择"monokai"“Darcula”

  说明：先选择“monokai”，再“Save As”为"monokai-pipi"，因为默认的主题是“只读的”，一些字体大小颜色什么的都不能修改，拷贝一份后方可修改！

  修改字体大小

> Colors & Fonts -> Font -> Size -> 设置为“14”

6. 设置缩进符为制表符“Tab”

  File -> Default Settings -> Code Style

  -> General -> 勾选“Use tab character”

  -> Python -> 勾选“Use tab character”

  -> 其他的语言代码同理设置

7. 去掉默认折叠
  > Code Folding -> Collapse by default -> 全部去掉勾选

8. pycharm默认是自动保存的，习惯自己按ctrl + s  的可以进行如下设置：
    > General -> Synchronization -> Save files on frame deactivation  和 Save files automatically if application is idle for .. sec 的勾去掉
    > Editor Tabs -> Mark modified tabs with asterisk 打上勾

9.>file and code template>python scripts

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '$Package_name'
__author__ = '$USER'
__mtime__ = '$DATE'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

10 python文件默认编码

File Encodings> IDE Encoding: UTF-8;Project Encoding: UTF-8;

11. 代码自动整理设置



这里line breaks去掉√，否则bar, 和baz会分开在不同行，不好看。

皮皮Blog

File -> Settings -> appearance

1. 修改IDE快捷键方案

  > Keymap

1) execute selection in console : add keymap > ctrl + enter

  系统自带了好几种快捷键方案，下拉框中有如“defaul”,“Visual Studio”,在查找Bug时非常有用,“NetBeans 6.5”,“Default for GNOME”等等可选项，

  因为“Eclipse”方案比较大众，个人用的也比较多，最终选择了“Eclipse”。

  还是有几个常用的快捷键跟Eclipse不一样，为了能修改，还得先对Eclipse方案拷贝一份：

  (1).代码提示功能，默认是【Ctrl+空格】，现改为跟Eclipse一样，即【Alt+/】

  Main menu -> code -> Completion -> Basic -> 设置为“Alt+/”

  Main menu -> code -> Completion -> SmartType -> 设置为“Alt+Shift+/”

  不过“Alt+/”默认又被

  Main menu -> code -> Completion -> Basic -> Cyclic Expand Word 占用，先把它删除再说吧（单击右键删除）！

  (2).关闭当前文档，默认是【Ctrl+F4】，现改为跟Eclipse一样，即【Ctrl+W】

  Main menu -> Window -> Active Tool Window -> Close Active Tab -> 设置为 “Ctrl+F4”;

  Main menu -> Window -> Editor -> Close -> 设置为 “Ctrl+W”;
2.设置IDE皮肤主题


 > Theme -> 选择“Alloy.IDEA Theme”

  或者在setting中搜索theme可以改变主题，所有配色统一改变

File > settings > build.excution

每次打开python控制台时自动执行代码

> console > pyconsole

import sys
# print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
import  os
print('current workdirectory : ', os.getcwd() )
import  numpy as  np
import  scipy as sp
import  matplotlib as mpl
如果安装了ipython，则在pyconsole中使用更强大的ipython

> console

选中use ipython if available

这样每次打开pyconsole就会打开ipython

Note: 在virtualenv中安装ipython: (ubuntu_env) pika:/media/pika/files/mine/python_workspace/ubuntu_env$pip install ipython



File > settings > Languages & Frameworks

如果在项目设置中开启了django支持，打开python console时会自动变成打开django console，当然如果不想这样就关闭项目对django的支持：



如果打开支持就会在 settings > build.excution > console下多显示一个django console:



Django console设置如下

import sys
print('Python %s on %s' % (sys.version, sys.platform))
import django
print('Django %s' % django.get_version())
sys.path.extend([WORKING_DIR_AND_PYTHON_PATHS])
if 'setup' in dir(django): django.setup()
import django_manage_shell; django_manage_shell.run(PROJECT_ROOT)
File > settings > Project : initial project

project dependencies > LDA > project depends on these projects > 选择sim_cluster就可以在LDA中调用sim_cluster中的包

[Configure PyCharm]

皮皮Blog



pycharm环境和路径配置
python解释器路径
python项目解释器路径
用于配置python项目执行的python路径

比如，有的项目是运行的是系统python2.7下的环境；有的是3.4；有的项目使用的是virtualenv的python环境[python虚拟环境配置 - pycharm中的项目配置]

在pycharm > file > settings > project:pythonworkspace > project interpreter > 选择对应项目 > project interpreter中指定python解释器

pycharm中运行configuration有一个选项add content roots to pythonpath

选中后sys.path中会多一整个项目project的路径/media/pika/files/mine/python_workspace，里面的目录就被当成包使用，这样就可以通过from SocialNetworks.SocialNetworks引入不是python包的目录中的文件了。

不过最好使用sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0],"../.."))来添加，这样在pycharm外也可以运行不出错 。

[python模块导入及属性：import ]

pycharm中进行python包管理
pycharm中的项目中可以包含package、目录（目录名可以有空格）、等等

目录的某个包中的某个py文件要调用另一个py文件中的函数，首先要将目录设置为source root，这样才能从包中至上至上正确引入函数，否则怎么引入都出错：

SystemError: Parent module '' not loaded, cannot perform relative import

Note:目录 > 右键 > make directory as > source root

python脚本解释路径
ctrl + shift + f10 / f10 执行python脚本时

当前工作目录cwd为run/debug configurations 中的working directory

可在edit configurations > project or defaults中配置

console执行路径和当前工作目录
python console中执行时

cwd为File > settings > build.excution > console > pyconsole中的working directory

并可在其中配置

pycharm配置os.environ环境
pycharm中os.environ不能读取到terminal中的系统环境变量

pycharm中os.environ不能读取.bashrc参数

使用pycharm，无论在python console还是在module中使用os.environ返回的dict中都没有~/.bashrc中的设置的变量，但是有/etc/profile中的变量配置。然而在terminal中使用python，os.environ却可以获取~/.bashrc的内容。

解决方法1：

在~/.bashrc中设置的系统环境只能在terminal shell下运行spark程序才有效，因为.bashrc is only read for interactive shells.

如果要在当前用户整个系统中都有效（包括pycharm等等IDE），就应该将系统环境变量设置在~/.profile文件中。如果是设置所有用户整个系统，修改/etc/profile或者/etc/environment吧。

如SPARK_HOME的设置[Spark：相关错误总结 ]

解决方法2：在代码中设置，这样不管环境有没有问题了

# spark environment settings
import sys, os
os.environ['SPARK_HOME'] = conf.get(SECTION, 'SPARK_HOME')
sys.path.append(os.path.join(conf.get(SECTION, 'SPARK_HOME'), 'python'))
os.environ["PYSPARK_PYTHON"] = conf.get(SECTION, 'PYSPARK_PYTHON')
os.environ['SPARK_LOCAL_IP'] = conf.get(SECTION, 'SPARK_LOCAL_IP')
os.environ['JAVA_HOME'] = conf.get(SECTION, 'JAVA_HOME')
os.environ['PYTHONPATH'] = '$SPARK_HOME/python/lib/py4j-0.10.3-src.zip:$PYTHONPATH'
pycharm配置第三方库代码自动提示
参考[Spark安装和配置]

皮皮Blog



Pycharm实用拓展功能
pycharm中清除已编译.pyc中间文件
选中你的workspace > 右键 > clean python compiled files

还可以自己写一个清除代码

pycharm设置外部工具
[python小工具 ]针对当前pycharm中打开的py文件对应的目录删除其中所有的pyc文件。如果是直接运行（而不是在下面的tools中运行），则删除E:\mine\python_workspace\WebSite目录下的pyc文件。

将上面的删除代码改成外部工具
PyCharm > settings > tools > external tools > +添加

Name: DelPyc

program: $PyInterpreterDirectory$/python Python安装路径

Parameters: $ProjectFileDir$/Oth/Utility/DelPyc.py $FileDir$

Work directory: $FileDir$

Note:Parameters后面的 $FileDir$参数是说，DelPyc是针对当前pycharm中打开的py文件对应的目录删除其中所有的pyc文件。

之后可以通过下面的方式直接执行


Note:再添加一个Tools名为DelPycIn

program: Python安装路径，e.g.     D:\python3.4.2\python.exe

Parameters: E:\mine\python_workspace\Utility\DelPyc.py

Work directory 使用变量 $FileDir$

参数中没有$FileDir$，这样就可以直接删除常用目录r'E:\mine\python_workspace\WebSite'了，两个一起用更方便

代码质量
当你在打字的时候，PyCharm会检查你的代码是否符合PEP8。它会让你知道，你是否有太多的空格或空行等等。如果你愿意，你可以配置PyCharm运行pylint作为外部工具。

python2转python3最快方式
/usr/bin/2to3 -wn $FileDir$



这样在pycharm中打开某个文件，右键external tools > py2topy3就可以瞬间将当前文件所在目录下的所有py2转换成py3，是不是很机智！

[python2和python3的区别、转换及共存 使用 2to3 工具对代码进行检查和转换]

其它
[pycharm版本控制和数据库管理]

[PyCharm中的那些实用功能]

[使用Pycharm打造高效Python IDE (下)]

from:http://blog.csdn.net/pipisorry/article/details/39909057
ref:pycharm的一些设置和快捷键

