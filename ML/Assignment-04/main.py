######################## Import liberies ############################
# import liberaries
import warnings
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPClassifier


batch_sizes = [200, 1000, 5000, 10000, 60000]
print("Neural Network using MLPClassifier(Multi-layer Perceptron classifier) with stochastic gradient descent.")
print("\nConsidered batch sizes are as follow: ")
print(batch_sizes)


######################## 2.Fetching online mnist_784 dataset ##########
# Fetching the mnist_784 dataset
print("\n loading mnist_784 dataset")
X, y = fetch_openml('mnist_784', version=1, return_X_y=True)

print("\n loaded datset.\n\n")
######################## 3.normalize the dataset ############################
# Normalize the intensity in range(0,1) from (0,255)
X = X / 255

######################## 4.Spliting the mnist dataset into training and testing dataset ############################
# Spliting the mnist dataset for testing and training
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]


######################## 5. Training and testing dataset using MLPClassifier(Multi-layer Perceptron classifier). ############################
# make a list of different batch sizes
print("Training without fliped dataset")
# batch_sizes = [200, 1000, 5000, 10000, 60000]
for b_s in batch_sizes:
    # Build model using MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(50,),max_iter=10,
                    solver='sgd',verbose=10, batch_size=b_s)

    # Remove unneccessary waring
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
        # Training the dataset
        mlp.fit(X_train, y_train)
    
    # printing the Batch size
    print("\nBatch size: ", b_s)
    
    # Accuracy/Score on training dataset
    print("Training set score: %f" % mlp.score(X_train, y_train))
    
    # Accuracy/Score on testing dataset
    print("Test set score: %f" % mlp.score(X_test, y_test))
    
    # plot the loss with the iteration
    plt.plot(mlp.loss_curve_)
    plt.xlabel('Iteration No')
    plt.ylabel('Loss')
    plt.show()

######################## 6.Flipping the image ############################
# Flip the intensities of the image for the testing and training dataset
Flip_X_train = (255 -X_train*255)/255
Flip_X_test = (255-X_test*255)/255

######################## 7.Training and testing for flipped dataset using MLPClassifier(Multi-layer Perceptron classifier). ############################
# make a list of different batch sizes
print("Training with fliped dataset")
# batch_sizes = [200, 1000, 5000, 10000, 60000]
for b_s in batch_sizes:
    # Build model using MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(50,),max_iter=10,
                    solver='sgd',verbose=10, batch_size=b_s)
    
    # Remove unneccessary waring
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
        # Training the dataset
        mlp.fit(Flip_X_train, y_train)
    
    # printing the Batch size
    print("\nBatch size: ", b_s)
    
    # Accuracy/Score on training dataset
    print("Fliped image training set score: %f" % mlp.score(Flip_X_train, y_train))
    
    # Accuracy/Score on testing dataset
    print("Fliped image test set score: %f" % mlp.score(Flip_X_test, y_test))
    
    # plot the loss with the iteration
    plt.plot(mlp.loss_curve_)
    plt.xlabel('Iteration No for flipped image')
    plt.ylabel('Loss')
    plt.show()

######################## 8.Training and testing for combined flipped and unflipped dataset using MLPClassifier(Multi-layer Perceptron classifier). ############################
import numpy as np
Combine_X_train = np.concatenate((X_train, Flip_X_train))
Combine_X_test = np.concatenate((X_test, Flip_X_test))
Combine_y_train = np.concatenate((y_train, y_train))
Combine_y_test = np.concatenate((y_test, y_test))

print("Training combined fliped and unfliped dataset")
# batch_sizes = [200, 1000, 5000, 10000, 60000]
for b_s in batch_sizes:
    # Build model using MLPClassifier
    mlp = MLPClassifier(hidden_layer_sizes=(50,),max_iter=10,
                    solver='sgd',verbose=10, batch_size=b_s)
    
    # Remove unneccessary waring
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=ConvergenceWarning, module="sklearn")
        # Training the dataset
        mlp.fit(Combine_X_train, Combine_y_train)
    
    # printing the Batch size
    print("\nBatch size: ", b_s)
    
    # Accuracy/Score on training dataset
    print("Combined image training set score: %f" % mlp.score(Combine_X_train, Combine_y_train))
    
    # Accuracy/Score on testing dataset
    print("Combined image test set score: %f" % mlp.score(Combine_X_test, Combine_y_test))
    
    # plot the loss with the iteration
    plt.plot(mlp.loss_curve_)
    plt.xlabel('Iteration No for Combined image')
    plt.ylabel('Loss')
    plt.show()
