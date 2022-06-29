# ShopAll-Ecommerce
An Ecommerce website which supports all features and payment integration with razorpay

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

### Models layout

