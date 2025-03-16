Piscine DataScience is a 42's project that aims to introduce us to data science's libraries and machine learning in Python.
In this project we use : Python and SQL.

There is 2 parts in this projects :
- The first one being python_0_starting, python_x_.... that gives us exercices to learn the differents libraries used in datascience like pandas, matplotlib and some concepts like Object-Oriented Programming.
- The second is an application of what we learned in the first part. (sklearn for machine learning)

### To run the project:

You need Python 3.12, Jupyter Notebook and Docker. 
Each day are different "project" of their own.

All the days use a Docker. So you can do as follow:
```bash
git clone https://github.com/Atroooo/Piscine_DataScience.git
cd Piscine_DataScience

python3 -m venv venv
source venv/bin/activate

cd datascience_0
pip install -r requirements.txt
cd ex00
docker compose up
```

When docker is up you can just move in each projects and run:
```bash
cd project
cd exercice
python ex.py
```


