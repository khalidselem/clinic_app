// Copyright (c) 2021, Ahmed Reda and contributors
// For license information, please see license.txt

frappe.ui.form.on('Clinic Equipment Checklist', {
	refresh:function(frm){ 
		hide_btn('.grid-remove-rows')
		hide_btn('.grid-remove-all-rows')
	},clinic_assets: function(frm) {
		frm.call('remove_all_records_on_change').then(r => {
			if(frm.doc.clinic_assets){
				frm.call('get_clinic_asset_doc',{docname:frm.doc.clinic_assets})
			}
		})
	},yes:function(frm){
		select_all(frm,"yes")
	},no:function(frm){
		select_all(frm,"no")
	}
});
frappe.ui.form.on("Clinic Equipment Checklist Item",{
	// this trigger event when you try to click edit label on the record 
	form_render:function(frm, cdt, cdn){
		hide_btn('.grid-delete-row')
	},yes:function(frm,cdt,cdn){
		let row = frappe.get_doc(cdt, cdn)
		// to validate check box and make sure both not clicked 
		if(row.no){
			row.yes = 0
			frm.refresh_fields()
			frappe.throw("You can not check both Yes and No")
		}
	},no:function(frm,cdt,cdn){
		let row = frappe.get_doc(cdt, cdn)
		// to validate check box and make sure both not clicked 
		if(row.yes){
			row.no = 0
			frm.refresh_fields()
			frappe.throw("You can not check both Yes and No")
		}
	}
});
/**
 * this hide_btn function is for change css props using .find method in jquery library 
 * @param {*} btn_name: is a name class of the element you can get it using insbect elment in your browser
 */
function hide_btn(btn_name){
	$('*[data-fieldname="clinic_equipment_checklist_item"]').find(btn_name).css({
		"display": "none"
	})
}
function select_all(frm,option){
	if(option=="yes"){
		for(let item of frm.doc.clinic_equipment_checklist_item){
			item.yes = 1
			item.no = 0
			frm.refresh_fields()
		}
	}else{
		for(let item of frm.doc.clinic_equipment_checklist_item){
			item.no = 1
			item.yes = 0
			frm.refresh_fields()
		}
	}
}