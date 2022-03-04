from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Devolve o codigo de duas letras do Pygal para um pais, dado o seu nome."""
    for code , name in COUNTRIES.items():
        if name == country_name:
            return code
    # Se o pais nao foi encontrado, devolve None
    return None
