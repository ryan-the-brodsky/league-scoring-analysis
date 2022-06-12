passing_2019 = pd.read_csv('./2019-qb-stats.csv')
passing_2019['Player'] = passing_2019['Player'].apply(lambda x : x.split('\\')[0])
passing_2019.drop(['Tm', 'Rk', 'G', 'GS', 'Age', 'QBrec','Att', 'Y/G', 'Rate', 'QBR', 'Sk', 'Sk%', 'NY/A', 'ANY/A', '4QC', 'GWD', 'Y/C', 'AY/A', 'Y/A', 'Lng', 'Yds.1', 'Int%', 'TD%', 'Cmp%'], axis='columns', inplace=True)
passing_2019.rename(columns={
    "Yds":"pass_yards",
    "Int":"thrown_ints",
    "Rec":"receptions",
    "FL":"fumbles_lost",
    "1D": "pass_first_downs", 
    "TD":"pass_touchdowns", 
    "Cmp":"pass_completions"
}, inplace=True)

rushing_2019 = pd.read_csv('./2019-rushing-stats.csv')
rushing_2019['Player'] = rushing_2019['Player'].apply(lambda x : x.split('\\')[0])
rushing_2019.drop(['Rk', 'Age', 'Y/A', 'Y/G', 'Att', 'Lng', "G", "GS", "Tm"], axis='columns', inplace=True)
rushing_2019.rename(columns={
    'Yds': 'rushing_yards',
    '1D': 'rushing_first_downs',
    'TD': 'rushing_tds',
    'Fmb':'fumbles_lost_rushing'
}, inplace=True)

receiving_2019 = pd.read_csv('./2019-receiving-stats.csv')
receiving_2019['Player'] = receiving_2019['Player'].apply(lambda x : x.split('\\')[0])
receiving_2019.drop(['Rk', 'Age', 'Y/R', 'R/G', 'Y/G' ,'Y/Tgt', 'Ctch%', 'Lng', 'Tm'], axis='columns', inplace=True)
receiving_2019.rename(columns={
    "Yds": "receiving_yards",
    "Rec": "receptions",
    "TD": "receiving_tds",
    "Fmb": "fumbles_lost_receiving",
    "1D": "receiving_first_downs"
    
}, inplace=True)
receiving_2019.head()


offensive_players_2019 = pd.merge(rushing_2019, passing_2019, how="outer", on='Player')
offensive_players_2019['position'] = offensive_players_2019.apply(lambda x : x['Pos'] if 'Pos' in x else x['Pos_x'], axis=1)
offensive_players_2019['position'] = offensive_players_2019['position'].apply(lambda x : str(x).upper())
offensive_players_2019 = pd.merge(offensive_players_2019, receiving_2019, how="outer", on="Player")
offensive_players_2019['position'] = offensive_players_2019.apply(lambda x : x['Pos'] if 'Pos' in x else x['Pos_y'], axis=1)
offensive_players_2019.drop(['Pos', 'Pos_x', 'Pos_y'], axis='columns', inplace=True)
offensive_players_2019.fillna(0, inplace=True)

# offensive_players.columns.tolist()
offensive_players_2019.sort_values(by="rushing_yards", ascending=False )

offensive_players_2019.head()