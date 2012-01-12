Introduction
------------
This directory contains files for ``webapp`` written in Django. This file will host Django related FAQs in future. For newbie's this page is kind of cheatsheet.



To setup a ``webapp`` project run the following command::

    $ django-admin.py startproject webapp

This will create 4 files in the ``PWD``.

1. __init__.py: An empty file that tells Python that this directory should be considered a Python package. (Read `more about packages <http://docs.python.org/tutorial/modules.html#packages>`_; in the official Python docs if you're a Python beginner.)

#. manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in `django-admin.py and manage.py <https://docs.djangoproject.com/en/1.3/ref/django-admin/>`_;.

#. settings.py: Settings/configuration for this Django project. `Django settings <https://docs.djangoproject.com/en/1.3/topics/settings/>`_; will tell you all about how settings work.

#. urls.py: The URL declarations for this Django project; a "table of contents" of your Django-powered site. You can read more about URLs in `URL dispatcher <https://docs.djangoproject.com/en/1.3/topics/http/urls/>`_;.
