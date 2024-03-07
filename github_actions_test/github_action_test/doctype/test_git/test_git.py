from frappe.model.document import Document

class TestGit(Document):
	def before_save(self):
		b = eval(sum([5,6]))
