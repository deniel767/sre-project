from datetime import datetime as dt
# Creating an HTML file 
file = open("test.html","w") 
   
# Adding input data to the HTML file 
file.write("<html>")
file.write("<head>")
file.write("<title>My Webpage</title>")
file.write("</head>")
file.write("<body>")
file.write(f"<h1>Welcome to my webpage! This html file was 'compiled' at {dt.now()}</h1>")
file.write("</body>")
file.write("</html>")
              
# Saving the data into the HTML file 
file.close()