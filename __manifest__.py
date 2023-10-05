{
    'name': 'alrabiya',
    # 'version': 'Version',
    # 'summary': 'Summery',
    # 'description': 'Description',
    # 'category': 'Category',
    'author': 'Elitbuzz-bd Team',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['crm', 'purchase', 'stock', 'sale', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        
        'purchase_inherit/report_purchase_view.xml',

        'crm_inherit/enquiry_source_view.xml',
        'crm_inherit/customer_type_view.xml',
        'crm_inherit/inherit_crm_view.xml',
        'purchase_inherit/purchase_type_view.xml',
        'purchase_inherit/inherit_purchase_view.xml',
        'inventory_inherit/eb_product_template_type_view.xml',
        'sale_inherit/eb_sale_inherit_payment_term.xml',
        'sale_inherit/eb_res_config_views.xml',
        'sale_inherit/eb_sale_order.xml',

    ],
    # 'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}
