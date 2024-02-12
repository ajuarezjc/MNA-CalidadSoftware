"""
Compute Sales

This script processes information about products and sales from JSON files.

"""

import sys
import json
import time


def import_product_list(json_str):
    """
    Import product list from JSON string.

    json_str (str): JSON string containing product information.

    Returns: Dictionary containing product titles and prices.
             None if there is an error in decoding JSON.
    """
    try:
        data = json.loads(json_str)
        if isinstance(data, list):
            product_dict = {}
            for item in data:
                title = item['title']
                price = item['price']
                if title:
                    product_dict[title] = float(price)
            return product_dict
        print("No list received")
        return None
    except json.JSONDecodeError as decoder_error:
        print(f"Error decoding JSON: {decoder_error}")
        return None


def import_sales(json_str):
    """
    Import sales list from JSON string.

    json_str (str): JSON string containing sales information.

    Returns: List containing sales data.
             None if there is an error in decoding JSON.
    """
    try:
        data = json.loads(json_str)
        if isinstance(data, list):
            return data
        print("No list received")
        return None
    except json.JSONDecodeError as decoder_error:
        print(f"Error decoding JSON: {decoder_error}")
        return None


def calculate_total_sales(product_dict, sales_list):
    """
    Calculate the total sales amount.

    product_dict: Dictionary containing product titles and prices.
    sales_list: List containing sales data.

    Returns: Total sales amount.
    """
    total_sales = 0.0

    for sale in sales_list:
        product_name = sale.get('Product', '')
        quantity = sale.get('Quantity', 0)

        product_price = product_dict.get(product_name, 0.0)
        sale_amount = product_price * quantity

        total_sales += sale_amount

    return total_sales


def main():
    """
    Main function to execute the sales calculation.

    Reads product and sales data from JSON files
    Calculates total sales
    Writes results to "SalesResults.txt".
    """
    if len(sys.argv) != 3:
        print("Didn't find product_list or sales file")
        sys.exit(1)

    product_list_file = sys.argv[1]
    sales_list_file = sys.argv[2]

    start_time = time.time()

    with open(product_list_file, 'r', encoding='utf-8') as file:
        product_json = file.read()

    with open(sales_list_file, 'r', encoding='utf-8') as file:
        sales_json = file.read()

    product_dict = import_product_list(product_json)
    sales_list = import_sales(sales_json)

    if sales_list:
        total_sales = calculate_total_sales(product_dict, sales_list)
        str_total_sales = round(total_sales, 2)
        print(f"TOTAL FOR {sales_list_file}: {str_total_sales}")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Execution time: {elapsed_time} s")

        with open("SalesResults.txt", 'a', encoding='utf-8') as results_file:
            results_file.write(f"Results for file: {sales_list_file}\n")
            results_file.write(f"Sales total: {str_total_sales}\n")
            results_file.write(f"Execution time: {elapsed_time} s\n")
            results_file.write("\n\n")


if __name__ == "__main__":
    main()
