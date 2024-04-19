# autwhois
This is a python script to discover new registered domains via recursive whois requests.

You can get an updated file with the most common domain extensions on the official iana website:

https://data.iana.org/TLD/tlds-alpha-by-domain.txt

**Example**:

`python autwhois.py -n MyCompany -d domains_list.txt`

`python autwhois.py -n MyCompany -d domains_list.txt -o outfile.txt -v`
