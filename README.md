# 🐴 Passeio do Cavalo (Knight's Tour)

Este projeto implementa a solução para o clássico problema do **Passeio do Cavalo** utilizando **Backtracking**, conforme as regras do movimento do cavalo no xadrez.

## 🧠 Sobre o problema

Dado um tabuleiro `n x n`, o objetivo é encontrar uma sequência de movimentos de um cavalo que visite cada célula **uma única vez**.  
O cavalo se move em "L", ou seja, duas casas em uma direção e uma casa em direção perpendicular.

## ⚙️ Como funciona

O algoritmo usa **Backtracking** para tentar todos os movimentos possíveis a partir de uma posição inicial (por padrão, `(0,0)`).  
Se algum caminho não leva a uma solução, o algoritmo retrocede (**backtrack**) e tenta outro.

## 📂 Arquivo principal

- `passeio_do_cavalo.py` → contém a implementação completa em Python.

## ▶️ Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório ou copie o arquivo `passeio_do_cavalo.py`.
3. No terminal, execute:

```bash
python passeio_do_cavalo.py
