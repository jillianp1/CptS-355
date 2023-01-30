-- CptS 355 - Spring 2022 -- Homework2 - Haskell
-- Name: Jillian Plahn
-- Collaborators: 

module HW2
     where

-- P1 - commons, commons_tail, and commons_all 
-- (a) commons – 5%
commons [] [] = []
commons list1 list2 = commonHelper list1 list2

commonHelper [] [] = []
commonHelper [] list2 = []
commonHelper list1 [] = []
commonHelper (x:xs) list2 = 
                         if (elem x list2)
                              then eliminateDuplicates(x:(commonHelper xs list2))
                              else commonHelper xs list2

eliminateDuplicates [] = []
eliminateDuplicates (x:xs) | (elem x xs) = eliminateDuplicates xs
                         | otherwise = x:(eliminateDuplicates xs)



-- (b) commons_tail –  9%
commons_tail list1 list2 = commons2Helper list1 list2 []
                         where 
                               commons2Helper [] list2 acc = acc
                               commons2Helper (x:xs) list2 acc = 
                                                                 if (elem x list2) && not(elem x acc)
                                                                      then commons2Helper xs list2 (x:acc)
                                                                      else commons2Helper xs list2 acc 

-- (c) commons_all –  3%
commons_all [] = []
commons_all (x:xs) = foldl commons x xs

------------------------------------------------------
-- P2  find_courses and max_count 
-- (a) find_languages – 10%
find_languages xs list = commons_all (map snd (filter (\(x,y) -> elem x list) xs ))

-- (b) find_courses – 12%
find_courses courses list = map (find_courses_helper courses) list 
                         where 
                              find_courses_helper courses language = 
                                   (language, map fst (filter (\(x,y) -> elem language y) courses))

------------------------------------------------------
-- P3  nested_max, max_maybe, and max_numbers
-- (a) nested_max - 2%
nested_max list = maxHelp (map maxHelp list)
               where 
                    maxHelp xs = foldr v (minBound::Int) xs
                    v x y = if x < y then y else x

-- (b) max_maybe - 8%

max_maybe list = maxHelp2 (map maxHelp2 list )
               where 
                    maxHelp2 xs = foldr v Nothing xs
                         where
                              v Nothing Nothing = Nothing
                              v Nothing (Just y) = (Just y)
                              v (Just y) Nothing = (Just y)
                              v (Just y1) (Just y2) = (Just (max y1 y2))

-- (c) max_numbers - 8%
data Numbers = StrNumber String | IntNumber Int
 deriving (Show, Read, Eq)
getInt x = read x::Int

max_numbers xs = foldr max (minBound::Int) (map maxNumHelper xs)
               where
                    maxNumHelper xs = foldr convert (minBound::Int) xs
                         where
                              convert (StrNumber x) y = max (getInt x) y
                              convert (IntNumber x) y = max x y


------------------------------------------------------
data Tree a = LEAF a | NODE a (Tree a) (Tree a)
 deriving (Show, Read, Eq)

-- P4  tree_scan, tree_search, merge_trees
-- (a) tree_scan 5%
tree_scan (LEAF a) = [a]
tree_scan (NODE a t1 t2) = (tree_scan t1) ++ [a] ++ (tree_scan t2)


-- (b) tree_search 12%
tree_search :: (Ord p, Num p, Eq a) => Tree a -> a -> p
tree_search (NODE a t1 t2) v = tree_search_helper (NODE a t1 t2) v 1
                              where
                                   tree_search_helper (NODE a t1 t2) v h | not(tree_search_helper t1 v h+1 == -1) = tree_search_helper t1 v h+1
                                                                         | (a == v) = h 
                                                                         | otherwise = tree_search_helper t2 v h+1
                                   tree_search_helper (LEAF a) v h | (a == v) = h
                                                                   | otherwise = -1 


-- (c) merge_trees  14%
merge_trees (LEAF a) (LEAF b) = LEAF (a+b)
merge_trees (LEAF a) (NODE x t1 t2) = (NODE (a+x) t1 t2)
merge_trees (NODE x t1 t2) (LEAF a) = (NODE (a+x) t1 t2)
merge_trees (NODE x t1 t2) (NODE v tree1 tree2) = NODE y tr1 tr2
                                             where
                                                  y = x+v
                                                  tr1 = merge_trees t1 tree1
                                                  tr2 = merge_trees t2 tree2