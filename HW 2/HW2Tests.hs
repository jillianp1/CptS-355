{- Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "run" at the Haskell prompt.  -} 

module HW2Tests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW2

------------------------------------------------------
-- INCLUDE YOUR TREE EXAMPLES HERE
t1 = NODE 3 (NODE 6 (NODE 9 (LEAF 12) (LEAF 15)) (LEAF 18)) (NODE 21 (LEAF 24) (LEAF 27)) 
t2 = NODE 1 (NODE 3 (NODE 4 (LEAF 3) (LEAF 6)) (LEAF 1) ) (NODE 2 (LEAF 10) (LEAF 6))

------------------------------------------------------

-- P1 - commons, commons_tail, and commons_all 
-- (a) commons tests
p1a_test1 = TestCase (assertEqual "commons test-1" 
                                   (sort [8,12,3])  
                                   (sort (commons [3,6,8,8,9,10,12,3] [4,5,8,12,3])) ) 
p1a_test2 = TestCase (assertEqual "commons test-2"
                                    (sort [1])
                                    (sort (commons [1,1,1,1,2] [3,1,1,3])) )
-- (b) commons_tail tests
p1b_test1 = TestCase (assertEqual "commons_tail test-1" 
                                    (sort [8,12,3])  
                                    (sort (commons_tail [3,6,8,8,9,10,12,3] [4,5,8,12,3])) ) 
p1b_test2 = TestCase (assertEqual "commons_tail test-2" 
                                    (sort [1])
                                    (sort (commons_tail [1,1,1,1,2] [3,1,1,3])))
-- (c) commons_all tests
p1c_test1 = TestCase (assertEqual "commons_all test-1" 
                                    []
                                    (sort (commons_all [[1,2,3],[5,2,6,7],[8,9,10,22]])))
p1c_test2 = TestCase (assertEqual "commons_all test-2" 
                                    (sort [8])
                                    (sort (commons_all [[8,9,10,8],[1,8],[22,23,8,7,6],[9,20,8,8,9,8]])))
------------------------------------------------------
{-Test input for find_languages and find_courses-}
progLanguages =
     [ ("CptS121" , ["C"]),
     ("CptS122" , ["C++"]),
     ("CptS223" , ["C++"]),
     ("CptS233" , ["Java"]),
     ("CptS321" , ["C#","Java"]),
     ("CptS322" , ["Python","JavaScript"]),
     ("CptS355" , ["Haskell", "Python", "PostScript", "Java"]),
     ("CptS360" , ["C"]),
     ("CptS370" , ["Java"]),
     ("CptS315" , ["Python"]),
     ("CptS411" , ["C", "C++"]),
     ("CptS451" , ["Python", "C#", "SQL","Java"]),
     ("CptS475" , ["Python", "R"])
     ]
-- P2  find_courses and max_count 
-- (a) find_languages tests
p2a_test1 = TestCase (assertEqual "find_languages test-1" 
                                    (["C++"])
                                    (find_languages progLanguages ["CptS122", "CptS223", "CptS411"]) )
p2a_test2 = TestCase (assertEqual "find_languages test-2" 
                                    ([])
                                    (find_languages progLanguages ["CptS475", "CptS360", "CptS315", "CptS322"]))
-- (b) find_courses tests
p2b_test1 = TestCase (assertEqual "find_courses test-1" 
                                    ([("SQL", ["CptS451"]), ("Java", ["CptS233", "CptS321", "CptS355", "CptS370", "CptS451"]), ("Python", ["CptS322", "CptS355", "CptS315", "CptS451", "CptS475"])])
                                    (find_courses progLanguages ["SQL", "Java", "Python"]))
p2b_test2 = TestCase (assertEqual "find_courses test-2" 
                                    ([("C", ["CptS121", "CptS360", "CptS411"]) , ("Ruby", []), ("SQL", ["CptS451"])])
                                    (find_courses progLanguages ["C", "Ruby", "SQL"]) )
------------------------------------------------------
-- P3  nested_max, max_maybe, and max_numbers
-- (a) nested_max tests
p3a_test1 = TestCase (assertEqual "nested_max test-1" 
                                    18
                                    (nested_max [[],[11,12,13],[4,5],[8,18,9],[1,5,6],[]]) ) 
