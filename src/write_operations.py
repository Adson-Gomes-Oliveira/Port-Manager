import pprint
from main import main
from src import update_methods
from src.helpers.manage_csv import writecsv


def insert_port(ports: list[dict]):
    """Insert a new port in portos.csv

    Parameters

    ----------

    ports: list
    """
    port_headers = [
        "PORTO",
        "REGIÃO",
        "AUTORIDADE PORTUARIA",
        "TIPO",
        "VIA",
        "ESTADO",
    ]

    new_port = input("insira o nome do porto: ")
    new_region = input("insira o nome da região: ")
    new_autority = input("insira o nome da autoridade portuaria: ")
    new_type = input("insira o tipo do porto: ")
    new_way = input("insira a via: ")
    new_state = input("insira o nome do estado: ")

    new_port = {
        "PORTO": new_port,
        "REGIÃO": f"REGIÃO {new_region}",
        "AUTORIDADE PORTUARIA": new_autority,
        "TIPO": new_type,
        "VIA": new_way,
        "ESTADO": new_state,
    }

    ports.append(new_port)
    writecsv("data/portos.csv", port_headers, ports)
    pprint.pprint(ports)
    main()


def update_port(ports: list[dict]):
    """Edit data about a specified port

    Parameters

    ----------

    ports: list
    """
    options = {
        0: update_methods.exit_update,
        1: update_methods.port_name,
        2: update_methods.port_region,
        3: update_methods.port_autority,
        4: update_methods.port_type,
        5: update_methods.port_way,
        6: update_methods.port_state,
    }

    port_select = input("digite o nome do porto: ").upper()

    print("----------MENU DE EDIÇÃO----------")
    print("Informe o campo que você quer editar")
    print("(1) NOME DO PORTO")
    print("(2) REGIÃO")
    print("(3) AUTORIDADE PORTUARIA")
    print("(4) TIPO")
    print("(5) VIA")
    print("(6) ESTADO")
    print("(0) Sair")

    choice = int(input("Escolha a função desejada (digite o número): "))

    while 0 > choice > 6:
        print(" Opção invalida. Por favor, selecione uma das opções do menu. ")
        choice = int(input("Escolha a função desejada: "))

    if choice == 0:
        options[choice]()
    else:
        options[choice](port_select, ports)

    main()


def delete_port(ports: list[dict]):
    """Delete a specified port

    Parameters

    ----------

    ports: list
    """
    port_headers = [
        "PORTO",
        "REGIÃO",
        "AUTORIDADE PORTUARIA",
        "TIPO",
        "VIA",
        "ESTADO",
    ]

    port_select = input("digite o nome do porto: ").upper()
    selected_port = [port for port in ports if port["PORTO"] != port_select]

    ports = selected_port
    writecsv("data/portos.csv", port_headers, ports)

    main()
