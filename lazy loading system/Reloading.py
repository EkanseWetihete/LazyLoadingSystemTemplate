# -*- coding: utf-8 -*-


class Load:
    def reload(self):
        print("test")
    
    def testing1(self):
        from testing1 import Testing1 as t1
        t1.test()
        return t1()
        
    def testing2(self):
        from testing2 import Testing2 as t2
        t2.test()
        return t2()
        
    
    