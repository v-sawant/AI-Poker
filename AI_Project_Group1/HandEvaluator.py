#PYHTON FILE TO EVALUATE HAND
import operator
from ClientBase import *

NORM_VAL = 2600000
class HandRankCategory(object):
	NB_COMB_5_CARD = 2598960

	#Hand categories
	HIGH = "High"
	ONE_PAIR = "One Pair"
	THREE_OF_A_KIND = "Three Of A Kind"
	TWO_PAIR = "Two Pair"
	STRAIGHT = "Straight"
	FLUSH = "Flush"
	FULL_HOUSE = "Full House"
	FOUR_OF_A_KIND = "Four Of A Kind"
	STRAIGHT_FLUSH = "Straight Flush"
	
	#Possible combinations of Hand categories
	nHIGH = 1302540 #1296420
	nONE_PAIR = 1098240 #1500720
	nTHREE_OF_A_KIND = 54912 #2475408
	nTWO_PAIR = 123552 #2544048
	nSTRAIGHT = 10240 #2588720
	nFLUSH = 5148 #2593812
	nFULL_HOUSE = 3744 #2595216
	nFOUR_OF_A_KIND = 624 #2598336
	nSTRAIGHT_FLUSH = 40 #2598920
	
	#assigning hand strengths/weights
	hand_wt_dict = {
	HIGH: NB_COMB_5_CARD - nHIGH, 
	ONE_PAIR: NB_COMB_5_CARD - nONE_PAIR, 
	THREE_OF_A_KIND: NB_COMB_5_CARD - nTHREE_OF_A_KIND,
	TWO_PAIR: NB_COMB_5_CARD - nTWO_PAIR,
	STRAIGHT: NB_COMB_5_CARD - nSTRAIGHT,
	FLUSH: NB_COMB_5_CARD - nFLUSH,
	FULL_HOUSE: NB_COMB_5_CARD - nFULL_HOUSE,
	FOUR_OF_A_KIND: NB_COMB_5_CARD - nFOUR_OF_A_KIND,
	STRAIGHT_FLUSH: NB_COMB_5_CARD - nSTRAIGHT_FLUSH
	}

