def program_syntatic(chain, number_of_errors):
    if chain[0]['token'] == 'symb_program':
        chain.pop(0)
        if chain[0]['token'] == 'ident':
            chain.pop(0)
            if chain[0]['token'] == 'symb_semicol':
                chain.pop(0)
                body = body_syntatic(chain)
                if body == 'symb_dot':
                    body.pop(0)
                    return body
                else:
                    print('erro de .')
            else:
                print('erro semicol')
        else:
            print("erro ident")
    else:
        print("erro program")

#################################################

def body_syntatic(chain):
    dc =  dc_syntatic(chain)
    if dc[0]['token'] == 'symb_begin':
        dc.pop(0)
        
        cmd = cmd_syntatic(dc)
        if cmd[0]['token'] == 'symb_end':
            cmd.pop(0)
            return cmd
        else:
            print('erro missing end')
    else:
        print('Erro symb begin')

    
###############################################
def dc_syntatic(chain):
    dc_c = dc_c_syntatic(chain)
    dc_v = dc_v_syntatic(dc_c)
    dc_p = dc_p_syntatic(dc_v)
    return dc_p
################################################
def cmd_syntatic(dc):
    return dc

################################################
def dc_c_syntatic(chain):
    if chain[0]['token'] =='symb_const':
        chain.pop(0)
        if chain[0]['token'] =='ident':
            chain.pop(0)
            if chain[0]['token'] == 'symb_eq':
                chain.pop(0)
                number = number_syntatic(chain)
                if number[0]['token'] =='symb_semicol':
                    number.pop(0)
                    dc_c = dc_c_syntatic(number)
                    return dc_c
                   
                else:
                    print('erro semicol')
            else:
                print('erro symb _eq')
        else:
            print('erro symb_ident')

                    
    else:
        return chain

################################################
def dc_v_syntatic(dc_c):
    if dc_c[0]['token'] =='symb_var':
        dc_c.pop(0)
        var = var_syntatic(dc_c)
        if var[0]['token'] =='symb_col':
            var.pop(0)
            type_var = type_var_syntatic(var)    
            if type_var[0]['token'] =='symb_semicol':
                type_var.pop(0)
                dc_v = dc_v_syntatic(type_var)
                return dc_v
                   
            else:
                print('erro symb semicol')
        else:
            print('erro symb_col')

                    
    else:
        return dc_c

################################################
def dc_p_syntatic(dc_v):
    return dc_v


################################################
def number_syntatic(number):
    if number[0]['token'] == 'num_int' or number[0]['token'] == 'num_real':
        number.pop(0)
    else:
        print('tratar erro number')
    
    return number

################################################
def var_syntatic(var):
    while var[0]['token'] == 'ident' or var[0]['token'] =='symb_coma':
        var.pop(0)
    return var


################################################
def type_var_syntatic(number):
    if number[0]['token'] == 'symb_integer' or number[0]['token'] == 'symb_real':
        number.pop(0)
    else:
        print('tratar erro number')
    
    return number

############ Syntatic Main #####################
def make_syntatic_analysis(chain: str):
    number_of_errors = 0
    program_syntatic(chain, number_of_errors)
    if len(chain) == 0:
        return 'Sucess'
    else:
        return 'ERRO, Programa não finalizado'
    return 0