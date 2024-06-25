###########knowledge check 1############################
kc1_question_1 = {
    'question': "Given R squared is 0.68. Find the adjusted R squared if the sample size is 600 and number of independent variables is 10.",
    'options_list': ['0.676', '0.688', '0.667', '0.674'],
    'correct_answer': '0.674',
    'chapter_information': 'Week 1, Slide 31'
}

kc1_question_2 = {
    'question': "Which of the following values cannot be an R squared value?",
    'options_list': ['0.5', '0.99', '.003', '1.2'],
    'correct_answer': '1.2',
    'chapter_information': 'Week 1, Slide 20'
}

kc1_question_3 = {
    'question': "The total deviation at observation (xi, yi) is:",
    'options_list': ['ŷi - ȳi', 'yi - ȳ', 'yi - ŷi', 'None of these'],
    'correct_answer': 'yi - ȳ',
    'chapter_information': 'Week 1, Slide 17'
}

kc1_question_4 = {
    'question': "How can we detect multicollinearity in a model?",
    'options_list': ['Variance Inflation factor (VIF)', 'Correlation matrix', 'R2', 'Both a) and b)'],
    'correct_answer': 'Both a) and b)',
    'chapter_information': 'Week 1, Slide 45-46'
}


###########knowledge check 2############################

kc2_question_1 = {
    'question': "If you convert a categorical variable with M categories into dummy variables, how many dummy variables are created?",
    'options_list': ['M – 2', 'M', 'M – 1', 'None of the above'],
    'correct_answer': 'M – 1',
    'chapter_information': 'Lesson 2 / Video 2 / Slides 3 –5'
}

kc2_question_2 = {
    'question': "Based on the following regression model summary (Note: the base case is Age = Young), what is the Amount Spent by a Middle-aged customer if his/her salary is 10000?",
    'options_list': ['20-6.12', '20 – 6.12 - 4.81', '20 – 6.12 + 23.28', '20'],
    'correct_answer': '20 – 6.12 - 4.81',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 1 – 4'
}

kc2_question_3 = {
    'question': "An interaction term is used to model how the synergies between multiple variables impact the response variable.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Video 4 / Slides 6 – 9'
}

###########knowledge check 3############################
kc3_question_1 = {
    'question': "Using the following regression equation, determine which statement is correct.\n\nPrice = b0 + b1*lotsize + b2*lotsize^2",
    'options_list': [
        "Coefficients b1 and b2 can be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 can be interpreted individually because when lotsize is decreased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.",
        "Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is possible (or meaningful) to hold lotsize^2 constant."
    ],
    'correct_answer': 'Coefficients b1 and b2 cannot be interpreted individually because when lotsize is increased by 1 unit, it is not possible (or meaningful) to hold lotsize^2 constant.',
    'chapter_information': 'Lesson 3 / Video 5 / Slide 3'
}

kc3_question_2 = {
    'question': "Increasing X by 1 percent is almost equivalent to increasing (natural) log(X) by 0.01 units.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 3 / Video 2 / Slide 3'
}

kc3_question_3 = {
    'question': "What type of plot do you see in the following image?",
    'options_list': ['Residuals vs Fitted', 'Normal Q-Q', 'Scale -Location', 'Residuals vs Leverage'],
    'correct_answer': 'Normal Q-Q',
    'chapter_information': 'Lesson 3 / Video 2 / Slide 5'
}

kc3_question_4 = {
    'question': "Which of the following are the main purposes of log-transformation? Choose all the right answers.",
    'options_list': [
        "Achieve a more exponential relationship",
        "Make a distribution more normal",
        "Increase the variance"
    ],
    'correct_answer': ['Make a distribution more normal'],
    'chapter_information': 'Lesson 3 / Video 4 / Slide 7'
}

