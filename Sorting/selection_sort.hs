selsort [] = []
selsort list = [y | y <- list, y == (minimum list)] ++ selsort ([y | y <- list, y /= (minimum list)])