import time
import sys


def exit_script():
    """Exit function for script"""
    print("Obrigado por utilizar.")
    for i in range(0, 3):
        sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()
        time.sleep(1)
    exit()


def main():
    """Main function for script"""
    from src.read_operations import (
        state_percentage,
        general_info,
        filtering_by_region,
        filtering_by_type
    )
    from src.write_operations import insert_port, update_port, delete_port
    from src.helpers.manage_csv import readcsv

    options = {
        0: exit_script,
        1: state_percentage,
        2: general_info,
        3: filtering_by_region,
        4: filtering_by_type,
        5: insert_port,
        6: update_port,
        7: delete_port,
    }

    print('\n----------MENU PRINCIPAL----------')
    print('(1) Porcentagem de portos por estado')
    print('(2) Informação geral do porto')
    print('(3) Portos por região')
    print('(4) Portos por tipo')
    print('(5) Inserir porto')
    print('(6) Editar porto')
    print('(7) Excluir porto')
    print('(0) Sair')

    choice = int(input('Escolha a função desejada (digite o número): '))

    while 0 > choice > 7:
        print(' Opção invalida. Por favor, selecione uma das opções do menu. ')
        choice = int(input('Escolha a função desejada: '))

    ports = readcsv('data/portos.csv')

    if choice == 0:
        options[choice]()
    else:
        options[choice](ports)


if __name__ == '__main__':
    main()
