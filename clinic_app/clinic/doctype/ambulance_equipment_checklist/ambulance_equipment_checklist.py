# Copyright (c) 2021, Ahmed Reda and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AmbulanceEquipmentChecklist(Document):
	def before_submit(self):
		self.check_fields_not_null_before_submit()
	'''
	This Function `ll set all ambulance assets item from Clinc Assets to  Ambulance Equipment Checklist Item

	Parameters:
		ambulance_assets (frappe.dic): this `ll hold Clinic Assets document  
		
	'''
	def set_child_table(self,ambulance_assets):
		for item in ambulance_assets.get('ambulance_assets_item'):
			row = self.append('ambulance_equipment_checklist_item',{})
			row.equipment_in_english= item.equipment_in_english
			row.equipment_in_arabic= item.equipment_in_arabic
			row.quantity= item.quantity
			
	'''
	This Function check all ambulance equipment checklist item rows to have a value either `ll throw exception  
	'''	
	def check_fields_not_null_before_submit(self):
		for row in self.get('ambulance_equipment_checklist_item'):
			yes_have_value = True if row.yes else False 
			no_have_value = True if row.no else False 
			if not yes_have_value and not no_have_value:
				frappe.throw("You Can not Submit without set value for Yes or No")
	
	'''
	This Function `ll get all ambulance assets from Clinc Assets 

	Parameters:
		docname (str): this `ll hold document name 

	'''
	@frappe.whitelist()
	def get_ambulance_asset_doc(self,docname):
		doc = frappe.get_doc('Clinic Assets',docname)
		self.set_child_table(doc)
	'''
	This Function `ll remove all ambulance assets from it`s table 
	'''
	@frappe.whitelist()
	def remove_all_records_on_change(self):
		table_has_rows = self.get('ambulance_equipment_checklist_item')
		if table_has_rows:
			self.get('ambulance_equipment_checklist_item').clear()
		else: return