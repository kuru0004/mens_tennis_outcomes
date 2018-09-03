# Men's Tennis Predictions

Do you know the feeling when your favorite team or player loses a game they were supposed to win?  As a sports fan, I have experienced that dejection, especially painfully in the elimination stages at the end of a season or tournament. What determines how well one can predict outcomes in sports competitions? One can start to answer this question with an example case, specifically men's tennis matches. This project predicts player win probabilities in men's professional tennis singles match on the ATP Tour. 

# Background
There have been several models developed for this purpose in the past. The [review](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) by Kovalchik (2016) has an excellent comparison and discussion of the models. Some have used regression ('logit' or 'probit') methods, whereas others have predicted winners based on point-by-point outcome probabilities.  One of the best methods comes from FiveThirtyEight, resulting in an accuracy of 70%.  This method uses a pair comparison model, based on Elo Ratings.  [Elo Ratings](https://en.wikipedia.org/wiki/Elo_rating_system), invented by physics professor Arpad Elo, were first used in chess rankings in 1960.

The biggest economic impact of accurate predictions is contributing to gambling and betting lines.  As suggested by Kovalchik (2016), it also could be useful for sports analysts and coaches. Both may gain insight into what makes one player more probable to win than another, where coaches may be able to use that information to benefit a player.

# Procedures followed

The project uses data gathered by Jeff Sackmann at [Tennis Abstract](http://www.tennisabstract.com/). It was available on GitHub in the [tennis_atp repo](https://github.com/JeffSackmann/tennis_atp).  Each row of data is for a particular match and each column contains the factors (features) of the match.  For data from 1992 through 2017, a larger set of data are available. (Data is also available for 2018, but this data was not used because the tournaments for that year were not complete at the time of the project.  Including this data would bias the data
The features are of three types:
* Tournament features: Tournament ID, Date, Playing Surface, etc.
* Players features: Height, Age, Handedness
* Match features: Aces, Double Faults, etc.

An overview of the process is shown in Figure 1.  The data was prepared using the stardard Python stack (numpy, pandas, etc.) to 

<p align="center"> 
<img src="images/workflow_tools_fig.png" height=80%, width=80%, alt="Workflow and Tech stack"><br> <b>Figure 1:</b> Machine Learning Workflow and Tools
</p>



Two challenges in this gathered data are as follows:
1. Each row contains both the winner and the loser, and so does not associate well with a single target.
2. Rows contain _match features_ about the match itself, which **would not** be available for the sake of predicting the match.

For the first issue, data needs separated into data for the winner and data for the loser.  For the second issue, the _match features_ are considered important to making a more accurate prediction. Thus, a method to populate these features is required.

### Feature engineering

_Feature engineering_ refers to the process of modifying the feature space (adding, removing, or transforming features) for the purpose of making them more predictive.  Feature engineering for the two steps mentioned above were accomplished using the following procedures.

The dataset was first paritioned into two sets, one for the winner and one for the loser. The feature names (i.e. column labels) were then matched when appropriate (e.g. "Winner Aces" and "Loser Aces" to "Aces").  A new column is added, with label "1" ascribed to the winner data and "0" ascribed to the loser data.  The next step is concatenating the two resultant datasets to make one large dataframe. This accomplishes the first step needed: each row is associated with a unique target. This step has the 

The second step involves generating the statistics of interest for a particular match. Since one only has access to _past_ data, some form of data from _previous matches_ is needed. In the project, data for any match were generated for the _players in the match_ from the past _one year_ of matches that the player played. This was done using rolling average in pandas, with the .rolling() DataFrame method.

<p align="center"> 
<img src="images/data_to_feature_eng.png" height=80%, width=80%, alt="Player Groups" align="middle"><br> <b>Figure 2:</b> Data Grouped by Player
</p>

<p align="center"> 
<img src="images/feature_eng_applies_to_each_record.png" height=80%, width=80%, alt="Expunge Extra Data" align="middle"><br> <b>Figure 3:</b> Eliminate Data Inaccessible <i>a priori</i>
</p>

<p align="center"> 
<img src="images/result_exmpl_of_feature_eng.png" height=85%, width=85%, alt="Expunge Extra Data" align="middle"><br> <b>Figure 4:</b> Generate New Feature Values Based on Previous Player Data
</p>

### Models Used

The models used were logistic regression, random forests, and gradient-boosted trees.  To make as direct a comparison between the models, the same features were used in the analysis. 

The list of features used is as follows:





# Results and Discussion

The results of this two-week project yielded an accuracy of 60%.  All three models are within 1% of this value. Accuracy is an acceptable metric since this is an eminently balanced class problem: For every winner, there is a loser.

Interestingly, all three models considered here yielded very similar accuracy using the same features. For the two tree-based methods, the hyper-parameters were tuned.  It is likely that the Random Forest model is nearly optimally tuned, but the Gradient-boosted Tree models may benefit from additional tuning.  However further efforts would likely best be spent on feature selection or on feature engineering.

## Insights


<p align="center"> 
<img src="images/logistic_reg_coeff_plot.jpg" height=80%, width=80%, alt="Fehttps://github.com/kuru0004/mens_tennis_outcomes/blob/18_readme_update/images/workflow_tools_fig.pngature Importance for Logistic Regression"><br> <b>Figure 5:</b> Logistic Regression Coefficients For Normalized Model Features
</p>


<p align="center"> 
<img src="images/random_forest_feature_imp_plot.jpg" height=80%, width=80%, alt="Expunge Extra Data" ><br> <b>Figure 6:</b> Generate New Feature Values Based on Previous Player Data
</p>



# Further Investigation 

Several avenues for further investigation exist:
1. Considering a simpler model, so that there is no need for computing statistics from previous matches.
2. Using clustering to group players to determine a style and utilize these groups to make better predictions. 
3. Distributing the statistics over the surfaces (eg. aces on grass) because I have a difficult time believing the results that surface is not a major predictor.


# Reference Cited :
Stephanie Ann Kovalchik. ["Searching for the GOAT of tennis win prediction"](http://vuir.vu.edu.au/34652/1/jqas-2015-0059.pdf) _Journal of Quantitative Analysis in Sports_. 12(3): 127–138 (2016).<br>
Wikipedia contributors, ["Elo rating system"](https://en.wikipedia.org/wiki/Elo_rating_system) _Wikipedia, The Free Encyclopedia_. https://en.wikipedia.org/w/index.php?title=Elo_rating_system&oldid=856785064 (accessed 15 Aug 2018). 
