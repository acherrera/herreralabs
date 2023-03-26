Title: Importance of Documentation
Date: 2023-0326
Tags: Programming, Management
Slug: importance-of-documentation
Author: Anthony Herrera
Summary: Thoughts on the importance of documentation

# Documentation

When I talk about documentation, I mean documentation in code such as docstrings and extra documentation
such as README files and higher level documentation. Documentation is often a scary word for some programmers.
There are a few reasons that this may be considered a problem. These include, documentation taking time,
documentation making you replaceable and finally, the code should be so readable that documentation isn't required.

## Roadblocks to Documentation

Let's go over some of the common issues that developers may have with creating documentation.

### Documentation Takes Time

Yes, documentation takes time. However, it doesn't usually take as much time as you think it does. More
importantly, even mediocre documentation can help other developers get up to speed much, much faster. Imagine
trying to figure out how a database is structured by looking at code or just seeing the tables that exist in a
database. The documentation of the database might take an hour to write down, but may save a person learning hours
of time AND save the person who knows the system hours of their time as well. Instead of having meetings and going
back and forth, the new developer can just read about the system.

Of course, the new developer might have questions after reading through the documentation, but the questions will
not be basic questions and instead will be more in-depth and insightful. At this point, the documentation can be
improved so these questions do not happen the next time around.

### Documentation Makes You Replaceable

Well, yes, this is technically true. If your documentation is good, it makes it so other people might be able to
come in and pick up the work you've been doing. However, the ability to have someone come in and pick up your code
is important for far more than just replacing the person who wrote it. Perhaps you move to a new company, end up in
a new position or have to onboard new employees. These are all good reasons why someone would make their code better
documented that are very positive.

It's been my experience that writing code that is valuable because you are the only one knows how to run it results
in being replaces with people who can work better with other programmers.

### Documentation Shouldn't Be Required

The idea here is that the code should be so well written that documentation is not required. This is interesting 
because your code _should_ be readable and well written. That is a prerequisite to writing good code not matter
what. Personally, I create docstraings for all my code. 

Example of what would be expected for docstrings is shown below:
```python
import os

def list_image_files(path: str)->list:
    """
    Returns a list of files for a given path which contains "png", "jpg", and "gif".
    Args:
        path: path to get lits of files from
    Returns: list of files
    """
    all_files =  os.listdir(path)

    valid = ["png", "jpg", "gif"]
    all_files = [i for i in all_files if i.split(".")[-1] in valid]

    return all_files
```

This makes the inputs and outputs of the functions very clear, but this doesn't answer the following questions:

* How to setup the environment
* How to run the codes
* What kind of inputs are expected to the code

These are the kind of items that should be documented and explained in the README file for the repo.

### Documentation Is Immediately Outdated



## What Needs Documented?

In short. Everything. Anything that someone might have a question about should be written down and documented.

## How Much Documentation is Enough?