p3a_test2 = TestCase (assertEqual "nested_max test-2" 
                                    20
                                    (nested_max [[20,20,20,20,1], [20,20], [20,20,20]]))
-- (b) max_maybe tests
p3b_test1 = TestCase (assertEqual "max_maybe test-1" 
                                    (Just 8) 
                                   (max_maybe [[(Just 1),(Just 2),(Just 3),(Just 8)],[Nothing], [(Just 6),(Just 4)],[(Just 6),(Just 8),Nothing ],[]]) )
p3b_test2 = TestCase (assertEqual "max_maybe test-2" 
                                    (Just "D")
                                    (max_maybe [[(Just "A"), (Just "B")], [Nothing, (Just "C")], [(Just "D"), Nothing, (Just "A")] ]))
-- (c) max_numbers tests
p3c_test1 = TestCase (assertEqual "max_numbers test-1" 
                                    (minBound::Int) 
                                    (max_numbers  [[]]) )
p3c_test2 = TestCase (assertEqual "max_numbers test-2" 
                                    (20)
                                    (max_numbers [[StrNumber "20",IntNumber 3,IntNumber 8],[StrNumber "4",IntNumber 6],[IntNumber 12,StrNumber "16"],[]]) )
------------------------------------------------------
-- P4  tree_scan, tree_search, merge_trees
-- (a) tree_scan tests
p4a_test1 = TestCase (assertEqual "tree_scan test-1"  
                                    [12,9,15,6,18,3,24,21,27] 
                                    (tree_scan t1) ) 
p4a_test2 = TestCase (assertEqual "tree_scan test-2" 
                                    [3,4,6,3,1,1,10,2,6] 
                                    (tree_scan t2) )
-- (b) tree_search tests
p4b_test1 = TestCase (assertEqual "tree_search test-1" 
                                    1
                                   (tree_search t1 3) ) 
p4b_test2 = TestCase (assertEqual "tree_search test-2" 
                                    4
                                   (tree_search t2 6) ) 
-- (c) merge_trees  tests
addedTree = NODE 4 (NODE 9 (NODE 13 (LEAF 15) (LEAF 21)) (LEAF 19)) (NODE 23 (LEAF 34) (LEAF 33))
p4c_test1 = TestCase (assertEqual "merge_trees test-1" 
                                   addedTree  
                                   (merge_trees t1 t2) ) 
------------------------------------------------------

-- add the test cases you created to the below list. 
tests = TestList [ 
                    TestLabel "Problem 1a - test1 " p1a_test1,
                    TestLabel "Problem 1a - test2 " p1a_test2,
                    TestLabel "Problem 1b - test1 " p1b_test1,
                    TestLabel "Problem 1b - test2 " p1b_test2,  
                    TestLabel "Problem 1c - test1 " p1c_test1,
                    TestLabel "Problem 1c - test2 " p1c_test2,
                    TestLabel "Problem 2a  - test1 " p2a_test1,
                    TestLabel "Problem 2a  - test2 " p2a_test2, 
                    TestLabel "Problem 2b  - test1 " p2b_test1,
                    TestLabel "Problem 2b  - test2 " p2b_test2,
                    TestLabel "Problem 3a - test1 " p3a_test1,
                    TestLabel "Problem 3a - test2 " p3a_test2, 
                    TestLabel "Problem 3b - test1 " p3b_test1,
                    TestLabel "Problem 3b - test2 " p3b_test2, 
                    TestLabel "Problem 3c - test1 " p3c_test1,
                    TestLabel "Problem 3c - test2 " p3c_test2,
                    TestLabel "Problem 4a - test1 " p4a_test1,
                    TestLabel "Problem 4a - test2 " p4a_test2,
                    TestLabel "Problem 4b - test1 " p4b_test1,
                    TestLabel "Problem 4b - test2 " p4b_test2,
                    TestLabel "Problem 4c - test1 " p4c_test1

                 ] 
                  
-- shortcut to run the tests
run = runTestTT  tests