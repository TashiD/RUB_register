# Copyright (c) 2013, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    frappe.msgprint("hi")
    data = get_daa(filters)
    columns = get_columns(filters)
    return data, columns, test


def get_data(filters):
    query = """
            SELECT name, index_no, cid, email_address, student_contact_no, 
            guardian_contact_no, mark_sheet, pass_certificate, status, remarks 
            FROM `tabPast Year List` 
    """
    if filters.get("status"):
        query += " and status = '{0}' ".format(filters.get(status))
   
    frappe.msgprint("i am working")

    data = frappe.db.sql(query, as_dict = 1)
    return data 

def get_columns(filters): 

    columns = [
        {
            'fieldname': 'name',
            'label': _('Document Link'),
            'fieldtype': 'Link',
            'options': 'Past Year List'
        },
        {
            'fieldname': 'index_no',
            'label': _('Index No'),
            'fieldtype': 'Int'
        },
        {
            'fieldname': 'cid',
            'label': _('CID No'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'email_address',
            'label': _('Email Address'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'student_contact_no',
            'label': _('Student Contact No'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'guardian_contact_no',
            'label': _('Gurdain Contact No'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'mark_sheet',
            'label': _('Mark Sheet'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'pass_certificate',
            'label': _('Pass Certificate'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'status',
            'label': _('Status'),
            'fieldtype': 'Data'
        },
		{
            'fieldname': 'remarks',
            'label': _('Remarks'),
            'fieldtype': 'Data'
        }
    ]
    return columns
