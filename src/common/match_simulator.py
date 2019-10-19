import random

MAX_ROUNDS = 16


class MatchSimulator():

    @staticmethod
    def simulate_match(team1, team2):
        teams = [team1, team2]

        team1_score = 0
        team2_score = 0
        match_finished = False

        while(not match_finished):
            round_winner = random.choice(teams)

            if (round_winner == team1):
                team1_score += 1

            if (round_winner == team2):
                team2_score += 1

            if (MAX_ROUNDS in [team1_score, team2_score]):
                match_finished = True

            if (team1_score == team2_score == 15):
                team1_score = 18
                match_finished = True

        return {
            'team1': team1_score,
            'team2': team2_score
        }
