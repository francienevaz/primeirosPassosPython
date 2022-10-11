def sacar (self, valor: float) -> None:
                                          # início do bloco do método
     if self.saldo >= valor:
                              # início do bloco do if
         self.saldo -= valor
     # fim do bloco do if
 # fim do bloco do método



# ISSO NÂO FUNCIONA EM PYTHON:
# def sacar (self, valor: float) -> None: # início do bloco do método
#  if self.saldo >= valor:
                         # início do bloco do if
#  self. saldo - = valor
# fim do bloco do if
# fim do bloco do método

# void sacar(double valor) {
#  if (this.saldo >= valor) {
# this.saldo -= valor;}}

def sacar (self, valor: float) -> None:
     if self.saldo >= valor:
         self. saldo -= valor

