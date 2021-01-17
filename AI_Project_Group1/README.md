# AI poker implementation
In the given AI Poker application, the server application allows clients to connect to it, and once all clients are connected then game starts. The game is controlled by the server which  sends query to each player’s client and waits some time to accept a decision from the client. 

Once started, the game goes in a loop until only a single player has all the chips. The loop, controlled by the server, performs these actions each playing round:  
1. The server informs all the players how many chips each player has. 
2. The players receive five cards each from the server. 
3. A forced bet (ante) is drawn from each player and put into the pot.
4. The first betting round. 
5. The draw phase, in which each player is offered to discard some of the cards on hand and receive new cards as replacement for the discarded. The player chooses what cards to discard (if any). 
6. The second betting round.
7. The showdown, which determines the winner of the round. The winner receives the contents of the pot. (In case of multiple winners, the pot is split.) 

Each betting round starts with a player making an opening action: “check”, which is to not place a bet (the opportunity to open moves to the next player); “open”, which is to make the first bet; or going “all-in”, which is to open with all the players remaining chips. Once the round has been opened each player may “fold”, which is to drop out of the hand losing any bets they have already made (but not risking any more); “call”, which is to match the highest bet so far made; “raise”, which is to increase the previous high bet; or go “all-in”, which is to put all the players remaining chips in the pot. 

## Server implementation
The implementation of AI poker server is developed in Java language. A company MediaWave AB based in Sweden had developed this GUI application for ISLAB in University of Sweden, Halmstad, Sweden.

When the AI Poker server is started, there are several settings that can be changed by the user:  
1. The server port is set to 5000 as default, but it can be changed to any suitable number.  
2. The default number of clients is two, in order to simplify testing. We change it to 5 when number of clients is five during the pre-tournament. 
3. The amount of chips is set to 200 as default for each player and should not be increased. 
4. The initial ante is set to 10, but can be changed to any number between 1 and 100.  
5. The ante can be doubled for every round that is a multiple of the specified value. For default value, the ante is 10 for round 1-10, 20 for round 11-20, 40 for round 21-30, 80 for round 31-40, etc. 
6. The client response time is set to 4000 ms. If a player does not respond to a query from the server within the specified time, the server disconnects the player. 

## Client implementation
The implementation of AI poker client is developed in Python language. This implementation is in the scope of students working on the AI poker.

The strategy of my agent is to bluff when making first voluntary bet (i.e. open with high amount for low strength hand and low amount for high strength hand) and bet appropriately low to high chips for week to strong hands respectively. 

## Experiment and tournament result 
- My agent acts based on current hand strength, while random agent it played with is completely randomly do its actions. Random agent does not consider hand cards and thus fold many times when having good cards. So, it is not at all rational. 
- Secondly, when I was playing against rational agent, I found that both agents were playing more number of rounds than with a random agent (which fold/ call early irrespective of its hand). 
- Finally, when I was playing with other agents in pre - tournament, the results were quite unexpected. My agent won only 3 matches out of total 20 matches. The oppent’s strategy was better than my agent. 
