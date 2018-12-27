# LogsAnalysis
Logs Analysis Project - the 3rd Udacity Full Stack Web Developer Nanodegree Project 

About
This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

Software Required
Python version 3
psycopg2 lib
Vagrant
VirtualBox

To Setup
Install Vagrant And VirtualBox
Download and unzip fsnd-virtual-machine.zip
cd to the director with Vagrantfile stored then run vagrant up at the shell promopt
Load the data, use the command psql -d news -f newsdata.sql to connect a database and run the necessary SQL statements.
The database includes three tables:
    Authors table
    Articles table
    Log table
Clone this repository

To Run
cd to the directory with Vagrantfile stored
Launch Vagrant VM by running vagrant up at shell prompt
Log in to Vagrant VM by running vagrant ssh at shell prompt
Run python LogsAnalysis.py from the VM command line.
