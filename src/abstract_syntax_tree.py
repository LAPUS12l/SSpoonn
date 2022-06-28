import lexer
from lexer import *
import os
import time
loop_hand = { }
def o3(todo):
	global strings
	global integers
	global line
	token = []
	for this in todo:
		if this[0:1] == " ":
			this = this.replace(" ", "", 1)
			if this[0:7] == "println":

				this = this.replace("println", "", 1)
				if this[0:1] == "[":
					if this[len(this)-1:len(this)] == "]":

						this = this.replace("[", "", 1)
						index = this.index("]")
						string = this[0:index]
						token.append({"key":"NEWLINE", "value":string})
					else:
						error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
				else:
					error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
			elif this[0:3] == "int":
				this = this.replace("int", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"Integer_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
						error.illgal_syn("Invalid syntax", line)
			elif this[0:6] == "input ":
				this = this.replace("input ", "", 1)
				index = this.index(" ", 1)
				token.append({"key":"input", "todo":this})
			elif this[0:6] == "string":
				this = this.replace("string", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"String_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
					error.illgal_syn("Invalid syntax", line)
			elif this[0:7] == "process":
					this = this.replace("process", "", 1)
					if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
						this = this[1:len(this)-1]
						token.append({"key":"osprocess", "todo":this})
					else:
						error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:4] == "call":
				this = this.replace("call", "", 1)
				if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"call", "file":this})
				else:
					error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:5] == "sleep":
				this = this.replace("sleep", "")
				if this[0] == "[" and this[len(this)-1] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"sleep", "duration":this})
				else:
					error.illgal_syn("No blocks found '[' ']'")
		
	for syntax in token:
		
		if syntax["key"] == "NEWLINE":
			try:
				value = str(syntax["value"])
				exec("print(str("+value+"))", strings, integers)
			except:
				error.no_var("No varriable found or int is in the line", line)
		elif syntax["key"] == "String_var":
			value = eval("str("+syntax["value"]+")", strings, integers)
			strings[syntax["name"]] = value
		elif syntax["key"] == "Integer_var":
			value = eval("int("+syntax["value"]+")", integers, strings)
			integers[syntax["name"]] = value
		elif syntax["key"] == "input":
			st = syntax["todo"]
			middle = len(st)
			end = len(st)
			had_hol_n = False
			if ' -p ' in st:
				middle = st.index(" -p ")
				had_hol_n = True
			if had_hol_n is True:
				holder = eval(st[0:middle], strings)
				strings[st[middle+4:end]] = input(holder)
		elif syntax["key"] == "osprocess":
			pro = syntax["todo"]
			if pro[0:1] == '"' and pro[len(pro)-1:len(pro)] == '"':
				os.system(pro[1:len(pro)-1])
			else:
				try:
					os.system(strings[pro])
				except:
					error.illgal_syn("No varriable found", line)
		elif syntax["key"] == "call":
			file = syntax["file"]
			if file[0:1] == '"' and file[len(file)-1:len(file)] == '"':
				file = file[1:len(file)-1]
			else:
				try:
					file = strings[file]
							
				except:
					error.illgal_syn("No varriable found", line)
			try:
				os.system("python SSpoon.py "+file)
			except:
				error.illgal_syn("No file found")
		elif syntax["key"] == "sleep":
			dur = syntax["duration"]
			try:
				time.sleep(int(dur))
			except:
				try:
					time.sleep(integers[dur])
				except:
					error.illgal_syn("No varriable found", line)
