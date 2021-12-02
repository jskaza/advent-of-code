library(dplyr)
input <- read.table("12.02.21/input.txt", header = F, 
                    col.names = c("direction", "units"))
input %>% 
  mutate(direction2 = ifelse(direction == "forward", "horizontal", "vertical")) %>%
  mutate(units = ifelse(direction == "up", -units, units)) %>% 
  group_by(direction2) %>% summarise(total = sum(units)) %>%
  summarise(final = prod(total))