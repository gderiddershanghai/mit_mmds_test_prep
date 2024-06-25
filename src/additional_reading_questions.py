###########GPT Generated Questions############################
###########ISLR Chapter 2############################
chapter2_question_1 = {
    'question': "What is the goal of statistical learning?",
    'options_list': [
        'To predict a quantitative response based on predictor variables',
        'To understand the association between inputs and outputs',
        'Both to predict a response based on inputs and to understand the association between inputs and outputs',
        'None of the above'
    ],
    'correct_answer': 'Both to predict a response based on inputs and to understand the association between inputs and outputs',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_2 = {
    'question': "Which term describes the inputs or predictors in statistical learning?",
    'options_list': [
        'Independent variables',
        'Dependent variables',
        'Response variables',
        'None of the above'
    ],
    'correct_answer': 'Independent variables',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_3 = {
    'question': "What is the error term in a statistical learning model?",
    'options_list': [
        'The part of the model that cannot be predicted from the input data',
        'The difference between the predicted and actual values of the response',
        'The variance of the model',
        'The bias of the model'
    ],
    'correct_answer': 'The part of the model that cannot be predicted from the input data',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_4 = {
    'question': "In the context of statistical learning, what does overfitting mean?",
    'options_list': [
        'The model is too simple to capture the underlying structure of the data',
        'The model captures the underlying structure of the data as well as random noise',
        'The model has not used enough training data',
        'The model is too complex to be interpreted'
    ],
    'correct_answer': 'The model captures the underlying structure of the data as well as random noise',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_5 = {
    'question': "What does the Bayes classifier do?",
    'options_list': [
        'Minimizes the test error rate by assigning the most likely class given the predictor values',
        'Maximizes the likelihood of the predictors given the class labels',
        'Estimates the unknown parameters in the model using Bayesian inference',
        'Directly computes the conditional probability of Y given X without error'
    ],
    'correct_answer': 'Minimizes the test error rate by assigning the most likely class given the predictor values',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_6 = {
    'question': "What is the Bayes error rate?",
    'options_list': [
        'The minimum possible error rate given by any classifier',
        'The error rate of the most flexible model applied to the data',
        'The error rate achieved by applying the least squares method',
        'The error rate achieved by the K-nearest neighbors classifier with K=1'
    ],
    'correct_answer': 'The minimum possible error rate given by any classifier',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_7 = {
    'question': "Which of the following statements about K-nearest neighbors (KNN) is TRUE?",
    'options_list': [
        'KNN always outperforms the Bayes classifier in terms of prediction accuracy',
        'KNN’s prediction accuracy is independent of the choice of K',
        'A smaller value of K makes the decision boundary smoother',
        'A larger value of K makes the model less flexible and reduces the variance'
    ],
    'correct_answer': 'A larger value of K makes the model less flexible and reduces the variance',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_8 = {
    'question': "In the context of bias-variance tradeoff, which of the following statements is TRUE?",
    'options_list': [
        'Increasing model flexibility always decreases both bias and variance',
        'Bias and variance are generally unrelated to each other',
        'Highly flexible models tend to have low bias and high variance',
        'Highly inflexible models tend to have high bias and low variance'
    ],
    'correct_answer': 'Highly flexible models tend to have low bias and high variance',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_9 = {
    'question': "The training error rate typically _____ as model flexibility increases.",
    'options_list': [
        'increases',
        'decreases',
        'stays the same',
        'first decreases, then increases'
    ],
    'correct_answer': 'decreases',
    'chapter_information': 'ISLR Chapter 2'
}

chapter2_question_10 = {
    'question': "Which approach attempts to directly estimate the conditional distribution of Y given X and classify a given observation to the class with highest estimated probability?",
    'options_list': [
        'Bayes classifier',
        'Linear regression',
        'K-nearest neighbors',
        'Logistic regression'
    ],
    'correct_answer': 'K-nearest neighbors',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_1 = {
    'question': "The total deviation at an observation (xi, yi) is calculated as yi minus y bar.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_2 = {
    'question': "In ordinary least squares, the estimates of slope and intercept do not depend on the sample being used.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_3 = {
    'question': "R squared equals zero implies that X values account for all the variation in the Y values.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_4 = {
    'question': "R squared can take any value from negative infinity to positive infinity.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_5 = {
    'question': "If the scatter plot of Y vs X shows a nonlinear pattern, then we should not change our linear regression model.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_6 = {
    'question': "Autocorrelation is the correlation between each of the ei variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 2'
}

tf_question_7 = {
    'question': "Heteroskedasticity means having constant error variance.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 2'
}

###########ISLR Chapter 3############################
chapter3_question_11 = {
    'question': "Which statement best describes the purpose of the F-statistic in multiple linear regression?",
    'options_list': [
        'It measures the individual impact of each predictor on the response.',
        'It is used to assess the overall significance of the model.',
        'It calculates the residual sum of squares.',
        'It determines the coefficient of determination (R^2).'
    ],
    'correct_answer': 'It is used to assess the overall significance of the model.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_12 = {
    'question': "In the context of multiple linear regression, how is the R^2 statistic interpreted?",
    'options_list': [
        'It indicates the percentage of the response variable variation that is explained by the model.',
        'It represents the residual standard error.',
        'It is the ratio of the total sum of squares to the residual sum of squares.',
        'It measures the correlation between the observed and predicted values of the response variable.'
    ],
    'correct_answer': 'It indicates the percentage of the response variable variation that is explained by the model.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_13 = {
    'question': "What does a large F-statistic in a multiple linear regression model indicate?",
    'options_list': [
        'A strong linear relationship between all predictors and the response.',
        'No relationship between any of the predictors and the response.',
        'High residual variance.',
        'Low correlation between predictors.'
    ],
    'correct_answer': 'A strong linear relationship between all predictors and the response.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_14 = {
    'question': "How does the addition of more predictors to a multiple linear regression model affect the R^2 statistic?",
    'options_list': [
        'It decreases regardless of the new predictors\' significance.',
        'It remains unchanged.',
        'It increases, possibly without improving model validity.',
        'It is directly proportional to the residual standard error.'
    ],
    'correct_answer': 'It increases, possibly without improving model validity.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_15 = {
    'question': "What role does the residual standard error (RSE) play in the interpretation of a multiple linear regression model?",
    'options_list': [
        'It quantifies the lack of fit of the model to the data.',
        'It determines the coefficients of the predictors.',
        'It calculates the F-statistic.',
        'It directly impacts the calculation of R^2.'
    ],
    'correct_answer': 'It quantifies the lack of fit of the model to the data.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_16 = {
    'question': "What does the F-statistic in multiple linear regression help to test?",
    'options_list': [
        'The significance of individual predictors',
        'Whether all regression coefficients are zero',
        'The goodness of fit of the model',
        'The linearity of the relationship between predictors and response'
    ],
    'correct_answer': 'Whether all regression coefficients are zero',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_17 = {
    'question': "Which statement is true regarding the relationship between the t-statistic for individual predictors and the F-statistic in multiple regression?",
    'options_list': [
        'The t-statistic for each predictor is unrelated to the F-statistic.',
        'A significant F-statistic implies all t-statistics are significant.',
        "The square of a predictor's t-statistic equals the F-statistic when including only that predictor.",
        'The F-statistic is the sum of all individual t-statistics squared.'
    ],
    'correct_answer': 'The square of a predictor\'s t-statistic equals the F-statistic when including only that predictor.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_18 = {
    'question': "In the context of variable selection, what does forward selection involve?",
    'options_list': [
        'Starting with all predictors and removing the least significant one at each step',
        'Starting with no predictors and adding one at a time based on significance',
        'Combining forward and backward steps to add and remove predictors',
        'Randomly selecting subsets of predictors to find the best model'
    ],
    'correct_answer': 'Starting with no predictors and adding one at a time based on significance',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_19 = {
    'question': "How does adding more predictors to a model affect the R^2 statistic?",
    'options_list': [
        'It decreases R^2 because of increased complexity.',
        'It does not affect R^2.',
        'It increases R^2, even if the new predictors are not significant.',
        'It resets R^2 to zero before recalculating.'
    ],
    'correct_answer': 'It increases R^2, even if the new predictors are not significant.',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_question_20 = {
    'question': "What is the primary use of an indicator (or dummy) variable in a regression model?",
    'options_list': [
        'To increase the model\'s complexity and flexibility',
        'To represent qualitative data with two levels',
        'To indicate the presence of interaction effects between variables',
        'To serve as a placeholder for missing data'
    ],
    'correct_answer': 'To represent qualitative data with two levels',
    'chapter_information': 'ISLR Chapter 3'
}







###########ISLR Chapter 4############################
chapter4_question_1 = {
    'question': "What is the primary reason logistic regression is preferred over linear regression for a binary response variable?",
    'options_list': [
        'Logistic regression predictions are continuous values.',
        'Linear regression can predict probabilities outside the [0, 1] range.',
        'Logistic regression coefficients are easier to interpret.',
        'Linear regression fits data faster than logistic regression.'
    ],
    'correct_answer': 'Linear regression can predict probabilities outside the [0, 1] range.',
    'chapter_information': 'ISLR Chapter 4'
}

chapter4_question_2 = {
    'question': "In logistic regression, what does the logit function estimate?",
    'options_list': [
        'The probability of the default class',
        'The linear combination of the predictors',
        'The log odds of the outcome variable',
        'The error term variance'
    ],
    'correct_answer': 'The log odds of the outcome variable',
    'chapter_information': 'ISLR Chapter 4'
}

chapter4_question_3 = {
    'question': "Which method is used to estimate the coefficients of a logistic regression model?",
    'options_list': [
        'Least squares estimation',
        'Maximum likelihood estimation',
        'Bayesian estimation',
        'Cross-validation'
    ],
    'correct_answer': 'Maximum likelihood estimation',
    'chapter_information': 'ISLR Chapter 4'
}

chapter4_question_4 = {
    'question': "Why can't linear regression be used for predicting outcomes of a qualitative response variable?",
    'options_list': [
        'Linear regression can only handle numeric predictor variables.',
        'Linear regression models are computationally too complex for qualitative responses.',
        'Linear regression predictions can be negative or greater than 1, which is not interpretable for categorical outcomes.',
        'Linear regression models do not allow for the inclusion of dummy variables.'
    ],
    'correct_answer': 'Linear regression predictions can be negative or greater than 1, which is not interpretable for categorical outcomes.',
    'chapter_information': 'ISLR Chapter 4'
    }

chapter4_question_5 = {
    'question': "What does the logistic function in logistic regression ensure about the predicted probabilities?",
    'options_list': [
        'Predicted probabilities are always multiples of 0.5.',
        'Predicted probabilities are linearly related to the predictors.',
        'Predicted probabilities are constrained between 0 and 1.',
        'Predicted probabilities are independent of the predictors.'
    ],
    'correct_answer': 'Predicted probabilities are constrained between 0 and 1.',
    'chapter_information': 'ISLR Chapter 4'
}

chapter4_question_6 = {
    'question': "How does the inclusion of multiple predictors in a logistic regression model affect its interpretation?",
    'options_list': [
        'It allows for interaction effects between predictors to be modeled directly.',
        'It changes the logistic function to a linear function.',
        'It makes the model interpretation independent of the scale of the predictors.',
        'Each predictor’s effect is interpreted while holding other predictors at a fixed value.'
    ],
    'correct_answer': 'Each predictor’s effect is interpreted while holding other predictors at a fixed value.',
    'chapter_information': 'ISLR Chapter 4'
    }

chapter4_question_7 = {
    'question': "What is the effect of adding more predictors to a logistic regression model?",
    'options_list': [
        'It simplifies the model by reducing the number of parameters.',
        'It decreases the chances of overfitting the model.',
        "It increases the model's complexity and can lead to overfitting.",
        'It has no effect on the model’s performance or interpretability.'
    ],
    'correct_answer': "It increases the model's complexity and can lead to overfitting.",
    'chapter_information': 'ISLR Chapter 4'
}

chapter4_question_8 = {
    'question': "What role does the sigmoid (logistic) function play in logistic regression?",
    'options_list': [
        'It ensures the independence of the predictors.',
        'It linearizes the relationship between predictors and the log odds.',
        'It transforms the log odds of the outcomes into probabilities.',
        'It calculates the coefficients of the predictors directly.'
    ],
    'correct_answer': 'It transforms the log odds of the outcomes into probabilities.',
    'chapter_information': 'ISLR Chapter 4'
    }

chapter4_question_9 = {
    'question': "Why is logistic regression considered a linear model?",
    'options_list': [
        'Because it uses a linear combination of predictors to model the response directly.',
        'Because the decision boundary it creates in the feature space is always a straight line.',
        'Because it models the log odds of the response as a linear function of the predictors.',
        'Because the probabilities it predicts are linear functions of the predictors.'
    ],
    'correct_answer': 'Because it models the log odds of the response as a linear function of the predictors.',
    'chapter_information': 'ISLR Chapter 4'
    }

# chapter4_question_4 = {
#     'question': "Linear Discriminant Analysis (LDA) is primarily used for:",
#     'options_list': [
#         'Estimating the relationship between predictors and a quantitative response',
#         'Predicting a binary outcome based on a set of predictors',
#         'Classifying observations into more than two categories',
#         'Reducing the dimensionality of the feature space'
#     ],
#     'correct_answer': 'Predicting a binary outcome based on a set of predictors',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_5 = {
#     'question': "Which assumption does LDA make about the predictors?",
#     'options_list': [
#         'The predictors follow a multivariate normal distribution with a common covariance matrix.',
#         'The predictors are independent of each other.',
#         'The predictors are normally distributed with different variances for each class.',
#         'The relationship between the predictors and the response is linear.'
#     ],
#     'correct_answer': 'The predictors follow a multivariate normal distribution with a common covariance matrix.',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_6 = {
#     'question': "What is the key difference between LDA and QDA?",
#     'options_list': [
#         'LDA assumes different covariance matrices for each class, while QDA assumes a common covariance matrix.',
#         'LDA can only be used for binary classification, whereas QDA can be used for multi-class classification.',
#         'LDA assumes a common covariance matrix for all classes, while QDA allows for class-specific covariance matrices.',
#         'QDA is computationally less intensive than LDA.'
#     ],
#     'correct_answer': 'LDA assumes a common covariance matrix for all classes, while QDA allows for class-specific covariance matrices.',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_7 = {
#     'question': "Which of the following statements about the naive Bayes classifier is true?",
#     'options_list': [
#         'It assumes that predictors within each class are dependent on each other.',
#         'It can only be applied when the predictors are normally distributed.',
#         'It assumes that all predictors within each class are independent.',
#         'It requires a larger amount of data to estimate the parameters accurately compared to LDA and QDA.'
#     ],
#     'correct_answer': 'It assumes that all predictors within each class are independent.',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_8 = {
#     'question': "Why might one prefer QDA over LDA?",
#     'options_list': [
#         'When the assumption of a common covariance matrix across all classes is strongly violated.',
#         'When the number of predictors p is much larger than the number of observations n.',
#         'When computational efficiency is the primary concern.',
#         'When the classes are linearly separable.'
#     ],
#     'correct_answer': 'When the assumption of a common covariance matrix across all classes is strongly violated.',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_9 = {
#     'question': "The naive Bayes classifier is especially useful in:",
#     'options_list': [
#         'Situations where predictors are highly correlated.',
#         'Settings where n is large relative to p.',
#         'Scenarios where the assumption of independent predictors is reasonable.',
#         'When the data does not have a clear classification boundary.'
#     ],
#     'correct_answer': 'Scenarios where the assumption of independent predictors is reasonable.',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_question_10 = {
#     'question': "In the context of classification, a higher value of K in K-nearest neighbors (KNN) generally results in:",
#     'options_list': [
#         'Higher flexibility and lower bias.',
#         'Higher variance and lower bias.',
#         'Lower flexibility and higher bias.',
#         'Lower variance and higher flexibility.'
#     ],
#     'correct_answer': 'Lower flexibility and higher bias.',
#     'chapter_information': 'ISLR Chapter 4'
# }

chapter4_tf_question_1 = {
    'question': "Logistic regression directly models the probability Pr(Y=k|X=x) using the logistic function for binary response classes.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 4'
}

# chapter4_tf_question_2 = {
#     'question': "LDA assumes that the distribution of predictors X is normal within each class and that each class has its own covariance matrix.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_tf_question_3 = {
#     'question': "QDA allows for class-specific covariance matrices, making it more flexible than LDA.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'True',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_tf_question_4 = {
#     'question': "Naive Bayes classifier assumes that within each class, the predictors are independent.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'True',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_tf_question_5 = {
#     'question': "The naive Bayes classifier can only be applied when the predictors are normally distributed.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_tf_question_6 = {
#     'question': "In QDA, the decision boundary can only be linear.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'ISLR Chapter 4'
# }

# chapter4_tf_question_7 = {
#     'question': "LDA is preferred over QDA when the assumption of a common covariance matrix across classes is strongly violated.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'ISLR Chapter 4'
# }

chapter3_tf_question_8 = {
    'question': "Odds are defined as the probability that an event will happen divided by the probability that it will not happen.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_9 = {
    'question': "In logistic regression, increasing X by one unit changes the log odds of the outcome by exactly the coefficient of X.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_10 = {
    'question': "A logistic regression model can predict probabilities outside the [0, 1] range.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_11 = {
    'question': "The logistic function is used in logistic regression to ensure the output is bounded between 0 and 1.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_12 = {
    'question': "Logistic regression is only suitable for datasets where the response variable is continuous.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_13 = {
    'question': "The coefficients in a logistic regression model can be interpreted in the same way as those in a linear regression model.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'ISLR Chapter 3'
}

chapter3_tf_question_14 = {
    'question': "Sensitivity, also known as the true positive rate, measures the proportion of actual positives correctly identified.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'ISLR Chapter 3'
}

########################'week_5_Program Evaluation and the Difference in Difference Estimator#######
week5_question_1 = {
    'question': "What fundamental assumption underlies the Difference in Differences (DiD) approach to program evaluation?",
    'options_list': [
        'Treatment groups receive the intervention randomly.',
        'Control groups have identical characteristics to treatment groups.',
        'Parallel trends assumption, where in the absence of treatment, the paths of outcomes for treated and untreated units would have followed the same trend over time.',
        'All units within the treatment and control groups are affected uniformly by the intervention.'
    ],
    'correct_answer': 'Parallel trends assumption, where in the absence of treatment, the paths of outcomes for treated and untreated units would have followed the same trend over time.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_question_2 = {
    'question': "Which of the following best describes the Difference in Differences (DiD) estimator?",
    'options_list': [
        'A statistical method that compares the pre-treatment and post-treatment changes in outcomes within the treatment group only.',
        'A technique that assesses the effect of a treatment by analyzing the difference in outcomes before and after the treatment, without a control group.',
        'An approach that compares the changes in outcomes over time between treatment and control groups to estimate the treatment effect.',
        'A method that requires randomized control trials as a precondition for its application.'
    ],
    'correct_answer': 'An approach that compares the changes in outcomes over time between treatment and control groups to estimate the treatment effect.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_1 = {
    'question': "What does the F-statistic in multiple linear regression test for?",
    'options_list': [
        'The overall significance of the model',
        'The significance of individual predictors',
        'The linearity of the relationship between predictors and response',
        'None of the above'
    ],
    'correct_answer': 'The overall significance of the model',
    'chapter_information': 'Week 5 Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_2 = {
    'question': "In the context of program evaluation using Difference in Difference (DiD) estimator, what assumption is crucial for its validity?",
    'options_list': [
        'The parallel trends assumption',
        'The homoscedasticity assumption',
        'The independence of errors assumption',
        'The normal distribution of errors assumption'
    ],
    'correct_answer': 'The parallel trends assumption',
    'chapter_information': 'Week 5 Program Evaluation and the Difference in Difference Estimator'
}
week5_tf_question_1 = {
    'question': "The Difference in Difference (DiD) estimator is used to assess the impact of a program or treatment by comparing the pre-treatment and post-treatment changes in outcomes between a treatment group and a control group.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_tf_question_2 = {
    'question': "For the DiD estimator to provide an unbiased estimate of the treatment effect, it is necessary for the treatment and control groups to have identical pre-treatment trends.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_tf_question_3 = {
    'question': "The parallel trends assumption implies that, in the absence of treatment, the difference between the treatment and control groups’ outcomes would have remained constant over time.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_tf_question_4 = {
    'question': "The DiD estimator is biased if there exist permanent differences in the outcome variable between the treatment and control groups that are not accounted for.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_tf_question_5 = {
    'question': "The DiD estimator can only be applied in experimental settings where individuals are randomly assigned to treatment and control groups.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_6 = {
    'question': "What does the F-statistic in multiple linear regression help to determine?",
    'options_list': [
        'The individual significance of each predictor in the model.',
        'The overall significance of the model.',
        'The correlation coefficient between the predictors and the response.',
        'The residual standard error of the regression model.'
    ],
    'correct_answer': 'The overall significance of the model.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_7 = {
    'question': "How is the R^2 statistic interpreted in the context of a linear regression model?",
    'options_list': [
        'It represents the residual standard error of the model.',
        'It indicates the percentage of the variance in the response that is explained by the model.',
        'It measures the correlation between the response and predictors.',
        'It quantifies the slope of the regression line.'
    ],
    'correct_answer': 'It indicates the percentage of the variance in the response that is explained by the model.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_8 = {
    'question': "What is the purpose of using dummy variables in a regression model?",
    'options_list': [
        "To increase the model's complexity and predictive power.",
        'To account for non-linear relationships between variables.',
        'To include qualitative predictors in the regression model.',
        'To reduce the residual standard error of the model.'
    ],
    'correct_answer': 'To include qualitative predictors in the regression model.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_9 = {
    'question': "Which of the following best describes the relationship between the F-statistic and the p-value in a regression model?",
    'options_list': [
        'A high F-statistic and a high p-value indicate a strong relationship between predictors and response.',
        'A low F-statistic and a low p-value suggest the model is not significant.',
        'A high F-statistic and a low p-value suggest the model is significant.',
        'The F-statistic and p-value are unrelated measures of model fit.'
    ],
    'correct_answer': 'A high F-statistic and a low p-value suggest the model is significant.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

week5_mpc_question_10 = {
    'question': "In the context of regression analysis, what does adding a predictor to a model always result in with respect to R^2?",
    'options_list': [
        'An increase in R^2.',
        'A decrease in R^2.',
        'No change in R^2.',
        'R^2 becomes negative.'
    ],
    'correct_answer': 'An increase in R^2.',
    'chapter_information': 'week_5_Program Evaluation and the Difference in Difference Estimator'
}

########################week_6_An Evaluation of Risk Metrics#######

week6_mpc_question_1 = {
    'question': "What is the primary purpose of using risk metrics in portfolio management?",
    'options_list': [
        'To eliminate all forms of financial risk.',
        'To precisely predict future portfolio performance.',
        'To quantify the uncertainty of outcomes and aid in portfolio construction and performance assessment.',
        'To guarantee a certain level of returns on investments.'
    ],
    'correct_answer': 'To quantify the uncertainty of outcomes and aid in portfolio construction and performance assessment.',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_2 = {
    'question': "Which of the following is considered an absolute risk measure?",
    'options_list': [
        'Beta',
        'Sharpe Ratio',
        'Standard Deviation',
        'Tracking Error'
    ],
    'correct_answer': 'Standard Deviation',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_3 = {
    'question': "Historical Value-at-Risk (VaR) is based on:",
    'options_list': [
        'The average return of the worst-case scenarios.',
        'A security’s worst results over a given period.',
        'The median return of the investment portfolio.',
        'The expected return calculated from the asset’s beta.'
    ],
    'correct_answer': 'A security’s worst results over a given period.',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_4 = {
    'question': "Which risk metric is most concerned with the frequency of negative returns?",
    'options_list': [
        'Shortfall Risk',
        'Risk of Loss',
        'Value-at-Risk (VaR)',
        'Standard Deviation'
    ],
    'correct_answer': 'Risk of Loss',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_5 = {
    'question': "The Sharpe Ratio measures:",
    'options_list': [
        'An asset’s return above or below that of a benchmark.',
        'The risk-adjusted return of a portfolio or security.',
        'The standard deviation of excess return.',
        'The magnitude of an investment’s fluctuations relative to the market.'
    ],
    'correct_answer': 'The risk-adjusted return of a portfolio or security.',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_8 = {
    'question': "Value at Risk (VaR) measures:",
    'options_list': [
        'The maximum expected loss over a given time period at a specific confidence level.',
        'The average return of a portfolio over its entire history.',
        'The volatility of a portfolio compared to its benchmark.',
        'The return on investment for the top-performing assets in a portfolio.'
    ],
    'correct_answer': 'The maximum expected loss over a given time period at a specific confidence level.',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_mpc_question_9 = {
    'question': "Conditional Value at Risk (CVaR) is:",
    'options_list': [
        'The same as Value at Risk, but calculated using conditional probabilities.',
        'The expected loss exceeding VaR in the worst-case scenarios.',
        'A measure that ignores the tail risk beyond the VaR threshold.',
        'Calculated without considering the distribution of returns.'
    ],
    'correct_answer': 'The expected loss exceeding VaR in the worst-case scenarios.',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_tf_question_1 = {
    'question': "Beta is a measure of an asset's volatility in comparison to the overall market's volatility.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_tf_question_2 = {
    'question': "The Sharpe Ratio can be negative if the portfolio's return is less than the risk-free rate.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}

week6_tf_question_3 = {
    'question': "Standard deviation is a risk metric that penalizes both upside and downside volatility equally.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'week_6_An Evaluation of Risk Metrics'
}



# ########################week_7_SSRN-id481881#######
# week7_mpc_question_1 = {
#     'question': "What fundamental concept is discussed in relation to risk and return in financial markets?",
#     'options_list': [
#         'Higher expected returns are associated with lower risk.',
#         'Risk and return are unrelated in efficient markets.',
#         'Higher expected returns require taking higher risk.',
#         'All assets have the same risk-return profile.'
#     ],
#     'correct_answer': 'Higher expected returns require taking higher risk.',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_2 = {
#     'question': "Which models are highlighted for explaining the relationship between risk and expected returns?",
#     'options_list': [
#         'The CAPM and the Fama-French Three-Factor Model',
#         'The Efficient Market Hypothesis and Modern Portfolio Theory',
#         'Dividend Discount Model and Arbitrage Pricing Theory',
#         'Black-Scholes Model and Monte Carlo Simulations'
#     ],
#     'correct_answer': 'The CAPM and the Fama-French Three-Factor Model',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_3 = {
#     'question': "How is volatility commonly measured in the context of risk?",
#     'options_list': [
#         'Beta coefficient',
#         'Sharpe Ratio',
#         'Standard deviation of returns',
#         'Alpha coefficient'
#     ],
#     'correct_answer': 'Standard deviation of returns',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_4 = {
#     'question': "What does diversification primarily aim to reduce?",
#     'options_list': [
#         'Systematic risk',
#         'Unsystematic risk',
#         'Interest rate risk',
#         'Currency risk'
#     ],
#     'correct_answer': 'Unsystematic risk',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_5 = {
#     'question': "What does the beta coefficient in the CAPM represent?",
#     'options_list': [
#         'The expected return of a portfolio',
#         'The volatility of an asset relative to the overall market',
#         'The risk-free rate of return',
#         "The portfolio's alpha"
#     ],
#     'correct_answer': 'The volatility of an asset relative to the overall market',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_8 = {
#     'question': "Which model expands CAPM by adding company-specific risk factors?",
#     'options_list': [
#         'The Efficient Market Hypothesis',
#         'The Fama-French Three-Factor Model',
#         'The Arbitrage Pricing Theory',
#         'The Dividend Discount Model'
#     ],
#     'correct_answer': 'The Fama-French Three-Factor Model',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_9 = {
#     'question': "What does the beta coefficient in CAPM represent?",
#     'options_list': [
#         'The risk-free rate of return',
#         'The total market return',
#         "The measure of an asset's volatility in relation to the market",
#         'The expected return of the market minus the risk-free rate'
#     ],
#     'correct_answer': 'The measure of an asset\'s volatility in relation to the market',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_10 = {
#     'question': "What is the primary purpose of the SMB (Small Minus Big) factor in the Fama-French Three-Factor Model?",
#     'options_list': [
#         'To account for the size premium in small-cap stocks',
#         'To measure the risk-free rate of return',
#         'To calculate the market risk premium',
#         'To determine the value premium in high book-to-market stocks'
#     ],
#     'correct_answer': 'To account for the size premium in small-cap stocks',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_11 = {
#     'question': "How is alpha (α) interpreted in the context of CAPM and the Fama-French Three-Factor Model?",
#     'options_list': [
#         'As the expected market return',
#         'As the risk-free rate',
#         "As the portfolio's return in excess of what is predicted by the model",
#         'As the covariance between the asset and market returns'
#     ],
#     'correct_answer': 'As the portfolio\'s return in excess of what is predicted by the model',
#     'chapter_information': 'week_7_SSRN-id481881'
# }

# week7_mpc_question_12 = {
#     'question': "Which of the following best describes the HML (High Minus Low) factor?",
#     'options_list': [
#         'It measures the premium for investing in stocks with high market capitalizations.',
#         'It represents the difference in returns between high and low dividend yield stocks.',
#         'It captures the value premium of high book-to-market stocks over low book-to-market stocks.',
#         'It quantifies the excess return of small-cap stocks over large-cap stocks.'
#     ],
#     'correct_answer': 'It captures the value premium of high book-to-market stocks over low book-to-market stocks.',
#     'chapter_information': 'week_7_SSRN-id481881'
# }



# #####################week 8#############

# week8_mpc_question_1 = {
#     'question': "What is factor investing?",
#     'options_list': [
#         'Investing in a portfolio consisting solely of government bonds',
#         'Selecting investments based on macroeconomic trends',
#         'Investing based on attributes that explain risk and return of securities',
#         'Focusing on short-term trading strategies to maximize returns'
#     ],
#     'correct_answer': 'Investing based on attributes that explain risk and return of securities',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_mpc_question_2 = {
#     'question': "Which of the following is NOT identified as an equity risk premia factor?",
#     'options_list': [
#         'Value',
#         'Low Volatility',
#         'High Yield',
#         'Market Capitalization'
#     ],
#     'correct_answer': 'Market Capitalization',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_mpc_question_3 = {
#     'question': "What is a primary challenge in factor investing according to the document?",
#     'options_list': [
#         'Identifying factors that influence stock prices',
#         'The cyclicality of factor returns and their periods of underperformance',
#         'Determining the correct timing for buying and selling assets',
#         'Calculating the exact risk premium for each factor'
#     ],
#     'correct_answer': 'The cyclicality of factor returns and their periods of underperformance',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_mpc_question_4 = {
#     'question': "How does diversification impact factor investing?",
#     'options_list': [
#         'Reduces the need to identify individual factors',
#         'Increases the risk associated with individual factors',
#         'Helps mitigate specific factor risks and enhances portfolio resilience',
#         'Has no significant impact on factor investing outcomes'
#     ],
#     'correct_answer': 'Helps mitigate specific factor risks and enhances portfolio resilience',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_mpc_question_5 = {
#     'question': "What role does quantitative analysis play in factor investing?",
#     'options_list': [
#         'Primarily used for marketing to potential investors',
#         'Serves as the basis for selecting and weighting investments according to identified factors',
#         'Used exclusively for risk management and not for portfolio construction',
#         'It is discouraged due to its complexity and reliance on historical data'
#     ],
#     'correct_answer': 'Serves as the basis for selecting and weighting investments according to identified factors',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_mpc_question_6 = {
#     'question': "According to the document, what is a significant benefit of factor investing?",
#     'options_list': [
#         'Guarantees higher returns than the market portfolio',
#         'Offers transparency and a systematic approach to investing',
#         'Eliminates the need for active management',
#         'Reduces investment costs to zero'
#     ],
#     'correct_answer': 'Offers transparency and a systematic approach to investing',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_tf_question_1 = {
#     'question': "Factor investing focuses solely on maximizing short-term returns.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_tf_question_2 = {
#     'question': "Value and momentum are considered fundamental factors in factor investing.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'True',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }

# week8_tf_question_3 = {
#     'question': "Diversification in factor investing can eliminate all investment risk.",
#     'options_list': ['True', 'False'],
#     'correct_answer': 'False',
#     'chapter_information': 'week_8_Foundations_of_Factor_Investing'
# }














####Additional Questions#####
week5_mpc_question_1 = {
    'question': "What does the F-statistic in multiple linear regression test for?",
    'options_list': [
        'The overall significance of the model',
        'The significance of individual predictors',
        'The linearity of the relationship between predictors and response',
        'None of the above'
    ],
    'correct_answer': 'The overall significance of the model',
    'chapter_information': 'N/A'
}

week5_mpc_question_2 = {
    'question': "In the context of program evaluation using Difference in Difference (DiD) estimator, what assumption is crucial for its validity?",
    'options_list': [
        'The parallel trends assumption',
        'The homoscedasticity assumption',
        'The independence of errors assumption',
        'The normal distribution of errors assumption'
    ],
    'correct_answer': 'The parallel trends assumption',
    'chapter_information': 'N/A'
}

week5_mpc_question_3 = {
    'question': "How can qualitative variables be included in a regression model?",
    'options_list': [
        'By transforming them into quantitative measures',
        'Using interaction terms',
        'Creating dummy variables',
        'They cannot be included in a regression model'
    ],
    'correct_answer': 'Creating dummy variables',
    'chapter_information': 'N/A'
}

week5_mpc_question_4 = {
    'question': "Which of the following best describes the purpose of using control variables in DiD estimation?",
    'options_list': [
        'To increase the accuracy of the treatment effect estimation',
        'To control for variables that may affect the treatment but not the outcome',
        'To account for variables that influence both the treatment and the outcome',
        'To directly measure the effect of the treatment on the outcome'
    ],
    'correct_answer': 'To account for variables that influence both the treatment and the outcome',
    'chapter_information': 'N/A'
}

week5_mpc_question_5 = {
    'question': "What is an indicator variable in the context of regression analysis?",
    'options_list': [
        'A variable that indicates the presence of multicollinearity',
        'A variable that measures the strength of the relationship between X and Y',
        'A dummy variable used to represent qualitative data',
        'A variable used to indicate the model fit'
    ],
    'correct_answer': 'A dummy variable used to represent qualitative data',
    'chapter_information': 'N/A'
}
week4_tf_question_1 = {
    'question': "Odds are defined as the probability of an event occurring divided by the probability that it will not happen.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'N/A'
}

week4_tf_question_2 = {
    'question': "In logistic regression, increasing X by one unit changes the log odds of the outcome by exactly the coefficient of X.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'N/A'
}

week4_tf_question_3 = {
    'question': "A logistic regression model can predict probabilities outside the [0, 1] range.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'N/A'
}

week4_tf_question_4 = {
    'question': "The logistic function is used in logistic regression to ensure the output is bounded between 0 and 1.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'N/A'
}

week4_tf_question_5 = {
    'question': "Logistic regression is only suitable for datasets where the response variable is continuous.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'N/A'
}

week4_tf_question_6 = {
    'question': "The coefficients in a logistic regression model can be interpreted in the same way as those in a linear regression model.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'N/A'
}

week4_tf_question_7 = {
    'question': "Sensitivity, also known as the true positive rate, measures the proportion of actual positives correctly identified by the model.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'N/A'
}

READING_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        READING_MPC_QUESTIONS.append(value)

READING_MPC_QUESTIONS = READING_MPC_QUESTIONS[:-1]
