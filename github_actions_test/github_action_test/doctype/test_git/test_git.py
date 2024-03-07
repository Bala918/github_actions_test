from frappe.model.document import Document

class TestGit(Document):
	def before_save():
		frappe.msgprint("Done")
		b = eval(print(5+2))
