library(stringr)
library(purrr)
library(dplyr)

fill_in_line <-function(x1,y1,x2,y2){
  if(x1 == x2){
    paste(x1,seq(min(y1,y2), max(y1,y2)),sep = ",")
  }
  else if(y1 == y2){
    paste(seq(min(x1,x2), max(x1,x2)), y1, sep = ",")
  }
  
}

readLines("12.05.21/input.txt") %>%
  str_split(" -> |,") %>%
  reduce(.f = rbind) %>%
  as.data.frame %>%
  setNames(c("x1","y1","x2","y2")) %>%
  filter(x1 == x2 | y1 == y2) %>%
  pmap(fill_in_line) %>%
  unlist %>%
  table %>%
  as.data.frame %>%
  setNames(c("point", "count")) %>%
  filter(count > 1) %>%
  nrow