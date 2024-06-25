# SA1
question_1 = {
    'question': "In Ordinary Least Squares we are trying to minimize:",
    'options_list': ['The Median Absolute Error', 'The Mean Absolute Error', 'The Sum of Squared Error', 'The Root Mean Squared Error'],
    'correct_answer': 'The Sum of Squared Error',
    'chapter_information': 'Week 1, page 18 slide 1'
}

question_2 = {
    'question': "An indicator variable is sometimes referred to as a:",
    'options_list': ['Hyperparameter', 'Dummy variable', 'Interaction variable', 'Continuous predictor variable'],
    'correct_answer': 'Dummy variable',
    'chapter_information': 'Week 2, page 9 slide 2'
}

question_3 = {
    'question': "Which of the following is an example of an Interaction Term?",
    'options_list': ['Height*Gender', 'Height^2', 'Height - Gender', 'Height + Gender'],
    'correct_answer': 'Height*Gender',
    'chapter_information': 'Week 2, page 18 slide 1'
}

question_4 = {
    'question': "If your dataset has a column that contained one of three states for each observation ('New York', 'California', 'Hawaii'), what would be the best way to code them for a regression model with one-hot encoding?",
    'options_list': ['1 for New York, 2 for California, 3 for Hawaii', 'Assign a unique identifier for each state', 'Use binary indicators for each state', 'Encode each state with a different color'],
    'correct_answer': 'Use binary indicators for each state',
    'chapter_information': 'Week 2, page 24 slide 2'
}

# question_5 = {
#     'question': "How much more would a person in California expect to pay per day vs a person in New York of the same age, given the regression model and coefficients?",
#     'options_list': ['$5', '$-5', '$10', '$-15'],
#     'correct_answer': '$10',
#     'chapter_information': 'Week 2, Page 27 slide 2'
# }

question_6 = {
    'question': "In a linear regression model with one qualitative (categorical) predicting variable with 4 values, we need to include 4 dummy variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Week 2, page 20 slide 2'
}

# question_7 = {
#     'question': "Based on the following regression model summary (Note: the base case is Age = Young), what is the Amount Spent by a Middle-aged customer if his/her salary is 10000?",
#     'options_list': ['20 – 6.12', '20 – 6.12 - 4.81', '20 – 6.12 +23.28', '20'],
#     'correct_answer': '20 – 6.12 - 4.81',
#     'chapter_information': 'Lesson 2 / Video 4 / Slides 1 – 4'
# }

question_8 = {
    'question': "An interaction term is used to model how the synergies between multiple variables impact the response variable.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 6 – 9'
}

# SA2
sa2_question_1 = {
    'question': "Select the equation that can be used for a linear-log model:",
    'options_list': ['Y = b0 + b1 * X', 'Y = b0 + b1 * log(X)', 'log(Y) = b0 + b1 * X', 'log(Y) = b0 + b1 * log(X)'],
    'correct_answer': 'Y = b0 + b1 * log(X)',
    'chapter_information': 'Module 3'
}

sa2_question_2 = {
    'question': "Select the equation that can be used for a log-log model:",
    'options_list': ['Y = b0 + b1 * X', 'Y = b0 + b1 * log(X)', 'log(Y) = b0 + b1 * X', 'log(Y) = b0 + b1 * log(X)'],
    'correct_answer': 'log(Y) = b0 + b1 * log(X)',
    'chapter_information': 'Module 3'
}

sa2_question_3 = {
    'question': "In regard to a linear-log model, increasing X by 1% is almost equivalent to which of the following:",
    'options_list': ['Increasing log(X) by 0.01 units', 'Decreasing (natural) log(X) by 0.01 units', 'Increasing (natural) log(X) by 0.01 units', 'Increasing x by one unit will increase (natural) log(y) by b1 units', 'None of the above'],
    'correct_answer': 'Increasing (natural) log(X) by 0.01 units',
    'chapter_information': 'Module 3'
}

sa2_question_4 = {
    'question': "Increasing (natural) log(X) by 0.01 leads to increasing (natural) log(Y) by b1 * 0.01 units best describes which model?",
    'options_list': ['Linear-Linear', 'Linear-Log', 'Log-Linear', 'Log-Log'],
    'correct_answer': 'Log-Log',
    'chapter_information': 'Module 3'
}

sa2_question_5 = {
    'question': "Which of the following results from the residual analysis of a linear regression model is not a clear signal for the need to explore non-linear models?",
    'options_list': ['The residuals vs. fitted values plot indicates that the model has heteroscedasticity',
                     'the QQ-plot suggest that there is non-linearity',
                     'The residuals suffer from non-constant variance',
                     'The residuals appear to be normally distributed.'],
    'correct_answer': 'The residuals appear to be normally distributed.',
    'chapter_information': 'Module 3, slide 4'
}

sa2_question_6 = {
    'question': "For a non-linear model salary = b0 + b1*log (years of experience). If b1 = 5122, which of the following statements is correct?",
    'options_list': ['When years of experience increases by 1, salary increases (on average) by $5122.', 'When years of experience decreases by 1, salary increases (on average) by $5122.',\
        'When years of experience increases by 1%, salary increases (on average) by $51.22.', 'When years of experience decreases by log (1), salary increases (on average) by $51.22.'],
    'correct_answer': 'When years of experience increases by 1%, salary increases (on average) by $51.22.',
    'chapter_information': 'Module 3, slide 8'
}

