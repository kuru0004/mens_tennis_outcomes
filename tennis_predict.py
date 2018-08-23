
import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV


"""
Pseudo code:

To train:

given1 = match_date
given2 = player_1_name
given3 = player_2_name
given4 = surface 
## posit : clay = 0.5 similar to grass (sseems should be higher)
## posit : hard = 0.8 similar to grss (seems right)
## posit : hard = 0.7 similar to clay 
### note: a players winning percentage with be deceptively low (if they lose a previous match, they might have won a subsequent match according to their abilities)
...Therefore, should I ascribe a winning percentage?

time_weights = 
for match1 in sorted(recent_matches1 asceiding=False):
	#
	for stat in stat_list: 

All this in a nutshell:
A player is the 'total' of their *relevant* stats
	--stat subset
	--stat falloff based on time
This valuation of player can be put in model

"""

