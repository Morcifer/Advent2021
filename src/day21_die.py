# Train
player_1 = 4
player_2 = 8

# Test
player_1 = 7
player_2 = 2


def get_final_score_deterministic() -> int:
    player_1_position = player_1
    player_2_position = player_2

    player_1_score = 0
    player_2_score = 0

    die_roll = 1

    total_rolled_dice = 0
    turn = 0

    player_1_turn = True

    while player_1_score < 1000 and player_2_score < 1000:
        player_position = player_1_position if player_1_turn else player_2_position
        for i in range(3):
            # Increment position
            player_position += die_roll
            player_position = player_position % 10
            if player_position == 0:
                player_position = 10

            # Increment die roll
            die_roll += 1
            if die_roll == 101:
                die_roll = 1
            total_rolled_dice += 1

        turn += 1

        # Set position and new score
        if player_1_turn:
            player_1_position = player_position
            player_1_score += player_position
        else:
            player_2_position = player_position
            player_2_score += player_position

        # print(f"At the end of turn {turn}, "
        #       f"player {'1' if player_1_turn else '2'} "
        #       f"is at {player_position} and has "
        #       f"{player_1_score if player_1_turn else player_2_score}")

        player_1_turn = not player_1_turn

    return min(player_1_score, player_2_score) * total_rolled_dice


all_3_rolls = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


global played_games


def get_final_score_dirac() -> int:
    global played_games
    played_games = 0

    player_1_wins, player_2_wins = simulate_single_turn(player_1, player_2, 0, 0)
    return max(player_1_wins, player_2_wins)


def simulate_single_turn(position_1: int, position_2: int, score_1: int, score_2: int) -> (int, int):
    global played_games

    player_1_wins = 0
    player_2_wins = 0

    for sum_1, games_1 in all_3_rolls.items():
        game_position_1 = get_new_position(position_1, sum_1)
        game_score_1 = score_1 + game_position_1
        # print(f"Player 1 rolled {sum_1} in {games_1} games for score of {game_score_1}")
        if game_score_1 >= 21:
            played_games += games_1
            player_1_wins += games_1
            continue

        for sum_2, games_2 in all_3_rolls.items():
            played_games += games_1 * games_2

            game_position_2 = get_new_position(position_2, sum_2)
            game_score_2 = score_2 + game_position_2
            # print(f"Player 2 rolled {sum_2} in {games_2} games for score of {game_score_2}")
            if game_score_2 >= 21:
                player_2_wins += games_1 * games_2
                continue

            result = simulate_single_turn(game_position_1, game_position_2, game_score_1, game_score_2)

            player_1_wins += games_1 * games_2 * result[0]
            player_2_wins += games_1 * games_2 * result[1]

    if played_games % 1000000 == 0:
        print(f"Played {int(played_games/1000000)} million games total (about 800000000 expected)")

    return player_1_wins, player_2_wins


def get_new_position(old_position: int, sum_of_rolls: int) -> int:
    position = old_position + sum_of_rolls
    position = position % 10
    return position if position != 0 else 10
