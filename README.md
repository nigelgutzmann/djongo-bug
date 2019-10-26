# Demo
https://www.loom.com/share/6e04c71a21fb45438f0de9a46a255264

You can see in the demo, errors are happening randomly, in no particular order, and inconsistenly.

# Models Explanation
The django project has a single app: myapp
The app has 3 models: a `Planet`, a `SolarSystem` and a `Universe`. The Foreign Keys work as follows:

```
Planet --> SolarSystem --> Universe
```

See `models.py` for the full details

# Running the app
Just run the app with `python manage.py runserver` and a mongodb instance running on your localhost.

In your browser, navigate to http://localhost:8000, you will see the page in the demo. The browser loads the page, then sends 20 identical API requests to load data and display it on the screen. 

There are 2 buttons to add in some data (add in a planet, with the corresponding solar system and universe). Once a planet has been created, clicking the button again doesn't do anything. The following data is possible to create:

```
Planets: 
    - earth
    - mars
Solar System:
    - milky way
Universe: 
    - Laniakea
```

Once an object has been created, it will be re-used (no duplicates will be created).

# Replicating the bug
Load the page a couple times, you'll see that it works well. Then click one of the buttons to add some data and refresh the page a couple times. You should see it start to print errors, and you should see the errors shown in the console output in the demo video as well. If you click the other button to add another planet, you will see the errors are more likely.