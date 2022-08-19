library(purrr)

input <- scan("12.07.21/input.txt", sep = ",")
h_max <- max(input)
h_min <- min(input)
search <- h_min:h_max
cost_function <- function(p1, p2){
  map(p2, function(x){abs(sum(0:(x-p1)))}) %>% unlist %>% sum
}

map(search, cost_function, p2 = input) %>% unlist %>% min

