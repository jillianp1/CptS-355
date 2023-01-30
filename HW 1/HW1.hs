-- CptS 355 - Spring 2022 -- Homework1 - Haskell
-- Name: Jillian Plahn 
-- Collaborators: 

module HW1
     where

-- P1 - list_diff 15%
-- takes two lists as input
-- returns list on non common elements from the two input lists

--write helper function to find differences in one list
--then call it twice for both lists and then append the lists together  

copyList [] = []
copyList (x:xs) = x:(copyList xs)

list_diff [] [] = []
list_diff list1 list2 = (diffHelper list1 list1 list2)


diffHelper  [] [] _ = []
diffHelper listCopy [] list2 = diffHelper [] list2 listCopy
diffHelper listCopy (x:xs) list2 = 
                         if (elem x list2)
                              then diffHelper listCopy xs list2
                              else x:(diffHelper listCopy xs list2)




-- P2  replace  15%
--takes a list, value 1, replacement value 2, number n 
-- replaces v1 with v2 n amount of times

replace [] v1 v2 n = []
replace (x:xs) v1 v2 0 = (x:xs)
replace (x:xs) v1 v2 n =
                         if (x == v1) 
                              then v2:(replace xs v1 v2 (n-1))
                              else x:(replace xs v1 v2 n)

-- P3  max_date 10%
-- hint to write a helper function that returns the max of two given date tuples

max_date [x] = x
max_date (x:xs)
               |maxHelper x max = x
               |otherwise = max
               where max = max_date xs

maxHelper (a1, b1, c1) (a2, b2, c2) = (c1 > c2) || ((c1 ==c2) && (a1 > a2)) || ((c1 == c2) && (a1 == a2) && (b1 > b2))

-- P4  num_paths  10%
-- takes grid length and width (m,n)

num_paths m n 
          |n == 1 || m == 1 = 1
          |otherwise = (num_paths (m-1) n) + (num_paths m (n-1))


-- P5  (a) find_courses 10%
-- takes a list of courses and returns list of courses

find_courses [] value = []
find_courses ((x,y):xs) value =
                              if (elem value y) 
                                   then  x:(find_courses xs value)
                                   else find_courses xs value
                                           

-- P5  (b) max_count  15%
-- takes list as input
-- returns course name and max number two tuple

-- max_count [] = []
-- max_count ((x,y):xs) = maxCountHelper list value

-- current value holds class and max 
-- current is (class, max) when you write comparisons 
--list is ((c,y):xs)
-- maxCountHelper ((x,y):xs) value = 
--                               if (length y == 1)
--                                    then maxCountHelper xs value
--                               else if (length y > 1)
--                                    then 
                         


-- P6  split_at_duplicate 15% 

split_at_duplicate  [] = []
split_at_duplicate (x:xs) = splitHelper xs [x] x
     where 
          splitHelper [] buf prev = (reverse buf) : []
          splitHelper (x:xs) buf prev | (x == prev) =  (reverse buf) : (splitHelper xs (x:[]) prev)
                                   |otherwise = splitHelper xs (x:buf) x
             


               
                   









