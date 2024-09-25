# AutWhois
This is a python script to discover new registered domains via recursive whois requests.

You can get an updated file with the most common domain extensions on the official iana website:

https://data.iana.org/TLD/tlds-alpha-by-domain.txt

**Usage**:

```
python autwhois.py -h
usage: autwhois.py [-h] -n NAME -d DOMAINSLIST [-o OUTPUT] [-v]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Domain name to check (example: company name)
  -d DOMAINSLIST, --domainslist DOMAINSLIST
                        Path to list with domains extensions
  -o OUTPUT, --output OUTPUT
                        Print the result in a file
  -v, --verbose         Increase output verbosity and show Registry Domain ID

Example: 

python autwhois.py -n MyCompany -d domains_list.txt

python autwhois.py -n MyCompany -d domains_list.txt -o outfile.txt -v
```


**Result**:
```
python autwhois.py -n CompanyX -d domainsextensions.txt   
companyx.com
companyx.org
companyx.net

