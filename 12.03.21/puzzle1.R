library(stringr)
input <- read.table("12.03.21/input.txt", 
                    header = F, colClasses = c("character"))[[1]]
m <- str_split(input, "", simplify = T) 
m2 <- matrix(as.numeric(m), ncol = ncol(m))
gamma_binary <- round(colSums(m2)/nrow(m2))
epsilon_binary <- as.numeric(!gamma_binary)
gamma_int <- strtoi(as.numeric(paste(gamma_binary, collapse = "")), base = 2)
epsilon_int <- strtoi(as.numeric(paste(epsilon_binary, collapse = "")), base = 2)
gamma_int*epsilon_int
