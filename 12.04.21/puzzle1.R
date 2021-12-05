library(stringr)
library(stringi)
library(purrr)

stacker <- function(start, length){
  apply(do.call(rbind, boards_raw[start:(start+length-1)] %>%
                  str_split("\\s+")),
        2, as.numeric)
}

draw_and_check <- function(board, number){
  replace(board, number == board, NA)
}

bingo_check <- function(m){
  m <- is.na(m)
  any(c(rowSums(m), colSums(m)) == 5)
}

draw_and_check_all <- function(boards, number){
  updated_boards <- boards %>% map(draw_and_check, number = number)
  check <- lapply(updated_boards, bingo_check)
  if (any(unlist(check))){
    winning_number <<- number
    done(updated_boards)
  }
  else{
    updated_boards
  }
}

id_winner <- function(boards){
  board_scan <- lapply(boards, bingo_check)
  boards[unlist(board_scan)]
}

calc_score <- function(final_board_vals, winning_number){
  sum(final_board_vals, na.rm = T) * winning_number
}

input <- readLines("12.04.21/input.txt")
numbers <- as.numeric(unlist(str_split(input[1], ",")))
boards_raw <- tail(input, -1) %>% stri_remove_empty() %>% trimws(which = "both")
boards <- seq(1,length(boards_raw), 5) %>% map(stacker, length = 5)
final_boards <- numbers %>% reduce(draw_and_check_all, .init = boards)
calc_score(unlist(id_winner(final_boards)), winning_number)