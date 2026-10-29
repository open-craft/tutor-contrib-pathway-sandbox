Pathway sandbox plugin for Tutor
================================

Builds three Open edX micro frontends from the OpenCraft pathway forks
instead of their published npm packages / upstream release branch.

The pathway work spans the catalog, the learner dashboard and the learning
(courseware) MFE, so no single MFE's own PR sandbox exercises it.

========================= =========================== ==============================
App                       Built by tutor-mfe as       Overridden to
========================= =========================== ==============================
``catalog``               frontend-base app            ``source``
``learner-dashboard``     frontend-base app            ``source``
``learning``              legacy MFE                  ``repository`` + ``version``
========================= =========================== ==============================

Refs in use:

- ``open-craft/frontend-app-catalog`` ``rpenido/fal-4374/slot-docs`` (tip of the #174 to #178 stack)
- ``open-craft/frontend-app-learner-dashboard`` ``chris/unenroll-pathways-warning`` (tip of the #879 to #881 stack)
- ``open-craft/frontend-app-learning`` ``chris/fal-4398-pathway-progress-page`` (tip of the #2159, #2231 to #2233 stack)


Installation
------------

.. code-block:: bash

    tutor plugins install pathway_sandbox
    tutor config save
    tutor images build mfe

``tutor images build mfe`` is required: giving a frontend app a ``source``, or
repointing a legacy MFE, changes the image build -- unlike toggling an app on
or off.


License
-------

The code in this repository is licensed under the AGPLv3 unless otherwise
noted. Please see `LICENSE.txt`_ for details.

.. _LICENSE.txt: https://github.com/open-craft/tutor-contrib-pathway-sandbox/blob/main/LICENSE.txt
