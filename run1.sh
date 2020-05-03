#1.py
import time
import progressbar
from time import sleep
bar = progressbar.ProgressBar(maxval=10, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(10):
    bar.update(i+1)
    sleep(1)
bar.finish()
