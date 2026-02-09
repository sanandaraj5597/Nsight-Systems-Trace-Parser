Pre-req is to have 'csv' package installed.

This script separates the CPU overhead and exposed kernel run-times and prints them separately. There's a runtime from profile which also gets printed to verify the parsing.

To run this script, add the absolute path of the Nsys trace CSV that you generated, also please remove the first title line from the CSV. The script doesn't detect that.

Code is experimental, expect bugs/issues.
