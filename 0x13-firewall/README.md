# Hello Firewall

Hi, in this project we will configure our ufw firewall to allow certain types of connections and block others.

# Files
- **0-block_all_incoming_traffic_but**

## 0-block_all_incoming_traffic_but

Lets install the `ufw` firewall and setup a few rules on `web-01`.

### Requirements:

-   The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it wont be checked)
-   Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    -   `22` (SSH)
    -   `443` (HTTPS SSL)
    -   `80` (HTTP)
-   Share the `ufw` commands that you used in your answer file

## Building environment

These scripts were developed in:

-   Ubuntu 14.04
-   All files were tested in their compilation with `gcc 4.8.4` using the `-Wall` `-Werror` `-Wextra` and `-pedantic` flags.

## Authors
**Diego Fernando Ahumada Bocanegra** - [@XvariaDev](https://twitter.com/XvariaDev)

## Date-time
-   Holberton School
-   26/04/2021
-   Cohort #13