Bookbot 📚
CLI tool em Python para análise de livros TXT: conta palavras totais e frequência de cada letra alfabética (case-insensitive), ignorando não-letras. Projeto do curso Back-end Developer Path (Python & Go) no boot.dev—primeiro exercício prático de file I/O, dicts e sorting.

[

Funcionalidades
Contagem de palavras: len(text.split()).

Frequência de caracteres: Dict com loop manual em text.lower(), só letras A-Z.

Ordenação: Lista de dicts sorted por count descending.

CLI args: python3 main.py <arquivo.txt> com validação e exit(1).
​

Demo
text
$ python3 main.py books/frankenstein.txt
Found 77986 total words
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
...
Testado com Frankenstein (~77k palavras), Moby Dick e Pride & Prejudice.

Instalação
Clone: git clone https://github.com/lucaslopes-ti/bookbot-python.git

Baixe livros:

text
mkdir books
curl -o books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt  # Ou do boot.dev
curl -o books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt
curl -o books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt
Rode: python3 main.py books/frankenstein.txt

Estrutura
text
bootdotdev/
├── main.py      # CLI, file read, calls stats
├── stats.py     # get_num_words(), get_num_characters(), sort_characters()
└── books/       # frankenstein.txt, etc.
Como Fiz
stats.py: Dict counting em loop (if char in char_counts).

main.py: sys.argv[1] para filepath, open() relative, print sorted alpha chars.

Sem libs extras—puro Python.
​

Lições Aprendidas
Manipulação de arquivos e strings.

Dicts/loops para counting.

sys.argv e error handling CLI.

Sorting com list.sort(key=...).

Boot.dev Tests Passados
text
bootdev run 7b6379ff-8a74-45fe-8084-a79f9680a371 -s
100% match nos outputs esperados (e:44538 Frankenstein, etc.).
