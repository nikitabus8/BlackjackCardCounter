def FindCount(cardsPlayed, NumberOfDecks):
    RunningCount = 0
    decksRemaining = round(NumberOfDecks - (len(cardsPlayed) / 52), 2)

    for card in cardsPlayed:
        if card >= 2 and card <= 6:
            RunningCount += 1
        elif card >= 10 and card <= 11:
            RunningCount -= 1
    
    TrueCount = round(RunningCount / decksRemaining, 2)
    return RunningCount, TrueCount

print(FindCount([10,5,2,9,11,10,3,10,10,6,4,2,10,11,9,10,8,5,10,4,10,10,10,6,10,10,10,8,9,2,10,7,11,10,7,3,10,10,10,5,8,4,7,4,8,5], 6)) #returns (-6, -1.17)