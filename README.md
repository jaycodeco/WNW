# <span style="color:red;" > What </span> <span style="color:green;" > New </span> <span style="color:blue;" > World </span>

A simple bot which scrapes CNN and BBC for fresh news every \
15min, then send it to a contact in a contact list through whatsapp.

It is build using <b>Selenium</b> and <b>BeautifulSoup</b>. For sure it is not yet \
fitted for deployment a, as it needs to further integrated some \
multiprocessing and chron job functionalities.

## <span style="color:red;" > getting started </span>
to start:
> pip install selenium BeautifulSoup lxml



head to app.py and provide the path to your chrome driver
> self.driver = webdriver.Chrome(executable_path= YOUR_PATH , options=options)



run the app.py and scan the Qr code form whatsapp nmber you want \
to use. leave the application to run and watch it every repeating \
sthe process every 15 minutes 



## <span style="color:red;" > adding contacts </span>
just create a contacts.txt file and add your contacts name as in your whatsapp cont.


## <span style="color:red;" > Avoid continuous Qr code scanning </span>
to avoid continuously scannin the Qr code, find the "User Data" from \
Chrome and enter the "Default" and copy the full path to "Default"(CRED_PATH).\
Then add the following code to the __init__ method of the bot\
class:

```python
options.add_argument('--disable-notifications')
options.add_argument('--user-data-dir = CRED_PATH')
options.add_argument('--profile-directory = Default')
```