def o2(todo):
	global strings
	global integers
	global line
	token = []
	for this in todo:
		if this[0:1] == " ":
			this = this.replace(" ", "", 1)
			if this[0:7] == "println":

				this = this.replace("println", "", 1)
				if this[0:1] == "[":
					if this[len(this)-1:len(this)] == "]":

						this = this.replace("[", "", 1)
						index = this.index("]")
						string = this[0:index]
						token.append({"key":"NEWLINE", "value":string})
					else:
						error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
				else:
					error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
			elif this[0:3] == "int":
				this = this.replace("int", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"Integer_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
						error.illgal_syn("Invalid syntax", line)
			elif this[0:6] == "input ":
				this = this.replace("input ", "", 1)
				index = this.index(" ", 1)
				token.append({"key":"input", "todo":this})
			elif this[0:6] == "string":
				this = this.replace("string", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"String_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
					error.illgal_syn("Invalid syntax", line)
			elif this[0:7] == "process":
					this = this.replace("process", "", 1)
					if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
						this = this[1:len(this)-1]
						token.append({"key":"osprocess", "todo":this})
					else:
						error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:4] == "call":
				this = this.replace("call", "", 1)
				if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"call", "file":this})
				else:
					error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:5] == "sleep":
				this = this.replace("sleep", "")
				if this[0] == "[" and this[len(this)-1] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"sleep", "duration":this})
				else:
					error.illgal_syn("No blocks found '[' ']'")
		
	for syntax in token:
		
		if syntax["key"] == "NEWLINE":
			try:
				value = str(syntax["value"])
				exec("print(str("+value+"))", strings, integers)
			except:
				error.no_var("No varriable found or int is in the line", line)
		elif syntax["key"] == "String_var":
			value = eval("str("+syntax["value"]+")", strings, integers)
			strings[syntax["name"]] = value
		elif syntax["key"] == "Integer_var":
			value = eval("int("+syntax["value"]+")", integers, strings)
			integers[syntax["name"]] = value
		elif syntax["key"] == "input":
			st = syntax["todo"]
			middle = len(st)
			end = len(st)
			had_hol_n = False
			if ' -p ' in st:
				middle = st.index(" -p ")
				had_hol_n = True
			if had_hol_n is True:
				holder = eval(st[0:middle], strings)
				strings[st[middle+4:end]] = input(holder)
		elif syntax["key"] == "osprocess":
			pro = syntax["todo"]
			if pro[0:1] == '"' and pro[len(pro)-1:len(pro)] == '"':
				os.system(pro[1:len(pro)-1])
			else:
				try:
					os.system(strings[pro])
				except:
					error.illgal_syn("No varriable found", line)
		elif syntax["key"] == "call":
			file = syntax["file"]
			if file[0:1] == '"' and file[len(file)-1:len(file)] == '"':
				file = file[1:len(file)-1]
			else:
				try:
					file = strings[file]
							
				except:
					error.illgal_syn("No varriable found", line)
			try:
				os.system("python SSpoon.py "+file)
			except:
				error.illgal_syn("No file found")
		elif syntax["key"] == "sleep":
			dur = syntax["duration"]
			try:
				time.sleep(int(dur))
			except:
				try:
					time.sleep(integers[dur])
				except:
					error.illgal_syn("No varriable found", line)
def o(todo):
	global strings
	global integers
	global line
	token = []
	for this in todo:
		if this[0:1] == " ":
			this = this.replace(" ", "", 1)
			if this[0:7] == "println":

				this = this.replace("println", "", 1)
				if this[0:1] == "[":
					if this[len(this)-1:len(this)] == "]":

						this = this.replace("[", "", 1)
						index = this.index("]")
						string = this[0:index]
						token.append({"key":"NEWLINE", "value":string})
					else:
						error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
				else:
					error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
			elif this[0:3] == "int":
				this = this.replace("int", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"Integer_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
						error.illgal_syn("Invalid syntax", line)
			elif this[0:6] == "input ":
				this = this.replace("input ", "", 1)
				index = this.index(" ", 1)
				token.append({"key":"input", "todo":this})

			elif this[0:6] == "string":
				this = this.replace("string", "", 1)
				if this[0:1] == " ":
					this = this.replace(" ", "", 1)
					if "=" in this:
						index = this.index("=")
						name = this[0:index]
						if " " in name:
							error.parametter("Tab and spaces in name", line)
						else:
							end = len(this)
							token.append({"key":"String_var", "value":this[index+1:end], "name":name})
					else:
						error.parametter("Missing '=' to get name and value", line)
				else:
					error.illgal_syn("Invalid syntax", line)
			elif this[0:7] == "process":
					this = this.replace("process", "", 1)
					if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
						this = this[1:len(this)-1]
						token.append({"key":"osprocess", "todo":this})
					else:
						error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:4] == "call":
				this = this.replace("call", "", 1)
				if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"call", "file":this})
				else:
					error.illgal_syn("No blocks found '[' ']'", line)
			elif this[0:5] == "sleep":
				this = this.replace("sleep", "")
				if this[0] == "[" and this[len(this)-1] == "]":
					this = this[1:len(this)-1]
					token.append({"key":"sleep", "duration":this})
				else:
					error.illgal_syn("No blocks found '[' ']'")
		else:
			error.illgal_syn("unmatch indentent")
	for syntax in token:
		
		if syntax["key"] == "NEWLINE":
			try:
				value = str(syntax["value"])
				exec("print(str("+value+"))", strings, integers)
			except:
				error.no_var("No varriable found or int is in the line", line)
		elif syntax["key"] == "String_var":
			value = eval("str("+syntax["value"]+")", strings, integers)
			strings[syntax["name"]] = value
		elif syntax["key"] == "Integer_var":
			value = eval("int("+syntax["value"]+")", integers, strings)
			integers[syntax["name"]] = value
		elif syntax["key"] == "input":
			st = syntax["todo"]
			middle = len(st)
			end = len(st)
			had_hol_n = False
			if ' -p ' in st:
				middle = st.index(" -p ")
				had_hol_n = True
			if had_hol_n is True:
				holder = eval(st[0:middle], strings)
				strings[st[middle+4:end]] = input(holder)
		elif syntax["key"] == "osprocess":
			pro = syntax["todo"]
			if pro[0:1] == '"' and pro[len(pro)-1:len(pro)] == '"':
				os.system(pro[1:len(pro)-1])
			else:
				try:
					os.system(strings[pro])
				except:
					error.illgal_syn("No varriable found", line)
		elif syntax["key"] == "call":
			file = syntax["file"]
			if file[0:1] == '"' and file[len(file)-1:len(file)] == '"':
				file = file[1:len(file)-1]
			else:
				try:
					file = strings[file]
							
				except:
					error.illgal_syn("No varriable found", line)
			try:
				os.system("SSpoon "+file)
			except:
				error.illgal_syn("No file found")
		elif syntax["key"] == "sleep":
			dur = syntax["duration"]
			try:
				time.sleep(int(dur))
			except:
				try:
					time.sleep(integers[dur])
				except:
					error.illgal_syn("No varriable found", line)

