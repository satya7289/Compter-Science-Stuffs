```
Create a neural network with Tensorflow. Use it for classification of MNIST or any other dataset of your choice. 
Divide the dataset into training, validation and test set. 
Report the accuracy obtained by 
1) Varying the number of hidden layers from 0 to 2. Choose the number of neurons in the hidden layers such that the total number of parameters in the network remain the same. 
2) Trying sigmoid and relu activation functions for the hidden layer nodes.
3) Not using any nonlinearity in the network

Your program should use the validation set to decide when to stop training. Compute the error on the validation set after every epoch. Stop the training once the error on the validation set starts increasing, or if there is negligible reduction in the error on the validation set for 5 consecutive epochs. 

Summarize your results in a report. Submit the report (as a pdf file) along with the code. 
```