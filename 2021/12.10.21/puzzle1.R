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
pts <- list(")" = 3,
            "]" = 57,
            "}" = 1197,
            ">" = 25137
)

select_list <- function(l, items){
  l[items %>% unlist]
}

freqs <- readLines("12.10.21/input.txt") %>%
  str_split("") %>%
  map(function(x){reduce(x, tracker, .init = stoppers_init)}) %>%
  Filter(f = is.list) %>%
  unlist %>%
  table

map(names(freqs), function(x){freqs[[x]]*pts[[x]]}) %>%
  unlist %>%
  sum