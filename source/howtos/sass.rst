Stylistically Awesome Styling Sheets
====================================

What is SASS?
-------------
Formally, Sass is a scripting language that is interpreted into CSS.  More casually, it's an extension of CSS which includes pre-processing directives, variables, inheritance, mixins, nesting, and a few other nifty things.  You do not need to know sass in order to edit a .scss file, but it's a pretty cool tool to learn and use!

To install:
-----------
.. code-block:: bash
	
	gem install sass

Compass:
--------------
Compass is an `"open-source CSS Authoring Framework"`__.  It's the tool we use to interpret our Sass files and generate CSS from them.  In order to use it, your file structure should look something like this:

::
	css
	├── sass
	│   ├── normalize.scss
	│   ├── _settings.scss
	│   └── style.scss
	├── screen.css
	└── style.css

What's most important about the files is that there is a parent directory which will hold both sass and css files and a sass directory to hold your sass files within that parent directory.  

To use Compass:
---------------
1. Install_ Compass by running
.. code-block:: bash

	gem update --system
	gem install compass

Once you've got it installed, run gem list to make sure it was installed correctly.  Make sure that sass is in there as well!

2. Open up style.scss in your sass directory, make some edits, and save the file.

3. Once you've made all your changes, cd to the parent directory (which will have your style.css file in it) and run 
.. code-block:: bash

	compass watch

4. Now you're done!  Another easy way to have Compass watch for changes is to have it running in a separate terminal while you edit your style.scss file.

.. _Compass: http://compass-style.org/reference/compass/
__ Compass_
.. _Install: http://compass-style.org/install/


What's up with the imports and extends in style.scss for the OSL site?
----------------------------------------------------------------------
@import_ is also a feature of CSS, and in sass allows you to import other scss files.  We are also using a tool called Foundation_ which has some components and settings that we are importing, which is why there's so many imports.  Similarly, @extend_ is used in conjunction with Foundation to denote which size of block should be used for that element. 

Resources:
----------
Where should you go to learn some Sass? 

* sass-lang.com_
* thesassway.com_
* codeschool.com_
* css-tricks.com_

And several others!  Google around until you find one that you like.

.. _import: http://sass-lang.com/documentation/file.SASS_REFERENCE.html#import
.. _extend: http://sass-lang.com/documentation/file.SASS_REFERENCE.html#extend
.. _Foundation: http://foundation.zurb.com/docs/
.. _sass-lang.com: http://sass-lang.com/documentation/file.SASS_REFERENCE.html
.. _thesassway.com: http://thesassway.com/beginner
.. _codeschool.com: https://www.codeschool.com/courses/assembling-sass
.. _css-tricks.com: http://css-tricks.com/video-screencasts/88-intro-to-compass-sass/

