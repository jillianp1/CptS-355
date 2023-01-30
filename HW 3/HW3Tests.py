#------------------------------------------------------
#-- INCLUDE YOUR OWN TESTS IN THIS FILE
#------------------------------------------------------
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    "Unittest setup file. Unittest framework will run this before every test."
    # this log will be for each year the different kinds of candy two different movie theateres ordered 
    # (x, y) x will be number ordered for the first theater y is number ordered for the second theater 
    def setUp(self):
        self.movie_candy_log = { 
            2018: { "KitKat":(100, 150), "Snickers":(270, 0),  "MilkDuds":(60,30),  "Crunch":(100,160), "JuniorMints":(55,35),  
                    "SwedishFish":(300, 247),  "Whoppers":(34,20), "SourPatch":(49,38), "Skittles":(19,13)}, 
            2019: {"KitKat":(59,0),  "Snickers":(120,170), "Crunch":(55, 70), "JuniorMints":(63,67), "SwedishFish":(200, 133),  
                    "Whoppers":(55, 78), "SourPatch":(41,10), "Skittles":(80, 0), "Dots":(99, 27)}, 
            2020: {"Snickers":(380, 22),  "MilkDuds":(66, 67), "Crunch":(130, 290), "JuniorMints":(28,45)}, 
            2021: { "Whoppers":(29, 88), "SwedishFish":(36, 68), "KitKat":(14,45), "SourPatch":(130, 240), "JuniorMints":(200, 155), 
                    "Skittles":(310, 400), "Snickers":(99, 100), "MilkDuds":(440, 90), "Gobbers":(66, 45),  
                    "RedVines":(200, 210), "Reeses":(20, 10)} } 
        self.newgraph = {'A':{'B', 'C'},'B':{'C'},'C':{'D'},'D':{}}

    #--- Problem 1----------------------------------

    def test_all_games(self):
        # Provide your own test here. Create your own input dictionary for this test (similar to self.wsu_games).
      output =      {'KitKat': {2018: (100, 150), 2019: (59, 0), 2021: (14, 45)},
                    'Snickers': {2018: (270, 0), 2019: (120, 170), 2020: (380, 22), 2021: (99, 100)},
                    'MilkDuds': {2018: (60, 30), 2020: (66, 67), 2021: (440, 90)},
                    'Crunch': {2018: (100, 160), 2019: (55, 70), 2020: (130, 290)},
                    'JuniorMints': {2018: (55, 35), 2019: (63, 67), 2020: (28, 45), 2021: (200, 155)},
                    'SwedishFish': {2018: (300, 247), 2019: (200, 133), 2021: (36, 68)},
                    'Whoppers': {2018: (34, 20), 2019: (55, 78), 2021: (29, 88)},
                    'SourPatch': {2018: (49, 38), 2019: (41, 10), 2021: (130, 240)},
                    'Skittles': {2018: (19, 13), 2019: (80, 0), 2021: (310, 400)},
                    'Dots': {2019: (99, 27)},
                    'Gobbers': {2021: (66, 45)},
                    'RedVines': {2021: (200, 210)},
                    'Reeses': {2021: (20, 10)}}
                
        
      self.assertDictEqual(all_games(self.movie_candy_log),output)
    
    #--- Problem 2----------------------------------
    def test_common_teams(self):
        output = {'Snickers': [(270, 0), (120, 170), (380, 22), (99, 100)],'JuniorMints': [(55, 35), (63, 67), (28, 45), (200, 155)]}
        self.assertDictEqual(common_teams(self.movie_candy_log),output)

    #--- Problem 3 ----------------------------------
    def test_get_wins(self):
        output = [(2019, (59, 0))]
        self.assertListEqual(get_wins(self.movie_candy_log,'KitKat'),output)

    #--- Problem 4----------------------------------
    def test_wins_by_year(self):
        output = [(2018, 7), (2019, 5), (2020, 1), (2021, 4)]
        self.assertListEqual(wins_by_year(self.movie_candy_log),output)

    
    #--- Problem 5 ----------------------------------
    def test_longest_path(self):
        self.assertEqual(longest_path(self.newgraph,'A'),4)


    #--- Problem 6----------------------------------
    def test_counter(self):
        pass
        # Provide your own test here. Initialize the iterator with your own input
    
if __name__ == '__main__':
    unittest.main()

