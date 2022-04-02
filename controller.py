#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pyfirmata
comport='COM5'
board = pyfirmata.Arduino(comport)

ledg= board.get_pin('d:6:o')
ledb= board.get_pin('d:5:o')
ledr= board.get_pin('d:4:o')
ledy= board.get_pin('d:3:o')
ledw= board.get_pin('d:2:o')

def led(total):
    if total==0:
        ledg.write(0)
        ledb.write(0)
        ledr.write(0)
        ledy.write(0)
        ledw.write(0)

    elif total==1:
        ledg.write(1)
        ledb.write(0)
        ledr.write(0)
        ledy.write(0)
        ledw.write(0)

    elif total==2:
        ledg.write(1)
        ledb.write(1)
        ledr.write(0)
        ledy.write(0)
        ledw.write(0)

    elif total==3:
        ledg.write(1)
        ledb.write(1)
        ledr.write(1)
        ledy.write(0)
        ledw.write(0)

    elif total==4:
        ledg.write(1)
        ledb.write(1)
        ledr.write(1)
        ledy.write(1)
        ledw.write(0)

    elif total==5:
        ledg.write(1)
        ledb.write(1)
        ledr.write(1)
        ledy.write(1)
        ledw.write(1)


# In[ ]:




