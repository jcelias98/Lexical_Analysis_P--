def program_syntatic(chain, number_of_errors):
    if chain[0]['token'] == 'symb_program':
        chain.pop(0)
        if chain[0]['token'] == 'ident':
            chain.pop(0)
            if chain[0]['token'] == 'symb_semicol':
                chain.pop(0)
                body = body_syntatic(chain)
                if body[0]['token'] == 'symb_dot':
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
        commands = comands_syntatic(dc)
        if commands[0]['token'] == 'symb_end':
            commands.pop(0)
            return commands
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
def comands_syntatic(dc):
    cmd = cmd_syntatic(dc)
    if cmd[0]['token'] == 'symb_semicol':
        cmd.pop(0)
        return comands_syntatic(cmd)
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
            print('erro ident')
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
    if dc_v[0]['token'] == 'symb_procedure':
        dc_v.pop(0)
        if dc_v[0]['token'] == 'ident':
            dc_v.pop(0)
            params = params_syntatic(dc_v)
            if params[0]['token'] == 'symb_semicol':
                params.pop(0)
                p_body = p_body_syntatic(params)
                return dc_p_syntatic(p_body)
            else:
                print('erro symb semicol dc_p ')
        else:
            print('erro ident dc_p')
    return dc_v

################################################
def number_syntatic(number):
    if number[0]['token'] == 'num_int' or number[0]['token'] == 'num_real':
        number.pop(0)
    else:
        print('tratar erro number')

    return number

################################################ SE SOBRAR TEMPO ARRUMA ISSO AQUI
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

 ################################################
def params_syntatic(dc_v):
    if dc_v[0]['token'] == 'symb_oparentesis':
        dc_v.pop(0)
        par_list = par_list_syntatic(dc_v)
        if par_list[0]['token'] == 'symb_cparentesis':
            par_list.pop(0)
            return par_list
        else:
            print('erro cparentesis')
    return dc_v

################################################
def p_body_syntatic(params):
    dc_v = dc_v_syntatic(params)
    if dc_v[0]['token'] == 'symb_begin':
        dc_v.pop(0)
        commands = comands_syntatic(dc_v)
        if commands[0]['token'] == 'symb_end':
            commands.pop(0)
            if commands[0]['token'] == 'symb_semicol':
                commands.pop(0)
                return commands
            else:
                print('erro symb_semicol p_body')
        else:
            print('erro symb end p_body')
    else:
        print('erro symb_begin p_body ')

################################################
def par_list_syntatic(params):
    var = var_syntatic(params)
    if var[0]['token'] == 'symb_col':
        var.pop(0)
        type_var = type_var_syntatic(var)
        if type_var[0]['token'] == 'symb_semicol':
            type_var.pop(0)
            return par_list_syntatic(type_var)
        else:
            return type_var
    return params

################################################
def cmd_syntatic(chain):
    if chain[0]['token'] == 'symb_read' or chain[0]['token'] == 'symb_write' :
        chain.pop(0)
        if chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
            var =  var_syntatic(chain)
            if var[0]['token'] == 'symb_cparentesis':
                var.pop(0)
                return var
            else:
                print("erro fecha parentesis cmd")
        else:
            print('erro open parentesis')
    elif chain[0]['token'] == 'symb_while':
        chain.pop(0)
        if chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
            condition = condition_syntatic(chain)
            if condition[0]['token'] == 'symb_cparentesis':
                condition.pop(0)
                if condition[0]['token'] == 'symb_do':
                    condition.pop(0)
                    return cmd_syntatic(condition)
            else:
                print("erro fecha parentesis cmd")
        else:
            print('erro open parentesis')

    elif chain[0]['token'] == 'ident':
        chain.pop(0)
        if chain[0]['token'] == 'symb_assign':
            chain.pop(0)
            return expression_syntatic(chain)
        elif chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
            args = arguments_syntatic(chain)
            if args[0]['token'] == 'symb_cparentesis':
                args.pop(0)
                return args
            else:
                print('erro cparentesis ident cmd')
        else:
            return chain
    elif chain[0]['token'] == 'symb_begin':
        chain.pop(0)
        commands = comands_syntatic(chain)
        if commands[0]['token'] == 'symb_end':
            commands.pop(0)
            return commands
        else:
            print('erro no end cmd begin')
    elif chain[0]['token'] == 'symb_if':
        chain.pop(0)
        condition = condition_syntatic(chain)
        if condition[0]['token'] == 'symb_then':
            condition.pop(0)
            cmd = cmd_syntatic(condition)
            return pfalse_syntatic(cmd)
    elif chain[0]['token'] == 'symb_for':
        chain.pop(0)
        var = var_syntatic(chain)
        if var[0]['token'] == 'symb_assign':
            var.pop(0)
            if var[0]['token'] == 'num_int':
                var.pop(0)
                if var[0]['token'] == 'symb_to':
                    var.pop(0)
                    if var[0]['token'] == 'num_int':
                        var.pop(0)
                        if var[0]['token'] == 'symb_do':
                            var.pop(0)
                            return cmd_syntatic(var)
                        else:
                            print('no do found in for')
                    else:
                        print(' not a  integer in for loop')
                else:
                    print('no terminal to in for loop')
            else:
                print('must be an int to loop for')
        else:
            print(' do you mean assing? :=')
    else:
        return chain

#################################################
def condition_syntatic(chain):
    expression = expression_syntatic(chain)
    if expression[0]['token']  in ['symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt']:
        expression.pop(0)
    else:
        print('irregular expression detected')
    return expression_syntatic(expression)

##################################################
def expression_syntatic(chain):
    term = term_syntatic(chain)
    other_term = other_therm_syntatic(term)
    return other_term
##################################################
def term_syntatic(chain):
    if chain[0]['token'] in ['symb_add', 'symb_diff']:
        chain.pop(0)
    factor = factor_syntatic(chain)
    return more_factors_syntatic(factor)
####################################################
def factor_syntatic(chain):
    if chain[0]['token'] in ['ident', 'num_int', 'num_real']:
        chain.pop(0)
        return chain
    elif chain[0]['token'] == 'symb_oparentesis':
        chain.pop(0)
        expression = expression_syntatic(chain)
        if expression[0]['token'] == 'symb_cparentesis':
            expression.pop(0)
            return expression
        else:
            print(' missing close parentesis in factor')
    else:
        print('error factor')

####################################################

def more_factors_syntatic(factor):
    if factor[0]['token'] in ['symb_mult', 'symb_div']:
        factor.pop(0)
        factor = factor_syntatic(factor)
        return more_factors_syntatic(factor)
    return factor

####################################################

def arguments_syntatic(chain):
    while chain[0]['token'] == 'ident' or chain[0]['token'] =='symb_semicol':
        chain.pop(0)
    return chain

####################################################

def pfalse_syntatic(chain):
    if chain[0]['token'] == "symb_else":
        chain.pop(0)
        return cmd_syntatic(chain)
    return chain

####################################################

def other_therm_syntatic(chain):
    if chain[0]["token"] in ['symb_add', 'symb_diff']:
        chain.pop(0)
        term = term_syntatic(chain)
        return other_therm_syntatic(term)
    return chain

############ Syntatic Main #####################
def make_syntatic_analysis(chain: str):
    number_of_errors = 0
    rest = program_syntatic(chain, number_of_errors)
    if len(rest) == 0:
        print('Sucess')
    else:
        print('ERRO, Programa não finalizado')
