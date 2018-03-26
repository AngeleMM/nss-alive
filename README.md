*nss alive*
-----------

This is an ambitious project to project a wrapper layer on top of the
Armenian NSS data sources. We use Python to download all the data that
the NSS provides, clean it up and store it in our sqlite database,
then with that data we expose it to a beautiful front end with React,
d3.


Building
--------

# Setting up the project for first time

## Python

You'll need to have `Python` installed, we are using
`Python3`. Assuming you are on `Debian` based distribution, aka
`Debian` or `Ubuntu`, then you do:

```
$ sudo aptitude install python3-pip -y
```

Then I recommend you update `pip3` itself with `pip3 install --upgrade pip`

To install the `Python` requirements, you'll need to run `$ npm run
pyrequire`. If you look in the `requirements.txt` file you'll see two
pacakges, one is `requests`, we will use that for `HTTP` requests and
the other is `xlrd`, this is a package to read and handle `Excel`
files. 

## node

Now you need to have the `node` part of the project working, for that
just do

```shell
$ npm install
```

Developing
----------

# Linux

You'll need to have some system requirements, primarily for our
sqlite3 database. For this project you can version control a junk
database under `junk`, to make it easier for testing and debugging the
code when not in a production environment.

Get sqlite with `aptitude`, as always: `aptitude install sqlite`.

If you're working on the `JavaScript` part of the project, then you
need to open a shell and just run `npm run watch`, and that will:

1. Restart the server when there's a change in backend code. 
2. Recompile the front end code whenever there is a `JSX` change. 
3. Bundle the code up for the front end

# Responsibilties and Task

The project is divided into tasks that reflect the pipeline of the
whole application.

Roughly: 

## Python
1. Download the data from `ArmStat`/`NSS`.
2. Clean up the data for a format suitable for an insert query to our
   sqlite database.
3. Do this periodically, can do it as a cron job or systemd job, I
   prefer systemd.

## JavaScript

4. node now needs to provide a layer on top of this database. Use
   `express` to create a nice `REST` API. Keep in mind that this
   `REST` API must be well made insofar as that we want to have unique
   graphs created by the user be recreatable by URL. Use `React`
   router on the serverside for this, examples in silicondzor.
5. Front end `React` provides a skeletion as an application box,
   handling events, UX, etc.
6. `d3` add the great UI effect of graphs that tell a story and narrative.

# Dev Notes

## Tmp Database For Dev Envirenment

1. From `nss-live` directory run
    ```
    python3 scripts/cpanel.py
    ```
2. You will see the project cpanel, it should look like this `[iterate-hackerspace]>`, from there run  
    ```
    migrate_up
    migrate_down
    ```
to fill database with some data or to clear it