sa2_question_7 = {
    'question': "Which of the following could be a reason for applying log transformation on a dataset?",
    'options_list': ['To make a distribution more normal', 'To make the variance more constant', 'To get a better fit in the model – i.e. increase R-Squared', 'All of the above'],
    'correct_answer': 'All of the above',
    'chapter_information': 'Module 3, slide 16'
}

sa2_question_8 = {
    'question': "Consider the equation Cost = 4.3 + 6.89 *log(length). How should the length be increased such that the cost increases by 6.89 units?",
    'options_list': ['Increase length by 1 unit', 'Increase length by e units', 'Multiply length by e units', 'Increase length by 6.89 units'],
    'correct_answer': 'Multiply length by e units',
    'chapter_information': 'Module 3'
}

sa2_question_9 = {
    'question': "Consider the equation 3.45 log (Y) = 2.33 + 87.6 log(X). What is the elasticity?",
    'options_list': ['2.33', '87.6', '25.39', '3.45'],
    'correct_answer': '25.39',
    'chapter_information': 'Module 3, page 14'
}

sa2_question_10 = {
    'question': "Which of the following statements is FALSE about Polynomial Regression?",
    'options_list': [
        "Polynomial provides a better approximation of the relationship between the dependent and independent variable",
        "Presence of outliers can greatly influence results of the non-linear analysis",
        "The fitted model is more reliable when it is built on a larger sample size n",
        "It allows for an isolated interpretation of coefficients of non-linear variables"
    ],
    'correct_answer': "It allows for an isolated interpretation of coefficients of non-linear variables",
    'chapter_information': 'Module 3, page 19'
}

#sa 3 is all R

#sa4
sa4_question_1 = {
    'question': "What is the orthogonality assumption in OLS, taking Y = a + bX as the model, and error term is e?",
    'options_list': ['Correlation(X, X) = 0', 'Correlation(X, e) = 0', 'Correlation(e, X) = 1', 'None of the above'],
    'correct_answer': 'Correlation(X, e) = 0',
    'chapter_information': 'Week 5, Lesson 2'
}

sa4_question_2 = {
    'question': "While calculating a difference in difference, we run a regression which is as follows: lm( y ~ d1 +d2 + d3) where d1 and d2 are dummy variables and d3 is their interaction term. What is the difference in difference estimator?",
    'options_list': ['a+b+c+d', '(d-c)-(b-a)', 'a', 'd'],
    'correct_answer': 'd',
    'chapter_information': 'Module 5, Slide 20'
}

sa4_question_3 = {
    'question': "We want to observe a column 'y' in dataset. We divide the observations into 2 parts, where y_0 is the set of observations of control group and y_1 is the set of observations of treatment group. What is the difference estimator given by?",
    'options_list': ['mean(y_1) – mean(y_0)', 'Covariance(y_1, y_2)', '1 – mean(y_1)/mean(y_2)', 'Var(y_2)'],
    'correct_answer': 'mean(y_1) – mean(y_0)',
    'chapter_information': 'Module 5, Slide 8'
}

sa4_question_4 = {
    'question': "True or False: The weakest linear relationship is indicated by a correlation coefficient equal to -1.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'General knowledge'
}

sa4_question_5 = {
    'question': "Which of the following is an example of a natural experiment?",
    'options_list': ['One state, but not others, increases income tax', 'Changing store policy to allow online orders to be picked up in any store', 'A mobile carrier implements an unlimited data plan open to all customers', 'Testing new plant growth in different soil conditions in a lab'],
    'correct_answer': 'One state, but not others, increases income tax',
    'chapter_information': 'Definition in Slide 15'
}

sa4_question_6 = {
    'question': "Researchers compare the average change over time of the independent variable for the treatment group to the average change over time of the independent variable for the control group. This comparison is called difference in difference.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Definition in Slide 15'
}

sa4_question_7 = {
    'question': "Which of the following is an indication that there is random assignment in an experiment?",
    'options_list': ['The coefficients of the regression model are all approximately equal to 1.', 'The intercept of the regression model is equal to 0.', 'The coefficients of the regression model are all significant.', 'The coefficients of the regression model are all insignificant.'],
    'correct_answer': 'The coefficients of the regression model are all insignificant.',
    'chapter_information': 'Module 5, Lesson 4'
}

sa4_question_8 = {
    'question': "The range of values of correlation is:",
    'options_list': ['[0,1]', '[-1,0]', '[-1,1]', '[-∞,∞]'],
    'correct_answer': '[-1,1]',
    'chapter_information': 'General knowledge'
}

sa4_question_9 = {
    'question': "To estimate the causal impact of a treatment, we need to compare the treatment outcome to the:",
    'options_list': ['Counterpoint', 'Counterfactual', 'Correlation', 'Confusion Matrix'],
    'correct_answer': 'Counterfactual',
    'chapter_information': 'Module 5, Lesson 5'
}

sa4_question_10 = {
    'question': "How can selection bias be avoided?",
    'options_list': ['Randomized controlled experiment', 'Natural experiment', 'Add control variables', 'All the above'],
    'correct_answer': 'All the above',
    'chapter_information': 'Week 5, slide 6'
}



