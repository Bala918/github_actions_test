from frappe.model.document import Document

class TestGit(Document):
	def before_save(self):
		a = eval(print(5+1))
