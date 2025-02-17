# -*- coding: utf-8 -*-
from Reloading import Load as load


def main():
    #load.reload()
    load_instance = load()
    t1 = load_instance.testing1()
    t1.test()
    
    print("Hello world!")
    

main()