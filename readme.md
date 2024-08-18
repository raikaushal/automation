# AUTOMATION SCRIPT

## _FOR https://epds.bihar.gov.in/_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Tech

This script uses a number of open source projects to work properly:

- [Python](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively
- [selenium](https://www.selenium.dev/) - awesome web-based text editor
- [pandas](https://pandas.pydata.org/) - Markdown parser done right. Fast and easy to extend.

## Installation

This requires [Python](https://www.python.org/downloads/) 3.8+ to run.

Install the dependencies and devDependencies and run the script.

#### Make sure to install selenium web driver if required on windows

```sh
cd automation
pip install -r requirements.txt
python main.py
```

## Dependencies

- Make sure to configure config.py (EXCEL_FILE_PATH, ORDER_FILE_PATH, NOTICE_FILE_PATH) according to your local system.
- Make sure to have all excel columns in string/text format.
- Make sure column name does not contain any leading or trailing spaces.
- change ENV variable in .env file to prod for actual deletion.
- Fill captcha within 10 seconds for moving ahead (don't click any other button , just fill captcha in textbox ).
- close the browser in case you want to stop the application or click ctrl + C on terminal.

## License

MIT

**Free Software!**