### hw1
hw1_question_1 = {
    'question': "Which of the following indicate that the result from a simple linear regression model could be potentially misleading?",
    'options_list': [
        'The dependent and the independent variable show a linear pattern.',
        'The error terms exhibit homoscedasticity',
        'The error terms follow a normal distribution',
        'The nth error term could be predicted with e_n = 0.91*e_{n-1}'
    ],
    'correct_answer': 'The nth error term could be predicted with e_n = 0.91*e_{n-1}',
    'chapter_information': 'Homework 1'
}

hw1_question_2 = {
    'question': "Consider a multiple linear regression model: Y = 0.55 + 0.93*x1 + 1.88*x2. Which of the following interpretation of the coefficients is correct?",
    'options_list': [
        'A unit increase in x1 is associated with an 0.93 increase in Y.',
        'Y is predicted to be equal to 0.55 when both x1 and x2 take the value of 1',
        'A unit increase in x2 is associated with a 1.88 increase in Y, keeping all else constant.',
        'A 0.93 increase in x1 is associated with a 1.88 increase in x2'
    ],
    'correct_answer': 'A unit increase in x2 is associated with a 1.88 increase in Y, keeping all else constant.',
    'chapter_information': 'Homework 1'
}

hw1_question_3 = {
    'question': "When testing our predictive variables for Multicollinearity we create a model in R of lm(pred1 ~ pred2 + pred3, data = dataset) and we get an R Squared of 0.85. What is the VIF for pred1?",
    'options_list': [
        '0.85',
        '0.15',
        '6.667',
        '0.5405'
    ],
    'correct_answer': '6.667',
    'chapter_information': 'Homework 1'
}

hw1_question_4 = {
    'question': "Consider a linear regression model estimating the fuel efficiency of a car in terms miles per gallon of gas (mpg) based on its origin (region A, B or C) \
        and number of cylinders with the following formula: mpg = b0 + b1*RegionB + b2*RegionC + b3*Cylinders. The estimated values of the regression coefficients are provided below: b0 = 40.7, b1 = -0.91, b2 = 2.66, b3 = -3.15. Based on this model, \
            if X is the mpg of a car with 4 cylinders originated from region B, and Z is the mpg of a car with 3 cylinders originated from region A, what is the value of X - Z:",
    'options_list': [
        '-0.91',
        '-3.15',
        '-4.06',
        '-6.72'
    ],
    'correct_answer': '-4.06',
    'chapter_information': 'Homework 1'
}

hw1_question_5 = {
    'question': "True or False, when you create a linear regression model with factors (i.e. male, female), R converts those factors into dummy variables?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'chapter_information': 'Homework 1'
}

hw1_question_6 = {
    'question': "From the following regression model: Gold_Price_Per_oz = B0 + B1*M2+B2*VIX+B3*War, where M2 is a continuous variable of the M2 money supply, VIX is a continuous variable of the VIX index, and War is a categorical variable (0 is Time period at peace, 1 is Time period at war). Which of the following would be a part of the base case conditions?",
    'options_list': [
        'Time period at war',
        'Time period at peace',
        'A high VIX index',
        'Period of inflation'
    ],
    'correct_answer': 'Time period at peace',
    'chapter_information': 'Homework 1'
}

hw1_question_7 = {
    'question': "Given the following model: price = b0 + b1*lotsize + b2*lotsize^2, how can one interpret the coefficients? Select the best answer.",
    'options_list': [
        'Price increases by b0 + b1 + b2^2 when lotsize is increased by 1 unit.',
        'A quadratic model does not allow for an isolated interpretation of coefficients.',
        'Price increases by b1 when lotsize is increased by 1 unit.',
        'Price increases by b2 when lotsize is increased by 1 unit.'
    ],
    'correct_answer': 'A quadratic model does not allow for an isolated interpretation of coefficients.',
    'chapter_information': 'Homework 1'
}

hw1_question_8 = {
    'question': "Select the model approximation that best matches the following statement: 'As X increases by 1%, Y increases by (b1/100) units, holding all other factors constant.'",
    'options_list': [
        'Y = b0 + b1*X',
        'Y = b0 + b1*log(X)',
        'log(Y) = b0 + b1*X',
        'log(Y) = b0 + b1*log(X)'
    ],
    'correct_answer': 'log(Y) = b0 + b1*X',
    'chapter_information': 'Homework 1'
}

hw1_question_9 = {
    'question': "Assume that you have concluded to use a log transformation on your data to model a relationship. However, on investigating the dataset, you found negative and zero values. How will you proceed?",
    'options_list': [
        'Throw out the data points which are negative or zero',
        'Use Log(x+1), where x is the variable you want to transform',
        'Use log(x + c +1), where c is the absolute value of the most negative number',
        'Use log(10 * x)'
    ],
    'correct_answer': 'Use log(x + c +1), where c is the absolute value of the most negative number',
    'chapter_information': 'Homework 1'
}

hw1_question_10 = {
    'question': "If we decrease the cutoff value and then consider that the number of true positives, true negatives, false positives, and false negatives changes, which of the following is true?",
    'options_list': [
        'False positive rate decreases',
        'Sensitivity increases',
        'Specificity increases',
        'None of the above'
    ],
    'correct_answer': 'Sensitivity increases',
    'chapter_information': 'Homework 1'
}