class ast:
	in_statement = False
	in_forloop = False
	making_fn = False
	def ast(self, tree):
		global line
		for syntax in tree:
			if self.in_statement is False and self.in_forloop is False and self.making_fn is False:
				if syntax["key"] == "NEWLINE":
					try:
						self.value = str(syntax["value"])
						exec("print(str("+self.value+"))", strings, integers)
					except:
						error.no_var("No varriable found or int is in the line", line)
				elif syntax["key"] == "String_var":
					self.value = eval("str("+syntax["value"]+")", strings, integers)
					strings[syntax["name"]] = self.value
				elif syntax["key"] == "Integer_var":
					try:
						self.value = eval("int("+syntax["value"]+")", integers, strings)
						integers[syntax["name"]] = self.value
					except:
						error.illgal_syn("Possible string in var", line)
				elif syntax["key"] == "statement_if":
					self.in_statement = True

				elif syntax["key"] == "for_loop":
					self.in_forloop = True
				elif syntax["key"] == "input":
					self.st = syntax["todo"]
					self.middle = len(self.st)
					self.end = len(self.st)
					self.had_hol_n = False
					if ' -p ' in self.st:
						self.middle = self.st.index(" -p ")
						self.had_hol_n = True
					if self.had_hol_n is True:
						self.holder = eval(self.st[0:self.middle], strings)
						strings[self.st[self.middle+4:self.end]] = input(self.holder)

				elif syntax["key"] == "osprocess":
					self.pro = syntax["todo"]
					if self.pro[0:1] == '"' and self.pro[len(self.pro)-1:len(self.pro)] == '"':
						os.system(self.pro[1:len(self.pro)-1])
					else:
						try:
							os.system(strings[self.pro])
						except:
							error.illgal_syn("No varriable found", line)
				elif syntax["key"] == "call":
					self.file = syntax["file"]
					if self.file[0:1] == '"' and self.file[len(self.file)-1:len(self.file)] == '"':
						self.file = self.file[1:len(self.file)-1]
					else:
						try:
							self.file = strings[self.file]
							
						except:
							error.illgal_syn("No int varriable found", line)
					os.system("SSpoon.py "+self.file)
				elif syntax["key"] == "sleep":
					self.dur = syntax["duration"]
					try:
						time.sleep(int(self.dur))
					except:
						try:
							time.sleep(integers[self.dur])
						except:
							error.illgal_syn("No varriable found", line)
				elif syntax["key"] == "callfunc":
					exec(syntax["func"])
			if self.in_statement is True:
				self.statement = syntax["statement"]
				if self.statement[0:2] == "if":
					self.statement = self.statement.replace("if", "", 1)
				if self.statement[0:1] == " ":
					self.statement = self.statement.replace(" ", "", 1)
					if "==" in self.statement:
						self.ind = self.statement.index("==")
						self.name = self.statement[0:self.ind]
						self.len = len(self.statement)
						if self.statement[self.len-4:self.len] == "THEN":
							self.ensef = self.len-4

							self.val = self.statement[self.ind+2:self.ensef]
							if self.val[0:1] == " ":
								self.val = self.val.replace(" ", "", 1)
							if self.val[len(self.val)-1:len(self.val)] == " ":
								self.val = self.val[0:len(self.val)-1]
							if self.name[len(self.name)-1:len(self.name)] == " ":
								self.name = self.name[0:len(self.name)-1]
							##string check carbon lodi
							if self.name[0:1] == '"':
								self.name = self.name.replace('"', "")
							else:
								try:
									self.name = int(self.name)
								except:
									try:
										try:
											self.name = strings[self.name]
										except:
											self.name = integers[self.name]
									except:
										error.illgal_syn("No varriable found", line)
							if self.val[0:1] == '"':
								self.val = self.val.replace('"', "")
							else:
								try:
									self.val = int(self.val)
								except:
									try:
										try:
											self.val = strings[self.val]
										except:
											self.val = integers[self.val]
									except:
										error.illgal_syn("No varriable found", line)
							
							if self.name == self.val:
								
								o(syntax["todo"])
							
								
						else:
							error.illgal_syn("No 'THEN' found", line)
					if "!=" in self.statement:
						self.ind = self.statement.index("!=")
						self.name = self.statement[0:self.ind]
						self.len = len(self.statement)
						if self.statement[self.len-4:self.len] == "THEN":
							self.ensef = self.len-4

							self.val = self.statement[self.ind+2:self.ensef]
							if self.val[0:1] == " ":
								self.val = self.val.replace(" ", "", 1)
							if self.val[len(self.val)-1:len(self.val)] == " ":
								self.val = self.val[0:len(self.val)-1]
							if self.name[len(self.name)-1:len(self.name)] == " ":
								self.name = self.name[0:len(self.name)-1]
							##string check carbon lodi
							if self.name[0:1] == '"':
								self.name = self.name.replace('"', "")
							else:
								try:
									self.name = int(self.name)
								except:
									try:
										try:
											self.name = strings[self.name]
										except:
											self.name = integers[self.name]
									except:
										error.illgal_syn("No varriable found", line)
							if self.val[0:1] == '"':
								self.val = self.val.replace('"', "")
							else:
								try:
									self.val = int(self.val)
								except:
									try:
										try:
											self.val = strings[self.val]
										except:
											self.val = integers[self.val]
									except:
										error.illgal_syn("No varriable found", line)
							try:
								if self.name != self.val:
								
									o(syntax["todo"])
							except:
								error.illgal_syn("Cant compare string to int or int to string", line)
							
								
						else:
							error.illgal_syn("No 'THEN' found", line)
				else:
					error.illgal_syn("No syntax found", line)
				self.in_statement = False
			elif self.in_forloop is True:
				self.arg = syntax["argument"]
				self.todo = syntax["todo"]
				if self.arg[0:3] == "for":
					self.arg = self.arg.replace("for", "", 1)
					if self.arg[0:1] == " ":
						self.arg = self.arg.replace(" ", "", 1)
						if self.arg[len(self.arg)- 4:len(self.arg)] == "THEN":
							if "to" in self.arg:
								self.index_mid = self.arg.index("to")
								self.arg1 = self.arg[0:self.index_mid]
								self.arg2 = self.arg[self.index_mid:len(self.arg)-4]
								if "to " in self.arg2:
									self.arg2 = self.arg2.replace("to ", "")
									
								if "=" in self.arg1:
									self.label = self.arg1[0:self.arg1.index("=")]
									self.arg1 = self.arg1.replace(self.arg1[0:self.arg1.index("=")+1], "", 1)
									self.arg1 = self.arg1.replace(" ", "")
									try:
										self.arg1 = int(self.arg1)
									except:
										try:
											self.arg1 = integers[self.arg1]
										except:
											error.illgal_syn("No varriable found", line)
									self.arg2 = self.arg2.replace(" ", "")
									try:
										self.arg2 = int(self.arg2)
									except:
										try:
											self.arg2 = integers[self.arg2]
										except:
											error.illgal_syn("No varriable found", line)

									try:
										for i in range(self.arg1, self.arg2):
											o(syntax["todo"])
										
									except:
										
										error.illgal_syn("Cant count a string", line)
							else:
								error.illgal_syn("Expected 'to' for loop count", line)
						else:
							error.illgal_syn("No 'THEN' found", line)
				self.in_forloop = False
			line += 1