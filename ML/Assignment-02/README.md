```
This assignment is on 
1. Familiarization with DataFrames, Matplotlib, Sklearn, 
2. Implementing Linear Regression.
```

```
Use Dataframe constructor in Pandas to create your own Dataframe. 

Print a chosen record (row) or a chosen column (data field). 

Print rows that satisfy a condition on one of the column entries. For example, if you create a DataFrame of players' performance in a cricket match and each record has the runs scored by the player in a cricket match, then you should be able to the print records of players who scored more than 50 runs. 
Also sort the records based on the number of runs scored by each player. 


Use vectorised operations. For example, you may be required to compute the percentage runs scored by each player, where the percentage is with respect to the total runs scored by the team in an innings. 

Add a new column to the Dataframe. For example, you may want to add the number written on the player's jersey. 

Export the Dataframe to a file in pickle format and save it as a file.  Read the pickle file back to the program. 


Use matplotlib library to make a scatter plot of columns that contain numeric
data. Provide labels to the axes. 


Implement linear regression to model the dependency between two variables - the predictor x and target y. You can choose any two columns in your data frame as the two variables. Print the coefficients obtained from linear regression and plot the straight line on the scatter plot.  Do not use any inbuilt function for implementing linear regression.  You need to formulate a linear system of equations and solve them using pseudo inverse.  You can compare your result with that produced by the fit() function of LinearRegression model in sklearn.
```