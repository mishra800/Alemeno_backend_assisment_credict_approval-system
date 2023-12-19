Key Components of a Credit Approval System:
Customer Data:

Includes personal information about the customer, such as name, phone number, monthly salary, current debt, and approved credit limit.
Loan Data:

Contains details about past and existing loans, such as loan amount, tenure, interest rate, monthly repayment (EMI), EMIs paid on time, start date, and end date.
Credit Score Calculation:

The system evaluates a customer's credit score based on various factors, including past loans paid on time, the number of loans taken in the past, loan activity in the current year, and the approved loan volume.
Loan Eligibility Assessment:

Determines whether a customer is eligible for a new loan based on their credit score. Criteria may include credit rating thresholds, the number of current loans, and the relationship between current EMIs and monthly salary.
Loan Approval Criteria:

Defines specific rules for approving loans based on credit scores:
If credit rating > 50, approve the loan.
If 50 > credit rating > 30, approve loans with an interest rate > 12%.
If 30 > credit rating > 10, approve loans with an interest rate > 16%.
If credit rating < 10, do not approve any loans.
If the sum of all current EMIs > 50% of monthly salary, do not approve any loans.
Correction of Interest Rate:

If the interest rate specified in the loan request does not match the credit limit, the system corrects the interest rate to the appropriate value.
API Endpoints:
Ingest Data:

Background task to ingest customer and loan data from Excel files into the system.
Check Loan Eligibility:

API to assess a customer's credit score and determine loan eligibility based on specified criteria.
Create Loan:

API for processing a new loan request, considering the customer's credit score and approval criteria.
View Loan Details:

API to retrieve details about a specific loan, including customer information, loan amount, interest rate, monthly installment, and tenure.
View All Loans by Customer:

API to retrieve a list of all current loans for a given customer, including loan ID, amount, interest rate, monthly installment, and repayments left.
General Guidelines:
Ensure code quality, organization, and segregation of responsibilities.
Dockerize the application and use PostgreSQL as the database.
Consider adding unit tests for bonus points in code assessment.
Implementing a Credit Approval System helps financial institutions make informed decisions, mitigating risks associated with extending credit while providing individuals with access to financial resources.
