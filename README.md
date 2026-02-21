# 📚 Bookbot

CLI tool em **Python** para análise de livros em formato **.txt**.  
O programa conta o total de palavras e a frequência de cada letra do alfabeto (case-insensitive), ignorando caracteres que não sejam letras.

Projeto desenvolvido no **Back-end Developer Path (Python & Go)** do **boot.dev**, como primeiro exercício prático envolvendo **file I/O**, **dicionários** e **ordenação**.

---

## 🚀 Funcionalidades

- **Contagem de palavras**  
  Utiliza `len(text.split())`.

- **Frequência de caracteres**  
  - Uso de `dict`  
  - Loop manual em `text.lower()`  
  - Considera apenas letras de `a` a `z`

- **Ordenação**  
  - Lista de dicionários  
  - Ordenada por frequência (`count`) em ordem decrescente

- **Interface de Linha de Comando (CLI)**  
  ```bash
  python3 main.py <arquivo.txt>

Validação de argumentos

Encerra com exit(1) em caso de erro

▶️ Demonstração
$ python3 main.py books/frankenstein.txt
Found 77986 total words
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...

Testado com:

Frankenstein (~77 mil palavras)

Moby Dick

Pride & Prejudice

🛠️ Instalação

Clone o repositório:

git clone https://github.com/lucaslopes-ti/bookbot-python.git
cd bookbot-python

Baixe alguns livros para teste:

mkdir books
curl -o books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt
curl -o books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt
curl -o books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt

Execute o programa:

python3 main.py books/frankenstein.txt
📁 Estrutura do Projeto
bootdotdev/
├── main.py      # CLI, leitura do arquivo e chamadas das funções
├── stats.py     # get_num_words(), get_num_characters(), sort_characters()
└── books/       # frankenstein.txt, mobydick.txt, etc.
🧠 Como Foi Desenvolvido
stats.py

Contagem usando dicionário

Loop manual caractere por caractere

Exemplo de lógica:

if char in char_counts:
    char_counts[char] += 1
main.py

Uso de sys.argv[1] para capturar o caminho do arquivo

Leitura com open() (caminho relativo)

Impressão apenas de caracteres alfabéticos ordenados

📌 Sem bibliotecas externas — Python puro.

📘 Lições Aprendidas

Manipulação de arquivos (open, read)

Processamento de strings

Uso de dicionários para contagem

Argumentos de linha de comando com sys.argv

Tratamento básico de erros

Ordenação com list.sort(key=...)

✅ Testes do boot.dev
bootdev run 7b6379ff-8a74-45fe-8084-a79f9680a371 -s

✔️ 100% de correspondência com os outputs esperados
(ex.: e: 44538 para Frankenstein)

📌 Observações

Este projeto marca o primeiro exercício prático do curso envolvendo:

File I/O

Estruturas de dados

Lógica de programação aplicada

Organização de código em múltiplos arquivos
