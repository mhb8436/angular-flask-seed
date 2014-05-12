# flask-angular-login-seed the seed for AngularJS apps using flask as backend 

This project is an application skeleton for a typical [AngularJS](http://angularjs.org/) web app 
and [flask] (http://flask.pocoo.org/)  as backend.

You can use it to quickly bootstrap your angular webapp projects and restful API service using 
flask. 

This seed has two directory. one is backend folder which contains all content to running RESTful
service with flask. And RESTful service use python default web server. 
other is frontend folder which contains all files to run SPA(Single Page Application) made by 
angularjs and bootstrap 2.3. This SPA also use web server made by node.js so that you should 
install node.js and grunt.js.

The seed contains AngularJS libraries, test libraries and a bunch of scripts all preconfigured for
instant web development gratification. Just clone the repository or download tar ball, start up
our (or yours) webserver and you are ready to develop and test your application.

This project use Python flask as backend restful API sevice.   This seed contains flask libraries 
you need to configuration restful API service including [http auth library](http://blog.miguelgrinberg.com/post/restful-authentication-with-flask).

This seed use sqlite3 as default database. If you want to change other database (like mysql), 
you can change easliy. you do change only one parameter SQLALCHEMY_DATABASE_URI in config.py.


## How to use angular-seed

Clone the angular-seed repository and start hacking...


### Running the app during development

You should follow guide.

1. You should move to backend directory and run `./run.sh` in command line.
2. After open another command line, move to frontend directory and then run `grunt` command.


Then navigate your browser to `http://localhost:<port>/` to see the app running in
your browser. 8888 is `<port>`'s default value.


### Running the app in production

This really depends on how complex is your app and the overall infrastructure of your system, but
the general rule is that all you need in production are all the files under the `/` directory.
Everything else should be omitted.

Angular apps are really just a bunch of static html, css and js files that just need to be hosted
somewhere, where they can be accessed by browsers.

If your Angular app is talking to the backend server via xhr or other means, you need to figure
out what is the best way to host the static files to comply with the same origin policy if
applicable. Usually this is done by hosting the files by the backend server or through
reverse-proxying the backend server(s) and a webserver(s).


### Running unit tests for RESTful API service



### Running unit tests for angularjs 



### Receiving updates from upstream

When we upgrade angular-seed's repo with newer angular or testing library code, you can just
fetch the changes and merge them into your project with git.


## Directory Layout

    backend/                 --> all of the files to be used in RESTful services
      server/                --> RESTful services app 
        main/                --> for main or index page RESTful services
          __init__.py        --> main module default py
          models.py          --> for main module models
          views.py           --> for main module view and controllers
        users/               --> for users or index page RESTful services
          __init__.py        --> users module default py
          models.py          --> for users module models
          views.py           --> for users module view and controllers

        auth.py              --> Http Authorization manipulation 
        data.py              --> Database CRUD and execution module files
        util.py              --> Utilization for this app 

      test/                  --> flask unit test directory
        test.sh              --> python -m unittest execution command file
        viewtest.py          --> unittest file for view

      base.py                --> base information of app's
      config.py              --> default directory and database setting directory
      run.py                 --> flask web service running app
      setup.sh               --> virtualenv install and python and library install command  

		frontend/ 
			app/                   --> all of the files to be used in production
        assets/              --> css and js files and bootstrap files
          bootstrap/         --> bootstrap js and css files
          vendor/            --> js files
        build/               --> builded js and css and minify files 
        js/                  --> javascript files
          config/            --> application router and configuration files
            config.js        --> configuration files
            routes.js        --> all routing information setting files of this app
          controllers/       --> directory for application controllers 
            controllers.js   --> application controllers
          directives/        --> directory for application directives
            directives.js    --> application directives
          lib/               --> directory for libraray files
            routers.js       --> convient method to manipulate router
          services/          --> directory for application services
            services.js      --> application services

          app.js             --> application

        template/            --> templates for angularjs
          partials/          --> angular view partials (partial html templates)
          views/             --> angular view (non partial templates)
          index.html         --> app layout file (the main html template file of the app)

      Gruntfile.js           --> Grunt setting file    




## Contact

For more information please send mail to me. (mhb8436@gmail.com)