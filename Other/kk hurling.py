import random

KK_Teams=['Ballyhale', 'Bennettsbridge', 'Clara', 'Dicksboro', 'Erins Own', 'GBC', 'Glenmore', 'James Stephens', 'Lisdowney', 'Mvat', 'OLG', 'Tullaroan']

def league_draw ():
    print("\n")
    
    print ("Teams: ", KK_Teams) 
    random.shuffle(KK_Teams) 

    
    print('\nThe two groups are: \n')
    print (KK_Teams[0:6])
    print (KK_Teams[6:])

def championship_draw():
    random.shuffle(KK_Teams)

    print('\nChampionship Draw \n')       
    print ('Match 1',(KK_Teams[0:2]))
    print ('Match 2',(KK_Teams[2:4]))
    print ('Match 3',(KK_Teams[4:6]))
    print ('Match 4',(KK_Teams[6:8]))
    print ('Match 5',(KK_Teams[8:10]))
    print ('Match 6',(KK_Teams[10:]))
    
league_draw()
championship_draw()
