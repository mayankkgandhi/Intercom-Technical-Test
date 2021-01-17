# Intercom-Technical-Test

## 1 - TECHNICAL CHALLENGE

## Tast

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

## Solution

The code is built to work with diffrent configuration files, just by changing values in the config.json file or giving a different config file.
The main function take in config file as an argument and outputs an Inivite List based on customer's location.

### Installation

```
pip3 install requirements.txt
```

### Usage

To run the program:

```
python3 src/main.py config/config.json
```

On success 'output.txt' file will be created with all customers within 100KM from Intercom's Dublin office. Result is saved in 'output/output.txt'.

### Test

To run all unit tests:

```
pytest -v 
```

All tests should pass.

To check the Test-cases Coverage, run:

```
pytest --cov=tests 
```

## 2 - PROUDEST ACHIVEMENT

Situation: I took over the responsibility of building the "Food Ordering Messenger Chatbot" product from scratch within one month of joining as my CTO resigned in the initial days of my employment, citing health reasons. I was assigned to design and to build the core product by the CEO. Since it was the primary product, there was tremendous pressure as our clientele and revenue depended on this product.

Behaviour: This was a challenging task and had a steep learning curve as I had fairly little idea about chatbots. I collaborated with initial clients to define contracts, gather their requirements and expectations, and promised three months of delivery.  I established a project plan with the CEO for multiple milestones, including a product launch date.

Impact: I delivered the messenger bot on time and increased our clientele from 2 clients to 14 clients within six months of product launch with an increase in revenue by 35%.
I'm most proud of this product because it was a vital win for the Start-up, and this project helped me grow tremendously in terms of leadership and technical skills.
