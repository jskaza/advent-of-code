library(tidyverse)

tracker <- function(stoppers, token){
  char_map <- list("(" = ")",
                   "[" = "]",
                   "{" = "}",
                   "<" = ">"
  )
  if (token %in% names(char_map)){
    return(c(stoppers, char_map[[token]]))
  }
  else if(length(stoppers) == 0){
    return(done(list("error" = token)))
  }
  else if (tail(stoppers, 1) != token){
    return(done(list("error" = token)))
  }
  else{
    return(head(stoppers, length(stoppers) - 1))
  }
}

stoppers_init <- c()
pts <- list(")" = 1,
            "]" = 2,
            "}" = 3,
            ">" = 4
)
score_updater <- function(score, x){
  5*score + pts[[x]]
}

select_list <- function(l, items){
  l[items %>% unlist]
}

readLines("12.10.21/input.txt") %>%
  str_split("") %>%
  map(function(x){reduce(x, tracker, .init = stoppers_init)}) %>%
  Filter(f = function(x){!is.list(x)}) %>%
  map(rev) %>%
  map(function(x){reduce(x, score_updater, .init = 0)}) %>%
  unlist %>%
  median