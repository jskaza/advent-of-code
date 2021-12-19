library(tidyverse)
library(zoo)
library(R.utils)
library(data.table)

input <- readLines("12.14.21/input.txt") %>% str_subset(".+")

template <- input[[1]] %>% str_split("") %>% unlist

df <- input[2:length(input)] %>%
  as.data.frame %>%
  rename(rule = 1) %>%
  separate(rule, c("pair", "insertion"), " -> ")

rules_lookup <- df$insertion
names(rules_lookup) <- df$pair

get_pairs <- function(template){
  pairs <- rollapply(template, width = 2, function(x){x})
  paste0(pairs[,1], pairs[,2])
}

lookup <- function(x){
  rules_lookup[[x]]
}

get_indices <- function(pairs){
  which(pairs %in% df$pair) + 1
}

inserter <- function(template){
  pairs <- get_pairs(template)
  indices <- get_indices(pairs)
  to_insert <- pairs %>% map(lookup) %>% unlist
  insert(template, indices, to_insert)
}

for(i in 1:10){
  template <- inserter(template)
}

max(table(template)) - min(table(template))