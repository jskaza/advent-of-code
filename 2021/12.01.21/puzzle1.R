library(dplyr)
input <- read.table("12.01.21/input.txt", header = F)[[1]]
sum(input > lag(input), na.rm = T)