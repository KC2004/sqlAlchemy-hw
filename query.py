"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``? 
#
# flask_sqlalchemy.BaseQuery object





# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
#
# Association table manages two, many to many, tables. It 
# links those tables through foriegn keys. Association table 
# has a one to many relationship
# to the tables.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = "Brand.query.filter_by(brand_id='ram').all()"

# Get all models with the name "Corvette" and the brand_id "che."
q2 = "Model.query.filter(Model.name=='Corvette', Model.brand_id=='che').all()"

# Get all models that are older than 1960.
q3 = "Model.query.filter(Model.year < 1960).all()"

# Get all brands that were founded after 1920.
q4 = "Brand.query.filter(Brand.founded > 1920).all()"

# Get all models with names that begin with "Cor."
q5 = "Model.query.filter(Model.name.like('Cor%')).all()"

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = "Brand.query.filter(Brand.founded=='1903', Brand.discontinued==None).all()"

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = "Brand.query.filter((Brand.founded < '1950') | (Brand.discontinued!=None)).all()"

# Get any model whose brand_id is not "for."
q8 = "Model.query.filter(Model.brand_id!='for').all()"



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    car_list = db.session.query(Model.name, Brand.brand_id, Brand.name, Brand.headquarters).filter(Model.year==year).\
    join(Brand).all()

    for car in car_list:
        print "%s \t %s \t %s \t %s \n" % (car[0], car[1], car[2], car[3])


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""


    car_list = db.session.query(Brand.name, Model.name).filter(Model.year).join(Brand).all()


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_objs = Brand.query.filter(Brand.name.like('%mystr%')).all()

    return brand_objs

def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    cars_in_range = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return cars_in_range


