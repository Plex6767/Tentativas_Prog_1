presidentes = " lula, flavio, renan, cury"

def separated_values(the_string, the_list):
    start = 0
    for n in range(len(the_string)):
        c = the_string[n]
        if c == ",":
            the_list.append(the_string[start:n])
            # a lista recebe "n" caracteres do inicio ate a ","
            start = n + 1
    if start < len(the_string):
        the_list.append(the_string[start::])
    return None
values_str = []
separated_values(presidentes, values_str)

def remove_spaces(the_string):
    start = 0
    end = len(the_string) - 1
    while the_string[start] == " ":
        start += 1
        #por parar na virgula, ele irá pular para outra casa
        if start == end:
            return ""
        #remove o espaco

    new_string = the_string[start:end + 1]
    return new_string



