
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "Partner Risk Insurance",
    "version": "0.1",
    "description": """
    This module adds a new tab in the partner form to introduce risk insurance
     information.
    --Module of nan-tic nan_partner_insurance ported by Factor Libre to
     OpenERP 7
""",
    "author": "Factor Libre S.L, NaN·tic, AvanzOSC",
    'contributors': ["Daniel Campos <danielcampos@avanzosc.es>"],
    "website": "http://www.factorlibre.com",
    "depends": [
        'base',
    ],
    "category": "Custom Modules",
    "data": ['views/res_partner_view.xml'],
    "active": False,
    "installable": True
}
