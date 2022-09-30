
import inflect

def main():
    names_list = []

    while True:
        try:
            names_list.append(input("Input a name: "))
        except EOFError:
            break

    #string = make_string(names_list)
    string = string_inflect(names_list)
    print()
    print(string)


def make_string(names_list):
    adieu = 'Adieu, adieu, to '

    if len(names_list) == 1:
        return adieu + names_list[0]

    for name in names_list[0:-2]:
        adieu += name + ', '

    adieu += f'{names_list[-2]} and {names_list[-1]}'
    return adieu


def string_inflect(names_list):
    p = inflect.engine()

    adieu = 'Adieu, adieu, to '
    joined_names = p.join(names_list, final_sep="")
    return adieu + joined_names

if __name__ == "__main__":
    main()