import panic_method
term_followers = {'symb_program': ["ident"], 'ident': ['symb_semicol', 'symb_coma', 'symb_col', 'symb_oparentesis', 'symb_begin', 'symb_cparentesis', 'symb_assign', 'symb_add', 'symb_diff', 'symb_div', 'symb_mult', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'],
'symb_semicol':['symb_const', 'symb_var', 'symb_procedure', 'symb_begin', 'symb_cparentesis', 'symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_semicol'],'symb_begin': ['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_end', 'symb_dot', 'symb_procedure', 'symb_semicol'],
'symb_end': ['symb_dot', 'symb_procedure', 'symb_begin', 'symb_semicol'], 'symb_const': ['ident', 'symb_var', 'symb_procedure', 'symb_begin'], 'ident': ['symb_eq', 'symb_var', 'symb_procedure', 'symb_begin'], 'symb_eq': ['num_integer', 'num_real','symb_var', 'symb_procedure', 'symb_begin'],'symb_var': ['ident', 'symb_procedure', 'symb_begin', 'symb_col', 'symb_semicol', 'symb_integer', 'symb_real', 'symb_read', 'symb_write', 'symb_while', 'ident', 'symb_if', 'symb_for', 'symb_end'],
'symb_col': ['symb_real', 'symb_integer', 'symb_procedure', 'symb_begin', 'symb_cparentesis'], 'symb_real': ['symb_semicol'], 'symb_integer': ['symb_semicol', 'symb_cparentesis'], 'symb_coma': ['ident', 'symb_col'],
'symb_oparentesis': ['ident', 'symb_semicol', 'symb_else', 'symb_add', 'symb_diff', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt', 'symb_mult', 'symb_div'],
'symb_cparentesis': ['symb_begin', 'symb_semicol', 'symb_else', 'symb_do', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt', 'symb_mult', 'symb_div'],
'symb_else': ['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for','symb_semicol'], 'symb_read': ['symb_oparentesis', 'symb_semicol'], 'symb_write': ['symb_oparentesis', 'symb_semicol'], 'symb_while': ['symb_oparentesis', 'symb_semicol'],
'do': ['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_semicol'], 'symb_if': ['symb_add', 'symb_diff', 'num_int', 'num_real', 'symb_oparentesis'],
'then': ['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_semicol'], 'symb_assing': ['symb_add', 'symb_diff', 'num_int', 'num_real', 'symb_oparentesis', 'symb_semicol'], 'symb_for': ['ident', 'symb_semicol'], 'symb_assign': ['num_int', 'symb_semicol'],
'num_int': ['symb_to', 'symb_semicol', 'symb_do', 'symb_add', 'symb_diff', 'symb_div', 'symb_mult', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'],
'num_real': ['symb_to', 'symb_semicol', 'symb_do', 'symb_add', 'symb_diff', 'symb_div', 'symb_mult', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'], 'symb_to': ['num_int', 'symb_semicol'], 'symb_do': ['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_end', 'symb_dot', 'symb_procedure', 'symb_semicol'],
'symb_eq': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'], 'symb_neq': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'],
'symb_gte': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'], 'symb_lte': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'],
'symb_gt': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'], 'symb_lt': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then'],
'symb_add': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'],
'symb_diff': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'],
'symb_mult': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'],
'symb_div': ['symb_add', 'symb_diff', 'ident', 'num_int', 'num_real', 'symb_oparentesis', 'symb_cparentesis', 'symb_then', 'symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt'], 'symb_procedure': ['symb_begin', 'ident'],
'symb_then':['symb_read', 'symb_write', 'symb_while', 'ident', 'symb_begin', 'symb_if', 'symb_for', 'symb_end', 'symb_dot', 'symb_procedure', 'symb_semicol']}


def program_syntatic(chain, number_of_errors):
    if chain[0]['token'] == 'symb_program':
        chain.pop(0)
    else:
        get_message_syntatic_error(chain, "'program'", 'symb_program')
    if chain[0]['token'] == 'ident':
        chain.pop(0)
    else:
        get_message_syntatic_error(chain, "identificador", 'ident')
    if chain[0]['token'] == 'symb_semicol':
        chain.pop(0)
    else:
        get_message_syntatic_error(chain, "';'", 'symb_semicol')
    body = body_syntatic(chain)
    if body and body[0]['token'] == 'symb_dot':
        body.pop(0)
        return body
    else:
        print("Erro sintático: '.' esperado")

#################################################

def body_syntatic(chain):
    dc =  dc_syntatic(chain)
    if dc and dc[0]['token'] == 'symb_begin':
        dc.pop(0)
    else:
        commands = get_message_syntatic_error(dc, "begin", 'symb_begin')
    commands = comands_syntatic(dc)
    if commands and commands[0]['token'] == 'symb_end':
        commands.pop(0)
    else:
        commands = get_message_syntatic_error(commands, "end", 'symb_end')
    return commands

###############################################

def dc_syntatic(chain):
    dc_c = dc_c_syntatic(chain)
    dc_v = dc_v_syntatic(dc_c)
    dc_p = dc_p_syntatic(dc_v)
    return dc_p

################################################

def comands_syntatic(dc):
    cmd = cmd_syntatic(dc)
    if cmd and cmd[0]['token'] == 'symb_semicol':
        cmd.pop(0)
        return comands_syntatic(cmd)
    return dc

################################################
def dc_c_syntatic(chain):
    if chain and chain[0]['token'] =='symb_const':
        chain.pop(0)
    elif chain and (chain[0]['token'] =='symb_var' or chain[0]['token'] =='symb_procedure' or chain[0]['token'] =='symb_begin'):
        return chain
    elif  chain[0]['token'] in term_followers['symb_begin'] and chain[0]['token'] != 'symb_begin':
        chain = get_message_syntatic_error(chain, 'begin', 'symb_begin')
        return chain
    else:
        chain = get_message_syntatic_error(chain, "const", 'symb_const')

    if chain and chain[0]['token'] =='ident':
        chain.pop(0)
    else:
        chain = get_message_syntatic_error(chain, "identificador", 'ident')

    if chain and chain[0]['token'] == 'symb_eq':
        chain.pop(0)
    else:
        chain = get_message_syntatic_error(chain, "'='", 'symb_eq')

    number = number_syntatic(chain)
    if number and number[0]['token'] =='symb_semicol':
        number.pop(0)
    else:
        number = get_message_syntatic_error(number, "';'", 'symb_semicol')
    dc_c = dc_c_syntatic(number)
    return dc_c

################################################
def dc_v_syntatic(dc_c):
    if dc_c and dc_c[0]['token'] =='symb_var':
        dc_c.pop(0)
    elif dc_c and dc_c[0]['token'] in ['symb_procedure', 'symb_begin']:
        return dc_c
    elif  dc_c and dc_c[0]['token'] in term_followers['symb_begin'] and dc_c[0]['token'] != 'symb_begin':
        dc_c = get_message_syntatic_error(dc_c, 'begin', 'symb_begin')
        return dc_c
    else:
        dc_c = get_message_syntatic_error(dc_c, "var", 'symb_var')
    var = var_syntatic(dc_c)

    if var and var[0]['token'] =='symb_col':
        var.pop(0)
    else:
        var = get_message_syntatic_error(var, "':'", 'symb_col')
    type_var = type_var_syntatic(var)

    if type_var and type_var[0]['token'] =='symb_semicol':
        type_var.pop(0)
    else:
        type_var = get_message_syntatic_error(type_var, "';'", 'symb_semicol')
    dc_v = dc_v_syntatic(type_var)

    return dc_v

################################################
def dc_p_syntatic(dc_v):
    if dc_v and dc_v[0]['token'] == 'symb_procedure':
        dc_v.pop(0)
    elif dc_v and  dc_v[0]['token'] =='symb_begin':
        return dc_v
    elif  dc_v and dc_v[0]['token'] in term_followers['symb_begin'] and dc_v[0]['token'] != 'symb_begin':
        dc_v = get_message_syntatic_error(dc_v, 'begin', 'symb_begin')
        return dc_v
    else:
        dc_v = get_message_syntatic_error(dc_v, 'procedure', 'symb_procedure')

    if dc_v and dc_v[0]['token'] == 'ident':
        dc_v.pop(0)
    else:
        dc_v = get_message_syntatic_error(dc_v, "identificador", 'ident')

    params = params_syntatic(dc_v)
    if  params and params[0]['token'] == 'symb_semicol':
        params.pop(0)
    else:
        params = get_message_syntatic_error(params, "';'", 'symb_semicol')
    p_body = p_body_syntatic(params)
    return dc_p_syntatic(p_body)

################################################
def number_syntatic(number):
    if number and (number[0]['token'] == 'num_int' or number[0]['token'] == 'num_real'):
        number.pop(0)
    else:
        get_message_syntatic_error(number, "número",  'num_int')
    return number

################################################ SE SOBRAR TEMPO ARRUMA ISSO AQUI
def var_syntatic(var):
    while var and (var[0]['token'] == 'ident' or var[0]['token'] =='symb_coma'):
        var.pop(0)
    return var

################################################
def type_var_syntatic(number):
    if number and (number[0]['token'] == 'symb_integer' or number[0]['token'] == 'symb_real'):
        number.pop(0)
    else:
        number = get_message_syntatic_error(number, 'tipo de número (real ou integer)', 'symb_integer')
    return number

 ################################################
def params_syntatic(dc_v):
    if dc_v and dc_v[0]['token'] == 'symb_oparentesis':
        dc_v.pop(0)
    elif  dc_v and (dc_v[0]['token'] == ['symb_semicol', "symb_begin"]):
        return dc_v
    else:
        dc_v = get_message_syntatic_error(dc_v, "'('", 'symb_oparentesis')

    par_list = par_list_syntatic(dc_v)
    if par_list and par_list[0]['token'] == 'symb_cparentesis':
        par_list.pop(0)
    else:
        par_list = get_message_syntatic_error(par_list, "')'", 'symb_cparentesis')
    return par_list

################################################
def p_body_syntatic(params):
    dc_v = dc_v_syntatic(params)
    if dc_v[0]['token'] == 'symb_begin':
        dc_v.pop(0)

    commands = comands_syntatic(dc_v)
    if commands[0]['token'] == 'symb_end':
        commands.pop(0)
    else:
        commands = get_message_syntatic_error(commands, "end", 'symb_end')

    if commands[0]['token'] == 'symb_semicol':
        commands.pop(0)
    else:
        commands = get_message_syntatic_error(commands, "';'", 'symb_semicol')
    return commands

################################################
def par_list_syntatic(params):
    var = var_syntatic(params)
    if var and var[0]['token'] == 'symb_col':
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
    if chain and (chain[0]['token'] == 'symb_read' or chain[0]['token'] == 'symb_write'):
        chain.pop(0)
        if chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
        else:
            chain = get_message_syntatic_error(chain, "'('", 'symb_oparentesis')

        var =  var_syntatic(chain)
        if var[0]['token'] == 'symb_cparentesis':
            var.pop(0)
        else:
            get_message_syntatic_error(var, "')'", 'symb_cparentesis')
        return var

    elif chain and chain[0]['token'] == 'symb_while':
        chain.pop(0)
        if chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
        else:
            chain = get_message_syntatic_error(chain, "'('", 'symb_oparentesis')

        condition = condition_syntatic(chain)
        if condition[0]['token'] == 'symb_cparentesis':
            condition.pop(0)
        else:
            get_message_syntatic_error(condition, "')'", 'symb_cparentesis')

        if condition[0]['token'] == 'symb_do':
            condition.pop(0)
        else:
            chain = get_message_syntatic_error(chain, "'do'", 'symb_do')
        return cmd_syntatic(condition)

    elif chain and chain[0]['token'] == 'ident':
        chain.pop(0)
        if chain[0]['token'] == 'symb_assign':
            chain.pop(0)
            return expression_syntatic(chain)
        elif chain[0]['token'] == 'symb_oparentesis':
            chain.pop(0)
            args = arguments_syntatic(chain)
            if args[0]['token'] == 'symb_cparentesis':
                args.pop(0)
            else:
                args = get_message_syntatic_error(args, "')'", 'symb_cparentesis')
            return args
        else:
            return chain

    elif chain and chain[0]['token'] == 'symb_begin':
        chain.pop(0)
        commands = comands_syntatic(chain)
        if commands[0]['token'] == 'symb_end':
            commands.pop(0)
        else:
            commands = get_message_syntatic_error(commands, 'end', 'symb_end')
        return commands

    elif chain and chain[0]['token'] == 'symb_if':
        chain.pop(0)
        condition = condition_syntatic(chain)
        if condition[0]['token'] == 'symb_then':
            condition.pop(0)
        else:
            condition = get_message_syntatic_error(condition, 'then','symb_then')
        cmd = cmd_syntatic(condition)
        return pfalse_syntatic(cmd)

    elif chain and chain[0]['token'] == 'symb_for':
        chain.pop(0)
        var = var_syntatic(chain)
        if var[0]['token'] == 'symb_assign':
            var.pop(0)
        else:
            var = get_message_syntatic_error(var, '":="', 'symb_assign')

        if var[0]['token'] == 'num_int':
            var.pop(0)
        else:
            var = get_message_syntatic_error(var, 'número inteiro', 'num_int')
        if var[0]['token'] == 'symb_to':
            var.pop(0)
        else:
            var = get_message_syntatic_error(var, '"to"', 'symb_to')
        if var[0]['token'] == 'num_int':
            var.pop(0)
        else:
            var = get_message_syntatic_error(var, 'número inteiro', 'num_int')
        if var[0]['token'] == 'symb_do':
            var.pop(0)
        else:
            var = get_message_syntatic_error(var, '"do"', 'symb_do')
        return cmd_syntatic(var)

    else:
        return chain

#################################################

def condition_syntatic(chain):
    expression = expression_syntatic(chain)
    if expression[0]['token']  in ['symb_eq', 'symb_neq', 'symb_gte', 'symb_lte', 'symb_gt', 'symb_lt']:
        expression.pop(0)
    else:
        expression = get_message_syntatic_error(expression, 'sinal de comparação', 'symb_eq')
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
        else:
            expression = get_message_syntatic_error(expression, "')'",'symb_cparentesis')
        return expression
    else:
        print('Erro sintático: identificador ou número esperado')
        return chain

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

def get_message_syntatic_error(chain, error, symb):
    print('Erro sintático: {} esperado'.format(error))
    return panic_method.panic_method(chain, term_followers[symb])

############ Syntatic Main #####################
def make_syntatic_analysis(chain: str):
    number_of_errors = 0
    rest = program_syntatic(chain, number_of_errors)
    if not rest:
        print('Sucess')
    else:
        print('ERRO, Programa não finalizado')
