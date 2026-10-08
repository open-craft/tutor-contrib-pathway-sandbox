"""Build the pathway MFEs from the OpenCraft forks, and turn on the flag.

Tutor has no per-app MFE configuration: since Palm, tutor-mfe dropped the
``MFE_APP_*`` settings, and per-app sources are reachable only from a plugin,
through these two filters. That is also why this is a plugin and not a Grove PR
sandbox ``**Settings**`` block, which can only set config values.

Which of the two shapes an app uses decides the hook:

- ``FRONTEND_APPS`` -- frontend-base apps, bundled into the single site as npm
  workspace packages. Setting ``source`` makes the image clone that git URL at
  build time instead of installing the published package from npm.
- ``MFE_APPS`` -- legacy MFEs, each built on its own from a git repository.

So ``catalog`` and ``learner-dashboard`` take a ``source``, while ``learning``
(whose repository used to be called ``frontend-app-learner``) is still a legacy
MFE and takes ``repository`` + ``version``.

Refs are branches, not SHAs: a sandbox redeploy is triggered by a change to
this repository's requirements, so teammates can push without a commit here.
All three keep their package.json identical to upstream master at version
0.0.0-dev, which satisfies the ``^1.0.0-alpha || 0.0.0-dev`` range in
tutor-mfe's site package.json -- so the workspace links and tutor-mfe's
package-lock.json stay valid.
"""

from tutor import hooks
from tutormfe.hooks import FRONTEND_APPS, MFE_APPS

FRONTEND_APP_SOURCES = {
    "catalog": (
        "https://github.com/open-craft/frontend-app-catalog.git"
        "#rpenido/navin/fal-4380/pathway-detail-page"
    ),
    "learner-dashboard": (
        "https://github.com/open-craft/frontend-app-learner-dashboard.git"
        "#chris/pathway-updates"
    ),
}

LEGACY_MFE_SOURCES = {
    "learning": {
        "repository": "https://github.com/open-craft/frontend-app-learning.git",
        "version": "chris/fal-4397-course-pathway-strip",
    },
}


@FRONTEND_APPS.add()
def _use_pathway_frontend_app_forks(apps: dict) -> dict:
    # Apps tutor-mfe does not register are skipped: an operator can remove any
    # frontend app, and that must not break `tutor config save`.
    for app_name, source in FRONTEND_APP_SOURCES.items():
        if app_name in apps:
            apps[app_name]["source"] = source
    return apps


@MFE_APPS.add()
def _use_pathway_legacy_mfe_forks(mfes: dict) -> dict:
    # update(), not assignment: the Dockerfile and the dev-services template
    # read `port` too. An explicit version also wins over alternate_master.
    for app_name, source in LEGACY_MFE_SOURCES.items():
        if app_name in mfes:
            mfes[app_name].update(source)
    return mfes


# Both pipelines: `learning` reads MFE_CONFIG, while the two frontend-base apps
# read the site config served from /api/frontend_site_config/v1/. This patch is
# rendered after both dicts exist, in the development and production settings
# templates alike. The apps compare the value strictly (`=== true`), so it has
# to survive as a JSON boolean.
hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-lms-common-settings",
        'MFE_CONFIG["ENABLE_PATHWAY_PILOT_UI"] = True\n'
        'FRONTEND_SITE_CONFIG["commonAppConfig"]["ENABLE_PATHWAY_PILOT_UI"] = True',
    )
)
