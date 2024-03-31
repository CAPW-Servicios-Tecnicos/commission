import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-commission",
    description="Meta package for oca-commission Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-sale_commission',
        'odoo14-addon-sale_commission_advance',
        'odoo14-addon-sale_commission_agent_restrict',
        'odoo14-addon-sale_commission_check_deposit',
        'odoo14-addon-sale_commission_delegated_partner',
        'odoo14-addon-sale_commission_formula',
        'odoo14-addon-sale_commission_geo_assign',
        'odoo14-addon-sale_commission_geo_assign_product_domain',
        'odoo14-addon-sale_commission_partial_settlement',
        'odoo14-addon-sale_commission_pricelist',
        'odoo14-addon-sale_commission_product_criteria',
        'odoo14-addon-sale_commission_product_criteria_discount',
        'odoo14-addon-sale_commission_product_criteria_domain',
        'odoo14-addon-sale_commission_queued',
        'odoo14-addon-sale_commission_salesman',
        'odoo14-addon-sale_quick_commission',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
