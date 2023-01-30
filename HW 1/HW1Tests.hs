{- Example of using the HUnit unit test framework.  See  http://hackage.haskell.org/package/HUnit for additional documentation.
To run the tests type "run" at the Haskell prompt.  -} 

module HW1Tests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW1

-- P1. list_diff tests
p1_test1 = TestCase (assertEqual "list_diff-test1" 
                                (sort [1,3,8,5])
                                (sort $ list_diff [1,3,8,5] []) )
p1_test2 = TestCase (assertEqual "list_diff-test2" 
                                 (sort ".aaddh")
                                 (sort $ list_diff "Computer science is fun." "Computer science is super hard and fun") ) 
 
-- P2. replace tests
p2_test1 = TestCase (assertEqual "replace-test1" 
                                  [10,2,10,3,4,10,5,6,1,7,8,1]
                                  (replace [1,2,1,3,4,1,5,6,1,7,8,1] 1 10 3 ) )
p2_test2 = TestCase (assertEqual "replace-test2" 
                                  [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)] 
                                  (replace [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0)] (6,0) (0,0) 2) ) 

-- P3. max_date tests                                  
p3_test1 = TestCase (assertEqual "max_date-test1" 
                                  (12,18,2001)
                                  (max_date [(12,18,2001)]) )
p3_test2 = TestCase (assertEqual "max_date-test2" 
                                  (12,18,2030)
                                  (max_date [(12,18,2030), (1,1,2020), (2,3,2019), (9,20,2001), (12,18,2001)]) )

-- P4. num_paths tests                                  
p4_test1 = TestCase (assertEqual "num_paths-test1" 
                                  1 
                                  (num_paths 3000 1) ) 
p4_test2 = TestCase (assertEqual "num_paths-test2" 
                                  6
                                  (num_paths 3 3) ) 
                                                           
-- P5. (a) and (b)
progLanguages =
     [ ("CptS121" , ["C"]),
     ("CptS122" , ["C++"]),
     ("CptS223" , ["C++"]),
     ("CptS233" , ["Java"]),
     ("CptS321" , ["C#"]),
     ("CptS322" , ["Python","JavaScript"]),
     ("CptS355" , ["Haskell", "Python", "PostScript", "Java"]),
     ("CptS360" , ["C"]),
     ("CptS370" , ["Java"]),
     ("CptS315" , ["Python"]),
     ("CptS411" , ["C", "C++"]),
     ("CptS451" , ["Python", "C#", "SQL"]),
     ("CptS475" , ["Python", "R"])
     ]
-- find_courses tests 
p5a_test1 = TestCase (assertEqual "(find_courses-test1)" 
                                  ["CptS233", "CptS355","CptS370"] 
                                  (find_courses progLanguages "Java") )
p5a_test2 = TestCase (assertEqual "(find_courses-test2)" 
                                  []
                                  (find_courses progLanguages "Science") )  

-- -- max_count tests  (one test is sufficient)
-- p5b_test1 = TestCase (assertEqual "(max_count-test1)" 
--                                     ("CptS355",4)
--                                     (max_count progLanguages) ) 


-- split_at_duplicate tests
p6_test1 = TestCase (assertEqual "(split_at_duplicate-test2)" 
                                 [[8],[8,1,3,5,8],[8,9,8],[8,3,4,5,8],[8]]  
                                 (split_at_duplicate [8,8,1,3,5,8,8,9,8,8,3,4,5,8,8]) ) 
p6_test2 = TestCase (assertEqual "(split_at_duplicate-test2)" 
                                 [[5],[5],[5],[5,6,7,5],[5],[5],[5]]  
                                 (split_at_duplicate [5,5,5,5,6,7,5,5,5,5]) ) 

-- add the test cases you created to the below list. 
tests = TestList [ TestLabel "Problem 1- test1 " p1_test1,
                   TestLabel "Problem 1- test2 " p1_test2,  
                   TestLabel "Problem 2- test1 " p2_test1,
                   TestLabel "Problem 2- test2 " p2_test2, 
                   TestLabel "Problem 3- test1 " p3_test1, 
                   TestLabel "Problem 3- test2 " p3_test2, 
                   TestLabel "Problem 4- test1 " p4_test1, 
                   TestLabel "Problem 4- test2 " p4_test2,
                   TestLabel "Problem 5a- test1 " p5a_test1, 
                   TestLabel "Problem 5a- test2 " p5a_test2,
                --    TestLabel "Problem 5b- test1 " p5b_test1,
                   TestLabel "Problem 6- test1 " p6_test1, 
                   TestLabel "Problem 6- test2 " p6_test2
                 ] 
                  
-- shortcut to run the tests
run = runTestTT  tests