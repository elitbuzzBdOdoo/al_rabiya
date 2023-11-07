{
    'name': 'alrabiya',
    # 'version': 'Version',
    # 'summary': 'Summery',
    # 'description': 'Description',
    # 'category': 'Category',
    'author': 'Elitbuzz-bd Team',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['base', 'crm', 'purchase', 'stock', 'sale', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'data/sequence.xml',

        'wizard/customer_wise_product_wizard.xml',

        'purchase_inherit/report_purchase_view.xml',

        'crm_inherit/customer_type_view.xml',
        'crm_inherit/inherit_crm_view.xml',
        'crm_inherit/emirates_view.xml',
        'crm_inherit/inherit_res_partner_view.xml',

        'purchase_inherit/purchase_type_view.xml',
        'purchase_inherit/inherit_purchase_view.xml',

        'inventory_inherit/eb_product_template_type_view.xml',
        'inventory_inherit/product_template_cost_hide.xml',
        'inventory_inherit/product_variant_cost_hide.xml',
        'inventory_inherit/eb_category_product_view.xml',

        'sale_inherit/eb_sale_inherit_payment_term.xml',
        'sale_inherit/eb_res_config_views.xml',
        'sale_inherit/eb_sale_order.xml',
        'sale_inherit/eb_credit_limit/res_partner_view.xml',
        'sale_inherit/eb_credit_limit/sale_inherit_view.xml',
    ],
    # 'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}
