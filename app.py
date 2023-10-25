'''
Given a number of customers and output file name, this script can generate trajectories and saved as a csv file
2023/10/25 by Eric
'''
from dot_gen import dots_df_gen
import pandas as pd

def main_fn(customer_num, output_name):
    customer_num = int(customer_num)
    output_name = str(output_name)
    df = dots_df_gen(customer_num)
    output_name = output_name + '.csv'
    df.to_csv(output_name, index=False)
    print('number of customer: ', customer_num)
    print('file has been saved as: ', output_name)

if __name__ == '__main__':
    customer_num = input('please enter number of customers: ')
    output_name = input('please enter output file name (withouth .csv): ')
    main_fn(customer_num, output_name)
