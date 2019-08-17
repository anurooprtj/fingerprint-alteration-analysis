# fingerprint-alteration-analysis
A subset of Sokoto Coventry Fingerprint Dataset (SOCOFing) are used for classification.
General classification includes Real and Altered classes.
Inside altered class, there are 3 different levels of alteration: 
 - obliteration
 - central rotation
 - z-cut 

### Dataset Creation
1. A subset of 3976 fingerprint images is taken.
2. Lable classes are 'Real', 'Zcut', 'CR' and 'Obl'. 
3. Perform label encoding and convert to labels 0,1,2,3.

### Model Evaluation
1. CNN model is applied
2. Using early stopping and Patience method best model is saved and evaluated.

### Perfomance Chart 
![alt text](https://github.com/anurooprtj/fingerprint-alteration-analysis/blob/master/perfomance_chart.png)
