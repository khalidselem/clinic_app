from __future__ import unicode_literals
from frappe import _
import frappe
def get_data():
        return [
                {
                        "label": _("Clinic"),
                        "icon": "fa fa-table",
                        "items": [
                                {
                                        "type": "doctype",
                                        "label": _("Clinic Assets"),
                                        "name": "Clinic Assets",
                                        "description": _("Clinic Assets")
                                },
                                {
                                        "type": "doctype",
                                        "label": _("Clinic Equipment Checklist"),
                                        "name": "Clinic Equipment Checklist",
                                        "description": _("Clinic Equipment Checklist")
                                },
                                {
                                        "type": "doctype",
                                        "label": _("Ambulance Equipment Checklist"),
                                        "name": "Ambulance Equipment Checklist",
                                        "description": _("Ambulance Equipment Checklist")
                                }
                        ]
                },
                {
                        "label": _("Daily Work"),
                        "icon": "fa fa-table",
                        "items": [
                                {
                                        "type": "doctype",
                                        "label": _("Sites Follow Up"),
                                        "name": "Sites Follow Up",
                                        "description": _("Sites Follow Up")
                                }
                        ]
                }
        ]
