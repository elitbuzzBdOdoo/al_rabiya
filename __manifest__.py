{
    'name': 'alrabiya',
    # 'version': 'Version',
    # 'summary': 'Summery',
    # 'description': 'Description',
    # 'category': 'Category',
    'author': 'Elitbuzz-bd Team',
    # 'website': 'Website',
    # 'license': 'License',
    'depends': ['crm', 'purchase'],
    'data': [
        'security/ir.model.access.csv',

        'crm_inherit/enquiry_source_view.xml',
        'crm_inherit/customer_type_view.xml',
        'crm_inherit/inherit_crm_view.xml',
        'purchase_inherit/purchase_type_view.xml',
        'purchase_inherit/inherit_purchase_view.xml',
    ],
    # 'demo': ['Demo'],
    'installable': True,
    'auto_install': False
}
