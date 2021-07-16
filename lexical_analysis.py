"""Lexical Analysis for Compiler P--

This script is used to make the lexical analysis of the P-- Compiler

This tool accepts an input file (.txt) and saves the result in the output file(.txt).

This script not requires any module to be installed, is only necessary Python >= 3.8 environment to running.

This file can also be imported as a module using:
	import lexical_analysis

Authors: Bruno Ribeiro Helou (10276852)
         Juan Carlos Elias Obando Valdivia (7487156)
         Maria Luisa do Nascimento da Silva (10310721)



"""

import re
lexical_errors = ""

def is_num_int_automata(final_word: str) -> list:

    """
    Check if a given word is an integer number.

    Regular definition for recognizing integer numbers:

    	digit_non_0 -> 1|...|9
		digit -> 0|1|...|9
		integer_number -> 0 | (digit_non_0)(digit)*

    Arguments:
    ----------------------------------------
    final_word : str
        word to be checked by the automata

    Returns:
    -----------------------------------------
    list : [bool, str]
        bool - True: if a given word is an integer number, False: otherwise
        str - 'num_int': if a given word is an integer number (i.e. token), "": otherwise

    """

    if re.match("^(0|[1-9]\d*)$", final_word):
        token = 'num_int'
        return [True, token]
    else :
        return [False, ""]

##########################################################################################################

def is_num_real_automata(final_word: str) -> list:

    """
    Check if a given word is a real number.

    Regular definition for recognizing real numbers:

        digit_non_0 -> 1|...|9
		digit -> 0|1|...|9
		integer_number -> (0)(.)(digit)+| (digit_non_0)(digit)*(.)(digit)+

    Arguments:
    ----------------------------------------
    final_word : str
        word to be checked by the automata

    Returns:
    -----------------------------------------
    list : [bool, str]
        bool - True: if a given word is a real number, False: otherwise
        str - 'num_real': if a given word is a real number (i.e. token), "": otherwise

    """
    if re.match('^(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$', final_word):
        token = 'num_real'
        return [True, token]
    else :
        return [False, ""]

###########################################################################################################

def is_identifier_automata(final_word: str) -> list:

    """
    Check if a given word is an identifier or a reserved word.

	Regular definition for recognizing identifiers:
    	letter -> a|b|...z|A|B|...|Z
		digit -> 0|1|...|9
		identifier -> letter(letter|digit)*

	Reserved words: ['program','begin','end', 'const'','var', 'real', 'integer', 'procedure', 'read', 'else', 'while', 'do','for','to', 'if','then','else']

    Arguments:
    ----------------------------------------
    final_word : str
        word to be checked by the automata

    Returns:
    -----------------------------------------
    list : [bool, str]
        bool - True: if a given word is an identifier or reserved word, False: otherwise
        str - 'ident': if a given word is an identifier or referent reserved token: if a given word is a reserved word, "": otherwise

    """

    reserved_words = ({'program':'symb_program','begin':'symb_begin','end':'symb_end', 'const': 'symb_const',
                    'var':'symb_var', 'real':'symb_real', 'integer':'symb_integer', 'procedure':'symb_procedure',
                    'read':'symb_read', 'else':'symb_else', 'while':'symb_while', 'do':'symb_do','for':'symb_for',
                    'to':'symb_to', 'if':'symb_if','then':'symb_then','else':'symb_else'})

    if final_word in reserved_words:
        token = reserved_words[final_word]
        return [True, token]
    elif re.match('(^[a-zA-Z][a-zA-Z0-9]*)$', final_word):
        token = 'ident'
        return [True, token]
    else:
        return [False, ""]

########################################################################################################

