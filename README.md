# mock-fs
Simple proof-of-concept mock file system example written in python 3.

## Usage
> PENDING DOCUMENTATION

### Running Tests
To run all unit tests, enter the following command from the `mock-fs` project directory:
> python3 -m unittest

## Documentation Notes
Several assumptions needed to be made when designing the system. 
To avoid confusion several relevant decisions have been listed below:
- uses built-in `FileNotFoundError` for _Path not found_ exception
- uses built-in `FileExistsError` for _Path already exists_ exception

### Specifications
The complete specifications can be found on the wiki under [Assignment Specifications](https://github.com/lwthatcher/mock-fs/wiki/Assignment-Specifications)
