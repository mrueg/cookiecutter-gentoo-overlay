# cookiecutter-gentoo-overlay
Create a Gentoo overlay using a [cookiecutter](https://cookiecutter.readthedocs.io) template

It will create the required metadata/layout.conf as well as profiles/repo_name.

Optionally it can provide a README.md and a [.travis.yml](https://github.com/mrueg/travis-repoman), that will run repoman via Travis CI.

## Usage

Install cookiecutter via
```
        emerge -av cookiecutter
```
or
```
        pip install cookiecutter
```
Run:
```
        cookiecutter https://github.com/mrueg/cookiecutter-gentoo-overlay
```

Answer:
```
        create_repoman_travis_cfg [y]:
        create_readme [y]:
        overlay_name [Your repository name]:
        aliases []:
        masters [gentoo]:
        eapis_banned [1]:
        eapis_deprecated [0 2 3 4]:
        sign_commits [true]:
        sign_manifests [true]:
        thin_manifests [true]:
        use_manifests [strict]:
        manifest_hashes [SHA256 SHA512 WHIRLPOOL]:
        update_changelog [false]:
        cache_formats [md5-dict]:
        profile_eapi_when_unspecified []:
        profile_formats [portage-2]:
```
