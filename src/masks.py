from typing import Union

def get_mask_card_number(card_number):
    '''Функция получения маски номера банковской карты,
    принимает номер карты числом, возвращает его маску в виде:
    XXXX XX** **** XXXX'''

    spl_number = ' '.join(str(card_number[i * 4:(i + 1) * 4]) for i in range(4))
    output = spl_number.replace(spl_number[7 : 14], '** ****')
    return output


def get_mask_account(acc_number):
    '''Функция получения маски номера банковской карты,
      принимает номер карты числом, возвращает его маску в виде:
      **XXXX'''

    return '**' + str(acc_number[-1:-5:-1])
