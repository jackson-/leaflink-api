# Backend Engineer Home Exercise

We've designed this exercise in order to measure your ability to structure, write, organize, and deliver a small API service.

We're mainly interested in the way you think through codebases like this and approach solutions to problems. Please note that some of these instructions are intentionally vague so that you can make choices that you think are best suited to the problem at hand. We'll use our time in-person to dive into some of those choices, so please make sure to think things through!

## Exercise Description

LeafLink is a B2B e-commerce company that facilitates relationships between buyers and sellers. Our core product is a marketplace that consists of a few data models and relationships. We'd like you to design an API that models out these relationships and presents standard RESTful endpoints to interact with those models and relationships.

### Data Models

* `Company` - The buyers and sellers of the marketplace
* `Product` - An item that a Company sells, and another Company buys
* `Order` - A contract made when a Company agrees to buy `N` amount of Product(s) from another Company

### Data Relationships

* A company can be **either** a "buyer" or a "seller" - but not both
* An Order is between two Companies, one buyer and one seller
* An Order consists of one or more Products, with each "line item" having a quantity and unit price
* A Product is sold by one Company and can be in many Orders

## Deliverables

The following requirements / guidelines should be kept in mind when developing the application.

* A runnable (preferably Python) project that exposes a RESTful API for the above models a relationships
* Documentation on how to install, run, and interact with your application
* Data modeling that reflects the above relationships and makes reasonable assumptions about fields and data types
* Clean, predictable URL routing
* Ability to list collections of all data models
* Ability to query a specific resource from all data models
* Ability to create all data models

Nice to haves:

* Reasonable test coverage
* Minimal system dependencies needed to get up and running
* Dockerized packaging of the application

Please submit your code as a `.zip` archive with all necessary files and instructions needed to run and interact with your application locally.
