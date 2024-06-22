import pandas as pd
df = pd.read_csv('/Users/liupaychern/Documents/pe8_data.csv')

def read_nba_standings(file_name):
    eastern_home_lt_away = []
    eastern_pf_pa_diff = 0
    eastern_count = 0
    western_pf_pa_diff = 0
    western_count = 0
    interconference_wins = {}

    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row

        for row in reader:
            # 確保該行有足夠的欄位
            if len(row) < 10:
                continue

            conference = row[0]
            team = row[1]
            try:
                win_loss_pct = float(row[3])
                home_record = row[7]
                away_record = row[8]
                points_for = float(row[5])
                points_against = float(row[6])
                interconference_record = row[9]  # 假設該欄位存在並包含勝-負紀錄
            except ValueError:
                # 忽略無法解析的行
                continue

            # 東區哪些球隊的主場勝率低於客場勝率
            if conference == 'Eastern' and calculate_win_rate(home_record) < calculate_win_rate(away_record):
                eastern_home_lt_away.append(team)

            # 計算東區和西區球隊的平均得分減掉失分
            pf_pa_diff = points_for - points_against
            if conference == 'Eastern':
                eastern_pf_pa_diff += pf_pa_diff
                eastern_count += 1
            elif conference == 'Western':
                western_pf_pa_diff += pf_pa_diff
                western_count += 1

            # 根據每支球隊和另一區球隊的對戰紀錄來對所有球隊排序
            wins, losses = map(int, interconference_record.split('-'))
            interconference_wins[team] = wins / (wins + losses)

    eastern_avg_pf_pa_diff = eastern_pf_pa_diff / eastern_count if eastern_count else 0
    western_avg_pf_pa_diff = western_pf_pa_diff / western_count if western_count else 0
    higher_avg_pf_pa_diff_conference = 'Eastern' if eastern_avg_pf_pa_diff > western_avg_pf_pa_diff else 'Western'

    sorted_teams_by_interconference_win = sorted(interconference_wins.keys(), key=lambda x: interconference_wins[x], reverse=True)

    return eastern_home_lt_away, higher_avg_pf_pa_diff_conference, sorted_teams_by_interconference_win


# 計算勝率 (檔案中的 W-L 欄位)
def calculate_win_rate(record):
    wins, losses = map(int, record.split('-'))
    total_games = wins + losses
    return wins / total_games

# 輸出
file_name = 'pe8_data.csv'
eastern_home_lt_away, higher_avg_pf_pa_diff_conference, sorted_teams_by_interconference_win = read_nba_standings(file_name)


print("(1) 東區哪些球隊的主場勝率低於客場勝率:")
for team in eastern_home_lt_away:
    print(team)

print("\n(2) 哪一區的球隊擁有較高的平均得分減掉失分:")
print(higher_avg_pf_pa_diff_conference)

print("\n(3) 根據每支球隊和另一區球隊的對戰紀錄來對所有球隊排序:")
for team in sorted_teams_by_interconference_win:
    print(team)