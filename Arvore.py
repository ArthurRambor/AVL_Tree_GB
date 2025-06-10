class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerdo = None
        self.direito = None
        self.altura = 1  # Começa com altura 1 para nós inseridos

class ArvoreAVL:
    def altura(self, no):
        return no.altura if no else 0

    def fator_balanceamento(self, no):
        return self.altura(no.esquerdo) - self.altura(no.direito) if no else 0

    def atualizar_altura(self, no):
        if no:
            no.altura = max(self.altura(no.esquerdo), self.altura(no.direito)) + 1

    def atualizar_altura_recursiva(self, no):
        if no:
            self.atualizar_altura_recursiva(no.esquerdo)
            self.atualizar_altura_recursiva(no.direito)
            self.atualizar_altura(no)

    def rotacao_direita(self, y):
        if not y or not y.esquerdo:
            return y
        x = y.esquerdo
        T2 = x.direito
        x.direito = y
        y.esquerdo = T2
        self.atualizar_altura_recursiva(y)
        return x

    def rotacao_esquerda(self, y):
        if not y or not y.direito:
            return y
        x = y.direito
        T2 = x.esquerdo
        x.esquerdo = y
        y.direito = T2
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda_direita(self, no):
        no.esquerdo = self.rotacao_esquerda(no.esquerdo)
        return self.rotacao_direita(no)

    def rotacao_direita_esquerda(self, no):
        no.direito = self.rotacao_direita(no.direito)
        return self.rotacao_esquerda(no)

    def inserir(self, raiz, chave):
        if not raiz:
            return No(chave)
        if chave < raiz.chave:
            raiz.esquerdo = self.inserir(raiz.esquerdo, chave)
        elif chave > raiz.chave:
            raiz.direito = self.inserir(raiz.direito, chave)
        else:
            return raiz  # chave duplicada

        self.atualizar_altura(raiz)
        fb_raiz = self.fator_balanceamento(raiz)
        fb_esquerdo = self.fator_balanceamento(raiz.esquerdo) if raiz.esquerdo else 0
        fb_direito = self.fator_balanceamento(raiz.direito) if raiz.direito else 0

        if fb_raiz > 1 and fb_esquerdo >= 0:
            return self.rotacao_direita(raiz)
        if fb_raiz > 1 and fb_esquerdo < 0:
            return self.rotacao_esquerda_direita(raiz)
        if fb_raiz < -1 and fb_direito <= 0:
            return self.rotacao_esquerda(raiz)
        if fb_raiz < -1 and fb_direito > 0:
            return self.rotacao_direita_esquerda(raiz)

        return raiz

    def menor_valor(self, no):
        atual = no
        while atual and atual.esquerdo:
            atual = atual.esquerdo
        return atual

    def remover(self, raiz, chave):
        if not raiz:
            return None

        if chave < raiz.chave:
            raiz.esquerdo = self.remover(raiz.esquerdo, chave)
        elif chave > raiz.chave:
            raiz.direito = self.remover(raiz.direito, chave)
        else:
            if not raiz.esquerdo or not raiz.direito:
                return raiz.esquerdo if raiz.esquerdo else raiz.direito
            sucessor = self.menor_valor(raiz.direito)
            raiz.chave = sucessor.chave
            raiz.direito = self.remover(raiz.direito, sucessor.chave)

        self.atualizar_altura_recursiva(raiz)
        fb_raiz = self.fator_balanceamento(raiz)
        fb_esquerdo = self.fator_balanceamento(raiz.esquerdo) if raiz.esquerdo else 0
        fb_direito = self.fator_balanceamento(raiz.direito) if raiz.direito else 0

        if fb_raiz > 1 and fb_esquerdo >= 0:
            return self.rotacao_direita(raiz)
        if fb_raiz > 1 and fb_esquerdo < 0:
            raiz.esquerdo = self.rotacao_esquerda(raiz.esquerdo)
            return self.rotacao_direita(raiz)
        if fb_raiz < -1 and fb_direito <= 0:
            return self.rotacao_esquerda(raiz)
        if fb_raiz < -1 and fb_direito > 0:
            raiz.direito = self.rotacao_direita(raiz.direito)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self.buscar(raiz.esquerdo, chave)
        return self.buscar(raiz.direito, chave)

    def pre_ordem_vlr(self, no):
        if not no:
            return ""
        return f"{no.chave} {self.pre_ordem_vlr(no.esquerdo)}{self.pre_ordem_vlr(no.direito)}"

    def pre_ordem_vrl(self, no):
        if not no:
            return ""
        return f"{no.chave} {self.pre_ordem_vrl(no.direito)}{self.pre_ordem_vrl(no.esquerdo)}"

    def in_ordem_lvr(self, no):
        if not no:
            return ""
        return f"{self.in_ordem_lvr(no.esquerdo)}{no.chave} {self.in_ordem_lvr(no.direito)}"

    def in_ordem_rvl(self, no):
        if not no:
            return ""
        return f"{self.in_ordem_rvl(no.direito)}{no.chave} {self.in_ordem_rvl(no.esquerdo)}"

    def pos_ordem_lrv(self, no):
        if not no:
            return ""
        return f"{self.pos_ordem_lrv(no.esquerdo)}{self.pos_ordem_lrv(no.direito)}{no.chave} "

    def pos_ordem_rlv(self, no):
        if not no:
            return ""
        return f"{self.pos_ordem_rlv(no.direito)}{self.pos_ordem_rlv(no.esquerdo)}{no.chave} "

    def limpar_espacos(self, resultado):
        return ' '.join(resultado.strip().split())
