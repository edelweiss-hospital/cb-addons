# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Invoice Integration Email",
    "summary": """
        Send invoices through emails as an integration method""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "author": "Creu Blanca",
    "website": "www.creublanca.es",
    "depends": ["edi_account", "l10n_es_facturae"],
    # TODO: Remove facturae after migration
    "data": ["data/method_data.xml", "views/res_partner_view.xml"],
}