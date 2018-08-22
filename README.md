# Men's Tennis Predictions

This project predicts win probabilities for players in professional mens tennis singles match on the ATP Tour. 

# Background
There have been several models developed for this purpose in the past. The [review](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) by Kovalchik (2016) has an excellent comparison and discussion of the models. Some have used regression ('logit' or 'probit') methods, whereas others have predicted winners based on point-by-point outcome probabilities.  One of the best methods comes from FiveThirtyEight, resulting in an accuracy of 70%.  This method uses a pair comparison model, based on Elo Rankings.  Elo Rankings, invented by physics professor Arpad Elo, were first used in chess rankings in 1960.

The biggest economic impact of accurate predictions is contributing to gambling and betting lines.  As suggested by Kovalchik (2016), it also could be useful for sports analysts and coaches. Both may gain insight into what makes one player more probable to win than another, where coaches may be able to use that information to benefit a player.

# Procedures followed

The project uses data gathered by Jeff Sackmann at [Tennis Abstract](http://www.tennisabstract.com/). It was available on GitHub in the [atp_mens__tennis repo](link).  Each row of data is for a particular match and each column contains the factors (features) of the match.  The features are of three types:
* Tournament features: Tournament ID, Date, Playing Surface, etc.
* Players features: Height, Age, Handedness
* Match features: Aces, Double Faults, etc.

Two challenges in this gathered data are as follows:
1. Each row contains both the winner and the loser, and so does not associate well with a single target.
2. Rows contain _match features_ about the match itself, which **would not** be available for the sake of predicting the match.

For the first issue, data needs separated into data for the winner and data for the loser.  For the second issue, the _match features_ are considered important to making a more accurate prediction. Thus, a method to populate these features is required.

## Feature engineering

_Feature engineering_ refers to the process of modifying the feature space (adding, removing, or transforming features) for the purpose of making them more predictive.  Feature engineering for the two steps mentioned above were accomplished using the following procedure.

The dataset was first paritioned into two sets, one for the winner and one for the loser. The feature names (i.e. column labels) were then matched when appropriate (e.g. "Winner Aces" and "Loser Aces" to "Aces").  A new column is added, with label "1" ascribed to the winner data and "0" ascribed to the loser data.  The next step is concatenating the two resultant datasets to make one large dataframe. This accomplishes the first step needed: each row is associated with a unique target.

The second step involves generating the statistics of interest for a particular match. Since one only has access to _past_ data, some form of past data is needed. In the project, data for any match were generated for the _players in the match_ from the past _one year_ of matches that player played. This was done using rolling average in pandas

 

## Logistic regression

Logistic regression: 60%
## Random Forest

Random forests: 60%
## Gradient-Boosted Trees



## Results and Discussion

The results of this two-week project yielded an accuracy of 60%.  All three models are within 1% (!!need to check!!) of this value. Accuracy is an acceptable metric since this is an eminently balanced class problem: For every winner, there is a loser

Interestingly, all three models considered here yielded very similar accuracy using the same features. For the two tree-based methods, the hyper-parameters were tuned.  It is likely that the Random Forest model is nearly optimally tuned, but the Gradient-boosted Tree models may benefit from additional tuning.


# Further Investigation 

Several avenues for 


# Reference Cited :
Stephanie Ann Kovalchik. ["Searching for the GOAT of tennis win prediction"](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) _Journal of Quantitative Analysis in Sports_. 12(3): 127–138, 2016.
