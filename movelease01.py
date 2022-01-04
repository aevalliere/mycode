#!/usr/bin/env python3

#Import modules
import shutil
import os

def main():
    #Force python to start in home directory
    os.chdir('/home/student/mycode/')

    #Move file or folder, and return path
    shutil.move('raynor.obj', 'ceph_storage/')

    #Prompt user for new name of Kerrigan object
    xname = input('What is the new name for kerrigan.obj ')

    #Rename kerrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()



