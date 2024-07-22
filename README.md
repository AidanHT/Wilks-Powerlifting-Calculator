# Wilks-Powerlifting-Calculator
The Wilks Powerlifting Score Calculator Class is used to create a valuation that represents the relative strength of powerlifters in different weight classes.

********************************************************************************************************************************************************************
Description of Data

The “Powerlifting Competition Data.csv” file created by Kaggle user ‘kukuroo3’, contains information on competitive powerlifters at powerlifting competitions in the past 3 decades from countries around the world. The information includes the recorded name, sex, equipment used on lifts, age, bodyweight, squat and deadlift in kilograms of over 11,000 unique competitive powerlifters during official powerlifting competitions. The restrictions and datatypes of each of these fields/attributes of a powerlifter can be found below.

1.  Name: string
2. Sex: 1 character string (‘F’, ‘M’)
3. Equipment: string
4. Age: float value greater than zero 
5. Bodyweight: float value greater than zero
6. Squat: float value greater than zero
7. Deadlift: float value greater than zero

This powerlifting data file could be useful for powerlifters, individuals or organizations who want to find trends and correlations between lifts and other factors. It could also be used by these groups to create scores and valuations for powerlifters for comparison and to search for other powerlifters' information. 

********************************************************************************************************************************************************************
Description of Valuation 

The Wilks Powerlifting Score Calculator Class is used to create a valuation that represents the relative strength of powerlifters in different weight classes. The program finds the Wilks coefficient or Wilk’s formula which uses the powerlifter’s body weight to create a relative strength value between different powerlifters. This value is then multiplied by the total lift (squat, deadlift and predicted bench) of a competitive powerlifter to create a valuation. This powerlifting score was chosen because it is very popular and allows for a fair comparison of relative strength between powerlifters of different weights.


********************************************************************************************************************************************************************
References
kukuroo3. (2022, June 23). Powerlifting benchpress weight predict. Kaggle. https://www.kaggle.com/datasets/kukuroo3/powerlifting-benchpress-weight-predict?resource=download&select=X_test.csv 

