# Difference Calculator

### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nik-NN/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Nik-NN/python-project-50/actions)
![Status](https://github.com/Nik-NN/python-project-50/actions/workflows/cheks.yml/badge.svg)
<a href="https://codeclimate.com/github/Nik-NN/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/606ae4e086acb5bfcbcf/maintainability" /></a>
<a href="https://codeclimate.com/github/Nik-NN/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/606ae4e086acb5bfcbcf/test_coverage" /></a>

## Getting Started

1. Clone the repo
   ```
   git clone https://github.com/Nik-NN/python-project-50.git
   ```
2. Install packages
   ```
   make package-install
   ```
## Requirements

Python (version 3.10)

Poetry (version 1.2.2)
   
## About The Project

The Difference Calculator is a program that determines the difference between two data structures.

### Features of the utility:

Support for different input formats: yaml, json

Report generation as plain text, stylish and json

## Example usage:

### Comparing attached files json (Stylish Format)
   ```
   gendiff filepath1.json filepath2.json
   ```
<h3 align="center"><a href="https://asciinema.org/a/gBDhaz37GhhTq5padjF1aqvME" target="_blank"><img src="https://asciinema.org/a/gBDhaz37GhhTq5padjF1aqvME.svg" /></a></h3>

### Comparing attached files yaml (Stylish Format)
   ```
   gendiff filepath1.yaml filepath2.yaml
   ```
<h3 align="center"><a href="https://asciinema.org/a/A9QDJqQqp1QEjrnQva8kCWdEo" target="_blank"><img src="https://asciinema.org/a/A9QDJqQqp1QEjrnQva8kCWdEo.svg" /></a></h3>

### Comparing attached files (Plain Format)
   ```
   gendiff --format plain filepath1.json filepath2.json
   ```
<h3 align="center"><a href="https://asciinema.org/a/IbL13ETIr8QbiDN8OrGxMv1xN" target="_blank"><img src="https://asciinema.org/a/IbL13ETIr8QbiDN8OrGxMv1xN.svg" /></a></h3>

### Comparing attached files (Json Format)
   ```
   gendiff --format json filepath1.json filepath2.json
   ```
<h3 align="center"><a href="https://asciinema.org/a/PG1qgR5oSG0dXh1YeF2bZMdXv" target="_blank"><img src="https://asciinema.org/a/PG1qgR5oSG0dXh1YeF2bZMdXv.svg" /></a></h3>
