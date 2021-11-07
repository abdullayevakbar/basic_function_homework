# Create function to find Pi to 4 number of decimal places.
def main():
    from math import pi 
    x=pi*10000
    x=x//1
    x=x/10000
    return x