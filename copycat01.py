#!/usr/bin/env python3

#Import additional code
import shutil
import os

def main():
    #Import into the working directory
    os.chdir("/home/student/mycode/")

    #Copy from A - B
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #Copy entire directory from A to B
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()


