library(dplyr)
library(purrr)

input <- scan("12.06.21/input.txt", sep = ",")

seq_vec <- Vectorize(seq.default, vectorize.args = c("from"))

gen_descendants <- function(p, n){
    seq_vec(from = (p+1), to = n, by = 7)
}

transition_vec <- function(v){
  newborns <- v[9] + v [16]
  new_cycle <- v[16]
  v <- c(newborns, head(v, 15))
  v[10] <- v[10] + new_cycle
  return(v)
}

simulation <- function(v, n){
  if (n == 0){
    sum(v)
  }
  else{
    simulation(transition_vec(v), n-1)
  }
}

simulation_vec <- Vectorize(simulation, vectorize.args = "n")

n <- 256
map(gen_descendants(input, n), function(x){256-x}) %>% map(simulation_vec, v = init_vec) %>%
  unlist %>% sum + length(input)