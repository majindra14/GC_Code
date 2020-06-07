from sys import argv
import xlsxwriter
import os

rootdir ='C:\\Users\\Baopa\\Documents\\Pfleger_Lab\\GC_Data\\February_2020\\MAJ_2_8_2020'
row = 0
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('GCData.xlsx')
worksheet = workbook.add_worksheet()

def ExcelWrite(file,row):
    in_file = open(file)

    col = 0
    flag=False


    # This block looks for the sample name and writes it to a new row in a spreadsheet
    for line in in_file:
        columns=line.split()
        if len(columns)==3 or len(columns)==4: # The or statement is in case someone names the file with a space, making len(columns) = 4
            if columns[0]=='Sample' and columns[1]=='Name':
                if len(columns)<4:
                    worksheet.write(row, col, columns[2])
                else:
                    worksheet.write(row, col, columns[2]+columns[3])

        # This block looks for the peak areas and retention times
        if len(columns)>1:
            if columns[0]=='Peak#':
                flag=True

        if flag==True:
            if len(columns)>1:
                row = row+1
                #print(line)
                #I understand everything until this part
                for col in range(6):
                    try:
                        worksheet.write(row, col, float(columns[col]))
                    except ValueError:
                        worksheet.write(row, col, columns[col])
            else:
                break


    return row+2

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        x = file.split('.')
        if x[1].upper() == 'TXT':
            row=ExcelWrite(file,row)

workbook.close()
'''
indata = in_file.readlines()
data = [line for line in indata if 'S' in line[0] and 'e' in line[10]]

print(data)


#print(f"Does the output file exist? {exists(to_file)}")
print("ready?")
input()

out_file = open(to_file, 'w')
out_file.writelines(data)


out_file.close()
in_file.close()

outfile = open(to_file)
print(outfile.read())
'''
