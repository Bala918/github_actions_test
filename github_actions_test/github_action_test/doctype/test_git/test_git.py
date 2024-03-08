from frappe.model.document import Document

class TestGit(Document):
	def before_save(self):		
		doc = frappe.get_doc({"Doctype":self.doctype, "name":self.name})
		a = eval(sum([5,6]))
		lst = [50, 6, 6, 7,4,33]
		if not lst:
			return None
		max_num = lst[0]
		for num in lst:
			if num > max_num:
				max_num = num
				print(max_num)
				break;
