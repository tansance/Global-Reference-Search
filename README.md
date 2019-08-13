Global Reference Search Tool
==========================
![build status](https://img.shields.io/badge/build-passing-brightgreen)
![version](https://img.shields.io/badge/version-1.0.0-orange)
[![platform](https://img.shields.io/badge/platform-windows-inactive)](https://shields.io/) 

全局被引检索工具主要功能是搜索指定文件夹下所有包含特定字符串的文件。搜索到符合条件的文件后，会返回并显示文件的路径、匹配行及匹配行上下文。双击文件路径，可直接打开对应文件。除此之外，工具针对Cocos引擎的CSD文件单独设置了一套搜索及打开文件的逻辑，可通过双击，直接打开包含该CSD文件的CCS文件。

## 1.准备工作
### 1.1环江配置
以下是工具的开发环境：
* Language: python2.7.16
* IDE: pycharm-community-2019.1.3
* Python Packages:
  * QT: PyQt4   
  * pip 19.1.1
  * pyinstaller

### 1.2安装
#### 1.2.1pip安装：   
pip是Python的包管理工具，该工具提供了对Python 包的查找、下载、安装、卸载的功能。我们后面会用它来安装PyQt4以及pyinstaller，因此先来解决它。   
Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。   
可以通过以下命令来判断是否已经安装：

```cmd
pip --version
```

#### 1.2.2pip下载
若未安装可通过以下方式安装：   
安装包下载地址：https://pypi.org/project/pip/#files   
[**一键下载pip**](://files.pythonhosted.org/packages/8b/8a/1b2aadd922db1afe6bc107b03de41d6d37a28a5923383e60695fba24ae81/pip-19.2.1.tar.gz)   
这里选择的是19.1.1版本的tar.gz

#### 1.2.3解压安装
下载完成后直接解压到工作目录下（如D:\），打开Windows cmd，运行如下命令进入解压后的pip目录

```cmd
cd /d D:\pip-9.0.1
```

进入pip的目录后，使用如下命令进行安装

```cmd
python setup.py install
```

#### 1.2.4添加环境变量
若python的目录是：F:\Python27\;   
则添加F:\Python27\Scripts;到系统环境变量中，即完成安装。直接在cmd中输入pip即可查看pip的帮助文档

#### 1.2.5常见问题
##### 执行python setup.py install报错
python错误：<font color="red">ImportError: No module named setuptools</font>   
这句错误提示的表面意思是：没有setuptools的模块，说明python缺少这个模块，那我们只要安装这个模块即可解决此问题，下面我们来安装一下：   
1.下载setuptools包：https://pypi.python.org/pypi/setuptools   
2.解压setuptools包   
3.进入解压路径，cmd中输入命令，开始编译setuptools：  
```cmd
python setup.py build   
```   
4.cmd中输入命令，开始执行setuptools安装：
```
python setup.py install   
```
安装完成后，再进入pip的解压文件夹，执行```python setup.py install```就ok了

### 1.3 PyQt4安装与工具配置   
PyQt4是Qt针对python开发的一套GUI开发工具   
#### 1.3.1 PyQt4安装
直接网上下载[PyQt4-4.11.4-cp27-cp27m-win_amd64.whl](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)，具体版本根据个人实际情况来，python版本以及x系统位数都对应上即可，下面以我的开发环境为例安装步骤如下：   
1. 下载PyQt4-4.11.4-cp27-cp27m-win_amd64.whl后将其放到E:\tools\Python2716\Scripts路径下； 
2. cmd 管理员身份运行，执行命令
```cmd
cd E:\tools\Python2716\Scripts
pip install PyQt4-4.11.4-cp27-cp27m-win_amd64.whl
```
3. 完成

#### 1.3.2 工具配置
##### Pycharm中添加QtDesigner   
PyQt自带的设计GUI的图形界面，可以通过拖动控件至窗体直接设计GUI，用起来很方便，设计后的文档会保存为*.ui文件   
###### 配置
打开Pycharm->File->Settings   
![Pycharm Settings](http://github.com/tansance/Global-Reference-Search/raw/master/images/setting.png)   
点击Tools->External Tools->'+'   
![Pycharm External Tools](http://github.com/tansance/Global-Reference-Search/raw/master/images/adding_external_tool.png)   
如图配置   
![Pycharm QTDesigner](http://github.com/tansance/Global-Reference-Search/raw/master/images/designer.png)   

##### Pycharm中添加pyuic    
PyQt自带的\*.ui文件转\*.py文件的工具，转换为\*.py文件后，程序才能直接引用。由于可能频繁多次将\*.ui文件转换为\*.py文件，旧的\*.py文件会被直接覆盖掉，因此任何与GUI布局无关的代码都不要写在转换后的\*.py文件中。
###### 配置
同样的地方，再点一次'+'开始按图配置   
![Pycharm pyuic](http://github.com/tansance/Global-Reference-Search/raw/master/images/pyuic.png)   

### 1.4 pyinstaller安装   
python用来将程序打包成\*.exe文件比较好用的一个工具。
#### 安装   
这里再一次用到了我们之前安装的pip，直接在cmd中执行:
```
pip install pyinstaller
```
搞定！

## 2.运行
### 2.1文件结构介绍
包名|职能|
----|----|
global_search|定义搜索逻辑。使用DFS遍历文件夹，搜索符合条件的文件|
search_utilities|定义一个QObject子类。用于搜索功能多线程的moveToThread方法实现|
searching_thread|定义一个QThread子类。用于搜索功能多线程的QThread.start()方法实现|
GUI|GUI与主函数所在。<font color="red">运行globalReferenceSearch.py文件即可运行工具</font>|
GUI/dist|包含打包好的可运行程序*.exe|

### 2.2使用说明    
当选择对所有文件搜索时，CCS文件路径设置栏会变更到无法编辑的状态。
![search_common_files](http://github.com/tansance/Global-Reference-Search/raw/master/images/search_normal.gif)

## 3.pyinstaller打包资源文件
### 3.1 pyinstaller使用方式：
#### 3.1.1 一步到位式
1. 需要先进入想要打包的\*.py文件所在目录
2. 使用```pyinstaller -F -w your_file_name.py```即可进行打包   
   * Note: 其中，```-F```表示只生成一个\*.exe文件，```-w```表示关闭控制台显示
3. 生成的\*.exe文件位于同一文件路径下新生成的dist文件夹中。

#### 3.1.2 分步式
1. 同样先进入想要打包的\*.py文件所在目录
2. 使用```pyi-makespec <options> filename.py```来单独生成spec文件，spec文件是pyinstaller的打包设置文件
3. 使用pyinstaller <options> filename.spec直接根据spec文件的设置进行打包

### 3.2 pyinstaller打包资源文件：
#### Step1
1. 使用```pyi-makespec <options> filename.py```来单独生成spec文件
2. 将需要打包的资源文件添加到spec文件中对应的位置   
示例spec文件：
```
# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'], // 被打包文件名
             pathex=['C:\\Users\\zhaozongyang\\Desktop\\tools\\diff\\GUI'], //打包路径
             binaries=[], //二进制资源文件，以tuple形式给出('当前路径','打包后存放的相对路径')
             datas=[('title.png','.')], //非二进制资源文件，以tuple形式给出('当前路径','打包后存放的相对路径')
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True /*运行时打开cmd*/, icon='title.ico' /*icon设置，格式只能为.ico类型的*/)
```
   * Note: 添加了资源文件再打包时，其实际会将所有资源一起打包进exe，点击exe运行时，会自解压生成一个临时文件夹，所有的资源都在这个文件夹内，程序关闭后临时文件夹将被删除，下次启动文件夹时自动创建。因此需要在程序中引用到资源的地方重新设置引用路径。

3. 在所有引用了被打包的资源文件的地方，重新设置引用路径
```python
import sys
import os
try:
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
except Exception:
    base_path = os.path.abspath(".")
final_path = os.path.join(base_path, resourse_path)
```

4. 使用```pyinstaller <options> filename.spec```对更改好的设置文件进行打包，生成\*.exe文件
   * Note:
在设置资源文件时要注意，若给定资源tuple('title.png','title.png')则资源文件title.png会被存储在临时文件夹的.\title.png\title.png处，('title.png','.')则表示直接将title.png存储在临时文件夹的根目录处