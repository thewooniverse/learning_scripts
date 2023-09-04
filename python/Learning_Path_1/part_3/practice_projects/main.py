import pandas as pd
import os
import pyperclip
import datetime

"""
Assumptions:
- Query already does the majority of column / row filtering ahead of time so that it is not neede in the script itself
-- Also, such that the load on downloading files from AWS / Athena is lower.


"""
# read the dataframes (later needs to be refactored to handle a directory full of files)
df_path = f"{os.getcwd()}{os.path.sep}normal_player_sample.csv"
df = pd.read_csv('normal_player_sample.csv')




columns = ['time', 'type', 'username', 'userid', 'deviceid', 'istransaction',
          'gameid', 'gametype', 'level', 'isbot', 'reason', 'result', 'endstatus', 'opponentusername',
          'prevbalance','newbalance', 'prevescrow', 'newescrow', 'balancechange', 'escrowchange',
          'originalprizetype', 'awardedprizetype', 'awardedprizeamount',
          'usedpowerup',
          'iserror', 'percentage', 'cashamount', 'charityamount', 'count']
# select the relevant columns for cashouts in order / organization
df = df[columns]

str_parsed_columns = ', '.join(columns)
print(str_parsed_columns)



# exclud the rows that are not of interest to me;
excluded_events = ['ClientEvent', 'MakeMove','FindMatch', 'GoalProgress', 'EditUser', 'RankUp', 'SessionStart', 
                   'CashOutStart', 'CashOutMismatch', 'CancelChallenge', 'CancelMatch']
df = df[~df['type'].isin(excluded_events)]

# convert the time column to datetime and set it as index of the dataframe
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)


# get the cashout timestamps and isolate the dataframe into events from previous cashout (or start) to current cashout;
cashouts = df.loc[(df['type'].str.contains('CashOutFinish'))
              &
             (~df['iserror'])]

# handle the duplicates if there are more CashoutFinish
if (len(cashouts)-1) != cashouts['count'][0]:
    cashouts.drop_duplicates(subset=['count'], inplace=True)
    # this needs to be tested as there were some errors in the past caused by faulty cashoutfinish events

ts1 = cashouts.index[0] # current cashout
ts2 = pd.Timestamp('2000-01-05') # default timestamp 2 is super early
if len(cashouts) > 1:
    ts2 = cashouts.index[1] # last cashout

current_df = df.loc[ts1:ts2]



# calculate the different money sources

## calculating amount of money won from live games, livegame TPG, winrates and levels
livegame_df = current_df.loc[
    current_df['type'] == 'GameEnd']
livegame_results = livegame_df['balancechange'] + (livegame_df['escrowchange'])
money_from_livegames = livegame_results.sum()

# take per game
n_livegame_wins = livegame_df.loc[df['reason'] == 'win'].shape[0]
n_livegames = livegame_df.shape[0]
livegame_tpg = round(money_from_livegames/n_livegames,2)


## calculating take per game from matchup games;
matchup_df = current_df.loc[
    current_df['type'] == 'AcknowledgeResult']

matchup_results = matchup_df['balancechange'] + matchup_df['escrowchange']
money_from_matchups = matchup_results.sum()

n_matchup_wins = livegame_df.loc[df['result'] == 'win'].shape[0]
n_matchups = matchup_df.shape[0]
matchup_tpg = round(money_from_matchups/n_matchups,2)


## calculating revenue source by player;
games_df = current_df.loc[(current_df['type'] == 'AcknowledgeResult')
                          |
                          (current_df['type'] == 'GameEnd')
                          ]

top_3_sources = games_df.groupby('opponentusername')['balancechange'].sum().sort_values(ascending=False)[0:3]








## calculating the financial value claimed in rewards;
rewards_df = current_df.loc[
    (current_df['type'] == 'ClaimGoalReward')
               &
               (current_df['awardedprizetype'] == 'Tokens')]

money_from_rewards = rewards_df['balancechange'].sum()



## calculating money from mega spins
megaspin_df = current_df.loc[
    (current_df['type'] == 'Awarded')
    &
    (current_df['usedpowerup'] == 'TowerJump')]

money_from_megaspin = megaspin_df['balancechange'].sum()










## calculate money from admin adding balance

## calculate money from tournament activities

types = ['Awarded', 'AcknowledgeResult', 'GameEnd', 'ClaimGoalReward']

non_gameplay_invite_df = current_df.loc[
    (~current_df['type'].isin(types))
    &
    (current_df['balancechange'] > 0)   
]

awarded_df = current_df.loc[
    (current_df['type'] == 'Awarded')
    &
    (current_df['usedpowerup'] == 'TowerJump')
]



# print(non_gameplay_invite_df[['type', 'balancechange']])




## eventually I must refactor / calculate for the amount spent for IAPs and joining tournaments







def calc_pct(indiv, group):
    return round((indiv / group) * 100,0)


# check the balances
total_won_calculated = money_from_megaspin + money_from_matchups + money_from_livegames + money_from_rewards
cashout_value = cashouts['prevbalance'][0]
username = cashouts['username'][0]
note = "Invited players are hard to track down based on the way our database is currently written"


# construct the response string
response_string = f"""
--- Overview ---
Username: {username}
Cashout Value: {cashout_value} 
Audited Value: {total_won_calculated}
Audit Date: {datetime.datetime.now().strftime("%d/%m/%Y %I:%M %p")}

Revenue Source Breakdown: Amount = % of whole
|- Mega Spins: {money_from_megaspin} = {calc_pct(money_from_megaspin, total_won_calculated)}%
|- Live Games: {money_from_livegames} = {calc_pct(money_from_livegames, total_won_calculated)}%
|- MatchUPs: {money_from_matchups} = {calc_pct(money_from_matchups, total_won_calculated)}%
|- Goals/Awards: {money_from_rewards} = {calc_pct(money_from_rewards, total_won_calculated)}%
|- Others (to be added) - AdminAddBalance, Tournament Win

--- GamePlay Analysis ---
Livegame TPG: {livegame_tpg}
MatchUP TPG: {matchup_tpg}

Livegame winrate: {calc_pct(n_livegame_wins, n_livegames)} %
MatchUP: {calc_pct(n_matchup_wins, n_matchups)}%
Most money won from: 
{top_3_sources}

Value mixed with invited players: 


NOTE:
- {note}
- All values in pennies
- If value between Audited value != Cashout value, there may be some value unaccounted for;
- If the amount is not great, we can ignore it, however, if it is significant, this requires manual review.

INCOMPLETE BUILD
"""
# print(response_string)
pyperclip.copy(response_string)







