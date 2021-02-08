import random


class Scoreboard(object):
    def __init__(self):
        self.score_list = []
        self.team1_score = 0
        self.updated_team1_score = 0
        self.team2_score = 0
        self.updated_team2_score = 0
        self.team3_score = 0
        self.updated_team3_score = 0
        self.A = 5
        self.B = 4
        self.C = 3
        self.D = 2
        self.E = 1
        self.F = 0
        self.country1 = "India"
        self.country2 = "Australia"
        self.country3 = "England"
        self.country1_player1 = 0
        self.country1_player2 = 0
        self.country2_player1 = 0
        self.country2_player2 = 0
        self.country3_player1 = 0
        self.country3_player2 = 0
        self.player1 = "Raja"
        self.player2 = "Ram"
        self.player3 = "Raj"
        self.player4 = "Akash"
        self.player5 = "Sanjay"
        self.player6 = "Amar"

    def start_play(self, round=1):
        incremented_value = round - 1
        A = self.A + incremented_value
        B = self.B + incremented_value
        C = self.C + incremented_value
        D = self.D + incremented_value
        E = self.E + incremented_value
        F = 0
        all_score = []

        for i in range(6):
            result = random.choice(['A', 'B', 'C', 'D', 'E', 'F'])
            all_score.append(result)
        score_dict = {'A': A, 'B': B, "C": C, "D": D, "E": E, "F": F}

        self.score_list = all_score
        print(f'round {round} \n players scored{all_score}\n')

        if score_dict.get(all_score[0]) == score_dict.get(all_score[1]):
            self.team1_score = score_dict.get(all_score[0]) + score_dict.get(all_score[1]) + 2
            print(f"""
{self.country1} scores {self.team1_score}   
{self.player1} scores {score_dict.get(all_score[0])}
{self.player2} scores {score_dict.get(all_score[1])}
with 2 bonus points
                  """)

        else:
            self.team1_score = score_dict.get(all_score[0]) + score_dict.get(all_score[1])
            print(f"""
{self.country1} scores {self.team1_score}
{self.player1} scores {score_dict.get(all_score[0])}
{self.player2} scores {score_dict.get(all_score[1])}
                  """)

        self.country1_player1 = self.country1_player1 + score_dict.get(all_score[0])
        self.country1_player2 = self.country1_player2 + score_dict.get(all_score[1])
        print(f"""{self.player1} updated scores {self.country1_player1}
{self.player2} updated scores {self.country1_player2}
{'-'*100}
""")

        if score_dict.get(all_score[2]) == score_dict.get(all_score[3]):
            self.team2_score = score_dict.get(all_score[2]) + score_dict.get(all_score[3]) + 2
            print(f""" 
{self.country2} scores {self.team2_score}
{self.player3} scores {score_dict.get(all_score[2])}
{self.player4} scores {score_dict.get(all_score[3])}
{'-'*10}
                    with 2 bonus points
                    """)

        else:
            self.team2_score = score_dict.get(all_score[2]) + score_dict.get(all_score[3])
            print(f"""
{self.country2} scores {self.team2_score}
{self.player3} scores {score_dict.get(all_score[2])}
{self.player4} scores {score_dict.get(all_score[3])}

                  """)

        self.country2_player1 = self.country2_player1 + score_dict.get(all_score[2])
        self.country2_player2 = self.country2_player2 + score_dict.get(all_score[3])

        print(f"""{self.player3} updated scores {self.country2_player1}
{self.player4} updated scores {self.country2_player2}
{'-'*100}
""")

        if score_dict.get(all_score[4]) == score_dict.get(all_score[5]):
            self.team3_score = score_dict.get(all_score[4]) + score_dict.get(all_score[5]) + 2

            print(f"""
{self.country3} scores {self.team3_score}
{self.player5} scores {score_dict.get(all_score[4])}
{self.player6} scores {score_dict.get(all_score[5])}
{'-'*100}

with 2 bonus points
                    """)

        else:
            self.team3_score = score_dict.get(all_score[4]) + score_dict.get(all_score[5])

            print(f"""
{self.country3} scores {self.team3_score}
{self.player5} scores {score_dict.get(all_score[4])}
{self.player6} scores {score_dict.get(all_score[5])}
                  """)

        self.country3_player1 = self.country3_player1 + score_dict.get(all_score[4])
        self.country3_player2 = self.country3_player2 + score_dict.get(all_score[5])

        print(f"""{self.player5} updated scores {self.country3_player1}
{self.player6} updated scores {self.country3_player2}
{'-'*100}
""")

        self.updated_team1_score = self.updated_team1_score + self.team1_score
        self.updated_team2_score = self.updated_team2_score + self.team2_score
        self.updated_team3_score = self.updated_team3_score + self.team3_score
        print(f"""after round {round} updated scores
                {self.country1} updated scores {self.updated_team1_score}
                    
                {self.country2} updated scores {self.updated_team2_score}
                
                {self.country3} updated scores{self.updated_team3_score}
{'-'*100}

                """)

        if self.updated_team1_score > 60 or self.updated_team2_score > 60 or self.updated_team3_score > 60:
            mydict = {self.country1: self.updated_team1_score, self.country2: self.updated_team2_score,
                      self.country3: self.updated_team3_score}
            print(max(mydict, key=mydict.get), "wins")

            exit()

        else:
            round = round + 1
            self.start_play(round)


obj = Scoreboard()
obj.start_play()