kc3_question_5 = {
    'question': "Which of the following are the main purposes of log-transformation? Choose all the right answers.",
    'options_list': [
        "Achieve a more exponential relationship",
        "Increase the variance",
        "Get a better fit such as higher R-squared"
    ],
    'correct_answer': ['Get a better fit such as higher R-squared'],
    'chapter_information': 'Lesson 3 / Video 4 / Slide 7'
}

###########knowledge check 4############################
kc4_question_1 = {
    'question': "If we want to arrive at the model given below:\n\ny = b0 + b1x1 + b2x2,\nwhere y is a continuous response variable in range (0,1) while x1 and x2 are binary predictors (with discrete values 0 or 1), what is the correct regression to be used:",
    'options_list': ['Simple linear regression', 'Multiple linear regression', 'Logistic regression', 'None of the above'],
    'correct_answer': 'Multiple linear regression',
    'chapter_information': 'Explanation: Since response variable is continuous and we have multiple predictors, we should use multiple linear regression.'
}

kc4_question_2 = {
    'question': "Which of the following is type 1 error?",
    'options_list': [
        "A null hypothesis is rejected when it should not be rejected",
        "A null hypothesis is not rejected when it should be rejected",
        "When p value is above a threshold",
        "When p value is below a threshold"
    ],
    'correct_answer': 'A null hypothesis is rejected when it should not be rejected',
    'chapter_information': 'Module 4, slide 27'
}

kc4_question_3 = {
    'question': "Which of the following generally takes place when we increase the cutoff value of p?",
    'options_list': ['Sensitivity increases', 'Specificity decreases', 'Precision increases', 'Recall increases'],
    'correct_answer': 'Precision increases',
    'chapter_information': 'Precision increases when we increase the classification threshold. Others are incorrect. Module 4, slide 29'
}

kc4_question_4 = {
    'question': "For the given logistic regression model output, select the correct option (Smoker is a categorical variable with 2 levels: Smoker/Non-Smoker):",
    'options_list': [
        "For smokers versus non-smokers, the odds of survival is ~21.4% lower than for non-smokers; assuming all else constant",
        "For smokers versus non-smokers, the log odds of survival decreases by 7.54; assuming all else constant",
        "For smokers versus non-smokers, the odds of survival decreases by 0.24; assuming all else constant",
        "None of these"
    ],
    'correct_answer': 'For smokers versus non-smokers, the odds of survival decreases by 0.24; assuming all else constant',
    'chapter_information': 'Correct interpretation of logistic regression model output regarding the effect of smoking on survival odds.'
}

###########knowledge check 5############################
kc5_question_1 = {
    'question': "A correlation of 1 means that there is a strong correlation and causation between two variables.",
    'options_list': ['True', 'False'],
    'correct_answer': 'False',
    'chapter_information': 'Lesson 1, Slide 4'
}

kc5_question_2 = {
    'question': "Which of the following approaches is a good way to avoid selection bias?",
    'options_list': ['Self-Selection', 'Voluntary-response', 'Random sampling', 'None of the above'],
    'correct_answer': 'Random sampling',
    'chapter_information': 'Lesson 2, slide 2,5'
}

kc5_question_3 = {
    'question': "Which of the following is not an example of a natural experiment?",
    'options_list': [
        "A law that changed the tax rate for some subjects, but not others",
        "Minimum wage is changed in one state but not another",
        "A mobile carrier implements an unlimited data plan in some cities but not others",
        "A hurricane that hits all the stores countrywide"
    ],
    'correct_answer': 'A hurricane that hits all the stores countrywide',
    'chapter_information': 'Lesson 5, slide 2'
}

###########knowledge check 6############################

kc6_question_1 = {
    'question': "Does the market value of a company change after a 2 for 1 stock split?",
    'options_list': ['Yes', 'No'],
    'correct_answer': 'No',
    'chapter_information': 'Lesson 1: Simple and Compound Returns'
}

kc6_question_2 = {
    'question': "Which of the following represents the cumulative effect that a series of gains or losses has on an original investment over a period of time?",
    'options_list': ['Simple Return', 'Compound Return'],
    'correct_answer': 'Compound Return',
    'chapter_information': 'Lesson 1 / Slide 6'
}

