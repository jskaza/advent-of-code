library(stringr)
library(purrr)

input <- read.table("12.03.21/input.txt", 
                    header = F, colClasses = c("character"))[[1]]
m <- str_split(input, "", simplify = T)
m2 <- matrix(as.numeric(m), ncol = ncol(m))

keep_most_common <- function(m, pos, method){
  current_bit <- m[,pos]
  avg <- mean(current_bit)
  most_common <- ifelse(avg == 0.5, 1, round(avg))
  if(method == "o"){
    to_keep <- current_bit == most_common
  }
  else if(method == "c"){
    to_keep <- current_bit != most_common
  }
  m[to_keep,]
}

get_rating <- function(method){
  rating <- cbind(m2)
  for (pos in 1:ncol(rating)){
    if (is.matrix(rating)){
      rating <- keep_most_common(rating, pos, method)
    } 
    else{
      return(strtoi(as.numeric(paste(rating, collapse = "")), base = 2))
      break
    }
  }
}

prod(map_int(c("o","c"), get_rating))