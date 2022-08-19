library(tidyverse)
input <- readLines("12.11.21/input.txt") 
m <- str_split(input, "") %>% unlist %>% matrix(nrow = length(input), byrow = T)

updater <- function(m){
  m + 1
}

in_bounds <- function(m, pt){
  pt < dim(m) && pt > c(0,0)
}

flash <- function(m, i, j){
  up <- c(i-1, j)
  down <- c(i+1, j)
  left <- c(i, j-1)
  right <- c(i, j+1)
  up_left <- c(i-1, j-1)
  down_left <- c(i+1, j-1)
  up_right <- c(i-1, j+1)
  down_right <- c(i+1, j+1)
  potential_pts <- list(up,down,left,right,
                        up_left,down_left,up_right,down_right)
  map(potential_pts, in_bounds, m = m)
}