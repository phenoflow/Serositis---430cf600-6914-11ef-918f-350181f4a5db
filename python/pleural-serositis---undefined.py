# phekb, 2024.

import sys, csv, re

codes = [{"code":"786.52","system":"ICD9 Diagnosis"},{"code":"786.7","system":"ICD9 Diagnosis"},{"code":"R07.1","system":"ICD9 Diagnosis"},{"code":"R07.81","system":"ICD9 Diagnosis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('serositis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pleural-serositis---undefined-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pleural-serositis---undefined-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pleural-serositis---undefined-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