kc6_question_3 = {
    'question': "Which of the following is not a measure of risk?",
    'options_list': ['Standard Deviation', 'Beta', 'Drawdown', 'Stock split'],
    'correct_answer': 'Stock split',
    'chapter_information': 'Lesson 2 / Slide 1'
}

kc6_question_4 = {
    'question': "What Beta represents a risk-free asset?",
    'options_list': ['0', '1', '2'],
    'correct_answer': '0',
    'chapter_information': 'Lesson 2 / Slide 7'
}

kc6_question_5 = {
    'question': "What measures sensitivity to market movements?",
    'options_list': ['Standard Deviation', 'Beta'],
    'correct_answer': 'Beta',
    'chapter_information': 'Lesson 2 / Slide 6'
}

kc6_question_6 = {
    'question': "Which of the following asset classes has the highest standard deviation over time?",
    'options_list': ['Bonds', 'Inflation', 'Small Cap'],
    'correct_answer': 'Small Cap',
    'chapter_information': 'Lesson 3 / Slide 5'
}

##########knowledge check 7############################
kc7_question_1 = {
    'question': "Which of the following measures risk adjusted performance?",
    'options_list': ['Sharpe Ratio', 'Treynor Ratio', 'Jensen’s Alpha', 'All of the above'],
    'correct_answer': 'All of the above',
    'chapter_information': 'Lesson 1 / Slide 1'
}

kc7_question_2 = {
    'question': "What does Jensen’s Alpha measure?",
    'options_list': [
        "Abnormal return by comparing to a benchmark",
        "Investment reward per unit risk",
        "Abnormal return that the portfolio earns after adjusting beta"
    ],
    'correct_answer': "Abnormal return by comparing to a benchmark",
    'chapter_information': 'Lesson 1 / Slide 8'
}

kc7_question_3 = {
    'question': "True or False: Transaction costs always lower our returns.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': 'Lesson 2 / Slide 8'
}

kc7_question_4 = {
    'question': "What is the bid-ask spread of stock symbol XYZ given the best ask price is $36 and best bid price is $34?",
    'options_list': ['$1', '$2', '$35', '$70'],
    'correct_answer': '$2',
    'chapter_information': 'Lesson 2 / Slides 4-5'
}

kc7_question_5 = {
    'question': "Which of the following transaction cost describes this scenario? An investor pays a fixed $5.00 fee per trade.",
    'options_list': ['Commissions', 'Bid-Ask Spread Cost', 'Delay Cost'],
    'correct_answer': 'Commissions',
    'chapter_information': 'Lesson 2 / Slide 4'
}

kc7_question_6 = {
    'question': "Which of the following is not a type of market efficiency?",
    'options_list': ['Weak Form', 'Semi-Weak Form', 'Semi-Strong Form', 'Strong Form'],
    'correct_answer': 'Semi-Weak Form',
    'chapter_information': 'Lesson 3 / Slide 1'
}

kc7_question_7 = {
    'question': "If the current stock price reflects all publicly available information and not private information, what type of market efficiency is it experiencing?",
    'options_list': ['Weak Form', 'Semi-Weak Form', 'Semi-Strong Form', 'Strong Form'],
    'correct_answer': 'Semi-Strong Form',
    'chapter_information': 'Lesson 3 / Slide 6'
}

kc7_question_8 = {
    'question': "The tendency of individuals to seek pride and avoid regret in their decisions is known as ______?",
    'options_list': ['Overconfidence', 'Loss Aversion', 'Recency Effect', 'Anchoring'],
    'correct_answer': 'Anchoring',
    'chapter_information': 'Lesson 4 / Slide 4'
}

