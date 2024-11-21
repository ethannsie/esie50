## K23: A RESTful Journey Skyward
### Due: `2024-11-21r` before class

Disco: 
- Reference dictionary value by key, like using 'explanation' to reference the corresponding content

QCC: 
- Given that the data we reference is a JSON object string, when would we make use of turning a python dictionary into a JSON object string during this assignment? I saw json.dumps() recommended below, but I'm not sure where it would have been used


_Step 0: Establish team comms. Fetch KtS._

### Your Duo MISSION: 

1. Read over a bit of primary documentation with your teammate:
   - python's urllib package. Specifically request, urlopen
   - python's json package, specifically loads and dumps 
1. Procure an API key from NASA Open APIs.
1. Verify that your key works by making a simple HTTP request using your new key.
   * Have dev console open while you do this...
   * Note anything notable.
   * Use QAF liberally.
3. __Write a Flask app__...
   * whose sole route
   * renders a template, which displays
   * your TNPG+roster, 
   * image(s) procured via API call,
   * and a bit of explanation of the image content.
     (You need only 2 files to accomplish this.)


--- 

#### Specifications/Guidelines:
* Use Q&A forum liberally.
* Comment liberally in-line. Speak to your future self and/or teammates.
* _Reminder:_ include heading as comment in all source files.
* Note anything notable in readme. (Include DISCO and QCC sections.)
* Display team name and roster on rendered page.
* Store your API key in a plaintext file as indicated, but __do not have git track it__. (Your key should be the sole content of the file.)
* You will need to import `urllib` and `json` python libraries.
* You will want to test drive and utilize these:
  - `requests.get()`
  - `requests.get().json()`
  - `requests.urlopen()`
  - `json.loads()`
  - `json.dumps()`

<br>

#### PROTIPS:
* _Simplicity is divine_.
* Diagnostic print statements are your friend.
  - Use them liberally.
  - When not in use, comment out rather than delete.
* __CONSOLE MAGICKS!__
  - Use flask console with diagnostic print statements to learn how to use urllib package.
  - Watch your browser's developer console as you work... (
* Comment liberally in-line. Speak to your future self and/or future teammates.

##### DELIVERABLES:
* Save to workshop as indicated.

```
path/to/myworkshop/23_rest$ tree
.
├── app.py
├── key_nasa.txt
├── readme
└── templates
    └── main.html
```

related:
<br>
[python3 urllib](https://docs.python.org/3/howto/urllib2.html)
<br>
[python3 json](https://docs.python.org/3/library/json.html)
<br>
[nasa](https://api.nasa.gov/)
<br>
[background](https://github.com/stuy-softdev/notes-and-code/blob/main/read/ibm_rest_api.pdf)
<br>
[background](https://en.wikipedia.org/wiki/REST)
<br>
[offground](https://xkcd.com/1133/)
