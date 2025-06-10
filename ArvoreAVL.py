# ArvoreAVL.py
from typing import Optional
from No import No

class ArvoreAVL:
    def altura(self, no: Optional[No]) -> int:
        return no.altura if no else 0

    def fator_balanceamento(self, no: Optional[No]) -> int:
        return self.altura(no.esquerdo) - self.altura(no.direito) if no else 0

    def atualizar_altura(self, no: Optional[No]):
        if no:
            no.altura = max(self.altura(no.esquerdo), self.altura(no.direito)) + 1

    def rotacao_direita(self, y: Optional[No]) -> Optional[No]:
        if not y or not y.esquerdo:
            return y
        x = y.esquerdo
        T2 = x.direito
        x.direito = y
        y.esquerdo = T2
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda(self, y: Optional[No]) -> Optional[No]:
        if not y or not y.direito:
            return y
        x = y.direito
        T2 = x.esquerdo
        x.esquerdo = y
        y.direito = T2
        self.atualizar_altura(y)
        self.atualizar_altura(x)
        return x

    def rotacao_esquerda_direita(self, no: Optional[No]) -> Optional[No]:
        if no and no.esquerdo:
            no.esquerdo = self.rotacao_esquerda(no.esquerdo)
        return self.rotacao_direita(no) if no else None

    def rotacao_direita_esquerda(self, no: Optional[No]) -> Optional[No]:
        if no and no.direito:
            no.direito = self.rotacao_direita(no.direito)
        return self.rotacao_esquerda(no) if no else None

    def inserir(self, raiz: Optional[No], chave: int) -> Optional[No]:
        if not raiz:
            return No(chave)
        if chave < raiz.chave:
            raiz.esquerdo = self.inserir(raiz.esquerdo, chave)
        elif chave > raiz.chave:
            raiz.direito = self.inserir(raiz.direito, chave)
        else:
            return raiz  # Chave duplicada

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

    def menor_valor(self, no: Optional[No]) -> Optional[No]:
        atual = no
        while atual and atual.esquerdo:
            atual = atual.esquerdo
        return atual

    def remover(self, raiz: Optional[No], chave: int) -> Optional[No]:
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
            raiz.chave = sucessor.chave if sucessor else raiz.chave
            raiz.direito = self.remover(raiz.direito, sucessor.chave if sucessor else None)

        self.atualizar_altura(raiz)
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

    def buscar(self, raiz: Optional[No], chave: int) -> Optional[No]:
        if not raiz or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self.buscar(raiz.esquerdo, chave)
        return self.buscar(raiz.direito, chave)

    def _pre_ordem_vlr(self, no: Optional[No]) -> str:
        if not no:
            return ""
        return f"{no.chave} {self._pre_ordem_vlr(no.esquerdo)}{self._pre_ordem_vlr(no.direito)}"

    def pre_ordem_vlr(self, no: Optional[No]) -> str:
        return ' '.join(self._pre_ordem_vlr(no).split()).strip()

    def _in_ordem_lvr(self, no: Optional[No]) -> str:
        if not no:
            return ""
        return f"{self._in_ordem_lvr(no.esquerdo)}{no.chave} {self._in_ordem_lvr(no.direito)}"

    def in_ordem_lvr(self, no: Optional[No]) -> str:
        return ' '.join(self._in_ordem_lvr(no).split()).strip()

    def _pos_ordem_lrv(self, no: Optional[No]) -> str:
        if not no:
            return ""
        return f"{self._pos_ordem_lrv(no.esquerdo)}{self._pos_ordem_lrv(no.direito)}{no.chave} "

    def pos_ordem_lrv(self, no: Optional[No]) -> str:
        return ' '.join(self._pos_ordem_lrv(no).split()).strip()
    def imprimir_arvore(self, raiz):
        lines = self._criar_linhas(raiz)
    for line in lines:
        print(line)

def _criar_linhas(self, no):
    if no is None:
        return []

    if not no.esquerdo and not no.direito:
        return [str(no.chave)]

    linha_atual = str(no.chave)
    esq_lines = self._criar_linhas(no.esquerdo) if no.esquerdo else []
    dir_lines = self._criar_linhas(no.direito) if no.direito else []

    altura = max(len(esq_lines), len(dir_lines))

    # Preencher com linhas vazias para alinhamento
    esq_lines += [''] * (altura - len(esq_lines))
    dir_lines += [''] * (altura - len(dir_lines))

    # Linha do nó atual centralizada
    linha_atual = " " * ((len(esq_lines[0]) - len(linha_atual)) // 2) + linha_atual
    linha_atual += " " * ((len(dir_lines[0]) - len(linha_atual) + len(esq_lines[0])) // 2)

    # Juntar as partes
    linhas = [linha_atual]
    for e, d in zip(esq_lines, dir_lines):
        linhas.append(e + " " + d)

    return linhas