'''
HAND STRENGTH EVALUATOR
'''
class HandEvaluator(object):
	def __init__(self):
		self.hand_cards = []#hand_cards
		self.hand_cat_name = ""
		self.hand_cat_wt = 0
		self.hand_value = 0.0

	# Rank: {2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A}
	rank_wt_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
	# Suit: {c, d, h, s}
	suit_wt_dict = {'c':20, 'd':21, 'h':22, 's':23}
	# HAND info
	def getHandInfo(self):
		#Store hand cards values into dictionary
		sorted_hand = self.sortByRank(self.convertCardValues(self.hand_cards))[::-1] # high to low card
		#print("sorted_hand-----------", sorted_hand)
		tmpdict = dict(name=self.hand_cat_name, rank1=sorted_hand[0][0], suit1=sorted_hand[0][1], rank2=sorted_hand[1][0], suit2=sorted_hand[1][1], rank3=sorted_hand[2][0], rank4=sorted_hand[3][0], rank5=sorted_hand[4][0])
		#print("tmpdict----------", tmpdict)
		return tmpdict

	#analyse hand
	def analyseHand(self, hand):
		#check for each hand types mentioned below
		#store and return integer value calculated from hand type with its other parameters like high card rank, suit, etc.
		
		#Get hand category name
		if(self.isStraightFlush(hand)): 
			self.hand_cat_name = HandRankCategory.STRAIGHT_FLUSH
		
		elif(self.isFourOfAKind(hand)): 
			self.hand_cat_name = HandRankCategory.FOUR_OF_A_KIND
		
		elif(self.isFullHouse(hand)): 
			self.hand_cat_name = HandRankCategory.FULL_HOUSE
		
		elif(self.isFlush(hand)):
			self.hand_cat_name = HandRankCategory.FLUSH
		
		elif(self.isStraight(hand)):
			self.hand_cat_name = HandRankCategory.STRAIGHT
		
		elif(self.isThreeOfAKind(hand)):
			self.hand_cat_name = HandRankCategory.THREE_OF_A_KIND
		
		elif(self.isTwoPair(hand)):
			self.hand_cat_name = HandRankCategory.TWO_PAIR
		
		elif(self.isOnePair(hand)):
			self.hand_cat_name = HandRankCategory.ONE_PAIR
		
		elif(self.isHighCard(hand)):
			self.hand_cat_name = HandRankCategory.HIGH
		
		self.hand_cat_wt = HandRankCategory.hand_wt_dict[self.hand_cat_name]
		
		#Store hand cards values into dictionary
		sorted_hand = self.sortByRank(hand)[::-1] # high to low card

		val = self.hand_cat_wt + sorted_hand[0][0] + sorted_hand[1][0] + sorted_hand[2][0] + sorted_hand[3][0] + sorted_hand[4][0]

		return val #integer value

	# Evaluate
	def evaluate(self, hand_cards):
		self.hand_cards = hand_cards
		global NORM_VAL
		hand_rank = self.analyseHand(self.convertCardValues(self.hand_cards))
		self.hand_value = hand_rank/float(NORM_VAL)
		return self.hand_value #float value
		
	# Convert hand cards w.r.t. their rank weights
	def convertCardValues(self, hand):
		card_list = []#list of tuple
		for c in hand:
			c_tp = (self.rank_wt_dict[c[0]], self.suit_wt_dict[c[1]])
			card_list.append(c_tp)
		return card_list

	'''
	pass converted hand to sort
	'''
	def sortBySuit(self, _hand):
		card_list = []#list of tuple
		card_list = sorted(_hand, key=operator.itemgetter(1,0))
		return card_list

	'''
	pass converted hand to sort
	'''
	def sortByRank(self, _hand):
		card_list = []#list of tuple
		card_list = sorted(_hand, key=operator.itemgetter(0,1))
		return card_list
	
	'''
	Flush means There is one suit of cards in the Poker hand.
	_hand: pass converted hand to sort
	'''
	def isFlush(self, _hand):
		h_list = []
		h_list = self.sortBySuit(_hand)
		return (h_list[0][1] == h_list[-1][1])
	
	'''
	Straight means The cards are increasing continuously in rank
	_hand: pass converted hand to sort
	'''
	def isStraight(self, _hand):
		isIt = False
		h_list = []
		h_list = self.sortByRank(_hand)
		isIt = h_list[0][0] == h_list[1][0]-1 == h_list[2][0]-2 == h_list[3][0]-3 == h_list[4][0]-4
		return isIt
	
	def isStraightFlush(self, _hand):
		return (self.isStraight(_hand) and self.isFlush(_hand))
		
	def isRoyalFlush(self, _hand):
		return (self.isStraight(_hand) and self.isFlush(_hand) and self.sortByRank(_hand)[-1][0] == rank_wt_dict['A'])
	
	def isFourOfAKind(self, _hand):
		isIt = False
		t_hand = self.sortByRank(_hand)
		case1 = t_hand[0][0] == t_hand[1][0] == t_hand[2][0] == t_hand[3][0]
		case2 = t_hand[1][0] == t_hand[2][0] == t_hand[3][0] == t_hand[4][0]
		isIt = case1 or case2
		return isIt
	
	def isFullHouse(self, _hand):
		isIt = False
		t_hand = self.sortByRank(_hand)
		case1 = t_hand[0][0] == t_hand[1][0] == t_hand[2][0] and t_hand[3][0] == t_hand[4][0]
		case2 = t_hand[0][0] == t_hand[1][0] and t_hand[2][0] == t_hand[3][0] == t_hand[4][0]
		isIt = case1 or case2
		return isIt
	
	def isThreeOfAKind(self, _hand):
		isIt = False
		t_hand = self.sortByRank(_hand)
		case1 = t_hand[0][0] == t_hand[1][0] == t_hand[2][0] and t_hand[3][0] != t_hand[4][0]
		case2 = t_hand[0][0] != t_hand[1][0] and t_hand[2][0] == t_hand[3][0] == t_hand[4][0]
		case3 = t_hand[0][0] != t_hand[4][0] and t_hand[1][0] == t_hand[2][0] == t_hand[3][0]
		isIt = case1 or case2 or case3
		return isIt
	
	def isTwoPair(self, _hand):
		isIt = False
		t_hand = self.sortByRank(_hand)
		case1 = t_hand[0][0] == t_hand[1][0] and t_hand[1][0] != t_hand[2][0] and t_hand[2][0] == t_hand[3][0] and t_hand[3][0] != t_hand[4][0] and t_hand[0][0] != t_hand[4][0]
		case2 = t_hand[0][0] == t_hand[1][0] and t_hand[1][0] != t_hand[2][0] and t_hand[2][0] != t_hand[3][0] and t_hand[3][0] == t_hand[4][0] and t_hand[0][0] != t_hand[4][0]
		case3 = t_hand[1][0] == t_hand[2][0] and t_hand[3][0] == t_hand[4][0] and t_hand[2][0] != t_hand[3][0] and t_hand[0][0] != t_hand[2][0] and t_hand[0][0] != t_hand[4][0]
		isIt = case1 or case2 or case3
		return isIt
		
	def isOnePair(self, _hand):
		isIt = False
		t_hand = self.sortByRank(_hand)
		other =  self.isFourOfAKind(_hand) or self.isFullHouse(_hand) or self.isThreeOfAKind(_hand) or self.isTwoPair(_hand)
		case1 = t_hand[0][0] == t_hand[1][0]
		case2 = t_hand[1][0] == t_hand[2][0]
		case3 = t_hand[2][0] == t_hand[3][0]
		case4 = t_hand[3][0] == t_hand[4][0]
		isIt = (case1 or case2 or case3 or case4) and not other
		return isIt

	def isHighCard(self, _hand):
		other = self.isStraight(_hand) or self.isFlush(_hand) or self.isFourOfAKind(_hand) or self.isFullHouse(_hand) or self.isThreeOfAKind(_hand) or self.isTwoPair(_hand) or self.isOnePair(_hand)
		case1 = _hand[0][0] != _hand[1][0] != _hand[2][0] != _hand[3][0] != _hand[4][0]
		return case1 and not other

