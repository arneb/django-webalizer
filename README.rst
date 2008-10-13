=====================================================================
A Django app for embedding Webalizer reports into the admin interface
=====================================================================

`django-webalizer`_ is a **very simple** app which let's developers embed
`Webalizer`_ statistics into the admin interface of a django project.

From the Webalizer Webpage:

    The Webalizer is a fast, free web server log file analysis program. It
    produces highly detailed, easily configurable usage reports in HTML
    format, for viewing with a standard web browser.


Install Instructions
---------------------

Just add the webalizer directory to your Python-Path. Add 'webalizer' to
settings.INSTALLED_APPS and add an entry similar to the following one, to 
your url-conf (before the include admin.site.root entry):

    url(r'^admin/webalizer/', include('webalizer.urls')),

django-webalizer requires the following third-party packages to be installed:

  * `BeautifulSoup`_ - just run: easy_install BeautifulSoup 
  
Additionally in your settings.py set the variable `WEBALIZER_DIR` to the
path to the directory where webalizer outputs the generated statistics.  

.. _`django-webalizer` : http://github.com/arneb/django-webalizer/
.. _`Webalizer` : http://www.webalizer.org/
.. _`BeautifulSoup` : http://www.crummy.com/software/BeautifulSoup/