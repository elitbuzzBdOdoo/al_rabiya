# al_rabiya
**Purchase Module**
  **Add Label/Field**
  Purchase Type will be Master data: Code and Name*
  2 Purchase Type: 1.LPO  2.IPO


**CRM Module**
**Add Label/Field**
  Enquiry Source (Master Data)
  Master Data field (Name* and Code).
  Customer Type (Master Data).
  Master Data field (Name* and Code).
  Additional fields required are – 
  Salesperson (Already Exist), Region, Emirates
  Emirates (Master data) 
  Master Data field (Name* and Code).

  
**Inventory Module**
  Product Code in internal Reference (When create a new product this will be generate a unique Code).


**Sales Module**

  **Sales Order (Quotation)**
   In sales order, shipping cost is to be shown separately after Total cost with VAT.
  
  **Sales commission** (Full Customization)  (Formulae to be needed)
   Existing customer – A percentage of the total sales amount is given to the salesperson. (Formulae to be needed)
   Existing customer (New Product) -  If a new product is sold to an existing customer, a separate commission is given to the salesperson.
   New Customer -  A different sales commission is given to the salesperson.

**Reports** (Date range)
(Sales Commission Report) 
  A report to track the sales of existing customers, existing customer’s new products and new customers should be available.
   Sales by salesperson 
   Sales by customer
   Sales by Item

  **Sales Order Warning**
   * Shows that product is unavailable (red mark), the system should not allow the salesperson to confirm the sales order. The system should show a warning that the product is not available in stock.
   * Payment Term
     Payment terms in quotation should be made mandatory.
   * Invoice Confirm
     The sales order is created then the invoicing happens, which will be done by the office team. So, Salesperson should not have access to do this.
   * Credit Limit
     Sales order to have a credit limit and credit period field and if the credit amount comes near to the limit, notification to pop up and further no credit sales to be approved. Similarly, for credit period also.
   * Shipping Cost
     Shipping cost is needed to under the total cost.
