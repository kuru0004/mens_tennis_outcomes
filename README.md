# Men's Tennis Predictions

This project predicts win probabilities for players in professional mens tennis singles match on the ATP Tour.  

# Background
There have been several models developed for this purpose in the past. The [review](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) by Kovalchik (2016) has an excellent comparison and discussion of the models. Some have used regression ('logit' or 'probit') methods, whereas others have predicted winners based on point-by-point outcome probabilities.  One of the best methods comes from FiveThirtyEight, resulting in an accuracy of 70%.  This method uses a pair comparison model, based on Elo Rankings.  Elo Rankings, invented by physics professor Arpad Elo, were first used in chess rankings in 1960.

The biggest economic impact would be in contributing to gambling and betting lines.  As suggested by Kovalchik (2016), it also could be useful for sports analysts and coaches. Both may gain insight into what makes one player more probable to win than another, where coaches may be able to use that information to benefit a player.

# Procedures followed

The project uses data gathered by Jeff Sackmann at [Tennis Abstracts](link). It was available on GitHub in the [atp_mens__tennis repo](link).  Each row of data is for a particular match and each column contains the factors (features) of the match.  The features are of three types:
* Tournament features: !! Make an eg list (Tournament ID, Date, Surface etc.)
* Players features:  !! Make an eg list (Height, Age, Handedness)
* Match features: !! Make an eg list (Aces, Double Faults, etc.)

Two challenges in this gathered data are as follows:
1. Each row contains both the winner and the loser, and so does not associate well with a single target
2. Rows contain _match features_ about the match itself, which **would not** be available for the sake of predicting the match.

Since the _match features_ are considered important to making a more accurate prediction, a method to obtain these features is required.

## Feature engineering




## Logistic regression

## Random Forest

## Gradient-Boosted Trees

# Results and Discussion

The results of this two-week project yielded an accuracy of 60%. Accuracy is an acceptable metric since this is an eminently balanced class problem

# Further Investigation



# Reference Cited :
Stephanie Ann Kovalchik. ["Searching for the GOAT of tennis win prediction"](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) _Journal of Quantitative Analysis in Sports_. 12(3): 127–138, 2016.
