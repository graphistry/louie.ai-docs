# Perspective: Expressions - Split By

Split By

A split by splits the dataset by the unique values of each column used as a split by. 

The underlying dataset is not aggregated, and a new column is created for each unique value of the split by. 

Each newly created column contains the parts of the dataset that correspond to the column header, i.e. a View that has ["State"] as its split by will have a new column for each state.

![Split By Example](./images/user/042_Perspective__Expressions___Split_By_1.png)

