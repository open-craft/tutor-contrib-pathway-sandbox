Pathway sandbox plugin for Tutor
================================

Builds three Open edX micro frontends from the OpenCraft pathway forks
instead of their published npm packages / upstream release branch, and turns on
the flag that reveals the pathway UI.

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

- ``open-craft/frontend-app-catalog`` ``rpenido/navin/fal-4380/pathway-detail-page``
- ``open-craft/frontend-app-learner-dashboard`` ``chris/pathway-updates``
- ``open-craft/frontend-app-learning`` ``chris/fal-4397-course-pathway-strip``

It also adds to ``mfe-lms-common-settings``::

    MFE_CONFIG["ENABLE_PATHWAY_PILOT_UI"] = True
    FRONTEND_SITE_CONFIG["commonAppConfig"]["ENABLE_PATHWAY_PILOT_UI"] = True

Both are needed: ``learning`` reads ``MFE_CONFIG``, while the two frontend-base
apps read the site config served from ``/api/frontend_site_config/v1/``.


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
