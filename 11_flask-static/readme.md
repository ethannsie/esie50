## K11: Notes

**Flask**

Module to development server (opens in web browsers)

print() -> Console (Helpful and commonly used for debugging)
return -> WWW (Sends it to the HTML)

@app.route("/") -> Decorator, joined with the below function (when root is requested in the URL by a user, foo runs)
def foo()...

**Manging many python files**

if \__name__ == "\__main__":  
    app.debug = True        
    app.run()

- Only runs a python script if it is the "driver"
- Prevents the chaos of many python scripts running at once
- Allows the seperation of computation functions from webserver code
- Main file 'A', Imported files 'B', 'C', and 'D'


**Newline**

'/n' -> Works in plaintext contexts
<\br> -> Works in HTML contexts

**"foo" behavior**

We noticed that accessing http://localhost:5000/static/foo does not have any text on the webpage. We predicted that nothing would happen since there is no code for the program to read or run.

However, when the HTML file is run, "Is this plaintext, though?" is displayed on the local webpage. We predicted that the page would generate the text since the document type and html tags were properly included (and closed).