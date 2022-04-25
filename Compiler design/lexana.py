import re
from tabulate import tabulate
import streamlit as st
import pandas as pd

def load_buffer(option):
    if option == 'ex1':
        arq = open('program.c', 'r')
    elif option == 'ex2':
        arq = open('programc2.c', 'r')
    elif option == 'ex3':
        arq = open('programc3.c', 'r')
    text = arq.readline()

    buffer = []
    cont = 1

    # The buffer size can be changed by changing cont
    while text != "":
        buffer.append(text)
        text = arq.readline()
        cont += 1

        if cont == 10 or text == '':
            # Return a full buffer
            buf = ''.join(buffer)
            cont = 1
            yield buf

            # Reset the buffer
            buffer = []

    arq.close()


def tokenize(code):
    lin_num = 1
    rules = [
        ('MAIN', r'main'),          # main
        ('INT', r'int'),            # int
        ('FLOAT', r'float'),        # float
        ('IF', r'if'),              # if
        ('ELSE', r'else'),          # else
        ('WHILE', r'while'),        # while
        ('READ', r'read'),          # read
        ('PRINT', r'print'),        # print
        ('LBRACKET', r'\('),        # (
        ('RBRACKET', r'\)'),        # )
        ('LBRACE', r'\{'),          # {
        ('RBRACE', r'\}'),          # }
        ('COMMA', r','),            # ,
        ('PCOMMA', r';'),           # ;
        ('EQ', r'=='),              # ==
        ('NE', r'!='),              # !=
        ('LE', r'<='),              # <=
        ('GE', r'>='),              # >=
        ('OR', r'\|\|'),            # ||
        ('AND', r'&&'),             # &&
        ('ATTR', r'\='),            # =
        ('LT', r'<'),               # <
        ('GT', r'>'),               # >
        ('PLUS', r'\+'),            # +
        ('MINUS', r'-'),            # -
        ('MULT', r'\*'),            # *
        ('DIV', r'\/'),             # /
        ('ID', r'[a-zA-Z]\w*'),     # IDENTIFIERS
        ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
        ('INTEGER_CONST', r'\d(\d)*'),          # INT
        ('NEWLINE', r'\n'),         # NEW LINE
        ('SKIP', r'[ \t]+'),        # SPACE and TABS
        ('MISMATCH', r'.'),         # ANOTHER CHARACTER
    ]

    tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
    lin_start = 0

    # Lists of output for the program
    token = []
    lexeme = []
    row = []
    column = []

    # It analyzes the code to find the lexemes and their respective Tokens
    for m in re.finditer(tokens_join, code):
        token_type = m.lastgroup
        token_lexeme = m.group(token_type)

        if token_type == 'NEWLINE':
            lin_start = m.end()
            lin_num += 1
        elif token_type == 'SKIP':
            continue
        elif token_type == 'MISMATCH':
            raise RuntimeError('%r unexpected on line %d' % (token_lexeme, lin_num))
        else:
                col = m.start() - lin_start
                column.append(col)
                token.append(token_type)
                lexeme.append(token_lexeme)
                row.append(lin_num)
                # To print information about a Token
                #print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, lin_num, col))

    return token, lexeme, row, column


def app():

    st.title('Lexical Analyzer using python')
    st.markdown('Lexical analysis is the first phase of a compiler. Its job is to turn a raw byte or char- acter input stream coming from the source file into a token stream by chopping the input into pieces and skipping over irrelevant details.')

    st.subheader('Example Input file')

    option = st.selectbox(
        'Select an option',
        ('example 1', 'example 2', 'example 3'))

    if(option == 'example 1'):
        option = 'ex1'
    elif(option == 'example 2'):
        option = 'ex2'
    elif(option == 'example 3'):
        option = 'ex3'

    if option == 'ex1':

        code = '''int main()
        {
            float a;
            a = 1.1;
            int i, inc, j;
            i = 0;
            inc = 2;
            read j;

            while (i < j)
            {
                i = i + inc;
                a = a*i;
            }

            if (a > 10.0)
            {
                print(a + i);
            }
        }'''

    elif option == 'ex2':
        code = '''int main()
    {
        float m;
        z = 1.1;
        int i, inc, j;

        while(z && 2 == 0){
            i = 0;
            inc = 2;
            j = 0;

            if( h >= 3,4 +3){
                print(k);
            else{
                print(k*6+2);
            }

            }
    
            }

    }'''

    elif option == 'ex3':
        code = '''int main()
    {
        float m;
        z = 1.1;
        int i, inc, j;

        while(z && 2 == 0){
            i = 0;
            inc = 2;
            j = 0;
    
            }

    }'''

    st.code(code, language='c')


    if st.button('Perform Lexical Analysis'):
        # Lists for every list returned list from the function tokenize
        token = []
        lexeme = []
        row = []
        column = []
        tabl = []

        # Tokenize and reload of the buffer
        for i in load_buffer(option):
            t, lex, lin, col = tokenize(i)
            token += t
            lexeme += lex
            row += lin
            column += col


        for i in range(len(token)):
            #lis = [token[i],lexeme[i],row[i],column[i]]
            lis = [token[i],lexeme[i]]
            tabl.append(lis)
        # print(tabl)
        headd=["token", "lexeme", "row","column"]
        headd = headd[:2]
        print(tabulate(tabl, headers=headd,tablefmt="pretty"))

        df = pd.DataFrame(list(zip(token, lexeme)),columns =['Token', 'Lexeme'])
        st.table(df)

        
        # print('\nRecognize Tokens: ', token)