def is_punctuation_automata(final_word: str) -> list:

    """
    Check if a given word is a punctuation.


    Punctuation words: ['+', '-', '*', '/', '>','<', '(', ')', '.', ':', ',', '=', ':=', '>=', '<=', '<>']

    Arguments:
    ----------------------------------------
    final_word : str
        word to be checked by the automata

    Returns:
    -----------------------------------------
    list : [bool, str]
        bool - True: if a given word is a punctuation word, False: otherwise
        str - referent punctuation token: if a given word is a punctuation word, "": otherwise

    """

    punct_words = ({'+': 'symb_add', '-': 'symb_diff', '*': 'symb_mult', '/': 'symb_div', '>': 'symb_gt',
                    '<': 'symb_lt', '(': 'symb_oparentesis', ')': 'symb_cparentesis', '.':'symb_dot',
                    ':': 'symb_col',';':'symb_semicol',',':'symb_coma', '=': 'symb_eq',':=':'symb_assign',
                    '>=':'symb_gte', '<=':'symb_lte', '<>':'symb_neq'})

    if final_word in punct_words:
        token = punct_words[final_word]
        return [True, token]
    else :
        return [False, ""]

########################################################################################################

def get_message_lexical_error (id_error: int, number_line: int) -> str:

    """
    Returns lexical error message.


    Arguments:
    ----------------------------------------
    id_error : int
        type of error (1: invalid number, 2: invalid identifier, 3: invalid character, 4: comment not finished)
    number_line: int
        file line where the error occurred

    Returns:
    -----------------------------------------
    str :
        error_message: lexical error message

    """
    global lexical_errors
    if id_error == 1:
        error_message = "Erro léxico na linha {}: Número inválido".format(str(number_line))
        lexical_errors = lexical_errors + error_message +'\n'
        return error_message
    if id_error == 2:
        error_message = "Erro léxico na linha {}: Identificador inválido".format(str(number_line))
        lexical_errors = lexical_errors + error_message + '\n'
        return error_message
    if id_error == 3:
        error_message = "Erro léxico na linha {}: Caracter inválido".format(str(number_line))
        lexical_errors = lexical_errors + error_message + '\n'
        return error_message
    if id_error == 4:
        error_message = "Erro léxico na linha {}: Comentário não finalizado".format(str(number_line))
        lexical_errors = lexical_errors + error_message + '\n'
        return error_message
        

##########################################

def add_final_word_to_table (table_tokens: list, lexical_message: str, final_word: str, counter_lines: int, counter_errors: int) -> list:

    """
    Add a word and the corresponding token to table when the word is recognized by one of the defined automatas is this module.
    Else the corresponding lexical message error is obtained.


    Arguments:
    ----------------------------------------

    table_tokens : list
    	list containing the word and the corresponding token until now
    lexical_message : str
    	result to be added in the output file until now
    final_word : str
        word to be checked by the automata
    counter_lines : int
        file line where the word occurred
    counter_errors : int
        current number of errors that ocurred until now


    Returns:
    -----------------------------------------
    list : [str, int]
    	str - lexical_message updated
    	int - counter_errors updated

    """

    is_error = False
    #if first character is digit, check if is an integer number or real number
    if final_word[0].isdigit() == True:
        resp_aux = is_num_int_automata(final_word)

        if resp_aux[0] == False:
            resp_aux = is_num_real_automata(final_word)

        #if is not a number, number error is detected
        if resp_aux[0] == False:
            resp_aux[1] = 'num_real'
            lexical_message = lexical_message + final_word + ',' + get_message_lexical_error (1, counter_lines) + "\n"
            counter_errors += 1
            is_error = True

    #check if is a punctuation character
    elif (final_word[0] >= ':' and final_word[0] <= '>') or (final_word[0] >= '(' and final_word[0] <= '/'):
        resp_aux = is_punctuation_automata(final_word)

    #check if is a identifier character
    elif re.match('^([a-zA-Z0-9]+)$', final_word[0]):
        resp_aux = is_identifier_automata(final_word)

        #if is not an identifier, identifier error is detected
        if resp_aux[0] == False:
            resp_aux[1] = 'ident'
            lexical_message = lexical_message + final_word + ',' + get_message_lexical_error (2, counter_lines) + "\n"
            counter_errors += 1
            is_error = True

    #if is not a number, or a punctuation or an identifier: invalid character error is detected
    else :
        lexical_message = lexical_message + final_word + ',' + get_message_lexical_error (3, counter_lines) + "\n"
        counter_errors += 1
        is_error = True

    #if error is not detected, add final_word and token to table_tokens
    if is_error == False:
        table_tokens.append({'cadeia': final_word, 'token': resp_aux[1], 'counter_lines':counter_lines})
        lexical_message = lexical_message + final_word + ',' + resp_aux[1] + "\n"
    return [lexical_message, counter_errors]

