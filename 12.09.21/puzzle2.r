library(tidyverse)

low_point_finder <- function(mat, i, j){
  up <- ifelse(i == 1, 99, mat[i-1,j])
  down <- ifelse(i == nrow(mat), 99, mat[i+1,j])
  left <- ifelse(j == 1, 99, mat[i,j-1])
  right <- ifelse(j == ncol(mat), 99, mat[i,j+1])
  all(mat[i,j] < c(up,down,left,right))
}

low_point_finder_vec <- Vectorize(low_point_finder, vectorize.args = c("i", "j"))

gen_coords <- function(mat, i, j, direction){
  if (direction == "up" & i != 1){
    data.frame(i_new = i-1, j_new = j)
  }
  else if (direction == "down" & i != nrow(mat)){
    data.frame(i_new = i+1, j_new = j)
  }
  else if (direction == "left" & j != 1){
    data.frame(i_new = i, j_new = j-1)
  }
  else if (direction == "right" & j != ncol(mat)){
    data.frame(i_new = i, j_new = j+1)
  }
  else{
    data.frame(i_new = NA_integer_, j_new = NA_integer_)
  }
}

get_val <- function(mat, i, j){
  mat[i,j]
}

basin_size <- function(mat, d){
  result <<- rbind(result, d)
  if (nrow(d) == 0){
    result_size <- result %>% distinct %>% nrow
    result <<- tibble(i = integer(), j = integer())
    return(result_size)
  }
  else{
    d <- 1:4 %>%
      map_dfr(function(x) d) %>%
      mutate(val = map2(i, j, get_val, mat = mat)) %>%
      unnest(val) %>%
      arrange(i,j) %>%
      mutate(direction = rep(c("up", "down", "left", "right"), nrow(.)/4)) %>%
      mutate(result = pmap(list(i, j, direction), gen_coords, mat = mat)) %>%
      unnest(result) %>%
      drop_na(i_new) %>%
      mutate(val_new = map2(i_new, j_new, get_val, mat = mat)) %>%
      unnest(val_new) %>%
      filter(val_new > val) %>%
      select(i_new,j_new) %>%
      rename(i = i_new, j = j_new)
    basin_size(mat, d)
  }
}

input <- readLines("12.09.21/input.txt")

mat <- input %>%
  str_split("") %>%
  unlist %>%
  as.integer %>%
  matrix(ncol = max(nchar(input)), byrow = T)

combos <- expand.grid(i = 1:nrow(mat),j = 1:ncol(mat))
low_points <- low_point_finder_vec(mat, combos$i, combos$j) %>%
 matrix(ncol = max(nchar(input)))

mat[mat == 9] <- NA_integer_

indices <- which(low_points, arr.ind = T)

result <<- tibble(i = integer(), j = integer())
split(indices, row(indices)) %>%
  map(function(x){tibble(i = x[1], j = x[2])}) %>%
  map(basin_size, mat = mat) %>%
  unlist() %>%
  sort() %>%
  tail(3) %>%
  reduce(`*`)
