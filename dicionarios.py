
# ATENÇÃO!!!!! ESSE ARQUIVO FOI KIBADO DO MONTADOR DE XAVIER NA CARA DE PAU.




# padrão i exemplo: addi $s $t imediato (16 bits)
# padrão r exemplo: add $d $s $t
# padrão s exemplo: sll $d $t a (5 bits)
# padrão d exemplo: div $s $t 
# padrões podem ser adicionados ou modificados (modificar também montar.py)]

def padroes(nome): # nome é string do nome da instrução
  instrucoes = { # dicionário de dicionários. Ideia xerocada do @maure-tads
    "add": {
      "instrucao": "000000"+"std"+"00000"+"100000", # instrução $d $s $t
      "padrao": "r"
    },
    "addi": {
      "instrucao": "001000"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "addiu": {
      "instrucao": "001001"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "addu": {
      "instrucao": "000000"+"std"+"00000"+"100001", # instrução $d $s $t
      "padrao": "r"
    },
    "and": {
      "instrucao": "000000"+"std"+"00000"+"100100", # instrução $d $s $t
      "padrao": "r"
    },
    "andi": {
      "instrucao": "001100"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "div": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011010", # instrução $s $t 
      "padrao": "d"
    },
    "divu": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011011", # instrução $s $t 
      "padrao": "d"
    },
    "mul": {
      "instrucao": "011100"+"std"+"00000"+"000010", # instrução $d $s $t
      "padrao": "r"
    },
    "mult": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011000", # instrução $s $t 
      "padrao": "d"
    },
    "multu": {
      "instrucao": "000000"+"st"+"00000"+"00000"+"011001", # instrução $s $t 
      "padrao": "d"
    },
    "nop": {
      "instrucao": "000000"+"00000"+"00000"+"00000"+"00000"+"000000", # caso à parte
      "padrao": "r"
    },
    "nor": {
      "instrucao": "000000"+"std"+"00000"+"100111", # instrução $d $s $t
      "padrao": "r"
    },
    "or": {
      "instrucao": "000000"+"std"+"00000"+"100101", # instrução $d $s $t
      "padrao": "r"
    },
    "ori": {
      "instrucao": "001101"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sll": {
      "instrucao": "000000"+"00000"+"tda"+"000000", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "slt": {
      "instrucao": "000000"+"std"+"00000"+"101010", # instrução $d $s $t
      "padrao": "r"
    },
    "slti": {
      "instrucao": "001010"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sltiu": {
      "instrucao": "001011"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
    "sltu": {
      "instrucao": "000000"+"std"+"00000"+"101011", # instrução $d $s $t
      "padrao": "r"
    },
    "sra": {
      "instrucao": "000000"+"00000"+"tda"+"000011", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "srl": {
      "instrucao": "000000"+"00000"+"tda"+"000010", # instrução $d $t a (5 bits)
      "padrao": "s"
    },
    "sub": {
      "instrucao": "000000"+"std"+"00000"+"100010", # instrução $d $s $t
      "padrao": "r"
    },
    "subu": {
      "instrucao": "000000"+"std"+"00000"+"100011", # instrução $d $s $t
      "padrao": "r"
    },
    "syscall": {
      "instrucao": "000000"+"00000"+"00000"+"00000"+"00000"+"001100", #caso a parte
      "padrao": "r"
    },
    "xor": {
      "instrucao": "000000"+"std"+"00000"+"100110", # instrução $d $s $t
      "padrao": "r"
    },
    "xori": {
      "instrucao": "001110"+"sti", # instrução $s $t imediato (16 bits)
      "padrao": "i"
    },
  }