#####################################################################################################################

def check_one_or_two_characters (character: str, final_word: str, sentence: str, counter_characters:int, counter_lines: int, counter_errors: int,
                                 is_comment: bool, has_2_characters: bool, lexical_message: str, table_tokens: list) -> list:

    """
    Check if the current character in the current sentence (that can be include more than one word) is a puctuation word that has one or two characters


    Arguments:
    ----------------------------------------
    character: str
        current character in the current sentence
    final_word : str
        current word to be checked by the automata
    sentence: str
        current sentence (that can be include more than one word)
        Ex: x:=x+1; {sentence with 6 words, but 7 characters}
    counter_characters: int
        number of characters in the current sentence
    counter_lines : int
        file line where the word occurred
    counter_errors : int
        current number of errors that ocurred until now
    is_comment : bool
        flag to detect if a comment was opened
    has_2_character: bool
        flag that suggest if we probably have a word with 2 characters
    lexical_message : str
        result to be added in the output file until now
    table_tokens : list
        list containing the word and the corresponding token until now


    Returns:
    -----------------------------------------
    list : [str, int, bool, str, list, int]
        str - lexical_message updated
        int - counter_errors updated
        bool - has_2_characters updated
        str - final_word updated
        list - table_tokens updated
        counter_characters - counter_characters updated

    """

    counter_characters += 1

    #check if the character is a common symbol
    if character in '=,;()+-/*' and is_comment==False and has_2_characters==False:
        if final_word != "":
            lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message,
                                                            final_word, counter_lines, counter_errors)
        final_word = ""
        counter_characters = 0
        final_word = final_word + character
        if counter_characters != len(sentence):
            if final_word != "":
                lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message,
                                                                final_word, counter_lines, counter_errors)
            final_word = ""
            counter_characters = 0

    #check if the current character is a symbol (':', '<', '>') that can have a final_word with 2 characters
    elif character in ':<>' and is_comment==False and has_2_characters==False:
        if final_word != "":
            lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message, final_word, counter_lines, counter_errors)
        final_word = ""
        counter_characters = 0
        final_word = final_word + character
        has_2_characters=True

    #check if a symbol with 2 characters was detected
    elif is_comment==False and has_2_characters==True:
        #if symbol has 2 characters (i.e. final word is in [':', '<', '>'] and the current character is  the corresponding character to complete the symbol) add them to table
        #LOOKAHEAD
        if (final_word == ':' and character == '=') or (final_word == '<' and character == '>') or (final_word == '>' and character == '=') or (final_word == '<' and character == '='):
            final_word = final_word + character
            if final_word != "":
                lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message, final_word, counter_lines, counter_errors)
            final_word = ""
            counter_characters = 0
        #else the symbol has only 1 character (i.e GO BACK)
        else:
            if final_word != "":
                lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message, final_word, counter_lines, counter_errors)
            final_word = ""
            counter_characters = 0
            #final_word is updated with the no processed character (this final_word will be processed later)
            final_word = final_word + character
        has_2_characters=False
    return [lexical_message, counter_errors, has_2_characters, final_word, table_tokens, counter_characters]

##############################################################################################################################################################

def check_end_program (character:str, final_word: str, counter_errors: int, counter_lines: int, lexical_message: str, table_tokens: list) -> list:

    """
    Insert 'end' to table_tokens and update the final_word with '.' (this character will be processed later)


    Arguments:
    ----------------------------------------
    character: str
        current character in the current sentence
    final_word : str
        current word to be checked by the automata
    counter_lines : int
        file line where the word occurred
    counter_errors : int
        current number of errors that ocurred until now
    lexical_message : str
        result to be added in the output file until now
    table_tokens : list
        list containing the word and the corresponding token until now


    Returns:
    -----------------------------------------
    list : [str, int, str, list, int]
        str - lexical_message updated
        int - counter_errors updated
        str - final_word updated
        list - table_tokens updated
        counter_characters - counter_characters updated

    """


    lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message, final_word, counter_lines, counter_errors)
    final_word = ""
    final_word = final_word + character
    return [lexical_message, counter_errors, final_word, table_tokens]


