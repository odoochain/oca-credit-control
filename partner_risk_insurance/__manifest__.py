# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Risk Insurance",
    "version": "15.0.1.0.2",
    "development_status": "Production/Stable",
    "summary": "Risk insurance partner information",
    "author": "AvanzOSC,"
    "Tecnativa,"
    "Factor Libre S.L,"
    "NaN·tic,"
    "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "website": "https://github.com/OCA/credit-control",
    "depends": ["mail"],  # required for tracking=True attribute
    "category": "Credit Control",
    "data": ["security/ir.model.access.csv", "views/res_partner_view.xml"],
    "installable": True,
    "maintainers": ["Daniel-CA", "sergio-teruel", "omar7r", "Tardo"],
}
