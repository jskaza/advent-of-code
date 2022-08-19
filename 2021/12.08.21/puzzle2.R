library(tidyverse)

str_arrange <- function(x){
  x %>%
    str_split("") %>%
    map(~sort(.) %>% paste(collapse = "")) %>%
    as_vector
}

grepl_vec <- Vectorize(grepl, vectorize.args = "pattern")

digits_map <- list("abcefg" = 0,
                   "cf" = 1,
                   "acdeg" = 2,
                   "acdfg" = 3,
                   "bcdf" = 4,
                   "abdfg" = 5,
                   "abdefg" = 6,
                   "acf" = 7,
                   "abcdefg" = 8,
                   "abcdfg" = 9
)

mapper <- function(s, key){
  segments <- sort(names(key[grepl_vec(key, s)])) %>% reduce(paste0)
  digits_map[segments]
}

decoder <- function(s){
  s <- str_split(s, " ") %>% unlist %>% str_arrange
  v <- s[1:10]
  o <- s[12:15]
  
  # some sloppy deductive reasoning
  lens <- nchar(v)
  freqs <- v %>% reduce(paste0) %>% str_split("") %>% unlist %>%
    table %>% sort %>% names
  one <- v[nchar(v) == 2] %>% str_split("") %>% unlist
  givens <- v[nchar(v) %in% c(2,4,3,7)] %>% str_split("") %>% unlist
  givens_freqs <- givens %>% table
  len_6 <- v[nchar(v) == 6]  %>% str_split("") %>% unlist
  a <- setdiff(strsplit(v[lens == 3],"")[[1]],
               strsplit(v[lens == 2],"")[[1]])
  b <- freqs[2]
  c <- len_6 %>% table %>% sort %>% names %>% head(3) %>% 
    intersect(one)
  e <- freqs[1]
  f <- freqs[7]
  remaining <- setdiff(letters[1:7], c(a,b,c,e,f))
  d <- givens_freqs[givens_freqs == 2] %>% names %>% intersect(remaining)
  g <- setdiff(letters[1:7], c(a,b,c,d,e,f))
  
  key <- list("a"=a,"b"=b,"c"=c,"d"=d,"e"=e,"f"=f,"g"=g) 
  map(o, mapper, key = key) %>% reduce(paste0) %>% as.integer
}

readLines("12.08.21/input.txt") %>% map(decoder) %>% unlist %>% sum