##############################################################################################################################################################

def check_comments (character: str, is_comment: bool, counter_lines: str) -> list:

    """
    Checks if a probably comment begun ('{'), or the comment is closed.


    Arguments:
    ----------------------------------------
    character: str
        current character in the current sentence
    is_comment : bool
        flag to detect if a comment was opened
    counter_lines : int
        file line where the word occurred


    Returns:
    -----------------------------------------
    list : [bool, int]
        bool - is_comment updated
        line_comment - number of line where the comment begun

    """
    line_comment = ""
    if (is_comment == False) and (character == '{'):
        line_comment = counter_lines
        is_comment = True
    elif (is_comment == True) and (character == '}'):
        is_comment = False

    return [is_comment, line_comment]

###############################################################################################################################################################

def make_lexical_analysis (file_name_input: str, file_name_output: str) -> str:
    """
    Make the lexical analysis of an input file (p--	code) and saves the result in the output file.


    Arguments:
    ----------------------------------------
    file_name_input: str
        name of the input file (p-- code)
    file_name_output: str
        name of the output file (file that contains the result of lexical analysis)


    Returns:
    -----------------------------------------
    None

    """

    #open and read lines of input file (p-- code)
    file_input = open(file_name_input, 'r')
    lines = file_input.readlines()

    is_comment = False
    has_2_characters = False
    counter_lines = 1
    counter_errors = 0
    counter_characters = 0
    table_tokens = []
    lexical_message = ""
    lexical_error = ""
    final_word = ""

	#get each line
    for line in lines:

        #get words in a line
        words_in_line = line.strip().split(' ')

        #get sentences for words in a line
        for sentence in words_in_line:

            counter_characters = 0

            #get character in a sentence
            for character in sentence:
	            #current character is a puctuation word?
                if (character in '=,;()+-/*' and is_comment==False and has_2_characters==False) or \
                    (character in ':<>' and is_comment==False and has_2_characters==False) or \
                    (is_comment==False and has_2_characters==True):

                    lexical_message, counter_errors, has_2_characters, final_word, table_tokens, counter_characters = check_one_or_two_characters (character, final_word, sentence, counter_characters, counter_lines,
                            counter_errors,is_comment, has_2_characters, lexical_message, table_tokens)

	            #current final_word is 'end' and current character is '.' (i.e. end of p-- code)?
                elif (is_comment==False) and (final_word == 'end' and character == '.'):
                    lexical_message, counter_errors, final_word, table_tokens = check_end_program (character, final_word, counter_errors, counter_lines, lexical_message, table_tokens)

	            #check if the comment starts or ends
                elif ((is_comment == False) and (character == '{')) or ((is_comment == True) and (character == '}')):
                    is_comment, line_comment = check_comments (character, is_comment, counter_lines)

	            #final word is probably an identifier, a reserved word, an integer number or a real number!!!
                elif is_comment == False:
                    final_word = final_word + character

            if final_word != "":
                #recognize the final_word and added to table
                lexical_message, counter_errors =  add_final_word_to_table (table_tokens, lexical_message, final_word, counter_lines, counter_errors)
                final_word = ""

	    #analyse next line
        counter_lines = counter_lines + 1

	#the comment was opened but not closed?
    if is_comment == True:
        lexical_message = lexical_message + final_word + ',' + get_message_lexical_error (4, counter_lines-1)
        counter_errors += 1

	#open output file and write lexical message
    
    file_output = open(file_name_output, 'w')
    file_output.write(lexical_errors)
    

    file_output.close()
    file_input.close()
    return table_tokens
