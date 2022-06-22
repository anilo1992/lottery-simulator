# lottery-simulator
Visualizes how pointless it is to play lottery. 

## Explanation
The price for one lottery ticket is at 1,20€ + 0,35€ extra charge for processing:

```lottopreis = 1,2```

The counter is at 0 and the script runs in a loop. Every iteration corresponds to one lottery ticket:

```count = 0```

So during the loop, every iteration the counter enumerates. And the counter corresponds to the tickets we virtually bought:

```count += 1```

Then, two lists of 6 randomized numbers will be created. One is the lottery ticket and the other one are the lottery numbers. The loop will continue until ```lottotipp``` equals to ```lottozahlen```. At the end, the amount of plays and its prices for the tickets will be printed.
