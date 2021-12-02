library(zoo)
input <- read.table("12.01.21/input.txt", header = F)[[1]]
rollsum <- rollsum(input, 3)
print(sum(rollsum > lag(rollsum), na.rm = T))