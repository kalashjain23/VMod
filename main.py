from s_t_t import *
from textmod import *


link = input("Enter the link to your audio file: ")
ex_text = text(link)

if ex_text == 'error':
    print("There was an error reading the audio file.. Please try again!")

else:
    profan_list = textmod(ex_text)
    if len(profan_list) == 0:
        print("The audio is clean!!\n")
        print(ex_text)

    else:
        print(f'''This audio contains some word that are {profan_list}''')
