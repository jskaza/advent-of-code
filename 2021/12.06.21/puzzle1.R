input <- scan("12.06.21/input.txt", sep = ",")
update_vector <- function(v, n){
  if(n == 0){
    return(v)
  }
  else{
    v <- c(replace(v, v==0, 7) - 1, rep(8, sum(v == 0)))
    return(update_vector(v, n-1))
  }
}

length(update_vector(input, 80))


