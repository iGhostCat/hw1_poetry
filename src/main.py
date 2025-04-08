def get_mask_card_number(card_number):
  splited_number = ' '.join(card_number[i*4:(i+1)*4] for i in range(4))
  output= splited_number.replace( splited_number[7:14],'** ****')
  return output


def get_mask_account(acc_number):
  return '**'+str(acc_number[-1:-5:-1])
