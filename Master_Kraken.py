import csv
import re
import random
import datetime
from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys
import multiprocessing
import os
from multiprocessing import Pool
from multiprocessing import Process


 #Creating the tuple of all the processes
#import Kraken_Medpex.py, Kraken_Aporot.py
import subprocess


#import time

# , ,

processes = ("Kraken_CompulandCity.py", "Kraken_DriveCity.py", "Kraken_Vibuonline.py", "Kraken_Mindfactory.py", "Kraken_MindfactoryCity.py", "Kraken_Compuland.py")


def run_process(process):
    os.system('python {}'.format(process))

if __name__ == '__main__':

    pool = Pool(processes=6)
    pool.map(run_process, processes)
    pool.close()
    pool.join()


processes = ("Kraken_guenstiger_Mindfactory.py", "Kraken_guenstiger_zurrose.py")


def run_process(process):
    os.system('python {}'.format(process))

if __name__ == '__main__':

    pool = Pool(processes=2)
    pool.map(run_process, processes)
    pool.close()
    pool.join()



processes = ('Kraken_Medpex.py', 'Kraken_Aporot.py', "Kraken_Docmorris.py", "Kraken_Eurapon.py", "Kraken_Vitalsana.py","Kraken_Zurrose.py")


def run_process(process):
    os.system('python {}'.format(process))

if __name__ == '__main__':

    pool = Pool(processes=6)
    pool.map(run_process, processes)

    pool.close()
    pool.join()


processes = ( "Kraken_Bol.py", "Kraken_Buecher.py", "Kraken_Jokers.py", "Kraken_Thalia.py", "Kraken_Weltbild.py", "Kraken_guenstiger_weltbild_thalia.py")


def run_process(process):
    os.system('python {}'.format(process))

if __name__ == '__main__':

    pool = Pool(processes=12)
    pool.map(run_process, processes)

    pool.close()
    pool.join()

