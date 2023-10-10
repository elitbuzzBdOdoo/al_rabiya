**CRM Module**
* _Add Label/Field_
  * Enquiry Source (Master Data): Master Data field (Name* and Code). 
  * Customer Type (Master Data): Master Data field (Name* and Code). 
  * Additional fields required are: Salesperson (Already Exist), Region, Emirates 
  * Emirates (Master data): Master Data field (Name* and Code).

**Purchase Module**
* _Add Label/Field_ 
  * Purchase Type (Master data)
    * LPO
    * IPO 
* _Landed Cost_
  * Landed cost charges are to be considered while delivery happens for the purchased items.

**Inventory Module**
* Product Code (When create a new product this will generate a unique Code). It is needed in internal reference. 
* Category field needed in product entry form under the company.
* Product cost price hide from product and product variant.

**Sales Order**
* Shows that product is unavailable (red mark), the system should not allow the salesperson to confirm the sales order. The system should show a warning that the product is not available in stock.
* _Payment Term_ in quotation is made mandatory.
* _**Partner/customer wise credit limit and credit period field.**_
  * Sales order to have the credit limit and credit period and if the credit amount comes near to the limit, notification to pop up and further no credit sales to be approved.
  * Similarly, for credit period, if the credit period is less then quotation date then also a notification popup and no credit sale to be approved.