kc7_question_9 = {
    'question': "XYZ’s stock price was trading at $50 last week. XYZ is trading at $40 today. You decided to purchase 1 share of XYZ at $40 because you think it will go back up to $50. You made the purchase even though you have no other evidence to suggest the valuation of XYZ should be at $50. What is this an example of?",
    'options_list': ['Overconfidence', 'Loss Aversion', 'Recency Effect', 'Anchoring'],
    'correct_answer': 'Anchoring',
    'chapter_information': 'Lesson 4 / Slide 4'
}
###########knowledge check 8############################
kc8_question_1 = {
    'question': "Which of the following statements is NOT true:",
    'options_list': [
        "A high B/M ratio stock is often called a value stock",
        "A low B/M ratio stock is often called a growth stock",
        "A low B/M ratio means the stock is inexpensive",
        "A high B/M ratio means the stock is inexpensive"
    ],
    'correct_answer': "A low B/M ratio means the stock is inexpensive",
    'chapter_information': "Explanation: C: A low B/M ratio means the stock is inexpensive is False."
}

kc8_question_2 = {
    'question': "Which of the following statements is/are a benefit of factor analysis?",
    'options_list': [
        "Investors can analyze what type of factors drove a stock’s performance over a period",
        "Investors can attribute performance of funds and fund managers to specific factor exposures",
        "Investors can construct more balanced portfolios",
        "Investors can better understand their portfolio’s exposure to factors",
        "All of the Above"
    ],
    'correct_answer': "All of the Above",
    'chapter_information': "Solution: E: All of the Above."
}

kc8_question_3 = {
    'question': "Which of the following coefficients indicates the fund is tilted towards growth stocks?",
    'options_list': [
        "A positive coefficient on BAB",
        "A negative coefficient on BAB",
        "A positive coefficient on HML",
        "A negative coefficient on HML"
    ],
    'correct_answer': "A negative coefficient on HML",
    'chapter_information': "Solution: D A negative coefficient on HML."
}

kc8_question_4 = {
    'question': "True or False? Each of the factors discussed in the lecture have experienced prolonged periods of underperformance.",
    'options_list': ['True', 'False'],
    'correct_answer': 'True',
    'chapter_information': "Solution: A: True."
}

kc8_question_5 = {
    'question': "What is Sharpe Ratio used for?",
    'options_list': [
        "To calculate stocks and mutual fund return rates",
        "To determine stocks and mutual fund risk",
        "To identify stocks and mutual funds risk adjusted return",
        "To determine what drives the stocks and mutual funds returns"
    ],
    'correct_answer': "To identify stocks and mutual funds risk adjusted return",
    'chapter_information': "Solution: C: To identify stocks and mutual funds risk adjusted performance."
}

kc8_question_6 = {
    'question': "Which of the following is NOT a metric discussed in lecture of stock or portfolio performance?",
    'options_list': ['Sharpe Ratio', 'Jensen’s Alpha', 'Treynor Ratio', 'Case-Shiller Index'],
    'correct_answer': 'Case-Shiller Index',
    'chapter_information': "Solution: D: Case-Shiller Index; This is not a topic covered in the lectures."
}

kc9_question_1 = {
    'question': "What does CPM mean?",
    'options_list': [
        'Cost per Million',
        'Cost per Thousand',
        'Click per Million',
        'Click per Thousand'
    ],
    'correct_answer': 'Cost per Thousand',
    'explanation': "CPM stands for Cost per Mille, which translates to Cost per Thousand. This is content covered in Module 9."
}

kc9_question_2 = {
    'question': "Which is not a traditional method of advertising",
    'options_list': [
        'Print',
        'Mail',
        'Television',
        'Facebook'
    ],
    'correct_answer': 'Facebook',
    'explanation': "Facebook is a digital method of advertising, as opposed to traditional methods such as print, mail, and television. This is discussed in Module 9."
}

kc9_question_3 = {
    'question': "The ratio between “households using tv” vs “total households with a tv” is called ____?",
    'options_list': [
        'HUT',
        'RATING',
        'SHARE',
        'REACH'
    ],
    'correct_answer': 'HUT',
    'explanation': "HUT stands for Households Using Television. It is the ratio of households using tv to total households with a tv, as presented in Module 9."
}

