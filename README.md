# 0x00. AirBnB clone - The console

This task was done in teams of 2 :

[Caleb](https://github.com/kiptoobarchok) and [Victor Ndudim]()

The goal of the project is to deploy on your server a simple copy of the [AirBnB website.](https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw)

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

    A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    
    A website (the front-end) that shows the final product to everybody: static and dynamic
    
    A database or files that store data (data = objects)
    
    An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## Final product

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253Df30ebb3a4fb5fb52b48b8de0c9f9c5e913abe75a0bc85a5c7979021e03a4f167)


![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253Dd8b78dc50896cd60070c08c248732a8d67f7a8a9c45b5eb39be2851517524c83)


# Concepts to learn

>[Unittest](https://intranet.alxswe.com/rltoken/87ml5W9WzLbH7yAJuGk_mA) 

>Python packages concept page

>Serialization/Deserialization

>*args, **kwargs

>datetime


# Steps

We won’t build this application all at once, but step by step.

Each step will link to a concept:

## The Console
    >create data model
    
    >manage (create, update, destroy, etc) objects via a console / command interpreter
    
    >store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI (which we will build later)

This abstraction will also allow us to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D453399e4e1fb17e093852d4fbea5be60e5c5c1eb400852561683d274e4d8eed6)


## The Web Static

    >learn HTML/CSS

    >create the HTML of your application

    >create template of each object

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D1156337be697ba621f41cc0746723fda19c7338ee27213fae00a98282ab891b7)

## MySQL storage

    >replace the file storage by a Database storage

    >map our models to a table in database by using an O.R.M.


## Web framework - templating
    >create our first web server in Python

    >make our static HTML file dynamic by using objects stored in a file or database

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253D377f860a3fb771449c53d64c66d78bb6c0549fca6eaa26c88a7af4259e75148d)

## RESTful API

    >expose all your objects stored via a JSON web interface

    >manipulate your objects via a RESTful API

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253Db7c643eae6628848cc75629587f473b00b134e842a55ef35b99b6a9fa38eabbf)


## Web dynamic
    >learn JQuery

    >load objects from the client side by using your own RESTful API

![Alt text](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm%253DAWS4-HMAC-SHA256%2526X-Amz-Credential%253DAKIARDDGGGOUSBVO6H7D%252F20231109%252Fus-east-1%252Fs3%252Faws4_request%2526X-Amz-Date%253D20231109T174244Z%2526X-Amz-Expires%253D86400%2526X-Amz-SignedHeaders%253Dhost%2526X-Amz-Signature%253Dbef20efcc0bed622777f08e23a4e48a6ec104b80815a0d51840f14dd7e57803c)


# Command Interpreter

