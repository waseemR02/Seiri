---
toc_depth: 1
---
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

[Click here to see the unreleased changes.](https://github.com/waseemr02/seiri/compare/v1.2.0...HEAD)

<!-- ### Fixed
### Changed
### Removed
### Added -->

## [1.2.0] - 2024-02-29

### Added
- Build seiri as a module with hachling and added it to the package [#1]
- Add coverage badge [#2]
- Add mkdocs to the project and deploy it to github pages [#2]

### Changed
- Coverage results are now deployed to codacy instead of github-pages [#1] and can be found [here](https://app.codacy.com/gh/waseemR02/seiri/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)


## [1.0.0] - 2024-02-26

### Added

- Seiri is an automation tool for handling csv<->xlsx transforms and validating against a specific set of rules
- It is made to be cross-platform package instead of a script for better adoption to GUI
- Tests were added under tests/ and it uses `pytest` which check the package against given csv and xlsx files to check if they are working as intended
- Coverage results are deployed at every push to static page and can be checked in [here](https://waseemr02.github.io/seiri)

[1.2.0]: https://github.com/waseemr02/seiri/releases/tag/v1.2.0
[1.0.0]: https://github.com/waseemr02/seiri/releases/tag/v1.0.0
