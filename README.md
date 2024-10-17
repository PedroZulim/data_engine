# Data Cleaning and Transformation Challenge

## Objective

You are provided with a dataset containing several columns with some intentional inconsistencies and errors. Your task is to clean the dataset using appropriate techniques and export the cleaned data to a CSV file. Additionally, there are bonus tasks for creating new columns based on the existing data and establishing table relationships.

## Dataset Overview

The dataset contains the following columns that require cleaning and transformation:

- **first_name**: The first names in this column have some inconsistencies that need to be fixed. Ensure all entries follow a standard format.
- **last_name**: The last names in this column also contain errors that should be corrected to follow proper formatting.
- **email**: The email addresses in this column are not in a standard format. Identify the issues and correct them to valid email formats.
- **phone_number**: This column contains phone numbers that are inconsistently formatted. Standardize the phone numbers to a common format.
- **address**: Some addresses in this column are not in the correct order. Rearrange or format the addresses properly.

### Bonus Columns (Optional Tasks)

- **final_price**: Create a new column called `final_price` that calculates the final price for each purchase. Multiply the existing `price` column by the `amount` column to get the final price for each row.
- **currency_code**: Based on the existing `currency` column, create a new column named `currency_code` that standardizes the currency as a 3-letter code (e.g., USD, EUR, GBP). Ensure the correct code is assigned based on the currency.

### Bonus Task: Table Relationships

If possible, establish a table relationship between purchases and customer data by identifying a common key (like an `id` column or `email` address) that could be used to link multiple purchases to a single customer. Document how you would implement this relationship using Pandas or SQL, and what improvements it would provide for future data analysis.

## Task Instructions

1. **Load the Data**: Load the dataset into a Pandas DataFrame to begin your analysis.
2. **Identify and Correct Errors**: Clean the specified columns (`first_name`, `last_name`, `email`, `phone_number`, and `address`). Ensure that the data follows a consistent format and correct any apparent errors.
3. **Calculate `final_price`**: Create a new column called `final_price` that is the product of `price` and `amount`.
4. **Add `currency_code`**: Based on the values in the `currency` column, create a new `currency_code` column with the appropriate currency codes.
5. **Export the Cleaned Data**: Once the data is cleaned and the new columns are added, export the cleaned DataFrame to a CSV file.

## Deliverables

1. **Cleaned CSV file**: Submit the cleaned dataset as a CSV file, including the bonus columns if applicable.
2. **Code**: Submit your code or Jupyter Notebook that details how you cleaned and transformed the dataset.
3. **Bonus**: If you attempt the bonus task of creating a table relationship, explain how you implemented it and submit the associated code.

## Evaluation Criteria

- **Accuracy of data cleaning**: Correct identification and correction of errors.
- **Consistency of formatting**: Consistent formatting across the dataset.
- **Efficient use of Pandas/Regex**: Effective use of tools like Pandas or Regex to clean the data.
- **Proper calculation of `final_price`**: Accurate calculation and correct assignment of `currency_code`.
- **Quality of the code**: Readability, documentation, and maintainability.
- **Bonus points**: Creating a meaningful table relationship and documenting how it could improve analysis.

Good luck!
