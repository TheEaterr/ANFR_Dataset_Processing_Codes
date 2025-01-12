import pandas as pd

communes_data = pd.read_csv('communes_data.csv', sep=',', header=0)
# make hash map for communes_data
communes_data = communes_data.set_index('code_insee')

def get_category_from_density(densite: float) -> int:
    if densite < 150:
        return 0
    if densite < 300:
        return 1
    if densite < 750:
        return 2
    if densite < 1200:
        return 3
    if densite < 2700:
        return 4
    return 5

def get_category(code_insee: str) -> int:
    # if the code insee starts with 751, it is a Paris arrondissement
    if code_insee.startswith('751'):
        code_insee = '75056'
    # if the code insee starts with 6938, it is a Lyon arrondissement
    if code_insee.startswith('6938'):
        code_insee = '69123'
    # if the code insee starts with 132, it is a Marseilles arrondissement
    if code_insee.startswith('132'):
        code_insee = '13055'
    # if the code insee starts with 98, it is in french Polynesia, Wallis and Futuna, or New Caledonia
    if code_insee.startswith('98'):
        return 1
    # Removing Mayotte, saint pierre and miquelon, saint barthelemy and saint martin
    if code_insee.startswith('975'):
        return 1
    if code_insee.startswith('976'):
        return 1
    if code_insee.startswith('977'):
        return 1
    if code_insee.startswith('978'):
        return 1
    # This communes were merged with others and have an updated code_insee
    if code_insee == '51063':
        code_insee = '51457'
    if code_insee == '85037':
        code_insee = '85289'
    if code_insee == '53239':
        code_insee = '53249'
    if code_insee == '24314' or code_insee == '24089':
        code_insee = '24325'
    if code_insee == '85307':
        code_insee = '85001'
    if code_insee == '01039':
        code_insee = '01138'
    if code_insee == '26219':
        code_insee = '26216'
    if code_insee == '16351':
        code_insee = '16233'
    if code_insee == '16140':
        code_insee = '16206'
    # find the commune with the same code_insee
    try:
        commune = communes_data.loc[code_insee]
        return get_category_from_density(commune['densite'])
    except KeyError:
        # print('Commune not found: ' + code_insee)
        return 0
