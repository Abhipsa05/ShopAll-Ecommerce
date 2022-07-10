# ShopAll-Ecommerce
*	Built a full-stack e-commerce site with fully-fledged database to store users, products and order information, reviews, and comments with user authentication.
*	Incorporated functionalities like filter orders by name and category. Users can view products, add and delete products from their cart, give ratings and reviews, see past orders.
*	Created an Admin panel in which Admin can view, add, remove and update products and users.
*	Created a mailing system for email authentication and sending customer invoice of their purchase.
*	Implemented payment gateway for placing orders using Razorpay.


### Tech Stacks Used


### Features

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
```
.        
├── accounts           
│   ├── Profile
|   |   |--
│   ├── migrations      
│   ├── __init__          
│   ├── tests.py         
|   ├── urls.py             
|   ├── models.py           
└── ...
```
Snippets of pages of the website
![Screenshot (5168)](https://user-images.githubusercontent.com/79036782/178137552-ef405860-e01e-4d0c-b213-0a8d501250c6.png)
![Screenshot (5182)](https://user-images.githubusercontent.com/79036782/178137527-56202640-12a9-460e-853e-6a83257faabd.png)
![Screenshot (5177)](https://user-images.githubusercontent.com/79036782/178137536-4fa7b596-bdbd-4bc8-9454-efc218cf90a8.png)
![Screenshot (5179)](https://user-images.githubusercontent.com/79036782/178137542-4bd19862-08c0-4406-ba47-1394ba9f0f90.png)
![Screenshot (5178)](https://user-images.githubusercontent.com/79036782/178137545-d6555e0d-6a4c-477d-b74e-7d0059be39d0.png)
![Screenshot (5171)](https://user-images.githubusercontent.com/79036782/178137559-d71758eb-d48f-4b9c-83b5-124d7bbd6ae2.png)
![Screenshot (5173)](https://user-images.githubusercontent.com/79036782/178137562-a35fdd8d-fcf8-4f4b-acc4-7739f2bf30e8.png)
![Screenshot (5175)](https://user-images.githubusercontent.com/79036782/178137565-d26cba41-7b7e-42d7-b998-b662606dc78c.png)
![Screenshot (5172)](https://user-images.githubusercontent.com/79036782/178137581-dc941cbf-29a8-4f15-9607-27a044b4ce5f.png)



