import re
import argparse

def format_price(price):

    if not isinstance(price,(str,float,int)):
        raise TypeError('Не правильный формат данных')

    if isinstance(price,str):
        if not re.match('\d+(\.)?\d+$',price):
            raise ValueError('Ошибка в значении цены')
        price = string_to_numeric(price)

    if isinstance(price,float):
        return '{:,.2f}'.format(price).replace(',',' ')

    if isinstance(price,int):
        return '{:,}'.format(price).replace(',', ' ')


def string_to_numeric(value):
    try:
        if value.find('.') >= 0:
            return float(value)
        else :
            return int(value)
    except ValueError:
        return None

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('-p','--price', required=True, help='Value of price')
    arguments = args.parse_args()

    print(format_price(arguments.price))
