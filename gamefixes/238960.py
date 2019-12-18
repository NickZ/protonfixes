""" Game fix for Path of Exile
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Enable Async and add preload options
    """
    # Enable preload options
    util.append_argument('--waitforpreload --nologo --gc2')

