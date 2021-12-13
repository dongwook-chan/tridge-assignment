# Dataset
## Q1. Normalization & Simplification
### 1. `Product` Column
`Product` column can be split into 2: `Product Name` and `Product Id`
### 2. `Variety` Column
`Variety` Column consists of three part of which the leading 2 are trivial.  
The column values must be replaced with third part.

This column contains aliases such as 
`(=Cerises)`, `(=Kamaroza)` and `(= Green Garlic=Young Garlic)`.  
Aliases must be removed and maintained in a separate lookup table.

### 3. `Grades` Column
#### A. Columns cannot have tables as values
`Grades` column contains a set of grade values: 
`Combination of U.S. Extra Fancy and U.S. Fancy`  

**Solutions**  
1. Create separate table for grade
    * This is the conventional normalization method.
    * However, this may increase the cost of `SELECT` due to join.
2. Define `Subject` column as `JSON` type
    * This is denormalization method to minimize join cost.
3. Switch to NoSQL

#### B. Grades belong to different criteria.
This column needs to be split into 2: `Grade Criteria` and `Grades`.  

### 4. `Region` Column
#### A. Unify column values
`Chillán, Diguillín` and `Chillán, Diguillín Province` refer to the same region.

#### B. Columns cannot have tables as values
Some of the column values contain 2 hierarchical region names.

#### C. Mind the encoding of the data
`Chillán, Diguillín`, `Concepción` are column values that can not be interpreted in ascii encoding.   
Encoding for this dataset must be set to `utf-8`. 

### 5. {datetime} Columns
Each time data for new date is generated, new column must be added.  
`ALTER` statements can be very expensive on large tables.  
These temporal columns suggest that this table is bound grow.  

These Columns must be merged into a single column `Date`.  
(Or any other name not included in target RDBMS's reserved keyword list.)  
Column name will be now column value of `Date` and what used to be column values will be the column value of `Figure` in the new design.

`Date` column can further be partitioned and comes advantages such as:
1. High performance by eliminating large amounts of I/O
2. Predicates in `SELECT` eliminates unrelated partition to increase query performance
3. Time consuming maintenance operations can be minimized by breaking them down into smaller operations
Plus, this does not harm the analytical potential of the dataset.

**Solutions**
1. Split the column into 2: `Region1` and `Region2`
2. Keep only 1 of the region names.

## Q2. Data Analysis
Linear regression on column values will lead to valuable insights that can add value to the business.  
### 1. (`Country`, `Region`) -> `Grades`
Regions producing high quality products can be prioritized.
### 2. `Date` -> `Figure`
It is unclear what exactly what `Figure` means.  
However, its seasonal fluctuation suggests it is related to the scale of production or transaction of the product.  
At `Date`s when `Figures` are high, company can assign more resources to boost transactions, or sourcing of products.  


## Q3. Loading Data into RDBMS
Below are the methods to load csv file into RDBMS.
### 1. Convert csv to sql
* Appropriate `CREATE TABLE` and `INSERT` statements can be generated.
* The resulting file merely needs to be applied using client-server protocol.  
### 2. Work with Clients for RDBMS
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
### Options to Mind
Encoding must be set to `utf-8`.