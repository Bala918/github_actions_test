from frappe.model.document import Document

class GitWorkflow(Document):
	def before_save():
		frappe.msgprint("Done")		
