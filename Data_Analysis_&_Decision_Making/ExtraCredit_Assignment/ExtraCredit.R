library(fpp)
library(fpp2)
#Question 1

#(a) Construct and run a regression model to predict the price of a house based on three independent variables for the area, the neighborhood rating, and the condition rating of the house.
#Answer : 
VARMAX <- read.csv("D:/Downloads/VARMAX.csv")
fit1 = lm(Price ~ Area + NeighborQualityRating + GeneralConditionRating ,data = VARMAX)

#(b) Evaluate the regression output of your regression model. Do you recommend using this regression model?
summary(fit1)
#From summary we can get that -
#R-Squared is close to 80% which means that the regression model is good fit to the given data
# Also , F-statistic is greater than ONE(F-statistic >1) So , we can recommend this model

#(c) What is the regression equation produced by the linear regression model?
#Y = B0 + B1x1(Area) + B2x2(NeighborQualityRating)  + B3x3(GeneralConditionRating) 
#So Equation is : y = -166694.46 +  88.02x(Area) + 39917.04x(NeighborQualityRating) + 42695.09x(GeneralConditionRating)

#(d) What is the predicted price of a house whose area is 3000 sq. feet with a neighbor hood ranking of 5 and a general condition ranking of 4?
#From the regression equation above we can get that :
#Theoritically:   y = -166694.46 +  88.02x1(Area) + 39917.04x2(NeighborQualityRating) + 42695.09x3(GeneralConditionRating) 
#Given : Area  = 3000
#NeighborQualityRating = 5
#GeneralConditionRating = 4
# Therefore y = -166694.46 + 88.02 * 3000 + 39917.04 * 5 + 42695.09 * 4 = 467731.1

# with R
new = data.frame(Area = 3000 , NeighborQualityRating = 5 ,GeneralConditionRating =4 )
predicited_price = predict(fit1,new)
predicited_price # 467743.8




#Question 2

#(a) Construct a linear regression model to predict uncovered unpaid taxes.
#Answer: 
AUDIT <- read.csv("D:/Downloads/AUDIT.csv")
fit2  =lm(UncoveredUnpaid ~ LaborHours + ComputerHours,data = AUDIT) 

#(b) Perform a significance test of the regression coefficients using the t-statistics in your regression model output. What do you find?
summary(fit2)
# From Summary,
# since, T-value of dependent variable(UncoveredUnpaid ) is -7.642 which is less than Alpha (0.05) significance level so the deoendent variable is significant 
# But the independent varibales LaborHours(8.453) and LaborHours(3.511) are found to be greater than Alpha 0.05 significance level so they are not significant.


#(c) Look at the scatter-plot of the regression residuals with each of the independent variables. Is there evidence of heteroscedasticity?
  fit.LaborHours = lm(UncoveredUnpaid ~ LaborHours,data = AUDIT)
  fit.ComputerHours =  lm(UncoveredUnpaid ~ ComputerHours,data = AUDIT)
  
  res.LaborHours = residuals(fit.LaborHours)
  res.ComputerHours = residuals(fit.ComputerHours)
  
  plot(res.LaborHours)
  abline(0,0)
  
  plot(res.ComputerHours)
  abline(0,0)
  
# From the plots we can conclude that there is NO pattern observed which  means that the variance of the residuals is not constant 
# meaning that there is no evidence of Heteroscedasticity in both res.LaborHours & res.ComputerHours.
  
#(d) Would you recommend IRS increase the number of computer hours devoted to auditing tax returns? Would you recommend that the IRS increase the number of field-audit hours? why or why not?

  summary(fit.LaborHours)
  
  summary(fit.ComputerHours)
  
#  From the above summary we can observe that the R-Squared Value of the Fitted model for  Labour Hours is 81% and that of ComputerHours is 25% which is less than Labour Hours
#  So,I would recommend increasing IRS for the number of field-audit hours.


