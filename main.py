import pygame

import display
from metro import Metro

def main():
    metro = Metro()
    metro.generate_random_metro()
    display.display(metro)

if __name__ == '__main__':
    main()