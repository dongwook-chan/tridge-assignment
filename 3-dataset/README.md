# Dataset
## Columns
### `Product` Column
`Product` column can be split into 2: `Product Name` and `Product Id`
### `Variety` Column
`Variety` Column consists of three part of which the leading 2 are trivial.  
The column values must be replaced with third part.

This column contains aliases such as 
`(=Cerises)`, `(=Kamaroza)` and `(= Green Garlic=Young Garlic)`.  
Aliases must be removed and maintained in a separate lookup table.

### `Grades` Column
#### 1. Columns cannot have tables as values
`Grades` column contains a set of grade values: 
`Combination of U.S. Extra Fancy and U.S. Fancy`  

**Solutions**  
1. Create separate table for grade
    * This is the conventional normalization method.
    * However, this may increase the cost of `SELECT` due to join.
2. Define `Subject` column as `JSON` type
    * This is denormalization method to minimize join cost.
3. Switch to NoSQL

#### 2. Grades belong to different criteria.
This column needs to be split into 2: `Grade Criteria` and `Grades`.  

### `Region` Column
#### 1. Unify column values
`Chillán, Diguillín` and `Chillán, Diguillín Province` refer to the same region.

#### 2. Columns cannot have tables as values
Some of the column values contain 2 hierarchical region names.

#### 3. Mind the encoding of the data
`Chillán, Diguillín`, `Concepción` are column values that can not be interpreted in ascii encoding.   
Encoding for this dataset must be set to `utf-8`. 

### {datetime} Column
Each time data for new date is generated, new column must be added.  
`ALTER` statements can be very expensive on large tables.  
These temporal columns suggest that this table is bound grow.  

These Columns must be merged into a single column `Date`.  
(Or any other name not included in target RDBMS's reserved keyword list.)  
Column name will be now column value of `Date` and what used to be column values will be the column value of `Figure` in the new design.

`Date` column can further be partitioned and comes

**Solutions**
1. Split the column into 2: `Region1` and `Region2`
2. Keep only 1 of the region names.

## Loading data to RDBMS
Below are the methods to load csv file into RDBMS.
### using clients for RDBMS
#### MySQL
* mysql client
  * `LOAD DATA` statement
* mysqlimport
  * `--use-threads` option for multi-threaded load 
* Parallel Table Import Utility (MySQL >= 8.0.17)
#### PostgreSQL
* psql client
  * `COPY` statement
* psycopg2 package 
  * `copy_to`, `copy_expert` and `copy_execute` method
### options to mind
Encoding must be set to `utf-8`.