hw1_question_12 = {
    'question': "Which of the following case is referred to Type II error?",
    'options_list': [
        'Null is false and we reject it.',
        'Null is True, but we fail to reject it.',
        'Null is True but we mistakenly reject it.',
        'Null is false but we fail to reject it.'
    ],
    'correct_answer': 'Null is false but we fail to reject it.',
    'chapter_information': 'Homework 1'
}
######## hw2
hw2_part1_q1 = {
    'question': "Given a complete deck of cards, the probability of drawing the Ace of Diamonds is 1/52. Based on this probability, what are the odds for this event?",
    'options_list': ['1/51', '1/52', '51/1', '52/1'],
    'correct_answer': '1/51',
    'chapter_information': 'Odds(for) = p/(1−p) = (1/52)/(1−1/52) = 1/51'
}

hw2_part1_q2 = {
    'question': "Which of the following is the reason why linear regression is not suitable for modelling binary responses?",
    'options_list': [
        'With a linear regression model, all predicted outcomes will fall between zero and one.',
        'With a linear regression model, some of the predicted outcomes may be less than zero or greater than one.',
        'Linear regression is not capable of modelling a response based on more than one variable at a time.',
        'Linear regression is not capable of modelling categorical variables.'
    ],
    'correct_answer': 'With a linear regression model, some of the predicted outcomes may be less than zero or greater than one.',
    'chapter_information': 'Lecture slide #8'
}

hw2_part1_q3 = {
    'question': "If we decrease the cutoff value of a logistic regression model then considering that number of True positives, True negatives, False positive and False negatives changes, which of the following is true? (Assume that there are no changes in the dataset used)",
    'options_list': [
        'False positive rate decreases',
        'Sensitivity increases',
        'Specificity increases',
        'None of the above'
    ],
    'correct_answer': 'Sensitivity increases',
    'chapter_information': "Module 4: As we decrease the cutoff value, the number of True positives \
    increase, the number of True negatives decrease, the number of False positives increase and \
    the number of False negatives decrease. Since the (number of True positives + number of \
    False negatives) = Actual positives and (number of True negatives + False positives) = Actual \
    negatives remain the same as we're using the same dataset, Sensitivity increases, Specificity \
        decreases and False positive rate increases. "
}

hw2_part1_q4 = {
    'question': "After running a logistic linear regression model in R where logit(p) = b0 + b1*student, you find that your coefficient estimate for your ‘non-students’ (intercept) is equal to –4.732 and your coefficient estimate for ‘student’ is equal to 1.748. Calculate the odds for non-students and students.",
    'options_list': [
        'e(-4.732), e(-4.732+1.748)',
        '-4.732, -4.732+1.748',
        '-4.732, 1.748',
        'log(-4.732), log(1.748)'
    ],
    'correct_answer': 'e(-4.732), e(-4.732+1.748)',
    'chapter_information': 'Module 4 (Page 17 Slide 2)'
}

hw2_part1_q5 = {
    'question': "Which of the following is not needed to establish causation?",
    'options_list': [
        'Hypothesized cause must precede its anticipated effect.',
        'Other possible explanations that can cause the effect must be ruled out.',
        'Change in cause must lead to a change in effect.',
        'The effect must always have a reverse impact on the cause.'
    ],
    'correct_answer': 'The effect must always have a reverse impact on the cause.',
    'chapter_information': '(Module 5, slide 3)'
}

hw2_part1_q7 = {
    'question': "Choose if the following statement is true or false: Correlation is sensitive to the scale of the data; however, covariance is not sensitive to the scale of the data.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Correlation is NOT sensitive to the scale and covariance is scale sensitive à If we scale each random variable (say X and Y) by the same factor (say 2), \
        the relative position of data won’t change, but the covariance between X and Y becomes 4 times which can be confirmed by the formula. However, in case of correlation – \ it has \
            normalizing standard deviation terms in denominator which makes it immune to the scale of data.'
}

hw2_part1_q8 = {
    'question': "Which of the following is NOT an example of selection bias?",
    'options_list': [
        'A voter survey to predict vote distribution for the presidential election in the US which is based on a sample of low-income household voters in the US.',
        'Taking surveys of people to participate in the study over email.',
        'Survey filled by audiences who have come to see radio/tv shows that are on controversial topics (abortion, affirmative action, gun control, etc.).',
        'Dividing states into subgroups based on important characteristics and randomly selecting houses to be surveyed.'
    ],
    'correct_answer': 'Dividing states into subgroups based on important characteristics and randomly selecting houses to be surveyed.',
    'chapter_information': '. D. is the only part where there is no selection bias for a state-wide survey. A is an example of Under-coverage Bias; B is an example of Nonresponse Bias and C is an example of Voluntary Response Bias.'
}

hw2_part1_q10 = {
    'question': "Suppose you invested in a fund for 1 year. The fund return was 10% and risk-free rate was 2%. The fund’s standard deviation over this period was 5% and beta was 1.3. What was the fund’s Sharpe ratio?",
    'options_list': ['0.06', '1.6', '4', '6.15'],
    'correct_answer': '1.6',
    'chapter_information': 'Sharpe Ratio = (0.10 – 0.02)/0.05 = 1.6'
}

hw2_part1_q11 = {
    'question': "Given beta (β) of the following stocks, which stock would have the most increase if the market has a 10% increase?",
    'options_list': [
        'Stock A beta = 1',
        'Stock B beta = 1.8',
        'Stock C beta = 0.1',
        'Stock D beta = -1.5'
    ],
    'correct_answer': 'Stock B beta = 1.8',
    'chapter_information': "Beta measures sensitivity and how the stock co-moves with changes in the market. If beta = 1, \
        then stock price moves up 1% in each 1% increase in market. If beta = 0, then stock price stays unchanged with each 1% increase in market. If beta > 1, then stock price moves greater than the 1% increase in market. \
            In this question, Stock B has the highest positive beta. A 10% increase in market would result in 18% (10% * 1.8) increase to the stock price"
}

