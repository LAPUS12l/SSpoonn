from sys import *
import os
integers = {
	
}
strings = {
	#Built in Vars
	"Hello_world" : "Hello",
	"Christ" : "Christian"
}
functions = { }

line = 1

class Error:
	def no_var(self, value, line):
		print(f"""Traceback error <{argv[1]}>:
	Dest : {os.getcwd()}
	Line : {line}
	Valu : {value}
""")
		exit()
	def illgal_syn(self, value, line):
		print(f"""Traceback error <{argv[1]}>:
	Dest : {os.getcwd()}
	Line : {line}
	Valu : {value}
""")
		exit()
		
		os.system("exit")
	def parametter(self, value, line):
		print(f"""Traceback error <{argv[1]}>:
	Dest : {os.getcwd()}
	Line : {line}
	Valu : {value}
""")
		exit()

error = Error()
def open_file(filename):
	data = open(filename, "r").readlines()
	return data

class lexer:
	file_con = open_file(argv[1])
	token = []
	def tokenizer(self):
		global line
		self.in_statement = False
		self.statement = ""
		self.collected = []
		self.loop_arg = ""
		self.in_forloop = False
		self.todo = []
		self.making_func = False
		self.func_arg = ""
		self.todo1 = []
		for this in self.file_con:
			this = this.replace("\n", "")
			this = this.replace("""
""", "")
			if self.in_statement is False and self.in_forloop is False and self.making_func is False:
				if this[0:7] == "println":
					this = this.replace("println", "", 1)
					if this[0:1] == "[":
						if this[len(this)-1:len(this)] == "]":
							this = this.replace("[", "", 1)
							self.index = this.index("]")
							self.string = this[0:self.index]
							self.token.append({"key":"NEWLINE", "value":self.string})
						else:
							error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
					else:
						error.illgal_syn("No clossing and starting blocks found '[', ']'", line)
				elif this[0:6] == "string":
					this = this.replace("string", "", 1)
					if this[0:1] == " ":
						this = this.replace(" ", "", 1)
						if "=" in this:
							self.index = this.index("=")
							self.name = this[0:self.index]
							if self.name[len(self.name)-1:len(self.name)]:
								self.name = self.name[0:len(self.name)-1]
							if " " in self.name:
								error.parametter("Tab and spaces in name", line)
							else:
								self.end = len(this)
								self.token.append({"key":"String_var", "value":this[self.index+1:self.end], "name":self.name})
						else:
							error.parametter("Missing '=' to get name and value", line)
					else:
						error.illgal_syn("Invalid syntax", line)
				elif this[0:3] == "int":
					this = this.replace("int", "", 1)
					if this[0:1] == " ":
						this = this.replace(" ", "", 1)
						if "=" in this:
							self.index = this.index("=")
							self.name = this[0:self.index]
							if self.name[len(self.name)-1:len(self.name)]:
								self.name = self.name[0:len(self.name)-1]
							if " " in self.name:
								error.parametter("Tab and spaces in name", line)
							else:
								self.end = len(this)
								self.token.append({"key":"Integer_var", "value":this[self.index+1:self.end], "name":self.name})
						else:
							error.parametter("Missing '=' to get name and value", line)
					else:
						error.illgal_syn("Invalid syntax", line)
				elif this[0:6] == "input ":
					this = this.replace("input ", "", 1)
					index = this.index(" ", 1)
					self.token.append({"key":"input", "todo":this})
				elif this[0:2] == "if":
					self.statement = this
					self.in_statement = True
					self.in_forloop = False
				elif this[0:3] == "for":
					self.loop_arg = this
					self.in_forloop = True
					self.in_statement = False
				elif this[0:7] == "process":
					this = this.replace("process", "", 1)
					if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
						this = this[1:len(this)-1]
						self.token.append({"key":"osprocess", "todo":this})
					else:
						error.illgal_syn("No blocks found '[' ']'", line)
				elif this[0:4] == "call":
					this = this.replace("call", "", 1)
					if this[0:1] == "[" and this[len(this)-1:len(this)] == "]":
						this = this[1:len(this)-1]
						self.token.append({"key":"call", "file":this})
					else:
						error.illgal_syn("No blocks found '[' ']'", line)
					
				elif this[0:5] == "sleep":
					this = this.replace("sleep", "")
					if this[0] == "[" and this[len(this)-1] == "]":
						this = this[1:len(this)-1]
						self.token.append({"key":"sleep", "duration":this})
					else:
						error.illgal_syn("No blocks found '[' ']'")
				elif this == "":
					None
			elif self.in_statement is True:
				if this[0:3] != "end":
					self.collected.append(this)
				elif this[0:3] == "end":
					self.in_statement = False
					self.token.append({"key":"statement_if", "statement":self.statement, "todo":self.collected})
					self.statement = ""
					self.collected = []
			elif self.in_forloop is True:
				if this[0:3] != "end":
					self.todo.append(this)
				elif this[0:3] == "end":
					self.in_forloop = False
					self.token.append({"key":"for_loop", "argument":self.loop_arg, "todo":self.todo})
					self.loop_arg = ""
					self.todo = []
			
					
			line += 1
		line = 1
		return self.token
lexer = lexer()

