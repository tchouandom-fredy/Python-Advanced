import fxns
print("         ",fxns.add(2,5))
###Random module : for generating random values
import random
#generate floar from 0.1to 1.0
print("Random Number1 => ", random.random())
print("Random Number2 => ", random.random())
#generating random intergers in a given range
print("Randon Interger1 = ", random.randint(1, 9))
#adding a step
print("Random even Num = ", random.randrange(0,18,2))
#list shuffling
list = [1,2,3,4,5,6,7,8]
random.shuffle(list)
print("The shuffled list is", list)
#random choices
print("Randmm selection of k elements in the list gives", random.choices(list, weights = (50,40,10,30,40,20,5,1), k=5))

###Statistics module : used to find mean, median, mode, etc
import statistics
scores = [6,7,7,9,4,7,9,1,5]
print("the mean is  ",statistics.mean(scores))
print(" the median is ",statistics.median(scores))
print(" the mode is  ",statistics.mode(scores))
score2 = [10,20,30,40]
print("The actual median is ", statistics.median(score2))
print(" The low median is ", statistics.median_low(score2))
print("The high median is ", statistics.median_high(score2))
print("The mean is ", statistics.mean(score2))
print("The Variance is ", statistics.variance(score2, statistics.mean(score2)))
print("The standard deviation of the list is ", statistics.stdev(score2))
eqscore = [3,3,3,3,3]
print("The mean is ", statistics.mean(eqscore))
print("The Variance is ", statistics.variance(eqscore, statistics.mean(eqscore)))
print('\n\n')
###Python time module : to synchronise system time to program

import time
epoch_time = time.time()
print("  ",epoch_time)#No of sec since 1 Jan 1970 ( the epoch)
local_time = time.ctime(epoch_time)
print(local_time)
