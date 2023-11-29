# -*- coding: utf-8 -*-
# Copyright (c) 2023, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class PastYearList(Document):
    def validate(self):
        frappe.msgprint("This is called from server side")
        self.validate_diplicate_file_name()


    def validate_diplicate_file_name(self):
        attachment = []
        if self.mark_sheet in attachment:
                frappe.throw("Duplicate File Name {0}".format(self.mark_sheet))
            #attachment.append(self.mark_sheet)
        
        if self.pass_certificate:
            if self.pass_certificate in attachment:
                frappe.throw("Duplicate File Name {0}".format(self.pass_certificate))
            #attachment.append(self.pass_certificate)

        if self.cid:
            if self.cid in attachment:
                frappe.throw("Duplicate File Name {0}".format(self.cid))
            #attachment.append(self.cid)
