# ShopAll-Ecommerce
An Ecommerce website which supports all features and payment integration with razorpay.

###Features 

- Profile:
    - Create new Profile
    - Activate account through link sent to mail
    - Add/Update Profile picture
    - Add Address/Phone number
    - View Previous Orders
    
- Items:
    - View items in a layout
    - View items from a search bar
    - Viweing items according to category selected
    
- Cart:
    - Add/remove items
    - Add/remove coupons
    - If user does not have an address, add new address before checkout
    - Razorpay payment integration
    - After payment order billing sent to the customer's registered email account

### Directory layout
```
.
├── accounts             # App that handles all the accounts related information including carts
├── base                 # Consists of helper files
├── ecommerce            # Project control file
├── home                 # App that handles all home page related information
├── media                # All the media files that are created is saved here(media root)
├── product              # App that handles all product specifications related information
├── static               # Static root of the project
├── templates            # Templates 
├── db.sqlite3
└── manage.py
```

### Main App layout
```
.                           .
├── ...                     ├── ...
├── accounts                ├── product   
│   ├── __pycache__         |   ├── __init__.py
│   ├── migrations          |   ├── urls.py
│   ├── __init__            |   ├── models.py
│   ├── tests.py            |   ├── views.py
|   ├── urls.py             |   |
|   ├── models.py           └── ...
|   ├── views.py         
│   └── ...                
└── ...
```
### Models layout

