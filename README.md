# 0x00. AirBnB clone - The console

This task was done in teams of 2 :

The goal of the project is to deploy on your server a simple copy of the [AirBnB website.](https://intranet.alxswe.com/rltoken/m8g02HcD2ovrl_K-zulYBw)

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, we will have a complete web application composed by:

    A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
    
    A website (the front-end) that shows the final product to everybody: static and dynamic
    
    A database or files that store data (data = objects)
    
    An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## Final product

![Alt text](hbnb_screenshot.png)


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

![Alt text](<Screenshot from 2023-11-12 14-26-53.png>)


## The Web Static

    >learn HTML/CSS

    >create the HTML of your application

    >create template of each object


## MySQL storage

    >replace the file storage by a Database storage

    >map our models to a table in database by using an O.R.M.


## Web framework - templating
    >create our first web server in Python

    >make our static HTML file dynamic by using objects stored in a file or database

## RESTful API

    >expose all your objects stored via a JSON web interface

    >manipulate your objects via a RESTful API


## Web dynamic
    >learn JQuery

    >load objects from the client side by using your own RESTful API

![Alt text](<Screenshot from 2023-11-12 14-21-58.png>)


# Command Interpreter



# Contributors

[Kiptoo Caleb](https://github.com/kiptoobarchok)

[Victor Ndudim](https://github.com/Pa-vic)