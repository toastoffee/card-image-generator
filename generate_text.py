import pandas as pd

def get_card_desc(entity):
    name = entity[0]
    type_name = entity[1]
    cost = entity[2]
    effects = entity[4]
    return f"{name}\t{cost}费\t{type_name}\n{effects}\n";


if __name__ == "__main__":

    card_data = pd.read_excel('card_data.xlsx', sheet_name='单卡')
    print(card_data.values)

    result_str = "";

    for entity in card_data.values:
        result_str += get_card_desc(entity)

    with open('card_desc.txt', 'w', encoding='utf-8') as f:
        f.write(result_str)