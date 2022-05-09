from playsound import playsound
import curses
import os
import time
import sys

# piano notes source https://github.com/fuhton/piano-mp3

#pth='/home/alan/Downloads/piano-mp3-master/piano-wav/'
pth='./piano-wav/'
note_seq = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
octaveN = '4'
octave4 = [note + octaveN + '.wav' for note in note_seq]

keyboard_rows = [
    ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
       ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'"],
         ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'],
]

note_dict = {}
note_dict.update({k: n+'5' for k, n in zip(keyboard_rows[1], note_seq)})
note_dict.update({k: n+'4' for k, n in zip(keyboard_rows[2], note_seq)})
note_dict.update({k: n+'3' for k, n in zip(keyboard_rows[3], note_seq)})

# manual
"""
note_dict1 = {
    'a': 'C4',
    's': 'Db4',
    'd': 'D4',
    'f': 'Eb4',
    'g': 'E4',
    'h': 'F4',
    'j': 'Gb4',
    'k': 'G4',
    'l': 'Ab4',
    ';': 'A4',
    "'": 'Bb4',
}
"""

min_delay = 0.25

def main(win):
    win.nodelay(True)
    key = ''
    last_key = ''
    last_time = 0
    win.clear()
    while 1:
        try:
           key = win.getkey()
           press_time = time.time()
           win.clear()
           win.addstr('%s\n' % (key))

           if key in note_dict:
               if key == last_key and press_time - last_time < min_delay:
                   pass
               else:
                   note_name = note_dict[key]
                   note_file = pth + note_name + '.wav'
                   win.addstr('%s\n%s' % (note_name, note_file))
                   playsound(note_file, False)
                   last_key, last_time = key, press_time
           else:
               win.addstr('no effect')

           if key == os.linesep:
              break

        except Exception as e:
           # No input
           pass

curses.wrapper(main)
