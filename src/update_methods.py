import time
import sys
from src.helpers.manage_csv import writecsv
from main import main

port_headers = [
        "PORTO",
        "REGIÃO",
        "AUTORIDADE PORTUARIA",
        "TIPO",
        "VIA",
        "ESTADO",
    ]


def port_name(port_select: str, ports: list[dict]):
    """Edit the port name

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_name = input("Escolha o novo nome do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    print(selected_port)
    ports[selected_port[0][0]]["PORTO"] = new_port_name
    writecsv("data/portos.csv", port_headers, ports)


def port_region(port_select: str, ports: list[dict]):
    """Edit the port region

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_region = input("Escolha a nova região do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    ports[selected_port[0][0]]["REGIÃO"] = new_port_region
    writecsv("data/portos.csv", port_headers, ports)


def port_autority(port_select: str, ports: list[dict]):
    """Edit the port autority

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_autority = input("Escolha a nova autoridade portuaria do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    ports[selected_port[0][0]]["AUTORIDADE PORTUARIA"] = new_port_autority
    writecsv("data/portos.csv", port_headers, ports)


def port_type(port_select: str, ports: list[dict]):
    """Edit the port type

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_type = input("Escolha o novo tipo do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    ports[selected_port[0][0]]["TIPO"] = new_port_type
    writecsv("data/portos.csv", port_headers, ports)


def port_way(port_select: str, ports: list[dict]):
    """Edit the port way

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_way = input("Escolha a nova via do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    ports[selected_port[0][0]]["VIA"] = new_port_way
    writecsv("data/portos.csv", port_headers, ports)


def port_state(port_select: str, ports: list[dict]):
    """Edit the port state

    Parameters

    ----------

    port_select: string
    ports: list
    """
    new_port_state = input("Escolha o novo estado do porto: ")
    selected_port = [
        (index, port)
        for index, port in enumerate(ports)
        if port["PORTO"] == port_select
    ]
    ports[selected_port[0][0]]["ESTADO"] = new_port_state
    writecsv("data/portos.csv", port_headers, ports)


def exit_update():
    """Exit function for update"""
    print("Obrigado por utilizar.")
    for i in range(0, 3):
        sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()
        time.sleep(1)
    main()
