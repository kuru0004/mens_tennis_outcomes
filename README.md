This project aims to predict win probability for one player of professional mens tennis singles match on the ATP Tour.  There have been several models developed for this purpose in the past (The review by Kovalchik (2016) has an excellent comparison and discussion of the models). Some have used regression ('logit' or 'probit') methods, whereas others have predicted winners based on point-by-point outcome probabilities.  One of the best methods comes from FiveThirtyEight, resulting in an accuracy of 70%.  This method uses a pair comparison model, based on Elo Rankings.  Elo Rankings, invented by physics professor Arpad Elo, were first used in chess rankings in 1960.

This proposal attempts to broaden the work done thus far, and would need to achieve accuracies in 70% range to be useful.  The predictors (features) that were found to be useful (especially relative rankings of the players) will be preserved, while considering other features not addressed by all models.  A pair of examples are as follows:
1. Player having early exits from more than one previous tournament
2. Weighting recent result less strongly than the exponential drop-off of one previous model, perhaps with a power law.
The most significant departure from existing model that this proposal will consider is using tree-based models (Random Forests and Boosted Trees).  Boosted trees have been shown to have high performance in other arenas, such as Kaggle competitions.

If this work is successful, the biggest economic impact would be in contributing to gambling and betting lines.  As suggested by Kovalchik (2016), it also could be useful for sports analysts and coaches. Both may gain insight into what makes one player more probable to win than another, where coaches may be able to use that information to benefit a player.

The following is the anticipated workflow and output of this project.  The data needed to implement the work are available in CSV files total approximately 600 MB.  The next step is to understand the data.  Several columns in the data have as-yet undeciphered meanings, such as the suffix 'slug'.  After cleaning the data (including an observed instance of misaligned columns), exploratory data analysis (EDA) will help gain insight into relationships in the data which can inform the model.  At the end of the project, results will be delivered using slides in a presentation. will  
The potential issues with this project anticipated thus far are as follows:
* Finding out if some of the features I think are there are not there
* Making sure that the model only uses past data for any given match
	--Preventing data leakage


 
 


Kovalchik: J. Quant. Anal. Sports 2016; 12(3): 127–138
