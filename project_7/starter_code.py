"""
Module docstring
Starter code for Random Walk Project
"""
import statistics as stat
from random import seed, choice
from math import hypot
from turtle import *

import sys

def set_seed(value):
    """ This function is used to set the seed for testing.
    When testing, this function needs to be called BEFORE main is called
    or any of function that uses random numbers.
    """
    seed(value)
    

def walk(walker, num_steps):
    """ Simulate one walk of length num_steps, using move generator move_generator.
    Return the final location after num_steps.
    """
    pass

def sim_walks(num_steps, num_trials, walker):
    """ Simulates num_trials walks of num_steps by a walker.
    int, int, triple -> list of (x,y) positions
    Returns a list of the final positions from each trial.
    """

def trials(walk_lengths, num_trials, walker):
    """ Given a walker, for each number of steps in walk_lengths, runs sim_walks with num_trials walks and print results.
    tuple, int, tuple -> None
    """
    pass

def plot_locations(walkers, num_steps, num_trials):
    """ Plot final locations in a turtle window.
    """
    pass

def sim_all(walkers, walk_lengths, num_trials):
   pass

if __name__ == "__main__":
    """ Program starts here.
    """
    seed(20190101)
    ##############################
    # Your main code starts here
    ##############################
   