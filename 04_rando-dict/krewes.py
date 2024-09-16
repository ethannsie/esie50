"""
Ethan Sie
Elmo's Cheez-it
SoftDev
K04 -- Python dictionairies and random selection
2024-09-13
time spent: 0.33
"""

import random

krewes = {
           4: [
'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
],
           5: [
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
              ]
         }

keys = list(krewes.keys())
#print(keys)

randKey = keys[random.randint(0, len(keys) - 1)]
#print(krewes.get(randKey))
names = krewes.get(randKey)

randDevo = names[random.randint(0, len(names) - 1)]
print(randDevo)


