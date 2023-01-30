# Name: Jillian Plahn 

from colors import *
from elements import StrConstant, DictConstant, CodeArray

class Stacks:
    def __init__(self):
        #stack variables
        self.opstack = []  #assuming top of the stack is the end of the list
        self.dictstack = []  #assuming top of the stack is the end of the list
        # The environment that the REPL evaluates expressions in.
        # Uncomment this dictionary in part2
        self.builtin_operators = {
            "add":self.add,
            "sub":self.sub,
            "mul":self.mul,
            "mod":self.mod,
            "eq":self.eq,
            "lt": self.lt,
            "gt": self.gt,
            "dup": self.dup,
            "exch":self.exch,
            "pop":self.pop,
            "copy":self.copy,
            "count": self.count,
            "clear":self.clear,
            "stack":self.stack,
            "dict":self.psDict,
            "string":self.string,
            "length":self.length,
            "get":self.get,
            "put":self.put,
            "getinterval":self.getinterval,
            "putinterval":self.putinterval,
            "search" : self.search,
            "begin":self.begin,
            "end":self.end,
            "def":self.psDef,
            "if":self.psIf,
            "ifelse":self.psIfelse,
            "for":self.psFor
        }
    #------- Operand Stack Helper Functions --------------
    
    """
        Helper function. Pops the top value from opstack and returns it.
    """
    def opPop(self):
        if len(self.opstack) > 0:
            x = self.opstack[len(self.opstack) - 1]
            self.opstack.pop(len(self.opstack) - 1)
            return x
        else:
            print("Error: opPop - Operand stack is empty")

    """
       Helper function. Pushes the given value to the opstack.
    """
    def opPush(self,value):
        self.opstack.append(value)

    #------- Dict Stack Helper Functions --------------
    """
       Helper function. Pops the top dictionary from dictstack and returns it.
    """  
    def dictPop(self):
        if len(self.dictstack) > 0:
            return self.dictstack.pop()
        else:
            print("Error: dictPop - Dictionary stack is empty")

    """
       Helper function. Pushes the given dictionary onto the dictstack. 
    """   
    def dictPush(self,d):
        return self.dictstack.append(d)

    """
       Helper function. Adds name:value pair to the top dictionary in the dictstack.
       (Note: If the dictstack is empty, first adds an empty dictionary to the dictstack then adds the name:value to that. 
    """  
    def define(self, name, value):
       if (len(self.dictstack)) == 0: 
            self.dictPush({})
       self.dictstack[len(self.dictstack)-1][name] = value

    """
       Helper function. Searches the dictstack for a variable or function and returns its value. 
       (Starts searching at the top of the dictstack; if name is not found returns None and prints an error message.
        Make sure to add '/' to the begining of the name.)
    """
    def lookup(self,name):
        Name = '/' + name
        for element in reversed(self.dictstack):
            if Name in element:
                return element[Name]
        return None
   
    #------- Arithmetic Operators --------------

    """
       Pops 2 values from opstack; checks if they are numerical (int); adds them; then pushes the result back to opstack. 
    """  
    def add(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 + op2)
            else:
                print("Error: add - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: add expects 2 operands")

    """
       Pops 2 values from opstack; checks if they are numerical (int); subtracts them; and pushes the result back to opstack. 
    """ 
    def sub(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1, int) or isinstance(op1, float)) and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op2 - op1)
            else: 
                print("Error: sub - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)  
        else:
            print("Error: sub expects 2 operands")    

    """
        Pops 2 values from opstack; checks if they are numerical (int); multiplies them; and pushes the result back to opstack. 
    """
    def mul(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int) or isinstance(op1,float))  and (isinstance(op2,int) or isinstance(op2,float)):
                self.opPush(op1 * op2)
            else:
                print("Error: mul - one of the operands is not a number value")
                self.opPush(op1)
                self.opPush(op2)             
        else:
            print("Error: mul expects 2 operands")

    """
        Pops 2 values from stack; checks if they are int values; calculates the remainder of dividing the bottom value by the top one; 
        pushes the result back to opstack.
    """
    def mod(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1,int))  and (isinstance(op2,int)):
                self.opPush(op2 % op1)
            else:
                print("Error mod- one of the operands is not an int value")
                self.opPush(op1)
                self.opPush(op2)        
        else:
            print("Error: mod expected 2 operands")

    """ Pops 2 values from stacks; if they are equal pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StrConstant values, compares the `value` attributes of the StrConstant objects;
          - if they are DictConstant objects, compares the objects themselves (i.e., ids of the objects).
        """
    def eq(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1, int) or isinstance(op1, bool) and isinstance(op2, int) or isinstance(op2, bool)):
                if (op1 == op2):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, StrConstant) and isinstance(op2, StrConstant)):
                if(op1.value == op2.value):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, DictConstant) and isinstance(op2, DictConstant)):
                if (op1 == op2):
                    self.opPush(True)
                else:
                    self.opPush(False)
        else:
            print("Error: eq expected 2 operands")


    """ Pops 2 values from stacks; if the bottom value is less than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StrConstant values, compares the `value` attributes of them;
          - if they are DictConstant objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def lt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1, int) or isinstance(op1, bool) and isinstance(op2, int) or isinstance(op2, bool)):
                if(op1 > op2):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, StrConstant) and isinstance(op2, StrConstant)):
                if(op1.value > op2.value):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, DictConstant) and isinstance(op2, DictConstant)):
                if(op1 > op2):
                    self.opPush(True)
                else:
                    self.opPush(False)
        else:
            print("Error: lt expected 2 operands")

    """ Pops 2 values from stacks; if the bottom value is greater than the second, pushes True back onto stack, otherwise it pushes False.
          - if they are integers or booleans, compares their values. 
          - if they are StrConstant values, compares the `value` attributes of them;
          - if they are DictConstant objects, compares the objects themselves (i.e., ids of the objects).
    """  
    def gt(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            if (isinstance(op1, int) or isinstance(op1, bool) and isinstance(op2, int) or isinstance(op2, bool)):
                if(op2 > op1):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, StrConstant) and isinstance(op2, StrConstant)):
                if(op2.value > op1.value):
                    self.opPush(True)
                else:
                    self.opPush(False)
            elif (isinstance(op1, DictConstant) and isinstance(op2, DictConstant)):
                if(op2 > op1):
                    self.opPush(True)
                else:
                    self.opPush(False)
        else:
            print("Error: gt expected 2 operands")

    #------- Stack Manipulation and Print Operators --------------
    """
       This function implements the Postscript "pop operator". Calls self.opPop() to pop the top value from the opstack and discards the value. 
    """
    def pop (self):
        if (len(self.opstack) > 0):
            self.opPop()
        else:
            print("Error: pop - not enough arguments")

    """
       Prints the opstack and dictstack. The end of the list is the top of the stack. 
    """
    def stack(self):
        print(OKGREEN+"**opstack**")
        for item in reversed(self.opstack):
            print(item)
        print("-----------------------"+CEND)
        print(RED+"**dictstack**")
        for item in reversed(self.dictstack):
            print(item)
        print("-----------------------"+ CEND)

    """
       Copies the top element in opstack.
    """
    def dup(self):
        value = self.opPop()
        self.opPush(value)
        self.opPush(value)

    """
       Pops an integer count from opstack, copies count number of values in the opstack. 
    """
    def copy(self):
        if(len(self.opstack) > 0):
            count = self.opPop()
            listCopy = []
            for x in range(0, count):
               listCopy.append(self.opPop())
            for item in reversed(listCopy):
                self.opPush(item)
            for item in reversed(listCopy):
                self.opPush(item)
        else:
            print("Error: copy enough arguments")

    """
        Counts the number of elements in the opstack and pushes the count onto the top of the opstack.
    """
    def count(self):
        self.opPush(len(self.opstack))

    """
       Clears the opstack.
    """
    def clear(self):
        self.opstack.clear()
        
    """
       swaps the top two elements in opstack
    """
    def exch(self):
        if len(self.opstack) > 1:
            op1 = self.opPop()
            op2 = self.opPop()
            self.opPush(op1)
            self.opPush(op2)
        else:
            print("Error: exch not enough arguments")

    # ------- String and Dictionary creator operators --------------

    """ Creates a new empty string  pushes it on the opstack.
    Initializes the characters in the new string to \0 , i.e., ascii NUL """
    def string(self):
        self.opPop()
        str = StrConstant("(\x00\x00\x00)")
        self.opPush(str)
    
    """Creates a new empty dictionary  pushes it on the opstack """
    def psDict(self):
        self.opPop()
        self.opPush(DictConstant({}))

    # ------- String and Dictionary Operators --------------
    """ Pops a string or dictionary value from the operand stack and calculates the length of it. Pushes the length back onto the stack.
       The `length` method should support both DictConstant and StrConstant values.
    """
    def length(self):
        if (len(self.opstack) > 0):
            popped = self.opPop()
            if (isinstance(popped, StrConstant)):
                self.opPush(len(popped.value)-2)
            elif (isinstance(popped, DictConstant)):
                self.opPush(len(popped.value.keys()))
            else:
                self.opPush(popped)
        else:
            print("Error length")


    """ Pops either:
         -  "A (zero-based) index and an StrConstant value" from opstack OR 
         -  "A `name` (i.e., a key) and DictConstant value" from opstack.  
        If the argument is a StrConstant, pushes the ascii value of the the character in the string at the index onto the opstack;
        If the argument is an DictConstant, gets the value for the given `name` from DictConstant's dictionary value and pushes it onto the opstack
    """
    def get(self):
        indexOrKey = self.opPop()
        stringOrDict = self.opPop()
        if(isinstance(stringOrDict, StrConstant)):
            element = stringOrDict.value[indexOrKey + 1]
            self.opPush(ord(element))
        elif(isinstance(stringOrDict, DictConstant)):
            self.opPush(stringOrDict.value[indexOrKey])
        else:
            self.opPush(stringOrDict)
            self.opPush(indexOrKey)
   
    """
    Pops either:
    - "An `item`, a (zero-based) `index`, and an StrConstant value from  opstack", OR
    - "An `item`, a `name`, and a DictConstant value from  opstack". 
    If the argument is a StrConstant, replaces the character at `index` of the StrConstant's string with the character having the ASCII value of `item`.
    If the argument is an DictConstant, adds (or updates) "name:item" in DictConstant's dictionary `value`.
    """
    def put(self):
        item = self.opPop()
        indexOrKey = self.opPop()
        strOrDict = self.opPop()
        if (isinstance(strOrDict, StrConstant)):
            strcopy = list((strOrDict.value))
            strcopy[indexOrKey + 1] = chr(item)
            strcopy = "".join(strcopy)
            strOrDict.value = strcopy
        elif(isinstance(strOrDict, DictConstant)):
            strOrDict.value[indexOrKey] = item
        else:
            self.opPush(strOrDict)
            self.opPush(indexOrKey)
            self.opPush(item)
    
    """
    getinterval is a string only operator, i.e., works only with StrConstant values. 
    Pops a `count`, a (zero-based) `index`, and an StrConstant value from  opstack, and 
    extracts a substring of length count from the `value` of StrConstant starting from `index`,
    pushes the substring back to opstack as a StrConstant value. 
    """ 
    def getinterval(self):
        count = self.opPop()
        index = self.opPop()
        string = self.opPop()
        if(isinstance (string, StrConstant)):
            #convert to list 
            stringcopy = list(string.value)
            #set up slice
            slice1 = slice((index + 1), (count+(index+1)), None)
            # substring should equal the sliced substring
            substring = stringcopy[slice1]
            # make the substring no longer a list 
            stringcopy = "".join(substring)
            string.value = "(" + stringcopy + ")"
            self.opPush(string)
        else:
            print("Value must be a string")

    """
    putinterval is a string only operator, i.e., works only with StrConstant values. 
    Pops a StrConstant value, a (zero-based) `index`, a `substring` from  opstack, and 
    replaces the slice in StrConstant's `value` from `index` to `index`+len(substring)  with the given `substring`s value. 
    """
    def putinterval(self):
        substring = self.opPop()
        index = self.opPop()
        string = self.opPop()
        i = 0
        #convert to list 
        stringlist = list(string.value)
        substringlist = list(substring.value)
        #remove paranthesis from substring
        substringlist.remove('(')
        substringlist.remove(')')
        lengthsub = len(substringlist)
        initialindex = index
        while (index+1) <= initialindex + lengthsub:
            stringlist[index+1] = substringlist[i]
            i += 1
            index += 1
        string.value = "".join(stringlist)

    """
    search is a string only operator, i.e., works only with StrConstant values. 
    Pops two StrConstant values: delimiter and inputstr
    if delimiter is a sub-string of inputstr then, 
       - splits inputstr at the first occurence of delimeter and pushes the splitted strings to opstack as StrConstant values;
       - pushes True 
    else,
        - pushes  the original inputstr back to opstack
        - pushes False
    """
    def search(self):
        delim = self.opPop()
        inputstr = self.opPop()
        inputstrlist = list(inputstr.value)
        inputstrlist.remove('(')
        inputstrlist.remove(')')
        delimcopy = list(delim.value)
        delimcopy.remove("(")
        delimcopy.remove(")")
        newstring = "".join(inputstrlist)
        newdelim = "".join(delimcopy)

        if (newdelim in newstring):
            split = newstring.split(newdelim, 1)
            secondSplit = split.insert(1, newdelim)
            for item in reversed(split):
                item = "(" + item + ")"
                item = StrConstant(item)
                self.opPush(item)
            self.opPush(True)
        else:
            string = "(" + newstring + ")"
            string = StrConstant(string)
            self.opPush(string)
            self.opPush(False)

    # ------- Operators that manipulate the dictstact --------------
    """ begin operator
        Pops a DictConstant value from opstack and pushes it's `value` to the dictstack."""
    def begin(self):
        if(len(self.opstack) > 0):
            popped = self.opPop()
            self.dictPush(popped.value)
        else:
            print("length error")

    """ end operator
        Pops the top dictionary from dictstack."""
    def end(self):
        if(len(self.dictstack) > 0):
            self.dictPop()
        else:
            print("end error")
        
    """ Pops a name and a value from stack, adds the definition to the dictionary at the top of the dictstack. """
    def psDef(self):
        value = self.opPop()
        name = self.opPop()
        self.define(name, value)

    # ------- if/ifelse Operators --------------
    """ if operator
        Pops a Block and a boolean value, if the value is True, executes the code array by calling apply.
       Will be completed in part-2. 
    """
    def psIf(self):
        pass

    """ ifelse operator
        Pops two Blocks and a boolean value, if the value is True, executes the bottom Block otherwise executes the top Block.
        Will be completed in part-2. 
    """
    def psIfelse(self):
        pass


    #------- Loop Operators --------------
    """
       Implements for operator.   
       Pops a Block, the end index (end), the increment (inc), and the begin index (begin) and 
       executes the code array for all loop index values ranging from `begin` to `end`. 
       Pushes the current loop index value to opstack before each execution of the Block. 
       Will be completed in part-2. 
    """ 
    def psFor(self):
        pass

    """ Cleans both stacks. """      
    def clearBoth(self):
        self.opstack[:] = []
        self.dictstack[:] = []

    """ Will be needed for part2"""
    def cleanTop(self):
        if len(self.opstack)>1:
            if self.opstack[-1] is None:
                self.opstack.pop()

