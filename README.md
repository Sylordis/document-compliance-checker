
# Documentation Compliance Checker

This program checks the compliance of a list of documents, producing a report for them.

## Installation

Just download/clone the folder on your machine.

## Requirements

You will need Python 3.10 (or more recent) in order to run this software.
Once python is installed, you can run `pip` to install the requirements depicted in the `requirements.txt` file.

```
pip install -r requirements.txt
```

Running it once should be enough, and from time to time regarding library updates.

## Usage

`py doc_compl_check.py <srcfile> <targetfile>`

## Development

- Implement or reuse existing document types in/from `lib/documents`, for simple DAO.
- Implement or reuse ingester according to your document type in/from `lib/ingesters` to import documents in the software.
- Implement or reuse strategy in `lib/strategies` to configure the strategies you desire for checking the compliance.
  - Implement or reuse criteria for this `lib/criteria`.
- Implement or reuse exporter in order to create the final report `lib/exporters`.

## Authors & Questions

- [Sylvain Domenjoud](s.domenjoud@cgi.com)

## License

This project is licensed under the Apache License v2 - see the LICENSE file for details

## Links

Project website: https://github.com/sylordis/doc_compliance_check