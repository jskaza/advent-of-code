library(tidyverse)

input <- readLines("12.09.21/input.txt")
# square matrix
n <- max(nchar(input))

low_point_calc <- function(m, i, j, n){
  up <- ifelse(i == 1, 99, m[i-1,j])
  down <- ifelse(i == n, 99, m[i+1,j])
  left <- ifelse(j == 1, 99, m[i,j-1])
  right <- ifelse(j == n, 99, m[i,j+1])
  all(m[i,j] < c(up,down,left,right))
}

low_point_calc_vec <- Vectorize(low_point_calc, vectorize.args = c("i", "j"))

combos <- expand.grid(i = 1:n,j = 1:n)
d <- input %>% str_split("") %>% unlist %>% as.integer %>%
  matrix(ncol = max(nchar(input)), byrow = T)

low_points <- low_point_calc_vec(d,combos$i,combos$j,n) %>%
  matrix(ncol = max(nchar(input)))

sum(d[low_points] + 1)