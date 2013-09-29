#!/usr/bin/env python
# Simulation of Monty Hall problem
# Note that these results are obvious, but the question demands we simulate...
import random


NUM_SIMS = 10000000

no_swap_wins = 0
no_swap_losses = 0
swap_wins = 0
swap_losses = 0

# Run simulation of not swapping
for i in range(0, NUM_SIMS):
    doors = ["goat", "goat", "car"]
    if random.choice(doors) == "car":
        no_swap_wins += 1
    else:
        no_swap_losses += 1

# Run simulation of swapping
for i in range(0, NUM_SIMS):
    doors = ["goat", "goat", "car"]
    # Many simplifications I'm ignoring here for the sake of verbosity
    # Make your pick
    you_picked = random.choice(doors)
    doors.remove(you_picked)

    # Host removes a goat
    doors.remove("goat")

    if doors[0] == "car":
        swap_wins += 1
    else:
        swap_losses += 1


no_swap_rate = float(no_swap_wins) / NUM_SIMS
swap_rate = float(swap_wins) / NUM_SIMS

print "No-swap wins: {}, losses: {}, rate: {}".format(no_swap_wins,
                                                      no_swap_losses,
                                                      no_swap_rate)
print "Swap wins/losses: {}/{}, rate: {}".format(swap_wins,
                                                 swap_losses,
                                                 swap_rate)
