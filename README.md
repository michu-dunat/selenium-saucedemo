# Selenium WebDriver

## Installation (Windows, Mozilla Firefox)
Latest geckodriver version: https://github.com/mozilla/geckodriver/releases.
This driver is needed for WebDriver to work with the Mozilla Firefox browser.

I installed WebDriver in a virtual environment using the command:
```python
pip install -U selenium
```

## Testing https://www.saucedemo.com/.

The test logs into the application. It then retrieves the list of items displayed on the page. 
If this has not been done before, it writes this list to a file. 
Otherwise it reads list of items from the file and compares whether the items on the page have been modified in terms of name and price. 
Any changes are displayed in the console window.

Provide any argument in the console when running script to enable simulation of the list.

Version without simulation:

```python
python main.py
```

With simulation

```python
python main.py 1
```
The simulated changes consist of: renaming the first item, changing the price of the last item and deleting one object before the last object.