library(dplyr)
input <- read.table("12.02.21/input.txt", header = F, 
                    col.names = c("direction", "units"))
input %>% 
  mutate(units = ifelse(direction == "up", -units, units)) %>%
  mutate(aim = direction != "forward") %>%
  mutate(current_aim = cumsum(aim*units)) %>%
  filter(direction == "forward") %>%
  mutate(depth = current_aim*units) %>%
  summarise(final = sum(units)*sum(depth))