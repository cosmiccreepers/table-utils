import os

class TableConverter:

    def __init__(self, file_path):
        self.file_path = file_path

    def to_HTML(self, output_location=None, headers=True, file_name_as_title = False):
        """Method for converting small-ish tables that can be held in memory, that are standard CSV format"""
        if output_location==None:
            output_location = os.path.join(os.getcwd(),'HTML')

        try:
            infile=open(self.file_path,"r")

            directory, file_name = os.path.split(self.file_path)
            file_name, ext = os.path.splitext(file_name)
            file_name += ".htm"
            
            if os.exists(os.path.join(output_location,file_name)):
                overwrite = input("The output file already exists, do you wish to overwrite? (y/n)")

                if overwrite.lower() == "n":
                   rename = input("Do you wish to choose another output file name? (y/n)")

                   if rename.lower() == "n":
                        print("File not created")
                        return
                   else:
                       file_name = input("Enter new output file name: ")
                       output_location, old_file_name = os.path.split(output_location)
                       self.to_HTML(output_location=os.path.join(output_location,file_name),headers=headers,file_name_as_title=file_name_as_title)
                       return
                       
        except FileNotFoundError as fnf_error:
            print(fnf_error)
        else:
            data = [line.split(',') for line in infile.readlines()]
            max_width = max([len(line) for line in data])
            
            outfile = open(output_location,"w")
            
            outfile.write("<table>\n")
            #maybe assume first line is headers for CSV read
            outfile.write("<th>\n")
            if headers==False:
                for i in range(0,len(max_width)):
                    outfile.write("<td> Column{} </td>\n".format(str(i)))
               
            else:
                for i in range(0,len(data[0])):
                    outfile.write("<td> Column{} </td>\n".format(str(i)))
                data = data[1:] #remove first row from data, as it's already been written
            
            outfile.write("</th>\n")


            #remember to clean out HTML tokens from data tables so they don't disrupt formating
            for line in data:
                outfile.write("<tr>\n")
                for col in line:
                    outfile.write("<td>{}</td>".format(col)) 

                outfile.write("</tr>\n")
            
            outfile.write("</table>")
            outfile.close()           
            return
        

if __name__ =='__main__':
    print('Hello World!')