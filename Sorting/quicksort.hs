quicksort [] = []
quicksort (x:rest) = quicksort [y | y <- rest, y <= x] ++ [x] ++ quicksort [y | y <- rest, y > x]  

