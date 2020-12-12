# 0x0F. Python - Object-relational mapping

# General

* Learning how to use the module MySQLdb to connect to a MySQL database and execute your SQL queries.  
* Learning how to use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).
* Learning how to connect to a MySQL database from a Python script
* Learning how to SELECT rows in a MySQL table from a Python script
* Learning how to INSERT rows in a MySQL table from a Python script
* Learning what ORM means
* Learning how to map a Python Class to a MySQL table

### [0-select_states.py](./0-select_states.py)
Script that lists all states from the database hbtn_0e_0_usa using the module MySQLdb (import MySQLdb).

### [1-filter_states.py](./1-filter_states.py)
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa using the module MySQLdb (import MySQLdb).

### [2-my_filter_states.py](./2-my_filter_states.py)
Script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument using the module MySQLdb (import MySQLdb).

### [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)
cript that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument using the module MySQLdb (import MySQLdb). But this time, write one that is safe from MySQL injections!

### [4-cities_by_state.py](./4-cities_by_state.py)
Script that lists all cities from the database hbtn_0e_4_usa using the module MySQLdb (import MySQLdb).

### [5-filter_cities.py](./5-filter_cities.py)
Script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa using the module MySQLdb (import MySQLdb).

### [model_state.py](./model_state.py)
Python file that contains the class definition of a State and an instance Base = declarative_base()) using the module SQLAlchemy.

### [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)
Script that lists all State objects from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)
Script that prints the first State object from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [9-model_state_filter_a.py](./9-model_state_filter_a.py)
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [10-model_state_my_get.py](./10-model_state_my_get.py)
Script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [11-model_state_insert.py](./11-model_state_insert.py)
Script that adds the State object “Louisiana” to the database hbtn_0e_6_usa using the module SQLAlchemy.

### [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)
Script that changes the name of a State object from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [13-model_state_delete_a.py](./13-model_state_delete_a.py)
Script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa using the module SQLAlchemy.

### [model_city.py](./model_city.py)
Python file similar to model_state.py named model_city.py that contains the class definition of a City.

### [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)
Script 14-model_city_fetch_by_state.py that prints all City objects from the database hbtn_0e_14_usa using the module SQLAlchemy.