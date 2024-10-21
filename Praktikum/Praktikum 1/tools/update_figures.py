#!/usr/bin/python3
from sys import argv
from os import system 

if len(argv)<2: 
    print("usage:\npython3 update_figures.py NAME")
else:
    system("pdftoppm {fig}.pdf {fig} -png -cropbox".format(fig=argv[1]))
    system("mv {fig}-1.png {fig}.png".format(fig=argv[1]))
    system("rm {fig}.pdf".format(fig=argv[1]))

