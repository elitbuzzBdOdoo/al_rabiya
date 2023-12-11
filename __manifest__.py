{
    'name': 'alrabiya',
    # 'version': 'Version',
    # 'summary': 'Summery',
    # 'description': 'Description',
    # 'category': 'Category',
    'author': 'Elitbuzz-bd Team',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['base', 'crm', 'purchase', 'stock', 'sale', 'sale_management', 'account', 'product', 'account_accountant'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'data/sequence.xml',
        'data/credit_limit_approval_mail.xml',

        'wizard/sale_by_item_wizard.xml',
        'wizard/stock_summary_wizard.xml',
        'wizard/warning_wizard.xml',

        'sale_inherit/eb_res_config_views.xml',
        'sale_inherit/eb_sale_order.xml',
        'sale_inherit/eb_credit_limit/credit_limit_res_partner_view.xml',
        'sale_inherit/eb_credit_limit/credit_limit_sale_order_view.xml',

        'purchase_inherit/report_purchase_view.xml',

        'crm_inherit/customer_type_view.xml',
        'crm_inherit/inherit_crm_view.xml',
        'crm_inherit/emirates_view.xml',
        'crm_inherit/region_view.xml',
        'crm_inherit/inherit_res_partner_view.xml',

        'purchase_inherit/purchase_type_view.xml',
        'purchase_inherit/inherit_purchase_view.xml',

        'inventory_inherit/eb_product_template_type_view.xml',
        'inventory_inherit/product_template_cost_hide.xml',
        'inventory_inherit/product_variant_cost_hide.xml',
        'inventory_inherit/eb_brand_product_view.xml',
        'inventory_inherit/eb_category_product_view.xml',
        'inventory_inherit/eb_sub_category_product_view.xml',

        'report/report.xml',
        'report/sale_by_item_template.xml',
        'report/stock_summary_pdf_template_report.xml',
    ],
    'installable': True,
    'auto_install': False
}
