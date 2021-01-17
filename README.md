# AI-Poker
This repository is mainly related with my university coursework where I was studying various concepts in artificial intelligence (AI). At the end, the course demands to deliever a project which is based on poker game using AI.

## Background:
Poker is a type of card game, using a standard 52-card deck, in which players bet on the value of the card combination (“hand”) in their possession, by placing a bet into a central pot. The winner of the pot is the non-folded player who holds the hand with the highest value according to an established hand rankings hierarchy. The rare card combinations are more valuable than common. But they aren’t much profitable if player doesn’t have good strategy to play with them.  

### Rules:
The game starts by forcing each player to bet an ante (a forced bet). Once the bet has been set, each player will receive five cards from the server. When it is a player's turn to act, the first action he takes binds him to his choice of action and changing his action after seeing how other players react to his initial action is not permitted. Once each player has received five cards the round can start. The first player can then choose to make one of a few specific actions:  
- Until the first bet is made each player in turn may “check”, which is to not place a bet, or “open”, which is to make the first bet.  
- After the first bet each player may “fold”, which is to drop out of the hand losing any bets they have already made; “call”, which is to match the highest bet so far made; or “raise”, which is to increase the previous high bet.  

Each game, every player will receive a specified amount of chips which they can use for betting. The
maximum amount of chips during a game, the amount the winner will have when the game is over,
are the sum of all players initial amount of chips. 

## Relevant work:
Many research papers already published on poker playing agent using artificial intelligence. The major role in this field is accomplished at University of Alberta, Canada. Darse Billings, Denis Richard Papp and their other colleagues have put light on Computer poker, Dealing with incomplete information in poker, Opponent Modelling in Poker in their papers. 

## Types of agent and AI methods can be applied:
We can implement reflex agent who uses current perceptions from the environment or memory agent who uses actions of self and opponents. Moreover, there many concepts of artificial intelligence that can be implement to improve our poker player. One of them is probability theory in which agent computes the possibility of coming particular hand; second one is using Utility theory which considers utility value for each action taken. We can also implement different search techniques to find which action to take and prune the search using simple alpha-beta or more advanced Monte-Carlo simulation. In addition, online search perform better that offline search techniques for such nondeterministic game. The historical data about similar game environment can be stored into lookup table which can be immediately used to achieve best results. On the other hand, machine learning concepts can be used to train our agent whenever it plays. This will improve its performance over time based on training samples.