hw2_part1_q12 = {
    'question': "Consider 2 stocks A and B. Over a period of time, the Jensen’s alpha for stock A was 0.5 and the Jensen’s alpha for stock B was -0.7. Given the beta for stock A was 1.2 and for stock B was 1.5, and considering that the return on the index used in calculating Jensen’s alpha and beta for these stocks over this time period was the same as the risk-free rate, which stock had better return over this period of time?",
    'options_list': [
        'Stock A',
        'Stock B',
        'Can’t say as more information is required to make this decision'
    ],
    'correct_answer': 'Stock A',
    'chapter_information': 'Since the return of the market index is same as the risk-free rate, the multiplier of the beta term (Rm-Rf) is zero and hence beta has no effect over the returns of these stocks. Since the error terms are insignificant, the stock with higher alpha has higher excess returns and hence has higher returns.'
}

##Hw 3


hw3_part1_q02 = {
    'question': "From 2012 to 2018, which pricing model (Performance, CPM, Hybrid) has brought in the most revenue?",
    'options_list': [
        'Performance Pricing Model',
        'CPM Pricing Model',
        'Hybrid Pricing Model',
        'All Models Performed The Same'
    ],
    'correct_answer': 'CPM Pricing Model',
    'explanation': "Since the CPM Pricing Model is marked as the correct answer, it implies that this model generated the most revenue from 2012 to 2018 compared to the other models."
}

hw3_part1_q03 = {
    'question': "Which customer metadata is not well suited for analyzing customer churn?",
    'options_list': [
        'Social Security Number',
        'Zip Code',
        'Spending Habits',
        'Hobbies'
    ],
    'correct_answer': 'Social Security Number',
    'explanation': "A Social Security Number does not provide useful insights for customer churn analysis compared to other metadata like spending habits or zip code which can indicate customer preferences and geographical trends."
}

hw3_part1_q04 = {
    'question': "What does CPM stand for?",
    'options_list': [
        'Cost Per Million',
        'Cost Per Mille (Cost Per Thousand)',
        'Counts Per Hundred',
        'None of the Above'
    ],
    'correct_answer': 'Cost Per Mille (Cost Per Thousand)',
    'explanation': "CPM stands for Cost Per Mille, which is also known as Cost Per Thousand, and refers to the cost per 1000 impressions in advertising."
}

hw3_part1_q06 = {
    'question': "Which of the following methods of Improving Customer Conversion Rates involves randomly splitting the traffic amongst two or more different versions of a webpage?",
    'options_list': [
        'Usability testing',
        'Competitor Benchmarking',
        'A/B Testing',
        'Segmentation'
    ],
    'correct_answer': 'A/B Testing',
    'explanation': "A/B Testing is the method where traffic is randomly divided between different webpage versions to test which one performs better in terms of conversion rates."
}

hw3_part1_q07 = {
    'question': "A website that uses Google Analytics wants to know how long visitors are spending on their landing page. Which metric should they use?",
    'options_list': [
        'Average Session Duration',
        'Pages Per Session',
        'Pageviews',
        'Bounce Rate'
    ],
    'correct_answer': 'Average Session Duration',
    'explanation': "Average Session Duration is the correct metric to analyze how long visitors are spending on a landing page."
}

hw3_part1_q08 = {
    'question': "Which factors does Google use to determine your ad rank?",
    'options_list': [
        'Company Brand, Marketing Budget',
        'Ad Break Even Price, Total Spent on Ads',
        'Maximum Bid, Ad Quality Score',
        'Company Financial Score, Landing Page Appearance'
    ],
    'correct_answer': 'Maximum Bid, Ad Quality Score',
    'explanation': "Google determines ad rank primarily based on the maximum bid set for the ad and the Quality Score which takes into account factors like relevancy and landing page experience."
}

