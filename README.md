# price-database

A simple Python library and a CLI for storage of prices

The purpose of this project is to provide a storage and means of accessing a price database. It can be reused among multiple projects.

The goal is very simple: separate a storage of prices of various elements (commodities) from other applications or components.

The Price object has several properties:

- unique identifier = uniquely identifies each record for ease of accessing
- namespace = distinguishes the namespace for the symbol. Often the exchange name.
- symbol = security/commodity symbol that identifies it within the namespace (exchange).
- date = The date of the price
- time = The time of the price
- value = Value in currency
- currency identifier = identifier for the currency. Can be anything the remote system is using.

With these, it should be possible to store prices for commodities used in GnuCash, GnuCash Portfolio, Asset Allocation and other similar financial packages.