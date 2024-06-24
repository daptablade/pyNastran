# PyNastran fork

This repository is a fork of [pyNastran](https://github.com/SteveDoyle2/pyNastran).

We use this fork to rapidly fix bugs when we need it, in particular in the
mascots_wp3_2 repository.

## Motivation

We encountered some bugs which crippled performance and functionality when using
pyNastran in the development of RTS optimisation. The simplest way to fix those
was to take a fork and fix those bugs.

## Development History

There are
[3 commits and 2 prs](https://github.com/daptablade/pyNastran/pulls?q=is%3Apr+is%3Aclosed)
The way I've used this repository is to push and merge to the `develop-1.3`
as the equivalent of our `develop` branch in most of our repositories. This is a
live working version.

The way I develop on this is to make pull requests on the `develop-1.3` branch.

## Limitations

- We have not run their test suite on our new changes

## Assumptions

- Other packages which need this need to track the correct branch.

## Lessons Learnt

N/A

## Development Roadmap

There is no short term plan for these things to happen but they are desirable.

- Run the test suite.
- Add tests for the bugs we fixed.
- Submit those bug fixes to the parent repository.

### Current Status

It does what we need it to, but it is not tested.

### Future Development

Ideally we should PR this back to the original repository to contribute.
