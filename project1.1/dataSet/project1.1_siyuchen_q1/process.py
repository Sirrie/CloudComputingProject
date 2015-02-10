import fileinput
# this file process the filtering of the records 
writeFile = open('processed-pagecounts-20140701.txt','w')

startCollection =("Media:","Special:","Talk:","User:","User_talk:","Project:","Project_talk:","File:",
"File_talk:","MediaWiki:","MediaWiki_talk:","Template:","Template_talk:","Help:","Help_talk:",
"Category:","Category_talk:","Portal:","Wikipedia:","Wikipedia_talk:")
endCollection = (".jpg",".gif",".png",".JPG",".GIF",".PNG",".txt",".ico")
titleCollection =("404_error/","Main_Page","Hypertext_Transfer_Protocol","Favicon.ico","Search")
dict={}
counter = 0
#for line in readFile.readlines():
for line in fileinput.input(['pagecounts-20140701-000000']):
    shouldFilterOut = False
    #fileter out not english ones    
   #filterout special pages
    fileInfo = line.split(" ")
    counter += int(fileInfo[2])
    #fileter out not english ones
    if not line.startswith("en "):
        shouldFilterOut = True
        continue    
    pageTitle = fileInfo[1]
    if pageTitle.startswith(startCollection):
        shouldFilterOut = True
        continue

    #filter out special title
    if pageTitle in titleCollection:
        shouldFilterOut = True
        continue

    #filter out all article that start with lowercase
    articleName = pageTitle
    if articleName[0].islower():
        shouldFilterOut = True
        continue
    
    #filter out all article that end wit some words
    if articleName.endswith(endCollection):
        shouldFilerOut = True
        continue

    if not shouldFilterOut:
       dict[fileInfo[1]]=int(fileInfo[2])
# sort records
for key in sorted(dict, key=dict.get):
    processedLine = key + "\t" + str( dict[key]) + "\n"
    writeFile.write(processedLine)
writeFile.write("final total click: "+str(counter))
print "the number of requests generated" + str(counter)
writeFile.close()

