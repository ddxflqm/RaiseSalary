#coding:UTF-8
'''
Created on 2018年5月23日
@author: vn0umhp

sys.modules是一个全局字典，该字典是python启动后就加载在内存中。
每当程序员导入新的模块，sys.modules都将记录这些模块。
字典sys.modules对于加载模块起到了缓冲的作用。当某个模块第一次导入，
字典sys.modules将自动记录该模块。当第二次再导入该模块时，python会
直接到字典中查找，从而加快了程序运行的速度。
'''

import sys

# print sys.modules
# print sys.modules.keys()
# print sys.modules.values()
print sys.modules["os"]