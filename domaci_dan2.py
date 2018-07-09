# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:14:35 2018

@author: Win 7
"""

fajl = open("corpus_sample.xml", "r", encoding="utf-8")
recnikImenica = dict()
for red in fajl:
    if red.startswith("<") != True:
        try:
            rec, mala_rec, lema, pos = red.split("\t")
            if pos.startswith("N") == True:
                if lema in recnikImenica.keys():
                    recnikImenica[lema] = recnikImenica[lema] + 1
                else:
                    recnikImenica[lema] = 1
        except:
            pass
        with open("recnikimenica.xml", "a+", encoding="utf-8") as kraj:
           for k in sorted(recnikImenica, key = recnikImenica.get): 
               for k,v in recnikImenica.items():
                   kraj.write(k + "\t\t" + str(v) + "\n")
fajl.close()