kc9_question_4 = {
    'question': "How do you calculate Frequency?",
    'options_list': [
        'Reach/GRP',
        'GRP/Reach',
        'GRP * Reach',
        'Reach + GRP'
    ],
    'correct_answer': 'GRP/Reach',
    'explanation': "Frequency is calculated as GRP divided by Reach. This is a concept explained in Module 9."
}

kc9_question_5 = {
    'question': "Which advertising method is considered digital advertising?",
    'options_list': [
        'Email',
        'Direct Messaging',
        'Display Advertising',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Email, Direct Messaging, and Display Advertising are all considered digital advertising methods. This is covered in Module 9."
}

kc9_question_6 = {
    'question': "What do digital marketers do?",
    'options_list': [
        'Build Campaigns',
        'Buy Media',
        'Optimize Media Campaigns',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Digital marketers build campaigns, buy media, and optimize media campaigns. These activities are described in Module 9."
}

kc9_question_7 = {
    'question': "Ad placement systems consider both audience relevancy and budget allocation to determine ad placement",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "Ad placement systems do consider both audience relevancy and budget allocation when determining ad placement. This is part of the content in Module 9."
}

kc9_question_8 = {
    'question': "Ad networks are restricted to work with only one media buying agency?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': "Ad networks are not restricted to work with only one media buying agency; they can work with multiple agencies. This information is included in Module 9."
}

kc9_question_9 = {
    'question': "In 2017 and 2018 which ad type had the highest revenue?",
    'options_list': [
        'Search',
        'Banner',
        'Video',
        'Classifieds'
    ],
    'correct_answer': 'Search',
    'explanation': "Search advertising had the highest revenue in 2017 and 2018. This is according to the information presented in Module 9."
}

kc9_question_10 = {
    'question': "From 2014 to 2018, mobile advertising had more growth than desktop advertising?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "Mobile advertising saw more growth compared to desktop advertising from 2014 to 2018. This information is highlighted in Module 9, slide 9."
}

kc9_question_11 = {
    'question': "From 2010 to 2018, CPM had higher internet advertising revenue than Performance and Hybrid pricing models.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "From 2010 to 2018, CPM generated higher internet advertising revenue compared to Performance and Hybrid pricing models. This is detailed in Module 9, slide 13."
}

kc9_question_12 = {
    'question': "From 2012 to 2018, social media advertising has been on a decline.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'False',
    'explanation': "It is incorrect that social media advertising has been on a decline from 2012 to 2018; the trend has been towards growth. The correct information can be found in Module 9, slide 11."
}

kc10_question_1 = {
    'question': "For display advertising which of the following factors play a role in the pricing?",
    'options_list': [
        'Size of the advertisement in a newspaper',
        'Position of the advertisement in a newspaper',
        'Duration of the advertisement on TV',
        'Airing time of the advertisement on TV',
        'All the above'
    ],
    'correct_answer': 'All the above',
    'explanation': "All the listed factors, including size, position, duration, and airing time of advertisements, influence the pricing in display advertising. This information is covered in Module 10."
}

kc10_question_2 = {
    'question': "Which form of digital advertising considers a quality score in determining ad placement?",
    'options_list': [
        'Display Advertising and Search Engine Marketing',
        'Social Media Marketing and Mobile Advertising',
        'Direct Messaging and Email Marketing',
        'Only Search Engine Marketing',
        'Only Social Media Marketing'
    ],
    'correct_answer': 'Only Search Engine Marketing',
    'explanation': "Only Search Engine Marketing typically considers a quality score when determining ad placement. This aspect of digital advertising is detailed in Module 10."
}

kc10_question_3 = {
    'question': "Which of the following are typical tasks for digital Marketers?",
    'options_list': [
        'Planning and Building Ad Campaigns',
        'Buying Media or ad placements',
        'Optimizing Media Campaigns',
        'All of the above are tasks handled by digital Marketers'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Digital marketers are involved in planning and building ad campaigns, buying media or ad placements, and optimizing media campaigns. These tasks are explored in detail in Module 10."
}

kc10_question_4 = {
    'question': "Why is the Cost per sale (CPS) payment model in social media marketing not risky for businesses?",
    'options_list': [
        'It guarantees tangible return (profit) for any money spent on the advertisement',
        'It increases the likelihood that the advertisement is seen frequently by potential customers',
        'It increases the likelihood that advertising companies will accept the ad campaign',
        'None of the above, CPS is a risky payment method for businesses'
    ],
    'correct_answer': 'It guarantees tangible return (profit) for any money spent on the advertisement',
    'explanation': "The Cost per Sale (CPS) payment model is considered less risky for businesses because it ensures that they only pay when an actual sale is made, thereby guaranteeing a tangible return on their advertising spend. This concept is discussed in Module 10."
}

kc11_question_1 = {
    'question': "Which of the following is a major choice consideration area of landing pages?",
    'options_list': [
        'Heading',
        'Offer',
        'Images',
        'Call to Action',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Heading, offer, images, and call to action are all critical elements of landing pages that can significantly influence conversion rates. These elements are emphasized in Module 11."
}

kc11_question_2 = {
    'question': "True or False? Google Analytics offers two subscription tiers. One for free standard use, and one priced at a premium for additional functionality.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "Google Analytics does offer two subscription tiers: a free version for standard use and a premium version that provides additional functionality. This is covered in Module 11."
}

kc11_question_3 = {
    'question': "Which of the following is NOT a report generated by Facebook Insight Reporting tool?",
    'options_list': [
        'Messages to Page',
        'People Engaged with Content',
        'Fans of a Page',
        'Daily and Hourly Activity',
        'All of the above are reports available via Facebook’s Insight Reports'
    ],
    'correct_answer': 'All of the above are reports available via Facebook’s Insight Reports',
    'explanation': "All listed options are indeed reports generated by Facebook Insight Reporting tool, which is part of the content taught in Module 11."
}

kc11_question_4 = {
    'question': "True or False? It is possible to view the advertisers that have targeted your personal Facebook account within your personal account settings.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "It is indeed possible to view the advertisers that have targeted your personal Facebook account within your account settings. This functionality is highlighted in Module 11."
}

kc11_question_5 = {
    'question': "Which of the following is not an option offered by Facebook for broad types of ad placement?",
    'options_list': [
        'Facebook',
        'Instagram',
        'Audience Network',
        'Tik-Tok'
    ],
    'correct_answer': 'Tik-Tok',
    'explanation': "Tik-Tok is not part of Facebook's ad placement options, unlike Facebook, Instagram, and Audience Network. This distinction is discussed in Module 11."
}


kc12_question_1 = {
    'question': "What are the types of decisions taken in Operations Management?",
    'options_list': [
        'Strategic, Technical, Operational',
        'Strategic, Tactical, Operational',
        'Policy, Administrative, Executive',
        'Policy, Regulatory, Executive'
    ],
    'correct_answer': 'Strategic, Tactical, Operational',
    'explanation': "Operations Management involves making strategic (long-term impact), tactical (mid-term impact), and operational (short-term impact) decisions. This is covered in Module 12."
}

kc12_question_2 = {
    'question': "What are the goals of OM?",
    'options_list': [
        'Improve Efficiency',
        'Improve Effectiveness',
        'Increase Value',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "The goals of Operations Management include improving efficiency, effectiveness, and increasing value. These objectives are discussed in Module 12."
}

kc12_question_3 = {
    'question': "True or False? In terms of the lecture we treat the goal of 'increasing value' as a tradeoff between quality and price?",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "True. The goal of increasing value in Operations Management is often treated as a tradeoff between quality and price, as presented in Module 12."
}

kc12_question_4 = {
    'question': "Knowledge of Operations Management is essential for all fields such as Finance, Marketing, HR, Strategy, Accounting etc.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "True. Knowledge of Operations Management is essential across various fields including finance, marketing, HR, strategy, and accounting. This concept is emphasized in Module 12."
}

kc12_question_5 = {
    'question': "Reasons for supply interruptions mentioned in lecture include which of the following?",
    'options_list': [
        'Labor shortages',
        'Supplier failures',
        'Inaccurate inventory',
        'Poor forecasting',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Labor shortages, supplier failures, inaccurate inventory, and poor forecasting are all reasons for supply interruptions discussed in Module 12."
}

kc12_question_6 = {
    'question': "Which of the following are emerging technologies that have/will continue to have large impacts on supply chain operations?",
    'options_list': [
        'Autonomous Vehicles',
        'Robotics',
        'Artificial Intelligence',
        '3D Printing',
        'All of the Above'
    ],
    'correct_answer': 'All of the Above',
    'explanation': "Emerging technologies like autonomous vehicles, robotics, artificial intelligence, and 3D printing are having significant impacts on supply chain operations, as discussed in Module 12."
}

kc12_question_7 = {
    'question': "Which of the following are some of key attributes of a queuing system?",
    'options_list': [
        'Line Length',
        'Queue Discipline',
        'Service Rate',
        'Arrival Rate',
        'All of the above'
    ],
    'correct_answer': 'All of the above',
    'explanation': "Line length, queue discipline, service rate, and arrival rate are all key attributes of a queuing system. These attributes are covered in Module 12."
}

kc12_question_8 = {
    'question': "Which of the following is NOT a suggestion for Queue Management?",
    'options_list': [
        'Encourage customers to come during off-peak hours',
        'Inform customers what to expect',
        'Train employees to be friendly',
        'Don’t divert the customers attention when waiting'
    ],
    'correct_answer': 'Don’t divert the customers attention when waiting',
    'explanation': "Diverting the customer's attention when waiting is actually a suggested method for managing queues, contrary to the incorrect option. This is covered in Module 12."
}

kc12_question_9 = {
    'question': "Which of these is NOT an assumption of the M/M/1 model?",
    'options_list': [
        'Random Arrivals',
        'Single Line',
        'Finite Customer Population',
        'First Come First Served'
    ],
    'correct_answer': 'Finite Customer Population',
    'explanation': "The M/M/1 model assumes an infinite customer population, not a finite one. This is explained in Module 12."
}

kc12_question_10 = {
    'question': "The Utilization of an M/M/1 queuing model is calculated as:",
    'options_list': [
        'Arrival Rate/Service Rate',
        'Service Rate/Arrival Rate',
        '1/Arrival Rate',
        '1/Service Rate'
    ],
    'correct_answer': 'Arrival Rate/Service Rate',
    'explanation': "The utilization (\(\rho\)) of an M/M/1 queuing model is calculated as the arrival rate (\(\lambda\)) divided by the service rate (\(\mu\)), \(\rho = \lambda/\mu\). This is taught in Module 12."
}

kc12_question_11 = {
    'question': "True or False? A one lane toll bridge with manual payment and a McDonalds drive through are both examples of single-phase.",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "True. Both a one-lane toll bridge with manual payment and a McDonald's drive-through are examples of single-phase systems. This concept is discussed in Module 12."
}

kc12_question_12 = {
    'question': "(True/False) Operations Management is at the core of every company",
    'options_list': [
        'True',
        'False'
    ],
    'correct_answer': 'True',
    'explanation': "True. Operations Management is a central aspect of every company, as it involves the oversight and management of the processes that produce and distribute goods and services. This is emphasized in Module 12."
}





KC_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        KC_MPC_QUESTIONS.append(value)

KC_MPC_QUESTIONS = KC_MPC_QUESTIONS[:-1]