hw3_part1_q09 = {
    'question': "Which of the following can have an impact on how visitors and potential customers interact with your landing page:",
    'options_list': [
        'Page Header',
        'Call to Action, and Offer',
        'Page Layout, Color, and Images',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "All the listed elements - Page Header, Call to Action, Offer, Page Layout, Color, and Images - can significantly affect visitor interaction and conversion on a landing page."
}

hw3_part1_q10 = {
    'question': "If your favorite tv show has a HUT of 80 and a Rating of 20, what is the Share of that show?",
    'options_list': [
        '25',
        '50',
        '75',
        'Not Enough Information Given'
    ],
    'correct_answer': '25',
    'explanation': "Share is calculated as the Rating divided by the HUT. Here, a Rating of 20 out of a HUT of 80 gives a Share of 25%."
}



sa5_question_5 = {
    'question': "What would be the adjusted stock price of XYZ after the stock split?",
    'options_list': [
        '$15',
        '$25',
        '$9',
        '$12'
    ],
    'correct_answer': '$9',
    'explanation': "After a 5 for 3 stock split, the number of shares increases from 3000 to 5000. The total market value remains the same, so the new share price is the old market value divided by the new number of shares: (3000 * 15) / 5000 = $9."
}

sa5_question_6 = {
    'question': "What would be the number of stocks of XYZ available in the market after the stock split?",
    'options_list': [
        '3000',
        '1800',
        '15000',
        '5000'
    ],
    'correct_answer': '5000',
    'explanation': "With a 5 for 3 stock split, the number of shares increases. The new number of shares is 3000 * (5 / 3) = 5000."
}

sa5_question_7 = {
    'question': "What would be the market value of all stocks of XYZ after the stock split?",
    'options_list': [
        '$3000',
        '$45000',
        '$27000',
        '$75000'
    ],
    'correct_answer': '$45000',
    'explanation': "The market value after the stock split is the new number of shares multiplied by the new share price: 5000 * 9 = $45000."
}

sa5_question_8 = {
    'question': "Which of the following statements is true for Apple stock?",
    'options_list': [
        'When the market goes down by 1.32%, on average, Apple stock goes down by 1%',
        'When the market goes up by 1.32%, on average, Apple stock goes up by 1%',
        'When the market goes down by 1%, on average, Apple stock goes down by 1.32%',
        'Both a and b'
    ],
    'correct_answer': 'When the market goes down by 1%, on average, Apple stock goes down by 1.32%',
    'explanation': "Beta is a measure of a stock's volatility in relation to the market. A beta of 1.32 for Apple means it moves 1.32% for every 1% market movement."
}

sa5_question_9 = {
    'question': "Based on the beta values, which of the following stocks has the greatest return potential but also poses the greatest market risk?",
    'options_list': [
        'Herbalife',
        'Apple',
        'Herbalife and Apple have equal return potential',
        'Walmart'
    ],
    'correct_answer': 'Herbalife',
    'explanation': "Higher beta indicates higher return potential and greater risk. Herbalife has the highest beta at 1.58, suggesting the greatest return potential and market risk."
}

sa5_question_10 = {
    'question': "Based on the beta values, which of the following stocks is the least risky to invest in?",
    'options_list': [
        'Herbalife',
        'Apple',
        'Costco',
        'Walmart'
    ],
    'correct_answer': 'Walmart',
    'explanation': "The stock with the lowest beta is considered the least risky. Walmart has the lowest beta at 0.62, making it the least risky among the given options."
}

sa7_question_1 = {
    'question': "Consider small town A. There are 100 households that possess a TV, where 80 of the households use the TV. If the share of a particular channel is 50, how many users are viewing the channel?",
    'options_list': [
        '40',
        '50',
        '60',
        '80'
    ],
    'correct_answer': '40',
    'explanation': "Share represents the percentage of households using TV that are tuned into a particular channel. With a share of 50 and 80 households using the TV, the number viewing the channel is 50% of 80, which is 40."
}

sa7_question_2 = {
    'question': "Consider small town B. If the share of a particular channel is 25, and its rating is 15, what is its HUT?",
    'options_list': [
        '16',
        '40',
        '60',
        '375'
    ],
    'correct_answer': '60',
    'explanation': "HUT (Households Using TV) is the percentage of all households with TVs in use at a particular time. The rating is the percentage of all TV households watching a specific channel. HUT can be found by (Rating / Share) * 100, which in this case is (15 / 25) * 100 = 60."
}

sa7_question_3 = {
    'question': "Consider small town C. There are 200 households that possess a TV, if the share of a particular channel is 25, and its rating is 10, how many households use the TV?",
    'options_list': [
        '80',
        '40',
        '12.5',
        '60'
    ],
    'correct_answer': '40',
    'explanation': "The number of households using TV (HUT) can be calculated as Rating / Share * Total Households. With a share of 25 and a rating of 10, the HUT is (10 / 25) * 200 = 40."
}

sa7_question_4 = {
    'question': "The formula of Click Through Rate (CTR) is Clicks/Revenue",
    'options_list': [
        'TRUE',
        'FALSE'
    ],
    'correct_answer': 'FALSE',
    'explanation': "The correct formula for Click Through Rate (CTR) is Clicks/Impressions, not Clicks/Revenue."
}

sa7_question_5 = {
    'question': "What is the length limit of Description in a paid search Ad (in characters)?",
    'options_list': [
        '15',
        '30',
        '80',
        '100'
    ],
    'correct_answer': '80',
    'explanation': "The length limit for the Description in a paid search Ad is typically 80 characters."
}

sa7_question_6 = {
    'question': "What is not included in Quality Score Factors?",
    'options_list': [
        'Landing Page',
        'CTR',
        'CPC',
        'Keywords'
    ],
    'correct_answer': 'CPC',
    'explanation': "Quality Score in digital advertising typically includes factors such as Landing Page quality, Click Through Rate (CTR), and relevance of Keywords, but not Cost Per Click (CPC)."
}

sa7_question_7 = {
    'question': "Frequency is a method of rating used in TV advertising and is given by:",
    'options_list': [
        'GRPs + REACH',
        'GRPs * REACH',
        'GRPs / REACH',
        'GRPs - REACH'
    ],
    'correct_answer': 'GRPs / REACH',
    'explanation': "Frequency, which is the average number of times a household is exposed to an advertisement, is given by the formula Frequency = GRPs / Reach."
}

sa7_question_8 = {
    'question': "Of the following, which type of deal is most preferred by advertisers?",
    'options_list': [
        'CPL',
        'CPC',
        'CPV',
        'CPM'
    ],
    'correct_answer': 'CPM',
    'explanation': "CPM, or Cost Per Mille (thousand), is often the preferred deal type for advertisers because it's based on the number of impressions, which is a basic metric for ad exposure."
}

sa7_question_9 = {
    'question': "Of the following, which type of deal is under range of win-win?",
    'options_list': [
        'CPV',
        'CPS',
        'CPM',
        'CTR'
    ],
    'correct_answer': 'CPM',
    'explanation': "CPM, or Cost Per Mille (thousand), is considered a win-win because it balances the needs of both publishers and advertisers. Advertisers pay for exposure (impressions), and publishers get compensated for displaying ads."
}

sa7_question_10 = {
    'question': "HUT (Households Using TV) is a method of rating used in TV advertising.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "HUT, or Households Using Television, is indeed a measure used in TV advertising to represent the number of households that are using a TV at a particular time."
}


sa8_question_1 = {
    'question': "According to the lecture, which of the following is not one of the characteristics of objectives when establishing social media goals?",
    'options_list': [
        'Attainable',
        'Comprehensive',
        'Relevant'
    ],
    'correct_answer': 'Comprehensive',
    'explanation': "The characteristics of objectives when establishing social media goals include specific, measurable, attainable, relevant, and time-bound. Comprehensive is not listed as one of these characteristics."
}

sa8_question_2 = {
    'question': "Please choose the correct ranking of the risks of running advertisements for advertisers, from the most risky to the least.",
    'options_list': [
        'Cost per view, cost per sale, cost per click',
        'Cost per sale, cost per click, cost per view',
        'Cost per view, cost per click, cost per sale'
    ],
    'correct_answer': 'Cost per view, cost per click, cost per sale',
    'explanation': "For advertisers, the advertising risk ranking from high to low of all the cost structures mentioned in the lecture is: cost per thousand > cost per view > cost per click > cost per lead > cost per sale."
}

sa8_question_3 = {
    'question': "According to the lecture, what model do hybrid advertisements use?",
    'options_list': [
        'Cost per view model.',
        'Cost per view + cost per click model',
        'Cost per view + cost per sale model'
    ],
    'correct_answer': 'Cost per view + cost per click model',
    'explanation': "Hybrid advertisements combine different models; according to the lecture, they use a cost per view plus cost per click model."
}

sa8_question_4 = {
    'question': "Select the incorrect statement from the following:",
    'options_list': [
        'The general structure of a paid search ad consists of 3 primary sections: 1) a Headline, 2) a Display URL and Path, and 3) Ad Group',
        'Landing Page is the first page a user reaches when clicking on a link in an online marketing campaign.',
        'According to Week 10 slides, Keywords, Ad Copy, Landing Page and CTR of the Ad are the factors that affect the quality score in Google AdWords system.',
        'An organization that attains a higher quality score relative to their competitors can realize a lower CPC and still rank higher than the competition'
    ],
    'correct_answer': 'The general structure of a paid search ad consists of 3 primary sections: 1) a Headline, 2) a Display URL and Path, and 3) Ad Group',
    'explanation': "The incorrect statement is that a paid search ad's general structure includes an Ad Group. The correct components are a Headline, a Display URL and Path, and a Description."
}

sa8_question_5 = {
    'question': "Planning and Setting Up a Paid Search Campaign does not involve the following step:",
    'options_list': [
        'Establishing a Budget',
        'Conduct keyword research',
        'Hiring professional digital advertisers to come up with a catchy tagline',
        'Defining business goals being supported by market research'
    ],
    'correct_answer': 'Hiring professional digital advertisers to come up with a catchy tagline',
    'explanation': "While creating a catchy tagline can be beneficial, it is not listed as a necessary step in the provided planning and setting up of a Paid Search Campaign process."
}

sa8_question_6 = {
    'question': "Which of the following is not used to measure the profitability of an Ad Campaign?",
    'options_list': [
        'CPC (Cost Per Click)',
        'Customer Complaint Rate',
        'Conversion Rate',
        'Lifetime Value of Customer'
    ],
    'correct_answer': 'Customer Complaint Rate',
    'explanation': "Customer Complaint Rate is not a direct measure of profitability for an Ad Campaign. Measures like CPC, Conversion Rate, and Lifetime Value of Customer are commonly used to assess profitability."
}

sa9_question_1 = {
    'question': "How would you best describe Operations Management?",
    'options_list': [
        'Direction and control of process that transform inputs into finished goods and services',
        'How to manage operating machines',
        'Scheduling of workers on the manufacturing floor',
        'Deciding what to make'
    ],
    'correct_answer': 'Direction and control of process that transform inputs into finished goods and services',
    'explanation': "Operations Management involves overseeing, designing, and controlling the process of production and redesigning business operations in the production of goods or services."
}

sa9_question_2 = {
    'question': "Which is not a question typically concerned with Operations Management?",
    'options_list': [
        'What benefits package should we offer our employees?',
        'What types of queues should we employ?',
        'How much capacity do we need?',
        'What is the critical path of this project?'
    ],
    'correct_answer': 'What benefits package should we offer our employees?',
    'explanation': "Employee benefits packages are typically a concern of human resources, not operations management."
}

sa9_question_3 = {
    'question': "Knowledge of Operations Management is essential to most of the business fields?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "Understanding Operations Management is crucial as it applies to various aspects across most business fields, affecting the efficiency and effectiveness of the organization."
}

sa9_question_4 = {
    'question': "In Queueing Theory, what two rates do we try to model?",
    'options_list': [
        'Exit Rate and Queue Length',
        'Arrival Rate and Exit Rate',
        'Payment Rate and Service Rate',
        'Service Rate and Arrival Rate'
    ],
    'correct_answer': 'Service Rate and Arrival Rate',
    'explanation': "Queueing Theory primarily concerns itself with modeling the service rate at which customers are served and the arrival rate at which they enter the system."
}

sa9_question_5 = {
    'question': "What are the queue metrics of this system?",
    'options_list': [
        'Utilization = .86, Lq =6 customers, Wq=10.29 min, Ls=5.14 customers, Ws= 12 min',
        'Utilization = .86, Lq =5.14 customers, Wq=17 min, Ls=6 customers, Ws= 20 min',
        'Utilization = .86, Lq =6 customers, Wq=20 min, Ls=5.14 customers, Ws=17 min',
        'Utilization = .86, Lq = 5.14 customers, Wq=10.29 min, Ls=6 customers, Ws=12 min'
    ],
    'correct_answer': 'Utilization = .86, Lq = 5.14 customers, Wq=10.29 min, Ls=6 customers, Ws=12 min',
    'explanation': "Utilization is calculated as the arrival rate divided by the service rate. Ls and Ws are the average number of customers in the system and the average time a customer spends in the system, respectively. Lq and Wq are the average number of customers in queue and the average time a customer spends in queue, respectively."
}

sa9_question_6 = {
    'question': "What service rate would be required to have customers average only 8 minutes in the system?",
    'options_list': [
        '40.5',
        '36.5',
        '37.5',
        '30.5'
    ],
    'correct_answer': '37.5',
    'explanation': "To find the required service rate for an average time in the system of 8 minutes, we can use the formula Ws = 1 / (mu - lambda), where Ws is the average time in the system, mu is the service rate, and lambda is the arrival rate."
}

sa9_question_7 = {
    'question': "For the service rate in question 6, what is the probability of having more than four check writers in the system?",
    'options_list': [
        '67%',
        '75%',
        '33%',
        '25%'
    ],
    'correct_answer': '25%',
    'explanation': "The probability of having more than four check writers in the system can be calculated using the Poisson distribution with the service rate from question 6."
}

sa9_question_8 = {
    'question': "What is the average time spent in the system?",
    'options_list': [
        '30 min',
        '40 min',
        '50 min',
        '60 min'
    ],
    'correct_answer': '60 min',
    'explanation': "The average time spent in the system (Ws) can be calculated as the inverse of the difference between the service rate (mu) and the arrival rate (lambda). Given lambda = 4/hr and mu = 5/hr, Ws is 60 minutes."
}

sa9_question_9 = {
    'question': "What is the average number of students waiting in line?",
    'options_list': [
        '2.2',
        '3.2',
        '2.4',
        '4.4'
    ],
    'correct_answer': '3.2',
    'explanation': "The average number of students waiting in line (Lq) can be found using the formula Lq = lambda^2 / mu(mu - lambda) for a system with Poisson arrivals and exponential service times."
}

sa9_question_10 = {
    'question': "Is 1 officer sufficient for this demand?",
    'options_list': [
        'Yes, average time in line is less than 50 min',
        'No, average time in line is more than 50 min',
        'Yes, productivity is 80%',
        'No, productivity is 80%'
    ],
    'correct_answer': 'Yes, average time in line is less than 50 min',
    'explanation': "Given the service rate and arrival rate, we can calculate the average time in line (Wq). If it's less than 50 minutes, one officer is sufficient to handle the demand."
}

sa10_question_1 = {
    'question': "Which best describes Quality?",
    'options_list': [
        'How to make stuff',
        'The change in look from one item to another',
        'How consistent machines produce the same product',
        'Meeting or exceeding customers’ expectations',
        'Fit for use'
    ],
    'correct_answer': 'Meeting or exceeding customers’ expectations',
    'explanation': "Quality is defined as meeting or exceeding customer expectations as per Module 13 lecture 1 slide 3."
}

sa10_question_2 = {
    'question': "Which is not a dimension of product quality?",
    'options_list': [
        'Value',
        'Conformance to Specifications',
        'Serviceability',
        'Performance',
        'Durability'
    ],
    'correct_answer': 'Value',
    'explanation': "Value is not listed among Garvin's 8 dimensions of product quality which include performance, functionality, durability, reliability, conformance to specifications, serviceability, aesthetics, and perceived quality."
}

sa10_question_3 = {
    'question': "Statistical Process Control looks at variation as being of two types: Random and Assignable?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "True. There are two primary types of variation identified in Statistical Process Control: random and assignable, as stated in Module 13 lecture 3 slide 6."
}

sa10_question_4 = {
    'question': "Which one is not a property of a Random (or Common) variance?",
    'options_list': [
        'Inherent in the process used',
        'Unavoidable with current process',
        'Can do nothing about this',
        'Can be identified'
    ],
    'correct_answer': 'Can be identified',
    'explanation': "Random or common variance is inherent and unavoidable in the current process, and typically, there is little that can be done about this type of variance. It is often not easily identifiable, which is what differentiates it from assignable variance."
}



COURSE_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        COURSE_MPC_QUESTIONS.append(value)

COURSE_MPC_QUESTIONS = COURSE_MPC_QUESTIONS[:-1]
