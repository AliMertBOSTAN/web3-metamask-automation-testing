**Anaconda installation**

  

Download the latest anaconda version from [here](https://www.anaconda.com/download) and follow the steps for installation.

  

**Creating a virtual environment**

  

- Create a new environment with Python 3.11.5 version from the

environments tab in Anaconda.

-  `conda activate myenv `

Replace `myenv` with the environment name or directory path

  

**Running web3 automation test**

  

Follow the steps in order

-  ` pip install requirement.txt`

-  `playwright install`

- For testing, you need to enter your own metamask extension file address. Don't be afraid, this address contains only the necessary extension files, it does not use any of your data.

-  `pytest test.py`

- In the first test run, you need to create a wallet manually, so proceed by following the options to create a new wallet on the metamask screen that appears in the first step.

- Change the password you created from within the .env file

- To run your tests in headed mode use the `--headed` flag. This will open up a browser window while running your tests.

`pytest test.py --headed`

- To run specific test use the `--k` flag

`pytest
test.py -k test_CrocSwap_172_SwapTransaction --headed`

- To generate html report for test use the `--html=report.html` flag.

but do not forget to install the reporter first using pip: pip

install pytest-reporter-html1   

`pytest test.py -k
test_CrocSwap_172_SwapTransaction --headed --html=report.html`

  

**This automation corresponds to the following operations**

test_CrocSwap_200_SwapTradePage:

Manuel test steps:

  

1. the Trade Page opens -- It is seen that the system displays the trade page.

  

2. Under the Swap tab which is selected on the Trade page, the token pair and amounts to be traded are entered.

  

3. Confirm Button is clicked -- swap confirmation popup is displayed

  

4. "Submit Swap" Button is clicked -- Wallet browser extention is opened

  

5. Click the "Confirm" button in the wallet browser extension that opens. -- it is seen that the system displays "Transaction Submitted" in the Swap Confirmation window

  

test_CrocSwap_205_LimitTradePage

Manuel test steps:

  

1. The Trade page opens. -- It is seen that the system displays the trade page.

  

2. Click on the limit option on the right side of the Trade page. -- It is seen that the system displays the limit option.

  

3. On the Trade page, the token to be traded is selected, the amount is entered. --

  

4. Confirm Button is clicked -- limit confirmation popup is displayed

  

5. "Submit Limit" Button is clicked -- Wallet browser extention is opened

  

6. Click the "Confirm" button in the wallet browser extension that opens. -- it is seen that the system displays "Transaction Submitted" in the limit Confirmation window