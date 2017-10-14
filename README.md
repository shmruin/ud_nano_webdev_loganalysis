# Introduction
This python file provides the answer below by postgreSQL in `newsdata.sql`.

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

# Files

* `newsdata.sql` - data source for queries
* `newsdata.py` - including queries to solve the problems above
* `log_analysis_result.PNG` - captured screen of the result which is executed in developer's computer

# Environment

* `newsdata.py` is written in `Python3`
* `newsdata.py` was tested in `window 10`, `git bash`, `vagrant(ubuntu)` environment
* Requires `postgreSQL`

# How to run this program

* First, run `git bash` in window
* Go to `vagrant` folder where you install it in `git bash`
* In `vagrant` folder, put `newsdata.py` and `newsdata.sql`
* Run `vagrant` by `vagrant up` `vagrant ssh` and `cd vagrant` to share the folder
* Make database by `psql -d news -f newsdata.sql`. Make sure you have `postgreSQL`
* Run `python3 newsdata.py`. Make sure you already install `python3`
* The result of the questions is shown by python dictionary format in `git bash`

