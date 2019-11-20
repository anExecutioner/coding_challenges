def baseballGame(players,target):
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        for player in players:
            for i in range(player, len(dp)): 
                dp[i].extend(comb + [player] for comb in dp[i - player])
        return len(dp[-1])
        
if __name__ == "__main__":
    players=[3,5,10]
    target=int(input())
    print(baseballGame(players,target))