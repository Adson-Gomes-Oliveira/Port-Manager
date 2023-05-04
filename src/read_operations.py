import pprint
from main import main


def state_percentage(ports: list[dict]):
    """Returns a percentage of ports that the state have in comparison with
    all states in Brazil

    Parameters

    ----------

    ports: list
    """
    state_select = input("digite o nome do estado: ").upper()
    total_ports = len(ports)

    selected_ports_by_state = [
        port
        for port in ports
        if port["ESTADO"] == state_select
    ]
    total_selected_ports_by_state = len(selected_ports_by_state)

    percentage = (total_selected_ports_by_state / total_ports) * 100

    result = {
        "porcentagem": f"{round(percentage)}%",
        "portos": [],
    }

    for port in selected_ports_by_state:
        result["portos"].append(port["PORTO"])

    pprint.pprint(result)
    main()


def general_info(ports: list[dict]):
    """Returns a general informations about a port choosen by the user

    Parameters

    ----------

    ports: list
    """
    port_select = input("digite o nome do porto: ").upper()
    selected_port = [
        port
        for port in ports
        if port["PORTO"] == port_select
    ]
    pprint.pprint(selected_port)
    main()


def filtering_by_region(ports: list[dict]):
    """Returns ports filtered by region

    Parameters

    ----------

    ports: list
    """
    region_select = input("digite o nome da região: ").upper()
    region = f"REGIÃO {region_select}"
    selected_port_by_region = [
        port
        for port in ports
        if port["REGIÃO"] == region
    ]
    pprint.pprint(selected_port_by_region)
    main()


def filtering_by_type(ports: list[dict]):
    """Returns ports filtered by type

    Parameters

    ----------

    ports: list
    """
    port_types = []
    for port in ports:
        port_types.append(port["TIPO"])
    port_types = list(set(port_types))

    print(
        f"""
    Essa é a lista de tipos de portos:
    {port_types}
    """
    )

    type_select = input("digite o tipo do porto: ").upper()
    selected_port_by_type = [
        port
        for port in ports
        if port["TIPO"] == type_select
    ]
    pprint.pprint(selected_port_by_type)
    main()
