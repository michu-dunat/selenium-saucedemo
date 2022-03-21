from selenium import webdriver
from pickle import dump, load
from os.path import exists
from os import stat
from sys import argv


def iterate_through_dictionary(bigger_dictionary, lesser_dictionary):
    was_something_changed = False
    for key in bigger_dictionary:
        item_from_lesser_dictionary = lesser_dictionary.get(key)
        if item_from_lesser_dictionary is None or bigger_dictionary.get(key) != lesser_dictionary.get(key):
            was_something_changed = True
            print(f"{key} item was added/removed/changed.")

    if not was_something_changed:
        print('Nothing was changed.')


def scan_page():
    dictionary = {}

    inventory_items = driver.find_elements_by_class_name('inventory_item')
    for item in inventory_items:
        name = item.find_element_by_class_name('inventory_item_name').text
        price = item.find_element_by_class_name('inventory_item_price').text
        dictionary.update({name: price})

    return dictionary


def make_changes(number_of_items):
    element = driver.find_elements_by_class_name('inventory_item')[0].find_element_by_class_name('inventory_item_name')
    driver.execute_script("arguments[0].innerText = 'Nice jacket'", element)

    element = driver.find_elements_by_class_name('inventory_item')[number_of_items - 1].find_element_by_class_name(
        'inventory_item_price')
    driver.execute_script("arguments[0].innerText = '$999.99'", element)

    element = driver.find_elements_by_class_name('inventory_item')[number_of_items - 2]
    driver.execute_script("arguments[0].remove()", element)


file_name = 'items_names_and_prices.txt'


driver = webdriver.Firefox()

driver.get('https://www.saucedemo.com/')

username_field = driver.find_element_by_name('user-name')
username_field.clear()
username_field.send_keys('standard_user')

password_field = driver.find_element_by_name('password')
password_field.clear()
password_field.send_keys('secret_sauce')

submit_button = driver.find_element_by_name('login-button')
submit_button.submit()

item_dict = scan_page()

exists_or_not_empty = exists(file_name)
if exists_or_not_empty:
    if stat(file_name).st_size == 0:
        exists_or_not_empty = False
    else:
        exists_or_not_empty = True

if not exists_or_not_empty:
    print('Saving scan.')
    file = open(file_name, 'wb')
    dump(item_dict, file)
    file.close()
    driver.close()
    exit()

if len(argv) > 1:
    make_changes(len(item_dict))
    item_dict = scan_page()


file = open(file_name, 'rb')
loaded_info_dict = load(file)
file.close()

iterate_with_item_dict = False

if len(item_dict) > len(loaded_info_dict):
    iterate_with_item_dict = True
    print('There are more elements on the page than before.')
elif len(item_dict) == len(loaded_info_dict):
    print('The number of elements on the page is the same as before.')
else:
    print('There are less elements on the page than before.')

if iterate_with_item_dict:
    iterate_through_dictionary(item_dict, loaded_info_dict)
else:
    iterate_through_dictionary(loaded_info_dict, item_dict)

driver.close()
