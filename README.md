# CLI RPN Calculator:
```c
  A Simple command-line reverse polish notation (RPN) calculator
```

### Setting up

We assume that you have `git` and `virtualenv` installed.

```bash
    # Clone the code repository
    git clone https://github.com/dcnoye/snapraise.git

    # Create & activate the virtual environment
    python3 -m venv venv3
    source venv3/bin/activate

    # Install required Python packages
    cd snapraise
    pip install -r requirements.txt

```
### Starting the CLI RPN calculator:

```bash
    python3 manage.py run-calc
```

### Running tests:

```bash
    python3 -mpytest tests  
```


Notes
-----

I hope you find this solution fairly straight forward.
I've incorporated my origin solution into a skeleton flask app.
If I were to spend more time on this, I'd create a docker-compose for development.
I'd also build out the api endpoints for rest & websocket connections.

