```
Choose an appropriate dataset of your choice such that every record (example) has at least 5 features which are numeric in nature and there is at least one attribute (feature) which is binary in nature. You can use the binary attribute as the binary target label to be predicted. 

Split your dataset into a training set and a test set. You can try different splits: 70:30 (70% training, 30% testing), 80:20 or 90:10 split. 

On the training set, train the following classifiers: 

1. Half Space
2. Logistic Regression (using inbuilt function)
3. SVM classifier (using a linear kernel)
4. SVM classifier (using a Polynomial kernel and a Gaussian kernel)
5. Logistic Regression using the SGD procedure. 

If your data is not linearly separable, then you will be required to use the soft SVM formulation. 
You can use the inbuilt implementation of logistic regression and SVM in SciKit Learn.

Compare and analyze the results obtained by using the different classifiers. For the soft SVM formulation, you should compare the performance with the different values of the regularization parameter. Report the number of support vectors obtained for every dataset split. 
You should submit a report along with the code. 
```

### File Structure
- README.md file for question and steps to run the program.
- It has Notebook file for demo purpose how code works.
- It also contains Report file for analytic purpose.

### Instruction to run the program

- Step1: Install the depencies like seaborn, sklearn, matplotlib, python
- Step2: python main.py

