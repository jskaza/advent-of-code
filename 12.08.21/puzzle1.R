library(readr)
library(dplyr)
library(tidyr)

read_delim("12.08.21/input.txt", delim = "| ", 
           col_names = c("signal", "output"), col_select = 2) %>%
  separate(col = output, into = paste0("output", rep(1:4))) %>%
  mutate_all(function(x){nchar(x) %in% c(2,4,3,7)}) %>%
  as.matrix %>% sum