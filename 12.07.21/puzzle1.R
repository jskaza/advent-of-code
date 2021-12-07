library(purrr)

input <<- scan("12.07.21/input.txt", sep = ",")
h_max <- max(input)
h_min <- min(input)
search <- h_min:h_max
map(search, function(x){sum(abs(input - x))}) %>% unlist %>% min
